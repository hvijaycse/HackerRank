class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        Answer = []
        nums.sort()
        if len(nums) > 3:
            for First in range(0, len(nums) - 3):
                for Fourth in range(First + 3, len(nums)):
                    Second = First + 1
                    Third = Fourth - 1
                    while Second < Third:
                        tmp_Array = [nums[First], nums[Second],
                                     nums[Third], nums[Fourth]]
                        Summer = sum(tmp_Array)
                        if Summer == target:
                            if tmp_Array not in Answer:
                                Answer.append( tmp_Array )
                            Second += 1
                            Third -= 1
                        elif Summer < target:
                            Second += 1
                        else:
                            Third -= 1
        return Answer
