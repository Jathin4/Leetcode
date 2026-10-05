class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        d = [0]*n
        pc = 0
        ps = 0
        for i in range(n):
            d[i] = pc*i - ps
            if boxes[i] == '1':
                pc += 1
                ps += i
        sc =0
        ss =0
        for i in range(n-1,-1,-1):
            d[i]+= ss - sc*i
            if boxes[i] == '1':
                sc += 1
                ss += i
        return d