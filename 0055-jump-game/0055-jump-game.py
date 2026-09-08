class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        
        for i, num in enumerate(nums):
            # If current index is beyond the furthest reachable index, we can't proceed
            if i > max_reach:
                return False
            
            # Update the furthest index reachable so far
            max_reach = max(max_reach, i + num)
            
            # Optimization: If we can reach or exceed the last index, return True immediately
            if max_reach >= len(nums) - 1:
                return True
                
        return True