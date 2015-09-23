
try:
    fh = open('xtext.txt')
    for line in fh.readlines():
        print(line, end='')
except IOError as e:
    print("error! ({})". format(e))