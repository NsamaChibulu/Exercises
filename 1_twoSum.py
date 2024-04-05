class Solution:
    def twoSum(self,nums, target):
        # Create an empty hash table to sore elements
        # and their indices
        numMap = {}
        n = len(nums)

        # Build hash table
        for i in range(n):
            numMap[nums[i]] = i

        # For each element nums[i], calculate the complement
        # by subtracting it from the target
        # complement = target - nums[i]
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

nums = [1, 2, 3, 4, 5, 6]
myObject = Solution()
target = 5 
output = myObject.twoSum(nums, target)
print(output)

    

