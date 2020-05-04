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
import os
import shutil
from tkinter import filedialog

window = tkinter.Tk(className="File Summarizer")


def summarize():
    """
    When given the data in a file the method will read the data and provide a summary of the data
    :return: a summary of the file
    """

    # TODO: Add the abliity to summarize a file


def read_in_file():
    """
    When provided a file the function will read in the data then provide the data to summarize so the program
    can summarize the file
    :return:
    """

    # TODO: Add the ability to read in files


def find_file():
    """
    Opens file dialog for the user and asks for a file.
    When the folder is provided then the script will go through and organize each file in the folder
    """

    # loops until the user provides a file
    while True:
        file = tkinter.filedialog.askopenfile()
        print(file)
        if file != '' and file is not None:
            break
        # TODO: Add other conditions such as only allowing certain file types

        read_in_file()
        summarize()


button = tkinter.Button(text="Open File", width=50, height=2, command=find_file)
button.pack()

window.mainloop()
