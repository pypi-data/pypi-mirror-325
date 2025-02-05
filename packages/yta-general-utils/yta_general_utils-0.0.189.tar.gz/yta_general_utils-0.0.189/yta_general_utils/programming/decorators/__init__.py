# Based on this: https://stackoverflow.com/a/5191224
class ClassPropertyDescriptor(object):
    def __init__(self, fget, fset = None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, cls = None):
        if cls is None:
            cls = type(obj)
        return self.fget.__get__(obj, cls)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self

def classproperty(func):
    """
    Decorator to implement a class property.
    """
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)