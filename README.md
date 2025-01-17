# katas

This is a place to keep my katas: whetstones for problem-solving and technical thought.

## Contents

### Kata0001 ![https://img.shields.io/badge/language-python-green.svg](https://img.shields.io/badge/language-python-green.svg)

Implement a function that takes a list of all-caps cardinal directions ("NORTH", "SOUTH", "EAST", "WEST") and simplifies them, cancelling out opposing pairs.

### Kata0002 ![https://img.shields.io/badge/language-python-green.svg](https://img.shields.io/badge/language-python-green.svg)

Given a square matrix, an `x_start_index` and a `y_start_index`, return a 3 * 3 subsquare from the matrix. Matrix dimensions are always minimum 3 * 3. If either start index is too high, give `None` in the out-of-bounds positions.

### Kata0003 ![https://img.shields.io/badge/language-python-green.svg](https://img.shields.io/badge/language-python-green.svg)

Create a `ConnectFourGame` class that keeps track of its state, with the methods:

+ `.get_board()`, returning the current state of the board (initialized as a 7 * 6 matrix filled with `None`)
+ `.get_player()`, returning a string indicating whether the current player is `x` or `o` (where `x` goes first)
+ `.play()`, which takes a column index number as its argument and 'drops' a counter into that column, raising the exception `This column is full` if appropriate, and returning nothing
+ `.check_winner()`, returning `False` if there is not yet any winner, or the winning player if 4 like counters are aligned either horizontally, vertically or diagonally

### Kata0004 ![Bash](https://img.shields.io/badge/language-bash-orange.svg)

From [TLDP](https://tldp.org/LDP/abs/html/writingscripts.html): Write a bash script that reads each line of a target file, then write the line back to stdout with an extra blank line following, effectively double-spacing the file. Check the script gets the necessary command-line argument (a filename), and whether the specified file exists. Modify the script to allow it:

+ to triple-space the target file, and
+ to remove all blank lines from the target file, single-spacing it.

### Kata0005 ![JavaScript](https://img.shields.io/badge/language-javascript-blue) ![MongoDB](https://img.shields.io/badge/-MongoDB-4DB33D?style=flat&logo=mongodb&logoColor=FFFFFF)

Using the MongoDB Atlas training database's `grades` collection, and referring solely to data for class 256, extract a list of students who meet both of the following criteria:

+ has at least one homework score above the class's homework average
+ has at least one homework score at least 25% higher than the average of their own exam and quiz scores

### Kata0006 ![reasoning](https://img.shields.io/badge/-reasoning-AF329B) ![Jupyter Notebook](https://img.shields.io/badge/-jupyter-F37626?logo=jupyter&logoColor=ffffff)

From [CodeKata.com](http://codekata.com/kata/kata03-how-big-how-fast/): Working out answers in your head, estimate storage space used and time taken for a variety of values and operations.

### Kata0007 ![https://img.shields.io/badge/language-python-green.svg](https://img.shields.io/badge/language-python-green.svg) ![pandas](https://img.shields.io/badge/-pandas-150458?logo=pandas&logoColor=ffffff)

From [CodeKata.com](http://codekata.com/kata/kata04-data-munging/): Given the text files `weather.dat` (containing weather data for Morristown, NJ for June 2002) and `football.dat` (containing results from the English Premier Leageue for 2001/2), write a program that outputs the day number with the smallest temperature spread, then a program that outputs the name of the team with the smallest difference in 'for' and 'against' goals. Both files require cleaning. Finally, factor out as much common code as possible.
