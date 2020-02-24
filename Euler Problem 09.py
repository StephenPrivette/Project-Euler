##A Pythagorean triplet is a set of three
##natural numbers, a < b < c, for which,
##
##a2 + b2 = c2
##For example, 32 + 42 = 9 + 16 = 25 = 52.
##
##There exists exactly one Pythagorean
##triplet for which a + b + c = 1000.
##Find the product abc

triplet = 0
sums = 1000
a = 1
b = 2
c = 3
while triplet != sums: 
    while a + b + c <= sums:
        while a + b + c <= sums:
            if (a * a) + (b * b) == (c * c):
                triplet = a + b + c
                print(a,b,c,triplet)
                if triplet == sums:
                    product = a * b * c
                    print()
                    print(a, b, c)
                    print(triplet)
                    print(product)
                    break
            c += 1
        b += 1
        c = b + 1
    a += 1
    b = a + 1
    c = b + 1
    
