import inspect
from pprint import pprint

info = {}


def introspection_info(obj):
    info['Тип объекта'] = type(obj)
    info['Атрибуты объекта'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['Методы объекта'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    info['Модуль'] = inspect.getmodule(obj)
    info['Строковое представление'] = str(obj)
    return info


number_info = introspection_info(42)
pprint(number_info)
