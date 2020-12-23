def number_increment(numbers):
    def increase():
        return [n + 1 for n in numbers]

    return increase


print(number_increment([1, 2, 3])) #need to be increase()


n = number_increment([1, 2, 3])
print(n())