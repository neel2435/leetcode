class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        shortest = float('inf')

        strs = sorted(strs)

        for s in strs:
            if len(s) < shortest:
                shortest = len(s)

        for i in range(shortest):
            if (strs[0][i] != strs[-1][i]):
                return string
            string += strs[0][i]



        return string