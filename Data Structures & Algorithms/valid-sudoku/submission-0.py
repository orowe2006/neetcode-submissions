class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()

            for j in range(9):
                s.add(board[i][j])
            
            if "." in board[i]:
                if len(s) - 1 != len(board[i]) - board[i].count("."):
                    return False
            else:
                if len(s) != len(board[i]):
                    return False

        for j in range(9):
            s = set()
            col = [board[i][j] for i in range(9)]

            for i in range(9):
                s.add(board[i][j])
            
            if "." in col:
                if len(s) - 1 != len(col) - col.count("."):
                    return False
            else:
                if len(s) != len(col):
                    return False

        for i in range(3):
            for j in range(3):
                s = set()
                count = 0

                for k in range(3*i, 3*i+3):
                    for l in range(3*j, 3*j+3):
                        if board[k][l] != ".":
                            s.add(board[k][l])
                            count+=1
                
                if(count!=len(s)):
                    return False

        return True