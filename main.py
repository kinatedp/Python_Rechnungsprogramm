from MainGUI import MainGUI
import sys
from PyQt6 import QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    Dialog = QtWidgets.QDialog()
    Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
    ui = MainGUI(Dialog)

    Dialog.show()
    sys.exit(app.exec())

