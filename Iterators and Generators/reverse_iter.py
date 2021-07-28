class reverse_iter:
    def __init__(self, nums):
        self.nums = nums
        self.index = len(self.nums) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        current = self.index
        self.index -= 1
        return self.nums[current]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
