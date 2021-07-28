def possible_permutations(seq):
    def all_permutations(string):
        if len(string) == 0:
            return []
        if len(string) == 1:
            return [string]
        result = []

        for i in range(len(string)):
            current = string[i]
            string_modified = string[:i] + string[i+1:]

            for p in all_permutations(string_modified):
                result.append([current] + p)

        return result

    permutations = all_permutations(seq)
    for perm in permutations:
        yield perm


[print(n) for n in possible_permutations([1, 2, 3])]