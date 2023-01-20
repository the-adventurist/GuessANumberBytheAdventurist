import random
refuse_anther_game = False

while True:
    score = 0
    level = 1


    you_are_winner = False
    tries = 8
    print('Your start level is 1!')
    while tries:
        computer_number = random.randint(1, level * 100)
        tries -= 1
        player_input = input(f'Guess the number (1 - {level * 100}): ')
        if not player_input.isdigit():
            print('Invalid input. Try again...')
            continue
        player_input = int(player_input)
        if player_input == computer_number:
            print('You guess it!')
            level += 1
            print(f'You turn up to the next level => Your current level is {level}!')
            score += 10
            tries = 8
            print(f'Your score is: {score}')
            print(f'You have {tries} tries more!')
        if player_input > computer_number:
            print('Too high!')
            print(f'You have {tries} tries more!')
            score -= 2
            if score < 0:
                score = 0
            print(f'Your score is: {score}')
        else:
            print('Too low!')
            print(f'You have {tries} tries more!')
            score -= 2
            if score < 0:
                score = 0
            print(f'Your score is: {score}')
    if not tries:
        print('You need more practice!')
        while True:
            if input('Do you wanna another game?(Y/N)') == 'Y':
                break
            elif input('Do you wanna another game?(Y/N)') == 'N':
                refuse_anther_game = True
                break
        break
    if level == 21:
        print('The game is over. You are the WINNER!')
        break
    while True:
        if input('Do you wanna another game?(Y/N)') == 'Y':
            break
        elif input('Do you wanna another game?(Y/N)') == 'N':
            refuse_anther_game = True
            break
    if refuse_anther_game:
        break


