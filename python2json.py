#!/usr/bin/env python
#
# turn output from python str/repr into json

import json
import sys

txt = sys.stdin.read()
val = eval(txt)
json.dump(val, sys.stdout, indent=2)
