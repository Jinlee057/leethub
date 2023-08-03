class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if nums1[m-1] >= nums2[n-1] and m>0: #각 리스트에서 마지막값끼리 비교
                nums1[m+n-1] = nums1[m-1] #nums1의 전체 길이는 m+n, 가장 마지막에 둘 중 큰값
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1                  #n이 0이되면 nums2 리스트내 모든 값 확인 완료