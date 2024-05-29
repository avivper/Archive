import os
import PyPDF2
import sys
from time import sleep

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class PDF(QWidget):
    def __init__(self):
        super().__init__()

        # Input
        self.input = QLabel("Select the PDF file: ")
        self.input_text = QLineEdit()
        self.input_file = QPushButton("Browse")

        # Output
        self.output = QLabel("Enter the name for your new PDF file:\n(Without .pdf)")
        self.output_text = QLineEdit()

        # Button that will execute the file creation method
        self.create = QPushButton("Start")

        self.Widgets = [
            self.input, self.input_text, self.input_file,
            self.output, self.output_text, self.create
        ]

        self.init()

    def init(self):
        layout = QVBoxLayout()

        # Creating the ui functions
        for i in range(len(self.Widgets)):
            widget = self.Widgets[i]
            layout.addWidget(self.Widgets[i])

            if isinstance(widget, (QLabel, QLineEdit)):
                widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                font = QFont("Arial", 11)  # Specify font name and size
                widget.setFont(font)  # Apply the font to the widget

        self.input_file.clicked.connect(self.choose)
        self.create.clicked.connect(self.input_pages)  # Will define input_pages

        self.setLayout(layout)
        self.setWindowTitle("PDF Creator")
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.show()

    def choose(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a PDF file", "", "PDF Files (*.pdf)"
        )

        if file_path:
            self.input_text.setText(file_path)

    def execute(self):
        if self.input_text.text().strip():
            return

    def input_pages(self, pdf_file):
        if os.path.exists(pdf_file) and os.path.splitext(pdf_file)[1].lower() == ".pdf":

            pdf = self.output_text.text() + "pdf"

            text, start_pressed = QInputDialog.getText(
                self, "Enter the page numbers",
                "Please type one list of numbers "
                "(Make sure it has spaces between them)\n"
                "or enter the range of pages you want, for example: '1-10'"
            )

            if not start_pressed or text:
                return
            else:
                page_list = self.unify_pages(text)
                self.create_pdf(self.input_text.text(), pdf, page_list)

    def unify_pages(self, text):
        if not text:
            return

        page_list = []

        for item in text.split():
            if "-" in item:
                try:

                    start, end = item.split("-")

                    start = int(start)
                    end = int(end)

                    if end >= start:
                        for page_number in range(start, end + 1):
                            page_list.append(page_number)
                    else:
                        QMessageBox.warning(self, "Invalid input",
                                            "The start page number should be less than or equal "
                                            "to the end page number.",
                                            QMessageBox.Ok)
                        return

                except ValueError:
                    QMessageBox.warning(self, "Invalid input",
                                        "Please enter valid page numbers "
                                        "(only numbers and spaces).", QMessageBox.Ok)
                    return

        return page_list

    def input_pages_old(self):
        if self.input_text.text().strip():
            if self.output_text.text().strip():

                pdf_file = self.input_file.text().strip()

                if os.path.exists(pdf_file) and os.path.splitext(pdf_file)[1].lower() == ".pdf":

                    text, start_pressed = QInputDialog.getText(
                        self, "Enter the page numbers",
                        "Please type one list of numbers (Make sure it has spaces between them)\n"
                        "or enter the range of pages you want, for example: '1-10"
                    )

                    if start_pressed:
                        if text:

                            page_list = []

                            for item in text.split():
                                if "-" in item:
                                    try:

                                        start, end = item.split("-")

                                        start = int(start)
                                        end = int(end)

                                        if start > end:
                                            QMessageBox.warning(
                                                self, "Invalid input",
                                                "The start page number should be less than or equal "
                                                "to the final page number. ",
                                                QMessageBox.Ok
                                            )
                                            return
                                        else:
                                            for page_number in range(start, end + 1):
                                                page_list.append(page_number)

                                    except ValueError:
                                        QMessageBox.warning(
                                            self, "Invalid input,"
                                                  "Please enter  valid page numbers "
                                                  "(Only numbers and spaces).", QMessageBox.Ok
                                        )

                                        return
                                else:
                                    try:
                                        page_list.append(int(item))

                                    except ValueError:  # Fix
                                        QMessageBox.warning(
                                            self, "Invalid input,"
                                                  "Please enter  valid page numbers "
                                                  "(Only numbers and spaces).", QMessageBox.Ok
                                        )
                            pdf = self.output_text.text() + ".pdf"
                            self.create_pdf(self.input_text.text(), pdf, page_list)

                        else:
                            QMessageBox.warning(self, "Warning",
                                                "You must enter at least one number.", QMessageBox.Ok)
                    else:
                        return False

                else:  # If the user type invalid file or unavailable pdf file
                    QMessageBox.warning(self, "Invalid PDF file",
                                        "Please select a valid PDF file", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Invalid name",
                                    "Please enter a name for your new file ", QMessageBox)
        else:
            QMessageBox.warning(
                self, "Invalid name", "Please select a PDF file",
                QMessageBox.Ok
            )

    def create_pdf(self, input_pdf_path, output_name, page_numbers):
        pdf_writer = PyPDF2.PdfWriter()
        folder = "Created PDF"

        if not os.path.exists(folder):
            os.makedirs(folder)

        output_path = os.path.join(folder, output_name)

        if os.path.exists(output_path):
            choice = QMessageBox.question(
                self, "File already exist",
                f"Are you sure to replace {output_name}?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if choice == QMessageBox.No:
                return

        with open(input_pdf_path, 'rb') as input_pdf:
            pdf_reader = PyPDF2.PdfReader(input_pdf)

            for i in page_numbers:
                if 1 <= i <= len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[i - 1])

                else:
                    QMessageBox.warning(
                        self, "Error",
                        f"Page {i} does not exist in the PDF enter valid numbers",
                        QMessageBox.Ok)

                    return

            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            sleep(0.5)
            QMessageBox.Information(
                self, "Success", "PDF created successfully!",
                QMessageBox.Ok
            )
            self.output_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDF()
    sys.exit(app.exec_())
