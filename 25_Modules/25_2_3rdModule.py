import bitstring

def bit():
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.uint)

def main():
    bit()
    


    

if __name__ == '__main__': main()