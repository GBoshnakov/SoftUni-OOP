def get_primes(seq):
    def is_prime(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    for el in seq:
        if is_prime(el) and el not in (0, 1):
            yield el

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))