"""
2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

#CHANGED = 0

#Iterate over the list created in the previous step and create another new list in which pairs of tiles in the first list are replaced with a tile of twice the value and a zero tile.
def shift_line(line):
    """
    this function shift all the number to the left of the list
    """
    num = len(line)
    shifted_line=[]
    iter1 = 0
    while (num):
        if ((iter1 < len(line)) and (line[iter1] != 0)):
            shifted_line.append(line[iter1])
            iter1 += 1
            num -= 1
        elif (iter1 >= len(line)):
            shifted_line.append(0)
            num -= 1
        else:
            iter1+=1
    return shifted_line

#Iterate over the input and create an output list that has all of the non-zero tiles slid over to the beginning of the list with the appropriate number of zeroes at the end of the list.
def merge_line(line):
    """
    this function merge the number if adjacent number are the same
    """
    print "before merge tiles: ", line
    #global CHANGED
    length = len(line)
    if (length == 2):
         if (line[0] == line[1]):
                line[0] = 2*line[0]
                line[1] = 0
                #CHANGED = 1
    for xx1 in range(length-1):
        if ( (line[xx1] == line[xx1+1]) and (line[xx1] != 0) ):
            line[xx1] = line[xx1]+line[xx1+1]
            line[xx1+1] = 0
            #CHANGED = 1
    print "after merge tiles: ", line
    return line

def merge(line):
    """
    shift number to the left, merge the numbers if the same, shift the numbers again
    """
    if (len(line)<1):
        return line
    shifted_line =  shift_line(line)
    #print shifted_line
    merged = merge_line(shifted_line)
    result = shift_line(merged)
    #print result
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        initialze the self, grid,height and width
        """
        self._grid_height1 = grid_height
        self._grid_width1 = grid_width
        self._grid = [[0 + 0 for dummy_col in range(grid_width)]
                           for dummy_row in range(grid_height)]
        #hua hard coded.
        up_initial_grid = []
        down_initial_grid = []
        left_initial_grid = []
        right_initial_grid = []

        for num_width1 in range(grid_width):
            up_initial_grid.append((0,num_width1))
            down_initial_grid.append((grid_height-1, num_width1))

        for num_height1 in range(grid_height):
            left_initial_grid.append((num_height1, 0))
            right_initial_grid.append((num_height1, grid_width-1))

        self._initial_grid = {UP: up_initial_grid,
                            DOWN: down_initial_grid,
                            LEFT: left_initial_grid,
                            RIGHT: right_initial_grid}
        #self.__str__()
        #self.reset()
        print "initial_grid is: ", self._initial_grid

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.__init__(self._grid_height1, self._grid_width1)
        self.new_tile()
        self.new_tile()
        self.__str__()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # "Print out values in grid"
#        print "the grid values are: "
#        for row in range(self.grid_height1):
#            if (row == 0):
#                print "[",self.grid[row]
#            elif (row == self.grid_height1-1):
#                print self.grid[row],"]"
#            else:
#                print self.grid[row]
#        print

        string = [str(row) for row in self._grid]
        print '[' + '\n'.join(string) + ']'
        print
        return '[' + '\n'.join(string) + ']'

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height1

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width1

    def move(self, direction):
        #global CHANGED
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        key = direction
        if (direction == UP):
            initial_tiles = self._initial_grid[UP]
            num_steps = self._grid_height1
        elif (direction == DOWN):
            initial_tiles = self._initial_grid[DOWN]
            #initial_tiles = self.initial_grid[self.height-1]
            num_steps = self._grid_height1
        #change code below
        elif (direction == LEFT):
            initial_tiles = self._initial_grid[LEFT]
            #initial_tiles = self.initial_grid[self.height-1]
            num_steps = self._grid_width1
        elif (direction == RIGHT):
            initial_tiles = self._initial_grid[RIGHT]
            #initial_tiles = self.initial_grid[self.height-1]
            num_steps = self._grid_width1

        #hua
        print "moving initial tiles: ", initial_tiles

        #old_grid = list(self.grid)
        old_grid = [row[:] for row in self._grid]

        #print "old grid is: ", old_grid
        moving_tiles = []
        #CHANGED = 0
        for xtile in initial_tiles:
            moving_tiles = []
            for step in range(num_steps):
                row = xtile[0] + step*OFFSETS[key][0]
                col = xtile[1] + step*OFFSETS[key][1]
                #print type (self.grid[row, col])
                moving_tiles.append(self._grid[row][col])

            #print "moving tile: ", moving_tiles
            moved_tiles = merge(moving_tiles)
            #print "after moving: ", moving_tiles
            for step in range(num_steps):
                row = xtile[0] + step*OFFSETS[key][0]
                col = xtile[1] + step*OFFSETS[key][1]
                self._grid[row][col] = moved_tiles[step]
        #hua
        #self.__str__()
        #if (CHANGED):
        # print "generated new tile"

        #print "old grid after move is: ", old_grid


        if (old_grid != self._grid):
            self.new_tile()


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if (row > self._grid_height1):
            print "row index out of range: ", row
            return
        if (col > self._grid_width1):
            print "col index out of range:", col
            return


        self._grid[row][col] = value


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #hua
        #keep track empty_square list of tuples
        empty_list = []
        for row_x in range(self._grid_height1):
            for col_y in range(self._grid_width1):
                if (self._grid[row_x][col_y] == 0):
                    empty_list.append( (row_x,col_y) )
        if (empty_list == []):
            print "Game Over, no more space"
            return

        select = random.choice(empty_list)
        random_value_list = [2,2,2,2,2,4,2,2,2,2]
        value = random.choice(random_value_list)

        self._grid[select[0]][select[1]] = value




    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
#obj = TwentyFortyEight(2, 2)
#obj.reset()
#obj = TwentyFortyEight(4, 4)
#obj.set_tile(0, 0, 2)
#obj.set_tile(0, 1, 4)
#obj.set_tile(0, 2, 8)
#obj.set_tile(0, 3, 16)
#obj.set_tile(1, 0, 16)
#obj.set_tile(1, 1, 8)
#obj.set_tile(1, 2, 4)
#obj.set_tile(1, 3, 2)
#obj.set_tile(2, 0, 0)
#obj.set_tile(2, 1, 0)
#obj.set_tile(2, 2, 8)
#obj.set_tile(2, 3, 16)
#obj.set_tile(3, 0, 0)
#obj.set_tile(3, 1, 0)
#obj.set_tile(3, 2, 4)
#obj.set_tile(3, 3, 2)
#obj.__str__()
#obj.move(UP)
#obj.__str__()
#obj = TwentyFortyEight(4, 4)
#obj.set_tile(0, 0, 2)
#obj.set_tile(0, 1, 0)
#obj.set_tile(0, 2, 0)
#obj.set_tile(0, 3, 0)
#obj.set_tile(1, 0, 0)
#obj.set_tile(1, 1, 2)
#obj.set_tile(1, 2, 0)
#obj.set_tile(1, 3, 0)
#obj.set_tile(2, 0, 0)
#obj.set_tile(2, 1, 0)
#obj.set_tile(2, 2, 2)
#obj.set_tile(2, 3, 0)
#obj.set_tile(3, 0, 0)
#obj.set_tile(3, 1, 0)
#obj.set_tile(3, 2, 0)
#obj.set_tile(3, 3, 2)
#obj.__str__()
#obj.move(UP)
#obj.__str__()
