##8. Write a program to input two sets of student roll numbers: one who play cricket and 
##another who play football. Find: 
##a. Students who play both sports 
##b. Students who play only one sport 
##c. Students who play neither (given a master list of all students)

master = input("Enter roll numbers of all students (comma-separated): ")
master = set(master.replace(" ", "").split(','))

cricket_input = input("Enter roll numbers of students who play cricket: ")
cricket_players = set(cricket_input.replace(" ", "").split(','))

football_input = input("Enter roll numbers of students who play football: ")
football_players = set(football_input.replace(" ", "").split(','))

#a. Students who play both cricket and football (intersection)
both_sports = cricket_players & football_players

# b. Students who play only one sport (symmetric difference)
only_one_sport = cricket_players ^ football_players

# c. Students who play neither (students in all_students but not in cricket or football)
neither = master - (cricket_players | football_players)

# Print the results
print("\n--- Results ---")
print("Students who play both cricket and football:", both_sports)
print("Students who play only one sport:", only_one_sport)
print("Students who play neither sport:", neither)
