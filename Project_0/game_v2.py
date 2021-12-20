"""Game - Guess a number(Computer only)"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Random guessing a number

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Attempts number
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101) # Suppouse number
        if number == predict_number:
            break # Game over
    return(count)

def score_game(random_predict) -> int:
    """Average attempts number

    Args:
        random_predict ([type]): Guess function

    Returns:
        int: Average attempts number
    """

    count_list = []
    np.random.seed(1) # reproduction fixation 
    random_array = np.random.randint(1, 101, size=(1000)) # Guess a number list

    for number in random_array:
        count_list.append(random_predict(number))

    score = int(np.mean(count_list))
    print(f'Your algorithm guesses a number by {score} attempts, on average.')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)