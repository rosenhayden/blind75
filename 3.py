
"""
This screams hashmap to me. Maintain a index last seen of each char in a hashmap of our sliding window.

start from first index
Do until right pointer hits len of string:
    while charRight not in seenWindow
        move right pointer forward
    update leftChar window to be increased 1 since leftChar found the same char as rightChar

"abcabcbb"
 L=a R=b dict has ab
 L=a R=c dict has abc
 L=b R=a dict has abc
 L=c R=b dict has
 L=a R =c
 L=b R =c
 L=c R=b

 So we need to store the string when our dict is largest


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # char mapped to their last seen index
        left = 0
        bestLen = 0
        for right, ch in enumerate(s):
            #char has been seen and the char was seen after our left pointer
            if ch in char_map and char_map[ch] >= left:
                left = char_map[ch] + 1
            #add the char as the right of the window increases
            char_map[ch] = right
            #keep track of the biggest window
            if right - left + 1 > bestLen:
                bestLen = right - left + 1
        return bestLen
