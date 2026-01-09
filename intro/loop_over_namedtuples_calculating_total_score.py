from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=None):
    if belts is None:
        belts = ninja_belts
    points = 0
    for stats in belts.values():
        points += stats.score * stats.ninjas

    return points
