# Uses python3
'''
Number of Subarrays With LCM Equal to K
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000
'''

from math import gcd
from typing import List

class Solution:
    """
    Solution class to find the number of subarrays where the LCM equals k.
    """
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        """
        Find the number of subarrays where the LCM of the subarray equals k.
        
        Args:
            nums: List of integers
            k: Target LCM value
            
        Returns:
            int: Number of subarrays with LCM equal to k
        """
        def lcm(a: int, b: int) -> int:
            """
            Calculate the Least Common Multiple (LCM) of two numbers.
            
            Formula: LCM(a, b) = |a * b| / GCD(a, b)
            Using integer division for efficiency and to avoid floating point operations.
            """
            return a // gcd(a, b) * b  # Calculate LCM using GCD

        n = len(nums)
        ans = 0  # Initialize counter for valid subarrays
        
        # Iterate through all possible starting indices of subarrays
        for i in range(n):
            l = 1  # Initialize LCM for current starting index
            
            # Check all subarrays starting at index i
            for j in range(i, n):
                # If current number doesn't divide k, no subarray starting at i
                # can have LCM k, so we can break early
                if k % nums[j] != 0:
                    break
                    
                # Update LCM for current subarray
                l = lcm(l, nums[j])
                
                # If current LCM matches k, increment counter
                if l == k:
                    ans += 1
                # If LCM exceeds k, no need to check longer subarrays
                # as LCM is non-decreasing with array length
                elif l > k:
                    break
                    
        return ans

if __name__ == "__main__":
    nums = [3]
    k = 2
    print(Solution().subarrayLCM(nums, k))