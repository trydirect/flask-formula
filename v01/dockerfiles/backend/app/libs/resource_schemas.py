from flask_restful import fields as fl
from datetime import datetime


class DateTimeFromTimestampField(fl.Raw):

    def format(self, value):
        if not value:
            return ''
        try:
            v = datetime.fromtimestamp(float(value))
            return str(v)
        except:
            return ''


class Str2DecimalField(fl.Raw):

    def format(self, value):
        return '{0:.2f}'.format(float(str(value or '0').strip('+')))