##The following iterative sequence is defined
##for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13,
##we generate the following sequence:
##
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##It can be seen that this sequence
##(starting at 13 and finishing at 1) contains 10 terms.
##Although it has not been proved yet (Collatz Problem),
##it is thought that all starting numbers finish at 1.
##
##Which starting number, under one million, produces the longest chain?

longest_chain = 0
for i in range (2, 1000000):
    current_number = i
    current_chain = 1
    while i > 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = i * 3 +1
        current_chain += 1
    if current_chain > longest_chain:
        longest_chain = current_chain
        longest_number = current_number
print (longest_number, "is the starting number with the longest chain of"\
       , longest_chain)
    
    

