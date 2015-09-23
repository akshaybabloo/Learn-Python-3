def main():
    # for loop
    print("this is for loop")
    fh = open('text.txt')
    for index, line1 in enumerate(fh.readlines()):
        print(index, line1, end='')
        
    print()
    
    c = 'this is a string'
    for i, s in enumerate(c):
        if s == 's' : print('index of s is {}'.format(i))
        
if __name__ == "__main__": main()