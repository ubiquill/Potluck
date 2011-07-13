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

# query.py
# by Thomas Schreiber <ubiquill@gmail.com>
#
# Query the repositories and AUR

import sys
import os
import json
import urllib
import stat
import subprocess


class Query:
    """Searches the AUR using the scripting API"""

    def __init__(self, term):
        self.AURURL = 'http://aur.archlinux.org/rpc.php?type=search&arg='
        self.query = []
        self.search(term)


    def search(self, term):
        queryURL = self.AURURL + term

        value = urllib.urlopen(queryURL).read()
        self.decodeResponse(value)
        

    def decodeResponse(self, value):
        jsonValue = json.loads(value);
        self.query = jsonValue['results']


    def printQuery(self):
        for app in self.query:
            print 'aur/' + app['Name'] + ' ' + app['Version']
            print '    ' + app['Description']
        #print jsonValue['results']




class Upgrade:

    def __init__(self, target):
        self.target = target
        self.downloadPkgbuild()
        self.buildDepends = self.getBuildDepends()
        self.depends = self.getDepends()
        #self.makePkg()


    def downloadPkgbuild(self):
        self.AURURL = 'http://aur.archlinux.org'
        self.getPkgInfo()
        self.getPkgbuild()

    def getPkgInfo(self):
        AURSearchURL = self.AURURL + '/rpc.php?type=info&arg='
        self.info = []
        infoURL = AURSearchURL + self.target

        value = urllib.urlopen(infoURL).read()
        self.decodeResponse(value)


    def decodeResponse(self, value):
        self.info = json.loads(value)
        response = self.info['results']
        self.pkgURL = self.AURURL + response['URLPath']


    def getPkgbuild(self):
        pkgbuildURL = self.AURURL + '/packages/' + self.target + '/PKGBUILD'
        urllib.urlretrieve(pkgbuildURL, self.target + '.PKGBUILD')


    def getDepends(self):
        retCode = subprocess.call(["chmod", "+x", self.target + ".PKGBUILD"])
        dependsString = subprocess.check_output(["./scripts/getDepends.sh", self.target])
        depends = list(dependsString.split())
        return depends


    def getBuildDepends(self):
        retCode = subprocess.call(["chmod", "+x", self.target + ".PKGBUILD"])
        dependsString = subprocess.check_output(["./scripts/getBuildDepends.sh", self.target])
        buildDepends = list(dependsString.split())
        return buildDepends


    def makePkg(self):
        os.system('makepkg -s PKGBUILD')





if (__name__ == "__main__"):
  
    if (len(sys.argv) <= 1):
        sys.exit()
    else:
        argument = sys.argv[1]
 
    os.system('/usr/bin/pacman -Ss ' + argument)

    query = QueryAUR(argument)
    query.printQuery()

# vim: set ts=2 sw=2 noet: