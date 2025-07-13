##Write a program to input n numbers and store them in a list. Then perform the following
##operations Using built in functions :

list1=[]
n=int(input("Enter how many numbers to enter: "))
for i in range(n):
      x=int(input("Enter Number:"))
      list1.append(x)
      
##a. Find the maximum and minimum number

list1.sort()
print("Maximum Number:",list1[-1])
print("Minimum Number:",list1[0])

##b. Sort the list in ascending order
print("Sorting in ascending order:",list1)

##c. Remove duplicate elements

print("List without duplicate elements:",list(set(list1)))
