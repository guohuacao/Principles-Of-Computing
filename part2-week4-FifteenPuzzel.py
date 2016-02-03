"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]


    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self.get_number(target_row, target_col) != 0:
            print "assert error 1"
            return False
        for index_k in range(target_col+1,self._width):
            if self.current_position(target_row, index_k) != (target_row, index_k):
                print "assert error 2"
                return False
        for index_h in range(target_row+1,self._height):
            for index_m in range(0,self._width):
                if self.current_position(index_h, index_m) != (index_h, index_m):
                    print "assert error 3"
                    return False
        return True

    def __position_tile_left_up(self, target_row, target_col, to_move_tile):
        """
        a helper function for tile left up
        """
        move_string = ""
#        section_string = ""
#        to_move_tile = self.current_position(target_row,target_col)
        print "A1"
#        section_string = ""
        index_i = to_move_tile[0]
        while index_i != target_row:
            index_i += 1
            move_string += "u"
#            section_string += "u"
#        self.update_puzzle(section_string)
        print self

        print "A2"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i < target_col:
            index_i += 1
            move_string += "l"
#            section_string += "l"
#        self.update_puzzle(section_string)
        print self

        print "A3"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i < target_col-1:
            index_i += 1
            move_string += "drrul"
#            section_string += "drrul"
#        self.update_puzzle(section_string)
        print self


        if to_move_tile[1] < target_col:
            print "A4"
            move_string += "dru"
#            section_string = ""
#            section_string += "dru"
#            self.update_puzzle(section_string)
            print self

        print "A5"
#        section_string = ""
        index_i = to_move_tile[0]
        while index_i != target_row-1:
            index_i += 1
            move_string += "lddru"
#            section_string += "lddru"
#        self.update_puzzle(section_string)
        print self

        print "A6"
        move_string += "ld"
#        section_string = "ld"
#        self.update_puzzle(section_string)
        print self
        self.update_puzzle(move_string)
        return move_string

    def __position_tile_left_down(self, target_row, target_col, to_move_tile):
        """
        a helper function for tile left dowm
         """
        move_string = ""
#        section_string = ""
#        to_move_tile = self.current_position(target_row,target_col)
#         print "E1"
        move_string += "u"
#        section_string = ""
#        section_string += "u"
#         self.update_puzzle(section_string)
#         print self

#         print "E2"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col:
            index_i += 1
            move_string += "l"
#            section_string += "l"
#         self.update_puzzle(section_string)
#         print self

#        print "E3"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col-1:
            index_i += 1
            move_string += "urrdl"
#            section_string += "urrdl"
#         self.update_puzzle(section_string)
#         print self

#         print "E4"
        move_string += "druld"
#        section_string = ""
#        section_string += "druld"
#         self.update_puzzle(section_string)
#         print self

        self.update_puzzle(move_string)
        return move_string

    def __position_tile_right_up(self, target_row, target_col, to_move_tile):
        """
        a helper function for tile right up
        """
        move_string = ""
#        section_string = ""
#        to_move_tile = self.current_position(target_row,target_col)
#            print "B1"
        index_i = to_move_tile[0]
        while index_i != target_row - 1:
            index_i += 1
            move_string += "u"
#            section_string += "u"
#         self.update_puzzle(section_string)
#         print self

#         print "B2"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col:
            index_i -= 1
            move_string += "r"
#            section_string += "r"
        move_string += "uldr"
#         self.update_puzzle(section_string)
#        section_string = ""
#        section_string += "uldr"
#         self.update_puzzle(section_string)
#         print self

#         print "B3"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col+1:
            index_i -= 1
            move_string += "ulldr"
#            section_string += "ulldr"
#         self.update_puzzle(section_string)
#         print self

#         print "B4"
        move_string += "ul"
#         section_string = "ul"
#         self.update_puzzle(section_string)
#         print self

#         print "B5"
#        section_string = ""
        index_i = to_move_tile[0]
        while index_i != target_row-1:
            index_i +=1
            move_string += "lddru"
#            section_string += "lddru"
#         self.update_puzzle(section_string)
#         print self

#         print "B6"
        move_string += "ld"
#        section_string = "ld"
#         self.update_puzzle(section_string)
#         print self
        self.update_puzzle(move_string)
        return move_string


    def __position_tile_right_down(self, target_row, target_col, to_move_tile):
        """
        a helper function for tile right dowm
        """
        move_string = ""
        section_string = ""
#        to_move_tile = self.current_position(target_row,target_col)
        section_string += "u"
        move_string += "u"
        self.update_puzzle(section_string)
#        print self

#        print "D2"
        section_string=""
        index_i = target_col
        while index_i != to_move_tile[1]:
            index_i += 1
            move_string += "r"
            section_string += "r"
        self.update_puzzle(section_string)
