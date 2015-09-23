def main():
    fin = open('utf8.txt', 'r', encoding = 'utf_8') # read permission 'r' and should be read as UTF8
    fout = open('utf8.html', 'w') # write permission 'w' and write it to utf8.html
    
    outbytes = bytearray() # constructor
    
    for line in fin: # finding each fin
        for char in line: # finding each char in line
            if ord(char) > 127: # ord('_') gives the unicode of any char given to it and 127 is that till 128 they have basic char
                outbytes += bytes('&#{:04d};'.format(ord(char)), encoding = 'utf_8') # :04d, 04 is the length d is the char type
            else: outbytes.append(ord(char)) # if less that 127 puts everything gin the same way
                
#     for i in outbytes: print(chr(i), end='') # this another type of giving the output
    
    outstr = str(outbytes, encoding = 'utf_8') # converts array to string
    
    print(outstr, file = fout)
    print(outstr)
    

if __name__ == '__main__': main()