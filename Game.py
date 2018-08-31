from Universe import Universe

class Game:
    def __init__(self,initial_configuration=0,dimension=8):
        self.dimension = dimension
        self.initial_configuration = initial_configuration
        self.universe = Universe(initial_configuration,dimension)

    def print_nicely(self):
        self.universe.print_nicely()

    def play(self):
        keep_going = True

        while(keep_going):
            choice = input('>')
            if choice != 0:
                self.universe.progress_one_generation()
                self.universe.print_nicely()
            else:
                keep_going = False

