#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import re

def one(): # this gives each line which has the same pattern as output
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line): # thats an binary or sign | not /
            print(line, end='')

def two(): # this gives the each word found in the file as the output
    fh = open('raven.txt')
    for line1 in fh:
        match = re.search('(Len|Neverm)ore', line1)
        if match:
            print(match.group())
            
def main():
    one()
    two()


if __name__ == "__main__": main()

