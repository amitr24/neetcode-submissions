from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Go through the whole board
        # Skip the empty ones
        # Else check if they are already in one of the appropriate sets
        # IF not, add them
        # Else boot time

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[str(i//3) + " " + str(j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[str(i//3) + " " + str(j//3)].add(board[i][j])

        return True

                