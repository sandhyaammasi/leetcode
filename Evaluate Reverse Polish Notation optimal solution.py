tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

opdict = {  '+': lambda x, y: int(y) + int(x),
            '-': lambda x, y: int(y) - int(x),
            '*': lambda x, y: int(y) * int(x),
            '/': lambda x, y: int(y) / int(x),
            '%': lambda x, y: int(y) % int(x),
            '^': lambda x, y: int(y) ^ int(x),}         
onlyNumStack = []
for i in range(len(tokens)):
    if tokens[i]  not in opdict.keys():
        onlyNumStack.append(tokens[i])
    else:
        if len(onlyNumStack) >1:
            onlyNumStack.append(opdict[tokens[i]]( onlyNumStack.pop(),onlyNumStack.pop() ))
print(onlyNumStack)            