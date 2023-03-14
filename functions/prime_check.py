def prime_is(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# to create a list of prime numbers using filter

print(list(filter(prime_is, range(100))))

