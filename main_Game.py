from tkinter import *     #This means I can use tkinter

import time   #Allows me to use time and measure how long bullets

import csv  #This allows me to use the library csv

######################################################################################################################################################################################################################################

class BulletsShot():
    
    """Made by Nathaniel Lowis 1st Edit: 17/10/18 Latest Edit:17/10/18
       This will work out how many bullets you have in a game"""
    
######################################################################################################################################################################################################################################    

    def __init__(self):

        """Made by Nathaniel Lowis 1st Edit: 17/9/18  Latest Edit: 17/10/18
           Inputs - None
           Outputs - None
           Sets up the class"""
            
        self.howManyShot = 10  #How many shots the person will have
        
######################################################################################################################################################################################################################################        
        
    def bullets_Sub(self):
        
        """Made by Nathaniel Lowis 1st Edit: 17/9/18  Latest Edit: 17/10/18
           Inputs - amount of bullets left (Integer)
           Outputs - None
           Takes bullets off when you shoot one"""
        
        self.howManyShot = self.howManyShot - 1  #Will take away a bullet when you shoot one
        
######################################################################################################################################################################################################################################       
       
    def bullets_Show(self):
        
        """Made by Nathaniel Lowis 1st Edit: 17/9/18  Latest Edit: 17/10/18
           Inputs - None
           Outputs - How many bullets you have (integer)
           Shows how many bullets you have"""
        
        return self.howManyShot  #Returns how many bullets you have to the main program
    
######################################################################################################################################################################################################################################    
######################################################################################################################################################################################################################################    

class Bullet():
    
    """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 3/10/18
       This is the superclass which will allow me to model how the bullet moves and output it to the screen.  Parts of code has been adapted from:https://stackoverflow.com/questions/25430786/moving-balls-in-tkinter-canvas
       """
    
######################################################################################################################################################################################################################################    
    
    def __init__(self, x1BulletGiven, y1BulletGiven, x2BulletGiven, y2BulletGiven, canvasToUse):
        
        """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 3/10/18
           Inputs - the canvas (tkinter Object), coordinates (Integers)
           Outputs - None
           Sets up the class when intialised"""
        
        self.intialSpeedHori = 50.0  #These will set up the intial speed, acceleration for use in the rest of the code for both the Parabolic bullet and Horizontal Bullet
        self.intialSpeedHoriPara = 50.0
        
        self.finalSpeedHori = 0.0
        self.finalSpeedVertical = 50.0
        self.finalSpeed = 0.0
        
        self.distanceHori = 0.0
        self.distanceVertical = 0.0
        
        self.horizontalAcceleration = 30.0
        self.verticalAccelerationUp = -9.81
        self.verticalAccelerationDown = 9.81
        
        self.x1Bullet = x1BulletGiven                       #This 4 co-ordinates are where each corner should be placed
        self.y1Bullet = y1BulletGiven
        self.x2Bullet = x2BulletGiven
        self.y2Bullet = y2BulletGiven
        
        self.canvasBullet = canvasToUse  #Sets up the code
        
        self.ball = canvasToUse.create_oval(self.x1Bullet, self.y1Bullet, self.x2Bullet, self.y2Bullet, fill="green")  #Outputs to screen
        self.time = 5       #More constants made.
        self.mass = 0.008
        self.energy = 0.0
        
######################################################################################################################################################################################################################################
    
    def delete_Bullet(self):  
        
        """Made by Nathaniel Lowis 1st Edit: 12/9/18  Latest Edit: 12/9/18
           Inputs - The class
           Outputs - Deletes the bullet from the screen
           Deletes the bullet from the screen"""
        
        self.canvasBullet.delete(self.ball)  #Deletes bullet
        
######################################################################################################################################################################################################################################
        
    def energy_In_Bullet(self):
        
        """Made by Nathaniel Lowis 1st Edit: 12/9/18  Latest Edit: 12/9/18
           Inputs - Class
           Outputs - The energy of the bullet (float)
           Works out the amount of energy in the bullet"""
        
        self.energy = .5 * self.mass * ( self.finalSpeed ** 2)   #Uses E = 1/2 mv^2
        ##print(self.energy)    #testing
        
######################################################################################################################################################################################################################################        
        
    def power_At_Point(self, timeTaken):
        
        """Made by Nathaniel Lowis 1st Edit: 12/9/18  Latest Edit: 12/9/18
           Inputs - Time (float), class
           Outputs - The amount of power from the bullet (float)
           Works out the amount of power in the bullet"""
        
        power = self.energy / timeTaken  #Uses p = E/t
        
        ##print(power)   #Testing
        
        return power
    
######################################################################################################################################################################################################################################    
    
    def coord_Bullet(self):  
        
        """Made by Nathaniel Lowis 1st Edit: 31/8/18.  Latest Edit: 12/9/18
           Inputs  - The class
           Outputs - Where the bullet is (Array of floats)
           This will show where the bullet is"""
        
        coordinatesBullet = self.canvasBullet.coords(self.ball)  #This gives the coordinates for the bullet
        return coordinatesBullet  #Returns it to the main program
    
######################################################################################################################################################################################################################################        
######################################################################################################################################################################################################################################
    
class HoriBullet(Bullet):
    
    """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
       This is a subclass of bullet which calculates and output it to the screen."""
    
