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

documentTypes = [".doc", ".pdf", ".txt"]
imageTypes = [".png"]

window = tkinter.Tk(className="Organize folder")


def find_folder():
    """
    Opens file dialog for the user and asks for a folder.
    When the folder is provided then the script will go through and organize each file in the folder
    """

    folder = tkinter.filedialog.askdirectory()

    if folder != '':
        documents_path = folder + "/Documents/"
        images_path = folder + "/Images/"
        for item in os.scandir(path=folder):

            if item.is_file():
                file_type = item.name[item.name.find(".", item.name.count(".")):].lower()

                if documentTypes.count(file_type) > 0:

                    if not (os.path.exists(documents_path)):
                        os.mkdir(documents_path)
                    shutil.move(item.path, documents_path + "/" + item.name)

                elif imageTypes.count(file_type) > 0:
                    if not (os.path.exists(images_path)) :
                        os.mkdir(images_path)
                    shutil.move(item.path, images_path + "/" + item.name)


button = tkinter.Button(text="Open File", width=50, height=2, command=find_folder)
button.pack()

window.mainloop()
