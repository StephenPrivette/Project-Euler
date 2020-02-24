##Let d(n) be defined as the sum of proper divisors of n
##(numbers less than n which divide evenly into n).
##If d(a) = b and d(b) = a, where a ≠ b, then a and b
##are an amicable pair and each of a and b are called amicable numbers.
##
##For example, the proper divisors of 220 are
##1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
##therefore d(220) = 284. The proper divisors of 284 are
##1, 2, 4, 71 and 142; so d(284) = 220.
##
##Evaluate the sum of all the amicable numbers under 10000.

amicable_sum = 0

for number in range (1, 10001):
    divisor_sum = 0
    test_sum = 0
    
    for i in range (1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i
            
    for n in range (1, divisor_sum // 2 + 1):
        if divisor_sum % n == 0:
            test_sum += n
            
    if number == test_sum and number != divisor_sum:
        amicable_sum += number
        
print(amicable_sum)
            
        
