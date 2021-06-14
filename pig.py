#!/usr/bin/env python3
""" Pig game written in Python. """

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

import random
import time

def die_roll():
    """ Rolls the die """
    return random.randint(1, 6)

def error():
    print('Invalid input, try again.')

def start_turn(player):
    """ Players turn process """
    if player.computer:
        print('Press the Enter key to roll.')
        time.sleep(2)
    else:
        input('Press the Enter key to roll.')
    player.turn_roll = die_roll()
    current_points = 0
    num_of_rolls = 0
    pass_die = False

    while player.turn_roll != 1 and not pass_die and not player.winner:
        print('You rolled a {}\n'.format(player.turn_roll))
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
            if player.computer:
                print('Do you wish to roll again? (y/n)')
                time.sleep(2)
                if current_points < 20:
                    player.turn_roll = die_roll()
                else:
                    player.scoreboard = player.scoreboard + current_points
                    pass_die = True
            else:
                while answer != 'y' and answer != 'n':
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

class Player:
    """ Child class of Player class for human. """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, name, computer):
        self.name = name
        self.scoreboard = 0
        self.turn_roll = 0
        self.computer = computer
        self.winner = False

    @property
    def name(self):
        """ Get name """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name """
        self._name = value

    @property
    def scoreboard(self):
        """ Get scoreboard """
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, value):
        """ Set scoreboard """
        self._scoreboard = value

    @property
    def turn_roll(self):
        """ Get turn_roll """
        return self._turn_roll

    @turn_roll.setter
    def turn_roll(self, value):
        """ Set turn_roll """
        self._turn_roll = value

    @property
    def winner(self):
        """ Get winner """
        return self._winner

    @winner.setter
    def winner(self, value):
        """ Set winner """
        self._winner = value

    def __repr__(self):
        return f'{self.name}: {self.scoreboard}'

def main():
    """ Main function for game. """
    num_of_players = 0
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(input('How many players (2-4)?: '))
        if num_of_players < 2 or num_of_players > 4:
            error()

    # Initializing players
    players = []
    if num_of_players == 2:
        players.append(Player(input('\nEnter your name: '), False))
        players.append(Player('CPU', True))
    else:
        for i in range(0, num_of_players):
            players.append(Player(
                input('\nPlayer {} enter your name: '.format(i + 1)), False))

    # Creating turn order
    turn_order = []
    for i in range(0, num_of_players):
        if players[i].computer:
            print('CPU press Enter key to roll for turn order.')
            time.sleep(2)
        else:
            input('\n{} press Enter key to roll for turn order.'.format(players[i].name))
        players[i].turn_roll = die_roll()
        time.sleep(1)
        print("You rolled a {}.".format(players[i].turn_roll))

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
