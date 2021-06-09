# INSTAGRAM-DETAILER

## Jump to [Documentation](#documentation)

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

![](Documentation%20Images/userdatatable.jpg)

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

## Jump to a section:
* [MySQL Database Connection](#documentation)
* [Font, Background and Text Colour](#documentation)
* [Initilization of Tkinter Pages](#documentation)
* [Login and Search Page](#documentation)
* [Search Result Page](#documentation)
* [Show Graph Page](#documentation)
* [Save Profile (Code)](#documentation)
* [Search Database Page](#documentation)
* [Search Database Result](#documentation)
* ["Go Home" Button (Code)](#documentation)
* ["Close" Button (Code)](#documentation)

## MySQL Database Connection:
![](Documentation%20Images/codemysqllogin.jpg)

## Font, Background and Text Colour:
![](Documentation%20Images/codefonts.jpg)

## Initilization of Tkinter Pages:
![](Documentation%20Images/codetkinit.jpg)

## Home Page:
![](Documentation%20Images/HomePage.jpg)

## Home Page (Code):
![](Documentation%20Images/codehomepage.jpg)

## Login and Search Page:
![](Documentation%20Images/loginpage.jpg)

## Login and Search Page (Code):
![](Documentation%20Images/codeloginpage1.jpg)
![](Documentation%20Images/codeloginpage2.jpg)

## Search Result Page:
![](Documentation%20Images/afterlogin.jpg)

## Search Result (Code):
![](Documentation%20Images/codesearchresult1.jpg)
![](Documentation%20Images/codesearchresult2.jpg)
![](Documentation%20Images/codesearchresult3.jpg)
![](Documentation%20Images/codesearchresult4.jpg)

## Show Graph Page:
![](Documentation%20Images/profileGraph.jpg)

## Graph (Code):
![](Documentation%20Images/codeshowgraph.jpg)

## Save Profile (Code):
![](Documentation%20Images/codesaveprofile1.jpg)
![](Documentation%20Images/codesaveprofile2.jpg)

## Search Database Page:
![](Documentation%20Images/codesearchdatabase1.jpg)

## Search Database Result:
![](Documentation%20Images/databaseresult.jpg)

## Search Database Result (Code):
![](Documentation%20Images/codesearchdatabase2.jpg)
![](Documentation%20Images/codesearchdatabase3.jpg)

## "Go Home" Button (Code):
![](Documentation%20Images/codebacktohome.jpg)

## "Close" Button (Code):
![](Documentation%20Images/codeexitprogram.jpg)