######################################################################################################################################################################################################################################    
    
    def speed_At_Any_Point(self, distanceGone):    
        
        """Made by Nathaniel Lowis 1st Edit: 12/9/18  Latest Edit: 12/9/18
           Inputs -  Distance Gone (Float), class
           Outputs - The final speed of bullet (Float)
           This works out the final speed of the bullet"""
        
        self.finalSpeedHori = ((self.intialSpeedHori ** 2) + (2 * self.horizontalAcceleration * distanceGone) )** .5   #Uses V^2 = u^2 + (2as)
        ##print(self.FinalSpeed)   #Testing
        
        self.finalSpeed = self.finalSpeedHori  #This means the program can use it later
        
        return self.finalSpeed  #Returns the speed
    
######################################################################################################################################################################################################################################    
    
    def move_Bullet_Hori(self, xMovement):  
        
        """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
           Input - How much to move by (Float)
           Output - Moving on the screen (Tkinter Object)
           This will move the bullet on the screen"""
        
        self.canvasBullet.move(self.ball, xMovement, 0)   #Moves the bullet
        self.canvasBullet.after(100)  #Waits 100 ms until it updates screen
        self.canvasBullet.update()  #Updates the screen
        
######################################################################################################################################################################################################################################        
        
    def distance_To_Work_Out(self):
        
        """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
           Inputs - class
           Outputs - The distance to go (Float)
           This will work out how far the bullet has to go"""
        
        self.distanceHori = (self.intialSpeedHori * self.time) + (.5 * self.horizontalAcceleration *(self.time **2)) #Uses S = ut + 1/2at^2
        return self.distanceHori
    
######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################
    
class ParabolicBullet(Bullet):
    
    """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
       This is a subclass of Bullet which works out the stuff for a parabolic Bullet"""
    
######################################################################################################################################################################################################################################    
    
    def distance_Worker_Up(self):
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
           Inputs - Class
           Outputs - Vertical Distance (Float), Horizontal Distance (Float)
           This will work out how far the bullet will have to move when the bullet moves upwards"""
        
        self.distanceVertical = (-.5 * self.verticalAccelerationUp * (self.time /2)**2)  # Uses S = vt - (1/2)at^2
        self.distanceHori = (self.intialSpeedHoriPara * (self.time /2))  #Uses S = ut
        ##print(self.distanceVertical, self.distanceHori)  #Testing
        return self.distanceVertical, self.distanceHori
    
######################################################################################################################################################################################################################################    
    
    def distance_Worker_Down(self):
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
           Inputs - Class
           Outputs - Vertical Distance (Float), Horizontal Distance (Float)
           This will work out how far the bullet will have to move when the bullet moves downwards"""
        
        self.distanceVertical = (.5 * self.verticalAccelerationDown * (self.time /2)**2)    #Uses S = ut + (1/2)at^2
        self.distanceHori = (self.intialSpeedHoriPara * (self.time / 2))    #Uses S = ut
        ##print(self.distanceVertical, self.distanceHori)  #testing
        return self.distanceVertical, self.distanceHori
    
######################################################################################################################################################################################################################################
    
    def speed_Vert_Up(self, distanceVertUp, timeTakenSoFar):
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
           Inputs - Class, Distance Gone Vertically Up (Float), time (Float)
           Outputs - The final Vertical speed (Float)
           This will work out the final vertical speed of the bullet when the bullet goes upwards"""
        
        self.finalSpeedVertical = (distanceVertUp + (.5 * self.verticalAccelerationUp * (timeTakenSoFar ** 2)))/ timeTakenSoFar  #Uses S = vt - .5at^2
        
        if self.finalSpeedVertical < 0:  #If the speed is worked to be less than 0 it sets the final speed to 0
            self.finalSpeedVertical = 0.0
        
        ##print(self.finalSpeedVertical)  #Testing
        return self.finalSpeedVertical

######################################################################################################################################################################################################################################

    def speed_Vert_Down(self, timeTaken):
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
           Inputs - Class, time (Float)
           Outputs - Final Vertical Speed (Float)
           This will work out the final vertical speed of the bullet when the bullet goes upwards"""
        
        self.finalSpeedVertical = self.verticalAccelerationDown * timeTaken  #Uses v = u + at and u is assumed to be 0
        ##print(self.finalSpeedVertical) #Testing
        return self.finalSpeedVertical  

######################################################################################################################################################################################################################################

    def final_Speed_Parabolic(self):
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 26/9/18
           Inputs - Class
           Outputs - Final Overall Speed (Float)
           This uses vector working to work out the final speed of a parabolic bullet"""
        
        self.finalSpeed = ((self.finalSpeedVertical  **2) + (self.intialSpeedHoriPara **2))**.5  #Uses Pythagorous Theorem to resolve into 1 vector
        ##print(self.finalSpeed)  #Testing
        return self.finalSpeed  

######################################################################################################################################################################################################################################

    def move_Ball_Para_Up(self, yMovement, xMovement):   
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 27/9/18
           Input - yMovement (Float), xMovement (Float)
           Output - Moving on the screen (Tkinter Object)
           Moves the bullet on the screen"""
        
        self.canvasBullet.move(self.ball, xMovement, -yMovement)   #Moves the bullet
        self.canvasBullet.after(100)  #Waits 100 ms until it updates screen
        self.canvasBullet.update()  #Updates the screen
        
