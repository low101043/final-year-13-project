import sqlite3  #Imports an external library which will allow me to work with databases

######################################################################################################################################################################################################################################

def create_Table(name):

    """Made By Nathaniel Lowis.  Edited from: https://repl.it/@NathanielLowis/Database-in-python  First Edit: 17/10/18.  Latest Edit: 18/10/18
       Inputs - Name of the filename (String)
       Outputs - None
       This will set up a database"""

    connection = sqlite3.connect(name)  #Connects to a database and allow you to edit it
    cursor = connection.cursor()
    
    cursor.execute('CREATE TABLE Highscores ("UniqueID" integer,"UserName" text, "Score" real)')  #This will make all the columns for the database
    
    connection.commit()  #Saves it and closes the database
    connection.close()
    
######################################################################################################################################################################################################################################    
    
#main
create_Table("highscores.db")  #This creates a database
