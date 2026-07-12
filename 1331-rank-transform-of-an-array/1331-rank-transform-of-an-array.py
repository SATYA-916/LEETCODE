class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d,c={},1
        for i in sorted(arr):
            if i not in d:
                d[i]=c
                c+=1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr