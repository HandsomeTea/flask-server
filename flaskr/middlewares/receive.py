import json
from opentelemetry import trace
from flaskr import app_name
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

    log_message = ''

    try:
        log_message = f'{request.method}:{request.path}\n' + json.dumps({
            'query': request.args.to_dict(),
            'body': _body,
            'headers': dict(request.headers),
        }, indent=4, ensure_ascii=False)
    except Exception:
        log_message = f'{request.method}:{request.path}\n' + {
            'query': request.args.to_dict(),
            'body': _body,
            'headers': dict(request.headers),
        }

    current_span = trace.get_current_span()
    current_span.update_name(f'{app_name}.tracer')
    current_span_context = current_span.get_span_context()

    current_span.add_event('http-request', {
        'log': log_message
    })
    log_api.info(log_message, extra={
        # 'trace_id': request.headers.get('X-B3-TraceId'),
        # 'span_id': request.headers.get('X-B3-SpanId'),
        # 'parent_span_id': request.headers.get('X-B3-ParentSpanId')
        'trace_id': current_span_context.trace_id,
        'span_id': current_span_context.span_id,
        'parent_span_id': ''
    })
