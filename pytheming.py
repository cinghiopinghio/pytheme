#!/usr/bin/env python3

import configobj
import pystache
import os
import argparse

def main(args):
    if os.path.isfile(args.palette):
        cols = configobj.ConfigObj(args.palette)
    else:
        print ('error: no such file', args.palette)
        exit(20)

    if os.path.isdir(args.template):
        tfiles = os.listdir(args.template)
        tfileslong = [args.template+'/'+t for t in tfiles]
        tfilesout = [args.outdir+'/'+t for t in tfiles]
    else:
        print ('error: no such dir', args.template)
        exit(28)

    for tmpl,outf in zip(tfileslong,tfilesout):
        print (tmpl, outf)
        with open(tmpl,'r') as fin, open(outf,'w') as fout:
            t = fin.read()
            fout.write(pystache.render(t,cols))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create themes from\
                                     palette and templates')
    parser.add_argument('-p','--palette', default='default.ini',\
                        help='file with color palette')
    parser.add_argument('-t','--template',default='templates',\
                        help='template file or folder')
    parser.add_argument('-o','--outdir',default='output',\
                        help='folder where to store themes')

    args=parser.parse_args()

    main(args)
