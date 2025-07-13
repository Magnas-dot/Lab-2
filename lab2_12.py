##12. Create a dictionary to store student names as keys and their scores in three subjects as
##values (in a list). Write functions to:
##a. Display the average marks of each student
##b. Find the topper
##c. Update the marks of a student

student={}
n=int(input("Enter how many data you want?: "))
for i in range(n):
    print(f"-----Data:{i+1}-----")
    name=input(f"Enter name : ")
    score=[]
    for j in range(3):
        x=float(input(f"Enter score in subject {j+1}: "))
        score.append(x)
    student[name]=score

def display_average(student):
    print("-----Average Marks-----")
    for name,marks in student.items():
        avg=sum(marks)/len(marks)
        print(f"{name}:{avg:.2f}")
    

def display_topper(student):  
    highest=0
    topper=''
    for name,marks in student.items():
        avg=sum(marks)/len(marks)
        if avg>highest:
            highest=avg
            topper=name
    print(f"Topper:{topper} with average {highest:.2f}")

def display_update(student):
    update_name=input("Enter name of student to update marks: ")
    if update_name in student:
        new_score=[]
        for i in range(3):
            score=float(input(f"Enter new score for subject {i+1}:"))
            new_score.append(score)
        student[update_name]=new_score
        print(f"Marks updated for student {update_name}.")
    else:
        print("student not found")

display_average(student)
display_topper(student)
display_update(student)

print("Updated dictionary:",student)

        

    
    
