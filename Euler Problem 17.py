##If the numbers 1 to 5 are written out in words: one, two, three, four,
##five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written
##out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
##and forty-two) contains 23 letters and 115 (one hundred and fifteen)
##contains 20 letters. The use of "and" when writing out numbers is
##in compliance with British usage.

numbers = ['','one','two','three','four','five','six','seven','eight','nine',\
           'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
           'seventeen','eighteen','nineteen','twenty'] + [''] * 980
numbers[30] = 'thirty'
numbers[40] = 'forty'
numbers[50] = 'fifty'
numbers[60] = 'sixty'
numbers[70] = 'seventy'
numbers[80] = 'eighty'
numbers[90] = 'ninety'
numbers[100] = 'onehundred'
numbers[200] = 'twohundred'
numbers[300] = 'threehundred'
numbers[400] = 'fourhundred'
numbers[500] = 'fivehundred'
numbers[600] = 'sixhundred'
numbers[700] = 'sevenhundred'
numbers[800] = 'eighthundred'
numbers[900] = 'ninehundred'
numbers[1000] = 'onethousand'

def tens(numbers, a, b, c):
    x = 1
    for i in range (a, b):
        numbers[i] = numbers[c] + numbers[x]
        x += 1

a = 21
b = 30
c = 20

for i in range(1,9):
    tens(numbers, a, b, c)
    a += 10
    b += 10
    c += 10
    
d = 100
e = 101
f = 200

for z in range(1,10):
    for i in range(e,f):
        numbers[i] = numbers[d] + 'and' + numbers[i - d]
    d += 100
    e += 100
    f += 100

j = 0
for y in numbers:
    j += len(y)

print(j)
