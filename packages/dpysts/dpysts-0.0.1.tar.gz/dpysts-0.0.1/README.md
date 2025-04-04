# step 1: init

Invoke init method: `sts_init(server: str, model: str)`

# step 2: get STS token

Invoke token method: `sts_token(schema: str, field: str)`

The response is in JSON, and may look like below:

```
{'Credentials': {'Token': 'tHZAaB******-***-***-***-***', 'TmpSecretId': 'AKID******PABfndE', 'TmpSecretKey': 'T2GX******lylh8='}, 'ExpiredTime': 1738912303, 'Expiration': '2025-02-07T07:11:43Z', 'RequestId': 'bb***83-3**7-4**a-9**4-a3***0d'}
```

