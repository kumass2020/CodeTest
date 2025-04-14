class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt = defaultdict(list)

        for i in range(len(nums)):
            # if dt.get(nums[i]):
            #     nums2 = dt.get(nums[i])
            #     for num2 in nums2:
            #         if abs(i-num2) <= k:
            #             return True

            dt[nums[i]].append(i)

        for key, value in dt.items():
            N = len(value)
            if N >= 2:
                for i in range(N):
                    for j in range(i+1, N):
                        if abs(value[i] - value[j]) <= k:
                            return True

        return False

            