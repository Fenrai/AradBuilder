#!/usr/bin/env python
# *****************************************************************************
# AradBuilder
# Copyright (c) 2014 Stefan Rainow <stefan.rainow@gmx.de>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Lenz <fslenz@gmail.com>
#
# *****************************************************************************

import os

#from setuptools import setup
from distutils.core import setup
from distutils.core import Extension
from distutils.core import Command
from distutils.command.build_py import build_py as _build_py

########################################################################
#                             Package data                             #
########################################################################

PKG_NAME        = 'arad-builder'
PKG_VERSION     = '0.0.0'
PKG_DESC        = 'Configurable builder for Dungeon Fighter Online / Arado Senki.'
PKG_AUTHOR      = 'Stefan Rainow'
PKG_AUTHOR_MAIL = 'stefan.rainow@gmx.de'
PKG_WEBSITE     = 'https://github.com/Fenrai/AradBuilder'
PKG_LICENSE     = 'GPLv2'

########################################################################
#                            Old util stuff                            #
########################################################################

designerFiles = []

def findDesignerFiles(path):
    """Search for designer files at given path."""
    dirList = []
    fileList = []
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            fileList.append(os.path.join(path, entry))
        elif os.path.isdir(os.path.join(path, entry)):
            dirList.append(os.path.join(path, entry))

    fileList.sort()
    dirList.sort()

    for entry in fileList:
        if os.path.splitext(entry)[1] == ".ui":
            designerFiles.append(entry)
    for entry in dirList:
        entry,findDesignerFiles(entry)


def buildDesignerFiles():
    """Build designer files."""
    print("Generate designer-code:")
    findDesignerFiles(".")

    for entry in designerFiles:
        filename = os.path.basename(entry)
        path = os.path.dirname(entry) + "/"
        out = "ui_" + os.path.splitext(filename)[0] + ".py"
        command = "pyuic4 " + entry + " > " + path + out
        result = "-"
        if os.system(command) == 0:
            result = "+"

        print(" %-2s %35s    >    %-35s" % (str(result), str(filename), str(out)))

def findFile(file, path):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            if entry == file:
                return str(os.path.join(path, entry))
        elif os.path.isdir(os.path.join(path, entry)):
            rtn = findFile(file,os.path.join(path, entry))
            if rtn:
                return rtn


class build_py(_build_py):
    """Specialized Python source builder."""

    def build_packages(self):
        buildDesignerFiles()
        _build_py.build_packages(self)

class build_design(Command):
    description = ""
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        buildDesignerFiles()


########################################################################
#                                Setup                                 #
########################################################################

setup(name=PKG_NAME,
      version=PKG_VERSION,
      description=PKG_DESC,
      author=PKG_AUTHOR,
      author_email=PKG_AUTHOR_MAIL,
      url=PKG_WEBSITE,
      license=PKG_LICENSE,
      package_dir={'aradbuilder' : 'aradbuilder'},
      packages=['aradbuilder'],
      scripts=['builder.py'],
      cmdclass={'build_py': build_py,
                'build_design': build_design}
      )