######################################################################################################################################################################################################################################        
        
    def move_Ball_Para_Down(self, yMovement2, xMovement2):   
        
        """Made by Nathaniel Lowis 1st Edit: 26/9/18  Latest Edit: 27/9/18
           Input - How much to move by
           Output - Moving on the screen
           Works out how far the bullet has to be moved """
        
        self.canvasBullet.move(self.ball, xMovement2, yMovement2)   #Moves the bullet
        self.canvasBullet.after(100)  #Waits 100 ms until it updates screen
        self.canvasBullet.update()  #Updates the screen

######################################################################################################################################################################################################################################        
######################################################################################################################################################################################################################################
        
class Character():
    
    """Made By Nathaniel Lowis 1st Edit: 25/08/18.  Latest Edit: 17/10/18
       This class will make the people on the screen and will allow the computer/user use the character"""
    
######################################################################################################################################################################################################################################            
    
    def __init__(self, canvasCharacter, x0Given, x1Given, y0Given, y1Given, colour):
        
        """Made By Nathaniel Lowis 1st Edit: 25/08/18.  Latest Edit: 31/08/18
           Inputs - The canvas (tkinter Object), and coordinates (Integers)
           Outputs - Character on the screen
           This will initilise the character meaning it can be used"""
        
        self.characterOnScreen = canvasCharacter.create_rectangle(x0Given, y0Given, x1Given, y1Given, fill= colour)  #Creates the character
        self.canvasForCharacter = canvasCharacter  #Allows programmer to still use the screen

        self.health = 200 #Sets the health for the character
        
######################################################################################################################################################################################################################################                
        
    def health_Left(self):
            
        """Made By Nathaniel Lowis 1st Edit: 17/10/18  Latest Edit: 17/10/18
           Inputs - Class
           Outputs - health (Float)
           This will output the health so the program can use it for scoring"""
            
        return self.health  #Returns the health
        
######################################################################################################################################################################################################################################                
        
    def jump(self):
        
        """Made By Nathaniel Lowis 1st Edit: 25/9/18 Latest Edit: 3/10/18
           Inputs - Class
           Outputs - None
           This will allow the character to jump and it be shown on the screen"""
        
        height = 0  #Sets how high the character is
        
        while height <= 50:  #Whilst the character has not reached the maxiumum height (50)
            
            self.canvasForCharacter.move(self.characterOnScreen, 0, -1)#Moves the character up
            self.canvasForCharacter.update()  #This will update the screen so the user can see it
            self.canvasForCharacter.after(10)  #Waits 10 ms until running the program.  Allows the user to move here I think
            height = height + 1  #Increments height by 1
        
        downHeight = 0  #Sets how high the character  Needed to get the character down
        
        while downHeight <=50:  #Whilst the charcter has not reached the floor (Need to go down 50 pixels)
            
            self.canvasForCharacter.move(self.characterOnScreen, 0, 1)#Moves the character
            self.canvasForCharacter.update()  #This will update the screen so the user can see it
            self.canvasForCharacter.after(10)  #Waits 10ms until it does the anything
            downHeight = downHeight + 1  #Increments downHeight by 1
        
######################################################################################################################################################################################################################################                
        
    def delete_Character(self):
        
        """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
           Input - Character Class
           Outputs - Deletes the character
           Deletes character if they are killed"""
        
        self.canvasForCharacter.delete(self.characterOnScreen)  #Deletes the character
        
######################################################################################################################################################################################################################################                
        
    def lose_Health(self, healthToLose):
        
        """Made by Nathaniel Lowis 1st Edit: 11/9/18  Latest Edit: 12/9/18
           Inputs - The health to lose (Float)
           Outputs - Health left (Float)
           Makes the character lose health"""
        
        self.health = self.health - healthToLose  #Lose health
        return self.health
        
######################################################################################################################################################################################################################################                
    
    def move_Left(self, amount):
        
        """Made By Nathaniel Lowis 1st Edit: 25/08/18.  Latest Edit: 26/9/18
           Inputs - The class
           Outputs - Move the Character left
           This will move the character left by 'amount' pixels"""
        
        self.canvasForCharacter.move(self.characterOnScreen, -amount, 0)#Moves the character
        self.canvasForCharacter.update()  #This will update the screen so the user can see it
    
######################################################################################################################################################################################################################################            
    
    def move_Right(self):
        
        """Made By Nathaniel Lowis 1st Edit: 25/08/18.  Latest Edit: 11/9/18
           Inputs - The class
           Outputs - Move the Character Right
           This will move the character right by 2 pixels"""
        
        self.canvasForCharacter.move(self.characterOnScreen, 2, 0)  #Moves the character
        self.canvasForCharacter.update()  #This will update the screen so the user can see it
        
######################################################################################################################################################################################################################################                
        
    def coord_Player(self):   
        
        """Made by Nathaniel Lowis 1st Edit: 31/8/18.  Latest Edit: 31/8/18
           Inputs  - The character
           Outputs - Where the character is
           This will show where the character is"""
        
        coordinatesPlayer = self.canvasForCharacter.coords(self.characterOnScreen)  #This gives the coordinates for the character
        return coordinatesPlayer #Returns it to the main program
    
######################################################################################################################################################################################################################################            
    
    def fire_Hori_Bullet_Class(self, coordinateInFireBulletHori):
        
        """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
           Inputs - Cordinates of character in an array
           Outputs - Shooting bullet
           This controls the bullet"""
        
        
        bulletShootingHori = HoriBullet(coordinateInFireBulletHori[2], coordinateInFireBulletHori[1], coordinateInFireBulletHori[2] + 5, coordinateInFireBulletHori[1]+5, self.canvasForCharacter)  #Makes an instant of the HoriBullet Class
        fire_Hori_Bullet(bulletShootingHori)   #Controls the bullet
        bulletShootingHori.delete_Bullet()  #These will delete the bullet afterwards
        del(bulletShootingHori)
     
