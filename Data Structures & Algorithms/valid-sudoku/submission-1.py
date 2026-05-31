class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if (num in boxes["row" + str(i)] 
                    or num in boxes["col" + str(j)]
                    or num in boxes[(i//3, j//3)]):
                    return False
                boxes["row" + str(i)].add(num)
                boxes["col" + str(j)].add(num)
                boxes[(i//3, j//3)].add(num)
        return True