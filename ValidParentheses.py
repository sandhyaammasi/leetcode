s = "([])}"
mystack = []
closeBracketDict = {
                    ')':'(',
                    ']':'[',
                    '}':'{'
                    }
if len(s)%2 ==0:
    # do something
    for i in range(len(s)):
        i
        if s[i]=="(" or s[i]=="[" or s[i]=="{" :
            mystack.append(s[i])
        else :
            if(closeBracketDict[s[i]]==mystack[-1]):
                mystack.pop()
            else:
                print("false8")
                break


else:
    print("false")

if mystack == []:
    print('true')