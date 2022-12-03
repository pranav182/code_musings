# Find total number of multiples of a given number (number) between two numbers (k and n) inclusive of both numbers (k and n).
import math

k = 21
n = 200
number = [i for i in range(1, 101)] # Took all numbers between 1 and 100 for testing
for ele in number:
    if k%ele == 0:
        ans = ((n//ele) - (k//ele)) + 1 # Formulae when k is divisible by number
    else:
        ans = ((n//ele) - (k//ele)) # Formulae when k is not divisible by number
    print(f"k = {k}, n = {n}, number = {ele}, answer = {ans}")
    
    # Possible one liner..
    ANS = (n//ele - math.ceil(k/ele)) + 1
    print(ANS)
    print('')
