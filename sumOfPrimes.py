'''Given an even number (greater than 2 ), print two prime numbers whose sum will be equal to given number.
There may be several combinations possible. Print only first such pair. 
An interesting point is, a solution always exist according to Goldbach’s conjecture.'''

# brute force , take primeNumberList(i) and iterate over primeNumberList(i+1) through primeNumberList(n) , find the matching sum
from math import sqrt

# step 1 : create a list of prime numbers 
num = int(input())
prime = 1
primeList = []
for i in range(2, int(sqrt(num))+1):
    prime = 1
    if num%i ==0 and i != num:
        prime = 0
        break
if prime == 0:
    print(str(num) + " is not prime")

