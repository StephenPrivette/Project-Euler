# prime factors
# What is the largest prime factor of the number 600,851,475,143
# the number given is too big

number = int(979797)
small_factor = int(1)
large_factor = int(2)
divider = int(2)
largest_prime = int(0)

while small_factor < large_factor:
    if number % divider == 0:
        small_factor = divider
        large_factor = number // divider
        
        small_prime = True
        for i in range (2, small_factor):
            if small_factor % i == 0:
                small_prime = False
        if small_prime == True and small_factor > largest_prime:
            largest_prime = small_factor
            print(largest_prime)

        large_prime = True
        for i in range (2, large_factor):
            if large_factor % i == 0:
                large_prime = False
        if large_prime == True and large_factor > largest_prime:
            largest_prime = large_factor
            print(largest_prime)

    divider += 1
print(largest_prime)
