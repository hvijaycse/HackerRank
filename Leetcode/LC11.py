class Solution:
    def maxArea(self, height: [int]) -> int:
        Volume = 0
        Sorted_array = sorted(set(height))
        i = 0
        j = len(height) - 1

        for H in Sorted_array:
            if i >= j:
                break
            while i < len(height) and height[i] < H:
                i += 1
            while j > -1 and height[j] < H:
                j -= 1
            Volume = max(
                Volume,
                H*(j - i)
            )
        return Volume

#Got it in First chance