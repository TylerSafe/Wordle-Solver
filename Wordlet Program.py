from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 141, 41))
        self.label.setObjectName("label")
        self.first_1 = QtWidgets.QPushButton(self.centralwidget)
        self.first_1.setGeometry(QtCore.QRect(200, 100, 51, 51))
        self.first_1.setText("")
        self.first_1.setObjectName("first_1")
        self.first_2 = QtWidgets.QPushButton(self.centralwidget)
        self.first_2.setGeometry(QtCore.QRect(270, 100, 51, 51))
        self.first_2.setText("")
        self.first_2.setObjectName("first_2")
        self.first_3 = QtWidgets.QPushButton(self.centralwidget)
        self.first_3.setGeometry(QtCore.QRect(340, 100, 51, 51))
        self.first_3.setText("")
        self.first_3.setObjectName("first_3")
        self.first_4 = QtWidgets.QPushButton(self.centralwidget)
        self.first_4.setGeometry(QtCore.QRect(410, 100, 51, 51))
        self.first_4.setText("")
        self.first_4.setObjectName("first_4")
        self.first_5 = QtWidgets.QPushButton(self.centralwidget)
        self.first_5.setGeometry(QtCore.QRect(480, 100, 51, 51))
        self.first_5.setText("")
        self.first_5.setObjectName("first_5")
        self.submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_1.setGeometry(QtCore.QRect(560, 110, 81, 31))
        self.submit_1.setObjectName("submit_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.counter = ButtonClicks()
        
        self.submit_1.clicked.connect(lambda: self.calculate_word())
        
        self.first_1.clicked.connect(lambda: self.button_colour(self.first_1, 0))
        self.first_2.clicked.connect(lambda: self.button_colour(self.first_2, 1))
        self.first_3.clicked.connect(lambda: self.button_colour(self.first_3, 2))
        self.first_4.clicked.connect(lambda: self.button_colour(self.first_4, 3))
        self.first_5.clicked.connect(lambda: self.button_colour(self.first_5, 4))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def button_colour(self, button, number):

        count = self.counter.button_counter(number)

        if (count - 2) % 3 == 0:
            button.setStyleSheet("QPushButton""{""background-color : #ffd24d;""}")
        elif count % 3 == 0:
            button.setStyleSheet("QPushButton""{""background-color : None;""}")
        else:
            button.setStyleSheet("QPushButton""{""background-color : #44a670;""}")

    def calculate_word(self):
        
        min_word = ''
        min_score = 99

        f = open('words.txt', 'r')
        words = f.read().split()

        for word in words:
            score = 0
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

            if score <= min_score:
                min_score = score
                min_word = word
        print('word:', min_word, '   score:', min_score)

        return min_word
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Wordlet Solver</span></p></body></html>"))
        self.submit_1.setText(_translate("MainWindow", "Submit"))


class ButtonClicks:
    def __init__(self):
        # class variables
        self.count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
    
    def button_counter(self, number):            
        self.count[number] += 1
        
        return self.count[number]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

