#!/usr/bin/env python
import os
import sys
import csv
from argparse import ArgumentParser as AP


ap = AP()
ap.add_argument('--min-pid', default=0.75, type=float)
ap.add_argument('blast_input')
args = ap.parse_args()

assert os.path.exists(args.blast_input)

with open(args.blast_input) as fi:
    reader = csv.reader(fi, delimiter='\t')
    reader.next()
    for row in reader:
        # chr1, start1, end1, chr2, start2, end2 = row[:6]
        if float(row[6]) >= args.min_pid:
            row[0] = 'DrChr_%s' % (row[0].split('_')[2])
            row[3] = 'Os' + row[3]
            sys.stdout.write(' '.join(row[:6]) + '\n')
