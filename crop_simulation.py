import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of simulated crop"""

    #Conatructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Crop Simulation") #Set Window Title

def main():
    crop_simulation = QApplication(sys.argv) #creates new application
    crop_window = CropWindow() #creates a new instance of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #monitor application for events

if __name__ =="__main__":
    main()
    
