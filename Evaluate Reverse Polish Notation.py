tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
xpointer = 0
ypointer = 1
operpointer = 2
opdict = {  '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y),
            '*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x) / int(y),
            '%': lambda x, y: int(x) % int(y),
            '^': lambda x, y: int(x) ^ int(y),}


while len(tokens)>3:
    if tokens[operpointer] in opdict.keys() and tokens[xpointer] not in opdict.keys() and tokens[ypointer] not in opdict.keys():
            buff = opdict[tokens[operpointer]](tokens[xpointer],tokens[ypointer])
            tokens.insert(xpointer,buff)
            tokens.pop(xpointer+1)
            tokens.pop(xpointer+1)
            tokens.pop(xpointer+1)
            xpointer = 0
            ypointer = 1
            operpointer = 2
            '''xpointer = xpointer + 1
            ypointer = xpointer + 1
            operpointer = ypointer + 1'''
            
    else:
            xpointer = xpointer + 1
            ypointer = xpointer + 1
            operpointer = ypointer + 1


'''if inputArray[2] in  opdict.keys():
    print(opdict[inputArray[2]](inputArray[0],inputArray[1]))'''
if tokens[2] in  opdict.keys():
    print(opdict[tokens[2]](tokens[0],tokens[1]))
print(tokens)

