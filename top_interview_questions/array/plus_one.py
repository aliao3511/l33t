class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        idx = len(digits) - 1
        while idx >= 0:
            if carry == 1:
                digits[idx] += 1
                carry = 0
            if digits[idx] > 9:
                carry = 1
                digits[idx] %= 10
            idx -= 1
        return [1] + digits if carry == 1 else digits
