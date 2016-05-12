#!/usr/bin/python
# usage: python make_command_download.py id auth > command.sh

import sys


for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    auth = sys.argv[2]
    print "curl -o "+spl[1]+".mgm"+spl[0]+".function_SEED.tab -X GET -H \"auth:"+auth+"\" \"http://api.metagenomics.anl.gov/1/annotation/similarity/mgm"+spl[0]+"?type=function&source=SEED\""

