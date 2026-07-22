class Solution:
    def mostWordsFound(self, sentences):
        maximum = 0

        for sentence in sentences:
            words = sentence.split()
            maximum = max(maximum, len(words))

        return maximum