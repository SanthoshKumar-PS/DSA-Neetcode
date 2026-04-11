class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for num in (nums2):
            while stack and stack[-1]<num:
                idx = stack.pop()
                dic[idx] = num
            stack.append(num)
        return [dic.get(num,-1) for num in nums1]
        