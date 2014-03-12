#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint


def size(matrix, topx, topy, lowx, lowy):
    count = 0
    for row in matrix[topx:lowx]:
        for col in row[topy:lowy]:
            if col == '-':
                return 0
            count += 1
    assert count == (topx - lowx) * (topy - lowy), \
        "{} {} {} {} {}".format(count, topx, topy, lowx, lowy)
    return (topx - lowx) * (topy - lowy)


def sizes(matrix):
    for i in range(0, len(matrix) + 1):
        for j in range(0, len(matrix[0]) + 1):
            for r in range(0, i + 1):
                for c in range(0, j + 1):
                    yield size(matrix, r, c, i, j)


if __name__ == '__main__':
    import sys
    block = []
    for line in sys.stdin:
        if line == '\n':
            print(max(sizes(block[1:])))
            block = []
        else:
            block.append(line.strip())
