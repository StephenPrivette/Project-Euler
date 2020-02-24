##A palindromic number reads the same both ways.
##The largest palindrome made from the product of
##two 2-digit numbers is 9009 = 91 × 99.
##
##Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = 0
largest_pal = 0
for n in range(100, 1000):
    for i in range(100, 1000):
        number = n * i
        if number < 100000:
            number = str(number)
            if number[0] == number[4] and number[1] == number[3]:
                palindrome = int(number)
                if palindrome > largest_pal:
                    largest_pal = palindrome
        else:
            number = str(number)
            if number[0] == number[5] and number[1] == number[4]\
               and number[2] == number[3]:
                palindrome = int(number)
                if palindrome > largest_pal:
                    largest_pal = palindrome
print(largest_pal)
