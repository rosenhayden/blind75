# nums len is small so we can consider sorting

# while nums.len != 0
#     seen (set) = {}
#     for i in len nums:
#         if not in seen add to seen and remove from nums
#     create new list of elements of seen and sort the list
#.    append that list to ans
#     empty out seen
#
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while len(nums) > 0:
          seen = set()
          remaining = []
          for x in nums:
            if x not in seen:
              seen.add(x)
            else:
              remaining.append(x)

          if seen:
            ans.extend(sorted(seen))
          nums = remaining
        return ans
