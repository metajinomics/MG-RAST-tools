#!/usr/bin/python
# usage: python changeID.py input output
# example: python changeID.py mgm4635901.3_function_SEED.tab mgm4635901.3_function_SEED_new_id.tab

import sys
fread =  open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
fwrite.write(fread.readline().strip()+'\n')
for line in fread:
    templine = line.strip().split('\t')
    tempid = templine[0]
    tempid2 = tempid.split('|')
    if(len(tempid2) < 2):
        continue
    tempname = tempid2[1].split('_')
    tempname2 = tempname[0].split('-')
    fwrite.write(tempname2[0])
    for i in range(1,len(tempname2)):
        fwrite.write('.'+tempname2[i])
    fwrite.write('_'+tempname[1])
    for i in range(1,len(templine)):
        fwrite.write('\t'+templine[i])
    fwrite.write('\n')
