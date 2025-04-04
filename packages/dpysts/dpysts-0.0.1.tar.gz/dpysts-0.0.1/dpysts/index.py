import json
import datetime

import threading
import requests

STS_SERVER = None
STS_MODEL = None

STS_CACHE = {}
STS_LOCK = threading.Lock()

STS_ACTION_GET_TOKEN = 'token'

def sts_init(server: str, model: str):
    global STS_SERVER, STS_MODEL

    if STS_SERVER is not None:
        raise 'sts_init can be invoked once only!'

    STS_SERVER = server
    STS_MODEL = model

def sts_token(schema: str, field: str):
    global STS_MODEL

    if STS_MODEL is None:
        raise 'sts_init must be invoked first!'

    key = f'{STS_MODEL}.{schema}.{field}'
    if key in STS_CACHE:
        payload = STS_CACHE[key]
        if not _is_expired(payload['Expiration']):
            return STS_CACHE[key]

    with STS_LOCK:
        print('# DEBUG with thread locking')
        return _sts_token_impl(key)

def _from_iso_format(ts: str):
    ts_noz = ts.replace('Z', '')
    dt = datetime.datetime.strptime(ts_noz, '%Y-%m-%dT%H:%M:%S')
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt

def _is_expired(ts: str):
    dt = _from_iso_format(ts)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    diff = dt - now
    # be valid only if over 1 hour
    return round(diff.total_seconds() / 60, 2) < 60
    
def _sts_token_impl(key: str):
    global STS_CACHE, STS_SERVER, STS_ACTION_GET_TOKEN

    response = requests.get(f'{STS_SERVER}/{STS_ACTION_GET_TOKEN}', params={'key': key})
    if not response.ok:
        response.raise_for_status()

    payload = json.loads(response.json()['data'])['Response']

    STS_CACHE[key] = payload
    return STS_CACHE[key]


if __name__ == '__main__':
    sts_init('https://sts-infra.meiyunji.net', 'infra')
    print(sts_token('checkaccesskey', 'myj1'))
    print(sts_token('checkaccesskey', 'myj1'))
