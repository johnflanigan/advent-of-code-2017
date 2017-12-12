def twisty_trampolines_part_one():
    f = open("day5_input.txt", "r")
    array = []
    for line in f:
        array.append(int(line))
    current = 0
    steps = 0
    while current >= 0 and current < len(array):
        new = current + array[current]
        array[current] += 1
        steps += 1
        current = new
    return steps


def twisty_trampolines_part_two():
    f = open("day5_input.txt", "r")
    array = []
    for line in f:
        array.append(int(line))
    current = 0
    steps = 0
    while current >= 0 and current < len(array):
        new = current + array[current]
        if array[current] >= 3:
            array[current] -= 1
        else:
            array[current] += 1
        steps += 1
        current = new
    return steps


print twisty_trampolines_part_one()
print twisty_trampolines_part_two()
