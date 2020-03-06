class TestClientRequestsMixin(object):

    def post(self, url, data=None, json=None, access_token=None):
        kwargs = {'data': data, 'json': json, 'url': url}
        if access_token:
            kwargs['headers'] = {'Authorization': f'Bearer {access_token}'}
        return self.client.post(**kwargs)

    def get(self, url, params=None, access_token=None):
        kwargs = {'params': params, 'url': url}
        if access_token:
            kwargs['headers'] = {'Authorization': f'Bearer {access_token}'}
        return self.client.get(**kwargs)
