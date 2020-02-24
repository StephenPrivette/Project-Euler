##n! means n × (n − 1) × ... × 3 × 2 × 1
##
##For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
##and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
##
##Find the sum of the digits in the number 100!

mults = 1
sums = 0

for i in range (100, 0, -1):
    mults *= i
product = str(mults)
for i in range (0, len(product)):
    print(i)
    adder = int(product[i])
    sums += adder
    print(sums)
    
