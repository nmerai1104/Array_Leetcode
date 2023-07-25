class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + sum(nums[i+1:i+4]) > target:
                break
            if nums[i] + sum(nums[-3:]) < target:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + sum(nums[j+1:j+3]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    currentSum = nums[i] + nums[j] + nums[left] + nums[right]

                    if currentSum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif currentSum < target:
                        left += 1
                    else:
                        right -= 1

        return result
