'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution(object):
    def isValidSudoku(self, board):
        
        #i tried my best but i had no starting position, so i copied teh solution
        columns = [[row[id] for row in board] for id in range(len(board[0]))] # transposition
        for row, row2 in zip(board, columns):
            for num, num2 in zip(row, row2):
                if (num.isdigit() and row.count(num) != 1) or (num2.isdigit() and row2.count(num2) != 1): #checking for reps in rows and columns
                    return False
        
        ###### Division into 3x3 blocks
        temp_arr = []
        arr = [] 
        for num in range(0,9,3): # division matrix to 3 columns 3x9
            for col in board:
                temp_arr.append(col[num:num+3])
        for num in range(0,27,3): # division columns to 9 blocks 3x3
            arr.append(temp_arr[num:num+3])
        # temp_arr:     List[List[str, str, str]]
        # arr:          List[List[List[str, str, str]]]
        ######

        values_arr = [] # Counting the temp_arr
        for quad in arr:
            temp_arr = [] # Temp list for 1 of 9 3х3 blocks

            for row in quad: # conversion matrix 3x3 to 1x9
                temp_arr += row

            for value in temp_arr: # Counting the number of each digit in a 3x3 block
                if value.isdigit():
                    values_arr.append(temp_arr.count(value))

        if values_arr != []:
            if max(values_arr) > 1: # if max(values_arr) > 1 -> sudoku invalid
                return False

        return True
      
      
      #best time complexity
     def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, column, grid = set(), set(), set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    r = (i, board[i][j])
                    c = (j, board[i][j])
                    g = (i // 3, j // 3, board[i][j])
                    if r in row or c in column or g in grid:
                        return False
                    row.add(r)
                    column.add(c)
                    grid.add(g)
        return True
      
      #best space complexity
      
 class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.isRowValid(board) and
                 self.isColValid(board) and 
                 self.isSqValid(board) )
    
    def isRowValid(self,board):
        for row in board:
            if not self.isUnitValid(row):
                return False
        return True

    def isColValid(self,board):
        for col in zip(*board):
            if not self.isUnitValid(col):
                return False
        return True

    def isSqValid(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                sq = [board[x][y] for x in range (i,i+3) for y in range (j , j+3)]


                if not self.isUnitValid(sq):
                    return False
        return True

    def isUnitValid(self,unit):
        unit = [i for i in unit if i !='.']
        return len(set(unit)) == len(unit)
