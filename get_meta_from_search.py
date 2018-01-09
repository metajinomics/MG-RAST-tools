#!/usr/bin/python

"""
Created on Thu Oct 19 08:21:46 EDT 2017

@author: Jin Choi
get_meta_from_search.py

This script fetch meta data from search 
usage: python get_meta_from_search.py meta_field, output_filename, search_feld
example: python get_meta_from_search.py --meta_field mgrast_field.txt --outfile fungal.meta.tsv --country usa --sequence_type amplicon --target_gene its
"""

import sys
import ijson
import urllib
import uuid

import argparse
from argparse import RawTextHelpFormatter

def read_url(url_string, out_file_name, field, search_string):
    out_file = open(out_file_name,'w')
    out_file.write(search_string+'\n')
    out_file.write('\t'.join(field)+'\n')
    #print url_string
    try:
        f = urllib.urlopen(url_string)
    except:
        print url_string
        return "None"
    objects = ijson.items(f, '')
    new_url = ""
    for item in objects:
        tot = item['total_count']
        result = []
        for x in item['data']:
            result = []
            for one in field:
                if x.has_key(one):
                    if type(x[one]) is unicode:
                        x[one] = x[one].encode('utf-8')
                    result.append(str(x[one]))
                else:
                    result.append("NULL")
            out_file.write('\t'.join(result)+'\n')
        if item.has_key("next"):
            #print item["next"]
            if item["next"] == None:
                new_url = "None"
            else:
                new_url = item["next"]
        else:
            new_url = "None"
        #if item.has_key('total_count'):
        #    print item['total_count']
    out_file.close()
    return new_url


def main():
    parseStr = 'Fetch meta data from MG-RAST\n'
    usage= sys.argv[0] + '-i '

    parser = argparse.ArgumentParser(usage=usage, description=parseStr, formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--meta_field',  type=str, action = 'store',
                        default='mgrast_field.txt', help='Meta feild file [default=mgrast_field55.txt]')
    parser.add_argument('-o', '--outfile',  type=str, action='store',
                        default='mgrast.meta.tsv', help='Output meta file [default=mgrast.meta.tsv]')
    parser.add_argument('-c', '--country', type=str, action='store',
                        default="", help='Country example:usa')
    parser.add_argument('-l', '--location', type=str, action='store',
                        default="", help='location')
    parser.add_argument('-s', '--sequence_type', type=str, action='store',
                        default="", help='sequency type, metagenome(shotgun) or amplicon',
                        choices = ['wgs','amplicon'])
    parser.add_argument('-t', '--target_gene', type=str, action='store',
                        default="", help='target_gene, 16S, its or no-input(when shotgun sequence) [default=none]',
                        choices = ['16S','its','metagenome'])
    parser.add_argument('-m', '--material', type=str, action='store',
                        default="", help='material')


    args = parser.parse_args()
    meta_file = open(args.meta_field,'r')
    out_file_name = args.outfile
    country = args.country
    location = args.location
    sequence_type = args.sequence_type
    target_gene = args.target_gene
    material = args.material
    offnum = 0
    offset = str(offnum)
    #url_string = "http://api.metagenomics.anl.gov/search?sequence_type=amplicon&country=usa&limit=1000&search=%22its%20fungal%22"
    #url_string = "http://api.metagenomics.anl.gov/search?sequence_type="+sequence_type+"&country="+country+"&limit=1000&target_gene="+target_gene
    #url_string = "http://api.metagenomics.anl.gov/search?country=usa&limit=1000&seq_meth=illumina&investigation_type=metagenome"
    #url_string = "http://api.metagenomics.anl.gov/search?country="+country+"&location="+location+"&investigation_type="+sequence_type+"&target_gene="+target_gene+"&limit=1000&seq_meth=illumina"
    url_string = "http://api.metagenomics.anl.gov/search?country="+country+"&location="+location+"&sequence_type="+sequence_type+"&target_gene="+target_gene+"&material="+material+"&offset="+offset+"&limit=1000&seq_meth=illumina"
    field = []

    for line in meta_file:
         field.append(line.strip())
    meta_file.close()
    
    search_string = 'search field: '+country+","+location+","+sequence_type+","+target_gene+","+material
    
    new_url = "first"
    iter = 1
    spl_file = out_file_name.split('.')
    file_name_header = '.'.join(spl_file[:len(spl_file)-1])
    file_extension = spl_file[len(spl_file)-1]
    filename = file_name_header+'.'+file_extension
    while (new_url != "None"):
        new_url = read_url(url_string, filename, field, search_string)
        url_string = new_url
        filename = file_name_header + str(iter) + '.' + file_extension
        iter += 1

if __name__ == '__main__':
    main()



