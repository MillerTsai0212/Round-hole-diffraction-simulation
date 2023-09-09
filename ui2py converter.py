# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 00:53:55 2019

@author: USER
"""
from PyQt5 import uic
fin = open('UiMainApp.ui','r')
fout = open('UiMainApp.py','w')
uic.compileUi(fin,fout,execute = True)
fin.close()
fout.close()