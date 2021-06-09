# INSTAGRAM-DETAILER

# Note:
* IP_project.py is the source code 
* img_start.jpg is necessary to execute the code and should be in the same directory as code
* All **File paths** and **MySQL** login deatils in code must be changed accordingly to your system
* A data-base with the following [structure](#structure-of-database) must be created before executing the program
* All necessary [imports](#imports) must be installed before executing the program

*Documentation Images folder has no use in execution of code and is only used for README.md file*

## Made using:
* Pyhton 3.7
* GUI- Tkinter
* Backend/Database- MySQL


## Structure of Database:

### Table name: userdata

Column Name | Type | Size
------------|------|--------
Username | Varchar | 40
Following	|Varchar | 20
Followers	| Varchar	| 20
Following	| Varchar	| 20
Posts	| Varchar	| 20
Total_Likes	| Varchar	| 20
Total_Comments | Varchar | 20
Ghost_Followers	| Varchar | 20
Date_Saved | Varchar | 20

## Imports:
* import datetime
* import matplotlib.pyplot as pl
* import sys
* import os
* import glob
* import shutil
* from PIL import ImageTk
* import PIL.Image
* import instaloader
* from instaloader import Instaloader, Profile
* from tkinter import*

# Documentation:
