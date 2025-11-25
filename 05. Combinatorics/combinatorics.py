from pprint import pprint

# Slices in python
# lst[start:stop:step]
# s[::] - clone(copy)
# s[::-1] - reverse
# s[1::2] - elements at odd indices

def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:
    
    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)
    
    return sorted(s, key=size_and_content)

# Complexity: O(2^N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1])
    return temp + [e + [s[-1]] for e in temp]

# Combinations: How to select k items from of a original set with n items where the order doesnt matter
# n Ck = (n k) <- binomial coefficient = n! / (k! * (n-k)!)

# Complexity: O(k * (n Ck))
def combinations[T](s: list[T], k: int) -> list[list[T]]:
    return [e for e in power_set(s) if len(e) == k]

# Permutations: How to select k items from an original set with n items where the order does matter
# n Pk = (n k)k! = (n! / k! (n-k)!)k! = n! / (n-k)!

# x[start: end:  step]
#     0   len(x)  1
def insert[T](x: T, s: list[T], i: int) -> list[T]:
    return s[:i] + [x] + s[i:]

def insert_everywhere[T](x: T, s: list[T]) -> list[list[T]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]

def permute[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], e) for e in permute(s[:-1])], empty)

def permutations[T](s: list[T], k: int) -> list[list[T]]:
    empty: list[list[T]] = []
    return sum([permute(e) for e in combinations(s, k)], empty)

if __name__ == "__main__":
    pprint(power_set([])) # type: ignore
    pprint(power_set(['a']))
    pprint(power_set(['a', 'b']))
    pprint(power_set(['a', 'b', 'c']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd', 'e'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 2)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 1)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 4)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 0)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 3)))
    pprint(insert(7, [1, 2, 3, 4], 1))
    pprint(insert_everywhere(7, [1, 2, 3, 4]))
    pprint(permute([1]))
    pprint(nicely_sorted(permute([1, 2])))
    pprint(nicely_sorted(permute([1, 2, 3])))
    pprint(len(nicely_sorted(permute([1, 2, 3, 4]))))
    pprint(nicely_sorted(permutations(['a', 'b', 'c', 'd'], 2)))
    pprint(nicely_sorted(permutations(['a', 'b', 'c', 'd'], 3)))