#        print self

#        print "D3"
        section_string=""
        index_i = target_col
        while index_i != to_move_tile[1]-1:
            index_i += 1
            move_string += "ulldr"
            section_string += "ulldr"
        self.update_puzzle(section_string)
#        print self

#        print "D4"
#        move_string += "ullddrlruld"
        move_string += "dluld"
        section_string = ""
#        section_string += "ullddrlruld"
        section_string += "dluld"
        self.update_puzzle(section_string)
#        print self
#        self.update_puzzle(move_string)
        return move_string


    def __position_tile_same_row(self, target_row, target_col, to_move_tile):
        """
        a helper function for tile same row
        """
        move_string = ""
#        section_string = ""
#        to_move_tile = self.current_position(target_row,target_col)

#         print "C1"
        move_string += "u"
#        section_string = "u"
#        self.update_puzzle(section_string)

#         print "C2"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col:
            index_i +=1
            move_string += "l"
#            section_string += "l"
#         self.update_puzzle(section_string)
#         print self

#         print "C3"
#        section_string = ""
        index_i = to_move_tile[1]
        while index_i != target_col:
            index_i +=1
            move_string += "rdlur"
#            section_string += "rdlur"
#         self.update_puzzle(section_string)
#         print self

#         print "C4"
        move_string += "ld"
#        section_string = "ld"
#         self.update_puzzle(section_string)
#         print self
        self.update_puzzle(move_string)
        return move_string

    def is_already_solved(self):
        """
        a helper function to check whether the puzzle to be solved is actually a solved puzzle
        """
        width = self.get_width()
        height = self.get_height()

        for index_h in range(height):
            for index_m in range(width):
                if self.current_position(index_h, index_m) != (index_h, index_m):
                    return False
        return True

    def __find_zero_tile(self):
        """
        find the zeor tile and returns its index of row and index of col
        """
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    return (row, col)
        return (-1, -1)

    def position_tile(self, target_row, target_col, to_move_tile=(-1, -1)):
        """
        a helper function to position tile in the target row and col
        """

        if to_move_tile[0]==-1 and to_move_tile[1]==-1:
            to_move_tile = self.current_position(target_row,target_col)
        print "to_move_tile=",to_move_tile,"target_row, target_col =", target_row, target_col

        if to_move_tile[0] < target_row and to_move_tile[0] +1 == target_row and to_move_tile[1] > target_col and to_move_tile[0] >= 1:
            print "position_tile_right_down"
            return self.__position_tile_right_down(target_row, target_col, to_move_tile)
        elif to_move_tile[0] < target_row and to_move_tile[1] > target_col:
            print "position_tile_right_up"
            return self.__position_tile_right_up(target_row, target_col, to_move_tile)
        elif to_move_tile[0] < target_row and to_move_tile[1] < target_col and to_move_tile[0] +1 == target_row and to_move_tile[0] >= 1:
            print "position_tile_left_down"
            return self.__position_tile_left_down(target_row, target_col, to_move_tile)
        elif to_move_tile[0] < target_row and to_move_tile[1] <=target_col :
            print "position_tile_left_up"
            return self.__position_tile_left_up(target_row, target_col, to_move_tile)
        else:
            print "position_tile_same_row"
            return self.__position_tile_same_row(target_row, target_col, to_move_tile)

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
#        assert self.lower_row_invariant(target_row, target_col)
#        assert target_row > 1 and target_col > 0, "target_row or target_col out of range"
        move_string = self.position_tile(target_row, target_col)
#        assert self.lower_row_invariant(target_row, target_col-1)
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
#        assert self.lower_row_invariant(target_row, 0)
        print "solve_col0_tile, (", target_row, ", 0)"
        to_move_tile = self.current_position(target_row,0)
        print to_move_tile
        target_value = self.get_number(to_move_tile[0], to_move_tile[1])
        print target_value
        move_string = "ur"
        self.update_puzzle(move_string)
        second_move_string = ""
        third_move_string = ""
        print "-----line1.1-----"
        print "G1, move_string = ", move_string
        print self
        if self.get_number(target_row,0) == target_value:
            count_temp = self.get_width() - 2
            while count_temp >0:
                second_move_string += "r"
                count_temp -=1
            self.update_puzzle(second_move_string)
            move_string = move_string + second_move_string
            print "-----line1.2-----"
            print self
        else:
            second_move_string += self.position_tile(target_row-1, 1, to_move_tile)
            print "-----line1.3-----, second_move_string = ",second_move_string
            print self
            third_move_string += "ruldrdlurdluurddlur"
            count_temp = self.get_width()-2
            while count_temp >0:
                third_move_string += "r"
                count_temp -=1
            self.update_puzzle(third_move_string)
            print "-----line1.4-----, third_move_string=",third_move_string
            print self
            move_string = move_string + second_move_string + third_move_string
        print "-----line1.5-----"
        print "G2"
        print self
