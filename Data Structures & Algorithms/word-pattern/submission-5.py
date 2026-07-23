class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()


        if len(pattern) != len(words): return False

        wordMap = {}
        charMap = {}

        for i, (char, word) in enumerate(zip(pattern,words)):
            if charMap.get(char, 0) != wordMap.get(word, 0): 
                return False

            wordMap[word] = i + 1
            charMap[char] = i + 1

        return True 





        