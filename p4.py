sentence="the cat and the hat and the bat"
print(sentence.split())

sentence="the cat and the hat and the bat"
words=sentence.split()
count={} #empty dic
for word in words:
    count[word]=count.get(word, 0) + 1
print (count)


sentence="the cat and the hat and the bat"
common=max(count , key=count.get)
print(common, len(common))