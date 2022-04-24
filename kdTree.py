import math


class Cordinate:
    best_distance = 0
    k = 2

    def __init__(self, x, y) -> None:
        self.cordl = [x, y]
        self.x = x
        self.y = y


def distance(x1, x2, y1, y2) -> int:
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)


def bulid_kdtree(items, depth=0):
    sorted_items = []
    n = len(items)
    if n <= 0:
        return None
    sorted_items = sorted(items,
                          key=lambda item: item.cordl[depth % Cordinate.k])
    depth += 1
    return {
        'item': sorted_items[int(n / 2)],
        'left': bulid_kdtree(sorted_items[:int(n / 2)], depth),
        'right': bulid_kdtree(sorted_items[int(n / 2 + 1):])
    }


def best_item_distance(item1: Cordinate, item2: Cordinate, pivot: Cordinate):
    if item1 is None:
        return item2
    if item2 is None:
        return item1
    if distance(item1.x, pivot[0], item1.y, pivot[1]) < distance(
                                                                item2.x,
                                                                pivot[0],
                                                                item2.y,
                                                                pivot[1]):
        return item1
    else:
        return item2


def neighbor_item(pivot, items, depth):
    if items is None:
        return None
    next_branch = None
    opposite_branch = None
    curr_n = depth % Cordinate.k
    if pivot[curr_n] > items['item'].cordl[curr_n]:
        next_branch = items['right']
        opposite_branch = items['left']
    else:
        next_branch = items['left']
        opposite_branch = items['right']
    best = best_item_distance(
                                            neighbor_item(pivot,
                                                          next_branch, depth),
                                            items['item'], pivot)
    dist_best = distance(pivot[0], best.cordl[0], pivot[1], best.cordl[1])
    if dist_best > abs(pivot[curr_n] - items['item'].cordl[curr_n]):
        best = best_item_distance(neighbor_item(
                                                pivot, opposite_branch,
                                                depth), best, pivot)
    return best
