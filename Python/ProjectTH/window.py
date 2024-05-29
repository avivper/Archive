import data
import units
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.hebrew = None
        self.english = None

        self.test_helper = QLabel(self)
        self.version = QLabel(self)
        self.aviv = QLabel(self)
        self.hebrew_category_button = QPushButton(self)
        self.english_category_button = QPushButton(self)

        self.setWindowTitle("Test Helper")
        self.setFixedSize(797, 549)
        self.initMainUI()
        self.setWindowIcon(QIcon('testhelper.ico'))
        self.setLayout(QGridLayout())

    def initMainUI(self):

        self.test_helper.setText("Test Helper")
        self.test_helper.setGeometry(QRect(245, 10, 341, 181))
        self.test_helper.setFont(QFont('Gisha', 30))

        self.version.setText("Version: Alpha 0.4")
        self.version.setFont(QFont('Gisha', 9))
        self.version.setGeometry(QRect(0, 0, 100, 30))
        self.version.adjustSize()

        self.aviv.setText("By Aviv.")
        self.aviv.setFont(QFont('Tahoma', 9))
        self.aviv.setGeometry(QRect(0, 520, 100, 30))
        self.aviv.adjustSize()

        self.hebrew_category_button.setText("Hebrew")
        self.hebrew_category_button.clicked.connect(self.switch_hebrew)
        self.hebrew_category_button.setGeometry(QRect(440, 290, 271, 151))
        self.hebrew_category_button.setFont(QFont('Gisha', 12))

        self.english_category_button.setText("English")
        self.english_category_button.clicked.connect(self.switch_english)
        self.english_category_button.setGeometry(QRect(90, 290, 271, 151))
        self.english_category_button.setFont(QFont('Gisha', 12))

    def switch_hebrew(self):
        self.hebrew = Hebrew()
        self.hebrew.show()
        self.hide()

    def switch_english(self):
        self.english = English()
        self.english.show()
        self.hide()


class Hebrew(QMainWindow):

    def __init__(self):
        super(Hebrew, self).__init__()

        self.hebrew_title = QLabel(self)
        self.ag_button = QPushButton(self)
        self.dv_button = QPushButton(self)
        self.lm_button = QPushButton(self)
        self.rt_button = QPushButton(self)
        self.ne_button = QPushButton(self)
        self.pk_button = QPushButton(self)
        self.zk_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self._main_window = None

        self.initHebrewUI()
        self.setWindowTitle("Test Helper")
        self.setFixedSize(797, 549)
        self.setLayout(QGridLayout())

    def initHebrewUI(self):

        self.hebrew_title.setText("עברית")
        self.hebrew_title.setGeometry(QRect(230, 10, 341, 181))
        self.hebrew_title.setFont(QFont('Gisha', 30))

        self.ag_button.clicked.connect(self.hide)
        self.ag_button.clicked.connect(lambda: data.testhelper(unit=units.a_g).reload())
        self.ag_button.setGeometry(QRect(530, 190, 151, 91))
        self.ag_button.setText("א-ג")

        self.dv_button.clicked.connect(self.unit_not_available)
        self.dv_button.setGeometry(QRect(330, 190, 151, 91))
        self.dv_button.setText("ד-ו")

        self.lm_button.clicked.connect(self.hide)
        self.lm_button.clicked.connect(lambda: data.testhelper(unit=units.l_m).reload())
        self.lm_button.setGeometry(QRect(530, 310, 151, 91))
        self.lm_button.setText("ל-מ")

        self.rt_button.clicked.connect(self.unit_not_available)
        self.rt_button.setGeometry(QRect(330, 430, 151, 91))
        self.rt_button.setText("ר-ת")

        self.ne_button.clicked.connect(self.hide)
        self.ne_button.clicked.connect(lambda: data.testhelper(unit=units.n_e).reload())
        self.ne_button.setGeometry(QRect(330, 310, 151, 91))
        self.ne_button.setText("נ-ע")

        self.pk_button.setGeometry(QRect(130, 310, 151, 91))
        self.pk_button.clicked.connect(self.hide)
        self.pk_button.clicked.connect(lambda: data.testhelper(unit=units.p_k).reload())
        self.pk_button.setText("פ-ק")

        self.zk_button.setGeometry(QRect(130, 190, 151, 91))
        self.zk_button.clicked.connect(self.unit_not_available)
        self.zk_button.setText("ז-כ")

        self.back_button.setGeometry(QRect(530, 430, 151, 91))
        self.back_button.clicked.connect(self.main_menu)
        self.back_button.setText("Back")

    def main_menu(self):
        self._main_window = MainWindow()
        self._main_window.show()
        self.hide()

    def unit_not_available(self):
        msg = QMessageBox()
        msg.about(self, "Test Helper", "Unit is not available yet")
        msg.setIcon(msg.Information)


