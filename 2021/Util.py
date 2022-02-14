import pathlib
base = pathlib.Path(__file__).parent.resolve()


def returnFileAsArrayOfInt(day, isTest):
    with open(returnPath(day, isTest), "r") as file:
        arr = [int(i) for i in file]
        return arr


def returnFileAsArray(day, isTest):
    with open(returnPath(day, isTest), "r") as file:
        return file.read().splitlines()


def returnPath(day, isTest):
    test = "Test" if isTest == True else ""
    return f"{base}/Input/Day{day}{test}.txt"
