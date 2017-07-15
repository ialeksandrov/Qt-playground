import sys
from PyQt4 import QtGui

def window():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    b = QtGui.QLabel(widget)
    b.setText("Hello World!")
    widget.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    widget.setWindowTitle("PyQT")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