class English(QMainWindow):
    def __init__(self):
        super(English, self).__init__()

        self._main_window = None
        self.english_title = QLabel(self)
        self.back_button = QPushButton(self)

        self.unit1_button = QPushButton(self)
        self.unit2_button = QPushButton(self)
        self.unit3_button = QPushButton(self)
        self.unit4_button = QPushButton(self)
        self.unit5_button = QPushButton(self)
        self.unit6_button = QPushButton(self)
        self.unit7_button = QPushButton(self)
        self.unit8_button = QPushButton(self)
        self.unit9_button = QPushButton(self)
        self.unit10_button = QPushButton(self)

        self.setLayout(QGridLayout())
        self.setWindowTitle("Test Helper")
        self.initEnglish()
        self.setFixedSize(797, 700)

    def initEnglish(self):

        self.english_title.setText("English")
        self.english_title.setGeometry(QRect(320, 10, 341, 181))
        self.english_title.setFont(QFont('Arial', 30))

        self.unit1_button.clicked.connect(self.hide)
        self.unit1_button.clicked.connect(lambda: data.testhelper(unit=units.unit1).reload())
        self.unit1_button.setGeometry(QRect(530, 190, 151, 91))
        self.unit1_button.setText("Unit 1")

        self.unit2_button.clicked.connect(self.hide)
        self.unit2_button.clicked.connect(lambda: data.testhelper(unit=units.unit2).reload())
        self.unit2_button.setGeometry(QRect(330, 190, 151, 91))
        self.unit2_button.setText("Unit 2")

        self.unit3_button.clicked.connect(self.unit_not_available)
        self.unit3_button.setGeometry(QRect(130, 190, 151, 91))
        self.unit3_button.setText("Unit 3")

        self.unit4_button.clicked.connect(self.unit_not_available)
        self.unit4_button.setGeometry(QRect(530, 310, 151, 91))
        self.unit4_button.setText("Unit 4")

        self.unit5_button.clicked.connect(self.unit_not_available)
        self.unit5_button.setGeometry(QRect(330, 310, 151, 91))
        self.unit5_button.setText("Unit 5")

        self.unit6_button.setGeometry(QRect(130, 310, 151, 91))
        self.unit6_button.clicked.connect(self.unit_not_available)
        self.unit6_button.setText("Unit 6")

        self.unit7_button.setGeometry(QRect(530, 430, 151, 91))
        self.unit7_button.clicked.connect(self.hide)
        self.unit7_button.clicked.connect(lambda: data.testhelper(unit=units.unit7).reload())
        self.unit7_button.setText("Unit 7")

        self.unit8_button.setGeometry(QRect(330, 430, 151, 91))
        self.unit8_button.clicked.connect(self.hide)
        self.unit8_button.clicked.connect(lambda: data.testhelper(unit=units.unit8).reload())
        self.unit8_button.setText("Unit 8")

        self.unit9_button.setGeometry(QRect(130, 430, 151, 91))
        self.unit9_button.clicked.connect(self.hide)
        self.unit9_button.clicked.connect(lambda: data.testhelper(unit=units.unit9).reload())
        self.unit9_button.setText("Unit 9")

        self.unit10_button.setGeometry(QRect(330, 550, 151, 91))
        self.unit10_button.clicked.connect(self.unit_not_available)
        self.unit10_button.setText("Unit 10")

        self.back_button.setGeometry(QRect(530, 550, 151, 91))
        self.back_button.clicked.connect(self.main_menu)
        self.back_button.setText("Back")

    def main_menu(self):
        self._main_window = MainWindow()
        self._main_window.show()
        self.close()

    def unit_not_available(self):
        msg = QMessageBox()
        msg.about(self, "Test Helper", "Unit is not available yet")
        msg.setIcon(msg.Information)


class question(QMainWindow):

    def __init__(self):
        super(question, self).__init__()
        self._main_window = None
        self.word = QLabel(self)
        self.setLayout(QGridLayout())
        self.setWindowTitle("Test Helper")
        self.initquestion()
        self.setFixedSize(1030, 500)

    def initquestion(self):
        self.word.setGeometry(QRect(230, 10, 341, 181))
        self.word.setFont(QFont('Arial', 27))
        self.word.setText("Failed to load unit")

    def main_menu(self):
        self._main_window = MainWindow()
        self._main_window.show()
        self.close()
