"""Game - Guess a number"""

import numpy as np

number = np.random.randint(1,101) # guess a number

# attempts number
count = 0

while True:
    count+=1
    predict_number = int(input("Guess a number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be less!")
        
    elif predict_number < number:
        print("Number should be more!")
    
    else:
        print(f'You have guessed the number! it is {number}! Attepmts number is {count}')
        break # Game over