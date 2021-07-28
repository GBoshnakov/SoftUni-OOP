class dictionary_iter:
    def __init__(self, d):
        self.d = d
        self.elements = [(key, val) for key, val in self.d.items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.d):
            raise StopIteration()
        current = self.index
        self.index += 1
        return self.elements[current]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
