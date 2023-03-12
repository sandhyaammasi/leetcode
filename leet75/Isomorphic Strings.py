'''s = 'paper'
t = 'title'
s_dict = {}
t_dict = {}
for i in range(len(s)):
    if s[i] not in s_dict:
        s_dict[s[i]] = [i]
    else :
        s_dict[s[i]].append(i)

for i in range(len(t)):
    if t[i] not in t_dict:
        t_dict[t[i]] = [i]
    else :
        t_dict[t[i]].append(i)        

flag = 0
for i,j in zip(s_dict.keys(),t_dict.keys()):

    if s_dict[i] !=t_dict[j]:
        flag = flag+1

if flag > 0 :
    print("false")
else :
    print("true")'''



def isIsomorphic( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    t_dict = {}   
    s_dict = {}
    
    if len(s) != len(t):
        return False
    else:

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else :
                s_dict[s[i]].append(i)

        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = [i]
            else :
                t_dict[t[i]].append(i)        

        flag = 0
        for i,j in zip(s_dict.keys(),t_dict.keys()):

            if s_dict[i] !=t_dict[j]:
                flag = flag+1

        if flag > 0 :
            return False
        else :
            return True

print(isIsomorphic('paper','title'))