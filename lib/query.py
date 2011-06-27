#!/usr/bin/env python2
# Thomas Schreiber 2011 <ubiquill@gmail.com>

# query.py
#
# Query the repositories and AUR

import sys
import os
import json

from twisted.internet import reactor
from twisted.web.client import getPage
from twisted.python.util import println


class queryAUR:
    """Searches the AUR using the scripting API"""

    def __init__(self, term):
        self.AURURL = 'http://aur.archlinux.org/rpc.php?type=search&arg='
        self.query = []
        self.search(term)


    def search(self, term):
        queryURL = self.AURURL + term
        
        getPage(queryURL).addCallbacks(
            callback=lambda value:(self.decodeResponse(value),reactor.stop()),
            errback=lambda error:(println("an error occured",error),reactor.stop()))

        reactor.run()


    def decodeResponse(self, value):
        jsonValue = json.loads(value);
        self.query = jsonValue['results']


    def printQuery(self):
        for app in self.query:
            print 'aur/' + app['Name'] + ' ' + app['Version']
            print '    ' + app['Description']
        #print jsonValue['results']



if (__name__ == "__main__"):
  
    if (len(sys.argv) <= 1):
        sys.exit()
    else:
        argument = sys.argv[1]
 
    os.system('/usr/bin/pacman -Ss ' + argument)

    query = queryAUR(argument)
    query.printQuery()

# vim: set ts=2 sw=2 noet:
