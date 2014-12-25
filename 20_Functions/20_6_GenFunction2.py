def main():
    for i in inclusiveRange(0, 25, 1):
        print(i, end=' ')

def inclusiveRange(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step
   
    
if __name__ == "__main__" : main()