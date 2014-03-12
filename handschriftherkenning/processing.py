#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

block = []
for line in sys.stdin:
    if line == '\n':
        block[0] = "{} {}".format(block[0], len(block) - 1)
        for i in block:
            print(i)
        print()
        block = []
    else:
        block.append(line.strip('\n'))
