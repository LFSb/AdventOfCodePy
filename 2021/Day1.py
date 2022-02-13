import os

with open(f"{os.getcwd()}/2021/Input/Day1.txt", "r") as file:
  arr = [int(i) for i in file]

if __name__ == "__main__":
  increases = 0
  prev = arr[0]

  for i in range(0, len(arr)):
    if arr[i] > prev:
      increases += 1
    
    prev = arr[i]

  print(increases)