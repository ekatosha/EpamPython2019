""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self.exception

    def __exit__(self, type_, value_, traceback_):
        return isinstance(value_, self.exception)


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")