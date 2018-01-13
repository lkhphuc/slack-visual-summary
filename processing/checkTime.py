import fnmatch
import string

def timeCheck(line):
    timePhrase = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'sunday', 'january', 'jan', 'february', 'feb', 'march', 'mar', 'april', 'apr', 'may', 'june', 'jun',
                  'july',
                  'august', 'aug', 'september', 'sep', 'october', 'oct', 'november', 'nov', 'december', 'dec', 'am',
                  'pm',
                  'morning', 'afternoon', 'night', 'midnight', 'day', 'week', 'month', 'year', 'second',
                  'minute', 'hour', 'noon', 'clock', 'oclock']
    a = line.lower().translate(str.maketrans('','',string.punctuation)).split()
    return set(a).intersection(timePhrase)
    #if str.lower() in timePhrase:
    #print(timePhrase.index(str.lower()))

#print(timePhrase.index('aug'))

