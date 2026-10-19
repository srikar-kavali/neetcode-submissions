class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for ch in s:
            if ch in s_freq:
                s_freq[ch] += 1
            else:
                s_freq[ch] = 1
        for ch in t:
            if ch in t_freq:
                t_freq[ch] += 1
            else:
                t_freq[ch] = 1
        if s_freq == t_freq:
            return True
        else:
            return False
