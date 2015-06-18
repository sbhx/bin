import sys
from xml.etree.ElementTree import iterparse, dump

author = sys.argv[1]
iparse = iterparse(sys.stdin, ['start', 'end'])

for event, elem in iparse:
    if event == 'start' and elem.tag == 'log':
        logNode = elem
        break

logentries = (elem for event, elem in iparse
                   if event == 'end' and elem.tag == 'logentry')

for logentry in logentries:
    if logentry.find('author').text == author:
        dump(logentry)
    logNode.remove(logentry)

#http://stackoverflow.com/questions/4499910/how-to-display-a-specific-users-commits-in-svn-log
