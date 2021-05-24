class Bot:
    def __init__ (self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __repr__(self):
        return "Bot(Name: {})".format(self.name)
