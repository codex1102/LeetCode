class Solution:
    def findAnagrams(self, s, p):

        if len(p) > len(s):
            return []

        result = []

        p_count = {}
        window = {}

        for ch in p:
            p_count[ch] = p_count.get(ch,0)+1

        left = 0

        for right in range(len(s)):

            window[s[right]] = window.get(s[right],0)+1

            if right-left+1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            if window == p_count:
                result.append(left)

        return result