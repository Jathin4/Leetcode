class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0
        for i in operations:
            if "-" in i:
                s += -1
            else:
                s += 1
        return s