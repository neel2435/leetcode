class Solution:
    def romanToInt(self, s: str) -> int:
        KV = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        last = 0

        for char in s:
            if KV[char] <= last:
                total += KV[char]
                last = KV[char]
            else:
                total += (KV[char] - (2*last))
                last = KV[char]

        return total