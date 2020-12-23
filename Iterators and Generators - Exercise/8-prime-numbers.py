def get_primes(numbers: list):
    idx = 0
    while idx < len(numbers):
        num = numbers[idx]
        idx += 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))