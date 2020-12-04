"""
--- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy.
Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole
seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while
Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a
total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second,
when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer
has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the
winning reindeer traveled?

--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple
reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as
doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the
lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his
first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points
by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with
the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does
the winning reindeer have?
"""

from aoc import *


def dist(t, speed, move_time, rest_time):
    d = 0
    moving = True

    while t > 0:
        if moving:
            d += speed * min(move_time, t)
            t -= min(move_time, t)
            moving = False
        else:
            t -= rest_time
            moving = True

    return d


def part1(inputs):
    most_dist = 0
    for i in inputs:
        parts = i.split(' ')
        speed = int(parts[3])
        move_time = int(parts[6])
        rest_time = int(parts[-2])

        t = 2503
        d = dist(t, speed, move_time, rest_time)
        most_dist = max(most_dist, d)

    return most_dist


def part2(inputs):
    reindeers = []
    for i in inputs:
        reindeer = []
        parts = i.split(' ')
        reindeer.append(int(parts[3]))
        reindeer.append(int(parts[6]))
        reindeer.append(int(parts[-2]))
        reindeer.append(0)
        reindeers.append(reindeer)

    for t in range(1, 2504):
        dists = [dist(t, r[0], r[1], r[2]) for r in reindeers]
        max_dist = max(dists)
        for i, reindeer in enumerate(reindeers):
            if dists[i] == max_dist:
                reindeer[-1] += 1

    points = [x[-1] for x in reindeers]
    return max(points)


puzzle_input = puzzle_input(14, 2015).split('\n')
print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
