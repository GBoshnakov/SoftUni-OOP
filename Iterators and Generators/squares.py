def squares(n):
    # num = task_1
    # while num <= n:
    #     yield num ** 2
    #     num += task_1
    for num in range(1, n+1):
        yield num ** 2


print(list(squares(5)))