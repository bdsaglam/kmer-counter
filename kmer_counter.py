#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import argparse
from itertools import islice
from collections import Counter


def window(seq, n=2):
    """Returns a sliding window (of width n) over data from the iterable
       s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ..."""

    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        if elem == 'N':
            continue
        result = result[1:] + (elem,)
        yield result


def read_fastq(filename, max_line=None):
    with open(filename, 'r') as f:
        for line in islice(f, 1, max_line, 4):
            yield line.rstrip()


def main(arguments):
    co = Counter()
    for entry in read_fastq(arguments.filename):
        co.update(window(entry, arguments.kmersize))
    return co.most_common(arguments.topcount)


def stringify(t):
    return ''.join(t[0]), t[-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='filename of fastq file', type=str)
    parser.add_argument('-k', '--kmersize', help='k-mer size', type=int)
    parser.add_argument('-t', '--topcount', help='number of top k-mers', type=int)

    argums = parser.parse_args(sys.argv[1:])

    out = main(argums)
    print(map(stringify, out))
