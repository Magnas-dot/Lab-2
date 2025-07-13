##5. Write a Python function that accepts a list and returns a new list containing only the
##elements at even indexes and those that are prime numbers.


def pyfunct():
  n=int(input("Enter Number of elements:"))
  list1=[]
  even_prime_list=[]
  for i in range(0,n):
        x=int(input("Enter element:"))
        list1.append(x)
        
  even_indices=range(0,len(list1),2)

  for index in even_indices:
        count=0
        num=list1[index]
        for i in range(1,num+1):
           if(num%i==0):
            count+=1
            
        if(count==2):
            even_prime_list.append(num)
  return(even_prime_list)
print(pyfunct())
