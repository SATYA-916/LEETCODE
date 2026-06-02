class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=float('inf')
        ans=0
        for i in range(len(landStartTime)):
            ans=landStartTime[i]+landDuration[i]
            st=ans
            for j in range(len(waterStartTime)):
                if waterStartTime[j]<=ans:
                    ans=ans+waterDuration[j]
                else:
                    ans=ans+(waterStartTime[j]-ans)+waterDuration[j]
                res=min(res,ans)
                ans=st
        for i in range(len(waterStartTime)):
            ans=waterStartTime[i]+waterDuration[i]
            st=ans
            for j in range(len(landStartTime)):
                if landStartTime[j]<=ans:
                    ans=ans+landDuration[j]
                else:
                    ans=landStartTime[j]+landDuration[j]
                res=min(res,ans)
                ans=st
        return res
                

        