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


import tkinter, os
from tkinter import filedialog

documentTypes = [".doc", ".pdf"]
imageTypes = [".png"]

window = tkinter.Tk(className="Organize folder")

def find_folder():
    folder = tkinter.filedialog.askdirectory()
    for item in os.scandir(path=folder):
        if item.is_file():
            file_type = item.name[item.name.find(".", item.name.count(".")):].lower()
            if documentTypes.count(file_type) > 0:
                print("DOC")
            elif imageTypes.count(file_type) > 0:
                print("IMAGE")


button = tkinter.Button(text="Open File", width=25, height=5, command=find_folder)
button.pack()

window.mainloop()
