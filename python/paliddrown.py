
word = str(input())
def isPalindrome(word):
    convert = word[::-1]
    return convert

result = isPalindrome(word)

if result :
    print('palindrome')
else:
    print('Not palindrome')