######################################################################################################################################################################################################################################             
     
    def fire_Hori_Bullet_Class_Enemy(self, coordinateInFireBulletHoriEne):
        
        """Made by Nathaniel Lowis 1st Edit: 2/10/18 Latest Edit: 2/10/18
           Inputs - Cordinates of enemy character in an array
           Outputs - Shooting bullet
           This controls the bullet for the enemy"""
        
        
        bulletShootingHoriEne = HoriBullet(coordinateInFireBulletHoriEne[2], coordinateInFireBulletHoriEne[1] + 45, coordinateInFireBulletHoriEne[2] +5 , coordinateInFireBulletHoriEne[1] + 40 , self.canvasForCharacter)  #Makes an instant of the HoriBullet Class
        fire_Hori_Bullet_Ene(bulletShootingHoriEne)   #Controls the bullet
        bulletShootingHoriEne.delete_Bullet()  #These will delete the bullet afterwards
        del(bulletShootingHoriEne)
        
######################################################################################################################################################################################################################################        
    def fire_Para_Bullet_Class(self, coordinateInFireBulletPara):
        
        """Made by Nathaniel Lowis 1st Edit: 27/9/18  Latest Edit: 28/9/18
           Inputs - Cordinates of character in an array
           Outputs - Shooting bullet
           This controls the Parabolic bullet """
        
        
        bulletShootingPara = ParabolicBullet(coordinateInFireBulletPara[2], coordinateInFireBulletPara[1], coordinateInFireBulletPara[2] + 5, coordinateInFireBulletPara[1]+5, self.canvasForCharacter)  #Makes an instant of the ParabolicBullet Class
        fire_Para_Bullet(bulletShootingPara)   #Controls the bullet
        bulletShootingPara.delete_Bullet()  #These will delete the bullet afterwards
        del(bulletShootingPara)
        
######################################################################################################################################################################################################################################        
######################################################################################################################################################################################################################################                  
        
def set_Up():     
    
    """Made by Nathaniel Lowis 1st Edit: 25/8/18 Latest Edit: 25/9/18
       Inputs - None
       Outputs - A working screen with the floor and endpoint and sent to main program
       This sets up the level the game"""
    
    rootSetUp = Tk()    #This makes the screen
    rootSetUp.title("Bullet Game")  #Gives game a name
    rootSetUp.resizable(True, True)    #This means the usre can make it full screen
    canvasSetUp = Canvas(rootSetUp, width = 500, height = 500)  #Sets up the
    canvasSetUp.pack()  #Outputs screen
    floorSetUp = canvasSetUp.create_rectangle(500, 500, 0, 400, fill="grey")  #Sets up the floor
    endPointSetUp = canvasSetUp.create_rectangle(375, 375, 400, 400, fill="red")  #Sets up the endpoint
    heroSetUp = Character(canvasSetUp, 50, 70, 350, 400, "Blue")  #This will make the user's character
    enemySetUp = Character(canvasSetUp, 300, 320, 350 ,400, "Cyan")  #This will make the enemy class
    
    bulletsLeftSetUp = BulletsShot()
    

    
    return rootSetUp, canvasSetUp, floorSetUp, endPointSetUp, heroSetUp, enemySetUp, bulletsLeftSetUp #Sends everything back to main program.

######################################################################################################################################################################################################################################        

def fire_Hori_Bullet_Ene(bulletFiringEne): 
    
    """Made by Nathaniel Lowis 1st Edit: 2/10/18 Latests: 3/10/18
       Inputs - The Class HoriBullet
       Outputs - The bullet moving and interacting with the environment
       This will allow the bullet to interact with the environment for the enemy bullet"""
    
    timer1StartEne = time.time()    #Starts a timer
    distanceToGoEne = bulletFiringEne.distance_To_Work_Out()  #Works out how far the bullet goes
    #print(distanceToGoEne, "Ene Dis")  #testing
    distPer10MilliEne = distanceToGoEne / 50   #Divides the distance by 50 so they are all in equal chunks
    bulletGoneEne = 0  #Creates a variable which works out how far the bullet has gone
    timeDoneHoriBulletEne = 0  #The time for how long the bullet has gone for
    
    while bulletGoneEne != distanceToGoEne and timeDoneHoriBulletEne < 5000:   #Whilst the bullet has not gone as far as it needs to
        
        heroCoordinatesEne = hero.coord_Player()  #Gets hero's coordinates in an array
        #print(heroCoordinatesEne) #Testing
        bulletCoordinatesEne = bulletFiringEne.coord_Bullet()  #Gets the bullets coordinates in an array
        #print(bulletCoordinatesEne) #Testing
        
        #try:  #The program will go down this route when there is an enemy class #Not needed anymore
        #print("TRY") #Testing
        if bulletCoordinatesEne[0] <= heroCoordinatesEne[2] and bulletCoordinatesEne[2] >= heroCoordinatesEne[0] and bulletCoordinatesEne[1] <= heroCoordinatesEne[3]: #If the bullet has hit the hero
            
            #print("HIT") #Testing
            timer1FinishEne = time.time()  #Stops timer
            timer1Ene = timer1FinishEne - timer1StartEne   #Works out length of time the  bullet has gone for
            
            ##print(bulletGone) #testing
            #print(timer1Ene)    #testing
            
            bulletFiringEne.speed_At_Any_Point(bulletGoneEne)   #Works out the speed of the bullet
            bulletFiringEne.energy_In_Bullet()    #Works out the energy of the bullet
            bulletPowerEne = bulletFiringEne.power_At_Point(timer1Ene)   #Works out the power of the bullet
            
            #print(bulletPowerEne, "Power") #testing
            
            bulletGoneEne = distanceToGoEne    #Means the while loop can stop
            hero_Lose_Health(bulletPowerEne) #Makes the hero lose health
            
           
          
        else:  
            
            negativeDistPer10MilliEne = distPer10MilliEne * -1  #This will allow the bullet to move towards the hero
            bulletFiringEne.move_Bullet_Hori(negativeDistPer10MilliEne)   #Moves the ball the amount it needs to
            bulletGoneEne = bulletGoneEne + distPer10MilliEne  #Added to  bulletGone
            timeDoneHoriBulletEne = timeDoneHoriBulletEne + 100

        
