# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 01:43:29 2019

@author: USER
"""
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtCore import pyqtSlot
from UiMainApp import Ui_MainWindow
from numpy import pi , linspace, meshgrid , sin , arctan , arange  ,log
import matplotlib.cm as cm
import scipy.special as sp
def j1(x):
    return sp.jv(1,x)
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.fig1()
   
   
    def fig1(self):
        

        Lambda=self.slider_lambda.value()*1.E-9

        a=0.1
        
        I0=self.slider_I0.value()*1e-6
        
        d=self.Slider_d.value()*1e-5

        L=self.slider_l.value()
        #######
        X_Mmax = a/2 ; X_Mmin = -a/2
        Y_Mmax = X_Mmax ; Y_Mmin = X_Mmin
        N=200
        X=linspace(X_Mmin,X_Mmax,N) ; Y = X

        x=arange(-0.03,0.03,0.0003)

        y=arange(-0.03,0.03,0.0003)
        
        
        X,Y=meshgrid(x,y)
        
        R=(X*X+Y*Y)**0.5
        
        theta_rad=arctan(R/L)
        
        k=2*pi/Lambda
        
        I=(2*j1(k*d*sin(theta_rad))/(k*d*sin(theta_rad)))**2

        ########
        mpl = self.mplwidget.canvas
        mpl.ax.clear()
        mpl.ax.imshow(log(I+I0), cmap=cm.gray)
        ################
        mpl.ax.set_xlabel(u'$X (m)$' , fontsize = 12, fontweight = 'bold')
        mpl.ax.set_ylabel(u'$Y (m)$' , fontsize = 12, fontweight = 'bold')
        mpl.ax.set_xticks(linspace(0, N, 5))
        mpl.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5), color = 'r')
        mpl.ax.set_yticks(linspace(0, N, 5))
        mpl.ax.set_yticklabels(linspace(Y_Mmax, Y_Mmin, 5), color = 'r')   
        mpl.figure.suptitle('Round hole diffraction', fontsize = 16, fontweight = 'bold')
        mpl.ax.set_title(r"$\lambda = %.3e \ m , \ I0 = %.2e \ m , \ d = %.2e \ m , \ L = %.1f \ m$"% (Lambda, I0, d, L), fontsize = 10)
        
        #########
        mpl.draw()
   
    
    @pyqtSlot ('double')   
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)
    
    @pyqtSlot ('double')   
    def on_SpinBox_d_valueChanged(self, value):
        self.Slider_d.setValue(value)
        

    @pyqtSlot ('double')   
    def on_SpinBox_I0_valueChanged(self, value):
        self.slider_I0.setValue(value)
    
    @pyqtSlot ('double')   
    def on_SpinBox_l_valueChanged(self, value):
        self.slider_l.setValue(value)
        
   
    @pyqtSlot ('int')   
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()
    
    @pyqtSlot ('int')   
    def on_Slider_d_valueChanged(self, value):
        self.SpinBox_d.setValue(value)
        self.fig1()
        
    @pyqtSlot ('int')   
    def on_slider_l_valueChanged(self, value):
        self.SpinBox_l.setValue(value)
        self.fig1()
    

        
    @pyqtSlot ('int')   
    def on_slider_I0_valueChanged(self, value):
        self.SpinBox_I0.setValue(value)
        self.fig1()
        
   
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.show()
    sys.exit(app.exec_())