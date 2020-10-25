import random 
print("Rules: \n" +"Stone vs Paper; Paper wins \n" + "Stone vs Scissors; Stone wins \n" +"Paper vs Scissors; Scissors wins \n") 

while True: 
	print("Enter choice \n 1. Stone \n 2. Paper \n 3. Scissors \n") 
	choice = int(input("Enter your choice: ")) 
	while choice > 3 or choice < 1: 
		choice = int(input("Please enter a valid input: ")) 
	if choice == 1: 
		choice_name = 'Stone'
	elif choice == 2: 
		choice_name = 'Paper'
	else: 
		choice_name = 'Scissors'
	print("The user chose: " + choice_name) 
	print("\nNow the computer's choice will be seen.......") 
	comp_choice = random.randint(1, 3) 
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 
	if comp_choice == 1: 
		comp_choice_name = 'Stone'
	elif comp_choice == 2: 
		comp_choice_name = 'Paper'
	else: 
		comp_choice_name = 'Scissors'
	print("The computer chose: " + comp_choice_name) 
	print(" ")
	print(choice_name + " V/s " + comp_choice_name) 

	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )): 
		print("\n Paper wins!", end = "") 
		result = "Paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)): 
		print("\n Stone wins!", end = "") 
		result = "Stone"
	else: 
		print("\n Scissors wins!", end = "") 
		result = "Scissors"

	if result == choice_name: 
		print("\n ***User wins!!!*** \n") 
	else: 
		print("\n ***Computer wins!!!*** \n") 
		
	print("Do you want to play again? (Y/N)") 
	ans = input() 

	if ans == 'n' or ans == 'N': 
		break

print("\n ***Thanks for playing*** \n") 
