##6 Write a program to create a tuple of n numbers, then find:
##a. The average of the numbers
##b. The median
##c. The mode (without using libraries)



n=int(input("Enter the value of n: "))
tup=[]
for i in range(0,n):
      x=int(input("Enter the Number: "))
      tup.append(x)

#average
tup=tuple(tup)
sum_tup=sum(tup)
length=len(tup)
average=sum_tup/length
print(f"Average of numbers is:{average:.2f}")

#median
tup=list(tup)
tup.sort()
if(length%2==0):
           median = (tup[length//2 - 1] + tup[length//2]) / 2
else:
    median=tup[length//2]
print("Median:",median)

#Mode
freq={}
for key in tup:
    if key in freq:
        freq[key]+=1
    else:
         count=1
         freq[key]=1
print(freq)
mode=[]
max_value=max(freq.values())
for k,v in freq.items():
    if v==max_value:
        mode.append(k)
print('Mode:',mode)
           
