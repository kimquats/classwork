def is_better_than(player0, player1):
    """
    Simulate a rock, paper, scissors game!

    Paper beats rock, scissors beats paper, rock beats scissors.

    This function only needs to consider strings as input.

    Parameters:

    player0 - a string (either "rock", "paper", or "scissors")
    player1 - a string (either "rock", "paper", or "scissors")

    Returns:
        True if player0 beats player1
        False if player1 beats player0
        None if a tie, or if an invalid string is passed
    """
    first_move = player0
    second_move = player1
    if (first_move == "rock" and second_move == "scissors") or (first_move == "scissors" and second_move == "paper") or (player0 == "paper" and player1 == "rock"):
      return True
    elif (first_move == "scissors" and second_move == "rock") or (first_move == "rock" and second_move == "paper") or (player0 == "paper" and player1 == "scissors"):
      return False
    else:
      return None
#function takes "rock", "paper", or "scissors" as input, 
#returns True if player0 beats player1, False if player1 beats player0,
#None if a tie or an invalid string is passed
#True conditions: 
# - if player0 == 'rock' and player1 == 'scissors'
# - if player0 == 'paper' and player1 == 'rock'
# - if player0 == 'scissors' and player1 == 'paper'
#False conditions:
# - if player0 == 'scissors' and player1 == 'rock',
# - if player0 == 'rock' and player1 == 'paper'
# - if player0 == 'paper' and player1 == 'scissors'
#Tie conditions = else return None
