class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt = defaultdict(list)

        for i in range(len(nums)):
            if dt.get(nums[i]):
                nums2 = dt.get(nums[i])
                for num2 in nums2:
                    if abs(i-num2) <= k:
                        return True

            dt[nums[i]].append(i)

        return False

            