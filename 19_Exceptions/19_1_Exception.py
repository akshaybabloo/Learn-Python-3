def main():
    try:
        fh = open('xtext.txt')
    except IOError as e:
        print("there was an error - {}".format(e))
    else:    
        for i in fh: print(i.strip())

if __name__ == "__main__" : main()