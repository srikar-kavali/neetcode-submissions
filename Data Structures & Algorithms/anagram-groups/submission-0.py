class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            freq = {}
            for ch in word:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
            key =  tuple(sorted(freq.items()))
            if key in results:
                results[key].append(word)
            else:
                results[key] = [word]
        return list(results.values())
        
            

