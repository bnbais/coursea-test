# write a programe to reverse a word
word=input('Enter word=')
rev=''
for i in range(len(word)-1,-1,-1):
    rev+=word[i]
print(rev)   