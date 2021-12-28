def accept_pos_int(prompt):
  while True: 
    try:
      val = int(input(prompt))
      if val >= 1:
        return int(val)
      else:
        raise ValueError
    except ValueError:
      print('Invalid input - please enter a positive integer')


def main():
  import random
  num_players = accept_pos_int('How many players? ')
  player_names = []
  player_scores = []
  for i in range(0, num_players):
    player_names.append(input(f'Enter the name of player {i + 1}: '))
    player_scores.append([])

  num_dice = accept_pos_int('How many dice would you like to roll? ')
  dice_size = accept_pos_int('How many sides are the dice? ')
  num_rounds = accept_pos_int('How many turns does each player get? ')

  for i in range(num_rounds):
    print(f'ROUND {i+1}:')

    for j in range(0, num_players):
      print(f"{player_names[j]}'s turn: ")

      dice_sum = 0
      for k in range(0, num_dice):
        roll = random.randint(1,dice_size)
        if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
        else:
          print(f'You rolled a {roll}')
        dice_sum += roll
      print(f'You have rolled a total of {dice_sum}\n')
      player_scores[j].append(dice_sum)

  for i in range(0, num_players):
    scores = str(player_scores[i])
    print(f"{player_names[i]}'s scores: {scores[1:-1]}")
  # Another way:
    # scores = ', '.join(map(str, player_scores[i])) #join function cannot take integers
    # print(f"{player_names[i]}'s scores: {scores}")

if __name__== "__main__":
  main()