def main():
    fin = open('text.txt', 'r') # specifing a 
    fout = open('new.txt', 'w') # writing to a new file to new.txt
    
    for i in fin: print(i, file = fout, end = '') # file = fout tells python to write file

#     Alternate way of reading and writing files
#     sometext = fin.read()
#     fout.write(sometext)

if __name__ == '__main__': main()

