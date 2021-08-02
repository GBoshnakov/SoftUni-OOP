def even_parameters(func):
    def wrapper(*args):
        for el in args:
            try:
                if el % 2 != 0:
                    return "Please use only even numbers!"
            except:
                return "Please use only even numbers!"

        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
