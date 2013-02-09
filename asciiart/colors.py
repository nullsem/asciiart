#!/usr/bin/env python

class colors:
    def __init__(self):
        self.start = '\[\033[34'
        self.end = '\[\033[0m\]'

        self.colors = {
                'black'     : '0;30',
                'red'       : '0:31',
                'green'     : '0:32',
                'brown'     : '0;33',
                'blue'      : '0;34',
                'purple'    : '0;35',
                'cyan'      : '0;36',
                'light_gray': '0;37',
                'dark_gray' : '1;30',
                'light_red' : '1;31',
                'light_green':'1;32',
                'yellow'    : '1;33',
                'light_blue': '1;34',
                'light_purple': '1;35',
                'light_cyan' : '1;36',
                'white'     : '1;37',
                }

        self.backgrounds = {

                'black'     : '40',
                'red'       : '41',
                'green'     : '42',
                'brown'     : '43',
                'blue'      : '44',
                'purple'    : '45',
                'cyan'      : '46',
                'light_gray': '47',
                }


        def convertRGB2color(self, rgb=None):
            if not rgb:
                return ''

            if rgb == 0,0,0:
                print