#        assert self.lower_row_invariant(target_row-1, self.get_width()-1)
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.get_number(0, target_col) != 0:
            return False
        target_row = 1
        for index_h in range(0,target_row+1):
            for index_k in range(target_col+1,self._width):
                if self.current_position(target_row, index_k) != (target_row, index_k):
                    return False
        for index_h in range(target_row+1,self._height):
            for index_m in range(0,self._width):
                if self.current_position(index_h, index_m) != (index_h, index_m):
                    return False
        if self.current_position(1, target_col) != (1, target_col):
            return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        target_row = 1
        if self.get_number(target_row, target_col) != 0:
            return False
        for index_h in range(0,target_row+1):
            for index_k in range(target_col+1,self._width):
                if self.current_position(target_row, index_k) != (target_row, index_k):
                    return False
        for index_h in range(target_row+1,self._height):
            for index_m in range(0,self._width):
                if self.current_position(index_h, index_m) != (index_h, index_m):
                    return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        print "solve_row0_tile(): (0,",target_col, ")"
        move_string1 = "ld"
        self.update_puzzle(move_string1)
        target_row = 0
        to_move_tile = self.current_position(target_row,target_col)
        target_value = self.get_number(to_move_tile[0], to_move_tile[1])
        if self.get_number(target_row, target_col) == target_value:
            return move_string1
        move_string2 = ""
        target_col_new = target_col - 1
        if to_move_tile[0]==1:
            for dummy_j in range(target_col_new- to_move_tile[1]):
                move_string2 += "l"
            for dummy_j in range(target_col_new- to_move_tile[1]-1):
                move_string2 += "urrdl"
            move_string2 += "urldurdlurrdluldrruld"
        elif to_move_tile[0]==0:
            for dummy_j in range(target_col_new- to_move_tile[1]):
                move_string2 += "l"
            move_string2 += "urdl"
            for dummy_j in range(target_col_new- to_move_tile[1]-1):
                move_string2 += "urrdl"
            move_string2 += "urldurdlurrdluldrruld"
#        print "-----solve_row0_tile A1-----"
#        print self
        self.update_puzzle(move_string2)
#        print self
        return move_string1 + move_string2

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        print "solve_row1_tile(): (1,",target_col, ")"
        target_row = 1
        move_string = ""
        to_move_tile = self.current_position(target_row,target_col)
        if to_move_tile[0]==1:
            for dummy_j in range(target_col- to_move_tile[1]):
                move_string += "l"
            for dummy_j in range(target_col- to_move_tile[1]-1):
                move_string += "urrdl"
            move_string += "ur"
        elif to_move_tile[0]==0:
            if to_move_tile[1]==target_col:
                move_string +="u"
            else:
                for dummy_j in range(target_col- to_move_tile[1]):
                    move_string += "l"
                move_string += "urdl"
                for dummy_j in range(target_col- to_move_tile[1]-1):
                    move_string += "urrdl"
                move_string += "ur"
        self.update_puzzle(move_string)
        print "solve_row1_tile(), move_string = ", move_string
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_string1=""
        move_string2=""
        zero_tile = self.current_position(0,0)
        if zero_tile == (0,1):
            move_string1 = "l"
        elif zero_tile == (1,0):
            move_string1 = "u"
        elif zero_tile == (1,1):
            move_string1 = "lu"
#        print "move_string1=", move_string1
        self.update_puzzle(move_string1)
        #0-3-1-2
        if self.get_number(0, 0) < self.get_number(1, 0) and self.get_number(1, 0) < self.get_number(1, 1) and self.get_number(1, 1) < self.get_number(0, 1):
           move_string2 =  "drul"
        #0-2-3-1
        elif self.get_number(0, 0) < self.get_number(1, 1) and self.get_number(1, 1) < self.get_number(0, 1) and self.get_number(0, 1) < self.get_number(1, 0):
           move_string2 =  "rdlu"
