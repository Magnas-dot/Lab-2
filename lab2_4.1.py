#Write a program to simulate a basic stack and queue using a list. Provide options to push, pop (stack), enqueue, and dequeue (queue).

stack=[]
while True:
  print("   ------------------")
  st=input('''  | 1:To push stack  | 
  | 2:To pop stack   | 
  | 3:Display stack  | 
  | 4:Exit           |
   ------------------
  ''')
  if(st=='1'):
    x=input("Enter element: ")
    stack.append(x)
    print("Stack pushed successfully...")
    
  elif(st=='2'):
    if(len(stack)==0):
        print("Empty stack!!")
        continue
    else:
        print("deleted element is:",stack.pop(0))
  elif(st=='3'):
      print(stack)
  elif(st=='4'):
    break
  else:
    print("Enter a valid number...")

        
