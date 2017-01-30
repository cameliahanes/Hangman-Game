class GameOver(Exception):
    pass


class OverUser(Exception):
    pass


class GameState():
    def __init__(self, sentence, trials, state):
        self.__sentence = sentence
        self.__trials = trials
        self.__state = state

    @property
    def trials(self):
        return self.__trials

    @property
    def state(self):
        return self.__state

    @property
    def sentence(self):
        return self.__sentence

    def __str__(self):
        return "{} {} {}".format(self.__sentence, self.__trials, self.__state)


class Game(object):
    def __init__(self, sentence):
        """"
        class to define a game state
        """
        self.__sentence = sentence
        self.__displayable = sentence.displayable
        self.__trials = 7
        self.__solved = False

    @property
    def trials(self):
        return self.__trials

    def play(self, letter):
        """"
        ===The game===
        :param the letter given by the user
        :returns the sentence, the number of trials remaining and
        the state of the game
        0 - correct; -1 - no more possible trials(failed game)
        1 - incorrect; 2 - end
        """
        if self.__solved is True:
            raise GameOver("Game is over already!")
        if self.__trials is 0:
            raise OverUser("You failed!")
        if letter in self.__displayable['letters']:
            for i in self.__displayable['letters'][letter]:
                self.__displayable['solvable'][i] = letter
            if '_' not in self.__displayable['solvable']:
                self.__solved = True
                return GameState(self.__displayable['solvable'], self.__trials, 2)
            return GameState(self.__displayable['solvable'], self.__trials, 0)
        else:
            self.__trials -= 1
            if self.__trials is 0:
                return GameState(self.__displayable['solvable'], self.__trials, -1)
            else:
                return GameState(self.__displayable['solvable'], self.__trials, 1)

    def get_sentence(self):
        return self.__displayable['solvable']



class HangmanController:
    def __init__(self, repo):
        self.__repository = repo

    def start_new_game(self):
        sentence = self.__repository.get_random()[0]
        return Game(sentence)

    def add_sentence(self, sentence: str):
        self.__repository.add_sentence(sentence)

    def save(self):
        self.__repository.save_repository()