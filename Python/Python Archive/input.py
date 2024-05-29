import os.path


def check_pdf(pdf_file):
    if os.path.exists(pdf_file) and os.path.splitext(pdf_file)[1].lower() == ".pdf":
        text, start_pressed = gui.QInputDialog.getText(
            gui.PDF(), "Enter the page numbers",
            "Please type one integer, list of numbers (Make sure it has spaces between them)\n"
            "or enter the range of pages you want, for example: '1-10'"
        )

        if start_pressed and text:
            num_list = pdf_list(text)
            main.create_pdf(num_list)


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
