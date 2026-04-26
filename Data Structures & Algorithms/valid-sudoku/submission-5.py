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
                num = board[i][j]
                if (num in rows[i] or num in cols[j] or num in squares[str(i//3) + " " + str(j//3)]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[str(i//3) + " " + str(j//3)].add(num)

        return True

                