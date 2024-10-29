class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNumLength = self.findLargestPeriod(nums)
        for i in range(0, len(nums)):
            nums[i] = bin(nums[i])[2:]

        for i in range(0, len(nums)):
            nums[i] = len(nums[i])
        maxBitLength = self.findLargestPeriod(nums)

        if maxBitLength > maxNumLength:
            return maxNumLength
        else:
            return maxBitLength


    def findLargestPeriod(self, nums):
        # Initialize params
        maxNum = 0
        maxNumIndex = 0
        maxLength = 0

        # Find biggest number and index
        currentLength = 0
        for i in range(0, len(nums)):
            # break currentLength
            if maxNum > nums[i]:
                currentLength = 0

            # update maxNum
            elif maxNum < nums[i]:
                maxNum = nums[i]
                maxNumIndex = i
                maxLength = 1 
                currentLength = 1 # reset

            # longer the length
            elif maxNum == nums[i]:
                currentLength += 1
            
            if maxLength < currentLength:
                maxLength = currentLength

        return maxLength

        

                