from __future__ import print_function
import configobj
import argparse
import sys


def main():
    """TODO: Docstring for main.
    """
    tconfig = configobj.ConfigObj('test/theme.ini')
    print_xdefaults(tconfig)

def print_xdefaults(tconfig,fileout=None):
    '''Print to file Xdefaults''' 

    if 'XDEFAULTS' not in list(tconfig['THEMES'].keys()):
        print ('no configuration for Xdefaults')
        exit()
    

    if fileout is None:
        fout = sys.stdout
    else:
        fout = open(fileout,'w')

    header = '''
! -------------------------------------------------------------
! Author: PyTheme
! vim:nu:ai:si:et:ts=4:sw=4:ft=xdefaults:
! -------------------------------------------------------------'''
    print (header,file=fout)

    if 'foreground' in tconfig['THEMES']:
        color_key = tconfig['THEMES']['foreground']
        color = tconfig['COLORS'][color_key]
        print ('*foreground:',color,file=fout)
    if 'background' in tconfig['THEMES']:
        color_key = tconfig['THEMES']['background']
        color = tconfig['COLORS'][color_key]
        print ('*background:',color,file=fout)
    if 'cursor' in tconfig['THEMES']['XDEFAULTS']:
        color_key = tconfig['THEMES']['XDEFAULTS']['cursor']
        color = tconfig['COLORS'][color_key]
        print ('URxvt.cursorColor:',color,file=fout)
    for n in range(16): 
        if 'color'+str(n) in tconfig['THEMES']['XDEFAULTS']:
            color_key = tconfig['THEMES']['XDEFAULTS']['color'+str(n)]
            color = tconfig['COLORS'][color_key]
            print ('!',color_key,file=fout)
            print ('*color{0:d}: {1:s}'.format(n,color),file=fout)
    fout.close()

if __name__ == '__main__':
    main()
