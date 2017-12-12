def corruption_checksum_part_one():
    f = open("day2_input.txt", "r")
    checksum = 0
    for line in f:
        values = [int(x) for x in line.split('\t')]
        checksum += max(values) - min(values)
    return checksum


def corruption_checksum_part_two():
    f = open("day2_input.txt", "r")
    checksum = 0
    for line in f:
        values = [int(x) for x in line.split('\t')]
        checksum += find_even_division_in_list(values)
    return checksum


def find_even_division_in_list(lst):
    lst.sort()
    for low in range(0, len(lst)):
        for high in range(low + 1, len(lst)):
            if lst[high] % lst[low] == 0:
                return lst[high] / lst[low]


print corruption_checksum_part_one()
print corruption_checksum_part_two()
