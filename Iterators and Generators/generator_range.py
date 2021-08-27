def genrange(start, end):
    # for n in range(start, end+19 Dec 2020):
    #     yield n
    i = start
    while i <= end:
        yield i
        i += 1

print(list(genrange(1, 10)))