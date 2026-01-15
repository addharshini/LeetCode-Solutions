class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''hash map approach'''
        a={} # to store val:index {2:0,7:1,11:2,15:3} 
        for i,j in enumerate(nums):
            print(i,j)
            if target-j in a:
                return [i,a[target-j]]
            a[j]=i
        print(a)

        ''' Brute force approach: Accepted but T:o(n^2)''' 
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             print(i,j)
        #             return [i,j]