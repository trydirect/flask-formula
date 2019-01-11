from flask import abort
from app import db


class ModelMixin():
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])


def __set_attrs_to_item(item, attr_dict):
    for k, v in attr_dict.items():
        try:
            setattr(item, k, v)
        except AttributeError:
            abort(500, "can't set attribute - {}: {}".format(k, v))


# Standard CRUD functions
# Create
def add_item(model, data):
    __set_attrs_to_item(model, data)
    try:
        db.session.add(model)
        db.session.commit()
    except Exception as e:
        abort(500, e.args)

    return model


def save(model, data):
    __set_attrs_to_item(model, data)
    try:
        db.session.add(model)
        db.session.commit()
    except Exception as e:
        abort(500, e.args)

    return model


def get_or_create(model, **kwargs):
    instance = db.session.query(model).filter_by(id=kwargs['id']).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        return instance


def get_or_create_rel(model, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        return instance
