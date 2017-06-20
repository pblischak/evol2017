from __future__ import print_function
from sys import argv

outfile = open(argv[2], 'w')
mapfile = open(argv[3], 'w')
matrix = {
    '1':  [],
    '2':  [],
    '3':  [],
    '4':  [],
    '5':  [],
    '6':  [],
    '7':  [],
    '8':  [],
    '9':  [],
    '10': [],
    '11': [],
    '12': [],
    '13': [],
    '14': [],
    '15': [],
    '16': []
    }

with open(argv[1]) as f:
    reps  = f.read().split(" 16 1\n")
    split_reps = [r.splitlines() for r in reps]
    for s in split_reps[1:]:
        for l in s:
            matrix[str(l.split()[0])].append(l.split()[1])

for i in range(1, 16+1):
    print("i"+str(i), "\t", sep='', end='', file=outfile)
    for base in matrix[str(i)]:
        print(base, sep='', end='', file=outfile)
    print("\n", end='', file=outfile)

# Yeah, this is an ugly way to do this. Oh well
print("i1", "sp1", sep='\t', file=mapfile)
print("i2", "sp1", sep='\t', file=mapfile)
print("i3", "sp1", sep='\t', file=mapfile)
print("i4", "sp1", sep='\t', file=mapfile)
print("i5", "sp1", sep='\t', file=mapfile)
print("i6", "sp2", sep='\t', file=mapfile)
print("i7", "sp2", sep='\t', file=mapfile)
print("i8", "sp2", sep='\t', file=mapfile)
print("i9", "sp2", sep='\t', file=mapfile)
print("i10", "sp2", sep='\t', file=mapfile)
print("i11", "sp3", sep='\t', file=mapfile)
print("i12", "sp3", sep='\t', file=mapfile)
print("i13", "sp3", sep='\t', file=mapfile)
print("i14", "sp3", sep='\t', file=mapfile)
print("i15", "sp3", sep='\t', file=mapfile)
print("i16", "out", sep='\t', file=mapfile)
