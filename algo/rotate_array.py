nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

# right rotate
n = len(nums)
	    k %= n
	    nums[:] = nums[n-k:] + nums[:n-k]

# left rotate
n = len(nums)
	    k %= n
	    nums[:] = nums[k:] + nums[0:k]