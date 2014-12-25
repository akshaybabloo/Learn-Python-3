import sys

    
def system():
    print('python version {}.{}.{}'.format(*sys.version_info))
    print('systome platform is', sys.platform)

def operating_system():
    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
#         print(os.getcwdb())
    print(os.urandom(25))

def url_lib():
    import urllib.request
 
    url = urllib.request.urlopen('http://www.gollahalli.com')
#         print(url) # this is an iterative object
    for i in url: print(str(i, encoding = 'utf_8'), end = ' ')
    
def randomNumGen():
    import random
    print(random.randint(1, 1000)) # prints one random number between 1 and 1000
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    
def dateAndTime():
    import datetime
    x = datetime.datetime.now()
    print(x)
    print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
    
        

def main():
    system()
    operating_system()
    randomNumGen()
    dateAndTime()
    url_lib()
    


    

if __name__ == '__main__': main()