def main():
    
    # while loop
    print("this is while loop")
    a, b = 0, 1
    
    while b < 50:
        print(b)
        a, b = b, a + b
        
if __name__ == "__main__": main()