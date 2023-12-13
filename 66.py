class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        c = ''
        for i in digits:
            c = c + str(i)
        w = int(c)+1
        for q in str(w):
            l.append(int(q))
        return l