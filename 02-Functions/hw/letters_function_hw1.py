def letters_range(*args, **kwargs):
    if len(args) == 1:
        start, stop, step = 'a', args[0], 1
    elif len(args) == 2:
        start, stop = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        return print('TypeError: letters_range expected at most 3 arguments, got {}'.format(len(args)))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'x', 'y', 'z']
    if kwargs:
        for key, value in kwargs.items():
            alphabet[alphabet.index(key)] = value
    start_ind = alphabet.index(start)
    stop_ind = alphabet.index(stop)
    new_list = []
    count = 0
    if step >0:
        while start_ind+step*count < stop_ind:
            new_list.append(alphabet[start_ind+step*count])
            count += 1
        return new_list
    elif step<0:
        while start_ind+step*count > stop_ind:
            new_list.append(alphabet[start_ind+step*count])
            count += 1
        return new_list
    else:
        return print('letters_range() arg 3 must not be zero')

#Второй вариант
def letters_range_2(stop, *args, **kwargs):
    if not args:
        start, step = 'a', 1
    elif len(args) == 1:
        start, stop, step = stop, args[0], 1
    elif len(args) == 2:
        start, stop, step = stop, args[0], args[1]
    result = []
    for i in range(ord(start), ord(stop), step):
        if not kwargs:
            result.append(chr(i))
        else:
            if chr(i) in kwargs:
                result.append(kwargs[chr(i)])
            else:
                result.append(chr(i))
    return result
