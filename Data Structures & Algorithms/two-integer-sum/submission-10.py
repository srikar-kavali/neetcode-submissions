class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 2:
            return [0, 1]
        else:
            for i in range(0, len(nums)):
                for j in range(1, len(nums)):
                    if i != j and nums[i] + nums[j] == target:
                        return [i, j]

        
        