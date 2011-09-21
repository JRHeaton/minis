#!/usr/bin/python

import os
import sys
import subprocess

o_null = open("/dev/null")

if(len(sys.argv) < 3):
    print "usage: fdump <sdk> <outdir>"
    exit()

outdir = sys.argv[2] + "/" + sys.argv[1] + "/"
subprocess.call(["mkdir", "-p", outdir])

sdk_root = "/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator" + sys.argv[1] + ".sdk"

f_path = sdk_root + "/System/Library/Frameworks"
pf_path = sdk_root + "/System/Library/PrivateFrameworks"

for file in os.listdir(f_path):
    basename = file[:len(file)-len(".framework")]
    print "Dumping %s..." % basename
    subprocess.call(["class-dump", "-H", f_path + "/" + file + "/" + basename, "-o", outdir + basename], stderr=o_null, stdout=o_null)

for file in os.listdir(pf_path):
    basename = file[:len(file)-len(".framework")]
    print "Dumping %s..." % basename
    subprocess.call(["class-dump", "-H", pf_path + "/" + file + "/" + basename, "-o", outdir + basename], stderr=o_null, stdout=o_null)

print "Dumping SpringBoard..."
subprocess.call(["class-dump", "-H", sdk_root + "/System/Library/CoreServices/SpringBoard.app/SpringBoard", "-o", outdir + "SpringBoard"])