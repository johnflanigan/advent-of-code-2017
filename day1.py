def inverseCaptchaPartOne(x):
    x_string = str(x)
    total = 0
    for i in range(1, len(x_string)):
        if (x_string[i - 1] == x_string[i]):
            total += int(x_string[i])
    if (len(x_string) != 0 and x_string[0] == x_string[len(x_string) - 1]):
        total += int(x_string[0])
    print total


def inverseCaptchaPartTwo(x):
    x_string = str(x)
    total = 0
    half_of_length = len(x_string) / 2
    for i in range(0, half_of_length):
        if (x_string[i] == x_string[i + half_of_length]):
            total += int(x_string[i]) * 2

    print total


inverseCaptchaPartOne(1122)
inverseCaptchaPartOne(1111)
inverseCaptchaPartOne(1234)
inverseCaptchaPartOne(91212129)

inverseCaptchaPartTwo(1212)
inverseCaptchaPartTwo(1221)
inverseCaptchaPartTwo(123425)
inverseCaptchaPartTwo(123123)
inverseCaptchaPartTwo(12131415)
