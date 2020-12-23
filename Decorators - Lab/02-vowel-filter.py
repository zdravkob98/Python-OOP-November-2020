def vowel_filter(fn):
    def wrapper():
        result = fn()
        return [c for c in result if c in 'aouei']
    return wrapper




@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
