def evens(limit=10):
    n = 0
    while True:
        n += 2
        if n > limit:
            return
        yield n


def odds(limit=10):
    n = 1
    while True:
        n += 2
        if n > 10:
            return
        yield n


def chain(g1, g2):
    yield from g1
    yield from g2


for i in chain(evens(), odds()):
    print(i)
