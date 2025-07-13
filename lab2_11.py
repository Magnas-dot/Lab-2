##11. Given a list of numbers with duplicates, use a set to remove the duplicates. Then,
##convert it back to a sorted list and display the result.


import random
list1=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    list1.append(random.randint(0,50))
list1=set(list1)
list1=list(list1)
list1.sort()
print("Sorted list:",list1)
