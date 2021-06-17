""" File for the Player class """
class Player:
    """ Holds name, total score, current roll,
    and booleans for if computer and if winner """
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
