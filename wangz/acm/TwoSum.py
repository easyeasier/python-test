#encoding:utf-8
class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dic = {}
        length= len(nums)
        i=0
        while(i<length):
            if(nums_dic.has_key(target-nums[i])):
                return [nums[target-nums[i]],i]
            else:
                nums_dic[nums[i]]=i
                i+=1
        raise Exception("wrong nums")

s = Solution()
ret=s.twoSum([2,7,11,15],9)
print ret