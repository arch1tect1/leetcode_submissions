class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        for n in reversed(digits):
            result.append((n + carry) % 10)
            carry = (n + carry) // 10
        while carry:
            result.append(carry % 10)
            carry = carry // 10
        return list(reversed(result))