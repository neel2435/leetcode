class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        strings = []

        if not nums:
            return strings
            
        first = nums[0]
        last = 0

        for num in range(1, len(nums)):
            if nums[num-1] + 1 != nums[num]:

                last = nums[num-1]

                if (first != last):
                    strings.append(str(first) + "->" + str(last))
                    first = nums[num]
                else:
                    first = nums[num]
                    strings.append(str(last))
                    
            else:

                last = nums[num]

        last = nums[-1]
        
        if (first != last):
            strings.append(str(first) + "->" + str(last))
        else:
            strings.append(str(last))

        return strings