import basepath
import utils.io as io
import math

test_cases = io.read_int()

for i in range(test_cases):
    line = input().split()
    shield = int(line[0])
    program = list(line[1])

    hacks_count = 0
    total_dmg = 0
    shoot_count = 0
    current_dmg = 1

    for char in program:
        if char == 'C':
            current_dmg <<= 1
        else:
            shoot_count += 1
            total_dmg += current_dmg

    if shoot_count == 0:
        io.out(i + 1, "0")
        continue
    elif shoot_count > shield:
        io.out(i + 1, "IMPOSSIBLE")
        continue

    while program[-1] == 'C':
        del program[-1]
        current_dmg >>= 1

    shoot_series_len = 0
    for char in reversed(program):
        if char == 'S':
            shoot_series_len += 1
        else:
            if shoot_series_len > 0:
                dmg_diff = total_dmg - shield
                shield_saved_on_one_hack = current_dmg >> 1
                hacks = min(shoot_series_len, int(math.ceil(dmg_diff / shield_saved_on_one_hack)))
                total_dmg -= hacks * shield_saved_on_one_hack
                current_dmg >>= 1
                hacks_count += hacks

        if total_dmg <= shield:
            io.out(i + 1, str(hacks_count))
            break
