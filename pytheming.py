#!/usr/bin/env python3

import configobj
import pystache
from opterator import opterate
import os

@opterate
def main(colors='default.ini',template='templates',outdir='output'):
    """Theming

    :param colors: theme ini file
    :param template: template file or folder
    :param outdir: dir where theme files should go
    """

    if os.path.isfile(colors):
        cols = configobj.ConfigObj(colors)
    else:
        print ('error: no such file', colors)
        exit(20)

    if os.path.isdir(template):
        tfiles = os.listdir(template)
        tfileslong = [template+'/'+t for t in tfiles]
        tfilesout = [outdir+'/'+t for t in tfiles]
    else:
        print ('error: no such dir', template)
        exit(28)

    for tmpl,outf in zip(tfileslong,tfilesout):
        print (tmpl, outf)
        with open(tmpl,'r') as fin, open(outf,'w') as fout:
            t = fin.read()
            fout.write(pystache.render(t,cols))

if __name__ == '__main__':

    main()
