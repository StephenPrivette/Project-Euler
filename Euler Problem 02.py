# even fibonacci numbers

fib_sum = 0
next_fib = 0
second_fib = 1
last_fib = 2
while last_fib < 4000000:
    next_fib = second_fib + last_fib
    second_fib = last_fib
    last_fib = next_fib
    print(last_fib, "lastfib")
    if last_fib % 2 == 0:
        fib_sum += last_fib
    print(fib_sum, "fibsum")
fib_sum += 2
print (fib_sum)
