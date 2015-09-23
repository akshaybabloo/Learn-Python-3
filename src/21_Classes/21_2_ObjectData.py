class Person:
    def __init__(self, color = 'white'):
        self._color = color
    
    def akshay(self):
        print('my name is akshay')
    
    def raj(self):
        print('my name is raj')
    
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color
    

def main():
    name = Person() # creating an instance
    
    print(name.get_color()) # to get the default color from the constructor
    
    name.set_color('red') # custom color to set_color
    print(name.get_color())
    
if __name__ == "__main__" : main()
    