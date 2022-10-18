class Solution(object):
        
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_list = []
        for i in nums:
            if i == 0:
                continue
            if i not in unique_list:
                unique_list.append(i)
        return (len(unique_list))
        
    