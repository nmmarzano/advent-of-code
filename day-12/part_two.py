# Not proud of this one. Went looking for a hint and got the solution spoiled.
# Got stuck trying to find the "more efficient way to simulate the universe".
# Said solution was to simulate each axis separatedly until they looped and then calculate the LCM of that loop.

import math


input_moons = [
    {
        'x': 16, 'y': -8, 'z': 13,
        'vx': 0, 'vy': 0, 'vz': 0
    },
    {
        'x': 4, 'y': 10, 'z': 10,
        'vx': 0, 'vy': 0, 'vz': 0
    },
    {
        'x': 17, 'y': -5, 'z': 6,
        'vx': 0, 'vy': 0, 'vz': 0
    },
    {
        'x': 13, 'y': -3, 'z': 0,
        'vx': 0, 'vy': 0, 'vz': 0
    }
    ]


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def update_velocity(moon, moons, axis):
    for other in moons:
        if not moon == other:
            if other[axis] > moon[axis]:
                moon['v'+axis] += 1
            elif other[axis] < moon[axis]:
                moon['v'+axis] -= 1


def move(moon, axis):
    moon[axis] += moon['v'+axis]


def step(moons, axis):
    for moon in moons:
        update_velocity(moon, moons, axis)
    for moon in moons:
        move(moon, axis)


def first_repeat(moons, axis):
    steps = set(())
    current_step = 1
    state = ''.join([str(x[axis]) for x in moons] + [str(x['v'+axis]) for x in moons])
    steps.add(state)
    while True:
        step(moons, axis)
        state = ''.join([str(x[axis]) for x in moons] + [str(x['v'+axis]) for x in moons])
        if state in steps:
            break
        else:
            steps.add(state)
        current_step += 1
    return current_step
    

if __name__ == '__main__':
    x_loop = first_repeat(input_moons, 'x')
    y_loop = first_repeat(input_moons, 'y')
    z_loop = first_repeat(input_moons, 'z')
    print(lcm(lcm(x_loop, y_loop), z_loop))
