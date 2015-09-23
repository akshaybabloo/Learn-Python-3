def main():

    c = 'this is a string'
    for s in c:
        if s == 's' : continue # this skips letter s
        print(s, end='')

    print()
    
    for s1 in c:
        if s1 == 's' : break # jumps out of the loop when s is seen
        print(s1, end='')
        
    for s2 in c:
        print(s2, end='')
    else: # when there is nothing else to loop then else activates
        print('loop ended')
    
        
if __name__ == "__main__": main()