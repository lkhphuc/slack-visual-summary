def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def delSentence(str, str2):
    with open(str2, 'w') as w:
        with open(str) as r:
            for line in r:
                cleaned = [x for x in line.split() if isfloat(x) and float(x)<=1]
                cleaned.append("\n")
                w.write(" ".join(cleaned))


delSentence("output.txt", "process.txt")