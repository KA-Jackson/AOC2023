import math

def get_game_max_per_colour(game_string):
    game_maxes = {'red':0, 'green':0, 'blue':0}
    grabs = game_string.split(';')
    for grab in grabs:
        picks = grab.split(',')
        for pick in picks:
            cube_count = int(pick.split()[0])
            colour = pick.split()[1]
            game_maxes[colour] = max(game_maxes[colour], cube_count)
    return game_maxes

def score_possible(game_maxes, allowed_maxes, game_number):
    possible = True
    for colour in game_maxes.keys():
        if game_maxes[colour] > allowed_maxes[colour]: possible = False
    return game_number if possible else 0

def score_power(game_maxes, allowed_maxes, game_number):
    return math.prod(game_maxes.values())

def day02(score_algo):
    allowed_maxes = {'red':12, 'green':13, 'blue':14}
    result = 0
    with open('day02.txt') as f:
        for line in f.readlines():
            line_parts = line.split(':')
            game_number = int(line_parts[0].split()[1])
            game_maxes = get_game_max_per_colour(line_parts[1])
            result += score_algo(game_maxes, allowed_maxes, game_number)
    return result    

print(day02(score_possible))
print(day02(score_power))