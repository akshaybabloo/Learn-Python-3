def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        # return keyword gives out booleans
    else:
        return True

def primes(n = 1):
    while(True):
        if isPrime(n): yield n
        # yield keyword gives out the value assigned to a variable
        n += 1
        
for n in primes():
    if n > 100: break
    print(n)