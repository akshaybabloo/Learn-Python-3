def main():
    call(10)
    
def call(a, b = None, c = 30):
    if b == None: # None is a singletone object
        b = 0
    print("This is a call() function which takes 3 numbers :", a, b, c)
    
if __name__ == "__main__" : main()