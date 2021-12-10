#!/usr/bin/env python3
import sys
for line in sys.stdin:
    if line.strip():
        if not line.startswith("#"):
            print('#include "{}"'.format(line.strip()))
