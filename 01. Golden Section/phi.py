from math import sqrt

PHI: float = 2 / (sqrt(5) - 1)

# Complexity:
#     Time = O(phi^N)
#     Space = O(N)
# def fibo(n: int) -> int:
#     if n <= 1:
#         return n
#     return fibo(n - 1) + fibo(n - 2)

# Complexity:
#     Time = O(N)
#     Space = O(1)
def fibo(n: int) -> int:
    a: int = 0
    b: int = 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

# Complexity:
#     Time = O(1)
#     Space = O(1)
def fibo_formula(n: int) -> int:
    return round((PHI ** n - (1 - PHI) ** n) / sqrt(5)) 


if __name__ == '__main__':
    prev: int = 1   
    for i in range(1, 42):
        result: int = fibo(i)
        print(f'fibo({i}) = {result} {result / prev}')
        prev = result
    print(f'{fibo_formula(41) = }')
    print(f'{PHI = }')