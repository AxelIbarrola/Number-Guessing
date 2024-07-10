def validations_bounds():
    while True: 
        try:
            lower_bound = int(input('Enter the lower bound: '))
            if lower_bound < 0:
                print('You must enter a number greater than 0.')
            else: 
                break
        except ValueError:
            print('You must enter a integer.')
     
    while True:   
        
        try:
            upper_bound = int(input('Enter the upper bound: '))
            
            if upper_bound < 0:
                print('You must enter a number greater than 0.')
            else: 
                break
        except ValueError:
            print('You must enter a integer.')
    
    return lower_bound, upper_bound

def validations_user_number(lower_bound, upper_bound):
    
    while True:
        try:
            user_number = int(input('Enter your number: '))
            if not lower_bound <= user_number <= upper_bound:
                print('your number is out of range')
            else:
                break
        except ValueError:
            print('You must enter a integer.')
            
    return user_number