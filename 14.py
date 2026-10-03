# base case is "" => i = 0
# while the ith letter is the same
#    iterate i
# return any str[0,i+1] if i never iterates this returns the empty substring of str satisfying the base case.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0]
        prefLen= len(pref)

        for s in strs[1:]:
            while pref != s[0:prefLen]:
                prefLen -= 1
                if prefLen == 0:
                    return ""
                pref = pref[0:prefLen]
        return pref
