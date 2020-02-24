##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.


number = 5
prime_sums = 5

while number < 1000:
    prime = True
    for i in range (2, number // 2 + 1):
        if number % i == 0:
            prime = False
            break
    if prime == True:
        prime_sums += number
    number += 2
print(prime_sums)
