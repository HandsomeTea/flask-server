from opentelemetry import trace
import traceback
from flaskr.app import application as app
from werkzeug.exceptions import HTTPException
from flaskr.configs import log, HttpError


@app.errorhandler(Exception)
def error_catch(error):
    result = HttpError('Internal Server Error: ' + str(error)).to_dict()

    if isinstance(error, HTTPException):
        result = HttpError(error.description).to_dict()
    elif isinstance(error, HttpError):
        result = error.to_dict()

    current_span = trace.get_current_span()

    current_span.add_event('http-error', {
        'stack':  traceback.format_exc()
    })
    log.error(traceback.format_exc())

    return result, result.get('status')
