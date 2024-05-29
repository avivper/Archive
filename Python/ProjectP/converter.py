from PyQt5.QtCore import Qt

from splitter import *


class Converter(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.soon = QLabel("Soon")

        self.soon.setFont(QFont("Arial", 9))
        self.soon.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.soon.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.soon)
        self.setLayout(self.layout)
