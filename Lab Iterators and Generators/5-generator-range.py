def genrange(start, end):
    while start <= end:
        yield start
        start += 1

print(list(genrange(1, 10)))
for n in genrange(1, 10):
    print(n)