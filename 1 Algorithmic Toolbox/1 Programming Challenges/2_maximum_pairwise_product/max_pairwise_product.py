#!/usr/bin/env python3
"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Module for solving the Maximum Product of Two Elements in an Array problem.
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""

from typing import List, Dict
import math
import heapq


class MaxPairwiseProduct:
    """
    Class for solving the Maximum Product of Two Elements in an Array problem.
    """
    def max_kwise_product_with_heap(self, nums: List[int], k: int) -> int:
        """
        Finds the product of (n-1) for the k largest numbers in the list.
        This implementation uses the heapq module for an optimal and readable solution.
        The time complexity is O(n log k).  
        """
        # heapq.nlargest is an efficient way to find the k largest items in an iterable.
        # It has an O(n log k) time complexity. For k=2, this is O(n).
        k_largest = heapq.nlargest(k, nums)
        return math.prod(k_largest)

    def max_pairwise_product_with_adversarial_strategy(self, nums: List[int]) -> int:
        """
        Finds the maximum product of two elements in the list using an adversarial strategy.
        The time complexity is O(n). Specifically [n + ceiling(log2(n))) - 2].
        No algorithm can be faster than this.
        """
        adversaries = {}
        max_adversary = self.max_adversary(nums, 0, len(nums) - 1, adversaries)
        first_max = nums[max_adversary]
        adversaries_of_max_adversary = list(map(lambda x: nums[x], adversaries[max_adversary]))
        second_max = adversaries_of_max_adversary[
            self.max_adversary(adversaries_of_max_adversary,
                               0, len(adversaries_of_max_adversary) - 1, {})]
        return (first_max-1) * (second_max-1)

    def max_adversary(self, nums: List[int], i: int, j: int,
                      adversaries: Dict[int, List[int]]) -> int:
        """
        Finds the maximum adversary for a given range of numbers.
        """
        if i == j:
            return i
        mid = (i + j) // 2
        left_adversary = self.max_adversary(nums, i, mid, adversaries)
        right_adversary = self.max_adversary(nums, mid + 1, j, adversaries)
        adversaries[left_adversary] = adversaries.get(left_adversary, []) + [right_adversary]
        adversaries[right_adversary] = adversaries.get(right_adversary, []) + [left_adversary]
        if nums[left_adversary] > nums[right_adversary]:
            return left_adversary
        return right_adversary

if __name__ == "__main__":
    input_nums = [1,5,4,5]
    print(MaxPairwiseProduct().max_kwise_product_with_heap(input_nums, 2))
    print(MaxPairwiseProduct().max_pairwise_product_with_adversarial_strategy(input_nums))
