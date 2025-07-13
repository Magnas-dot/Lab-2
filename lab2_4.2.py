#4 Write a program to simulate a basic stack and queue using a list.
#Provide options to push, pop (stack), enqueue, and dequeue (queue).

queue=[]
while True:
  print("   ------------------")
  st=input('''  | 1:To enquee      | 
  | 2:To dequeue     | 
  | 3:Display queue  | 
  | 4:Exit           |
   ------------------
  ''')
  if(st=='1'):
    x=input("Enter element: ")
    queue.append(x)
    print("element enquequed successfully...")
    
  elif(st=='2'):
    if(len(queue)==0):
        print("Empty queue!!")
        continue
    else:
        print("deleted element is:",queue.pop(0))
  elif(st=='3'):
      print(queue)
  elif(st=='4'):
    break
  else:
    print("Enter a valid number...")

        
