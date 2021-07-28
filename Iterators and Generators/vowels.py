class vowels:
    def __init__(self, text):
        self.text = text
        self.text_vowels = [el for el in self.text if el in "AEIOUYaeiouy"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.text_vowels):
            raise StopIteration()
        current = self.index
        self.index += 1
        return self.text_vowels[current]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
