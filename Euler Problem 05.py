# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

number = 20
test = False
while test == False:
    test = True
    for i in range (1,20):
        if number % i != 0:
            test = False
    if test == False:
        number += 20
    else:
        answer = number
print(answer)
    

