
# O(1)
def is_even(n: int) -> bool:
    return (n & 1) == 0


# O(1)
def turn_uneven(n: int) -> int:
    return n | 1


# O(log N)
def count_bits(n: int) -> int:
    count: int = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count


# O(1)
def is_power_of_2(n: int) -> bool:
    return (n & (n - 1)) == 0


# O(log N)
def int_mul(m: int, n: int) -> int:
    negative: bool = (m < 0) ^ (n < 0)
    m = abs(m)
    n = abs(n)
    result: int = 0
    while n:
        result += m if n & 1 else 0
        m <<= 1
        n >>= 1
    return -result if negative else result


# O(log N)
def int_log2(n: int) -> int:
    if n <= 0:
        raise ValueError(f'int_log2 not defined for {n}')
    count: int = 0
    while n > 1:
        count += 1
        n >>= 1
    return count

if __name__ == '__main__':
    print(f'{is_even(4) = }')
    print(f'{is_even(13) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(665) = }')
    print(f'{turn_uneven(5) = }')
    print(f'{turn_uneven(10) = }')
    print(f'{count_bits(0) = }')
    print(f'{count_bits(1) = }')
    print(f'{count_bits(27) = }')
    print(f'{count_bits(1024) = }')
    print(f'{count_bits(1023) = }')
    print(f'{is_power_of_2(8) = }')
    print(f'{is_power_of_2(64) = }')
    print(f'{is_power_of_2(5) = }')
    print(f'{is_power_of_2(500) = }')
    print(f'{int_mul(4, 5) = }')
    print(f'{int_mul(100, 234) = }')
    print(f'{int_mul(100, -234) = }')
    print(f'{int_mul(-100, -234) = }')
    print(f'{int_log2(10) = }')
    print(f'{int_log2(32) = }')
    print(f'{int_log2(63) = }')
    print(f'{int_log2(64) = }')