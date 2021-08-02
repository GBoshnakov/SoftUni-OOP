def tags(t):
    def add_tag(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{t}>{result}</{t}>"
        return wrapper
    return add_tag


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
