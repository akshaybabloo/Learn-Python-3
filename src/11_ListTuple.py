def main():
    
    a = (1,2,3) # this is Tuple
    b = [4,5,6] # this is List
    b.append(7) # insert number 7 at the end of the list
    b.insert(0, 8) # syntax insert(index, value)
    c = 'Hello!'
    
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(c), c[1]) # returns the letter at address 1
    print(type(c), c[1:4]) # this is called slice, returns the letters at the address 1 to 3 but not 4
    
    for i in a:
        print(i)
    
    for j in c:
        print(j)
    
if __name__ == "__main__": main()