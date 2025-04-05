class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regex approach
        # s = re.sub('[^a-zA-Z0-9]', '', s).lower()     # -> amanaplanacanalpanama

        # s = s.replace(' ', '')
        i = 0
        j = len(s)-1

        while i <= j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            print(i, j)

            # if i > j:
            #     return True

            if s[i].upper() != s[j].upper():
                return False
            
            i += 1
            j -= 1

        return True