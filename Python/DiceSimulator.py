import random 
a = "y"
while a == "y": 
	rn = random.randint(1,6) 
	
	if rn == 1: 
		print("[ 0 ]")

	if rn == 2: 
		print("[ 0 ]") 
		print("[ 0 ]") 

	if rn == 3: 
		print("[0 0 0]") 

	if rn == 4: 
		print("[0 0]") 
		print("[0 0]") 

	if rn == 5: 
		print("[0 0]") 
		print("[ 0 ]") 
		print("[0 0]") 
	
	if rn == 6: 
		print("[0 0 0]") 
		print("[0 0 0]") 

	a=input("Enter y to roll the dice again and n to exit: ") 
	print("\n") 

