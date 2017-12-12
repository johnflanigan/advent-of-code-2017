def memory_reallocation_part_one():
    f = open("day6_input.txt", "r")
    line = f.readline()
    memory = [int(x) for x in line.split("\t")]
    previous_configurations = []
    steps = 0
    while str(memory) not in previous_configurations:
        previous_configurations.append(str(memory))
        largest = 0
        # Find the largest block, break ties by taking first appearance
        for i in range(1, len(memory)):
            if memory[largest] < memory[i]:
                largest = i
        reallocating = memory[largest]
        memory[largest] = 0
        index = largest + 1
        # Reallocate memory
        while reallocating > 0:
            if index >= len(memory):
                index = 0
            memory[index] += 1
            index += 1
            reallocating -= 1
        steps += 1
    return steps


def memory_reallocation_part_two():
    f = open("day6_input.txt", "r")
    line = f.readline()
    memory = [int(x) for x in line.split("\t")]
    previous_configurations = []
    steps = 0
    while str(memory) not in previous_configurations:
        previous_configurations.append(str(memory))
        largest = 0
        # Find the largest block, break ties by taking first appearance
        for i in range(1, len(memory)):
            if memory[largest] < memory[i]:
                largest = i
        reallocating = memory[largest]
        memory[largest] = 0
        index = largest + 1
        # Reallocate memory
        while reallocating > 0:
            if index >= len(memory):
                index = 0
            memory[index] += 1
            index += 1
            reallocating -= 1
        steps += 1
    return steps - previous_configurations.index(str(memory))


print memory_reallocation_part_one()
print memory_reallocation_part_two()
