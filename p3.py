

#numbers=[1,2,3,4,5,6,7,8,9,10]
square=[i**2 for i in range(1,11) if i%2==0 ]
print(square)

words=["ai", "python" , "data"]
words_length={}

for word in words:
     words_length[word]=len(word)
print(words_length)

word="banana"
unique=set(word)
print(unique)