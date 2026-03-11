input = "abccba"
input_1 = "소주만병만주소"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[len(string) - 1]:
        return False
    return is_palindrome(string[1:len(string) - 1])


print(is_palindrome(input))
print(is_palindrome(input_1))