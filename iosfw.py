#!/usr/bin/python

import urllib2
import plistlib

print "Downloading info from Apple..."
rawplist = urllib2.urlopen("http://itunes.com/versions?touchUpdate=true")

plistobj = plistlib.readPlist(rawplist)
used_urls = []

for appleisdumb in plistobj["MobileDeviceSoftwareVersionsByVersion"]:
    for sv in plistobj["MobileDeviceSoftwareVersionsByVersion"][appleisdumb]["MobileDeviceSoftwareVersions"]:
        for build in plistobj["MobileDeviceSoftwareVersionsByVersion"][appleisdumb]["MobileDeviceSoftwareVersions"][sv]:
            chunk = plistobj["MobileDeviceSoftwareVersionsByVersion"][appleisdumb]["MobileDeviceSoftwareVersions"][sv][build]
            if(chunk.has_key("Restore")):
                if(chunk["Restore"]["FirmwareURL"] in used_urls):
                   continue;
                print "%s- %s(%s): %s" % (sv, chunk["Restore"]["ProductVersion"], chunk["Restore"]["BuildVersion"], chunk["Restore"]["FirmwareURL"])
                used_urls.append(chunk["Restore"]["FirmwareURL"])