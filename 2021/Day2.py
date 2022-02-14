from Util import returnFileAsArray

arr = returnFileAsArray(2)

def p1():
  depth = 0
  x = 0

  for line in arr:
    spl = line.split()
    op = spl[0]
    val = int(spl[1])

    if (op == "up"):
      depth -= val
    elif (op == "down"):
      depth += val
    elif (op == "forward"):
      x += val

  return x * depth

def p2():
  depth = 0
  x = 0
  aim = 0

  for line in arr:
    spl = line.split()
    op = spl[0]
    val = int(spl[1])

    if (op == "up"):
      aim -= val
    elif (op == "down"):
      aim += val
    elif (op == "forward"):
      x += val
      depth += (aim * val)

  return x * depth

if __name__ == "__main__":
  print(p1())
  print(p2())