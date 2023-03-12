def hammingWeight(n):
    
    countOnes = 0
    for e in n:
        if e =='1':
            countOnes+=1
    return countOnes


n = "11111111111111111111111111111101"
print(hammingWeight(n))

