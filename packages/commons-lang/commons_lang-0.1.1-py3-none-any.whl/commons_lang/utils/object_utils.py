def get(obj: object | dict, attr_name: str, default=None):
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(attr_name, default)
    else:
        return getattr(obj, attr_name, default)
