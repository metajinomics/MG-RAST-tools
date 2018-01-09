#!/usr/bin/python

"""
this script fetch metagenome id from project id
usage:
python 
"""
import sys

def main():
    filename = sys.argv[1]
    col_file_type = 0
    col_metagenome_id = 0
    for n, line in enumerate(open(filename,'r')):
        if n == 0:
            continue
        elif n == 1:
            spl = line.strip().split('\t')
            for i, x in enumerate(spl):
                if x == "file_type":
                    col_file_type = i
                elif x == "metagenome_id":
                    col_metagenome_id = i
        else:
            spl = line.strip().split('\t')
            print "curl -o "+spl[col_metagenome_id]+"."+spl[col_file_type]+" -X GET http://api.metagenomics.anl.gov/1/download/"+spl[col_metagenome_id]+"?file=100.1"



if __name__ == '__main__':
    main()
