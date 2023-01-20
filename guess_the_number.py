import random

computer_number = random.randint(1, 100)

while True:
    player_input = input('Guess the number (1 - 100): ')
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue
    player_input = int(player_input)
    if not(1 <= player_input <= 100):
        print('Try again. Enter valid number between 1 and 100...')
        continue
    if player_input == computer_number:
        print('You guess it!')
        break
    if player_input > computer_number:
        print('Too high!')
    else:
        print('Too low!')
