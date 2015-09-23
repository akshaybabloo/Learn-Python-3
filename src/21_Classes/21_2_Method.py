class Person:
    def __init__(self, value): # this is a constructor 
        self._v = value # _v is a local variable
        print('constructor')
    
    def akshay(self):
        print('my name is akshay', self._v)
    
    def raj(self):
        print('my name is raj', self._v)

def main():
    name = Person(10) # creating an instance
    hello = Person(20)
    
    name.akshay()
    name.raj()

    hello.akshay()
    hello.raj()
    
    
if __name__ == "__main__" : main()
    