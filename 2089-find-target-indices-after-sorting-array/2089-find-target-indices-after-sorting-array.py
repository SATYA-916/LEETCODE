class Solution:
    def targetIndices(self, arr: List[int], t: int) -> List[int]:
        arr.sort()
        ans=[]
        for i in range(len(arr)):
            if arr[i]==t:
                ans.append(i)
        return ans

        