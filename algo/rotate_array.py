nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])


n = len(nums)
	    k %= n
	    nums[:] = nums[n-k:] + nums[:n-k]