buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"


def sunsetViews(buildings, direction):
    # Write your code here.
    res = []

    idx = 0 if direction == 'WEST' else len(buildings)-1
    step = 1 if direction == 'WEST' else -1

    maxHeight = 0

    while idx >= 0 and idx < len(buildings):

        if buildings[idx] > maxHeight:
            res.append(idx)

        maxHeight = max(maxHeight, buildings[idx])
        idx += step

    if direction == 'EAST':
        res = res[::-1]

    print(res)
    return res


sunsetViews(buildings, direction)
