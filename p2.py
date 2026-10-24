word="Programming"
#reverse=word[::-1]
#print("Reverse:", reverse)
print("1st three char:", word[:3] ,"     Last 3 char:" ,word[-3:])
print(word.count("m"))
def is_palindrome(word):
    return word==(word[::-1])
print(is_palindrome("python"))
print(is_palindrome("level"))
    
