"""Game - Guess a number(AI)"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Random guess

    Args:
        number (int, optional): Predict number. Defaults to 1.

    Returns:
        int: Attempts number
    """
    top = 101
    bottom = 1
    count = 0

    while True:
        count+=1
        predict = (top+bottom) // 2 # Predict the middle
        
        if predict > number:
            top = predict - 1 # Top border goes down
        elif predict < number:
            bottom = predict + 1  # Bottom border goes up
        elif predict == number:
            break  # Game over 
    return count



def score_game(random_predict) -> int:
    """Get average number of attpemtps for 1000 repetitions of guess function runs

     Args:
        random_predict ([type]): Guess function

    Returns:
        int: Average attempts number
    """
    count_list = [] # list of attempts number
    np.random.seed(1) # fixation seed for reproduction
    random_array = np.random.randint(1, 101, size=(1000)) # Guessed number list

    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list)) # Average number of attempts
    print(f'Your algorithm guesses a number on average per {score} attempts.')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)