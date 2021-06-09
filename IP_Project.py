#--Credentials-----------------------------------------------------------------------------------------

## Author: Rahul V Sumbly
## Copyright: Copyright 2020, Instagram-Detailer
## Credits: Rahul V Sumbly
## License: ~None~
## Maintainer: Rahul V Sumbly
## Email: rahulrtg7703@gmail.com
## Status: COMPLETED

#------------------------------------------------------------------------------------------------------

#--MySQL-Connection-------------------------------------------------------------------------------------
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="school_project")
mycursor = mydb.cursor()

#-IMPORTS-----------------------------------------------------------------------------------------------
import datetime

import matplotlib.pyplot as pl

import os
import glob
import shutil
# Shutil is used to remove folder/files with read only attribute

from PIL import ImageTk
import PIL.Image

import time
import sys

import instaloader
from instaloader import Instaloader, Profile

from tkinter import*

#-FONTS-BACKGROUND-COLOUR-TEXT-COLOUR------------------------------------------------------------
high_font_col = "#D85D11"
bg ='#E8E6E0'
fg='#2B2B2B'

#-INITILIZATION-OF-TKINTER-PAGES-----------------------------------------------------------------
root = Tk()
root.title("Instagram Detailer")
root.geometry('800x600')
root.config(bg = bg)

root_main = Tk()
root_main.title("Home Page")
root_main.geometry('800x500')
root_main.config(bg = bg)

root_db = Tk()
root_db.title("Acess Databases")
root_db.geometry('800x500')
root_db.config(bg = bg)

root_credits = Tk()
root_credits.title("Credits")
root_credits.geometry('800x500')
root_credits.config(bg = bg)

root.withdraw()
root_db.withdraw()
root_credits.withdraw()

#-HOME-PAGE----------------------------------------------------------------------------------------------
heading = Label(root_main, text ='Instagram Detailer - Navigation Page',font =('',30), bg = bg, fg = high_font_col)
heading.place(x = 100, y = 10)

user_Button1 = Button(root_main, text ='Login and Search New User', font = (30),command = lambda:login_page(), bg = bg, fg = fg)
user_Button1.place(x = 250, y = 120)

user_Button2 = Button(root_main, text ='Search for user in Data-base', font = (30), command = lambda:user_search(), bg = bg, fg = fg)
user_Button2.place(x = 245, y = 180)

user_Button3 = Button(root_main, text ='Credits', font = (30), command = lambda:credits_page(), bg = bg, fg = fg)
user_Button3.place(x = 330, y = 250)

user_Button4 = Button(root_main, text ='Close', font = (30),command = lambda:exit_program(), bg = bg, fg = fg)
user_Button4.place(x = 335, y = 350)


#--BACK-TO-HOME-----------------------------------------------------------------------------------------
def back_to_home():
    root_main.deiconify()
    root.withdraw()
    root_db.withdraw()
    root_credits.withdraw()

    try:
        user_search.Data_Lable.config(Text = "")
    except:
        print("No Lable found")
    try:
        login_page.Data_Lable.config(text = "")
    except:
        print("No Lable found")


#--EXIT-PROGRAM------------------------------------------------------------------------------------------
def exit_program():
    shutil.rmtree(path = 'C:\\Users\\RAHUL\\Desktop\\IP_Project\\target_profile', ignore_errors= True)
    try:
        os.remove('C:\\Users\\RAHUL\\Desktop\\IP_Project\\profile.ppm')
    except: pass
    
    root.quit()
    sys. exit()


#--CREDITS-PAGE----------------------------------------------------------------------------------------------
def credits_page():
    root_credits.deiconify()
    root_main.withdraw()
    root_db.withdraw()
    root.withdraw()

    heading = Label(root_credits, text ='Credits',font =('',40), bg = bg, fg = high_font_col)
    heading.place(x = 300, y = 10)
    heading = Label(root_credits, text ='Rahul Sumbly',font =('',20), bg = bg, fg = high_font_col)
    heading.place(x = 150, y = 200)
    user_Button = Button(root_credits, text ='Go Home', font = (30),command = lambda:back_to_home() , bg = bg, fg = fg)
    user_Button.place(x = 500, y =200)

    
