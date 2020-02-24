# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

prime_counter = 1
number = 2

while prime_counter < 10001:
    number += 1
    if number % 2 != 0:
        
        prime = True
        for i in range (2, number):
            if number % i == 0:
                prime = False
        if prime == True:
            prime_counter += 1
print(number)
