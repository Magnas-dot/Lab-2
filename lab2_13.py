##13. Write a program that reads a text and counts the frequency of each character (excluding
##spaces and special characters) using a dictionary.


text=input("Enter the text:")
word=[]
for i in text:
    if i!=" ":
       word.append(i)
print(word)
dicti={}
for key in word:
    if key in dicti:
        dicti[key]+=1
    else:
        dicti[key]=1
print(dicti)
