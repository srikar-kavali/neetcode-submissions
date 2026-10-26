class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch
        result = result.lower()
        left, right = 0, len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        