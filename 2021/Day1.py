from Util import returnFileAsArrayOfInt

arr = returnFileAsArrayOfInt(1, False)


def p1():
    inc = 0
    prev = arr[0]

    for i in range(0, len(arr)):
        if arr[i] > prev:
            inc += 1

        prev = arr[i]

    return inc


def p2():
    inc = 0
    prev = arr[0] + arr[1] + arr[2]

    for i in range(0, len(arr) - 2):
        sum = arr[i] + arr[i + 1] + arr[i + 2]
        if sum > prev:
            inc += 1

        prev = sum
    return inc


if __name__ == "__main__":
    print(p1())
    print(p2())
