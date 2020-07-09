fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    l = line.upper()
    print(l.rstrip())