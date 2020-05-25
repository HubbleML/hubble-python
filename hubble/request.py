from datetime import date, datetime
import logging
import json
from gzip import GzipFile
from requests import sessions, Request
from io import BytesIO

from hubble.version import VERSION
from hubble.utils import remove_trailing_slash

_session = sessions.Session()


def post(write_key, host=None, gzip=False, timeout=15, **kwargs):
    """Post the `kwargs` to the API"""
    log = logging.getLogger('hubble')
    body = kwargs
    url = remove_trailing_slash(host or 'https://9o393i2p27.execute-api.eu-west-1.amazonaws.com/dev') + '/batch'
    data = json.dumps(body)
    log.debug('making request: %s', data)
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'hubble-client-python/' + VERSION,
        'x-api-key': write_key,
    }
    if gzip:
        headers['Content-Encoding'] = 'gzip'
        buf = BytesIO()
        with GzipFile(fileobj=buf, mode='w') as gz:
            # 'data' was produced by json.dumps(),
            # whose default encoding is utf-8.
            gz.write(data.encode('utf-8'))
        data = buf.getvalue()

    req = Request('POST', url, data=data, headers=headers)
    prepped_req = _session.prepare_request(req)
    log.debug(
        'Posting request: method: %s, url: %s, headers: %s, body: %s',
        prepped_req.method,
        prepped_req.url,
        prepped_req.headers,
        prepped_req.body
    )
    res = _session.send(prepped_req, timeout=timeout)

    if res.status_code == 200:
        log.debug('data uploaded successfully')
        return res

    try:
        payload = res.json()
        log.debug('received response: %s', payload)
        raise APIError(res.status_code, payload['code'], payload['message'])
    except (ValueError, KeyError):
        raise APIError(res.status_code, 'unknown', res.text)


class APIError(Exception):

    def __init__(self, status, code, message):
        self.message = message
        self.status = status
        self.code = code

    def __str__(self):
        msg = "[Hubble-python-client] {0}: {1} ({2})"
        return msg.format(self.code, self.message, self.status)


class DatetimeSerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)