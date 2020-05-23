# Main Game

from tkinter import *     #This means I can use tkinter
#import gamePrototype4

######################################################################################################################################################################################################################################

def instructions():
    
    """Made By Nathaniel Lowis.  1st Edit: 17/10/18.  Latest Edit: 17/10/18
       Inputs - None
       Outputs - None
       Displays the instructions for how to play the game"""
    
    instructionScreen = Tk()   #Makes a window
    instructionScreen.title("Bullet Game")  #Name of the window
    instructionScreen.geometry("500x500")  #Size of the window

    #menu.wm_iconbitmap("favicon.ico")
    instructionScreen.configure(background = ("navy"))  #Background of the window

    instructionsToDo= Label(instructionScreen, text = "To play the game click on the screen.  Controls (Do not have caps lock on) \n q: Fires a horizontal Bullet.  Powerful however the enemy will shoot \n w: Fires a Parabolic Bullet.  Not so powerful \n Aim: Get to the red block as fast as you can using the least amount of bullets possible and having the most health at the end. \nCyan Block - Enemy\nDark Blue Block - You", bg = "grey", fg = "black")  #This will output all the instructions onto the window so the user can see how to play the game
    instructionsToDo.pack()  #Sends the label to the screen
    
######################################################################################################################################################################################################################################

def play_Game():
    
    """Made By Nathaniel Lowis 1st Edit: 17/10/18  Latest Edit: 17/10/18
       Inputs - None
       Outputs - None
       Plays the game"""
    
    import main_Game  #Goes to file named gamePrototype4 and runs it.  This will run the game
    #exec(open("gamePrototype4.py").read())  #Testing
    
######################################################################################################################################################################################################################################    
    
def database_To_Display():
    
    """Made By Nathaniel Lowis 1st Edit: 18/10/18  Latest Edit: 18/10/18
       Inputs - None
       Outputs - None
       Will go to the file which ouputs the leaderboard"""
    
    import displaying_Database  #Goes to file called displaying_Database and runs the code

######################################################################################################################################################################################################################################

#main
window = Tk()  #Makes a window for the GUI

window.title("Bullet Game") #Names the window
window.geometry("500x500")  #The size of the window

#window.wm_iconbitmap("favicon.ico")
window.configure(background = ("navy"))  #Sets the background colour


labelWelcome =Label(window, text = "Bullet Shot", bg = "green", fg = "white")  #This is the welcome label saying the name of the game (Bullet Shot)
labelWelcome.pack()  #Sends it to the main screen


buttonInstructions = Button(window, text = "Instructions", bg = "green", fg = "white", command = instructions )  #This is the button to Go to the instructions
buttonInstructions.pack()  #Sends button to window

buttonGame = Button(window, text = "Game", bg = "green", fg = "white", command = play_Game)  #This is the button to play the game
buttonGame.pack()  #Sends button to the screen

buttonLeaderboard = Button(window, text = "Leaderboard", bg = "green", fg = "white", command = database_To_Display)  #This is the button to go to the leaderboard
buttonLeaderboard.pack()  #Sends button to the screen

window.mainloop()  #Infinte loop.

