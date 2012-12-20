#!/usr/bin/env python

import argparse
from image import image
from ascii_generator import ascii_generator

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='ASCIIart generator')
    parser.add_argument('-g', '--gamma',  metavar='GAMMA', default=1.0, type=float, help='a float > 0')
    parser.add_argument('-c', '--contrast', metavar='CONTRAST', default=1.0 , type=float, help='a float > 0')
    parser.add_argument('-m', '--mode', metavar='MODE', default='L', help='a string with image modes: 1, L, RGB')
    parser.add_argument('--width', metavar='WIDTH', default=100.0, type=float, help='a float > 0')
    parser.add_argument('--height', metavar='HEIGHT', default=100.0, type=float, help='a float > 0')
    parser.add_argument('-o', '--output', metavar='FILENAME', default=None, help='a file to dump the output')
    parser.add_argument('-i', '--input', metavar='IMAGE', default=None, help='use IMAGE as input')

    args = parser.parse_args()

    filename=args.input
    output=None

    if not args.input:
        import sys
        import os
        try:
            f = open('temp', 'wb')
            f.write(sys.stdin.read())
            f.close()
            filename='temp'
        except IOError as ex:
            print 'Error: Image file is of unsupported format or corrupted.'
            sys.exit()

    if not args.output:
        import sys
        output=sys.stdout
    else:
        try:
            output = open(args.output, 'w')
        except IOError as ex:
            print 'Error: Could not open file "'+args.output+'" for writing. Reason: '+str(ex)
            sys.exit()

    size = args.width, args.height

    im = image()
    im.load(filename, size, args.mode)

    asc = ascii_generator(im)
    asc.set_gamma(args.gamma)
    asc.set_contrast(args.contrast)
    asc.generate(output)

    output.close()

    if filename=='temp':
        os.remove(filename)



