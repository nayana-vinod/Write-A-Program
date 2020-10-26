import random 
print("\n ***Welcome to Halloween Special Jumbled Words Game!!!***\n")
def choose(): 
	words = ['halloween', 'spooky', 'scary', 'vampires', 
			'blood', 'witch', 'ghosts', 'zombies', 
			'cannibal', 'monsters', 'tricks'] 
	pick = random.choice(words) 
	return pick 

def jumble(word): 
	random_word = random.sample(word, len(word)) 
	jumbled = ''.join(random_word) 
	return jumbled 

def thank(p1n, p2n, p1, p2): 
	print(p1n, 'Your score is :', p1) 
	print(p2n, 'Your score is :', p2) 

	check_win(p1n, p2n, p1, p2) 

	print('\n***Thank you for playing!!! Happy Halloween!!!***\n') 

def check_win(player1, player2, p1score, p2score): 
	if p1score > p2score: 
		print("The winner is:", player1,". Congratulations!\n") 
	elif p2score > p1score: 
		print("The winner is:", player2,". Congratulations!\n") 
	else: 
		print("It is a tie! Congratulations to both ",player1," and ",player2) 

def play(): 
	p1name = input("Please enter Player 1 name: ") 
	p2name = input("Please enter Player 2 name: ") 
	pp1 = 0
	pp2 = 0
	turn = 0
	while True: 
		picked_word = choose() 
		qn = jumble(picked_word) 
		print("Jumbled word is:", qn) 
		if turn % 2 == 0: 
			print(p1name, 'Your Turn.') 

			ans = input("Guess the word!\n") 

			if ans == picked_word: 
				pp1 += 1

				print('Your score is:', pp1) 
				turn += 1

			else: 
				print("Oops! Better luck next time!") 

				print(p2name, 'Your turn.') 

				ans = input('Guess the Word!\n') 

				if ans == picked_word: 
					pp2 += 1
					print("Your Score is:", pp2) 

				else: 
					print("Oops! Better luck next time! Answer is :", picked_word) 

				c = int(input("Enter 1 to continue and 0 to exit:")) 
				if c == 0: 
					thank(p1name, p2name, pp1, pp2) 
					break
		else: 
 
			print(p2name, 'Your turn.') 
			ans = input('Guess the Word!\n') 

			if ans == picked_word: 
				pp2 += 1
				print("Your Score is:", pp2) 
				turn += 1

			else: 
				print("Oops! Better luck next time!") 
				print(p1name, 'Your turn.') 
				ans = input('Guess the Word!\n') 

				if ans == picked_word: 
					pp1 += 1
					print("Your Score is:", pp1) 

				else: 
					print("Oops! Better luck next time! Answer is: ", picked_word) 

					c = int(input("Enter 1 to continue and 0 to Exit: ")) 

					if c == 0: 
						thank(p1name, p2name, pp1, pp2) 
						break

			c = int(input("Enter 1 to continue and 0 to Exit: ")) 
			if c == 0: 
				thank(p1name, p2name, pp1, pp2) 
				break

if __name__ == '__main__': 
	play() 
