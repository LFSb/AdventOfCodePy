from Util import returnFileAsArray

arr = returnFileAsArray(3, False)


def returnSlicedPostionOfArray(index, arr):
    ret = ""

    for y in range(0, len(arr)):
        ret += arr[y][index]

    return ret


def p1():
    lineLength = len(arr[0])
    halfway = len(arr) / 2

    gamma = ""
    epsilon = ""

    for x in range(0, lineLength):  # depth

        res = returnSlicedPostionOfArray(x, arr)

        ones = res.count('1')

        if(ones > halfway):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def bitwiseFilterArray(arr, isMsb):

    lineLength = len(arr[0])

    result = ""

    for x in range(0, lineLength):  # travel the array by depth
        res = returnSlicedPostionOfArray(x, arr)

        halfway = len(arr) / 2

        msb = '1' if res.count('1') >= halfway else '0'

        if(isMsb):
            arr = list(filter(lambda l: l[x] == msb, arr))
        else:
            arr = list(filter(lambda l: l[x] != msb, arr))

        if(len(arr) == 1):
            result = arr[0]

    return result


def p2():

    lsr = bitwiseFilterArray(arr, True)
    ogr = bitwiseFilterArray(arr, False)

    return int(lsr, 2) * int(ogr, 2)

if __name__ == "__main__":
    print(p1())
    print(p2())
