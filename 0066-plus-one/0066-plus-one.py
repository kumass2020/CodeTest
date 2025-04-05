class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        s = ''.join(digits)
        s = str(int(s)+1)
        # s = list(str(s))
        # return s
        return [int(x) for x in s]
        