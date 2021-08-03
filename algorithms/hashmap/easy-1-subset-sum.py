class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Send all numbers in nums into all nums map
        all_nums = {}
        for num in range(len(nums)):
            all_nums[nums[num]] = num
        
        # Find the range and answer
        for num in range(len(nums)):
            if (target - nums[num]) in all_nums and num != all_nums[(target-nums[num])]:
                return [num, all_nums[(target-nums[num])]]     
                