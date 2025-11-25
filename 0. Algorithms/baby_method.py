def baby_sqrt(s: float, guess: float, delta: float) -> float:
    if s < 0:
        raise ValueError(f'Cannot compute square root of: {s}')
    
    prev: float = guess
    while True:
        guess = (prev + s / prev) / 2
        if abs(guess - prev) <= delta:
            return guess
        
        prev = guess

# if __name__ == '__main__':
#     print("Running a script:", __name__)
# else:
#     print("Importing a module:", __name__)

if __name__ == '__main__':
    temp: float = baby_sqrt(9, 1, 1e-10)
    print(temp * temp)