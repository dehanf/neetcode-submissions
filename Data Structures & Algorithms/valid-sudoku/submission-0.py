class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if(val in rows[i]):
                    return False
                rows[i].add(val)

                if(val in cols[j]):
                    return False
                cols[j].add(val)

                idx = int(i/3) * 3 + int(j/3)
                if(val in boxes[idx]):
                    return False
                boxes[idx].add(val)
        return True


