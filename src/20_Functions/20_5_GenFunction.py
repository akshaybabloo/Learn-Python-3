def main():
    try:
        for i in inclusiveRange(2, 100, 3):
            print(i, end=' ')
    except TypeError as e:
        print('there was an error :',e)
        
def inclusiveRange(*args):
    number = len(args)
    
    if number < 1:
        raise TypeError('There should atleast be one argument')
    if number == 1:
        stop = args[0]
        start = 0
        step = 1
    elif number == 2:
        (start, stop) = args
        step = 1
    elif number == 3:
        (start, stop, step) = args
    else:
        raise TypeError('There should at at most 3 arguments, got {}'.format(args))
    
    i = start
    while i <= stop:
        yield i
        i += step
    
   
    
if __name__ == "__main__" : main()