#--SEARCH-USER-ONLINE-PAGE-----------------------------------------------------------------------------------
def user_search():
    root_db.deiconify()
    root.withdraw()
    root_main.withdraw()
    root_credits.withdraw()

    heading = Label(root_db, text ='Enter the Username you want to check',font =('',20), bg = bg, fg = high_font_col)
    heading.place(x = 80, y = 10)
    check_Button = Button(root_db, text ='Check', font = (30),command = lambda:user_database(username_entry.get()), bg = bg, fg = fg)
    check_Button.place(x = 500, y = 95)
    username_entry = Entry(root_db, font = ('',20), bg =bg, fg = fg)
    username_entry.place(x = 180, y = 100)
    user_search.Data_Lable = Label(root_db, text ='Resulting Data is shown here', font = (30), bg = bg, fg = fg)
    user_search.Data_Lable.place(x= 180, y =200)
    home_Button = Button(root_db, text ='Go Home', font = (30),command = lambda:back_to_home(), bg = bg, fg = fg)
    home_Button.place(x = 600, y = 95)


#--SEARCH-USER-FROM-DATABASE--------------------------------------------------------------------------------
def user_database(a):
    username = a
    query = "SELECT EXISTS(SELECT * from userdata WHERE username = "+"'"+username+"'"+")"
    print(query)
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    for i in result:
        for x in i:
            print(x)
            res = x
    lst_data = []

    if res == 1:
        query_upd = "SELECT * FROM userdata WHERE username = "+"'"+username+"'"
        print(query_upd)
        mycursor.execute(query_upd)
        result = mycursor.fetchall()
        for i in result:
    	    for x in i:
                lst_data.append(x)
                print(x)

        user_search.Data_Lable.config(text ="Username-@"+lst_data[0]+
                                            "\n"+lst_data[1]+" followers"+
                                            "\n"+lst_data[2]+" following"+
                                            "\n"+lst_data[3]+" posts"+
                                            "\n"+lst_data[4]+" total likes"+
                                            "\n"+lst_data[5]+" total comments"+
                                            "\n"+lst_data[6]+" ghost followers"
                                            "\n"+"Date Updated on "+lst_data[7], justify = LEFT)
        user_Button = Button(root_db, text ='Show Graph', font = (30),command = lambda:user_graph(lst_data[1],lst_data[2],lst_data[6]), bg = bg, fg = fg)
        user_Button.place(x = 300, y = 420)
    
    elif res == 0:
        user_search.Data_Lable.config(text ='Username dosent exist in databses', justify = LEFT)


#--LOGIN-PAGE------------------------------------------------------------------------------------
def login_page():
    root.deiconify()
    root_main.withdraw()
    root_db.withdraw()
    root_credits.withdraw()

    #--LOGO---------------------------------------------------------------------------------------
    img_add = "C:\\Users\\RAHUL\\Desktop\\IP_PROJECT\\img_start.jpg"
    img = ImageTk.PhotoImage(file = img_add)
    login_page.image_ = Label(root, image = img)
    login_page.image_.place(x = 100, y = 300)
    login_page.image_.image = img


    #--BASIC-GUI-----------------------------------------------------------------------------------
    heading = Label(root, text ='Instagram Detailer Plus',font =('',30), bg = bg, fg = high_font_col)
    heading.place(x = 100, y = 20)
    
    login_page.Data_Lable = Label(root, text ='This Displays Stats on\n Target Profile', font = (30), bg = bg, fg = fg)
    login_page.Data_Lable.place(x= 300, y =270)

    user_login = Label(root, text ='Your username \n (must follow target)',font =(20), bg = bg, fg = high_font_col)
    user_login.place(x = 100, y = 80)
    user_login_entry = Entry(root, font = (40), bg =bg, fg = fg)
    user_login_entry.place(x = 300, y = 80)

    user_password = Label(root, text ='Your password',font =(20), bg = bg, fg = high_font_col)
    user_password.place(x = 100, y = 140)
    user_password_entry = Entry(root, font = (40), bg =bg, fg = fg, show = "*")
    user_password_entry.place(x = 300, y = 140)

    user_tar = Label(root, text ='Target profile',font =(20), bg = bg, fg = high_font_col)
    user_tar.place(x = 100, y = 200)
    user_tar_entry = Entry(root, font = (40), bg =bg, fg = fg)
    user_tar_entry.place(x = 300, y = 200)

    user_Button = Button(root, text ='Submit', font = (20),command = lambda:ui(user_tar_entry.get(),user_login_entry.get(),user_password_entry.get()), bg = bg, fg = fg)
    user_Button.place(x = 550, y = 75)

    user_Button = Button(root, text ='Go Home', font = (20),command = lambda:back_to_home(), bg = bg, fg = fg)
    user_Button.place(x = 550, y = 135)

    user_Button = Button(root, text ='Close', font = (20),command = lambda:exit_program(), bg = bg, fg = fg)
    user_Button.place(x = 550, y = 195)


