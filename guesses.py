game_on = 'yes'
guesses = [0]
num = pick_number()

print_welcome()

while game_on == 'yes':
    
    guesses.append(get_inputs())
    game_on = check_guess(guesses,num)
    
print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)-1} GUESSES!!')

def print_welcome():
    
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")
    

def pick_number():
    
    import random

    return random.randint(1,100)
    
    
def get_inputs():
    
    input_guess = input("What is your guess? ")
    
    while input_guess.isdigit() == False or int(input_guess) not in range(0,101):
        input_guess = input("please enter a valid number: ")
        
    guess = int(input_guess)
    
    return guess
    

def check_guess(guesses,num):
    
    if guesses[-1] == num:
        return 'finished'
        
    if guesses[-2]:  
        if abs(num-guesses[-1]) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guesses[-1]) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    
    return 'yes'