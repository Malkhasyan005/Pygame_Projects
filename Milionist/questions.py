class Question:
    def __init__(self, q, c, a2, a3, a4, b):
        self.__question = q
        self.__corrans = c
        self.__answ2 = a2
        self.__answ3 = a3
        self.__answ4 = a4
        self.__bonus = b

    def __repr__(self):
        pass

    @property
    def corrans(self):
        return self.__corrans

    @property
    def bonus(self):
        return self.__bonus

    @property
    def question(self):
        return self.__question

    @property
    def answ2(self):
        return self.__answ2

    @property
    def answ3(self):
        return self.__answ3

    @property
    def answ4(self):
        return self.__answ4
