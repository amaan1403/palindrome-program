#Function to check string is Palindrome or not
def isPalindrome(s):
    return s == s[::-1]
 
#driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
