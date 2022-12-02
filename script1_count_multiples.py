# Final total number of multiples of a given number (number) between two numbers (k and n)
k = 21
n = 200
number = [i for i in range(1, 101)] # Took all numbers between 1 and 100 for testing
for ele in number:
    if k%ele == 0:
        ans = ((n//ele) - (k//ele)) + 1 # Main algorithm
    else:
        ans = ((n//ele) - (k//ele)) # Main algorithm
    print(f"k = {k}, n = {n}, number = {ele}, answer = {ans}")