#--COLLECTION-OF-DATA-------------------------------------------------------------------------------------------
def ui(a,b,c):
    #-DELETING-PREVIOUS-RECORDS-IF-EXISTS-BEFORE-EXECUTION-TO-AVOID-DUPLICATE-FILE-ERROR
    try:
        shutil.rmtree(path = 'C:\\Users\\RAHUL\\Desktop\\IP_Project\\target_profile')
        os.remove('C:\\Users\\RAHUL\\Desktop\\IP_Project\\profile.ppm')
    except: pass
    
    username = a
    username_login = b
    password = c

    print(username_login)
    print("--------------------------")
    print(username)

    #--INSTAGRAM-LIKES-AND-COMMENTS-AND-FOLLOWERS-AND-FOLLOWING---------------------------------------------------
    L = instaloader.Instaloader()
    try:
        L.login(username_login, password)
    except:
        login_page.Data_Lable.config(text = "Wrong Login Details", justify = LEFT)

    PROFILE = username

    profile = instaloader.Profile.from_username(L.context, PROFILE)

    #-DOWNLOAD-PROFILE-PIC-------------------------------------------------------------------------------------
    L.download_profile(username, profile_pic_only=TRUE)
    os.rename('C:\\Users\\RAHUL\\Desktop\\IP_Project\\{}'.format(username) , 'C:\\Users\\RAHUL\\Desktop\\IP_Project\\target_profile')
    
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0

    #-GETTING-LIKES-AND-COMMENS-FROM-EACH-POST----------------------------------------------------------------
    for post in profile.get_posts():
        total_num_posts = total_num_posts + 1
        total_num_likes += post.likes 
        total_num_comments += post.comments
    
    no_likes = str(total_num_likes)
    comments = str(total_num_comments)
    no_posts = str(total_num_posts)

    #-FOLLOWERS-AND-FOLLOWEES--------------------------------------------------------------------------------
    print("Fetching followees of profile {}.".format(profile.username))
    followees = set(profile.get_followees())
    total_num_following = str(len(followees))
    print(len(followees))

    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())
    total_num_followers = str(len(followers))
    print(len(followers))

    #--GHOST-FOLLOWERS----------------------------------------------------------------------------------------
    likes = set()
    print("Fetching likes of all posts of profile {}.".format(profile.username))
    for post in profile.get_posts():
        print(post)
        likes = likes | set(post.get_likes())
        print(likes)

    ghosts = followers - likes
    num_ghost = 0

    for ghost in ghosts:
        num_ghost = num_ghost + 1
    print("Total no of Ghost followers are: ",num_ghost)

    ghost_num_str = str(num_ghost)

    #--PRINTING-RESULTS-----------------------------------------------------------------------------------------
    login_page.Data_Lable.config(text = "@" + username + "\n"
                             "\n" + total_num_followers + ' Followers' + 
                             "\n" + total_num_following + ' Following' +
                             "\n" + no_posts + ' Posts' +
                             "\n" + no_likes + " total likes" +
                             "\n" + comments + " total comments" +
                             "\n" + ghost_num_str + " ghost followers" ,justify = LEFT)

#--Adding-Graph-Button-----------------------------------------------------------------------------------------
    user_Button = Button(root, text ='Show Graph', font = (30),command = lambda:user_graph(total_num_followers,total_num_following,ghost_num_str), bg = bg, fg = fg)
    user_Button.place(x = 420, y = 510)

