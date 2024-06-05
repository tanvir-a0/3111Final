import copy
import time


class Grid:
    def __init__(self, number_of_column, number_of_row, target_cell):
        self.grid = []
        self.target_cell = target_cell
        self.number_of_rows = number_of_row
        self.number_of_columns = number_of_column
        for i in range(number_of_row):
            self.grid.append([])
            for j in range(number_of_column):
                self.grid[i].append(float(0))
        print("Grid Created")
    
    def add_row(self, row_no, row_li):
        if len(row_li) != self.number_of_columns:
            print("Enter the row properly")
            return
        self.grid[row_no] = row_li
    
    def get_direction_value(self, row_index, col_index, direction):
        if direction == 'up':
            if row_index == 0:
                return self.grid[row_index][col_index]
            if self.grid[row_index-1][col_index] == None:
                return self.grid[row_index][col_index]
            return self.grid[row_index-1][col_index]
        
        if direction == 'down':
            if row_index == self.number_of_rows - 1:
                return self.grid[row_index][col_index]
            if self.grid[row_index+1][col_index] == None:
                return self.grid[row_index][col_index]
            return self.grid[row_index+1][col_index]

        if direction == 'left':
            if col_index == 0:
                return self.grid[row_index][col_index]
            if self.grid[row_index][col_index-1] == None:
                return self.grid[row_index][col_index]
            return self.grid[row_index][col_index-1]
        
        if direction == 'right':
            if col_index == self.number_of_columns-1:
                return self.grid[row_index][col_index]
            if self.grid[row_index][col_index+1] == None:
                return self.grid[row_index][col_index]
            return self.grid[row_index][col_index+1]

    def __str__(self):
        print_statement = '\n'
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                if self.grid[i][j] == None:
                    print_statement = print_statement + str( self.grid[i][j]) + '\t'
                else:
                    print_statement = print_statement + "{:0.2f}".format(self.grid[i][j])+ "\t"

            print_statement = print_statement + '\n'
        print_statement = print_statement + "\n"
        return print_statement
    
def value_iterate(grid, noise, discount, living_reward, k):
    if k == 0:
        print("K == 0")
        return Grid(grid.number_of_columns, grid.number_of_rows, grid.target_cell)
    if k == 1:
        print("K == 1")
        return grid
    old_grid = value_iterate(copy.deepcopy(grid),noise=noise, discount=discount, living_reward=living_reward, k=k-1)
    new_grid = copy.deepcopy(grid)

    #print("noc: ", grid.number_of_columns, " nor: ", grid.number_of_rows)

    for i in range(grid.number_of_rows):
        for j in range(grid.number_of_columns):
            #print("k: ", k, " i: ", i, " j: ", j)
            if grid.grid[i][j] == None:
                continue
            if [i,j] in grid.target_cell:
                continue

            up = (1-noise) * old_grid.get_direction_value(i,j,'up') + (noise/2) * old_grid.get_direction_value(i,j,'left') + (noise/2) * old_grid.get_direction_value(i,j,'right')
            down = (1-noise) * old_grid.get_direction_value(i,j,'down') + (noise/2) * old_grid.get_direction_value(i,j,'left') + (noise/2) * old_grid.get_direction_value(i,j,'right')
            left = (1-noise) * old_grid.get_direction_value(i,j,'left') + (noise/2) * old_grid.get_direction_value(i,j,'up') + (noise/2) * old_grid.get_direction_value(i,j,'down')
            right = (1-noise) * old_grid.get_direction_value(i,j,'right') + (noise/2) * old_grid.get_direction_value(i,j,'up') + (noise/2) * old_grid.get_direction_value(i,j,'down')
            #print("k: ", k, " up: ", up, " down: ", down, " left: ", left , " right: " , right)
            #time.sleep(2)
            max_value = max(up,down,left,right)
            new_grid.grid[i][j] = grid.grid[i][j] + living_reward + discount * max_value
    return new_grid


mdp = Grid(4,3,[[0,3],[1,3]])
mdp.add_row(0,[0,0,0,+1])
mdp.add_row(1,[0,None,0,-1])
mdp.add_row(2,[0,0,0,0])
print(value_iterate(grid = mdp, noise= 0.2,discount= 0.9, living_reward=0, k = 100))