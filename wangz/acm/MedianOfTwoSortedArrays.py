# encoding:utf-8
class MedianOfTwoSortArrays(object):
    """
        问题:两个有序数组，计算其中值
        例如: nums1 = [1, 3] nums2 = [2] ，ans = 2.0
             nums1 = [1, 2] nums2 = [3, 4] ans = 2+3/2 = 2.5
    """

    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        mid_index = (len1 + len2) / 2  # 当是偶数时，需要取mid+1和mid的值
        arr = [0]*(mid_index+1)  # 用来存放新的排序，到取到mid为止
        i = 0
        index1 = 0  # 用来记录两个数组的位置
        index2 = 0
        while i < mid_index + 1:
            if index1 >= len1:
                arr[i] = nums2[index2]
                index2 += 1
            elif index2 >= len2:
                arr[i] = nums1[index1]
                index1 += 1
            else:
                if nums1[index1] > nums2[index2]:
                    arr[i] = nums2[index2]
                    index2 += 1
                else:
                    arr[i] = nums1[index1]
                    index1 += 1

            i += 1

        if (len1 + len2) % 2 is 0:
            return (arr[mid_index] + arr[mid_index - 1]) / 2.0
        else:
            return arr[mid_index]


nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]
print MedianOfTwoSortArrays().findMedianSortedArrays(nums1, nums2)
