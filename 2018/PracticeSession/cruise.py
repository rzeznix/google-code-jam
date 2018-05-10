import basepath
import utils.io as io

test_cases = int(input())
for i in range(test_cases):
    params = io.read_ints()
    distance = params[0]
    horses = params[1]
    max_time = 0

    for horse in range(horses):
        horse_params = io.read_ints()
        horse_position = horse_params[0]
        horse_speed = horse_params[1]
        distance_to_ride = distance - horse_position
        time = distance_to_ride / horse_speed
        if time > max_time:
            max_time = time

    max_speed = distance / max_time
    io.out(i + 1, "%.6f" % max_speed)
