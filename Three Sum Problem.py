def find_triplets(nums):
    nums.sort()
    n = len(nums)
    result = []
    
    def two_sum(i):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        two_sum(i)

    return result
