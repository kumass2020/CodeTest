from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        maga = Counter(magazine)
        # print(ransom, maga)
        
        for key, value in ransom.items():
            if maga[key] < value:
                return False

        return True