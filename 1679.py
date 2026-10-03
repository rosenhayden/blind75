''' naive, check if each i x j = k for j /= i for all i
 n2 worst
 we can do better.
 We can load nums into hashtable for constant time lookups. O(n) for building the hashmap instead nlogn of sorting.
 The issue with the hashmap is that when there are duplicates they will hash to the same value. What we store in the value of each key must fix this issue

 ideas:
 - store a list of indices, when a dupe is found push its indice onto the value list. Does this solve the duplicates issue? When we 'use' a num to make our target we update remove it from the value list. If we need a value that hashes to an empty list (or is not in the map) we know we cannot make the target. So it does fix the duplicate issue

alg:
load nums into hashmap
    if num[i] in hashmap:
        append i to what num[i] hashes to
    else:
        hash num[i] to list[0] = i (set first value to first index we see num[i] at)

we now have nums mapped to the indices of occurance for each num. So we must go through each num in nums and check if it - target is unused in the hashmap. We should check if the current nums index is still a value in the list it hashes too, otherwise skip it.

for i in range(len(nums)):
    #make sure index we are using is still unused
    if i in map[num]:
        if  (nums[i] - k) in map:
            map[nums[i]-k].removefromlist(nums[])

Wait but if we just keep track of the frequency of each char that makes it way easier bc it the index doesnt matter we just cant use more of one number than is in nums

kSum=0
for i in range(len(nums)):
    if nums[i] in map and map[nums[i]] != 0:
        if (nums[i] - k) in map and map[nums[i]-k] != 0
            kSum += 1



'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        fmap = {}
        ksum = 0
        for i in range(len(nums)):
            target = k - nums[i]
            if target in fmap:
                ksum +=1
                if fmap[target] == 1:
                    fmap.pop(target,None)
                else:
                    fmap[target] -= 1
            else:
                #.get is uses zero if nums[i] not in dict
                fmap[nums[i]] = fmap.get(nums[i], 0) + 1
        return ksum
