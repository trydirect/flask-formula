from werkzeug.exceptions import NotAcceptable, InternalServerError
from flask import request
from flask import make_response as original_flask_make_response
from flask_restful import Api as DefaulApi
from flask import current_app


class Api(DefaulApi):

    def make_response(self, data, *args, **kwargs):
        """Looks up the representation transformer for the requested media
        type, invoking the transformer to create a response object. This
        defaults to default_mediatype if no transformer is found for the
        requested mediatype. If default_mediatype is None, a 406 Not
        Acceptable response will be sent as per RFC 2616 section 14.1

        :param data: Python object containing response data to be transformed
        """
        default_mediatype = kwargs.pop('fallback_mediatype', None) or self.default_mediatype
        mediatype = request.accept_mimetypes.best_match(
            self.representations,
            default=default_mediatype,
        )
        if mediatype is None:
            raise NotAcceptable()
        if mediatype in self.representations:
            resp = self.representations[mediatype](data, *args, **kwargs)
            resp.headers['Access-Control-Allow-Origin'] = current_app.config['ACCESS_CONTROL_ALLOW_ORIGIN_HEADER']
            resp.headers['Access-Control-Allow-Headers'] = current_app.config['ACCESS_CONTROL_ALLOW_HEADERS']
            resp.headers['Access-Control-Allow-Methods'] = current_app.config['ACCESS_CONTROL_ALLOW_METHODS']
            resp.headers['Content-Type'] = mediatype
            return resp
        elif mediatype == 'text/plain':
            resp = original_flask_make_response(str(data), *args, **kwargs)
            resp.headers['Access-Control-Allow-Origin'] = current_app.config['ACCESS_CONTROL_ALLOW_ORIGIN_HEADER']
            resp.headers['Access-Control-Allow-Headers'] = current_app.config['ACCESS_CONTROL_ALLOW_HEADERS']
            resp.headers['Access-Control-Allow-Methods'] = current_app.config['ACCESS_CONTROL_ALLOW_METHODS']
            resp.headers['Content-Type'] = 'text/plain'
            return resp
        else:
            raise InternalServerError()
