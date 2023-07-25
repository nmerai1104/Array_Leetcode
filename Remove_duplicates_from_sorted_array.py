class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        new_list = OrderedDict()
        for i in range(n-1,-1,-1):
            if nums[i] not in new_list:
                new_list[nums[i]]=1
            else:
                del nums[i]
        return len(new_list)
