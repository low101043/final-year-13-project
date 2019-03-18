from tkinter import *   #These commands will import external libraries which are needed for this file .  tkinter - GUI

import sqlite3   #See above . sqlite3 - Database

import csv   #See above csv -holds score from other file

######################################################################################################################################################################################################################################

def checker():
    
    """Made By Nathaniel Lowis First Edit: 17/10/18 Latest Edit: 18/10/18
       Inputs - None
       Outputs - largest ID (Integer)
       This will work out what the latest Unique ID is in the Database"""
    
    connNew = sqlite3.connect("highscores.db") #This will connect to the database and set it up
    curser = connNew.cursor()
    
    largest = 0   #This will be the largest unique ID we have 
    curser.execute('SELECT UniqueID FROM Highscores')   #gets all the Primary keys from the table (Will be in a list of tuples)
    uniqueID = curser.fetchall()  #Lets me use the primary keys
    
    for idRecord in uniqueID:   #Checks every primary key
        if idRecord[0] > largest:  #If the primary key is larger than the largest at the moment 
            largest = idRecord[0]  #We will get largest to equal it
            
    connNew.close()  #Shuts the database
    
    return largest  #Returns it to the main program
        
    

    #print(curser.fetchall())  #Testing
    
######################################################################################################################################################################################################################################    

def username_Entering():
    
    """Made By Nathaniel Lowis.  First Edit: 17/10/18 Latest Edit: 18/10/18
       Inputs - None (Do get score (Float) and username (string) from csv file and gui though)
       Outputs - None
       This will allow the username to be entered and for the score to be taken out of the csv file and added to the database"""
    #finalScore = 5
    
    with open("Scores.csv", mode= "rt", encoding = "utf-8") as readingScores:   #Opens the csv file as a reader
        
        reader = csv.reader(readingScores)  #Sets up a reader
        
        for recordToBeRead in reader: #Checks all records in the csv file (should only be 1)
           
            if recordToBeRead == []:  #If the record is empty (EG the 2nd one) the code should do nothing
                pass
            
            else:   #If the record has something in it 
                finalScoreDatabaseFile = recordToBeRead[0]  #We allow the program to access it so it can be used
    
    username = addingUserName.get()  #This will get the username from the screen
    uniqueIDFunction = checker()  #This will get the largest uniqueID so far in the database
    
    newID = uniqueIDFunction + 1   #This will add 1 to the last UniqueID to make the primary key for the code
        
    labelChange.configure(text = "Your score is being added to the database.  Your score was {}".format(finalScoreDatabaseFile))  #This will output the score and saying everything is being added to the database
    adding_To_Database(newID, username, finalScoreDatabaseFile)  #Adds everything to the database
    
######################################################################################################################################################################################################################################
    
def adding_To_Database(uniqueIDToUse, usernameToAdd, scores):
    
    """Made By Nathaniel Lowis  First Edit: 18/10/18  Latest Edit: 18/10/18
       Inputs - uniqueIDToUse (Integer), usernameToAdd (string), scores (Float)
       Outputs - None
       This will add the user's username and score to the database"""
    
    connectionNew = sqlite3.connect("highscores.db")  #Opens the database and sets it up to be used
    curserNew = connectionNew.cursor()
    
    toAdd = [(uniqueIDToUse, usernameToAdd, scores)]  #This is all the data to be added to the database in a way which the database will allow
    
    curserNew.executemany('INSERT INTO Highscores VALUES (?,?, ?)', toAdd)  #Adds the data into the database.  Done like this so it adds everything using variable names
    connectionNew.commit()  #Commits (Saves) it to the database
    connectionNew.close()  #Closes the database
    
######################################################################################################################################################################################################################################    
    
#main    
databaseScreen = Tk()  #Makes a screen

databaseScreen.title("Bullet Game")  #The name of the screen
databaseScreen.geometry("500x500")  #The size

#menu.wm_iconbitmap("favicon.ico")  #If I wanted to change the image for the file

databaseScreen.configure(background = ("navy"))  #Sets the background

addingUserName = Entry(databaseScreen)  #Adds an entry which the user will enter their username
addingUserName.pack()  #Sends to the screen

labelChange = Label(databaseScreen, text = "Enter username", bg = "green", fg = "white")  #Sets a label which will say what is going on
labelChange.pack()  #Sends to the screen
  
buttonAskingForUserName = Button(databaseScreen, text = "Enter Username!", bg = "green", fg = "white", command = username_Entering)  #The button which will send the username off
buttonAskingForUserName.pack()  #Sends to the screen
  
databaseScreen.mainloop()  #Infinite loop needed to allow GUI to work.
    