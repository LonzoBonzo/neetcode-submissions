class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        basket = set()

        for n in nums:
            if n in basket:
                return True
            basket.add(n)
        return False