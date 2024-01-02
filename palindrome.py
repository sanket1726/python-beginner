isPalindrome = True


def checkPalindrome(string):
    global isPalindrome
    lengthOfString = len(string)
    print(lengthOfString)
    for i in range(lengthOfString):
        print(f'{string[i]} | {string[lengthOfString - i - 1]}')
        if string[i] == string[lengthOfString - i - 1]:
            isPalindrome = True
        else:
            isPalindrome = False
            break

    if isPalindrome:
        print(f'String {string} is palindrome')
    else:
        print(f'String {string} is not palindrome')


checkPalindrome('racecar')
