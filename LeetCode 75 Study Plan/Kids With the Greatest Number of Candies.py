class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []

        for candy in candies:
            new = candy + extraCandies
            b = True
            for i in candies:
                if new<i:
                    b = False
            ans.append(b)
        return ans
