'''
Efficient Python code to find sum of numbers from 1 to N excluding N which are divisible by num1 or num2.


Logic:

1. Find the sum of numbers that are divisible by 3 upto N. Denote it by S1.
2. Find the sum of numbers that are divisible by 4 upto N. Denote it by S2.
3. Find the sum of numbers that are divisible by 12(3*4) upto N. Denote it by S3.
4. The final answer will be S1 + S2 – S3.

Using Arihmatic Porgression formula:

Sn = (n/2) * {2*a + (n-1)*d}

Where,
n -> total number of terms
a -> first term
d -> common difference


Example:

For 10, if we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Similarly for 100, we get 2318.
'''


def logic(N, num1, num2):
    '''Function to calculate the sum of numbers divisible by num1 or num2 between 1 to N excluding N'''
    
    mul = num1 * num2
    S1 = ((((N-1) // num1)) * (2 * num1 + ((N-1) // num1 - 1) * num1) //2)
    S2 = ((((N-1) // num2)) * (2 * num2 + ((N-1) // num2 - 1) * num2) // 2)
    S3 = ((((N-1) // mul)) * (2 * mul + ((N-1) // mul - 1) * mul) // 2)

    return (S1 + S2 - S3)

N = 10
print(logic(N, 3, 5))
