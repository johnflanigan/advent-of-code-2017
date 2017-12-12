def inverseCaptchaPartOne(x):
    x_string = str(x)
    total = 0
    for i in range(1, len(x_string)):
        if x_string[i - 1] == x_string[i]:
            total += int(x_string[i])
    return total


def inverseCaptchaPartTwo(x):
    x_string = str(x)
    total = 0
    half_of_length = len(x_string) / 2
    for i in range(0, half_of_length):
        if x_string[i] == x_string[i + half_of_length]:
            total += int(x_string[i]) * 2
    return total


print inverseCaptchaPartOne(1122)
print inverseCaptchaPartOne(1111)
print inverseCaptchaPartOne(1234)
print inverseCaptchaPartOne(91212129)

print inverseCaptchaPartTwo(1212)
print inverseCaptchaPartTwo(1221)
print inverseCaptchaPartTwo(123425)
print inverseCaptchaPartTwo(123123)
print inverseCaptchaPartTwo(12131415)
