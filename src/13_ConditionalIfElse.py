def main():
    
    a, b = 10, 20
    
    if a < b:
        c = "a is less than b"
    elif b > a:
        c = "b is gr8r than a"
    else:
        c = "b is less than a"
    print(c)
    
    # below is an conditional expression
    
    v = "a is less than b" if a < b else "a is gr8r than b"
    print(v)
    
if __name__ == "__main__": main()