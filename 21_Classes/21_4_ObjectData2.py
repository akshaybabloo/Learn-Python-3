class Person:
    def __init__(self, **kwargs):
        self.variable = kwargs
    
    def akshay(self):
        print('my name is akshay')
    
    def raj(self):
        print('my name is raj')
    
    def set_variable(self, k, v):
        self.variable[k] = v

    def get_variable(self, k):
        return self.variable.get(k, None)

def main():
    name = Person(eyes = 2, nose = 1, eye_color = 'brown')
    print(name.get_variable('eyes'))
    print(name.get_variable('nose'))
    print(name.get_variable('eye_color'))
    
    
    name.set_variable('color', 'red')
    print(name.get_variable('color'))
    
    
if __name__ == "__main__" : main()
    