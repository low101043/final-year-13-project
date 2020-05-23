import sqlite3   #Imports all the libraries needed for this file  

from tkinter import *  #Imports everything from the library tkinter

######################################################################################################################################################################################################################################

def display_Database():
    
    """Made By Nathaniel Lowis  Edited from: https://repl.it/@NathanielLowis/Database-in-python  1st Edit: 18/10/18.  Latest Edit: 18/10/18
       Inputs - None
       Outputs - A sorted table of highscores (list of tuples)
       Gets data from database and sorts it and sends it to the main program"""
    
    connectionDisplay = sqlite3.connect("highscores.db")  #Connects to the database and sets it up to be accessed
    cursorDisplay = connectionDisplay.cursor()
    
    cursorDisplay.execute('SELECT * FROM Highscores')  #This will get all records from the database
    table = cursorDisplay.fetchall()  #Allows the program to access it
    
    sortedTable = quick_Sort(table)  #This will sort out the database
    
    
    
    connectionDisplay.close()  #Closes the database
    return(sortedTable)  #Returns the sorted database to the main program

######################################################################################################################################################################################################################################
    
def quick_Sort(dataArray):
    
    """Made By Nathaniel Lowis  Edited from: https://repl.it/@NathanielLowis/Quick-Sort  First Edit: 18/10/18  Latest Edit: 18/10/18
       Inputs - dataArray (List of tuples)
       Outputs - dataArray (List of tuples)
       Sorts the data out on order of the scores."""

    #print("running quick sort\n")
    if len(dataArray) == 1 or len(dataArray) == 0:                                       # base case for the recursive call
        return dataArray
    else:
        pivot = dataArray[0][2]           # using first value as the pivot value
        i = 0
        
        for j in range(len(dataArray)-1):                                                           # rearranging values around  pivot
            if dataArray[j+1][2] > pivot:
                dataArray[j+1],dataArray[i+1] = dataArray[i+1], dataArray[j+1]
                i = i + 1
        dataArray[0],dataArray[i] = dataArray[i],dataArray[0]
        
        #print("dataArray sorted either side of pivot", dataArray,"pivot", pivot)
        
        first_part = quick_Sort(dataArray[:i])                                                    # recursive calls on either side of pivot
        second_part = quick_Sort(dataArray[i+1:])
        first_part.append(dataArray[i])                                                             # put pivot in correct position
        
        #print("first part",first_part, "second part", second_part,"dataArray", dataArray)
        return first_part + second_part
    
###################################################################################################################################################################################################################################### 

def make_Text():
    
    """Made By Nathaniel Lowis 1st Edit: 18/10/18  Latest Edit: 18/10/18
       Inputs - None
       Outputs - Text to display (String)
       This creates the table needed to be displayed"""
    
    tableToDisplay = display_Database()  #Gets the database table

    tableDisplay = "HighScores \n Place, UniqueID, Username, Score \n"  #What the user will see
    place = 0  #The posistion in the table#

    for recordToDisplay in tableToDisplay:  #Takes each record in the array
    
        place = place + 1  #Increments place to the correct position
        placeString = str(place)  #Turns it into a string
        
        recordToDisplayStr = str(recordToDisplay) #Turns the tuple into a string so it can be added to the final string
    
        tableDisplay = tableDisplay, placeString,  recordToDisplayStr + "\n"  #Adds all the data to the main table so all the scores will be on it
        
    return tableDisplay
        
######################################################################################################################################################################################################################################         

#main   
databaseShowScreen = Tk()  #Makes Window
databaseShowScreen.title("Bullet Game")  #Names Window
databaseShowScreen.geometry("500x500")  #The size of the window

#window.wm_iconbitmap("favicon.ico")
databaseShowScreen.configure(background = ("navy"))  #The background colour

displayTable = make_Text()  #Makes the table to be displayed
    
labelWithTable = Label(databaseShowScreen, text = displayTable, bg = "green", fg = "white")  #Adds the label with the scores on it
labelWithTable.pack()  #Packs label to screen

databaseShowScreen.mainloop()  #Infinite loop