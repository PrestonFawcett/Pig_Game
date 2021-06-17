#!/usr/bin/env python3
""" Pig game written in Python. """

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

import time
from player import Player
from functions import error
from functions import rearrange
from functions import start_turn

def main():
    """ Main function for game. """
    # Asking how many players
    num_of_players = 0
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(input('How many players (2-4)?: '))
        if num_of_players < 2 or num_of_players > 4:
            error()

    # Initializing players
    players = []
    if num_of_players == 2:
        answer = input('Is player 2 a computer? (y/n): ')
        players.append(Player(input('\nEnter your name: '), False))
        if answer == 'y':
            players.append(Player('John Scarne', True))
        else:
            players.append(Player(input('\nEnter your name: '), False))
    else:
        for i in range(0, num_of_players):
            players.append(Player(
                input('\nPlayer {} enter your name: '.format(i + 1)), False))

    # Creating turn order
    turn_order = rearrange(players)

    print('\n------Turn Order------')
    for i in range(0, num_of_players):
        print('{}. {}'.format((i + 1), turn_order[i].name))

    # Start Pig game
    current = 0
    while not turn_order[current].winner:
        print('\n*******SCOREBOARD*******')
        for i in range(0, num_of_players):
            print(turn_order[i])
        print('************************')

        print('\n{}\'s turn.'.format(turn_order[current].name))
        time.sleep(1)
        start_turn(turn_order[current])
        if not turn_order[current].winner:
            current = (current + 1) % num_of_players

    print('{} wins!'.format(turn_order[current].name))

if __name__ == '__main__':
    main()
