#2. Given two lists of integers, write a program to merge them into a single list and then
#remove the elements that are common in both.
import random
l1=[]
l2=[]
for i in range (10):
    l1.append(random.randint(1,20))
    l2.append(random.randint(1,20))
merge=l1+l2
common=[]
for j in l1:
    if j in l2:
        common.append(j)
result=[]
for k in merge:
    if k not in common:
        result.append(k)
print("first list:",l1)
print("Second list:",l2)
print("Result list without common elements:",result)
    
