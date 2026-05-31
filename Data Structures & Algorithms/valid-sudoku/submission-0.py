class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(list)
        for i, row in enumerate(board):
            boxes["row" + str(i)] = row
            for j, num in enumerate(row):
                boxes["col" + str(j)].append(num)
                boxes[(i//3, j//3)].append(num)
        
        for box in boxes.values():
            seen = set()
            for num in box:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
        return True