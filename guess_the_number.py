import random
refuse_anther_game = False
while True:
    computer_number = random.randint(1, 100)

    you_are_winner = False
    tries = 8
    while tries:
        tries -= 1
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
            you_are_winner = True
            break
        if player_input > computer_number:
            print('Too high!')
        else:
            print('Too low!')
    if not you_are_winner:
        print('You need more practice!')
    while True:
        if input('Do you wanna another game?(Y/N)') == 'Y':
            break
        elif input('Do you wanna another game?(Y/N)') == 'N':
            refuse_anther_game = True
            break
    if refuse_anther_game:
        break
        

