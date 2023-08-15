#puzzle is a list, where each inner list is a row of sudoku.
#returns if the solutions exists and mutates the list so to be the solution.

def find_next(puzzle):
    #finds the next empty space in the puzzle and returns it
    # indices are from 0-8
    # r is row and c is column
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
            
    return None, None #if no empty space is found   

def  guess_valid(puzzle, guess, row, col):  
# to find is guess is valid
# return true if valid n=and false if not
# A] row:
   row_value = puzzle[row]
   if guess in row_value:
       return False
   #B] col:
   col_value = [puzzle[i][col] for i in range(9)]
   if guess in col_value:
       return False
   #3 by 3 puzzle matrix:
   row_start = (row//3) * 3
   col_start = (col//3) * 3

   for r in range(row_start, row_start +3):
       for c in range(col_start, col_start + 3):
           if puzzle[r][c] == guess:
               return False
   return True      
    

def sudoku_solver(puzzle):
    #step 1: choose where to go in the puzzle
    row, col = find_next(puzzle)
    if row is None: #if there is no empty space after allowing valid inputs
        return True 
    
    #step 2: if there is a empty space to make guess from 1-9
    for guess in range(1, 10): 
        #step 3: to find if guess is valid
        if guess_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            #recurse until we reach at the end of the puzzle 
            if sudoku_solver(puzzle):
                return True
        # step 4: if guess not valid
        # thus we backtrack
        puzzle[row][col] = 0 # reset guess
    # step 5: if no guess work, then puzzle cannot be solved  
    return False      

if __name__ =='__main__':
    puzzle_board = [
        
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,    1, 0, 5,   0, 4, 0],
        [1, 0, 9,    0, 0, 0,   2, 0, 0],
    ]
    print(sudoku_solver(puzzle_board))
    print(puzzle_board)