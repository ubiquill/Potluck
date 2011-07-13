#!/usr/bin/env python2
# coding=UTF-8

# Copyright © 2011 Thomas Schreiber
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# Potluck
# by Thomas Schreiber <ubiquill@gmail.com>

import os, subprocess
import string


class PackageError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def sync():
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        output = subprocess.check_output(["pacman", "-Syy"])


def getInstalled():
    cmdOutput = subprocess.check_output(["pacman", "-Qeq"])
    installed = string.split(cmdOutput, '\n')
    return installed


def installed(name):
    installedList = getInstalled()
    if name in installedList:
        return True
    else:
        return False


def remove(name):
    if not installed(name):
        raise PackageError(name + ' is not installed.')
    else:
        if (os.geteuid() != 0):
            raise PackageError("Must be root to perform this action")
        else:
            output = subprocess.check_output(["pacman", "-R", "--noconfirm", name])


def upgrade():
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        output = subprocess.check_output(["pacman", "-Syyu", "--noconfirm"])


def install(name):
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        retValue = subprocess.call(["pacman", "-S", "--noconfirm", name])
    if retValue != 0:
        raise PackageError("Package does not exist")
    

def search(term):
    result = []
    output = subprocess.check_output(["pacman", "-Ssq", term])
    matches = string.split(output, '\n')
   
    for match in matches:
        if match != '':
            d = {}              
            info = subprocess.check_output(["pacman", "-Si", match])
            info = info.splitlines()
            for line in info:
                if line[0:10] == 'Repository':
                    d['repo'] = line[17:]
                if line[0:4] == 'Name':
                    d['Name'] = line[17:]
                if line[0:13] == 'Download Size':
                    d['dsize'] = line[17:]
                if line[0:14] == 'Installed Size':
                    d['isize'] = line[17:]
                if line[0:11] == 'Description':
                    d['Description'] = line[17:]
            result.append(d)
    return result