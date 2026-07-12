class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h=int(endTime[:2])-int(startTime[:2])
        m=int(endTime[3:5])-int(startTime[3:5])
        s=int(endTime[6:])-int(startTime[6:])
        return s+m*60+h*60*60

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna