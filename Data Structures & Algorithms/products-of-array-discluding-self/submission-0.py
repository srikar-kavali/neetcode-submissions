class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []

        product = 1
        for num in nums:
            result.append(product)
            product *= num
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        return result

        