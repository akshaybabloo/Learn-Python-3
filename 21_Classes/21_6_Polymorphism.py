class Dog:
    def bark(self): print('dog barks')
    def walk(self): print('dog walk on four legs')
    def sings(self): print('dogs cannot sing like birds')
    def feathers(self): print('dogs dont have feathers')

class Bird:
    def sings(self): print('birds can sing')
    def feathers(self): print('birds have nice feathers')
    def bark(self): print('birds cannot bark')
    def walk(self): print('birds have two legs')
    
def main():
    animal1 = Dog()
    bird1 = Bird()
    
    in_the_house(bird1) # change it with animal1 and see the difference
    on_the_tree(bird1)
    
def in_the_house(someDog): # this function expects only two methods, which has different meaning in different class, but has the 
    # has the same function name
    someDog.bark()
    someDog.walk()
    
def on_the_tree(someBird):
    someBird.sings()
    someBird.feathers()
    
    
#     for o in (animal1, bird1):
#         o.bark()
#         o.walk()
#         o.sings()
#         o.feathers()
    
if __name__ == "__main__" : main()
    