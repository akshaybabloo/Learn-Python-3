def main():
    buffersize = 50000 # give it a size of 50000 bytes
    
    fin = open('olives.jpg', 'rb') # read the file in binary mode
    fout = open('new.jpg', 'wb') # writing to a new file to new.jpg in binary mode
     
    buffer = fin.read(buffersize) # reads the file at every 50000 bytes
     
    while len(buffer): # when length of the buffer is not 0 do the following
        fout.write(buffer) # write at every 50000 bytes
        print('.', end = '') # at every write print '.' in the console
        buffer = fin.read(buffersize) # so that the buffer does not write for ever
    print()
    print('Done')
    

if __name__ == '__main__': main()

