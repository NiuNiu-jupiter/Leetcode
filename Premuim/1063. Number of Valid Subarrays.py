"""
 Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

 The leftmost element of the subarray is not larger than other elements in the subarray.

  

 Example 1:

 Input: [1,4,2,5,3]
 Output: 11
 Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
 Example 2:

 Input: [3,2,1]
 Output: 3
 Explanation: The 3 valid subarrays are: [3],[2],[1].
 Example 3:

 Input: [2,2,2]
 Output: 6
 Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
  

 Note:

 1 <= A.length <= 50000
 0 <= A[i] <= 100000

"""
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        if not nums: return []
        """
        res = 0
        j = 0
        for i in range(len(nums)):
            j = i
            while j < len(nums):
                if nums[i]<=nums[j]:
                    res+=1
                    j+=1
                else:
                    break
        return res
        """

        res, stack = 0, []
        for a in nums:
            while stack and stack[-1] > a:
                stack.pop()
            stack.append(a) # 1 2 3
            res += len(stack) #1,3,5,8,11
        return res