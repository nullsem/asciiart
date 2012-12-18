#!/usr/bin/env python

import os
from PIL import Image

class image:
    '''
        The image class is a layer above PIL.Image that handles resizing and aspect ratio
        issues during the conversion. Also, it handles tonality detection and image file
        loading for the ascii art generation.

        Accepts:
            - path: The path to the image file.

    '''

    def __init__(self, path=''):
        # image file path
        self.path = os.path.abspath(path)

        # image size. Tuple of (width, height) in pixels
        self.size = 0,0

        # aspect ratio to preserve during resize
        self.aspect_ratio=0

        # max_size is a tuple in the form of (width, height)
        # max height and width are used to calculate the aspect ratio for an image.
        # That is ratio=min(max.width/image.width, max.height/image.height). For ascii
        # art, 1000x1000 images are just enough. But you can change these values
        # according to the screen used and whatnot.
        self.max_size=50.0, 50.0

        # image object from PIL library.
        self.load(self.path)

    def __calculate_aspect_ratio(self):
        '''
            Calculates the aspect ratio of the loaded image object. It uses the formula
            of ratio = min(max.width/image.width, max.height/image.height)

            Accepts: None
            Returns: None
            Raises:
                - AttributeError: in case of an image object not being loaded.

        '''
        if not self.image:
            raise AttributeError('Image object given was None.')

        # load image size
        self.size = self.image.size

        # calculate image aspect ratio
        self.aspect_ratio = min(self.max_size[0] / float(self.size[0]), self.max_size[1] / float(self.size[1]))

    def __resize(self, size=None):
        '''
        Resizes the loaded image. If a size is provided, then it uses the Image.resize() method.
        Else, it uses the Image.thumbnail() method and it tries to preserve the image's aspect
        ratio.

        Accepts:
            - size: a tuple in the form of (new_width, new_height)

        Raises:
            - IOError: if the thumbnail method fails to preserve the ratio

        Returns:
            - True: if resize() was successful
            - False: in case of Error
        '''
        # if not size, that means preserve aspect ratio.
        if not size:
            try:
                self.image.thumbnail((int(self.size[0]*self.aspect_ratio), int(self.size[1]*self.aspect_ratio)), Image.ANTIALIAS)
            except IOError:
                print 'Error: Could not preserve image aspect ratio. Please specify a sampling size.'
                return False
        else:
             self.image = self.image.resize(size, Image.ANTIALIAS)

        self.size = self.image.size

    def __convert(self, mode='L'):
        '''
            Converts a loaded image object to a different image mode. Available modes are:
            1, 1;I, 1;R, L, L;I, P, RGB, BGR, RGBX, RGB;L

            Accepts:
                - mode: a string with the desired image mode
            Raises:
                - AttributeError: in case the mode is None.

        '''
        if not mode:
            raise AttributeError('Image mode was None.')

        self.image = self.image.convert(mode)

    def __load_image(self):
        '''
            Loads a PIL.Image object from a given self.path.

            Accepts: None
            Returns:
                - True: if the object is loaded
                - False: in case of error

            Raises: None
        '''
        try:
            self.image = Image.open(self.path)
            return True
        except IOError as ex:
            print 'Error: Could not open image "'+str(self.path)+'". Reason: '+str(ex)
            return False

    def load(self, path='', size=None, mode='L'):
        '''
            Wrapper for automatic image loading, converting and resizing.

            Accepts:
                - path: string that holds the path to the image
                - size: Tuple of ints of the form (width, height)
                - mode: string of one of the available modes for __convert().

            Returns: None

        '''

        # sanitize input
        if not path:
            raise AttributeError('Path to image was None')

        if not os.path.exists(path):
            raise IOError('Image file "'+str(path)+'" does not exist.')

        try:
            self.path = os.path.abspath(path)
        except IOError as ex:
            print 'Error: '+str(ex)
            return

        if not self.__load_image():
            return

        self.__calculate_aspect_ratio()

        self.__resize(size)

        self.__convert(mode)

if __name__=='__main__':
    im = image(r'genius-meme.png')
