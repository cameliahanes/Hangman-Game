from collections import deque
from random import sample

from src.Domain.Sentence import Sentence


class Repository:
    def __init__(self, load_from_file=True):
        self.__list = deque()
        if load_from_file:
            self.load_repository()

    def get_all(self):
        return self.__list

    def get_random(self):
        """"
        function to get a random sentence from the repository file
        :return thr sentence
        """
        return sample(self.__list, 1)

    def add_sentence(self, sentence):
        """"
        function to add a new sentence in the repository
        :param sentence the entity to be added
        """
        if len(sentence) < 4:
            raise ValueError("Sentence too short!")
        for w in sentence.split(" "):
            if len(w) < 3:
                raise ValueError("Word '{}' from the sentence has len {}, at least 3 expected.".\
                                 format(w, len(w)))
        sente = Sentence(sentence)
        if sente in self.__list:
            raise ValueError("Sentence already in list...")
        self.__list.append(sente)

    def load_repository(self):
        with open("intrebari.txt", "r") as f:
            for line in f.read().splitlines():
                self.__list.append(Sentence(line))

    def save_repository(self):
        with open("sentences.txt", "w") as f:
            for elem in self.__list:
                f.write(elem.sentence + "\n")