import functools


def print_result(func):
    @new_decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result, args
    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def new_decorator(f1):
    def wrapper2(wrapper_func, wraped=f1):
        name = getattr(wraped, '__name__')
        doc = getattr(wraped, '__doc__')
        original_func = wraped
        def wrapper3(*args, **kwargs):
            return wraped(*args, **kwargs)
        setattr(wrapper3, '__name__', name)
        setattr(wrapper3, '__doc__', doc)
        setattr(wrapper3, '__original_func', original_func)
        return wrapper3
    return wrapper2
