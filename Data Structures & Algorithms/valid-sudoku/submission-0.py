class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        hs = set()
        for row in board:
            for i in row:
                if i in hs:
                    return False
                elif i != ".":
                    hs.add(i)
            hs.clear()
        
        #check columns

        for c in range(9):
            for r in range(9):
                if board[r][c] in hs:
                    return False
                elif board[r][c] != ".":
                    hs.add(board[r][c])
            hs.clear()

        
        #check boxes
        for box in range(9):
            boxrow = (box//3)*3
            boxcol = 3*(box%3)
            for row in range(3):
                r = boxrow + row
                for column in range(3):
                    c = boxcol + column
                    if board[r][c] in hs:
                        return False
                    elif board[r][c] != ".":
                        hs.add(board[r][c])
            hs.clear()

        return True