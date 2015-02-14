#!/usr/bin/env python
# encoding: utf-8

import colorsys as colors
from matplotlib.colors import rgb2hex
import numpy as np

Ncol = 8

black = 0.15
bhue = 0.0
bsat = 0.0
white = 0.85
whue = 0.125
wsat = 1.0
gray_hue = np.linspace(bhue,whue,Ncol)
#gray_sat = np.linspace(bsat,wsat,Ncol)
gray_sat = np.logspace(-5,0,Ncol)*(wsat-bsat) + bsat
lightness = np.linspace(black,white,Ncol)

sat = 0.45
hue0 = 0.0
AUTO=False
clight = [.5,.7]
ndark = 3
nlight = 6

hue = [ (hue0+(h/Ncol))%1 for h in range(Ncol) ]

print ('# Grays')
for ng,(h,l,s) in enumerate(zip(gray_hue,lightness,gray_sat)):
    clr_rgb = colors.hls_to_rgb(h, l, s)
    clr_hex = rgb2hex(clr_rgb)
    print ('gray{0}= "{1}"'.format(ng,clr_hex))
    
print ('\n# Colors')
for ng, cl, char in zip([ndark,nlight],clight,['d','l']):
    for nc,h in enumerate(hue) :
        l = lightness[ng] if AUTO else cl
        clr_rgb = colors.hls_to_rgb(h, l, sat)
        clr_hex = rgb2hex(clr_rgb)
        print ('col{0}{1}= "{2}"'.format(nc,char,clr_hex))
