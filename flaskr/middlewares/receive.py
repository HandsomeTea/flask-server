import json
from flaskr.app import application as app
from flask import request
from flaskr.configs import log_api
from flaskr.utils import random_string


@app.before_request
def set_log_trace_header():
    request.headers.environ['HTTP_X_B3_TRACEID'] = request.headers.get('X-B3-TraceId') or random_string()
    request.headers.environ['HTTP_X_B3_PARENTSPANID'] = request.headers.get('X-B3-SpanId') or ''
    request.headers.environ['HTTP_X_B3_SPANID'] = random_string()


@app.before_request
def log_request():
    _body = request.get_data()

    if 'application/json' in request.headers.get('Content-Type', ''):
        _body = json.loads(_body)

    if (len(_body) == 0):
        _body = {}

    try:
        log_api.info(f'{request.method}:{request.path}\n' + json.dumps({
            'query': request.args.to_dict(),
            'body': _body,
            'headers': dict(request.headers),
        }, indent=4, ensure_ascii=False), extra={
            'trace_id': request.headers.get('X-B3-TraceId'),
            'span_id': request.headers.get('X-B3-SpanId'),
            'parent_span_id': request.headers.get('X-B3-ParentSpanId')
        })
    except Exception:
        log_api.info(f'{request.method}:{request.path}\n' + {
            'query': request.args.to_dict(),
            'body': _body,
            'headers': dict(request.headers),
        }, extra={
            'trace_id': request.headers.get('X-B3-TraceId'),
            'span_id': request.headers.get('X-B3-SpanId'),
            'parent_span_id': request.headers.get('X-B3-ParentSpanId')
        })
