def palindrome(str):
    left = 0
    right = len(str) - 1
    for i in range(left,right):
        if str[left] != str[right]:
            return False

    return True
str = "121"
print(f"palindrome - {palindrome(str)}")
 