##        except:  #This is when there is no enemy     #All not needed anymore
##            
##            print("Except")
##            
##            negativeDistPer10MilliEne = distPer10MilliEne * -1
##            bulletFiringEne.move_ball(negativeDistPer10MilliEne)   #Moves the ball the amount it needs to
##            bulletGoneEne = bulletGoneEne + distPer10MilliEne #Added to BulletGone
##            timeDoneHoriBulletEne = timeDoneHoriBulletEne + 100
                       
######################################################################################################################################################################################################################################                    

def fire_Hori_Bullet(bulletFiring):  
    
    """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 12/9/18
       Inputs - The Class HoriBullet
       Outputs - The bullet moving and interacting with the environment
       This will allow the bullet to interact with the environment"""
    
    timer1Start = time.time()    #Starts a timer
    distanceToGo = bulletFiring.distance_To_Work_Out()  #Works out how far the bullet goes
    #print(distanceToGo, "Distance Hori")  #testing
    distPer10Milli = distanceToGo / 50   #Divides the distance by 50 so they are all in equal chunks
    bulletGone = 0  #Creates a variable which works out how far the bullet has gone
    timeDoneHoriBullet = 0  #How long the bullet has gone for
    
    while bulletGone != distanceToGo and timeDoneHoriBullet < 5000:   #Whilst the bullet has not gone as far as it needs to
            
        enemyCoordinates = enemy.coord_Player()  #Gets enemy's coordinates in an array
        bulletCoordinates = bulletFiring.coord_Bullet()  #Gets the bullets coordinates in an array
        
        try:  #The program will go down this route when there is an enemy class
            
            if bulletCoordinates[0] > enemyCoordinates[0] and bulletCoordinates[1] >= enemyCoordinates[1]:  #If the bullet is past the enemy
                timer1Finish = time.time()  #Stops timer
                timer1 = timer1Finish - timer1Start   #Works out length of time the  bullet has gone for
                
                ##print(bulletGone) #testing
                ##print(timer1)    #testing
                
                bulletFiring.speed_At_Any_Point(bulletGone)   #Works out the speed of the bullet
                bulletFiring.energy_In_Bullet()    #Works out the energy of the bullet
                bulletPower = bulletFiring.power_At_Point(timer1)   #Works out the power of the bullet
                
                #print(bulletPower, "Power") #testing
                
                bulletGone = distanceToGo    #Means the while loop can stop
                enemyHealth = enemy.lose_Health(bulletPower)  #Makes the enemy lose health
                
                #print(enemyHealth, "EnemyHealth")  #testing
                
                if enemyHealth <= 0:  #If the enemy's health is below or equal to 0
                    #CULD PUT THIS IN OWN FUNCTION
                   enemy.delete_Character()  #Deletes the enemy
               
              
            else:  
        
                bulletFiring.move_Bullet_Hori(distPer10Milli)   #Moves the ball the amount it needs to
                bulletGone = bulletGone + distPer10Milli  #Added to  bulletGone
                timeDoneHoriBullet = timeDoneHoriBullet + 100
        
        except:  #This is when there is no enemy
            
            bulletFiring.move_Bullet_Hori(distPer10Milli)   #Moves the bullet
            bulletGone = bulletGone + distPer10Milli #Added to BulletGone
            timeDoneHoriBullet = timeDoneHoriBullet + 100
            
######################################################################################################################################################################################################################################                  

