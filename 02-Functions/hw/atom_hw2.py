def atom(value=None):
    atom.__value = getattr(atom, 'value', value)
    def get_value():
        return atom.__value
    def set_value(new_val):
        atom.__value = new_val
        return print('The value has been changed to {}'.format(new_val))
    def process_value(*args):
        for i in args:
            atom.__value = i(atom.__value)
        return atom.__value
    def delete_value():
        atom.__value = None
        return print('The value has been deleted')
    return get_value, set_value, process_value, delete_value
