from sys import argv
pyFile, fname, action = argv

from os.path import exists

print "hi %s thx for passing %s" % (fname,action)
print "to %s; it does exists, so %s !!" % (pyFile, exists(pyFile))
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
print "bye"
