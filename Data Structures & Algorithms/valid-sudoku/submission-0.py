class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [[] for _ in range(len(board))]
        rows = [[] for _ in range(len(board))]
        threeGrids =  [[] for _ in range(len(board))]

        for i in range (len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != '.'):
                    columns[i].append(board[i][j])
                    rows[j].append(board[i][j])
                    threeGrids[(i // 3) * 3 + (j // 3)].append(board[i][j])
                if((j+1) % 3 == 0 and (i+1) % 3 == 0): #At a grid
                    print(f"FIRST: {len(threeGrids[(i // 3) * 3 + (j // 3)])} SECOND: {len(set(threeGrids[(i // 3) * 3 + (j // 3)]))}")
                    if(len(threeGrids[(i // 3) * 3 + (j // 3)]) != len(set(threeGrids[(i // 3) * 3 + (j // 3)]))):
                        return False
                if(j == 8):
                    if(len(columns[i]) != len(set(columns[i]))):
                        return False
                
        for j in range(len(board)):
            if(len(rows[j]) != len(set(rows[j]))):
                return False

        return True