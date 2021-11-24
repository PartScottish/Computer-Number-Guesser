"""
Lab ex02
"""


def computer_guess(your_number):
    min_guess = 1
    max_guess = 100
    guess = (-1) #-1 is used here to force the program into the loop.
    count = 1
    while guess != your_number:
        guess = (min_guess + max_guess)//2 #first guess will always be 50(or half way between range), making the program as short as possible.
        bigger_smaller = input(f"Is your number greater (>), equal to (=) or less than (<) {guess}? \nPlease use '<', '=' or '>' ") 
        if bigger_smaller == '<' or bigger_smaller == '=' or bigger_smaller == '>': #forcing the use of only the symbols we want.
            userislying = False        
            if your_number < guess and bigger_smaller != '<':
                userislying = True
            if your_number > guess and bigger_smaller != '>':
                userislying = True
            if your_number == guess and bigger_smaller != '=':
                userislying = True
            if userislying: #The above IF statements do work in a long OR argument and whilst it's less repetetive it's far less presentable. This is easier to debug/change.
                print("I think you're lying")
                continue
            count = count + 1 #because this will loop is entered per guess this will add +1 to the count per attempt

            if bigger_smaller == '<': 
                max_guess = guess - 1                    
            elif bigger_smaller == '>':
                min_guess = guess + 1
        else:
            continue #returns to the above while loop for the next guess and/or to check the conditions to continue or finish the game.

    print(f"I have guessed it!\nI needed {count} step(s)!")



def usernumber():
    minimum = 1
    maximum = 100
    user_number = minimum - 1 #-1 is used here to force the program to enter the while loop. The value itself has no effect.
    while user_number < minimum or user_number > maximum:
        try:
            user_number = int(input(f"Think of a number between {minimum} and {maximum}! "))
            if user_number < minimum or user_number > maximum: #forcing entering a number between {minimum},{maximum} range
                print("Your number was out of range")
            
        except ValueError:
            print(f"Please use a number between {minimum} and {maximum}") #This ValueError exception prevents the use of strings.
        
    computer_guess(user_number)



usernumber() #this begins the program by calling the function usernumber

   
    
    
    
    
    
    
    
""" 
debugging
islessthan = bigger_smaller == '<'
isequalthan = bigger_smaller == '='
ismorethan = bigger_smaller == '>'
isvalidinput = islessthan or isequalthan or ismorethan
43
"""