class Solution:
    def removeDuplicates(self, numbers: [int]) -> int:
        count = 0
        prev = ''
        index = 0
        while index < len(numbers):
            if prev != numbers[index]:
                prev = numbers[index]
                count += 1

            while index + 1 < len(numbers) and numbers[index] == numbers[index + 1]:
                numbers.pop(index + 1)
            index += 1
        return count