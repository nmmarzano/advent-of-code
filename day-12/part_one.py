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


def update_velocity(moon, rest):
    for r in rest:
        difx = r['x'] - moon['x']
        dify = r['y'] - moon['y']
        difz = r['z'] - moon['z']
        if difx != 0:
            moon['vx'] += (difx)//abs(difx)
        if dify != 0:
            moon['vy'] += (dify)//abs(dify)
        if difz != 0:
            moon['vz'] += (difz)//abs(difz)


def move(moon):
    moon['x'] += moon['vx']
    moon['y'] += moon['vy']
    moon['z'] += moon['vz']


def step(moons):
    for moon in moons:
        update_velocity(moon, [m for m in moons if m != moon])
    for moon in moons:
        move(moon)


def total_energy(moons):
    total = 0
    potential_energy = 0
    kinetic_energy = 0
    for moon in moons:
        potential_energy = abs(moon['x']) + abs(moon['y']) + abs(moon['z'])
        kinetic_energy = abs(moon['vx']) + abs(moon['vy']) + abs(moon['vz'])
        total += potential_energy * kinetic_energy
    return total


if __name__ == '__main__':
    for i in range(1000):
        step(input_moons)
    print(total_energy(input_moons))
