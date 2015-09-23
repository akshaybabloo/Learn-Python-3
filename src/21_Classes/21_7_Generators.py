class Inclusive_range:
    def __init__(self, *args):
        number = len(args)
    
        if number < 1:
            raise TypeError('There should atleast be one argument')
        if number == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif number == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif number == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('There should at most 3 arguments, got {}'.format(number))
        
    def __iter__(self):
        i = self.start
            
        while i <= self.stop:
            yield i
            i += self.step



def main():
    try:
        o = Inclusive_range(30, 40, 1, 0, 5)
        for i in o: print(i, end = ' ')
#         for i in Inclusive_range(30): print(i, end = ' ') # i can even use it like this which will same output as above
    except TypeError as e:
        print('there was an error -', e)
        
    
if __name__ == '__main__': main()