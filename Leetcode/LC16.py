class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        Final_Ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if abs(target - Sum) < abs(target - Final_Ans):
                    Final_Ans = Sum
                    if Final_Ans == target:
                        return target
                if (Sum - target) < 0:
                    j += 1
                else:
                    k -= 1
        return Final_Ans
