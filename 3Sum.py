class Solution:
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        n=len(nums)
        solutions = set()
        nums.sort()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum == 0:
                        solutions.add((nums[i], nums[j], nums[k]))
                if triplet_sum <= 0:  
                        j += 1
                elif triplet_sum > 0:
                        k -= 1
        return list(map(list, solutions))
