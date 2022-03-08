# Wordle-Solver
Created by Tyler Safe in 2022

Description:
A solver written in Python code that suggests a 5 letter word based on scrabble score to be entered, using the rules of the Wordle game. This works
on the assumption that the lower scrabble score a letter gives the more common it is and the higher chance of it being in any given word. The program
was created for fun after I had played the Wordle game and was interested in how well a solver would perform as well as how difficult it would be to
write. The solver does work very well, only encountering issues where it is just a guess as to what the word is. For example the solver works out the 
last 4 letters of the word are 'orse' the word could be horse, morse, worse etc. A human would have the same issue though and is one of the limitations
that cannot be fixed. 

Installation:
- Download the zip file titled 'wordle_solver_complete'
- Extract to your preferred location
- Ensure you have Python 3.0 or later installed
- You will need to install the PyQT5 library to run the program, the pip install is here ---> pip install PyQt5
- Run the code in the .py file titled 'wordle_solver', can be from an IDE

How to Use:
The program is very easy to use. Upon launching click the 'Start' button to begin a game, a word will be suggested to enter into your wordle game. 
Enter the word into your game on your device to find out which letters are not used, green (correct location) or yellow (incorrect location). Then
mirror this on the solver by clicking a box once to turn it green, twice to turn it yellow or a third time to turn it back to no colour. Once the
solver reflects the game press the submit button and a new word will be suggested. Repeat until the word is solved. Upon the solver being correct
change all squares green and press submit to make the solver happy and want to celebrate. Pressing the 'Reset' button wipes the current game, 
allowing for a new one to be started. 
