import random

def data_generator(n):
    for x in range(n):
        yield (x, random.randint(50, 100))
