class Egg:
    def __init__(self, kind="fried"): # kind is a default variable, if no arguments is passed then kind is returned
        # __init__ is a constructor
        self.kind1 = kind
    
    def whatKind(self):
        return self.kind1
    
def main():
    fried1 = Egg()
    scrambled = Egg('scrambled')
    
   
    
    print(fried1.whatKind())
    print(scrambled.whatKind())
    
if __name__ == "__main__" : main()