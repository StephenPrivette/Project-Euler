# multiples of 3 and 5
sums = 0
for i in range (1000):
    if i % 3 == 0:
        sums = sums + i
    elif i % 5 == 0:
        sums = sums + i
print(sums)
    
