def productExceptSelf(nums):
    product = 1
    num_of_zero = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            product = product * nums[i]
        else:
            num_of_zero+=1
    sol = []
    for i in range(len(nums)):
        if num_of_zero == 1: # 1 zero - return product of non zero 0 and 0 as product
            if nums[i]==0:
                sol.append(product)
            else :
                sol.append(0)
        elif num_of_zero > 1:
            sol.append(0)
        else:
            try:
                sol.append(int(product / nums[i]))
            except ZeroDivisionError:
                sol.append(0)

    return sol

    
soln = productExceptSelf([1,2,3,4])
print(soln)
soln = productExceptSelf([1,2,3,4,0])
print(soln)
soln = productExceptSelf([1,0,2,3,4,0])
print(soln)