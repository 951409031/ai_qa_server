from utils.util import to_json
from django.http import JsonResponse


class Response(JsonResponse):

    def __init__(self, code=0, msg="成功", **data):
        self.data = data
        self.code = code
        self.msg = msg
        super().__init__(self.__dict__)



class Request:
    def __init__(self, params, **kwargs):
        self.__dict__.update(params)
        self.__dict__.update(kwargs)
        for k, v in self.__dict__.items():
            v = to_json(v)
            self.__dict__.update({k: v})

    def __getattr__(self, item, default=None):
        return self.__dict__.get(item, default)

    def __delattr__(self, item, default=None):
        self.__dict__.setdefault(item, None)
        return self.__dict__.pop(item)

    def __str__(self):
        return self.__dict__.__str__()

    def to_dict(self):
        return self.__dict__

    def get(self, item, default=None):
        return self.__getattr__(item, default)

    def pop(self, item, default=None):
        return self.__delattr__(item, default)
