from math import log
from random import randint
from validations import validations_bounds, validations_user_number

print(f'\n{'Welcome to Number Guessing'.center(50, '-')}\n')


            
def logic_of_game():
    
    lower_bound, upper_bound = validations_bounds()
    random_number = randint(lower_bound, upper_bound)
    minimum_number_of_guessing = round(log(upper_bound - lower_bound + 1, 2))
    guesses = 0
    acierto = False
    
    print(f'\nYour number is between {lower_bound}-{upper_bound}')
    print(f'you have {minimum_number_of_guessing} chances to guess the number\n')
    
    
    while guesses < minimum_number_of_guessing:
        
        user_number = validations_user_number(lower_bound=lower_bound, upper_bound=upper_bound)
        
        if user_number > random_number:
            print('Try Again! You guessed too high')
            guesses += 1
            print(f'Total Number of Guesses: {guesses}\n')
            
        elif user_number < random_number:
            print('Try Again! You guessed too small')
            guesses += 1
            print(f'Total Number of Guesses: {guesses}\n')
    
        else:
            acierto = True
            print(f'Congratulations! you did it in {guesses} tries')
            break
    
    
    if not acierto:
        print('Oh, you have not managed to get the minimum number of correct answers expected.')
        print(f'The number was {random_number}')
    
    

logic_of_game()