class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # nums.sort()
        # I cant sort as i have to return the Indexs, stupid me
        Indexs = {}
        for index, Value in enumerate(nums):
            if Value not in Indexs:
                Indexs[Value] = [index]
            else:
                Indexs[Value].append(index)
        for index1, number in enumerate(nums):
            my_target = target - number
            if my_target in Indexs:
                for index2 in Indexs[my_target]:
                    if index1 != index2:
                        return [index1,  index2]
