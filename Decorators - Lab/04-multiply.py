def multiply(n):
    def inner(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, *kwargs)
            return result * n
        return wrapper
    return inner




@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
