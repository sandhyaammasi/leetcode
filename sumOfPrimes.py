'''Given an even number (greater than 2 ), print two prime numbers whose sum will be equal to given number.
There may be several combinations possible. Print only first such pair. 
An interesting point is, a solution always exist according to Goldbach’s conjecture.'''

# brute force , take primeNumberList(i) and iterate over primeNumberList(i+1) through primeNumberList(n) , find the matching sum
from math import sqrt
import time
# step 1 : create a list of prime numbers 
#   create a list with all the numbers 2 through num
num = 499979
primeList = list(range(2, num))
primeList = [n for n in primeList if n%2 == 1]
primeList2 = primeList.copy()
for p in primeList:
    for i in range(2,int(sqrt(num))+1):
        if (p % i == 0) and (p!=i) and (p in primeList2):
            primeList2.remove(p)


print(len(primeList2)+1)

        