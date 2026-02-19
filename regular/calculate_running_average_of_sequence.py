def running_mean(sequence):
    running_sum = 0
    ans = []
    for count, value in enumerate(sequence, start=1):
        running_sum += value
        ans.append(round(running_sum / count, 2))

    return ans
