class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        l1=l1+l2
        l1.sort()
        print(l1,l1[len(l1)//2],l1[(len(l1)//2)-1])
        if len(l1)%2==0:
            return (l1[len(l1)//2]+l1[(len(l1)//2)-1])/2
        return l1[len(l1)//2]