class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # key insight here is that if 2 are almost equal and you remove the current
        # you increment the removals counter and then you skip the next val
        # because removals compeletley erase a val from array so that
        # the removed value cannot be compared to the next adjacent because
        # its "gone" from the array
        removals = 0

        i = 1
        while i < len(word):
            if (abs(ord(word[i]) - ord(word[i - 1]))) < 2:
                removals += 1
                i += 2
            else:
                i += 1
        return removals