#        print "move_string2=", move_string2
        print "before solve_2x2()____\n",self
        self.update_puzzle(move_string2)
        print "after solve_2x2()____\n",self
        return move_string1+ move_string2

    def  solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        move_string = ""
        width = self.get_width()
        height = self.get_height()
        if self.is_already_solved():
            return move_string
        # pre processing
        start_i = -1
        start_j = -1
        for start_i in range(0,height)[::-1]:
            for start_j in range(0,width)[::-1]:
                if self.current_position(start_i, start_j) !=  (start_i, start_j):
                    break;
            if self.current_position(start_i, start_j) !=  (start_i, start_j):
                break;
        print "pre-test", start_i, start_j
        zero_tile = self.__find_zero_tile()
        print "pre-test, zero_tile = ", zero_tile
        if zero_tile[1]<= start_j:
            for dummy_step in range(start_j - zero_tile[1]):
                move_string += "r"
        else:
            for dummy_step in range(zero_tile[1] - start_j):
                move_string += "l"
        for dummy_step in range(start_i - zero_tile[0]):
            move_string += "d"
        self.update_puzzle(move_string)
        print self
        for index_i in range(2,height)[::-1]:
            for index_j in range(1,width)[::-1]:
                print "solve() continued the loop:", index_i, index_j
                if self.current_position(index_i, index_j) == (index_i, index_j):
                    continue;
                if index_i > start_i:
                    continue
                if index_i ==start_i and index_j>start_j:
                    continue
                print "before solve()___: (", index_i, ", ", index_j,")"
                assert self.lower_row_invariant(index_i, index_j)
                print self
                move_string += self.solve_interior_tile(index_i, index_j)
                print "after solve()___: (", index_i, ", ", index_j,")", move_string,"\n", self
                assert self.lower_row_invariant(index_i, index_j-1)
            if index_i > start_i:
                continue
            move_string += self.solve_col0_tile(index_i)
            print self
        for index_j in range(2,width)[::-1]:
            if self.current_position(1, index_j) == (1, index_j):
                continue;
            assert self.row1_invariant(index_j)
            move_string += self.solve_row1_tile(index_j)
            print "after solve_row1()___:\n", self
            if self.current_position(0, index_j) == (0, index_j):
                continue;
            assert self.row0_invariant(index_j)
            move_string += self.solve_row0_tile(index_j)
            print "after solve_row0()___:\n", self
            assert self.current_position(1, index_j-1) == (1, index_j-1) or self.row1_invariant(index_j - 1)
        move_string += self.solve_2x2()
        return move_string


# Start interactive simulation

#poc_fifteen_gui.FifteenGUI(Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 15, 4, 3], [5, 11, 12, 13, 14], [0, 16, 17, 18, 19]]))
#puzzle1 = Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 15, 4, 3], [5, 11, 12, 13, 14], [0, 16, 17, 18, 19]])
#print puzzle1, puzzle1.solve_col0_tile(3)
#print "------line2------\n", puzzle1


#poc_fifteen_gui.FifteenGUI(Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]))
#puzzle1 = Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]])#
#print puzzle1, puzzle1.solve_col0_tile(2)
#print "------line2------\n", puzzle1



#poc_fifteen_gui.FifteenGUI(Puzzle(5, 5,[[8,10,13,15,21],[7,9,11,12,14],[2,16,1,19,18],[4,6,3,17,20],[5,0,22,23,24]]))
#puzzle = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#move_string = puzzle.solve_interior_tile(2,2)
#print puzzle
#print move_string

#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4,[[6,2,12,8],[10,4,5,9],[11,1,7,3],[0,13,14,15]]))
#puzzle = Puzzle(4, 4,[[6,2,12,8],[10,4,5,9],[11,1,7,3],[0,13,14,15]])
#print puzzle.solve_interior_tile(3,0)


#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4, [[4, 2, 0, 3], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]))
#puzzle = Puzzle(4, 4, [[4, 2, 0, 3], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
#print puzzle
#print puzzle.row0_invariant(2)

#poc_fifteen_gui.FifteenGUI(Puzzle(4, 5, [[7, 2, 0, 3, 4], [5, 6, 1, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]))
#puzzle = Puzzle(4, 5, [[7, 2, 0, 3, 4], [5, 6, 1, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print puzzle
#print puzzle.row0_invariant(2)
#print puzzle.solve_row0_tile(3)
#print puzzle


#poc_fifteen_gui.FifteenGUI(Puzzle(2, 2, [[1, 3], [2,0]]))
#puzzle = Puzzle(2, 2, [[1, 3], [2,0]])
#print puzzle
#print puzzle.row0_invariant(1)
#print puzzle.solve_row0_tile(1)
#print puzzle.solve_2x2()
#print puzzle

poc_fifteen_gui.FifteenGUI(Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]]))
puzzle = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
print puzzle
print puzzle.is_already_solved()
print puzzle.solve_puzzle()


#poc_fifteen_gui.FifteenGUI(Puzzle(5, 4, [[5, 4, 2, 3], [1, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]]))
#puzzle = Puzzle(5, 4, [[5, 4, 2, 3], [1, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]])
#print puzzle
#print puzzle.solve_puzzle()

#poc_fifteen_gui.FifteenGUI(Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]]))
#puzzle = Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]])
#print puzzle
#print puzzle.solve_puzzle()
