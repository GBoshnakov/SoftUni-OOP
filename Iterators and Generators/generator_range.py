def genrange(start, end):
    # for n in range(start, end+task_1):
    #     yield n
    i = start
    while i <= end:
        yield i
        i += 1

print(list(genrange(1, 10)))