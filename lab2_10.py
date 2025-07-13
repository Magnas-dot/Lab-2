##10. Write a Python function that accepts a sentence and returns a set of all unique vowels
##used.


sentence=input("Enter a sentence:")
sentence=sentence.lower()
sentence=set(sentence)
vowel=[]
print(sentence)
for i in sentence:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel.append(i)
print("Set of all vowels used:",vowel)

