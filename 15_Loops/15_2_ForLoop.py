def main():
    # for loop
    print("this is for loop")
    fh = open('text.txt')
    a = [1, 2, 3, 4]
    for line1 in fh.readlines():
        print(line1, end='')
        # the tag end='' will make sure that there is no new line while looping 
        
    print()    
    
    for line2 in a: # iterating through list
        print(line2)

if __name__ == "__main__": main()