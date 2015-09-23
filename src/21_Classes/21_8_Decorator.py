class Dog:
    def __init__(self, **kwargs):
        self.properties = kwargs
    
    def bark(self):
        print('woof!')
     
    def walks(self):
        print('walks on four legs')
     
    def set_properties(self, k):
        return self.properties
 
    def get_property(self, k):
        return self.properties.get(k, None)
     
    @property
    def color(self):
        return self.properties.get('color', None)
    
    @color.setter
    def color(self, c):
        self.properties['color'] = c
    
    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    animal = Dog()
    
#     name = Dog(color = 'blue')
#     print(name.get_property('color'))
     
    animal.set_properties('color', 'red')
    print(animal.get_property('color'))
    
    animal.color = 'yellow', 'red'
    print(animal.color[0])
    print(animal.color[1])
    
    
if __name__ == "__main__" : main()
    