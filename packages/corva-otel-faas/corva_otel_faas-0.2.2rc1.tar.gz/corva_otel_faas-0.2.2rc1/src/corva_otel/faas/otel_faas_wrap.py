# Copyright 2020, OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The opentelemetry-instrumentation-aws-lambda package provides an Instrumentor
to traces calls within a Python AWS Lambda function.

Usage
-----

.. code:: python

    # Copy this snippet into an AWS Lambda function
    from corva.otel.faas import otel_faas

    # Lambda function
    @otel_faas()
    def lambda_handler(event, context):
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket.name)

        return "200 OK"

API
---

The `otel_faas` method accepts the following keyword args:

event_context_extractor (Callable) - a function that returns an OTel Trace
tracer_provider (TracerProvider) - an optional tracer provider
meter_provider (MeterProvider) - an optional meter provider
Context given the Lambda Event the AWS Lambda was invoked with
this function signature is: def event_context_extractor(lambda_event: Any) -> Context
for example:

.. code:: python

    from opentelemetry.instrumentation.aws_lambda import AwsLambdaInstrumentor

    def custom_event_context_extractor(lambda_event):
        # If the `TraceContextTextMapPropagator` is the global propagator, we
        # can use it to parse out the context from the HTTP Headers.
        return get_global_textmap().extract(lambda_event["foo"]["headers"])

    AwsLambdaInstrumentor().instrument(
        event_context_extractor=custom_event_context_extractor
    )

