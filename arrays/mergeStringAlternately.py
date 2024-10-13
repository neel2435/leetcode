class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        count = 0

        if len(word1) > len(word2):
            for char in range(len(word1)):
                count += 1
                if count <= len(word2):
                    mergedString += word1[char]
                    mergedString += word2[char]
                else:
                    mergedString += word1[char]
            
        elif len(word1) < len(word2):
            for char in range(len(word2)):
                count += 1
                if count <= len(word1):
                    mergedString += word1[char]
                    mergedString += word2[char]
                else:
                    mergedString += word2[char]

        else:
            for char in range(len(word1)):
                mergedString += word1[char]
                mergedString += word2[char]
            
        return mergedString