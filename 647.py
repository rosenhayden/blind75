'''

two pointers

[aaa]

total will always be at least the length of the array
[a] -> 1
[abc] - > 3

[aaa]
 ^^
 ^ ^
  ^^

could we just use the solution to the other

sum of times the LPSS is changes plus the len of the array

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            left, right = i,i
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            left,right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        return count

#Time: o(n2)? space o(1)
