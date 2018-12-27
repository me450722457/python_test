origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        pos += step
        return pos

    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
