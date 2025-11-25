def gcd2(a: int, b: int) -> int:
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

def gcd(a: int, b: int, *rest: int) -> int:
    result: int = gcd2(a, b)
    for n in rest:
        result = gcd2(result, n)
    return result

def are_comprimes(a: int, b: int) -> bool:
    return gcd2(a, b) == 1

def lcm(a:int , b:int) -> int:
    return a*b // gcd(a, b)

#int / int -> float
#float / float -> float
#int / float -> float

# Normal division 1/2 -> 0.5 (float)
# Floor division 1//2 -> 0 (int)

# Ceil division int() just take away the decimal part
 
if __name__=='__main__':
    print(f'{gcd(20,15) = }')
    print(f'{gcd(20,150) = }')
    print(f'{gcd(20,15, 35, 100, 50) = }')
    print(f'{are_comprimes(25, 14) = }')
    print(f'{lcm(10, 15) = }')