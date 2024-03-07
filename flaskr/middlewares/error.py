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

    log.error(traceback.format_exc())

    return result, result.get('status')
