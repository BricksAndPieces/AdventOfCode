"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since
you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information
Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the
satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they
produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your
puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random
orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with
its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented
correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other
tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this
with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

--- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  #
#    ##    ##    ###
 #  #  #  #  #  #
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need
to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and
rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea
monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?
"""

from collections import deque
from itertools import product
import numpy as np
import math

from aoc import *


def tile_edges(tile):
    return {"U": tile[0], "D": tile[-1], "L": tile[:, 0], "R": tile[:, -1]}

tiles = dict()
for raw_tile in puzzle_input(20, 2020, sample=False).split('\n\n'):
    lines = raw_tile.split('\n')
    key = int(lines[0][5:-1])
    lines = lines[1:]

    tile = np.zeros((10, 10), dtype=np.str)
    for x, y in product(range(10), repeat=2):
        tile[x][y] = lines[x][y]

    tiles[key] = tile

tileSize = len(tiles[list(tiles.keys())[0]])
tileConnections = {}
for tile1ID, tile1 in tiles.items():
    for tile2ID, tile2 in tiles.items():
        if tile1ID == tile2ID: continue

        for side1Direction, side1 in tile_edges(tile1).items():
            for side2Direction, side2 in tile_edges(tile2).items():
                if (side1 == side2).all() or (side1 == side2[::-1]).all():
                    if tile1ID not in tileConnections:
                        tileConnections[tile1ID] = {}
                    tileConnections[tile1ID][side1Direction] = tile2ID

cornerTiles = [tileID for tileID, conns in tileConnections.items() if len(conns) == 2]
print(f'Part 1: {mult(cornerTiles)}')

mov4 = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
dirsOpposite = {"D": "U", "U": "D", "L": "R", "R": "L"}
dirsRot90CW = {"D": "L", "U": "R", "L": "U", "R": "D"}
dirsFlipH = {k: (v if k in "LR" else dirsOpposite[v]) for k, v in dirsOpposite.items()}

dim = int(math.sqrt(len(tiles)))
img = np.zeros((dim, dim), dtype=np.ndarray)

startTile = cornerTiles[0]
if all(c in tileConnections[startTile] for c in "DR"):  # Top-left
    startPos = (0, 0)
elif all(c in tileConnections[startTile] for c in "DL"):  # Top-right
    startPos = (0, len(img) - 1)
elif all(c in tileConnections[startTile] for c in "UR"):  # Bottom-left
    startPos = (len(img) - 1, 0)
elif all(c in tileConnections[startTile] for c in "UL"):  # Bottom-right
    startPos = (len(img) - 1, len(img) - 1)

# BFS starting from the picked corner until the grid is filled
queue = deque([(startPos, startTile)])
tilesPlaced = set()
while queue:
    pos, tile = queue.popleft()

    if tile in tilesPlaced:
        continue

    tilesPlaced.add(tile)
    img[pos] = tiles[tile]

    for direction, adjTile in tileConnections[tile].items():
        tries = 0
        while not (tile_edges(tiles[adjTile])[dirsOpposite[direction]] == tile_edges(tiles[tile])[direction]).all():
            if tries == 3:
                tiles[adjTile] = np.flip(tiles[adjTile], axis=1)
                tileConnections[adjTile] = {dirsFlipH[k]: v for k, v in tileConnections[adjTile].items()}
            else:
                tiles[adjTile] = np.rot90(tiles[adjTile], 3)
                tileConnections[adjTile] = {dirsRot90CW[k]: v for k, v in tileConnections[adjTile].items()}
            tries += 1

        delta = mov4[direction]
        nxtPos = (pos[0] + delta[0], pos[1] + delta[1])
        queue.append((nxtPos, adjTile))

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- #

# Remove the borders of each tile
for x, y in product(range(dim), repeat=2):
    img[x][y] = img[x][y][1:9, 1:9]

# Create a 2d array of the actual image
rows = [reduce(lambda a, b: np.concatenate((a, b), axis=1), img[y]) for y in range(dim)]
img = reduce(lambda a, b: np.concatenate((a, b), axis=0), rows)

# Monster as a 2d array
monster = [list('                  # '),
           list('#    ##    ##    ###'),
           list(' #  #  #  #  #  #   ')]
hash_per_monster = 15


def num_monsters(img):
    count = 0
    for x in range(len(img) - len(monster)):
        for y in range(len(img[0]) - len(monster[0])):
            if contains_monster(img[x:x+len(monster), y:y+len(monster[0])]):
                count += 1

    return count


def contains_monster(img_section):
    for x in range(len(img_section)):
        for y in range(len(img_section[0])):
            if monster[x][y] == '#' and img_section[x][y] != '#':
                return False

    return True


def tile_versions(tile):
    versions = []
    for t in tile_rotations(tile):
        versions.append(t)
        versions.append(t[::-1])

    return versions


def tile_rotations(tile: np.ndarray):
    versions = [tile]
    for i in range(3):
        versions.append(np.rot90(versions[-1]))

    return versions


img_versions = tile_versions(img)
most_monsters = max(num_monsters(v) for v in img_versions)
num_hash = np.count_nonzero(img == '#')
print(f'Part 2: {num_hash - hash_per_monster * most_monsters}')