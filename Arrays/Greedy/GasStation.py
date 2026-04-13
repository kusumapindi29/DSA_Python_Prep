'''
Problem : Gas Station
Platform : Leetcode
Pattern : Greedy Approach

let us start from starting position and if total is less than 0
then we know we can bot start from that, so make total zero and go from next index, 
but assume next index will be the result and start, if it fails next will be the result, 
in that intuition we go to end of the array and if total is greater than zero or zero we know that is the starting index.

we dont need to go cyclic because we know startig indexes wont make it, if they make it that would be the unique solution

Time Complexity : O(n)
Space Complexity : O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        total=0
        if sum(gas)>=sum(cost):
            for i in range(0,len(gas)):
                total+=gas[i]-cost[i]
                if total<0:
                    total =0
                    start = i+1
            return start
        else:
            return -1
