class Participant:
    def __init__(self, n, p):
        self.__name = n
        self.__point = p

    def __repr__(self):
        return "%s-%d"%(self.__name, self.__point)

    @property
    def name(self):
        return self.__name

    @property
    def point(self):
        return int(self.__point)

    def __lt__(self, other):
        if self.point < other.point:
            return True

    def __add__(self, other):
        return "%s-%d"%(self.__name, self.__point) + other

    def isname(self, other):
        if self.name == other:
            return True
