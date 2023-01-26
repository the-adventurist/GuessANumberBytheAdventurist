import random
refuse_anther_game = False

while True:
    score = 0
    level = 1

    you_are_winner = False
    tries = 8
    print('Your start level is 1!')
    computer_number = random.randint(1, level * 100)
    while tries:
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
            computer_number = random.randint(1, level * 100)
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

        if not tries or level == 21:
            print('You need more practice!')
            if input('Do you wanna another game?(Y/N)').upper() == 'Y':
                break
            elif input('Do you wanna another game?(Y/N)').upper() == 'N':
                refuse_anther_game = True
                break
    break
# proverka