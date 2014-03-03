

import sys
block = []
cases = 0
for line in sys.stdin:
    if line == '\n':
        print("{} {}".format(len(block), len(block[0])))
        for string in block:
            print(string)
        print()
        block = []
        cases += 1
    else:
        block.append(line.strip())

print("cases: {}".format(cases))
