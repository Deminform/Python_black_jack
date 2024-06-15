
import art
import random
art.print_centered(art.logo)

is_game_on = True
my_wins = 0
pc_wins = 0
draw = 0

def games_result():
    print(f'My wins = {my_wins}\nPC wins = {pc_wins}\nDraw = {draw}')


def take_card(dict: dict):
    keys = list(cards_list.keys())
    random_card = random.choice(keys)
    dict[random_card] = cards_list.pop(random_card)

def calculate_card(dict: dict):
    points = 0
    aces = 0
    for key, value in dict.items():
        points += value
        if key == 'A ♠️' and value == 11 or key == 'A ♥️' and value == 11 or key == 'A ♣️' and value == 11 or key == 'A ♦️' and value == 11:
            aces += 1

    while points > 21 and aces > 0:
        if 'A ♠️' in dict.keys() and dict['A ♠️'] == 11:
            dict['A ♠️'] = 1
            points -= 10
        elif 'A ♥️' in dict.keys() and dict['A ♥️'] == 11:
            dict['A ♥️'] = 1
            points -= 10
        elif 'A ♦️' in dict.keys() and dict['A ♦️'] == 11:
            dict['A ♦️'] = 1
            points -= 10
        elif 'A ♣️' in dict.keys() and dict['A ♣️'] == 11:
            dict['A ♣️'] = 1
            points -= 10
        aces -= 1

    return points

def winner_is(my_wins, draw, pc_wins):
    if (pc_points > 21 and my_points < 22) or \
    (pc_points < 22 and my_points < 22 and my_points > pc_points):
        print(f'\nYour cards is: {list(my_cards.keys())} = {my_points}')
        print(f'Dealer cards is: {list(pc_cards.keys())} = {pc_points}')
        print('*-*-*-*-*-*-*-* You Win! *-*-*-*-*-*-*-*\n')
        my_wins += 1
    elif pc_points < 22 and my_points < 22 and my_points == pc_points:
        print(f'\nYour cards is: {list(my_cards.keys())} = {my_points}')
        print(f'Dealer cards is: {list(pc_cards.keys())} = {pc_points}')
        print('*-*-*-*-*-*-*-* Draw *-*-*-*-*-*-*-*\n')
        draw += 1
    else:
        print(f'\nYour cards is: {list(my_cards.keys())} = {my_points}')
        print(f'Dealer cards is: {list(pc_cards.keys())} = {pc_points}')
        print('*-*-*-*-*-*-*-* Dealer Win *-*-*-*-*-*-*-*\n')
        pc_wins += 1
    return [my_wins, draw, pc_wins]

while is_game_on:
    cards_list = {
    '2 ♠️': 2, '2 ♥️': 2, '2 ♦️': 2, '2 ♣️': 2,
    '3 ♠️': 3, '3 ♥️': 3, '3 ♦️': 3, '3 ♣️': 3,
    '4 ♠️': 4, '4 ♥️': 4, '4 ♦️': 4, '4 ♣️': 4,
    '5 ♠️': 5, '5 ♥️': 5, '5 ♦️': 5, '5 ♣️': 5,
    '6 ♠️': 6, '6 ♥️': 6, '6 ♦️': 6, '6 ♣️': 6,
    '7 ♠️': 7, '7 ♥️': 7, '7 ♦️': 7, '7 ♣️': 7,
    '8 ♠️': 8, '8 ♥️': 8, '8 ♦️': 8, '8 ♣️': 8,
    '9 ♠️': 9, '9 ♥️': 9, '9 ♦️': 9, '9 ♣️': 9,
    '10 ♠️': 10, '10 ♥️': 10, '10 ♦️': 10, '10 ♣️': 10,
    'J ♠️': 10, 'J ♥️': 10, 'J ♦️': 10, 'J ♣️': 10,
    'Q ♠️': 10, 'Q ♥️': 10, 'Q ♦️': 10, 'Q ♣️': 10,
    'K ♠️': 10, 'K ♥️': 10, 'K ♦️': 10, 'K ♣️': 10,
    'A ♠️': 11, 'A ♥️': 11, 'A ♦️': 11, 'A ♣️': 11
}
    my_cards = {}
    my_points = 0
    pc_cards = {}
    pc_points = 0

    take_card(my_cards)
    take_card(my_cards)
    take_card(pc_cards)
    my_points = calculate_card(my_cards)
    pc_points = calculate_card(pc_cards)

    while my_points < 22 and my_points != 21:
        print(f'\n\n{list(my_cards.keys())} = {my_points}')
        print(f'{list(pc_cards.keys())} = {pc_points}')

        one_more_card = input('Type "y" to get another card, type "n" to pass: ').lower()
        if one_more_card == 'y':
            take_card(my_cards)
            my_points = calculate_card(my_cards)
        elif one_more_card == 'n':
            break
        else:
            print('Wrong answer, please type "y" to get another card, type "n" to pass: ')
            continue
        print(f'{list(my_cards.keys())} = {my_points}')

    while pc_points < 17 and my_points < 22 and pc_points != 21:
        take_card(pc_cards)
        pc_points = calculate_card(pc_cards)
        print(f'{list(pc_cards.keys())} = {pc_points}')

    result = list(winner_is(my_wins, draw, pc_wins))
    my_wins = result[0]
    draw = result[1]
    pc_wins = result[2]

    one_more_game = None
    while one_more_game != 'y' or one_more_game != 'n':
        one_more_game = input('\nOne more game? type "y", type "n" to end or "stat" to show statistics: ').lower()
        if one_more_game == 'n':
            is_game_on = False
            break
        elif one_more_game == 'y':
            break
        elif one_more_game == 'stat':
            games_result()
            continue
        else:
            print('Wrong answer, please type "y" for new game and "n" for end ')
            continue