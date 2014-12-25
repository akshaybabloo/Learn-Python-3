def main():
    call(1, 2, 3, 4, 5, 6, one = 1, two = 2, nine = 9)
    
def call(this, that, others, *args, **kwargs): # **kwargs is also know as key word args, which is of type dictionary
   
    print(this, that, others, args, kwargs['one'], kwargs['two'], kwargs['nine'])
   
    
if __name__ == "__main__" : main()