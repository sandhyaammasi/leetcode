'''Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''
roman ='IXIX'
buff = 0
romanDict = {
'I':buff + 1,
'V':buff + 5,
'X':buff + 10,
'L':buff + 50,
'C':buff + 100,
'D':buff + 500,
'M':buff + 1000,

}

romanDict2 = {
'IV':buff + 4,
'IX':buff + 9,
'XL':buff + 40,
'XC':buff + 90,
'CD':buff + 500,
'CM':buff + 900,
}
for key in romanDict2.keys():
    if (roman.find(key))>=0:
        buff = buff + romanDict2[key]
        roman = roman.replace(key,"",1)
print(buff)
print(roman)
