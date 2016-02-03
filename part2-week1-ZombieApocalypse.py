
"""
Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        num = 0
        while num < self.num_zombies():
            yield self._zombie_list[num]
            num += 1
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        num = 0
        while num<self.num_humans():
            yield self._human_list[num]
            num += 1
        return

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[ self._grid_width * self._grid_height for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        if entity_type == HUMAN:
            boundary = poc_queue.Queue()
            for each in self._human_list:
                visited.set_full(each[0],each[1])
                distance_field[each[0]][each[1]] = 0
                boundary.enqueue(each)
            while len(boundary)>0:
                cur_cell = boundary.dequeue()
                four_neighbors = poc_grid.Grid.four_neighbors(self,cur_cell[0],cur_cell[1])
                for each_neighbor in four_neighbors:
                    if  visited.is_empty(each_neighbor[0],each_neighbor[1]) and poc_grid.Grid.is_empty(self, each_neighbor[0], each_neighbor[1]) :
                        visited.set_full(each_neighbor[0],each_neighbor[1])
                        if distance_field[cur_cell[0]][cur_cell[1]]+1 < distance_field[each_neighbor[0]][ each_neighbor[1]]:
                            distance_field[each_neighbor[0]][ each_neighbor[1]] = distance_field[cur_cell[0]][cur_cell[1]]+1
                        boundary.enqueue(each_neighbor)
        elif  entity_type == ZOMBIE:
            boundary = poc_queue.Queue()
            for each in self._zombie_list:
                visited.set_full(each[0],each[1])
                distance_field[each[0]][each[1]] = 0
                boundary.enqueue(each)
            while len(boundary)>0:
                cur_cell = boundary.dequeue()
                four_neighbors = poc_grid.Grid.four_neighbors(self,cur_cell[0],cur_cell[1])
                for each_neighbor in four_neighbors:
                    if  visited.is_empty(each_neighbor[0],each_neighbor[1]) and poc_grid.Grid.is_empty(self, each_neighbor[0], each_neighbor[1]):
                        visited.set_full(each_neighbor[0],each_neighbor[1])
                        if distance_field[cur_cell[0]][cur_cell[1]]+1 < distance_field[each_neighbor[0]][ each_neighbor[1]]:
                            distance_field[each_neighbor[0]][ each_neighbor[1]] = distance_field[cur_cell[0]][cur_cell[1]]+1
                        boundary.enqueue(each_neighbor)
        return   distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for idx in range(len(self._human_list)):
            eight_neighbor_human = poc_grid.Grid.eight_neighbors(self, self._human_list[idx][0],self._human_list[idx][1])
            max_distance = zombie_distance[self._human_list[idx][0]][self._human_list[idx][1]]
            max_pos =(self._human_list[idx][0],self._human_list[idx][1])
            for eight_neighbor in eight_neighbor_human:
                if zombie_distance[eight_neighbor[0]][eight_neighbor[1]]> max_distance:
                    max_distance = zombie_distance[eight_neighbor[0]][eight_neighbor[1]]
                    max_pos =(eight_neighbor[0],eight_neighbor[1])
            self._human_list[idx]=(max_pos[0],max_pos[1])

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for idx in range(len(self._zombie_list)):
            four_neighbor_zombie = poc_grid.Grid.four_neighbors(self, self._zombie_list[idx][0],self._zombie_list[idx][1])
            min_distance = human_distance[self._zombie_list[idx][0]][self._zombie_list[idx][1]]
            min_pos =(self._zombie_list[idx][0],self._zombie_list[idx][1])
            for four_neighbor in four_neighbor_zombie:
                if human_distance[four_neighbor[0]][four_neighbor[1]]< min_distance:
                    min_distance = human_distance[four_neighbor[0]][four_neighbor[1]]
                    min_pos =(four_neighbor[0],four_neighbor[1])
            self._zombie_list[idx]=(min_pos[0],min_pos[1])

# Start up gui for simulation - You will need to write some code above

test_zombie =  Apocalypse(3, 3, [], [], [(2, 2)])
print test_zombie.compute_distance_field('human')

#obj = Apocalypse(3, 3, [], [], [(2, 2)])
#obj.compute_distance_field(HUMAN)
# poc_zombie_gui.run_gui(Apocalypse(20, 15))  
