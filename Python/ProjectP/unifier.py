from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from main import Confirmation
from splitter import PyPDF2, os


class Unifier(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # 2 Input in parallel
        self.input = QLabel("Select two PDF files to unify")
        self.input_1 = QLineEdit()
        self.input_2 = QLineEdit()
        self.browse = QPushButton("Browse")

        # File labels
        self.file_1 = QLabel("File 1")
        self.file_2 = QLabel("File 2")

        # Output
        self.output = QLabel("Enter the name for your new PDF file:\n(Without .pdf)")
        self.output_text = QLineEdit()  # Textfield of output new file

        self.unify = QPushButton("Unify")

        self.Widgets = [
            self.input, self.file_1, self.input_1, self.file_2, self.input_2, self.browse,
            self.output, self.output_text, self.unify
        ]

        self.init()

    def init(self):
        for i in range(len(self.Widgets)):
            widget = self.Widgets[i]
            self.layout.addWidget(widget)

            if isinstance(widget, (QLabel, QLineEdit)):
                widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                font = QFont("Arial", 9)
                widget.setFont(font)

        self.browse.clicked.connect(self.choose)
        self.unify.clicked.connect(self.execute)
        self.setLayout(self.layout)

    def clear(self):  # Clears the inputs, will call if the user choose to clear
        self.output_text.clear()
        self.input_1.clear()
        self.input_2.clear()

    def choose(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a PDF file", "", "PDF Files (*.pdf)"
        )

        if file_path:
            self.embed_path(file_path)

    def generate_str(self):
        return self.output_text.text() + ".pdf"

    def embed_path(self, file_path):   # Set the file on QLineedit based on user's choice
        embed = RadioInput()
        option = embed.parse_input()

        if option:
            self.input_1.setText(file_path)
        elif option is False:
            self.input_2.setText(file_path)
        else:
            return

    def execute(self):  # Execute the merge algorithm
        if self.input_1.text().strip() and self.input_2.text().strip() and self.output_text.text().strip():
            filename = self.generate_str()

            if self.input_1.text().strip() == self.input_2.text().strip():
                confirmation = Confirmation()
                confirmation.confirm("You chose the same file, are you sure to proceed?")
                confirm = confirmation.exec_()

                if confirm:
                    self.merger(self.input_1.text().strip(), self.input_2.text().strip(), filename)
                else:
                    return
            else:
                self.merger(self.input_1.text().strip(), self.input_2.text().strip(), filename)
        else:
            QMessageBox.warning(self, "Invalid", "Please fill all the blank lines",
                                QMessageBox.Ok)

    def merger(self, input_1, input_2, output_name):  # Merge the files
        confirmation = Confirmation()
        merger = PyPDF2.PdfMerger()

        folder = "Created PDF"

        if not os.path.exists(folder):
            os.makedirs(folder)

        output_path = os.path.join(folder, output_name)

        if os.path.exists(output_path):
            choice = Confirmation()
            choice.confirm(f"File already exists, Are you sure you want to replace {output_name}?")
            result = choice.exec_()

            if not result:
                return

        with open(input_1, 'rb') as pdf_file1:
            merger.append(pdf_file1)

        with open(input_2, 'rb') as pdf_file2:
            merger.append(pdf_file2)

        with open(output_path, 'wb') as merged_file:
            merger.write(merged_file)

        confirmation.confirm("PDF Created successfully, clear the input lines?")
        confirm = confirmation.exec_()

        if confirm:  # clears the lines
            self.clear()
        else:
            return


class RadioInput(QDialog):
    def __init__(self, parent=None):
        super(RadioInput, self).__init__(parent)

        self.setWindowTitle("Input")

        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout(self)

        self.file = None

        self.input_1 = QRadioButton("File 1")
        self.input_2 = QRadioButton("File 2")

        self.form_layout.addRow("Select an option: ", self.input_1)
        self.form_layout.addRow("", self.input_2)

        self.buttons_layout = QHBoxLayout()
        self.select_button = QPushButton("Select")
        self.cancel_button = QPushButton("Cancel")

        self.buttons_layout.addWidget(self.select_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttons_layout)

        self.select_button.clicked.connect(self.return_option)
        self.cancel_button.clicked.connect(self.reject)

    def return_option(self):
        if self.input_1.isChecked():
            self.file = True
        elif self.input_2.isChecked():
            self.file = False
        else:
            return None

        self.accept()

    def parse_input(self):
        result = self.exec_()
        if result == QDialog.Accepted:
            return self.file

        return None
