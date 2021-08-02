def type_check(type_obj):
    def check_accept(func):
        def wrapper(arg):
            if type(arg) == type_obj:
                return func(arg)
            return "Bad Type"
        return wrapper
    return check_accept


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))
