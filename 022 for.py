import sys

filename=sys.argv[1]
f= open(filename)
print f.read()
f.close
