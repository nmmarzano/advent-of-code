import math, functools, sys


input_map = '''#.....#...#.........###.#........#..
....#......###..#.#.###....#......##
......#..###.......#.#.#.#..#.......
......#......#.#....#.##....##.#.#.#
...###.#.#.......#..#...............
....##...#..#....##....#...#.#......
..##...#.###.....##....#.#..##.##...
..##....#.#......#.#...#.#...#.#....
.#.##..##......##..#...#.....##...##
.......##.....#.....##..#..#..#.....
..#..#...#......#..##...#.#...#...##
......##.##.#.#.###....#.#..#......#
#..#.#...#.....#...#...####.#..#...#
...##...##.#..#.....####.#....##....
.#....###.#...#....#..#......#......
.##.#.#...#....##......#.....##...##
.....#....###...#.....#....#........
...#...#....##..#.#......#.#.#......
.#..###............#.#..#...####.##.
.#.###..#.....#......#..###....##..#
#......#.#.#.#.#.#...#.#.#....##....
.#.....#.....#...##.#......#.#...#..
...##..###.........##.........#.....
..#.#..#.#...#.....#.....#...###.#..
.#..........#.......#....#..........
...##..#..#...#..#...#......####....
.#..#...##.##..##..###......#.......
.##.....#.......#..#...#..#.......#.
#.#.#..#..##..#..............#....##
..#....##......##.....#...#...##....
.##..##..#.#..#.................####
##.......#..#.#..##..#...#..........
#..##...#.##.#.#.........#..#..#....
.....#...#...#.#......#....#........
....#......###.#..#......##.....#..#
#..#...##.........#.....##.....#....'''


def raycast_by_angle(spacemap, xo, yo, angle):
    result = 0
    x = xo
    y = yo
    while True:
        x += angle[0]
        y -= angle[1]
        if not (x < len(spacemap) and y < len(spacemap[0])
                and x >= 0 and y >= 0):
            break
        if spacemap[x][y] == '#':
            result = 1
            break
    return (result, x, y)


def get_key_from_angle(angle):
    if angle[1] != 0:
        return angle[0] / angle[1]
    else:
        return sys.maxsize


def get_sorted_angles_quadrant(spacemap, x, y, q):
    xm = 0 - x -1
    ym = 0 - (len(spacemap[0]) - y)
    if q == 1 or q == 2:
        xm = len(spacemap) - x
    if q == 1 or q == 4:
        ym = y + 1
        
    angles = set(())
    for x in range(0, xm, -1 if xm < 0 else 1):
        for y in range(0, ym, -1 if ym < 0 else 1):
            if x!=0 or y!=0:
                div = math.gcd(x, y)
                angle = ((int)(x/div), (int)(y/div))
                angles.add(angle)
    angles = sorted(list(angles),
                    key=get_key_from_angle)
    
    if q == 2 and (1,0) in angles:
        angles.remove((1,0))
    if q == 3 and (0,-1) in angles:
        angles.remove((0,-1))
    if q == 4:
        if (-1,0) in angles:
            angles.remove((-1,0))
        if (0,1) in angles:
            angles.remove((0,1))
        
    return angles


def get_sorted_angles(spacemap, x, y):
    q = []
    for i in range(1, 5):
        q += get_sorted_angles_quadrant(spacemap, x, y, i)
    return q


def shoot_in_sight_until(spacemap, x, y, top):
    count = 0
    result = (0, 0, 0)
    while count < top:
        for angle in get_sorted_angles(spacemap, x, y):
            result = raycast_by_angle(spacemap, x, y, angle)
            if result[0] == 1:
                count += 1
                spacemap[result[1]][result[2]] = '.'
                if count == top:
                    break
    return (result[1], result[2])


def process_input(smap):
    smap = smap.split('\n')
    for i, row in enumerate(smap):
        smap[i] = list(row)
    smap = list(map(list, zip(*smap)))
    return smap


def main():
    spacemap = process_input(input_map)
    (x, y) = shoot_in_sight_until(spacemap, 26, 29, 200)
    print(x*100 + y)
    

if __name__ == '__main__':
    main()
