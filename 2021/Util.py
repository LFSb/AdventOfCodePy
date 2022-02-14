import os

def returnFileAsArrayOfInt(day):
  with open(f"{os.getcwd()}/2021/Input/Day{day}.txt", "r") as file:
    arr = [int(i) for i in file]
    return arr

def returnFileAsArray(day):
  with open(f"{os.getcwd()}/2021/Input/Day{day}.txt", "r") as file:
    return file.readlines()