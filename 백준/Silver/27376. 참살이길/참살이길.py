import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lights = [tuple(map(int, input().split())) for _ in range(k)]
lights.sort(key=lambda x: (x[0]))

current_time = 0
current_position = 0

for light in lights:
    x, t, s = light

    current_time += x - current_position

    time_since_first_green = (current_time - s) % (2 * t)
    if time_since_first_green < t:
        pass
    else:
        wait_time = 2 * t - time_since_first_green
        current_time += wait_time

    current_position = x

current_time += n - current_position

print(current_time)

