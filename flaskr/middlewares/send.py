import json
from flaskr.app import application as app
from opentelemetry import trace
from flask import request
from flaskr.configs import log_api


@app.after_request
def log_response(response):
    result = response.get_data().decode('utf-8')
    json_result = None

    if 'application/json' in response.headers['Content-Type']:
        json_result = json.dumps(
            json.loads(result),
            indent=4,
            ensure_ascii=False
        )

    log_message = f'{request.method}:{request.path} => \n' + (json_result or result)

    current_span = trace.get_current_span()
    current_span_context = current_span.get_span_context()

    current_span.add_event('http-response', {
        'log': log_message
    })

    if (response.status_code > 299):
        current_span.set_status(trace.StatusCode.ERROR)

    log_api.info(
        log_message,
        extra={
            # 'trace_id': request.headers.get('X-B3-TraceId'),
            # 'span_id': request.headers.get('X-B3-SpanId'),
            # 'parent_span_id': request.headers.get('X-B3-ParentSpanId')
            'trace_id': current_span_context.trace_id,
            'span_id': current_span_context.span_id,
            'parent_span_id': ''
        }
    )

    return response
