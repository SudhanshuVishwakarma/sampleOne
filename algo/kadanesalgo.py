def maxSubArraySum(a, size):

    max_till_now = a[0]
    max_ending_here = 0

    for n in range(0, size):
        max_ending_here = max_ending_here + a[n]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_till_now < max_ending_here:
            max_till_now = max_ending_here
    return max_till_now


a = [-2, -3, 4, -1, -2, 5, -3]

print("maximum contiguous sum is", maxSubArraySum(a, len(a)))
