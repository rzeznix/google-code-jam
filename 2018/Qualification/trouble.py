import basepath
import utils.io as io

test_cases = io.read_int()

for i in range(test_cases):
    n = io.read_int()
    to_sort = io.read_ints()

    even = list(to_sort[::2])
    even.sort()
    odd = list(to_sort[1::2])
    odd.sort()

    index = 0
    index_odd = 0
    index_even = 0
    correct = True

    while correct and index_odd < len(odd) and index_even < len(even):
        if even[index_even] > odd[index_odd]:
            correct = False
            break

        index_even += 1
        index += 1

        if index_even == len(even):
            break

        if odd[index_odd] > even[index_even]:
            correct = False
            break

        index_odd += 1
        index += 1

    if correct:
        io.out(i + 1, "OK")
    else:
        io.out(i + 1, str(index))
