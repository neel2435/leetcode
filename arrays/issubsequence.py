class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0

        for char in t:
            if (count == len(s)):
                return True
            elif char == s[count]:
                count += 1
            else:
                continue
        
        if (count == len(s)):
            print(count)
            return True
        else:
            print(count)
            return False