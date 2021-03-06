"""
 Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 Example:

 Input: nums = [-2,0,1,3], and target = 2
 Output: 2
 Explanation: Because there are two triplets which sums are less than 2:
              [-2,0,1]
              [-2,0,3]
 Follow up: Could you solve it in O(n2) runtime?
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
        
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[0] + nums[1] + nums[2] > target:
                    break
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),...,
                # (i,j,j+1) all work, totally (k-j) triplets
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count
