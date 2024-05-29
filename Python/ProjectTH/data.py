import json
import random
import sys
import os
import uuid
import window

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
from time import sleep

file_name = f"log{uuid.uuid4()}.txt"  # create random log ID file for errors

# Try to load the json file, if not available, it will throw Exception
try:
    data_file = 'data/psychometric_data.json'
    with open(data_file, encoding='utf-8') as file:
        data = json.load(file)

except FileNotFoundError as e:
    app = QApplication(sys.argv)
    # Message error for data
    error = QMessageBox()
    error.about(error, "Test Helper", "Data file not found")
    error.setIcon(error.Information)

    try:
        os.mkdir('errors')
        f = open("errors/" + file_name, "w")
        f.write(str(e))
        f.close()
    except FileExistsError:
        f = open(file_name, "w")
        f.write(str(e))
        f.close()
    sys.exit(e)


class testhelper(QMainWindow):

    def __init__(self, unit):
        super().__init__()

        self.answer = None

        self.time = 21  # 20 secs to answer a question, a int variable
        self.questions = 1  # question number
        self.score_count = 0  # Score number

        self.words = []  # List of random words, reload() function generate new words to the class's list
        self.element_list = [0, 1, 2, 3]  # List of numbers that presents the 4 choices

        self.question = window.question()  # The question window from window.py
        self.timer = QTimer(self)  # Timer function from Qt lib
        self.unit = unit  # Variable that Inherit from units.py to place the data on question window

        self.word = QLabel(self.question)  # Creating the word label
        self.bool_answer = QLabel(self.question)  # Shows if the answer is true or false
        self.timer_label = QLabel(self.question)  # Timer label
        self.score_label = QLabel(self.question)  # Score label

        # Buttons
        self.choice1 = QPushButton(self.question)
        self.choice2 = QPushButton(self.question)
        self.choice3 = QPushButton(self.question)
        self.choice4 = QPushButton(self.question)
        self.back_button = QPushButton(self.question)

        # Widgets
        self.word.setFont(QFont('Arial', 19))
        self.word.setGeometry(QRect(420, -350, 341, 900))

        self.choice1.setObjectName("choice1")
        self.choice1.setGeometry(QRect(530, 190, 151, 900))
        self.choice1.resize(450, 100)
        self.choice1.setFont(QFont('Gisha', 8))

        self.choice2.setObjectName("choice2")
        self.choice2.setGeometry(QRect(530, 310, 151, 900))
        self.choice2.resize(450, 100)
        self.choice2.setFont(QFont('Gisha', 8))

        self.choice3.setObjectName("choice3")
        self.choice3.setGeometry(QRect(7, 310, 151, 900))
        self.choice3.resize(450, 100)
        self.choice3.setFont(QFont('Gisha', 8))

        self.choice4.setObjectName("choice4")
        self.choice4.setGeometry(QRect(7, 190, 151, 900))
        self.choice4.resize(450, 100)
        self.choice4.setFont(QFont('Gisha', 8))

        self.timer_label.setGeometry(QRect(900, 10, 100, 50))
        self.timer_label.setFont(QFont('Gisha', 15))
        self.timer_label.setText('Timer: invalid')
        self.timer_label.adjustSize()

        self.bool_answer.setGeometry(QRect(0, 20, 900, 900))
        self.bool_answer.setFont(QFont('Arial', 10))

        self.question.word.clear()

        self.score_label.setGeometry(QRect(885, 450, 100, 50))
        self.score_label.setFont(QFont('Gisha', 12))
        self.score_label.setText('Score: invalid')

        # Back to main menu button if the users wants to quit from test to another test
        self.back_button.setText("Main Menu")
        self.back_button.clicked.connect(lambda: self.question.main_menu())
        self.back_button.clicked.connect(self.Total)
        self.back_button.setGeometry(QRect(10, 10, 100, 50))

        self.question.show()

    def update_timer(self):
        # Timer function, just clears and shows the number of time ...
        self.timer_label.clear()
        self.timer_label.setText('Timer: ' + str(self.time))

    def Total(self):
        # Calculates the number of questions and number of answers that the user knows how much words he was right
        total = "You succeeded to answer right " + str(self.score_count) + " questions from " + str(self.questions)
        msg = QMessageBox()
        msg.about(self, "Test Helper", total)
        msg.setIcon(msg.Information)

    def score(self):
        # Score function, shows the score data for the user
        self.score_label.clear()
        self.score_label.setText('Score: ' + str(self.score_count))
        self.score_label.adjustSize()

    def refresh(self):
        self.choice1.disconnect()
        self.choice2.disconnect()
        self.choice3.disconnect()
        self.choice4.disconnect()

    def check_answer(self):
        # sender() is function from QMainWindow that signals the button
        # Correct
        if self.sender().text() == self.answer:
            self.bool_answer.setText("Correct!, it is: " + self.answer)  # Shows the right word after answering
            self.sender().setStyleSheet(
                'background-color: green')  # Shows background color green if the user is right
            self.score_count += 1

        # Wrong
        elif self.sender().text() != self.answer:
            self.bool_answer.setText("Wrong, the word for \n" + self.word.text() + " is " + self.answer)
            self.sender().setStyleSheet('background-color: red')  # Shows background color red if the user is wrong

            # Shows the right answer if we wrong
            if self.choice1.text() == self.answer:
                self.choice1.setStyleSheet('background-color: green')
            elif self.choice2.text() == self.answer:
                self.choice2.setStyleSheet('background-color: green')
            elif self.choice3.text() == self.answer:
                self.choice3.setStyleSheet('background-color: green')
            elif self.choice4.text() == self.answer:
                self.choice4.setStyleSheet('background-color: green')

        self.time = 1
        self.words.clear()  # Clears the data from the program

    def reload(self):

        self.timer.timeout.connect(self.timeout)  # Start the timer event (from 20)
        self.timer.start(1000)  # 1000 = 1 sec

        _random_word = random.choice(self.element_list)  # Word generator, one word to present in the GUI
        unit_words = random.sample(self.unit.items(), 5)  # Choosing 5 items from the data to present
        random.shuffle(self.element_list)  # Makes the random effect here on buttons
        self.words.append(unit_words)  # Loads the data to words list

        #  Variables to show the data on GUI
        word = self.words[0][self.element_list[_random_word]][0]
        choice1 = self.words[0][self.element_list[0]][1]
        choice2 = self.words[0][self.element_list[1]][1]
        choice3 = self.words[0][self.element_list[2]][1]
        choice4 = self.words[0][self.element_list[3]][1]

        self.answer = self.words[0][self.element_list[_random_word]][1]

        self.word.clear()
        self.word.setText(word)
        self.choice1.setText(choice1)
        self.choice2.setText(choice2)
        self.choice3.setText(choice3)
        self.choice4.setText(choice4)

        # Resets the color after the user choice
        self.choice1.setStyleSheet('background-color: none')
        self.choice2.setStyleSheet('background-color: none')
        self.choice3.setStyleSheet('background-color: none')
        self.choice4.setStyleSheet('background-color: none')

        # check_answer() method connecting to buttons
        self.choice1.clicked.connect(self.check_answer)
        self.choice2.clicked.connect(self.check_answer)
        self.choice3.clicked.connect(self.check_answer)
        self.choice4.clicked.connect(self.check_answer)

        self.timeout()  # Resets the timer
        self.score()  # Updates the Score
        self.questions += 1

        return self.answer

    def timeout(self):
        self.time -= 1  # Decrease timer by 1

        # Reset the timer and back again for next question
        if self.time == 0:
            sleep(0.8)
            self.time = 21
            self.timer.disconnect()  # Killing the previous timer
            self.refresh()  # Killing the previous buttons
            self.reload()  # Reload again the questions

        self.update_timer()  # Calls the function to reset it again, to another question


