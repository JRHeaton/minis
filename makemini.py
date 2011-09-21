#!/usr/bin/python

import sys
import subprocess

if(len(sys.argv) < 2):
    print "usage: makemini <name>"
    exit()

name = sys.argv[1] + ".py"

subprocess.call(["touch", name])
subprocess.call(["chmod", "+x", name])

open(name, "w").write("#!/usr/bin/python\n")