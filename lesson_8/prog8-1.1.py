def print_map(function, iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(func(next(iterator)))
    except StopIteration:
        pass

def func(item):
    return item
