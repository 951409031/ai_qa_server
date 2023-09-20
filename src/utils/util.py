import json

def to_json(o):
    try:
        return json.loads(o)
    except Exception as e:
        return o