#!/usr/bin/env python

from bisect import bisect
from image import image

class ascii_generator:
    def __init__(self, imobj=None):

        if not imobj:
            raise AttributeError('Image object given was None.')

        self.image = imobj
        self.gamma = 1.0
        self.contrast = 1.0

        #self.greyscale = [ " ", " ", ".,-", "_ivc=!/|\\~", "gjez2]/(YL)t[+T7Vf", "mdK4ZGbNDXY5P*Q", "W8KMA", "#%$" ]
        self.greyscale = [ ' ', '.', '-', 'i', 't', '4', '8', '#' ]
        self.tonalzones = [ 36,72,108,144,180,216,252 ]


    def set_gamma(self, gamma=1):
        if gamma == 0:
            raise ZeroDivisionError()
        for z in xrange(len(self.tonalzones)):
            self.tonalzones[z]/=gamma
        self.gamma = gamma

    def set_contrast(self, contr=1.0):
        if contr == 0:
            raise ZeroDivisionError()
        for z in xrange(len(self.tonalzones)):
            self.tonalzones[z]+=self.tonalzones[0]/contr
        self.contrast = contr

    def generate(self, fstream=None):

        if not fstream:
            import sys
            fstream=sys.stdout

        if self.image.image.mode == '1':
            for y in xrange(self.image.size[1]):
                for x in xrange(self.image.size[0]):
                    fstream.write(' ' if self.image.image.getpixel((x,y)) else '0')
                    fstream.flush()
                fstream.write("\n")

        elif self.image.image.mode == 'L':
            for y in xrange(self.image.size[1]):
                for x in xrange(self.image.size[0]):
                    luminosity = 255 - self.image.image.getpixel((x,y))
                    fstream.write(self.greyscale[bisect(self.tonalzones, luminosity)])
                    fstream.flush()
                fstream.write("\n")
        elif self.image.image.mode == 'RGB':
            for y in xrange(self.image.size[1]):
                for x in xrange(self.image.size[0]):
                    print self.image.image.getpixel((x,y))
                print

if __name__=='__main__':
    im = image('genius-meme.png')
    asc = ascii_generator(im)
    asc.set_gamma(1.4)
    asc.set_contrast(0.8)
    asc.generate()
