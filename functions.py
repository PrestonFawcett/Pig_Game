""" File for all functions used in pig.py """

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

import random
import time

def die_roll():
    """ Rolls the die """
    value = random.randint(1, 6)
    time.sleep(1)
    print('You rolled a {}\n'.format(value))
    return value

def error():
    """ Error message for wrong input """
    print('Invalid input, try again.')

def ai_roll(value):
    """ Computer decision for rolling """
    time.sleep(1)
    if value < 20:
        return 'y'
    return 'n'

def rearrange(players):
    """ Rearrange players based on die roll """
    turn_order = []
    for i in range(0, len(players)):
        if players[i].computer:
            print('\n{} press Enter key to roll for turn order.'.format(
                players[i].name))
            time.sleep(1)
        else:
            input('\n{} press Enter key to roll for turn order.'.format(
                players[i].name))
        players[i].turn_roll = die_roll()
        #time.sleep(1)
        #print("You rolled a {}.".format(players[i].turn_roll))

        if i < 1:
            turn_order.append(players[i])
        else:
            found = False
            for j in range(0, i):
                if players[i].turn_roll >= turn_order[j].turn_roll:
                    turn_order.insert(j, players[i])
                    found = True
                elif j == i - 1:
                    turn_order.append(players[i])
                    found = True
                if found:
                    break
    return turn_order



def start_turn(player):
    """ Players turn process """
    if player.computer:
        print('Press the Enter key to roll.')
        time.sleep(1)
    else:
        input('Press the Enter key to roll.')
    player.turn_roll = die_roll()
    current_points = 0
    num_of_rolls = 0
    pass_die = False

    while player.turn_roll != 1 and not pass_die and not player.winner:
        current_points = current_points + player.turn_roll
        num_of_rolls = num_of_rolls + 1

        if player.scoreboard + current_points >= 100:
            player.winner = True
        else:
            time.sleep(1)
            print('Current turn total points: {}'.format(current_points))
            print('Total score if hold:       {}'.format(
                player.scoreboard + current_points))
            print('Number of rolls:           {}\n'.format(num_of_rolls))

            time.sleep(1)
            answer = ''
            while answer not in ('y', 'n'):
                if player.computer:
                    print('Do you wish to roll again? (y/n)')
                    answer = ai_roll(current_points)
                else:
                    answer = input('Do you wish to roll again? (y/n)')

                if answer == 'y':
                    player.turn_roll = die_roll()
                elif answer == 'n':
                    player.scoreboard = player.scoreboard + current_points
                    pass_die = True
                else:
                    error()

    if player.turn_roll == 1:
        print('You rolled a 1. Next players turn.')
        time.sleep(1)
