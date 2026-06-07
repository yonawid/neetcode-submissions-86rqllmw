class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        square=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num=board[r][c]
                if (num in rows[r] or
                    num in cols[c] or
                    num in square[(r//3,c//3)]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                square[(r//3,c//3)].add(num)
        return True
        