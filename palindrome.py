
def isPalindrome(x):
    if x < 0 :
        return False
    # idea is to reverse a number and subtract it , if 0 => palindrome else not a palindrome
    rev = 0
    while (x>0) :
        rev = (rev + (x % 10) )*10
        x = int(x/10)
    print(int(rev/10),x)
    if int(rev/10) == x:
        return True
    else:
        return False

