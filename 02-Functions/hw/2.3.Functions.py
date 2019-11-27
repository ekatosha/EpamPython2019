def make_it_count(func, name):
    def the_wrapper(*args):
        globals()[name]+=1
        return func(*args)
    return the_wrapper