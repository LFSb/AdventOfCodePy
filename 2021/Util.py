import os

def returnFileAsArrayOfInt(day, isTest):
  with open(returnPath(day, isTest), "r") as file:
    arr = [int(i) for i in file]
    return arr

def returnFileAsArray(day, isTest):
  with open(returnPath(day, isTest), "r") as file:
    return file.readlines()

def returnPath(day, isTest):
  test = "Test" if isTest == True else ""
  return f"{os.getcwd()}/2021/Input/Day{day}{test}.txt"