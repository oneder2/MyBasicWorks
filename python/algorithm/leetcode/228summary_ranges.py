from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 1:
        return [f"{nums[0]}->{nums[1]}"]

    ans = []
    l, r  = nums[0], nums[0]
    for num in nums[1:]:
        if r + 1 == num:
            r = num
        else:
            if l != r:
                ans.append(f"{l}->{r}")
            else:
                ans.append(l)
            l = num
            r = num
    if l == r:
        ans.append(l)
    else:
        ans.append(f"{l}->{r}")
    return ans


nums = [0,1,2,4,5,7,8]
print(summaryRanges(nums))
