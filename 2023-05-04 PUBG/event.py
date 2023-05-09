import random

MAX_LOCATION = 100


def get_random_location():
    return random.randint(0, MAX_LOCATION)


# 기능 추가 2
def battle(player_list):
    length = len(player_list)
    winner = random.randint(0, length - 1)
    player_list[winner].health += 10
    for i in range(length):
        if i != winner:
            player_list[i].health = 0

    print(f'Battle occurred: Players {[p.id for p in player_list]} at {player_list[0].location}')
    print(f'Player {player_list[winner].id} won')
