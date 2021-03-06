#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# TODO: this file should be replaced with calls to libalpm/pyalpm

import os, subprocess


class PackageError(Exception):
    """Exception that is raised when package operations fail.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotFoundError(Exception):
    """Exception that is raised when a package is not found.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def sync():
    """Syncs remote database with the local database.
    """
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        output = subprocess.call(["pacman", "-Syy"])


def getInstalled():
    """Get a list of installed applications.
    """
    cmdOutput = subprocess.check_output(["pacman", "-Qeq"])
    cmdOutput = cmdOutput.decode("utf-8")
    installed = cmdOutput.splitlines()
    rList = []
    for app in installed:
        rList.append(str(app))
    return rList


def installed(name):
    """Returns if specific package is installed or not
    """
    installedList = getInstalled()
    if name in installedList:
        return True
    else:
        return False


def remove(name):
    """Remove given package.
    :param name: Name of package to remove.
    """
    if not installed(name):
        raise PackageError(name + ' is not installed.')
    else:
        if (os.geteuid() != 0):
            raise PackageError("Must be root to perform this action")
        else:
            output = subprocess.call(["pacman", "--noconfirm", "-R", name])


def upgrade():
    """Upgrade all packages. This is currently not in use.
    """
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        output = subprocess.call(["pacman", "-Syyu", "--noconfirm"])


def toBeUpgraded():
    """Returns list of packages to be upgraded.
    """
    result = []
    try:
        output = subprocess.check_output(["pacman", "-Quq"])
        output = output.decode("utf-8")
        output = output.splitlines()
        for app in output:
            result.append(getPkgInfo(app))
    except:
        result = []
    return result


def install(name):
    """Installs a given package.
    :param name: Name of package to install.
    """
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        retValue = subprocess.call(["pacman", "--noconfirm", "-S", name])
    if retValue != 0:
        raise PackageError("Package does not exist")


def installLocal(name):
    """Install a package located locally.
    :param name: Name of the package to install.
    """
    if (os.geteuid() != 0):
        raise PackageError("Must be root to perform this action")
    else:
        if not os.path.exists(name):
            os.makedirs(name)
        os.chdir(name)
        retValue = subprocess.call(["pacman", "-U", "--noconfirm", name])
        os.chdir('../')
    if retValue != 0:
        raise PackageError("Package does not exist")


def getPkgInfo(name):
    """Get information about a given package.
    :param name: Name of package to get information about.
    """
    d = {}
    try:
        info = subprocess.check_output(["pacman", "-Si", name])
        info = info.decode("utf-8")
        info = info.splitlines()
        for line in info:
            if line[0:10] == 'Repository':
                d['repo'] = str(line[17:])
            if line[0:4] == 'Name':
                d['Name'] = str(line[17:])
            if line[0:13] == 'Download Size':
                d['dsize'] = line[17:]
            if line[0:14] == 'Installed Size':
                d['isize'] = line[17:]
            if line[0:11] == 'Description':
                d['Description'] = str(line[17:])
        return d
    except subprocess.CalledProcessError:
        return None
    

def search(term):
    """Search for a package.
    :param term: Term to search for.
    """
    result = []

    try:
        output = subprocess.check_output(["pacman", "-Ssq", term])
        output = output.decode("utf-8")
    except subprocess.CalledProcessError:
        output = ''

    matches = output.splitlines()
   
    for match in matches:
        if match != '':
            result.append(getPkgInfo(match))
    return result




# vim: set ts=4 sw=4 noet:
