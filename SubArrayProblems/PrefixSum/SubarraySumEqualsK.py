'''
Problem: Subarray Sum Equals K
Platform: LeetCode

Since the array may contain negative numbers, the sliding window (two pointer) 
approach does NOT work reliably.

Instead, we use Prefix Sum + HashMap.

We maintain a running prefix sum. At each index:
- If (sum - k) exists in the hashmap, it means there is a subarray 
  ending at the current index whose sum is k.

Why?
Because:
    sum - previous_prefix_sum = k
→ So removing the previous prefix gives a subarray of sum k.

We store prefix sums in a hashmap along with their frequencies to count 
all such subarrays efficiently.
'''

