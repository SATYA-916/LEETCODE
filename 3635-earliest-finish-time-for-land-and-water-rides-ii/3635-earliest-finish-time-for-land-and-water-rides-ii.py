class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m=float('inf')
        m1=float('inf')
        for i in range(len(landStartTime)):
            m=min(landStartTime[i]+landDuration[i],m)
        for i in range(len(waterStartTime)):
            st=m
            if m<=waterStartTime[i]:
                st=waterStartTime[i]+waterDuration[i]
            else:
                st=st+waterDuration[i]
            m1=min(m1,st)
        m=float('inf')
        for i in range(len(waterStartTime)):
            m=min(waterStartTime[i]+waterDuration[i],m)
        for i in range(len(landStartTime)):
            st=m
            if m<=landStartTime[i]:
                st=landStartTime[i]+landDuration[i]
            else:
                st=st+landDuration[i]
            print(st)
            m1=min(m1,st)
        return m1

        


        
        
                

        