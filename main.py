#import os,sys,pygame,copy
from pygame.locals import *

WHEIGHT = 800 #Window Height (px)
WWIDTH = 600 #Window Width (px)
HALF_WWIDTH = int(WWIDTH / 2) #1/2 Width
HALF_WHEIGHT = int(WHEIGHT / 2) #1/2 Height
FPS = 60 #Frames Max: 60 Min: 30

TWIDTH = 50 #Tile Width
THEIGHT = 85 #Tile Height
TFLOORHEIGHT = 45 #Tile Floor Height

CAMSPEED = 5 #px per frame

DECCOUNT = 10 #Percentage of tiles that have a decoration (foilage)

#COLOR DEFS
BLUE = (0,170,255)
WHITE = (255,255,255)
BG = BLUE
TEXT = WHITE

#Self Explanatory
LEFT = 'left'
UP = 'up'  
DOWN = 'down'
RIGHT = 'right'

def main():
	global DISPLAYSURF, FPSCLOCK, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage
	
	#init pygame
	pygame.init()
	FPSCLOCK = pygame.time.Clock()

	#Display.update now called
	DISPLAYSURF = pygame.display.set_mode((WWIDTH,WHEIGHT))
	
	#Set win title
	pygame.display.set_caption('Discordia')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	
	IMAGESDICT = {'player_main' : pygame.image.load('N/A.png'),
				  'wall' : pygame.image.load('N/A.png'),
				  }
				  #etc, I have no images yet

	TILEMAPPING = {'x' : IMAGESDICT['corner'],
				   '*' : IMAGESDICT['wall'],
				   'o' : IMAGESDICT['inside floor'],
				   ' ' : IMAGESDICT['outside floor'],
				   }
	#Skipping for now			   
	OUTSIDECOMAPPING = {}
	
	currentImage = 0
	
	#Skipping For Now
	PLAYERIMAGES = [IMAGESDICT['main']]
	
	startScreen() #Show title until user input is detected
	
	#Read levels from text file
	levels = readLevelFile('Discordia_Lvl1.txt')
	#Remeber - Level # in name does not match with currentLevelIndex increment by 1
	currentLevelIndex = 0
	
	#Main game loop
	
	while True:
		lvlstart = runLevel(levels, currentLevelIndex)
		
		if lvlstart in('solved', 'next'):
			#Proceed to next level
			currentLevelIndex +=1
			if currentLevelIndex >=len(levels):
			#If no more levels go back to first (currentLevelIndex = 0)
				currentLevelIndex = 0
			elif lvlstart == 'back'
				#Previous Level
				currentLevelIndex -= 1
				if currentLevelIndex < 0:
					#If there are no previous levels, go to the last one
					currentLevelIndex = len(levels)-1
				elif lvlstart == 'reset'
					pass #Loop recalled runLevel() to reset
					
def runLevel(levels,levelNum):
	global currentImage
	lObj = levels[levelnum]
	mObj = decorateMap(lObj['mObj'],lObj['startState']['player'])
	gameState = copy.deepcopy(lObj['startState']) #Return a deep copy of x, keep obj's stored in RAM
	mRed = True #Draw Map
	lSurf = BASICFONT.render('Level%s of %s'%(lObj['levelNum']+1, totalNumOfLevels), 1, TEXTCOLOR)
	lRect = lSurf.get_rect()
	lRect.bottomleft = (20, WHEIGHT - 35)
	mWidth = len(mapOBj)* TWIDTH
	mHeight = (len(mapObj[0] - 1)*(TWIDTH - TFLOORHEIGHT) + THEIGHT)
	CAM_X_PAN = abs(HALF_WHEIGHT - int(mHeight/2)) + TWIDTH
	CAM_Y_PAN = abs(HALF_WWIDTH - int(mWidth/2))+THEIGHT
	
	lvlIsComplete = False #Set boolean
	
	#Cam Movement
	camOffsetX = 0
	camOffsetY = 0
	#UI input track
	camUp = False
	camDown = False
	camLeft = False
	camRight = False
	
	while True: #main Loop
		#Var reset
		pMoveTo = None
		keyPressed = False
		
		for event in pygame.event.get(): #Event Handler 
			if event.type == QUIT: #Player clicked close
			gc.collect() #clear RAM
			terminate() #(process terminates)
			
		elif event.type == KEYDOWN:
			#Handle UI 
			keyPressed = True
			if event.key == K_Left: #Left Arrow Not the actual key (K)
				playerMoveTo = LEFT
			elif event.key == K_RIGHT:
				playerMoveTo = RIGHT
			elif event.key == K_UP:
				playerMoveTo = UP
			elif event.key == K_DOWN:
				playerMoveTo = DOWN
			
			
