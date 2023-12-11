str1 = "ABABAB"
str2 = "ABAB"

factors = [str2]

#find factors of str2
#replace every factor in str2 and if result is "" then its factor

for i in range(int(len(str2)/2)+1):
    if str2.replace(str2[:i],"")=="":
        factors.append(str2[:i])

for i in range(len(factors)):
    if str1.replace(factors[i],"")=="":
        continue
    else:
        factors[i]=""
print(max(factors, key = len))


