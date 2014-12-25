def main():
    
    a = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
    b = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five' # this is an another way or representing dictionary values
        )
    a['seven'] = 7 # inserting a value in dictionary
    b['seven'] = 7
    
    
    print(type(a), a)
    
    for i in a:
        print(i, a[i])
        
    print() # this is for space

    for i in sorted(a.keys()): # sorted() method will sort in alphabetical order by its key
        print(i, a[i])

    print() # this is for space

    for i in sorted(b.keys()): # sorted() method will sort in alphabetical order by its key
        print(i, b[i])
    
if __name__ == "__main__": main()