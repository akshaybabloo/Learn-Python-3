def isPrime(n):
# def keywoard tells the python that anything after that is a function name, a function can have comma seperated value
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, "is a prime number")
        return True

for a in range(1, 20):
    isPrime(a)
    # calling the function
    