s = "abc"
t = "ahbgdc"

s_pt = 0
t_pt = 0

while s_pt < len(s) and t_pt < len(t) :
    if(s[s_pt] == t[t_pt]):
        s_pt += 1
        t_pt += 1
    else:
        t_pt+= 1

if s_pt == len(s):
    print("True")

else :
    print("False")