# _*_ coding: utf-8 _*_

import os, subprocess
from config import config


__author__ = 'wwy'
__version__ = '0.1.0'

"""
Convert Avi format to Mp4
Python version : 3.5
"""


class Converter(object):
    """class Converter"""
    
    ffmpeg_path = config.get('ffmpeg', 'bin')
    command = ffmpeg_path + ' -i' + ' {} {}'
#    print(command)

    def __init__(self, path):
        super(Converter, self).__init__()
        self.path = path

    def check_path(self):
        if not os.path.isdir(self.path):
            print('Bad dir path')
            return False

        self.avi_filedir = path
        self.avi_files = [fp for fp in os.listdir(self.avi_filedir) if fp.endswith('.avi')]
 
        if not self.avi_files:
            print('Do not exists avi files!')
            return False
        return True


    def convert(self):
        for file in self.avi_files:
            avi_file = file
            mp4_file = file.replace('.avi', '.mp4')
            #print(self.command.format(avi_file, mp4_file))
            subprocess.call(self.command.format(self.path + "//"+avi_file, self.path + "//" + mp4_file))


if __name__ == "__main__":

    path = input(">>>>>>>>>>:")
    converter = Converter(path)
    if converter.check_path():
        converter.convert()
