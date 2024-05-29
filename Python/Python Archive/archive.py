import os
import sys
import PyPDF2
from time import sleep


def check_pdf(pdf_file):
    if os.path.exists(pdf_file) and os.path.splitext(pdf_file)[1].lower() == ".pdf":
        text, start_pressed = gui.QInputDialog.getText(
            gui.PDF(), "Enter the page numbers",
            "Please type one integer, list of numbers (Make sure it has spaces between them)\n"
            "or enter the range of pages you want, for example: '1-10'"
        )

        if start_pressed:
            if text:
                create_pdf(gui.PDF.input_str(), gui.PDF.output_str(), pdf_list(text))
            else:
                gui.QMessageBox.warning(
                    gui.PDF(), "Warning", "You must enter at least one number.", gui.QMessageBox.Ok
                )
        else:
            return False
    else:
        gui.QMessageBox.warning(
            gui.PDF(), "Invalid PDF file",
            "Please select a valid PDF file", gui.QMessageBox.Ok
        )


def pdf_list(text):
    page_list = []

    for item in text.split():
        try:
            if "-" in item:
                start, end = item.split("-")

                start = int(start)
                end = int(end)

                if start > end:
                    gui.QMessageBox.warning(
                        gui.PDF(), "Invalid input",
                        "The start page number should be less than or equal "
                        "to the final page number.", gui.QMessageBox.Ok
                    )

                    return

                else:
                    for page_number in range(start, end + 1):
                        page_list.append(page_number)
                        return page_list
            else:
                page_list.append(int(item))
                return page_list

        except ValueError:
            gui.QMessageBox.warning(
                gui.PDF(), "Invalid input",
                "Please enter valid page numbers.", gui.QMessageBox.Ok
            )

            return


def create_pdf(input_pdf_path, output_name, page_numbers):
    pdf_writer = PyPDF2.PdfWriter()
    folder = "Created PDF"

    if not os.path.exists(folder):  # Creating the folder for the PDF
        os.makedirs(folder)

    output_path = os.path.join(folder, output_name)

    if os.path.exists(output_path):
        choice = gui.QMessageBox.question(
            gui.PDF(), "File already exist", f"Are you want to replace {output_name}?",
            gui.QMessageBox.Yes | gui.QMessageBox.No, gui.QMessageBox.No
        )

        if choice == gui.QMessageBox.No:
            return

    with open(input_pdf_path, 'rb') as input_pdf:
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        for i in page_numbers:
            if 1 <= i <= len(pdf_reader.pages):
                pdf_writer.add_page(pdf_reader.pages[i - 1])
            else:
                gui.QMessageBox.warning(
                    gui.PDF(), "Error",
                    f"Page {i} doesn't exist in the PDF, enter valid numbers",
                    gui.QMessageBox.Ok
                )
                return
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        sleep(0.5)
        gui.QMessageBox.information(
            gui.PDF(), "Success", "PDF Created successfully!",
            gui.QMessageBox.Ok
        )

        gui.PDF.clear()


if __name__ == '__main__':
    app = gui.QApplication(sys.argv)
    window = gui.PDF()
    sys.exit(app.exec_())
