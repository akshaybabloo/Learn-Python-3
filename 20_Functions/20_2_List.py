def main():
    call(10, 20, 30, 1, 2, 3, 4)
    
def call(a, b, c, *args): # *args is simple list argument to take inmultiple values
    print(a, b, c)
    for i in args: print(i, end=' ')
    
if __name__ == "__main__" : main()