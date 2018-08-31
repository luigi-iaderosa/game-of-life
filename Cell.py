class Cell:
    def __init__(self,cell_x_cohordinate,cell_y_coordinate,status):
        self.status = status # the only two states allowed for the cell: True (cell alive), False (cell dead)
        self.x = cell_x_cohordinate
        self.y = cell_y_coordinate
    def set_cell_dead (self):
        self.status = False

    def set_cell_alive (self):
        self.status = True



