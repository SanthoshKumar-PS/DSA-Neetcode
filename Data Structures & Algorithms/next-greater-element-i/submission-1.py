class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        res = [-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                idx = stack.pop()
                dic[nums2[idx]] = nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            if nums1[i] in dic:
                nums1[i] = dic[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