---
"""
import importlib.metadata
import logging
import os
import time
from typing import Any, Callable, Optional
from urllib.parse import urlencode

from opentelemetry.context import get_current as get_current_context
from opentelemetry.context.context import Context
from opentelemetry.metrics import MeterProvider, get_meter_provider
from opentelemetry.propagate import get_global_textmap
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.semconv.trace import SpanAttributes
from opentelemetry.trace import (
    Span,
    SpanKind,
    TracerProvider,
    get_tracer,
    get_tracer_provider,
)
from opentelemetry.trace.propagation import get_current_span
from opentelemetry.trace.status import Status, StatusCode
from wrapt import decorator

from corva_otel.semconv import corva_semattrs

try:
    version = importlib.metadata.version("corva_otel.faas")
except Exception:
    version = "unknown"


def _getattr(obj: Any, attr_name: str) -> Any:
    obj = obj[0] if isinstance(obj, list) else obj
    return (
        getattr(obj, attr_name) if hasattr(obj, attr_name) else obj[attr_name]
    )


def _extract_attribute(
    obj: Any, attr_name: str, default: Any = None
) -> Optional[str]:
    try:
        return _getattr(obj, attr_name)
    except Exception:
        pass

    try:
        inner_obj = _getattr(obj, "metadata")
        return _getattr(inner_obj, attr_name)
    except Exception:
        pass

    try:
        inner_obj = _getattr(obj, "records")
        return _getattr(inner_obj, attr_name)
    except Exception:
        pass

    try:
        inner_obj = _getattr(obj, "data")
        return _getattr(inner_obj, attr_name)
    except Exception:
        pass

    app_key = os.getenv("APP_KEY")
    if app_key is not None:
        try:
            inner_obj = _getattr(obj, "metadata")
            inner_obj = _getattr(inner_obj, "apps")
            inner_obj = _getattr(inner_obj, app_key)
            return _getattr(inner_obj, attr_name)
        except Exception:
            pass

    return default


def extract_corva_attributes(event: Any):
    if isinstance(event, (list, tuple)) and len(event) > 0:
        event = event[0]

    company_value = _extract_attribute(event, "company")
    app_stream_id = _extract_attribute(event, "app_stream_id")

    corva_attrs = {
        corva_semattrs.CORVA_TASK_ID:
            _extract_attribute(event, "id")
            or _extract_attribute(event, "task_id"),
        corva_semattrs.CORVA_ASSET_ID:
            _extract_attribute(event, "asset_id"),
        corva_semattrs.CORVA_ASSET_TYPE:
            _extract_attribute(event, "asset_type"),
        corva_semattrs.CORVA_ASSET_NAME:
            _extract_attribute(event, "asset_name"),
        corva_semattrs.CORVA_COMPANY_NAME:
            None if isinstance(company_value, int) else company_value,
        corva_semattrs.CORVA_COMPANY_ID:
            company_value if isinstance(company_value, int)
            else _extract_attribute(event, "company_id"),
        corva_semattrs.CORVA_APP_PROVIDER:
            _extract_attribute(event, "provider"),
        corva_semattrs.CORVA_APP_ID:
            None if app_stream_id
            else _extract_attribute(event, "app"),
        corva_semattrs.CORVA_APP_KEY:
            _extract_attribute(event, "app_key"),
        corva_semattrs.CORVA_APP_CONNECTION_ID: (
            _extract_attribute(event, "app_connection_id")
            or _extract_attribute(event, "app_connection")),
        corva_semattrs.CORVA_APP_STREAM_ID: (
            _extract_attribute(event, "app_stream_id")
            or _extract_attribute(event, "app_stream")),
        corva_semattrs.CORVA_SEGMENT: _extract_attribute(event, "source_type"),
        # TODO: Introduce proper semattr for that
        "corva.log_type": _extract_attribute(event, "log_type"),
    }
    # Filter out None values
    return {k: v for k, v in corva_attrs.items() if v is not None}


logger = logging.getLogger(__name__)

_HANDLER = "_HANDLER"
_X_AMZN_TRACE_ID = "_X_AMZN_TRACE_ID"
ORIG_HANDLER = "ORIG_HANDLER"
OTEL_INSTRUMENTATION_AWS_LAMBDA_FLUSH_TIMEOUT = (
    "OTEL_INSTRUMENTATION_AWS_LAMBDA_FLUSH_TIMEOUT"
)
OTEL_LAMBDA_DISABLE_AWS_CONTEXT_PROPAGATION = (
    "OTEL_LAMBDA_DISABLE_AWS_CONTEXT_PROPAGATION"
)


def _default_event_context_extractor(lambda_event: Any, lambda_context: Any) -> Optional[Context]:
    """Default way of extracting the context from the Lambda or OpenFaaS Event and Context.

    See more:
    https://github.com/corva-ai/monorepo-node/pull/1207
    https://github.com/corva-ai/kafka-consumer-java/pull/94
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    Args:
        lambda_event: user-defined, so it could be anything, but this
            method counts on it being a map with a 'headers' key
        lambda_context: user-defined, so it could be anything, but this
            method counts on it being a map with a 'custom' or 'Custom' key
    Returns:
        A Context with configuration found in the lambda event or lambda context
    """
    context = Context()
    global_textmap = get_global_textmap()
    client_context = getattr(lambda_context, "client_context", {})
    first_event = lambda_event[0] if isinstance(lambda_event, list) and len(lambda_event) else (lambda_event or {})

    def try_extract(carrier: Any) -> Optional[Context]:
        """Returns the OpenTelemetry context if extracted, otherwise None."""
        otel_ctx = global_textmap.extract(carrier) if carrier else None
        return otel_ctx if otel_ctx is not context else None

    return (
        try_extract(getattr(client_context, "custom", None)) or
        # TODO: validate NodeJS invoking Python would work, given `Custom` is not transferred
        try_extract(getattr(client_context, "Custom", None)) or
        try_extract(first_event.get("headers", None)) or
        try_extract(first_event) or
        try_extract(first_event.get("otel_ctx", None))
    )


def _determine_parent_context(
    lambda_event: Any, lambda_context: Any, event_context_extractor: Callable[[Any], Context]
) -> Context:
    """Determine the parent context for the current Lambda invocation.

    See more:
    https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/instrumentation/aws-lambda.md#determining-the-parent-of-a-span

    Args:
        lambda_event: user-defined, so it could be anything, but this
            method counts it being a map with a 'headers' key
        event_context_extractor: a method which takes the Lambda
            Lambda Event and Lambda Context as input and extracts an OTel Context from it. By default,
            the context is extracted from the HTTP headers of an API Gateway
            request.
    Returns:
        A Context with configuration found in the carrier.
    """
    parent_context = get_current_context()

    if (
        parent_context
        and get_current_span(parent_context)
        .get_span_context()
        .trace_flags.sampled
    ):
        return parent_context

    if not event_context_extractor:
        event_context_extractor = _default_event_context_extractor

    parent_context = event_context_extractor(lambda_event, lambda_context) or parent_context

    return parent_context


def _set_api_gateway_v1_proxy_attributes(
    lambda_event: Any, span: Span
) -> Span:
    """Sets HTTP attributes for REST APIs and v1 HTTP APIs

    More info:
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    """
    span.set_attribute(
        SpanAttributes.HTTP_METHOD, lambda_event.get("httpMethod")
    )

    if lambda_event.get("headers"):
        if "User-Agent" in lambda_event["headers"]:
            span.set_attribute(
                SpanAttributes.HTTP_USER_AGENT,
                lambda_event["headers"]["User-Agent"],
            )
        if "X-Forwarded-Proto" in lambda_event["headers"]:
            span.set_attribute(
                SpanAttributes.HTTP_SCHEME,
                lambda_event["headers"]["X-Forwarded-Proto"],
            )
        if "Host" in lambda_event["headers"]:
            span.set_attribute(
                SpanAttributes.NET_HOST_NAME,
                lambda_event["headers"]["Host"],
            )
    if "resource" in lambda_event:
        span.set_attribute(SpanAttributes.HTTP_ROUTE, lambda_event["resource"])

        if lambda_event.get("queryStringParameters"):
            span.set_attribute(
                SpanAttributes.HTTP_TARGET,
                f"{lambda_event['resource']}?{urlencode(lambda_event['queryStringParameters'])}",
            )
        else:
            span.set_attribute(
                SpanAttributes.HTTP_TARGET, lambda_event["resource"]
            )

    return span


def _set_api_gateway_v2_proxy_attributes(
    lambda_event: Any, span: Span
) -> Span:
    """Sets HTTP attributes for v2 HTTP APIs

    More info:
    https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
    """
    if "domainName" in lambda_event["requestContext"]:
        span.set_attribute(
            SpanAttributes.NET_HOST_NAME,
            lambda_event["requestContext"]["domainName"],
        )

    if lambda_event["requestContext"].get("http"):
        if "method" in lambda_event["requestContext"]["http"]:
            span.set_attribute(
                SpanAttributes.HTTP_METHOD,
                lambda_event["requestContext"]["http"]["method"],
            )
        if "userAgent" in lambda_event["requestContext"]["http"]:
            span.set_attribute(
                SpanAttributes.HTTP_USER_AGENT,
                lambda_event["requestContext"]["http"]["userAgent"],
            )
        if "path" in lambda_event["requestContext"]["http"]:
            span.set_attribute(
                SpanAttributes.HTTP_ROUTE,
                lambda_event["requestContext"]["http"]["path"],
            )
            if lambda_event.get("rawQueryString"):
                span.set_attribute(
                    SpanAttributes.HTTP_TARGET,
                    f"{lambda_event['requestContext']['http']['path']}?{lambda_event['rawQueryString']}",
                )
            else:
                span.set_attribute(
                    SpanAttributes.HTTP_TARGET,
                    lambda_event["requestContext"]["http"]["path"],
                )

    return span


def get_span_type(event) -> SpanKind:
    try:
        if event["Records"][0]["eventSource"] in {
            "aws:sqs",
            "aws:s3",
            "aws:sns",
            "aws:dynamodb",
        }:
            # See more:
            # https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
            # https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html
            # https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
            # https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html
            return SpanKind.CONSUMER
    except (IndexError, KeyError, TypeError):
        # We default to SpanKind.SERVER if we cannot determine span kind from event
        pass

    return SpanKind.SERVER


def get_account_id(arn: Optional[str]) -> str:
    if arn is None:
        return ""

    parts = arn.split(":")

    if len(parts) < 5:
        return ""

    return parts[4]


def otel_faas(
    span_name: str = None,
    event_context_extractor: Callable[[Any], Context] = None,
    tracer_provider: TracerProvider = None,
    meter_provider: MeterProvider = None,
):
    timeout_value = os.getenv("OTEL_FLUSH_TIMEOUT", "3000")
    flush_timeout = int(timeout_value) if timeout_value.isdigit() else 3000

    @decorator
    def wrapper(wrapped, instance, args, kwargs):
        if os.environ.get("OTEL_SDK_DISABLED") == "true":
            return wrapped(*args, **kwargs)

        nonlocal span_name
        if span_name is None:
            span_name = f"{wrapped.__module__}.{wrapped.__name__}"

        lambda_event = {}
        if len(args) > 0:
            lambda_event = args[0]

        corva_attrs = extract_corva_attributes(lambda_event)

        lambda_context = {}
        if len(args) > 1:
            lambda_context = args[1]

        parent_context = _determine_parent_context(
            lambda_event, lambda_context, event_context_extractor
        )

        span_kind = get_span_type(lambda_event)

        tracer = get_tracer(
            __name__,
            version,
            tracer_provider,
            schema_url="https://opentelemetry.io/schemas/1.11.0",
        )

        with tracer.start_as_current_span(
            name=span_name,
            context=parent_context,
            kind=span_kind,
        ) as span:
            if span.is_recording():
                span.set_attribute(
                    SpanAttributes.FAAS_EXECUTION,
                    getattr(lambda_context, "aws_request_id", ""),
                )

                span.set_attribute(
                    ResourceAttributes.FAAS_ID,
                    getattr(lambda_context, "invoked_function_arn", ""),
                )

                span.set_attribute(
                    ResourceAttributes.CLOUD_ACCOUNT_ID,
                    get_account_id(
                        getattr(lambda_context, "invoked_function_arn", "")
                    ),
                )

                if corva_attrs:
                    span.set_attributes(corva_attrs)

            exception = None
            try:
                result = wrapped(*args, **kwargs)
            except Exception as exc:  # pylint: disable=W0703
                exception = exc
                span.set_status(Status(StatusCode.ERROR))
                span.record_exception(exception)

            # If the request came from an API Gateway, extract http attributes from the event
            # https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/instrumentation/aws-lambda.md#api-gateway
            # https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/semantic_conventions/http.md#http-server-semantic-conventions
            if isinstance(lambda_event, dict) and lambda_event.get(
                "requestContext"
            ):
                span.set_attribute(SpanAttributes.FAAS_TRIGGER, "http")

                if lambda_event.get("version") == "2.0":
                    _set_api_gateway_v2_proxy_attributes(lambda_event, span)
                else:
                    _set_api_gateway_v1_proxy_attributes(lambda_event, span)

                if isinstance(result, dict) and result.get("statusCode"):
                    span.set_attribute(
                        SpanAttributes.HTTP_STATUS_CODE,
                        result.get("statusCode"),
                    )

        now = time.time()
        _tracer_provider = tracer_provider or get_tracer_provider()
        if hasattr(_tracer_provider, "force_flush"):
            try:
                # NOTE: `force_flush` before function quit in case of Lambda freeze.
                _tracer_provider.force_flush(flush_timeout)
            except Exception:  # pylint: disable=broad-except
                logger.exception("TracerProvider failed to flush traces")
        else:
            logger.warning(
                "TracerProvider was missing `force_flush` method. This is necessary in case of a Lambda freeze and would exist in the OTel SDK implementation."
            )

        _meter_provider = meter_provider or get_meter_provider()
        if hasattr(_meter_provider, "force_flush"):
            rem = flush_timeout - (time.time() - now) * 1000
            if rem > 0:
                try:
                    # NOTE: `force_flush` before function quit in case of Lambda freeze.
                    _meter_provider.force_flush(rem)
                except Exception:  # pylint: disable=broad-except
                    logger.exception("MeterProvider failed to flush metrics")
        else:
            logger.warning(
                "MeterProvider was missing `force_flush` method. This is necessary in case of a Lambda freeze and would exist in the OTel SDK implementation."
            )

        if exception is not None:
            raise exception.with_traceback(exception.__traceback__)

        return result

    return wrapper
