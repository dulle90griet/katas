# katas

This is a place to keep my katas: whetstones for problem-solving and technical thought.

## Contents

### Kata0001 ![Python](https://img.shields.io/badge/language-python-green.svg) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

Implement a function that takes a list of all-caps cardinal directions ("NORTH", "SOUTH", "EAST", "WEST") and simplifies them, cancelling out opposing pairs.

### Kata0002 ![Python](https://img.shields.io/badge/language-python-green.svg) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

Given a square matrix, an `x_start_index` and a `y_start_index`, return a 3 * 3 subsquare from the matrix. Matrix dimensions are always minimum 3 * 3. If either start index is too high, give `None` in the out-of-bounds positions.

### Kata0003 ![Python](https://img.shields.io/badge/language-python-green.svg) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

Create a `ConnectFourGame` class that keeps track of its state, with the methods:

+ `.get_board()`, returning the current state of the board (initialized as a 7 * 6 matrix filled with `None`)
+ `.get_player()`, returning a string indicating whether the current player is `x` or `o` (where `x` goes first)
+ `.play()`, which takes a column index number as its argument and 'drops' a counter into that column, raising the exception `This column is full` if appropriate, and returning nothing
+ `.check_winner()`, returning `False` if there is not yet any winner, or the winning player if 4 like counters are aligned either horizontally, vertically or diagonally

### Kata0004 ![Bash](https://img.shields.io/badge/language-bash-orange.svg)

From [TLDP](https://tldp.org/LDP/abs/html/writingscripts.html): Write a bash script that reads each line of a target file, then writes the line back to stdout with an extra blank line following, effectively double-spacing the file. Check the script gets the necessary command-line argument (a filename), and whether the specified file exists. Modify the script to allow it:

+ to triple-space the target file, and
+ to remove all blank lines from the target file, single-spacing it.

### Kata0005 ![JavaScript](https://img.shields.io/badge/language-javascript-blue) ![MongoDB](https://img.shields.io/badge/-MongoDB-4DB33D?style=flat&logo=mongodb&logoColor=FFFFFF)

Using the MongoDB Atlas training database's `grades` collection, and referring solely to data for class 256, extract a list of students who meet both of the following criteria:

+ has at least one homework score above the class's homework average
+ has at least one homework score at least 25% higher than the average of their own exam and quiz scores

### Kata0006 ![reasoning](https://img.shields.io/badge/-reasoning-AF329B)

From [CodeKata.com](http://codekata.com/kata/kata03-how-big-how-fast/): Working out answers in your head, estimate storage space used and time taken for a variety of values and operations.

### Kata0007 ![Python](https://img.shields.io/badge/language-python-green.svg) ![pandas](https://img.shields.io/badge/-pandas-150458?logo=pandas&logoColor=ffffff) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

From [CodeKata.com](http://codekata.com/kata/kata04-data-munging/): Given the text files `weather.dat` (containing weather data for Morristown, NJ for June 2002) and `football.dat` (containing results from the English Premier Leageue for 2001/2), write a program that outputs the day number with the smallest temperature spread, then a program that outputs the name of the team with the smallest difference in 'for' and 'against' goals. Both files require cleaning. Finally, factor out as much common code as possible.

### Kata0008 ![Bash](https://img.shields.io/badge/language-bash-orange.svg)

Write a bash script that transfers a file to a new destination with rsync, appends '_TO_DELETE' to the original filename, and creates a symbolic link to the file's new destination. Show a progress bar, and assume names containing spaces are quoted. Modify the script to: 

+ take any number of filenames for transfer (as arguments $2, $3, $4, etc.),
+ work with file names containing escaped characters, and
+ ensure the symbolic link is created in the file's origin directory, not in the script's working directory.

### Kata 0009 ![Python](https://img.shields.io/badge/language-python-green.svg) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

Given two integer lists sorted in ascending order, `nums1` and `nums2`, and two integers, `m` and `n`, representing the number of elements to be used from the beginnings of `nums1` and `nums2` respectively, merge the two lists into a single list sorted in ascending order. `nums1` is assumed to have a length of `m + n`, and the final sorted list should be produced by modifying `nums1` in place, not by returning a new list.

### Kata 0010 ![Python](https://img.shields.io/badge/language-python-green.svg) ![PyTest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=ffffff)

Shifting pointers: Refresh your memory of CS fundamentals by completing a series of tasks involving iteration over lists or strings.

1. Convert a string number in Roman numerals into an integer.

2. Given a list of integers and an integer `val`, remove all occurrences of `val` from the list **in place**.

3. Given a list of integers and an integer target number, return the indices of two numbers in the list that add up to the target.

4. Given a list of integers sorted in ascending order, remove duplicates **in place** such that ascending order is retained. Return the number of unique elements.
