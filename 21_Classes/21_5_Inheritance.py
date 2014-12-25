class Country:
    def raj(self): print('hey i am from India')
    def usa(self): print('hey i am from USA')
    def nz(self): print('hey i am from NZ')

class Person(Country): # class Person inherits Country
    def akshay(self):
        print('my name is akshay')
    
    def raj(self):
        super().raj()
        print('my name is raj')

class person2(Country):
    pass

def main():
    name = Person() # creating an instance
    
    name.akshay()
    name.raj()

    name.usa()
    name.nz()

    person = person2()
    person.usa()
    
if __name__ == "__main__" : main()
    