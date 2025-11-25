# Bitwise Instructions
# & -- AND
# | -- OR
# ^ -- XOR
# ~ -- NOT
# << -- SHIFT LEFT
# >> -- SHIFT RIGHT


# 0b -- binary
# 0o -- octal
# 0x -- hexadecimal

a: int = 5  #0b0101
b: int = 9  #0b1001
c: int = 15 #0b1111

print(f'{bin(a) = }')
print(f'{oct(b) = }')
print(f'{hex(c) = }')

s: str = '1010'
print(f'{int(s, 10) = }')
print(f'{int(s, 2) = }')
print(f'{int(s, 8) = }')
print(f'{int(s, 16) = }')
print(f'{int(s, 36) = }')


# AND (&)
print(f'{a & b = }')
print(f'{a & c = }')
print(f'{b & c = }')

# OR (|)
print(f'{a | b = }')
print(f'{a | c = }')
print(f'{b | c = }')

# XOR (Hat, Gorrito ^)
print(f'{a ^ b = }')
print(f'{a ^ c = }')
print(f'{b ^ c = }')

# NOT (Tilde ~)
print(f'{~a = }')
print(f'{~b = }')
print(f'{~c = }')

# Shift left (<<) (same thing as multiplying x * 2^n)
print(f'{a << b = }')
print(f'{a << c = }')
print(f'{b << c = }')

# Shift right (>>) (same thing as floor(x / 2^n))
print(f'{a << b = }')
print(f'{a << c = }')
print(f'{b << c = }')