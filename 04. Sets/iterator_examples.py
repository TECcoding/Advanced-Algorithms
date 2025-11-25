from collections.abc import Iterator

c1 = [4, 8, 15, 116, 23, 42]
c2 = 'hello'
c3 = (3.14, 2.91, 9.1)

# for elem in c1:
#     print(elem)
    
# print()

# for char in c2:
#     print(char)

# print()
    
# for x in c3:
#     print(x)

# it1 = iter(c2)
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))

# it2 = iter(c2)
# try:
#     while True:
#         print(next(it2))
# except StopIteration:
#     ...

class Pow2Iterator:
    
    current: int
    
    def __init__(self):
        self.current = 1
        
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        if self.current > 1_000_000:
            raise StopIteration
        result: int = self.current
        self.current *= 2
        return result
    
# pow_it = Pow2Iterator()
# print(next(pow_it))
# print(next(pow_it))
# print(next(pow_it))
# print(next(pow_it))

# for n in Pow2Iterator():
#   print(n)

def simple_generator() -> Iterator[int]:
    x: int = 5
    yield x
    x *= 2
    yield x
    x -= 1
    yield x

it = simple_generator()
print(next(it))
print(next(it))
print(next(it))