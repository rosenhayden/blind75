# there is probably a DP solution but im gonna give two pointers a go.
'''
constraints 1 <= s.length <= 1000
this implies that we can get away with something like n^2

s will never be empty
if s.len = 1 we can return s

for each char we expand outward and check if its a palindrome
need to handle even and odd len substring cases.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #solution = ""
        bestL,bestR = 0,0
        solutionLength = 0
        for i in range(len(s)):
            left,right = i,i
            #odd len string case
            while left >= 0 and right < len(s) and s[left] == s[right]:
                candidateSolutionLength = right - left + 1
                if candidateSolutionLength > solutionLength:
                    #solution = s[left : right+1]
                    bestL = left
                    bestR = right
                    solutionLength = candidateSolutionLength
                #expand out
                left -= 1
                right += 1
            #even len palindromic substrings case
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                candidateSolutionLength = right - left + 1
                if candidateSolutionLength > solutionLength:
                    #solution = s[left:right+1]
                    bestL = left
                    bestR = right
                    solutionLength = candidateSolutionLength
                #expand out
                left -= 1
                right += 1
        return s[bestL : bestR +1]
