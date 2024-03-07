class ErrorCode:
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'
    __INTERNAL_SERVER_ERROR__ = 500

    NOT_FOUND = 'NOT_FOUND'
    __NOT_FOUND__ = 404

    URL_NOT_FOUND = 'URL_NOT_FOUND'
    __URL_NOT_FOUND__ = 404

    USER_NOT_FOUND = 'USER_NOT_FOUND'
    __USER_NOT_FOUND__ = 404

    UNAUTHORIZED = 'UNAUTHORIZED'
    __UNAUTHORIZED__ = 401

    INVALID_ARGUMENTS = 'INVALID_ARGUMENTS'
    __INVALID_ARGUMENTS__ = 400

    @classmethod
    def get_error_number(self, error_code) -> int:
        return getattr(self, '__' + error_code + '__', 500)