def fire_Para_Bullet(bulletFiring2):  
    
    """Made by Nathaniel Lowis 1st Edit: 27/9/18  Latest Edit: 28/9/18
       Inputs - The Class ParabolicBullet
       Outputs - The bullet moving and interacting with the environment
       This will allow the bullet to interact with the environment"""
    
    
    #This bit is for the bullet moving upwards
    timer2Start = time.time()    #Starts a timer
    distanceToGoUp, distanceLeft = bulletFiring2.distance_Worker_Up()  #Works out how far the bullet goes
    #print(distanceToGoUp, distanceLeft, "Distance Para")  #testing
    distLeft = distanceLeft / 25  #Divides the distance by 25 so they are all in equal chunks to go left
    distPer10MilliUp = distanceToGoUp / 25  #Divides the distance by 25 so they are all in equal chunksto go up
    bulletGoneUp = 0  #Creates a variable which works out how far the bullet has gone
    timeDoneParaBullet = 0  #This will be how long the bullet has moved for
    goDown = True  #This is used to say whether the bullet should go down
    
    while bulletGoneUp != distanceToGoUp and timeDoneParaBullet < 2500:   #Whilst the bullet has not gone as far as it needs to and not gone for long enough
        
        enemyCoordinates = enemy.coord_Player()  #Gets enemy's coordinates in an array
        bulletCoordinates2 = bulletFiring2.coord_Bullet()  #Gets the bullets coordinates in an array
        
        try:  #The program will go down this route when there is an enemy class
            
            if bulletCoordinates2[0] > enemyCoordinates[0] and bulletCoordinates2[1] >= enemyCoordinates[1] -5 and bulletCoordinates2[0] < enemyCoordinates[2]:  #If the bullet is hitting the enemy
                ##print("HIT UP") #Testing
                
                timer2Finish = time.time()  #Stops timer
                timer2 = timer2Finish - timer2Start   #Works out length of time the  bullet has gone for
                ##print("HIT UP", timer2)  #Testing
                
                ##print(bulletGone) #testing
                ##print(timer1)    #testing
                
                bulletFiring2.speed_Vert_Up(bulletGoneUp, timer2)   #Works out the speed of the bullet going upwards
                ##print("Working With Speed") #Testing
                
                bulletFiring2.final_Speed_Parabolic()  #Works out the final speed for the bullet
                ##print("Final Speed") #Testing
                bulletFiring2.energy_In_Bullet()    #Works out the energy of the bullet
                ##print("Energy")  #Testing
                bulletPowerPara = bulletFiring2.power_At_Point(timer2) #Works out the power of the bullet
                ##print("Power") #Testing
                
                #print(bulletPowerPara, "Para") #testing
                
                bulletGoneUp = distanceToGoUp    #Means the while loop can stop
                enemyHealth2 = enemy.lose_Health(bulletPowerPara)  #Makes the enemy lose health
                
                #print(enemyHealth2, "Ene Health")  #testing
                goDown = False  #Means the bullet dows not have to go down
                
                if enemyHealth2 <= 0:  #If the enemy's health is below or equal to 0
                    #CULD PUT THIS IN OWN FUNCTION
                   enemy.delete_Character()  #Deletes the enemy
               
              
            else:  
        
                bulletFiring2.move_Ball_Para_Up(distPer10MilliUp, distLeft)   #Moves the ball the amount it needs to up and left
                bulletGoneUp = bulletGoneUp + distPer10MilliUp  #Added to  bulletGoneUp how far it went
                timeDoneParaBullet = timeDoneParaBullet + 100   #Time is updated
        
        except:  #This is when there is no enemy
            
            bulletFiring2.move_Ball_Para_Up(distPer10MilliUp, distLeft)   #Moves the ball the amount it needs to up and left
            bulletGoneUp = bulletGoneUp + distPer10MilliUp  #Added to  bulletGone how far it went
            timeDoneParaBullet = timeDoneParaBullet + 100    #Time is updated
            
            
            
    if goDown == True:         #Means the bullet can go downwards
        timer3Start = time.time()    #Starts a timer
        distanceToGoDown, distanceLeft2 = bulletFiring2.distance_Worker_Down()  #Works out how far the bullet goes
        #print(distanceToGoDown, distanceLeft2, "Para Dis 2")  #testing
        distLeftToGo = distanceLeft / 25   #Divides the distance by 25 so they are all in equal chunks to go up
        distPer10MilliDown = distanceToGoDown / 25  #Divides the distance by 25 so they are all in equal chunks to go down
        bulletGoneDown = 0  #Creates a variable which works out how far the bullet has gone
        timeDoneParaBullet2 = 0  #Creates a variable for amount of time it has been
        
        while bulletGoneDown != distanceToGoDown and timeDoneParaBullet2 < 2500:   #Whilst the bullet has not gone as far as it needs to and not for long enough
            
            enemyCoordinates2 = enemy.coord_Player()  #Gets enemy's coordinates in an array
            bulletCoordinates3 = bulletFiring2.coord_Bullet()  #Gets the bullets coordinates in an array
            
            try:  #The program will go down this route when there is an enemy class
                
                if bulletCoordinates3[0] > enemyCoordinates2[0] and bulletCoordinates3[1] >= enemyCoordinates2[1] -5 and bulletCoordinates3[0] < enemyCoordinates2[2]:  #If the bullet is hitting the enemy
                    
                    #print("HIT Down") #testing
                    timer3Finish = time.time()  #Stops timer
                    timer3 = timer3Finish - timer3Start   #Works out length of time the  bullet has gone for
                    
                    #print("HIT Down", timer3) #Testing
                
                    
                    ##print(bulletGone) #testing
                    ##print(timer1)    #testing
                    
                    bulletFiring2.speed_Vert_Down(timer3)   #Works out the speed of the bullet going downwards
                    
                    bulletFiring2.final_Speed_Parabolic()  #Works out the final speed of the bullet
                    bulletFiring2.energy_In_Bullet()    #Works out the energy of the bullet
                    bulletPowerPara2 = bulletFiring2.power_At_Point(timer3)   #Works out the power of the bullet
                    
                    #print(bulletPowerPara2, "Power") #testing
                    
                    bulletGoneDown = distanceToGoDown    #Means the while loop can stop
                    enemyHealth3 = enemy.lose_Health(bulletPowerPara2)  #Makes the enemy lose health
                    #print("Health: ", enemyHealth) #Testing
                    
                    if enemyHealth3 <= 0:  #If the enemy's health is below or equal to 0
                        #CULD PUT THIS IN OWN FUNCTION
                       enemy.delete_Character()  #Deletes the enemy
                   
                  
                else:  
            
                    bulletFiring2.move_Ball_Para_Down(distPer10MilliDown, distLeft)   #Moves the ball the amount it needs to left and down
                    bulletGoneDown = bulletGoneDown + distPer10MilliDown #Added to  bulletGoneDown 
                    timeDoneParaBullet2 = timeDoneParaBullet2 + 100  #Updates time
            
            except:  #This is when there is no enemy
                
                bulletFiring2.move_Ball_Para_Down(distPer10MilliDown, distLeft)   #Moves the ball the amount it needs to
                bulletGoneDown = bulletGoneDown + distPer10MilliDown #Added to  bulletGoneDown
                timeDoneParaBullet2 = timeDoneParaBullet2 + 100  #Updates Time

