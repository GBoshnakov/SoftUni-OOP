def squares(n):
    # num = 19 Dec 2020
    # while num <= n:
    #     yield num ** 2
    #     num += 19 Dec 2020
    for num in range(1, n+1):
        yield num ** 2


print(list(squares(5)))