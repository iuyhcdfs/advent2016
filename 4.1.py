#!/usr/bin/python3.5

import sys
import re
for stdl in sys.stdin:
    m = re.match(r"^(.*)-(...)\[(.....)\]$", stdl)
    if m:
        print(m.group(1))
        print(m.group(2))
        print(m.group(3))