######################################################################################################################################################################################################################################
                
#def key(event):
    
#    """Used as testing """
    
#    print("pressed", repr(event.char))  #TESTING
  
######################################################################################################################################################################################################################################          
  
def enemy_Shooting():
    
    """Made By Nathaniel Lowis 1st Edit: 2/10/18,  Latest Edit: 2/10/18
       Inputs - None
       Outputs - None
       This allows the enemy to shoot"""
     
    characterPosistionForEnemy = enemy.coord_Player() #Gets the coordinates for the enemy's character
    enemy.fire_Hori_Bullet_Class_Enemy(characterPosistionForEnemy)  #Fires bullet
  
######################################################################################################################################################################################################################################          
  
def hero_Touch_Enemy():
    
    """Made By Nathaniel Lowis 1st Edit: 28/9/18, Latest Edit: 3/10/18
       Inputs - None
       Outputs - None
       This will mean the user's charatcer is hurt if it touches the enemy"""
    
    heroCurrentCoordinates = hero.coord_Player()  #Gets the hero's coordinates
    enemyCurrentCoordinates = enemy.coord_Player() #Gets the Enemy's coordinates
    
    try:  #If there is an enemy
        
        if heroCurrentCoordinates[2] >= enemyCurrentCoordinates[0] and heroCurrentCoordinates[3] >= enemyCurrentCoordinates[1]:  #If the hero touches the enemy
            
            hero_Lose_Health(50) #Hero Loses health
            hero.move_Left(20)  #Hero pushed back
            
    except:  #If there is no enemy niothing should happen
        pass
    
######################################################################################################################################################################################################################################        

def scoring(timeDoneIn, levelScore):
    
    """Made By Nathaniel Lowis  1st Edit: 17/10/18 Latest Edit: 18/10/18
       Inputs - the time the level has been done in (Float), the score for the level (integer)
       Outputs - The final Score (Float)"""
    
    healthForHero = hero.health_Left()  #Gets how much health the hero has
    howManyBulletsLeft = bulletsLeft.bullets_Show()  #Gets how many bullets the user has
    finalScore = (1 / timeDoneIn) + (howManyBulletsLeft * 5) + healthForHero + levelScore  #Works outs the score for the level
    
    with open("Scores.csv", mode = "wt", encoding = "utf-8") as addingScores:  #OPens and wipes a csv file which will hold the score which will be added to the database
        
        writingARow = csv.writer(addingScores)  #Allows to write into the csv
        arrayWithScoreIn = [finalScore, "\n"]  #What needs to be entered into the csv
        writingARow.writerow(arrayWithScoreIn)  #Writes in the data to the csv
        
    import adding_To_Database  #Runs the code to add data to a database
    
    
    
    
    return finalScore  #Returns score to the main program

######################################################################################################################################################################################################################################        
        
def hero_Lose_Health(healthToLoseFunction):
    
    """Made by Nathaniel Lowis 1st Edit: 28/9/18, Latest Edit: 17/10/18
       Inputs - Health to lose (Float)
       Outputs - None
       This will take away health if the hero is hit and stop the game if the hero is dead"""
    
    heroHealth = hero.lose_Health(healthToLoseFunction)  #Gets Hero to lose health
    #print(heroHealth, "Health Hero")  #Testing
    
    if heroHealth <= 0:  #If the hero is 'dead' it should delete everything
       # print("DEAD")
        finalTimerEnd2 = time.time()  #Gets the latest time
        frame.destroy()  #Deletes everything

           
        finalTime2 = finalTimerEnd2 - finalTimerStart  #Works out how long it took to complete the level
        #print(finalTimerEnd2, "Time")   #testing
        scoring(finalTime2, 0)  #Calls the function to work out the school
        
######################################################################################################################################################################################################################################                
        
def callback(event):
    
    """Editied from: http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm  Made by Nathaniel Lowis  1st Edit: 25/8/18  1st Edit: 31/8/18
    Inputs - What the user did
    Output- Allows user to move left and right
    Means we can press on the screen and use the buttons"""
      
    frame.focus_set()   #This will mean we can use the left and right button as you have to press the window
    ##print("clicked at", event.x, event.y)  Used as testing
    
######################################################################################################################################################################################################################################            
    
