##7.Write a program that receives a list of tuples representing (x, y) coordinates. Determine
##whether the points form a straight line.

points=[]
n=int(input("How many coordinates to enter?: "))
for i in range(0,n):
    x=int(input(f"Enter x{i+1}:"))
    y=int(input(f"Enter y{i+1}:"))
    points.append((x,y))
x1,y1=points[0]
x2,y2=points[1]
dx1=x2-x1
dy1=y2-y1

straight=True
for i in range(2,n):
    x,y=points[i]
    dx2=x-x1
    dy2=y-y1

    if dy2*dx1 != dy1*dx2:
        straight=False
        break

if straight:
    print("the given points forms a straight line")
else:
    print("the given points doesnt form a straight line")

