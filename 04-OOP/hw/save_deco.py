import functools


def save_func_info(wraped):
    def wrapper1(wrapper_func):
        def wrapper2(*args, **kwargs):
            return wraped(*args, **kwargs)
        setattr(wrapper2, '__name__', wraped.__name__)
        setattr(wrapper2, '__doc__', wraped.__doc__)
        setattr(wrapper2, '__original_func', wraped)
        return wrapper2
    return wrapper1


def print_result(func):
    @save_func_info(func)
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


if __name__ == '__main__':
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    print(custom_sum.__original_func)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
