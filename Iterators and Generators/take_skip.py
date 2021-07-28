class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 1:
            raise StopIteration()
        current = self.number
        self.count -= 1
        self.number += self.step
        return current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
