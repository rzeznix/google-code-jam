import basepath
import utils.io as io
import math


# Calculate min and max of Ls, Rs for series of stalls of length l
def min_max_lr(l):
    _min_lr = math.floor((l - 1) >> 1)
    _max_lr = math.floor(l >> 1)
    return int(_min_lr), int(_max_lr)

test_cases = io.read_int()
for i in range(test_cases):
    args = io.read_ints()
    n = args[0]
    k = args[1]
    # key = series length, value = series count
    series = {n: 1}
    while k > 0:
        max_series_length = max(series.keys())
        max_series_count = series.pop(max_series_length)
        min_lr, max_lr = min_max_lr(max_series_length)
        k -= max_series_count
        if k <= 0:
            io.out(i + 1, str(max_lr) + " " + str(min_lr))
        else:
            max_lr_series_count = series.get(max_lr, 0)
            series.update({max_lr: max_lr_series_count + max_series_count})
            min_lr_series_count = series.get(min_lr, 0)
            series.update({min_lr: min_lr_series_count + max_series_count})
