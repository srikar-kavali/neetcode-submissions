class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        group = {}
        my_list = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for key, num in freq.items():
            if num not in group:
                group[num] = [key]
            else:
                group[num].append(key)
        for i in range(len(nums), 0, -1):
            if i in group:
                for num in group[i]:
                    my_list.append(num)
                    k -= 1
                    if k == 0:
                        return my_list
        return None

        