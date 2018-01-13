import fnmatch

def getMetion(line):
    pattern = '<@*>'
    matching = fnmatch.filter(line.split(), pattern)
    return matching.__len__()