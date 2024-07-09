class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        res=0
        for i in range(len(points)-1):
            res=max(res,points[i+1][0]-points[i][0])
        return res
        """
        :type points: List[List[int]]
        :rtype: int
        """
        