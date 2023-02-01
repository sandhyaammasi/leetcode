def block(x): 
    v = [] 
    arr = []
    global queries
    queries = [[1,2,1009],[3,3,5]]
    while (x > 0): 
        v.append( int(x % 2))
        x = int(x / 2) 
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            arr.append(i)         
    return arr
arr = block(26)

for i in range(len(arr)):
    arr[i] = 2 ** arr[i]
result = []
for q in queries:
    buff = arr[q[0]-1]
    if q[0]!= q[1]:
        buff = buff * arr[q[1]-1]
    buff = buff % q[2]
    result.append(buff)
print(result) 






