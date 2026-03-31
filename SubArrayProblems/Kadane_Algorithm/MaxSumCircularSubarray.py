"""
Problem: Maximum Subarray Sum Circular
Platform: LeetCode
Algorithm: Kadane's Algorithm (Modified)

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Find maximum subarray sum using Kadane's algorithm.
2. Find minimum subarray sum using Kadane's algorithm.
3. Compute total sum of the array.
4. Circular max = total_sum - minimum_subarray_sum
5. Edge case: if all elements are negative, return max subarray.
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Step 1: Standard Kadane's (max subarray)
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], nums[i] + current_max)
            global_max = max(global_max, current_max)

        # Step 2: Kadane's for minimum subarray
        current_min = nums[0]
        global_min = nums[0]

        for i in range(1, len(nums)):
            current_min = min(nums[i], nums[i] + current_min)
            global_min = min(global_min, current_min)

        # Step 3: Total sum of array
        total_sum = sum(nums)

        # Step 4: Circular case
        circular_max = total_sum - global_min

        # Step 5: Edge case (all numbers are negative)
        if total_sum == global_min:
            return global_max

        # Final answer
        return max(global_max, circular_max)
