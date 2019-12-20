def instances_counter(cls):
    count_instance = 0

    def __new__(cls, *args, **kwargs):
        nonlocal count_instance
        count_instance += 1
        return super(cls, cls).__new__(cls)

    def get_created_instances(*args, **kwargs):
        nonlocal count_instance
        return count_instance

    def reset_instances_counter(*args, **kwargs):
        nonlocal count_instance
        old = count_instance
        count_instance = 0
        return old

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
