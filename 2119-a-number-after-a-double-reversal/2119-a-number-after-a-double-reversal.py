class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        reversed1 = str(num)[::-1]
        reversed1 = reversed1.lstrip('0')
        print(reversed1)
        reversed2 = reversed1[::-1]
        print(reversed2)
        if reversed2 != str(num):
            return False
        return True