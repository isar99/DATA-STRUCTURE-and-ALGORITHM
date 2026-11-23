class Solution:
    def maxArea1(self, heights):
        # TC -> N**2
        # SC -> N**2
        len_arr = len(heights)
        if len_arr <= 1:
            return 0
        water_areas = []
        for i in range(len(heights) -1):
            j = i+1
            while j < len(heights):
                height = min(heights[i], heights[j])
                width = j-i
                area = height*width
                water_areas.append(area)
                j += 1
        return max(water_areas)

class Solution:
    def maxArea2(self, heights):
        # TC -> N
        # SC -> 1
        left = 0
        right = len(heights)-1
        max_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height*width
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area



if __name__ == "__main__":
    heights = [1,7,2,5,4,7,3,6]
    sol = Solution()
    result = sol.maxArea2(heights)
    print(result)

