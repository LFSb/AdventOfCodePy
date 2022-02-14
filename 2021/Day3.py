from Util import returnFileAsArray

arr = returnFileAsArray(3, False)


def p1():
    lineLength = len(arr[0])
    halfway = len(arr) / 2

    gamma = ""
    epsilon = ""

    for x in range(0, lineLength):  # depth
        res = ""

        for i in range(0, len(arr)):
            res += arr[i][x]

        ones = res.count('1')

        if(ones > halfway):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def p2():
    return "p2"


if __name__ == "__main__":
    print(p1())
    print(p2())
