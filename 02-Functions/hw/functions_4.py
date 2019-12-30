import inspect

def modified_func(func, *fixated_args, **fixated_kwargs):
    def wrapper(*args, **kwargs):
        if args and kwargs:
            nonlocal fixated_args
            fixated_args = list(fixated_args)
            fixated_kwargs.update(kwargs)
            fixated_args.extend(args)
            return func(*fixated_args, **fixated_kwargs)
        return func(*fixated_args, **fixated_kwargs)
    name = func.__name__
    source = inspect.getsource(func)
    wrapper.__name__ = 'func_{}'.format(name)
    wrapper.__doc__ = "A func implementation of {} with pre-applied arguments being: {}, {}. source_code: {}".format(name, str(fixated_args), str(fixated_kwargs), source)
    return wrapper
