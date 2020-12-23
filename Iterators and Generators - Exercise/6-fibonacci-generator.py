def fibonacci():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

generator = fibonacci()
for i in range(5):
    print(next(generator))
