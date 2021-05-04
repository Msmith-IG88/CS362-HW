def calc_avg(nums):
    if len(nums) == 0:
        return "input invalid"
    else:
        for num in nums:
            if type(num) != int:
                return "input invalid"
        return float((sum(nums)/(len(nums))))


