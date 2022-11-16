class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        if len(triplets) == 1:
            if triplets[0] == target:
                return True
            else:
                return False
        
        pos = set()
        
        for i, [x,y,z] in enumerate(triplets):
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            else:
                pos.add(i)
            
        a,b,c = 0,0,0
        for i in pos:
            a = max(a, triplets[i][0])
            b = max(b, triplets[i][1])
            c = max(c, triplets[i][2])
        
        return a == target[0] and b == target[1] and c == target[2]
        
        
        