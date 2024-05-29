import window
import sys
import os
import uuid
from PyQt5.QtWidgets import QApplication, QMessageBox

"""
Author: Aviv
Name of the project: Test Helper


Test Helper created to help me learn words in Hebrew and English, for the Psychometric test,
it can be used for self learn to everyone.

I tried to find a App that test me and helps to memorize the dictionary of Hebrew and English words for the test.
Unfortunately, I didn't find one, so I made one.

Happy study new words,
Aviv. 
"""

file_name = f"log{uuid.uuid4()}.txt"
path = "errors/" + file_name

if __name__ == '__main__':
    try:
        if sys.version_info < (2, 7):
            error = QMessageBox()
            error.about(error, "Test Helper", "You need to install Python 3 to able to use Test Helper")
            error.setIcon(error.Information)
            sys.exit(1)

        app = QApplication(sys.argv)

        main = window.MainWindow()
        main.show()

        sys.exit(app.exec_())

    except Exception as e:
        try:
            os.mkdir('errors')
            f = open(path, "w")
            f.write(str(e))
            f.close()
        except FileExistsError:
            f = open(path, "w")
            f.write(str(e))
            f.close()
        sys.exit(e)

