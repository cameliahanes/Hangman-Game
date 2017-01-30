class Sentence():
    def __init__(self, sentence):
        self.__sentence = sentence

    @property
    def sentence(self):
        return self.__sentence

    @property
    def displayable(self):
        endf = []
        for w in self.__sentence.split():
            if len(w) < 4:
                endf.append(w)
                continue
            w = list(w)
            for i in range(1, len(w) - 1):
                w[i] = '_'
            endf.append("".join(w))
        letters = {}
        i = 0
        for letter in self.__sentence:
            if letter not in letters:
                letters[letter] = [i]
            else:
                letters[letter].append(i)
            i += 1
        return {
            'solvable':list(" ".join(endf)),
            'letters':letters
        }

    def __eq__(self, other):
        if other == None:
            return False
        return self.__sentence == other.sentence

    def __str__(self):
        return self.__sentence