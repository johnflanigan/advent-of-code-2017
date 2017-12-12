def spiral_memory(x):
    i = 1
    # construct ranges
    steps = []
    count = 0
    while i < x:
        steps.append(i)
        i += 8 * count
        count += 1
    steps.append(i)
    # calculate distance to nearest mid point
    high = steps[count]
    low = steps[count - 1]
    distance = (high - low + 1) / 4
    start = low + count - 1
    lst = []
    for index in range(0, 4):
        current = start + distance * index
        lst.append(abs(x - current))
    return min(lst) + count - 1


print spiral_memory(1)
print spiral_memory(12)
print spiral_memory(23)
print spiral_memory(1024)
print spiral_memory(277678)
