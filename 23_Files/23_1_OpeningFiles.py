def main():
    fh = open('text.txt') # by default open() has read mode
    
    for i in fh: print(i, end = '')
    
#     (OR)
#     for j in fh.readlines(): print(j, end = '')

if __name__ == '__main__': main()