"""
Calculations:

Test Helper:

List Number:
   l = first_list (First Question)
   l = 0
   l += 1 # Moving from generating Question
  
Element presenting the String variable name in the dict,
Because we generating 5 random dict data from json, we need to present the random words by element number.

Element Number:

   element = 0
   element += 1 # No need to present in the code, easier to by making element list (4 Numbers), instead of increase by 1


# For English random words, works for Hebrew words also.

Hebrew Number:
   h = 1 (h must to be 1 to present Hebrew)

English Number: 
   e = 0 (e must to be 0 to present English)

Hebrew Object = [l][element][h]
English Object = [l][element][e]

Question Number = [l][element][0]
Answer Number = [l][element][1]

Choices = Answer([l][element][1]), Choice1([l][element+1][1], Choice2([l][element+2][1], Choice3([l][element+3][1] and
 Choice([l][element+4][1]

# From my tested list in my test python app

List 0:
   [0][0]  [0][1]  [1][0]   [1][1]   [2][0]    [2][1]       [3][0]  [3][1]     [4][1]     [4][0]
[[('Cat', 'חתול'), ('Fish', 'דג'), ('Dolphin', 'דולפין'), ('Rhino', 'קרנף'), ('Octupus', 'תמנון')]

List 1:
   [0][0]     [0][1]      [1][0]   [1][1]   [2][0]    [2][1]    [3][0]  [3][1]  [4][1]     [4][0]
[('Dolphin', 'דולפין'), ('Octupus', 'תמנון'), ('Cat', 'חתול'), ('Rhino', 'קרנף'), ('Fish', 'דג')]

List 2:
Another list of 5 objects

and etc ...
"""
