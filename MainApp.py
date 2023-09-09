# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 01:43:29 2019

@author: USER
"""
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtCore import pyqtSlot
from UiMainApp import Ui_MainWindow
from numpy import pi , linspace, meshgrid , sin
import matplotlib.cm as cm
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.fig1()
        
    def fig1(self):
        lamda = self.slider_lambda.value()*1.E-9 ; k=(2.*pi)/lamda
        b = self.slider_b.value()*1.e-5
        h=self.slider_h.value()*1.e-5
        f_2 = self.slider_f2.value()
        a =  self.slider_a.value()*1e-2
        X_Mmax = a/2 ; X_Mmin = -a/2
        Y_Mmax = X_Mmax ; Y_Mmin = X_Mmin
        N=400
        X=linspace(X_Mmin,X_Mmax,N) ; Y = X
        B = (k*b*X)/(2.*f_2) ; H = (k*h*Y)/(2.*f_2)
        BB ,HH = meshgrid(B,H)
        I = ((sin(BB)/BB)**2)*((sin(HH)/HH)**2)
        mpl = self.mplwidget.canvas
        mpl.ax.clear()
        mpl.ax.imshow(I, cmap=cm.gray, interpolation = 'bilinear', origin = 'lower', vmin=0,vmax= .01)
        mpl.ax.set_xlabel(u'$X (m)$' , fontsize = 12, fontweight = 'bold')
        mpl.ax.set_ylabel(u'$Y (m)$' , fontsize = 12, fontweight = 'bold')
        mpl.ax.set_xticks(linspace(0, N, 5))
        mpl.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5), color = 'r')
        mpl.ax.set_yticks(linspace(0, N, 5))
        mpl.ax.set_yticklabels(linspace(Y_Mmin, Y_Mmax, 5), color = 'r')   
        mpl.figure.suptitle('Fraunhofer Diffraction by rectangular aperture', fontsize = 14, fontweight = 'bold')
        mpl.ax.set_title(r"$\lambda = %.3e \ m , \ b = %.2e \ m , \ h = %.2e \ m , \ f_2 = %.1f \ m$"% (lamda, b, h, f_2), fontsize = 10)
        mpl.draw()
    
    @pyqtSlot ('double')   
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)
        
    @pyqtSlot ('double')   
    def on_SpinBox_b_valueChanged(self, value):
        self.slider_b.setValue(value)
        
    @pyqtSlot ('double')   
    def on_SpinBox_h_valueChanged(self, value):
        self.slider_h.setValue(value)

    @pyqtSlot ('double')   
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(value)
        
    @pyqtSlot ('double')   
    def on_SpinBox_f2_valueChanged(self, value):
        self.slider_f2.setValue(value)
        
    @pyqtSlot ('int')   
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()
        
    @pyqtSlot ('int')   
    def on_slider_b_valueChanged(self, value):
        self.SpinBox_b.setValue(value)
        self.fig1()
        
    @pyqtSlot ('int')   
    def on_slider_h_valueChanged(self, value):
        self.SpinBox_h.setValue(value)
        self.fig1()
        
    @pyqtSlot ('int')   
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()
        
    @pyqtSlot ('int')   
    def on_slider_f2_valueChanged(self, value):
        self.SpinBox_f2.setValue(value)
        self.fig1()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.show()
    sys.exit(app.exec_())