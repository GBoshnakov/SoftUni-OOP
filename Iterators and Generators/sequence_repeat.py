class sequence_repeat:
    def __init__(self, seq, count):
        self.seq = seq
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count:
            raise StopIteration()
        current = self.index
        self.index += 1
        return self.seq[current % len(self.seq)]


result = sequence_repeat('abcdef', 50)
for item in result:
    print(item, end ='')

