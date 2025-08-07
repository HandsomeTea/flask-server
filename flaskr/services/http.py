import os
import requests
import json
from flask import g
from urllib.parse import urlparse
from flaskr.configs import log_api
from flaskr.configs import HttpError


class __HTTPAdapter:

    @classmethod
    def __request_to_adela_server(self, method, url, body=None, query=None, headers=None):
        _headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-B3-TraceId': g.request_id or '',
            'X-B3-SpanId': g.span_id or '',
            'X-B3-Sampled': '1'
        }
        if headers and len(headers) > 0:
            _headers.update(headers)
        _body = {}
        if body and len(body) > 0:
            _body = body
        _query = {}
        if query and len(query) > 0:
            _query = query

        log_api.info('\n' + json.dumps({
            'query': _query,
            'body': _body,
            'headers': _headers,
        }, indent=4, ensure_ascii=False) + '\n', extra={
            'method': method.upper(),
            'api': url,
            'direction': '[>request<]',
            'trace_id': g.request_id,
            'span_id': g.span_id,
            'parent_span_id': g.parent_span_id,
            'useragent': 'python-requests: by adela-server',
            'error_code': '',
            'error_message': '',
            'error_stack': ''
        })
        result = None
        success = False
        try:
            response = requests.request(
                method=method,
                url=url,
                params=_query,
                json=_body,
                headers=_headers
            )
            if response.ok:
                result = response.json()
                success = True
            else:
                result = HttpError(response.content)
        except Exception as e:
            result = HttpError(e)
        finally:
            log_api.info('\n' + json.dumps(
                result if success else result.to_dict(),
                indent=4,
                ensure_ascii=False
                ) + '\n', extra={
                'method': method,
                'api': url,
                'direction': '[>response<]',
                'trace_id': g.request_id,
                'span_id': g.span_id,
                'parent_span_id': g.parent_span_id,
                'useragent': 'python-requests: by adela-server',
                'error_code': '',
                'error_message': '',
                'error_stack': ''
            })
            if success:
                return result
            else:
                raise result

    @classmethod
    def request_to_device_manager(self, method, url, body=None, query=None, headers=None):
        server_addr = urlparse(os.getenv('DEVICE_MANAGER_ADDR', 'http://0.0.0.0:8801'))
        return self.__request_to_adela_server(
            method=method,
            url=f'{server_addr.scheme}://{server_addr.netloc}/api/adelasvc/devicemgr{url}',
            query=query,
            body=body,
            headers=headers
        )


class HTTP(__HTTPAdapter):

    @classmethod
    def test_to_device_get(self, id, keyword, data):
        return self.request_to_device_manager(
            method='GET',
            url=f'/v1/test/{id}/{keyword}/tt',
            query=data
        )

    @classmethod
    def test_to_device_post(self, id, keyword, data):
        return self.request_to_device_manager(
            method='POST',
            url=f'/v1/test/{id}/{keyword}/tt',
            body=data
        )
