#!/usr/bin/python
# usage: python make_command_download.py id auth > command.sh

import sys


for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    auth = sys.argv[2]
    print "curl -o "+spl[1]+".fastq -X GET http://api.metagenomics.anl.gov/1/download/"+spl[1]+"?file=100.1"

