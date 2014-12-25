def main():
    num = 10 
    a = 'Hello!'
    b = "Hello!"
    c = "Hello\nHi"
    d = r"Hello\nHi" # r means raw strings which gives the exact output, and usually used in regular expressions
    e = """ This is a big line """
    # this \ escapes the first blank line
    f = '''\ 
   this allows you to
   put multiple lines
   in python3
   '''
    g = "this number is {}".format(num)
   
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(d), d)
    print(type(e), e)
    print(type(f), f)
    print(type(g), g)

if __name__ == "__main__": main()