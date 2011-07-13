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

# MainWindow.py
# by Thomas Schreiber <ubiquill@gmail.com>
#
# The main window for potluck, an AUR GUI frontend.

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view.protoUi import Ui_MainWindow
from view.Dialogs import searchDialog

import os, sys, time
import string
import shlex, subprocess
from model.Transaction import Transaction

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        QObject.connect(self.ui.queryButton, SIGNAL('clicked()'), self.newSearch)
        QObject.connect(self.ui.queryEdit, SIGNAL('returnPressed()'), 
                        self.ui.queryButton, SIGNAL('clicked()'))


    def newSearch(self):
        self.busy = searchDialog(self)
        self.ui.queryList.clear()

        self.busy.show()
        self.busy.setValue(0)

        self.q = runQuery(self)
        self.connect(self.q, SIGNAL("update(PyQt_PyObject)"), self.displaySearch)
        self.connect(self.busy, SIGNAL("canceled()"), self.cancelSearch)
        self.q.begin()

    def displaySearch(self, response):
        for q in response:
            item = QTreeWidgetItem([' ', q['Name'], q['Description']])
            if q['Installed'] == True:
                item.setCheckState(0,Qt.Checked)
            else:
                item.setCheckState(0,Qt.Unchecked)
            self.ui.queryList.addTopLevelItem(item)
        self.busy.hide()

    def cancelSearch(self):
        self.q.terminate()
        self.q = None



class runQuery(QThread):
    def __init__(self, mw):
        QThread.__init__(self)
        self.mw = mw


    def run(self):
        self.t = Transaction()
        self.t.query(unicode(mw.ui.queryEdit.text().toUtf8()))
        self.emit(SIGNAL('update(PyQt_PyObject)'), self.t.queryResult)
        return
        


    def begin(self):
        self.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Main()
    mw.show()
    sys.exit(app.exec_())
