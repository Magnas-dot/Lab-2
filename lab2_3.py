##3. Create a program that reads a sentence from the user and stores each word as an
##element of a list. Then count the frequency of each word using only lists.

sentence=input("Enter a sentence:")
list1=sentence.split(" ")
unique_list=[]
frequencies=[]
for word in list1:
    if word in unique_list:
        index=unique_list.index(word)
        frequencies[index]+=1
    else:
        unique_list.append(word)
        frequencies.append(1)

for i in range(len(unique_list)):
    print(f"{unique_list[i]}:{frequencies[i]}")