#--Adding-Saving-Profile-Button--------------------------------------------------------------------------------
    user_Button = Button(root, text ='Save Result', font = (30),command = lambda:save_profile(username,total_num_followers,total_num_following,no_posts,no_likes,comments,ghost_num_str), bg = bg, fg = fg)
    user_Button.place(x = 250, y = 510)


#--ADDING-AND-DISPLAY-IMG-TO-GUI-------------------------------------------------------------------------------
    files = glob.glob('C:\\Users\\RAHUL\\Desktop\\IP_Project\\target_profile\\*.jpg')
    for f in files:
        image_path = f
    print(image_path)
    
    temp = open(image_path,"rb")
    image = PIL.Image.open(temp)
    image = image.resize((200, 200), PIL.Image.ANTIALIAS) #---# The (250, 250) is (height, width)
    image.save("profile.ppm", "ppm") #------------------------#Saving in a simple format for Tkinter
    photo = PhotoImage(file = "profile.ppm") #----------------#Opening file in Tkinter
    login_page.image_.config(image = photo) #-----------------#Set lable
    login_page.image_.image = photo #-------------------------#Set photo to display


#--DISPLAY-GRAPH----------------------------------------------------------------------------------------------
def user_graph(a,b,c):
    followers = int(a.replace(",",""))
    following = int(b.replace(",",""))
    ghost_followers = int(c.replace(",",""))
    print(followers,following,ghost_followers)
    active_followers = followers - ghost_followers

    # Data to plot-1
    labels1 = 'Active Followers', 'Ghost Followers'
    sizes1 = [active_followers, ghost_followers]
    colors1 = ['gold', 'lightcoral']
    explode1 = (0.1, 0)  # explode 1st slice

    # Data to plot-2
    labels2 = 'Following', 'Followers'
    sizes2 = [following, followers]
    colors2 = ['yellowgreen', 'lightskyblue']
    explode2 = (0.1, 0)  # explode 1st slice

    # create a figure with two subplots
    fig, (ax1, ax2) = pl.subplots(1, 2)

    # plot each pie chart in a separate subplot
    ax1.pie(sizes1, explode=explode1, labels=labels1, colors=colors1,autopct='%1.1f%%', shadow=True, startangle=180)
    ax2.pie(sizes2, explode=explode2, labels=labels2, colors=colors2,autopct='%1.1f%%', shadow=True, startangle=180)

    ax1.legend(labels=labels1,loc="lower right")
    ax2.legend(labels=labels2,loc="lower left")
    pl.show()


#--SAVING/UPDATING-USER-PROFILE-------------------------------------------------------------------------------
def save_profile(a,b,c,d,e,f,g):
    now = datetime.datetime.now()
    time_saved = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    print(time_saved)
    #-print(now.year, now.month, now.day, now.hour, now.minute, now.second) # 2021 5 6 8 53 40

    username = a
    print(a)
    followers = b
    following = c
    posts = d
    likes = e
    comments = f
    ghost = g

    query = "SELECT EXISTS(SELECT * from userdata WHERE username = "+"'"+username+"'"+")"
    print(query)
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    for i in result:
        for x in i:
            print(x)
            res = x
    if res == 1:
        query_upd = "UPDATE userdata SET Followers = " + "'" +b+ "'" + ",Following = " + "'" +c+ "'" + ",Posts = " + "'" +d+ "'" + ",Total_Likes = " + "'" +e+ "'" + ",Total_Comments = " + "'" +f+ "'" + ",Ghost_Followers = " + "'" +g+ "'" + ",Date_Saved = " + "'" +time_saved+ "'" + " WHERE username = " + "'" +username+ "'"
        # '+' is concat operator
        print(query_upd)
        mycursor.execute(query_upd)
        mydb.commit()
    elif res == 0:
        query_insert = "INSERT INTO userdata VALUES("+"'"+username+"',"+"'"+followers+"',"+"'"+following+"',"+"'"+posts+"',"+"'"+likes+"',"+"'"+comments+"',"+"'"+ghost+"',"+"'"+time_saved+"'"+")"
        # '+' is concat operator
        print(query_insert)
        mycursor.execute(query_insert)
        mydb.commit()

root_main.mainloop()
