class vowels:
    def __init__(self, string: str):
        self.string = string
        self.i = 0

    def __iter__(self):
        return self

    def is_vowel(self, char):
        vowels_word = 'aeiuyo'
        return char.lower() in vowels_word

    def __next__(self):
        while self.i <= len(self.string) - 1:
            c = self.string[self.i]
            self.i += 1
            if self.is_vowel(c):
                return c
        raise StopIteration



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
