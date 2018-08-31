from Cell import Cell
from Configurations import Configurations
class Universe:
    def __init__(self,initial_state=0,dimension=8):
        self.dimension = dimension
        self.initial_state = initial_state
        self.available_configurations = Configurations()
        self.universe_space = self.alloc_universe()


    def alloc_universe(self):
        array_structure = [[0 for x in range(self.dimension)] for y in range(self.dimension)]
        for x in range(self.dimension):
            array_structure[x] = [Cell(x, y, False) for y in range(self.dimension)]
        if self.initial_state == 0 and self.dimension == 8 :
            initial_configuration = self.available_configurations.getTestConfiguration()
            for couple in initial_configuration:
                x = couple[0]
                y = couple[1]
                array_structure[x][y]=Cell(x,y,True)
        else:
            raise ValueError('initial state = 0 and dimension = 8 not respected')

        return array_structure

    def print_nicely(self):
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.universe_space[x][y].status == True:
                    if (y != self.dimension -1):
                        print("1",end='')
                    else:
                        print("1")
                else:
                    if (y != self.dimension -1):
                        print("0",end='')
                    else:
                        print("0")


    def progress_one_generation(self):
        targets = self.target_actions_on_cells_in_next_generation()
        to_kill = targets['kill']
        to_spawn = targets['spawn']
        for item in to_kill:
            self.universe_space[item['x']][item['y']].set_cell_dead()
        for item in to_spawn:
            self.universe_space[item['x']][item['y']].set_cell_alive()


    def target_actions_on_cells_in_next_generation(self):
        to_kill_in_next_generation = []
        to_spawn_in_next_generation = []
        for x in range(self.dimension):
            for y in range(self.dimension):
                neighbours_count = self.count_cell_neighbours(x, y)
                if self.cell_is_empty(x,y):
                    if neighbours_count == 3:
                        to_spawn_in_next_generation.append({'x': x, 'y': y})
                if neighbours_count <= 1 or neighbours_count > 3:
                    to_kill_in_next_generation.append({'x':x,'y':y})
        return {'kill': to_kill_in_next_generation,'spawn': to_spawn_in_next_generation}



    def cell_is_empty(self,x,y):
        return self.universe_space[x][y].status == False

    def count_cell_neighbours(self,x,y):
        possible_neighbours = self.neighbours_cohordinates(x,y)
        cell_neighbours = 0
        for i in possible_neighbours:
            if self.universe_space[i[0]][i[1]].status == True:
                cell_neighbours = cell_neighbours + 1
        return cell_neighbours




    def neighbours_cohordinates(self,x,y):
        # step 1: all of possible arithmethic neighbours
        neighbours = []

        #upper row neighbours
        neighbours.append([x-1,y-1])
        neighbours.append([x-1,y])
        neighbours.append([x-1,y+1])

        #same row neighbours
        neighbours.append([x, y - 1])
        neighbours.append([x, y + 1])

        #lower row neighbours
        neighbours.append([x + 1, y - 1])
        neighbours.append([x + 1, y])
        neighbours.append([x + 1, y + 1])

        # get only non negative and non overflowing cohordinates
        neighbours = filter(lambda xx: 0 <= xx[0] and xx[0] <= self.dimension-1 and 0<=xx[1] and xx[1]<=self.dimension-1,neighbours)
        return neighbours