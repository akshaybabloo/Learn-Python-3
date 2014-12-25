
# while loop
print("this is while loop")
a, b = 0, 1

while b < 50:
    print(b)
    a, b = b, a + b
    
# for loop
print("this is for loop")
fh = open('text.txt')
for line in fh.readlines():
    print(line, end='')
    # the tag end='' will make sure that there is no new line while looping 