import json
from flaskr.app import application as app
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

    log_api.info(
        f'{request.method}:{request.path} => \n' + (json_result or result),
        extra={
            'trace_id': request.headers.get('X-B3-TraceId'),
            'span_id': request.headers.get('X-B3-SpanId'),
            'parent_span_id': request.headers.get('X-B3-ParentSpanId')
        }
    )

    return response
