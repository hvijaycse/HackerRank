class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        zeroes = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        zeroes = min( zeroes, 3)
        nums += [0 for _ in range( zeroes)]
        Answer = {}
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                summer = nums[i] + nums[j] + nums[k]
                if summer == 0:
                    key = '|'.join(str(i) for i in [nums[i], nums[j], nums[k]])
                    if key not in Answer:
                        Answer[key] = [nums[i], nums[j], nums[k]]
                    j += 1
                    k -= 1
                elif summer < 0:
                    j += 1
                else:
                    k -= 1

        return list(Answer.values())
