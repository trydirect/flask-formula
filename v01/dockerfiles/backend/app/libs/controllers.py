from zlib import adler32
from functools import wraps
from flask_restful import Resource as DefaultResurce, ResponseBase, OrderedDict, request, unpack, marshal


VALIDATION_ERROR_MESSAGE = 'Fields validation error'


class marshal_with(object):
    """A decorator that apply marshalling to the return values of your methods.

    >>> from flask_restful import fields, marshal_with
    >>> mfields = { 'a': fields.Raw }
    >>> @marshal_with(mfields)
    ... def get():
    ...     return { 'a': 100, 'b': 'foo' }
    ...
    ...
    >>> get()
    OrderedDict([('a', 100)])

    >>> @marshal_with(mfields, envelope='data')
    ... def get():
    ...     return { 'a': 100, 'b': 'foo' }
    ...
    ...
    >>> get()
    OrderedDict([('data', OrderedDict([('a', 100)]))])

    see :meth:`flask_restful.marshal`
    """
    def __init__(self, fields, envelope=None):
        """
        :param fields: a dict of whose keys will make up the final
                       serialized response output
        :param envelope: optional key that will be used to envelop the serialized
                         response
        """
        self.fields = fields
        self.envelope = envelope

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                if code != 200 or data.get('success') is False:
                    return resp
                return marshal(data, self.fields, self.envelope), code, headers
            else:
                return marshal(resp, self.fields, self.envelope)
        return wrapper


class Resource(DefaultResurce):

    def __serialize_errors(self, resp):
        """reformat the error structure and add the error codes"""
        if not resp.get('errors'):
            return resp
        elif resp['errors'].get('global_error'):
            ge_message = resp['errors'].pop('global_error')
            resp['errors']['global_error'] = {
                'code': adler32(ge_message.encode('UTF-16')),
                'message': ge_message
            }
            return resp
        else:
            # compose field errors
            field_errors = {}
            for field in resp['errors']:
                field_errors[field] = {
                    'code': adler32(resp['errors'][field].encode('UTF-16')),
                    'message': resp['errors'][field]
                }
            resp['errors'] = {
                'fields': field_errors
            }
            # compose global_error
            if resp['errors'].get('global_error'):
                ge_message = resp['errors']['global_error']
                resp['errors']['global_error'] = {
                    'code': adler32(ge_message.encode('UTF-16')),
                    'message': ge_message
                }
            else:
                resp['errors']['global_error'] = {
                    'code': adler32(VALIDATION_ERROR_MESSAGE.encode('UTF-16')),
                    'message': VALIDATION_ERROR_MESSAGE
                }
            return resp

    def dispatch_request(self, *args, **kwargs):

        # Taken from flask
        #noinspection PyUnresolvedReferences
        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        for decorator in self.method_decorators:
            meth = decorator(meth)

        resp = meth(*args, **kwargs)

        # adds default success key
        if isinstance(resp, dict):
            if resp.get('success', None) is None:
                resp['success'] = True
            elif resp.get('success', True) is False:
                resp = self.__serialize_errors(resp)
        elif isinstance(resp, tuple):
            if resp[0].get('success', True) is False:
                list(resp)[0] = self.__serialize_errors(resp[0])
                resp = tuple(resp)

        if isinstance(resp, ResponseBase):  # There may be a better way to test
            return resp

        representations = self.representations or OrderedDict()

        #noinspection PyUnresolvedReferences
        mediatype = request.accept_mimetypes.best_match(representations, default=None)
        if mediatype in representations:
            data, code, headers = unpack(resp)
            resp = representations[mediatype](data, code, headers)
            resp.headers['Content-Type'] = mediatype
            return resp

        return resp

