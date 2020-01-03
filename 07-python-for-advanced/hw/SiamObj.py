import weakref


class MyMeta(type):

    def __new__(cls, clsname, bases, dct):
        cls.instances = {}
        cls.instances = weakref.WeakKeyDictionary(cls.instances)
        return super(MyMeta, cls).__new__(cls, clsname, bases, dct)

    def __init__(cls, name, bases, dct):
        def __init__cls(self, *args, **kwargs):
            self.__dict__ = kwargs
            self.args = args

        cls.__init__ = __init__cls
        super(MyMeta, cls).__init__(name, bases, dct)

    def connect(cls, *args, **kwargs):
        if kwargs:
            d = kwargs
            d.update({'args': args})
            for key, value in cls.instances.items():
                if d in cls.instances.values():
                    return key
            return print('there is no such instance')
        else:
            arg = list(args)
            for key, value in cls.instances.items():
                check = []
                for val in value.values():
                    if isinstance(val, (int, str)):
                        check.append(val)
                    else:
                        part = [i for i in val]
                check = part + check
                if check == arg:
                    return key
            return print('there is no such instance')

    def __call__(cls, *args, **kwargs):
        setattr(cls, 'connect', cls.connect)
        setattr(cls, 'pool', cls.instances)
        instance = super().__call__(*args, **kwargs)
        for key, value in cls.instances.items():
            if cls.instances[key] == instance.__dict__:
                return key
        cls.instances[instance] = instance.__dict__
        return instance


class SiamObj(metaclass=MyMeta):
    pass
