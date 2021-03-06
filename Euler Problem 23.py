##A perfect number is a number for which the sum of its proper divisors
##is exactly equal to the number. For example, the sum of the proper
##divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
##is a perfect number.
##
##A number n is called deficient if the sum of its proper divisors is
##less than n and it is called abundant if this sum exceeds n.
##
##As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
##smallest number that can be written as the sum of two abundant numbers
##is 24. By mathematical analysis, it can be shown that all integers greater
##than 28123 can be written as the sum of two abundant numbers.
##However, this upper limit cannot be reduced any further by analysis
##even though it is known that the greatest number that cannot be expressed
##as the sum of two abundant numbers is less than this limit.
##
##Find the sum of all the positive integers which cannot be written
##as the sum of two abundant numbers.

all_nums = []
abundant_numbers = []
two_abuns = 0
all_two_abuns = []
answer_sum = 0

for number in range (1, 28124):
    all_nums.append(number)
    divisor_sum = 0
    
    for divisor in range (1, number // 2 + 1):
        if number % divisor == 0:
            divisor_sum += divisor
            
    if divisor_sum > number:
        abundant_numbers.append(number)

for i in abundant_numbers:
    for n in abundant_numbers:
        two_abuns = i + n
        if two_abuns < 28124:
            all_two_abuns.append(two_abuns)
            
new_abuns = list(set(all_two_abuns))    

for i in new_abuns:
    all_nums.remove(i)

for i in all_nums:
    answer_sum += i

print (answer_sum)

























    
    