def hero_Move_Left(event):
    
    """Made by Nathaniel Lowis  1st Edit: 31/8/18  1st Edit: 28/9/18
    Inputs - What the user did
    Output- Allows user to move left
    Makes the hero move left and checks if the game has finished"""
    
    #print("pressed 'Left'")  #testing
    hero.move_Left(2)#Calls this method to move character
    hero_Touch_Enemy()  #This will check if you have touched the enemy
    finish_Game()  #Checks to see whether you have finished the game

######################################################################################################################################################################################################################################        

def hero_Move_Right(event):
    
    """Made by Nathaniel Lowis  1st Edit: 31/8/18  1st Edit: 28/9/18
    Inputs - What the user did
    Output- Allows user to move Right
    Makes the hero move Right and checks if the game has finished"""
    
    #print("pressed 'Right'")  #testing
    hero.move_Right() #Calls this method to move character##
    hero_Touch_Enemy()  #Will check if you are touching the enemu
    finish_Game()  #Checks to see if the user has finished the game

######################################################################################################################################################################################################################################        

def hero_Jump(event):
    
    """Made by Nathaniel Lowis  1st Edit: 25/9/18.  Latest Edit: 3/10/18
    Inputs - What the user did
    Output- Allows user to move Jump
    Makes the hero move Right and checks if the game has finished"""
    
    #print("pressed 'Up'")  #testing
    heroCoordinatesJumpFunction = hero.coord_Player()
    if heroCoordinatesJumpFunction[3] != 400:   #This is used to check if the user is touching the floor. If not it will pass
        pass
    else:
        hero.jump() #Calls this method to move character##

######################################################################################################################################################################################################################################        
  
def finish_Game():
    
    """Made by Nathaniel Lowis  1st Edit: 31/8/18  Latest Edit: 17/10/18
       Inputs - Nothing
       Outputs - Checks if game has finished
       This will check if you have passed the ending point and if you have deletes the screen"""
    
    
    ##print("TRYING")  Used for testing
    x0Endpoint = 375  #These are the known coordinates for the endpoint 
    x1Endpoint = 400
    y0Endpoint = 375
    y1Endpoint = 400
    
    characterPosistion = hero.coord_Player()  #Works out where the user's character is
    
    if characterPosistion[2] >= x0Endpoint and characterPosistion[3] >= y0Endpoint and characterPosistion[3] <= y1Endpoint and characterPosistion[2] <= x1Endpoint:   #Checks if the character has passed the endpoint
        
        finalTimerEnd = time.time()   #Gets the latest time
        frame.destroy()  #If they have it will delete all objects on the canvas
        finalTime = finalTimerEnd - finalTimerStart  #Work out how long it took the user to play the level
        #print(finalTime, "time") #testing
        scoring(finalTime, 100)  #Works out the score for the user
       
######################################################################################################################################################################################################################################            

def fire_Bullet(letter):
    
    """Made by Nathaniel Lowis 1st Edit: 10/9/18  Latest Edit: 17/10/18
       Inputs - The q which must (for some reason) be included
       Outputs - None
       This will start the process of firing a Horizontal bullet and get the enemy to shoot first"""
    
    #print("pressed 'q'")  #testing
    bulletLeftHori = bulletsLeft.bullets_Show()  #Checks out how many bullets the user has
    #print(bulletLeftHori)  #testing
    if bulletLeftHori > 0: # If you have bullets it will start the shooting process
        
        bulletsLeft.bullets_Sub()  #Takes away a bullet from your score
        
        try:  #If there is an enemy it should start the shooting process
            
            enemy_Shooting()  #Allows the enemy to shoot
          
        except: #If there is no enemy it should do nothing
            pass
    
        characterPosistion = hero.coord_Player() #Gets the coordinates for the user's character
        hero.fire_Hori_Bullet_Class(characterPosistion)  #Fires bullet
        
######################################################################################################################################################################################################################################                
    
def fire_Bullet_Para(letter):
    
    """Made by Nathaniel Lowis 1st Edit: 27/9/18  Latest Edit: 17/10/18
       Inputs - The w which must (for some reason) be included
       Outputs - None
       This will start the process of firing a Parabolic bullet"""
    
    #print("pressed 'w'")  #testing

    bulletLeftPara = bulletsLeft.bullets_Show()  #Checks to see if you have bullets left
    #print(bulletLeftPara)  #testing
    
    if bulletLeftPara > 0:  #If you do it will start shooting
        
        bulletsLeft.bullets_Sub()  #Takes away a bullet
        
        characterPosistionPara = hero.coord_Player() #Gets the coordinates for the user's character
        hero.fire_Para_Bullet_Class(characterPosistionPara)  #Fires bullet

######################################################################################################################################################################################################################################        

#main
finalTimerStart = time.time()  #Gets time so it can work out how long it took the user

root, frame, floor, endPoint, hero, enemy, bulletsLeft= set_Up()  #Sets up game



frame.bind("<Left>", hero_Move_Left)  #Moves Character left if left button pressed
frame.bind("<Right>", hero_Move_Right)  #Moves Character Right if right button pressed
frame.bind("<Up>", hero_Jump)      #Allows the user to jump
frame.bind("<Button-1>", callback)  #Means user can press screen
frame.bind("<q>", fire_Bullet)     #Allows the user can shoot a horizontal Bullet
frame.bind("<w>", fire_Bullet_Para)   #Allows the user to shoot a parabolic bullet

#frame.bind("<Key>", key) # testing
frame.pack() #Sends it to the screen



frame.mainloop() #Infinte loop used 