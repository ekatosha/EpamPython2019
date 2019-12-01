def applydecorator(func):
    def wrapper1(f):
        def wrapper(*args, **kwargs):
            return func(f, *args, **kwargs)
        return wrapper
    return wrapper1


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
