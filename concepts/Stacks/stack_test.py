buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"


def sunsetViews(buildings, direction):
    # Write your code here.
    res = []
    idx = 0
    while idx < len(buildings):
        print("idx:", idx)
        current = idx
        ittr = idx+1
        while current < len(buildings):
            print("current:", current)
            if buildings[ittr] > buildings[current]:
                print("largerst found")
                larger = buildings[ittr]
                print("larger: ", larger)
                print()

            current += 1
        idx += 1
        # if res[-1]
        res.append(larger)
        print(res)
        print("############################")

    return res


sunsetViews(buildings, direction)
