# Wordle solver created by Tyler Safe in Feb/March 2022

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
import os

# class that creates the UI and performs the functionality of the solver
class Ui_MainWindow(object):
    # auto generated code from pyqt5 to create the UI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 141, 41))
        self.label.setObjectName("label")
        self.first_1 = QtWidgets.QPushButton(self.centralwidget)
        self.first_1.setGeometry(QtCore.QRect(200, 120, 51, 51))
        self.first_1.setText("")
        self.first_1.setObjectName("first_1")
        self.first_1.setFont(QFont('Times', 20))
        self.first_2 = QtWidgets.QPushButton(self.centralwidget)
        self.first_2.setGeometry(QtCore.QRect(270, 120, 51, 51))
        self.first_2.setText("")
        self.first_2.setObjectName("first_2")
        self.first_2.setFont(QFont('Times', 20))
        self.first_3 = QtWidgets.QPushButton(self.centralwidget)
        self.first_3.setGeometry(QtCore.QRect(340, 120, 51, 51))
        self.first_3.setText("")
        self.first_3.setObjectName("first_3")
        self.first_3.setFont(QFont('Times', 20))
        self.first_4 = QtWidgets.QPushButton(self.centralwidget)
        self.first_4.setGeometry(QtCore.QRect(410, 120, 51, 51))
        self.first_4.setText("")
        self.first_4.setObjectName("first_4")
        self.first_4.setFont(QFont('Times', 20))
        self.first_5 = QtWidgets.QPushButton(self.centralwidget)
        self.first_5.setGeometry(QtCore.QRect(480, 120, 51, 51))
        self.first_5.setText("")
        self.first_5.setObjectName("first_5")
        self.first_5.setFont(QFont('Times', 20))
        self.submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_1.setGeometry(QtCore.QRect(560, 130, 81, 31))
        self.submit_1.setObjectName("submit_1")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(340, 70, 81, 31))
        self.start.setObjectName("start")
        self.second_1 = QtWidgets.QPushButton(self.centralwidget)
        self.second_1.setGeometry(QtCore.QRect(200, 190, 51, 51))
        self.second_1.setText("")
        self.second_1.setObjectName("second_1")
        self.second_3 = QtWidgets.QPushButton(self.centralwidget)
        self.second_3.setGeometry(QtCore.QRect(340, 190, 51, 51))
        self.second_3.setText("")
        self.second_3.setObjectName("second_3")
        self.submit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_2.setGeometry(QtCore.QRect(560, 200, 81, 31))
        self.submit_2.setObjectName("submit_2")
        self.second_2 = QtWidgets.QPushButton(self.centralwidget)
        self.second_2.setGeometry(QtCore.QRect(270, 190, 51, 51))
        self.second_2.setText("")
        self.second_2.setObjectName("second_2")
        self.second_4 = QtWidgets.QPushButton(self.centralwidget)
        self.second_4.setGeometry(QtCore.QRect(410, 190, 51, 51))
        self.second_4.setText("")
        self.second_4.setObjectName("second_4")
        self.second_5 = QtWidgets.QPushButton(self.centralwidget)
        self.second_5.setGeometry(QtCore.QRect(480, 190, 51, 51))
        self.second_5.setText("")
        self.second_5.setObjectName("second_5")
        self.third_1 = QtWidgets.QPushButton(self.centralwidget)
        self.third_1.setGeometry(QtCore.QRect(200, 260, 51, 51))
        self.third_1.setText("")
        self.third_1.setObjectName("third_1")
        self.third_3 = QtWidgets.QPushButton(self.centralwidget)
        self.third_3.setGeometry(QtCore.QRect(340, 260, 51, 51))
        self.third_3.setText("")
        self.third_3.setObjectName("third_3")
        self.submit_3 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_3.setGeometry(QtCore.QRect(560, 270, 81, 31))
        self.submit_3.setObjectName("submit_3")
        self.third_2 = QtWidgets.QPushButton(self.centralwidget)
        self.third_2.setGeometry(QtCore.QRect(270, 260, 51, 51))
        self.third_2.setText("")
        self.third_2.setObjectName("third_2")
        self.third_4 = QtWidgets.QPushButton(self.centralwidget)
        self.third_4.setGeometry(QtCore.QRect(410, 260, 51, 51))
        self.third_4.setText("")
        self.third_4.setObjectName("third_4")
        self.third_5 = QtWidgets.QPushButton(self.centralwidget)
        self.third_5.setGeometry(QtCore.QRect(480, 260, 51, 51))
        self.third_5.setText("")
        self.third_5.setObjectName("third_5")
        self.fourth_1 = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_1.setGeometry(QtCore.QRect(200, 330, 51, 51))
        self.fourth_1.setText("")
        self.fourth_1.setObjectName("fourth_1")
        self.fourth_3 = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_3.setGeometry(QtCore.QRect(340, 330, 51, 51))
        self.fourth_3.setText("")
        self.fourth_3.setObjectName("fourth_3")
        self.submit_4 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_4.setGeometry(QtCore.QRect(560, 340, 81, 31))
        self.submit_4.setObjectName("submit_4")
        self.fourth_2 = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_2.setGeometry(QtCore.QRect(270, 330, 51, 51))
        self.fourth_2.setText("")
        self.fourth_2.setObjectName("fourth_2")
        self.fourth_4 = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_4.setGeometry(QtCore.QRect(410, 330, 51, 51))
        self.fourth_4.setText("")
        self.fourth_4.setObjectName("fourth_4")
        self.fourth_5 = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_5.setGeometry(QtCore.QRect(480, 330, 51, 51))
        self.fourth_5.setText("")
        self.fourth_5.setObjectName("fourth_5")
        self.fifth_1 = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_1.setGeometry(QtCore.QRect(200, 400, 51, 51))
        self.fifth_1.setText("")
        self.fifth_1.setObjectName("fifth_1")
        self.fifth_3 = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_3.setGeometry(QtCore.QRect(340, 400, 51, 51))
        self.fifth_3.setText("")
        self.fifth_3.setObjectName("fifth_3")
        self.submit_5 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_5.setGeometry(QtCore.QRect(560, 410, 81, 31))
        self.submit_5.setObjectName("submit_5")
        self.fifth_2 = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_2.setGeometry(QtCore.QRect(270, 400, 51, 51))
        self.fifth_2.setText("")
        self.fifth_2.setObjectName("fifth_2")
        self.fifth_4 = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_4.setGeometry(QtCore.QRect(410, 400, 51, 51))
        self.fifth_4.setText("")
        self.fifth_4.setObjectName("fifth_4")
        self.fifth_5 = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_5.setGeometry(QtCore.QRect(480, 400, 51, 51))
        self.fifth_5.setText("")
        self.fifth_5.setObjectName("fifth_5")
        self.sixth_1 = QtWidgets.QPushButton(self.centralwidget)
        self.sixth_1.setGeometry(QtCore.QRect(200, 470, 51, 51))
        self.sixth_1.setText("")
        self.sixth_1.setObjectName("sixth_1")
        self.sixth_3 = QtWidgets.QPushButton(self.centralwidget)
        self.sixth_3.setGeometry(QtCore.QRect(340, 470, 51, 51))
        self.sixth_3.setText("")
        self.sixth_3.setObjectName("sixth_3")
        self.submit_6 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_6.setGeometry(QtCore.QRect(560, 480, 81, 31))
        self.submit_6.setObjectName("submit_6")
        self.sixth_2 = QtWidgets.QPushButton(self.centralwidget)
        self.sixth_2.setGeometry(QtCore.QRect(270, 470, 51, 51))
        self.sixth_2.setText("")
        self.sixth_2.setObjectName("sixth_2")
        self.sixth_4 = QtWidgets.QPushButton(self.centralwidget)
        self.sixth_4.setGeometry(QtCore.QRect(410, 470, 51, 51))
        self.sixth_4.setText("")
        self.sixth_4.setObjectName("sixth_4")
        self.sixth_5 = QtWidgets.QPushButton(self.centralwidget)
        self.sixth_5.setGeometry(QtCore.QRect(480, 470, 51, 51))
        self.sixth_5.setText("")
        self.sixth_5.setObjectName("sixth_5")
        self.reset_game = QtWidgets.QPushButton(self.centralwidget)
        self.reset_game.setGeometry(QtCore.QRect(560, 130, 81, 31))
        self.reset_game.setText("")
        self.reset_game.setObjectName("reset_game")
        self.reset_game.move(340, 538)
        # resize text within the buttons
        self.second_1.setFont(QFont('Times', 20))
        self.second_2.setFont(QFont('Times', 20))
        self.second_3.setFont(QFont('Times', 20))
        self.second_4.setFont(QFont('Times', 20))
        self.second_5.setFont(QFont('Times', 20))
        self.third_1.setFont(QFont('Times', 20))
        self.third_2.setFont(QFont('Times', 20))
        self.third_3.setFont(QFont('Times', 20))
        self.third_4.setFont(QFont('Times', 20))
        self.third_5.setFont(QFont('Times', 20))
        self.fourth_1.setFont(QFont('Times', 20))
        self.fourth_2.setFont(QFont('Times', 20))
        self.fourth_3.setFont(QFont('Times', 20))
        self.fourth_4.setFont(QFont('Times', 20))
        self.fourth_5.setFont(QFont('Times', 20))
        self.fifth_1.setFont(QFont('Times', 20))
        self.fifth_2.setFont(QFont('Times', 20))
        self.fifth_3.setFont(QFont('Times', 20))
        self.fifth_4.setFont(QFont('Times', 20))
        self.fifth_5.setFont(QFont('Times', 20))
        self.sixth_1.setFont(QFont('Times', 20))
        self.sixth_2.setFont(QFont('Times', 20))
        self.sixth_3.setFont(QFont('Times', 20))
        self.sixth_4.setFont(QFont('Times', 20))
        self.sixth_5.setFont(QFont('Times', 20))
        # setup party gif (for some reason doesn't work when launched from executable)
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(170, 115, 600, 410))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.movie = QMovie(os.path.join(__location__, "party_gif.gif"))
        self.label_13.setMovie(self.movie)
        self.label_13.setHidden(True)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
        # get all the word data from the text file
        f = open('words.txt', 'r')
        self.words = f.read().split()
        # create list to track amount of button clicks
        self.count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
        # keep track of used letters
        self.used_letters = []
        self.green_letter = []
        self.position = []
        self.yellow_letter = []
        self.place = []
        self.min_word = ''
        
        try:
            # when a word is submitted perform the calculation
            self.start.clicked.connect(lambda: self.calculate_word(self.first_1, self.first_2, self.first_3, self.first_4, self.first_5, 999))
            self.submit_1.clicked.connect(lambda: self.calculate_word(self.second_1, self.second_2, self.second_3, self.second_4, self.second_5, 0))
            self.submit_2.clicked.connect(lambda: self.calculate_word(self.third_1, self.third_2, self.third_3, self.third_4, self.third_5, 5))
            self.submit_3.clicked.connect(lambda: self.calculate_word(self.fourth_1, self.fourth_2, self.fourth_3, self.fourth_4, self.fourth_5, 10))
            self.submit_4.clicked.connect(lambda: self.calculate_word(self.fifth_1, self.fifth_2, self.fifth_3, self.fifth_4, self.fifth_5, 15))
            self.submit_5.clicked.connect(lambda: self.calculate_word(self.sixth_1, self.sixth_2, self.sixth_3, self.sixth_4, self.sixth_5, 20))
            self.submit_6.clicked.connect(lambda: self.calculate_word(self.sixth_1, self.sixth_2, self.sixth_3, self.sixth_4, self.sixth_5, 20))
        except:
            print('Incorrect button, please use them in order or press the Reset button to start again')
        
        # chance the colour of buttons as they are selected to idicate whether they are in the word or correct position
        self.first_1.clicked.connect(lambda: self.button_colour(self.first_1, 0))
        self.first_2.clicked.connect(lambda: self.button_colour(self.first_2, 1))
        self.first_3.clicked.connect(lambda: self.button_colour(self.first_3, 2))
        self.first_4.clicked.connect(lambda: self.button_colour(self.first_4, 3))
        self.first_5.clicked.connect(lambda: self.button_colour(self.first_5, 4))
        self.second_1.clicked.connect(lambda: self.button_colour(self.second_1, 5))
        self.second_2.clicked.connect(lambda: self.button_colour(self.second_2, 6))
        self.second_3.clicked.connect(lambda: self.button_colour(self.second_3, 7))
        self.second_4.clicked.connect(lambda: self.button_colour(self.second_4, 8))
        self.second_5.clicked.connect(lambda: self.button_colour(self.second_5, 9))
        self.third_1.clicked.connect(lambda: self.button_colour(self.third_1, 10))
        self.third_2.clicked.connect(lambda: self.button_colour(self.third_2, 11))
        self.third_3.clicked.connect(lambda: self.button_colour(self.third_3, 12))
        self.third_4.clicked.connect(lambda: self.button_colour(self.third_4, 13))
        self.third_5.clicked.connect(lambda: self.button_colour(self.third_5, 14))
        self.fourth_1.clicked.connect(lambda: self.button_colour(self.fourth_1, 15))
        self.fourth_2.clicked.connect(lambda: self.button_colour(self.fourth_2, 16))
        self.fourth_3.clicked.connect(lambda: self.button_colour(self.fourth_3, 17))
        self.fourth_4.clicked.connect(lambda: self.button_colour(self.fourth_4, 18))
        self.fourth_5.clicked.connect(lambda: self.button_colour(self.fourth_5, 19))
        self.fifth_1.clicked.connect(lambda: self.button_colour(self.fifth_1, 20))
        self.fifth_2.clicked.connect(lambda: self.button_colour(self.fifth_2, 21))
        self.fifth_3.clicked.connect(lambda: self.button_colour(self.fifth_3, 22))
        self.fifth_4.clicked.connect(lambda: self.button_colour(self.fifth_4, 23))
        self.fifth_5.clicked.connect(lambda: self.button_colour(self.fifth_5, 24))
        self.sixth_1.clicked.connect(lambda: self.button_colour(self.sixth_1, 25))
        self.sixth_2.clicked.connect(lambda: self.button_colour(self.sixth_2, 26))
        self.sixth_3.clicked.connect(lambda: self.button_colour(self.sixth_3, 27))
        self.sixth_4.clicked.connect(lambda: self.button_colour(self.sixth_4, 28))
        self.sixth_5.clicked.connect(lambda: self.button_colour(self.sixth_5, 29))

        # reset the game
        self.reset_game.clicked.connect(lambda: self.reset())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def button_colour(self, button, number):
        # check how many times the button has been clicked
        self.count[number] += 1        
        count = self.count[number]

        # based on the number of clicks cycle through the different colours
        if (count - 2) % 3 == 0:
            button.setStyleSheet("QPushButton""{""background-color : #ffd24d;""}")
        elif count % 3 == 0:
            button.setStyleSheet("QPushButton""{""background-color : None;""}")
        else:
            button.setStyleSheet("QPushButton""{""background-color : #44a670;""}")
    
    def calculate_word(self, box_1, box_2, box_3, box_4, box_5, first_number):
        # declare variables        
        min_score = 99
        party = 0
        same_letter = [0, 0, 0, 0, 0]
        
        # iterate over the previous word to factor in user input
        for i in range(len(self.min_word)):
            # allow multiple of the same letters to be stored in green letters 
            for j in range(len(self.min_word)):
                if (self.count[i + first_number] - 1) % 3 == 0 and self.min_word[i] == self.min_word[j] and i != j and (self.count[j + first_number] - 1) % 3 == 0:
                    same_letter[j] = 1

            # store letters that are in the correct position to ensure they are used in the same place
            if (self.count[i + first_number] - 1) % 3 == 0 and set(self.min_word[i].lower()).intersection(self.green_letter) == set() or same_letter[i] == 1:
                self.green_letter.append(self.min_word[i].lower())
                self.position.append(i)
                # if a letter moves from the yellow list to the green list remove it from the yellow list
                if set(self.min_word[i].lower()).intersection(self.yellow_letter) != set():
                    index = self.yellow_letter.index(self.min_word[i].lower())
                    del self.yellow_letter[index]
                    del self.place[index]
            # store letters that are in the incorrect position to ensure they are used but not in the same place
            elif (self.count[i + first_number] - 2) % 3 == 0:
                self.yellow_letter.append(self.min_word[i].lower())
                self.place.append(i)
            # add letters that are not in the word to the used letters list
            elif self.count[i + first_number] % 3 == 0:
                self.used_letters.append(self.min_word[i].lower())
            
            # keep track of the amount of green tiles, if they are all green play the celebration big
            if (self.count[i + first_number] - 1) % 3 == 0:
                party += 1
                if party == 5:
                    self.label_13.setHidden(False)
                    self.movie.start()

        # iterate over the words to assess their suitability
        for word in self.words:
            standing = ''
            score = 0
            new_word = ''
            allow = ''
            # iterate over each character in order to determine a score for the word
            for letter in word:
                if letter == 'a':
                    score += 1
                elif letter == 'b':
                    score += 3
                elif letter == 'c':
                    score += 3
                elif letter == 'd':
                    score += 2
                elif letter == 'e':
                    score += 1
                elif letter == 'f':
                    score += 4
                elif letter == 'g':
                    score += 2
                elif letter == 'h':
                    score += 4
                elif letter == 'i':
                    score += 1
                elif letter == 'j':
                    score += 8
                elif letter == 'k':
                    score += 5
                elif letter == 'l':
                    score += 1
                elif letter == 'm':
                    score += 3
                elif letter == 'n':
                    score += 1
                elif letter == 'o':
                    score += 1
                elif letter == 'p':
                    score += 3
                elif letter == 'q':
                    score += 10
                elif letter == 'r':
                    score += 1
                elif letter == 's':
                    score += 1
                elif letter == 't':
                    score += 1
                elif letter == 'u':
                    score += 1
                elif letter == 'v':
                    score += 4
                elif letter == 'w':
                    score += 4
                elif letter == 'x':
                    score += 8
                elif letter == 'y':
                    score += 4
                elif letter == 'z':
                    score += 10
                else:
                    print('Error! Word contains non standard character')

            # for the first guess after the start do not guess a word with 2 of the same letter to ensure coverage of more letters (improves chances of winning)
            if first_number == 0:
                if self.double_letter(word) == True:
                    standing = 'illegal'
            
            if len(self.green_letter) != 0:
                # check that the word has green letters in the correct positions, if they aren't then do not use the word
                for i in range(len(self.green_letter)):
                    if self.green_letter[i] != word[self.position[i]]:
                        standing = 'illegal'
                        
                # check if the letter is in the used list and in the green list
                if set(word).intersection(self.used_letters) != set() and set(word).intersection(self.green_letter) != set():
                    new_word = word
                    for i in range(len(self.green_letter)):
                        new_word = new_word.replace(self.green_letter[i], '', 1)
                    for i in range(len(self.yellow_letter)):
                        new_word = new_word.replace(self.yellow_letter[i], '', 1)
                                        
                    if set(new_word).intersection(self.used_letters) != set():
                        standing = 'illegal'
                    else:
                        allow = 'yes'

            if len(self.yellow_letter) != 0:                                
                # check that the word has yellow letters in the correct positions, if they aren't then do not use the word
                for i in range(len(self.yellow_letter)):
                    if self.yellow_letter[i] == word[self.place[i]]:
                        standing = 'illegal'
                                   
                    # if the word does not contain the yellow letters it cannot be used
                    if set(self.yellow_letter[i]).intersection(word) == set():
                        standing = 'illegal'
                        
                # check if the letter is in the used list and in the yellow list
                if set(word).intersection(self.used_letters) != set() and set(word).intersection(self.yellow_letter) != set():
                    # if it is remove the green/yellow letters from the word and check if it still has used letters
                    new_word = word
                    for i in range(len(self.yellow_letter)):
                        new_word = new_word.replace(self.yellow_letter[i], '', 1)
                    for i in range(len(self.green_letter)):
                        new_word = new_word.replace(self.green_letter[i], '', 1)

                    # change standing to illegal if there are used letters, otherwise allow the word                    
                    if set(new_word).intersection(self.used_letters) != set():
                        standing = 'illegal'
                    else:
                        allow = 'yes'

            # if the new word has a lower score and no used letters outside the green/yellow list set it as the new word
            if score <= min_score and (set(word).intersection(self.used_letters) == set() or allow == 'yes') and standing != 'illegal':
                min_score = score
                self.min_word = word.upper()

        # insert the letters of the chosen word into the relevant boxes      
        try:
            box_1.setText(self.min_word[0])
            box_2.setText(self.min_word[1])
            box_3.setText(self.min_word[2])
            box_4.setText(self.min_word[3])
            box_5.setText(self.min_word[4])
        except:
            print('No word in dictionary matches criteria')

    # check if a word has 2 of the same letter in it
    def double_letter(self, word):
        for i in range(len(word)):
            for j in range(len(word)):
                if i != j and word[i] == word[j]:
                    return True
    
    # reset everything for another game to start
    def reset(self):
        self.count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
        self.used_letters = []
        self.green_letter = []
        self.position = []
        self.yellow_letter = []
        self.place = []
        self.min_word = ''
        self.first_1.setText('')
        self.first_2.setText('')
        self.first_3.setText('')
        self.first_4.setText('')
        self.first_5.setText('')
        self.second_1.setText('')
        self.second_2.setText('')
        self.second_3.setText('')
        self.second_4.setText('')
        self.second_5.setText('')
        self.third_1.setText('')
        self.third_2.setText('')
        self.third_3.setText('')
        self.third_4.setText('')
        self.third_5.setText('')
        self.fourth_1.setText('')
        self.fourth_2.setText('')
        self.fourth_3.setText('')
        self.fourth_4.setText('')
        self.fourth_5.setText('')
        self.fifth_1.setText('')
        self.fifth_2.setText('')
        self.fifth_3.setText('')
        self.fifth_4.setText('')
        self.fifth_5.setText('')
        self.sixth_1.setText('')
        self.sixth_2.setText('')
        self.sixth_3.setText('')
        self.sixth_4.setText('')
        self.sixth_5.setText('')
        self.first_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.first_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.first_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.first_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.first_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.second_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.second_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.second_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.second_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.second_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.third_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.third_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.third_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.third_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.third_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fourth_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fourth_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fourth_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fourth_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fourth_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fifth_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fifth_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fifth_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fifth_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.fifth_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.sixth_1.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.sixth_2.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.sixth_3.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.sixth_4.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.sixth_5.setStyleSheet("QPushButton""{""background-color : None;""}")
        self.label_13.setHidden(True)

    # auto generated code for the UI from pyqt5
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Wordle Solver</span></p></body></html>"))
        self.submit_1.setText(_translate("MainWindow", "Submit"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.submit_2.setText(_translate("MainWindow", "Submit"))
        self.submit_3.setText(_translate("MainWindow", "Submit"))
        self.submit_4.setText(_translate("MainWindow", "Submit"))
        self.submit_5.setText(_translate("MainWindow", "Submit"))
        self.submit_6.setText(_translate("MainWindow", "Submit"))
        self.reset_game.setText(_translate("MainWindow", "Reset"))

# run program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

