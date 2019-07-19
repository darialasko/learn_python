def my_for(interable, func):
    iterator = iter(interable)
    while True:
        try:
            thing = (next(iterator))
        except StopIteration:
            break
        else:
            func(thing)


# to jest to samo co:
# for x in [1, 2, 3]:
#   print(x)
my_for([1, 2, 3], print)
