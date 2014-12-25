#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import re

def one(): # this replaces the reg exp with replacement ### and outputs full text
    fh = open('raven1.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end='') # thats an binary or sign | not /

def two(): # this replaces the text and gives out the line out put where ever it has replaced
    fh = open('raven1.txt')
    for line1 in fh:
        match = re.search('(Len|Neverm)ore', line1)
        if match:
            print(line1.replace(match.group(), '###'), end='')
            
def main():
    one()
    two()


if __name__ == "__main__": main()

