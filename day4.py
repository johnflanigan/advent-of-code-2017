def high_entropy_passphrases_part_one():
    f = open("day4_input.txt", "r")
    count = 0
    for line in f:
        line = line.replace("\n", "")
        words = line.split(" ")
        if no_duplicates_exist(words):
            count += 1
    print count


def high_entropy_passphrases_part_two():
    f = open("day4_input.txt", "r")
    count = 0
    for line in f:
        line = line.replace("\n", "")
        words = line.split(" ")
        rearrangedWords = []
        for word in words:
            rearrangedWords.append(sorted(word))
        if no_duplicates_exist(rearrangedWords):
            count += 1
    print count


def no_duplicates_exist(lst):
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            return False
    return True


high_entropy_passphrases_part_one()
high_entropy_passphrases_part_two()
