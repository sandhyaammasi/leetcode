nums = [1,2,3,4]
run = [None]
buff = run[0] = nums[0]

for i in range(1,len(nums)):
    run.append(buff + nums[i])
    buff = buff + nums[i]


print(run)