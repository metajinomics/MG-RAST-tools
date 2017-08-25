#!/usr/bin/python

"""
this script fetch metagenome id from project id
usage:
python fetch_mgm_id_from_project_id.py list.project.id.txt > metagenome_id.txt
"""
import sys
import ijson
import urllib
import time

def main():
    url_string = "http://api.metagenomics.anl.gov/project/mgp%s?verbosity=full"
    
    for line in open(sys.argv[1],'r'):
        mgp = line.strip()
        f = urllib.urlopen(url_string % mgp)
        objects = ijson.items(f,'')
        for item in objects:
            for x in item["metagenomes"]:
                result = [mgp,x["metagenome_id"],x["sequencing_method"]]
                print '\t'.join(result)
        time.sleep(1.0/3)
                

if __name__ == '__main__':
    main()
