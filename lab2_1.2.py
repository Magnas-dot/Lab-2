##1. Write a program to input n numbers and store them in a list. Then perform the following
##operations without using built-in functions:

list1=[]
n=int(input("Enter how many numbers to enter: "))
for i in range(n):
      x=int(input("Enter Number:"))
      list1.append(x)
      
##a. Find the maximum and minimum number

for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print("Maximum Number:",list1[-1])
print("Minimum Number:",list1[0])

##b. Sort the list in ascending order
print("Sorting in ascending order:",list1)

##c. Remove duplicate elements
unique_list=[]
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print("List without duplicate elements:",unique_list)
