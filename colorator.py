#!/usr/bin/env python
# encoding: utf-8

import colorsys as colors
from matplotlib.colors import rgb2hex
import numpy as np

Ncol = 8
sat = 0.6

black = 0.2
white = 0.8
hue = 0.0
ndark = 2
nlight = 5

lightness = [ black + (white-black)*ng/(Ncol-1) for ng in range(Ncol) ]
hues = [ (hue+(h/Ncol))%1 for h in range(Ncol) ]

print ('# Grays')
for ng,l in enumerate(lightness):
    clr_rgb = colors.hls_to_rgb(0, l, 0)
    clr_hex = rgb2hex(clr_rgb)
    print ('gray{0}= "{1}"'.format(ng,clr_hex))
    
print ('\n# Colors')
for ng, char in zip([ndark,nlight],['d','l']):
    for nc,h in enumerate(hues) :
        clr_rgb = colors.hls_to_rgb(h, lightness[ng], sat)
        clr_hex = rgb2hex(clr_rgb)
        print ('col{0}{1}= "{2}"'.format(nc,char,clr_hex))
