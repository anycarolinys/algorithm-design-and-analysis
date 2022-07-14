class Member:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.discrepancy = 0

class Movie:
    def __init__(self, code, name, rank):
        self.code = code
        self.name = name
        self.rank = rank