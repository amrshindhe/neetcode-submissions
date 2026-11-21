class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowValidate = defaultdict(set)
        colValidate = defaultdict(set)
        box_validate = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowValidate[row]:
                    return False
                if board[row][col] in colValidate[col]:
                    return False
                if board[row][col] in box_validate[int(row/3)][int(col/3)]:
                    return False
                rowValidate[row].add(board[row][col]) 
                colValidate[col].add(board[row][col]) 
                box_validate[int(row/3)][int(col/3)].add(board[row][col])
        
        return True

