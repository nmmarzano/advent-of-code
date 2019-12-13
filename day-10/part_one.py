import math, functools


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


def raycast(spacemap, xo, yo, xt, yt):
    result = 0
    xr = xt - xo
    yr = yt - yo
    div = math.gcd(xr, yr)
    i = 1
    while div > 0:
        x = (int)(xr/div)*i + xo
        y = (int)(yr/div)*i + yo
        if x < 0 or y < 0 or x >= len(spacemap) or y >= len(spacemap[0]):
            break
        if spacemap[x][y] == '#':
            result = 1
            break
        i += 1
    return result


def asteroids_in_sight(spacemap, x, y):
    tested_angles = set(())
    w = len(spacemap)
    h = (len(spacemap[0]))
    count = 0
    for x1 in range(w):
        for y1 in range(h):
            if x1 != x or y1 != y:
                div = math.gcd(x1-x, y1-y)
                angle = ((int)((x1-x)/div), (int)((y1-y)/div))
                if angle not in tested_angles:
                    count += raycast(spacemap, x, y, x1, y1)
                    tested_angles.add(angle)
    return count


def count_all(spacemap):
    results = []
    w = len(spacemap)
    h = (len(spacemap[0]))
    for y in range(h):
        for x in range(w):
            if spacemap[x][y] == '#':
                res = asteroids_in_sight(spacemap, x, y)
                results.append([(x, y), res])
    return results


def max_detects(count_list):
    return functools.reduce(lambda a, b: a if a[1] > b[1] else b, count_list)


def process_input(smap):
    smap = smap.split('\n')
    for i, row in enumerate(smap):
        smap[i] = list(row)
    smap = list(map(list, zip(*smap)))
    return smap


def main():
    spacemap = process_input(input_map)
    print(max_detects(count_all(spacemap)))
    

if __name__ == '__main__':
    main()
