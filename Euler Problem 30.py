##Surprisingly there are only three numbers that
##can be written as the sum of fourth powers of their digits:
##
##1634 = 14 + 64 + 34 + 44
##8208 = 84 + 24 + 04 + 84
##9474 = 94 + 44 + 74 + 44
##As 1 = 14 is not a sum it is not included.
##
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
##Find the sum of all the numbers that can be
##written as the sum of fifth powers of their digits.

number = 10
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
fifth_sums = 0
while number < 1000000:
    x = str(number)
    if number < 100:
        a,b = int(x[0]), int(x[1])
    elif number < 1000:
        a,b,c = int(x[0]), int(x[1]), int(x[2])
    elif number < 10000:
        a,b,c,d = int(x[0]), int(x[1]), int(x[2]), int(x[3])
    elif number < 100000:
        a,b,c,d,e = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4])
    else:
        a,b,c,d,e,f = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])
    if a**5 + b**5 + c**5 + d**5 + e**5 + f**5 == number:
        fifth_sums += number
    number += 1
print(fifth_sums)






        
