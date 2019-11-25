class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for row in range(9)]
        cols = [set() for col in range(9)]
        boxes = [set() for box in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    n = int(num)
                    box_index = ( row // 3 ) * 3 + col // 3
                    if n in rows[row] or n in cols[col] or n in boxes[box_index]:
                        return False
                    rows[row].add(n)
                    cols[col].add(n)
                    boxes[box_index].add(n)
        return True
