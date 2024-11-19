# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

winner = {
  "R": "P",
  "P": "S",
  "S": "R"
}

def player(prev_play, opponent_history=[]):
  move = ""

  # Reset history and guess a random option if there is no prev_play
  if not prev_play:
    opponent_history = []
    move = random.choice(["R", "P", "S"])
  elif len(opponent_history) <= 2:
    # Guess a random option if history has < 3 entries
    opponent_history.append(prev_play)
    move = random.choice(["R", "P", "S"])
  elif opponent_history[-1] == opponent_history[-2]:
    # Guess the option that beats the previous one played if the penultimate entry equals the last entry
    opponent_history.append(prev_play)
    move = winner[prev_play]
  elif opponent_history[-1] != opponent_history[-2]:
    # Guess the option that beats the option that beats the last entry if it is not equal
    opponent_history.append(prev_play)
    move = winner[winner[prev_play]]
  else:
    # Catchall that guesses a random option
    opponent_history.append(prev_play)
    move = random.choice(["R", "P", "S"])

  return move
