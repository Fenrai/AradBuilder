#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Device Settings Backup Tool (DSBT)
# Copyright (C) 2013 Stefan Rainow
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

# import os
import sys

import aradbuilder.mainwindow as GUI
# import aradbuilder.paths as paths


def main (argv=None):
    if argv is None:
        argv = sys.argv

#     p = paths.Paths()
#     print 'charpictures'
#     print p.charPicturePaths
#     print 'skillpictures'
#     print p.skillPicturePaths
#     print 'skillfiles'
#     print p.skillFilePaths
#
#     print os.path.join(p.getSPicPath('General', 'SP'), '0.png')

    GUI.launchGui(argv)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
