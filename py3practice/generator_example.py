def frange(start, stop, increments):
    x = start
    while x < stop:
        # yield statement turns it into a generator
        yield x
        x += increments

#A generator only runs  in response to iteration
for n in frange(0, 4, 0.5):
    print(n)