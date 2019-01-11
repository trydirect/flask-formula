from flask import request, current_app


class SessionException(Exception):
    pass


class session(object):

    @classmethod
    def __key_prefix(cls):
        if request.user_id:
            return request.user_id
        raise SessionException('user_id is not defined')

    @classmethod
    def set(cls, key, value):
        current_app.extensions['redis'].set(name='%s:%s' % (cls.__key_prefix(), key),
                                            value=value,
                                            ex=int(current_app.config['REDIS_SESSION_LIFETIME'].total_seconds()))
        return True

    @classmethod
    def get(cls, key, default=None):
        value = current_app.extensions['redis'].get(name='%s:%s' % (cls.__key_prefix(), key))
        if value:
            return value
        return default

    @classmethod
    def delete(cls, name):
        current_app.extensions['redis'].delete('%s:%s' % (cls.__key_prefix(), name))
        return True

    @classmethod
    def hmset(cls, key, mapping):
        current_app.extensions['redis'].hmset(name='%s:%s' % (cls.__key_prefix(), key),
                                              mapping=mapping)
        current_app.extensions['redis'].expire(name='%s:%s' % (cls.__key_prefix(), key),
                                               time=int(current_app.config['REDIS_SESSION_LIFETIME'].total_seconds()))
        return True

    @classmethod
    def hgetall(cls, key, default={}):
        value = current_app.extensions['redis'].hgetall(name='%s:%s' % (cls.__key_prefix(), key))
        if value:
            return value
        return default

    @classmethod
    def hdel(cls, name, *keys):
        current_app.extensions['redis'].hdel('%s:%s' % (cls.__key_prefix(), name), *keys)
        return True