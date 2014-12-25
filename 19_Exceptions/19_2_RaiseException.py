def main():
    try:
        for i in readLine('text.txtt'): print(i.strip())
    except IOError as e:
        print("there was an error - {}".format(e))
    except ValueError as e1:
        print('bad file name - ', e1)
        

def readLine(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('the document must end with .txt')

if __name__ == "__main__" : main()