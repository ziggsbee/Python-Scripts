# -----------------------------------------------------------------------------
# MIT License

# Copyright (c) 2020 nwporsch

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import filedialog

window = tkinter.Tk(className="Sum Of ASCII Values")
listOfLines = []
listOfSums = []


def sumofascii(line):
    """
    When provided the line of a file the sum of every ASCII value in the line is added to the listOfSums
    :param line:
    """
    index = 0
    sum = 0
    for c in line:
        if index < 10:
            sum = sum + ord(c)
            index += 1

    listOfSums.append(sum)


def read_in_file(f):
    """
    When provided a file the function will read in the data into the listOfLines variable
    :return:
    """
    index = 0
    line = f.readline()[0:999]
    while line:
        listOfLines.append(line)
        line = f.readline()[0:999]
        index += 1

    f.close()


def find_file():
    """
    Opens file dialog for the user and asks for a file.
    When the file is provided then the script will sum up each line in the file
    """

    # loops until the user provides a file
    while True:
        file = tkinter.filedialog.askopenfile()
        if file != '' and file is not None:
            break

    read_in_file(file)

    for line in listOfLines:
        sumofascii(line)

    index = 0

    # loops through the sum of ASCII characters and returns the difference from the sum before the current sum
    while index is not len(listOfSums) - 1:
        print(index, "-", index + 1, ": ", listOfSums[index] - listOfSums[index + 1])
        index += 1


button = tkinter.Button(text="Open File", width=50, height=2, command=find_file)
button.pack()

window.mainloop()
