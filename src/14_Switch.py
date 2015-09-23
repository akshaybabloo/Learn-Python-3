# python does not support switch statements, below is one of the many alternatives

def main():
    
    option = dict(
        one = 'first',
        two = 'secound',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    
    var = 'one'
    
    print(option[var]) # prints out the value assigned to one which is first
if __name__ == "__main__": main()