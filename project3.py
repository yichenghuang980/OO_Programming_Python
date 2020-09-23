from graphics import *
from graphics import color_rgb
from time import sleep
import string
from random import *
import re
import secrets

# project3.py
# Cody Tempel,Wilson Huang
# This is a demonstration of basic Graphics module functions
# Full documentation of the Graphics module can be found in
# the Zelle Python textbook Ch. 4 (2nd and 3rd edition) and at:
# http://www.math.uci.edu/icamp/computing/python/zellegraphics.pdf
#
# This program is a game where the user has to complete a maze in
#   the least amount of moves by avoiding tripwires.  It keeps track
#   of players names, moves, and scores.  The home screen displays the
#   top scores and enables the user to start new games while the field
#   window is used for gameplay.

def gamePanel():

    #initialize necessary variables
    clickCnt = 0
    check = 0
    startCheck = 0
    endGame = 0
    inputScore = 0
    fail = 0

    #create game panel graphics window with light grey background
    win = GraphWin("Game Panel", 300, 200)
    win.setBackground(color_rgb(211,211,211))

    #draw title border line
    b = Rectangle(Point(0,0),Point(300,40))
    b.setOutline("black")
    b.setFill("white")
    b.draw(win)

    #draw Title
    t = Text(b.getCenter(), "Pete-A-Maze")
    t.setSize(24)
    t.draw(win)

    #draw top scores panel
    ts = Rectangle(Point(50,50), Point(250,160))
    ts.setOutline("black")
    ts.setFill("white")
    ts.draw(win)

    #display title of top scores
    titleTopScore = Text(Point(150,60), "TOP SCORES")
    divider = Text(Point(150,75), "**********")
    divider.setSize(18)
    titleTopScore.draw(win)
    divider.draw(win)

    #draw exit button
    e = Rectangle(Point(265,170),Point(300, 200))
    e.setOutline("black")
    e.setFill(color_rgb(255, 0, 0))
    e.draw(win)
    et = Text(e.getCenter(), 'EXIT')
    et.setSize(14)
    et.draw(win)

    #draw new player button
    r = Rectangle(Point(100,170),Point(200, 200))
    r.setOutline("black")
    r.setFill(color_rgb(0, 255, 0))
    r.draw(win)
    rt = Text(r.getCenter(), 'NEW PLAYER')
    rt.setSize(14)
    rt.draw(win)

    # draw the chance button
    c = Rectangle(Point(230,60),Point(300,100))
    c.setOutline("black")
    c.setFill("green")
    ct = Text(c.getCenter(), 'CHANCE')
    ct.setSize(10)

    #display the top 4 scores
    spaceFromTitle = 12
    name = scoresIn()
    name1 = name[0].replace(",","\t")
    name2 = name[1].replace(",","\t")
    name3 = name[2].replace(",","\t")
    name4 = name[3].replace(",","\t")
    score1 = Text(Point(150,80 + spaceFromTitle), name1)
    score2 = Text(Point(150,92 + spaceFromTitle), name2)
    score3 = Text(Point(150,104 + spaceFromTitle), name3)
    score4 = Text(Point(150,116 + spaceFromTitle), name4)
    score1.setSize(12)
    score2.setSize(12)
    score3.setSize(12)
    score4.setSize(12)
    score1.draw(win)
    score2.draw(win)
    score3.draw(win)
    score4.draw(win)

    #check for exit button
    while(check != 1):
        
        #get clicked point
        clickPoint = win.getMouse()
        x = clickPoint.x
        y = clickPoint.y

        #check if exit button clicked and close window
        if((x >= 250) and (x <= 300)):
            if((y >= 170) and (y <= 200)):
                clickCnt += 1
                x = clickPoint.x
                y = clickPoint.y
                check = 1

        #check if new player button clicked and close window
        if((x >= 100 ) and (x <= 200)):
            if((y >= 170) and (y <= 200)):
                clickCnt += 1
                x = clickPoint.x
                y = clickPoint.y
                check = 0

                #check if new player button was pressed
                if(startCheck != 1):

                    #rewrite new player button to say start
                    #set check var to start button state
                    rt.undraw()
                    rt = Text(r.getCenter(), 'START!')
                    rt.setSize(14)
                    rt.draw(win)
                    startCheck = 1

                    #erase the title, score panel, title score panel,
                    #divider, and all 4 top scores
                    ts.undraw()
                    titleTopScore.undraw()
                    divider.undraw()
                    score1.undraw()
                    score2.undraw()
                    score3.undraw()
                    score4.undraw()

                    #display label for entry box
                    playerName = Text(Point(80,60), "Player Name:")
                    playerName.draw(win)

                    #draw entry box for user input
                    nameEntry = Entry(Point(180,60),15)
                    nameEntry.setFill("white")
                    nameEntry.draw(win)

                #otherwise start button is pressed
                else:

                    #get the text from the entry box
                    inputName = nameEntry.getText()

                    #check if user entered information in entry box
                    if(inputName != ""):

                        #draw the reset button on the game panel
                        rb = Rectangle(Point(0,170),Point(50,200))
                        rb.setOutline("black")
                        rb.setFill(color_rgb(255, 255, 0))
                        rb.draw(win)
                        rbt = Text(rb.getCenter(), 'RESET')
                        rbt.setSize(14)
                        rbt.draw(win)

                        #erase the entry box 
                        nameEntry.undraw()

                        #display the name the user entered
                        savedName = Text(Point(150,60),inputName)
                        savedName.draw(win)
                        c.draw(win)
                        ct.draw(win)

                        #display the score 
                        score = Text(Point(98,100),"Score:")
                        score.draw(win)
                        savedScore = Text(Point(130,100),inputScore)
                        savedScore.draw(win)

                        #create the field window and return
                        #its objects
                        gameWin, pete, gridList, bummer, circ1, circ2, startTime = field()

                        #create and display the sensors in the
                        #field window and return their locations
                        sensorList = sensors(gridList, gameWin)

                        #initialize variables to move Pete object
                        colsIndex = 0
                        rowsIndex = 0

                        #loop while the field game has not ended
                        while(endGame != 1):

                            #animate pete and return necessary objects
                            colsIndex, rowsIndex, peteLocList, inputScore, savedScore, fail = animatePete(circ1, circ2, colsIndex, rowsIndex, win, gameWin, pete, gridList, bummer, sensorList, inputScore, savedScore, win, fail)                                    

                            #update score
                            savedScore.undraw()
                            savedScore = Text(Point(130,100),inputScore)
                            savedScore.draw(win)
                        
                            #get pete objects x and y coords
                            peteX1 = pete.getP1().getX()
                            peteX2 = pete.getP2().getX()
                            peteY1 = pete.getP1().getY()
                            peteY2 = pete.getP2().getY()

                            #get the coords of the red rectangle at the end
                            #of the maze
                            lastRectX1 = gridList[-1].getP1().getX()
                            lastRectX2 = gridList[-1].getP2().getX()
                            lastRectY1 = gridList[-1].getP1().getY()
                            lastRectY2 = gridList[-1].getP2().getY()                                                      

                            #check if pete is at the red rectangle 
                            if((peteX1 > lastRectX1) and (peteX2 < lastRectX2)):
                                if((peteY1 > lastRectY1) and (peteY2 < lastRectY2)):

                                    # undraw chance and text
                                    c.undraw()
                                    ct.undraw()
                                    
                                    # calculate the total amount of time to finish the game
                                    spend = time.time()-startTime

                                    # if it is within 20 sec
                                    if spend<20:
                                        
                                        #set the var to exit field loop
                                        endGame = 1

                                        #display final message on field window
                                        finalMsg = Text(Point(200,200), "Finished, Click to Close")
                                        finalMsg.draw(gameWin)

                                        # generate a list of different fill colors
                                        colorList = ["red","blue","yellow","orange","green","pink","purple"]

                                        # define a while loop to set fill for celebration
                                        while True:

                                            # loop through the list to set fill
                                            for i in gridList:
                                                i.setFill(secrets.choice(colorList))
                                            celebration = gameWin.checkMouse()

                                            # #wait for last mouse click
                                            if celebration!=None:

                                                #update top_scores.txt file with new scores
                                                scoresOut(inputScore, inputName)

                                                #close field window
                                                gameWin.close()
                                                win.close()
                                                main()
                                                break

                                    # if the time is over 20 sec   
                                    if spend>20:

                                        # display text to ask user to player again
                                        ending = Text(Point(200,200),"Sorry! You need to spend less than 20s to be recorded!")
                                        ending.draw(gameWin)
                                        timeSpent = Text(Point(200,250),"Your have spent,"+str(round(spend,2)))
                                        timeSpent.draw(gameWin)

                                        # wait for 3 seconds
                                        sleep(3)

                                        # close the game and graph window
                                        gameWin.close()
                                        win.close()
                                        main()

        #check if reset button clicked and close window
        if((x >= 0 ) and (x <= 50)):
            if((y >= 170) and (y <= 200)):

                #reset the score
                inputScore = 0
                
                
    #close game panel graphics window 
    win.close()

#define field function to create field for pete to move
#in the maze
def field():

    #initialize necessary variables
    gridList = []
    randomNums = []
    start = time.time()
    bummerList = []

    #create field graphics window with white background
    gameWin = GraphWin("The Field", 400, 400)
    gameWin.setBackground("white")

    #constantly loop to create black circles
    while(True):

        #create a list of random numbers from 20 to 400
        #in increments of 40
        for i in range(20,380,40):
            randomNums.append(i)

        #save a random number from the random number list
        randC1x = sample(randomNums,1)
        randC1y = sample(randomNums,1)
        randC2x = sample(randomNums,1)
        randC2y = sample(randomNums,1)

        #check if each random x and y coords do not equal
        if((randC1x != randC2x) and (randC1y != randC2y)):

            #check that the random x and y coords are not at the first rectangle
            if((randC1x != 20 and randC1y != 20) and (randC2x != 20 and randC2y != 20)):

                #create and draw the first black circle
                circ1 = Circle(Point(randC1x[0],randC1y[0]),5)
                circ1.setFill('black')
                circ1.draw(gameWin)

                #create and draw the second black circle
                circ2 = Circle(Point(randC2x[0],randC2y[0]),5)
                circ2.setFill('black')
                circ2.draw(gameWin)

                #break out of the loop
                break

    #create 40x40 rectangles with light grey outlines
    #save each one to grid list
    for i in range(0,400,40):
        for j in range(0,400,40):
            point1 = Point(i,j)
            point2 = Point(i+40,j+40)
            grid = Rectangle(point1,point2)
            grid.setOutline(color_rgb(211,211,211))
            grid.draw(gameWin)
            gridList.append(grid)

    #set the 1st rectangle to green and last to red
    gridList[0].setFill(color_rgb(0,255,0))
    gridList[-1].setFill(color_rgb(255,0,0))

    #draw Pete, center in top left rectangle, and color gold
    pete = Rectangle(Point(0,0),Point(36,36))
    dx = (gridList[0].getP2().getX() - pete.getP2().getX()) / 2
    dy = (gridList[0].getP2().getX() - pete.getP2().getX()) / 2
    pete.move(dx, dy)
    pete.setFill("gold")
    pete.draw(gameWin)

    # randomly select three grids in gridList as Bummers
    while len(bummerList)<3:
        bummer = secrets.choice(gridList[1:99]).getCenter()

        # check if the choice is already a bummer
        if bummer not in bummerList:

            # check if the choice is already a warp zone
            if (str(bummer)!=str(circ1.getCenter()) and str(bummer)!=str(circ2.getCenter())):

                # append it into bummerList if not
                bummerList.append(str(bummer))

    #return field objects
    return gameWin, pete, gridList, bummerList, circ1, circ2, start

#define animatePete function to move pete in the maze
def animatePete(circ1, circ2, colsIndex, rowsIndex, windowName, gameWin, pete, gridList, bummersList, sensorList, inputScore, savedScore, win, failIndex):

    #initialize necessary variables
    upperAlpha = string.ascii_uppercase
    lowerAlpha = string.ascii_lowercase
    cols = []
    rows = []
    peteLocList = ""
    checkForSensor = 0
    possibility = ["No attendence today!","Partner is ill!","Mom is calling!"]
    i = 0

    #create list of uppercase alphanumeric vals
    for i in upperAlpha:
        for j in range(10):
            cols.append(i+str(j))

    #create list of lowercase alphanumeric vals
    for k in lowerAlpha:
        for l in range(10):
            rows.append(k+str(l))

    #wait for mouse click in the field and get the
    #x and y coords of the click and pete
    mouseClick = gameWin.getMouse()
    mouseX = mouseClick.getX()
    mouseY = mouseClick.getY()
    peteX1 = pete.getP1().getX()
    peteX2 = pete.getP2().getX()
    peteY1 = pete.getP1().getY()
    peteY2 = pete.getP2().getY()

    #check if click is in the same column
    if((peteX1 <= mouseX) and (peteX2 >= mouseX)):

        #loop through the difference between the click and
        #pete in increments of 40 (size of rects)
        for i in range(0,int(mouseY) - int(peteY2),40):

            #get x and y coords of pete
            peteX1 = pete.getP1().getX()
            peteX2 = pete.getP2().getX()
            peteY1 = pete.getP1().getY()
            peteY2 = pete.getP2().getY()

            #check if click is below pete and move pete down
            if(peteY2 < mouseY):

                #erase pete and redraw pete by increments of 40
                pete.undraw()
                pete.move(0,40)
                pete.draw(gameWin)
                center = pete.getCenter()

                #create list of the columns that pete crosses 
                colsIndex += 1
                rowsIndex += 10
                crossCols = cols[colsIndex]
                crossRows = rows[rowsIndex]
                peteLocList = crossCols

                #check if pete crossed a sensor and update score
                #accordingly and set check var for sensor
                if(peteLocList in sensorList):
                    inputScore += 3
                    checkForSensor = 1

                #check if sensor is not crossed and update score
                #accordingly
                if(checkForSensor != 1):
                    inputScore += 1

                #otherwise reset check var
                else:
                    checkForSensor = 0

                #check if pete moves into a Hoosier Bummer
                if str(center) in bummersList:
                    failIndex += 1

                    # if it is the first time
                    if failIndex==1:

                        # add 20 points to the total score
                        inputScore += 20

                        # display the first alert text
                        alert = Text(Point(200,200),"You’ve hit a Hidden Hoosier Bummer!")
                        alert.draw(gameWin)

                        # after 3 seconds, undraw the alert
                        sleep(3)
                        alert.undraw()
                        
                    # if it is the second time
                    if failIndex==2:

                        # display the alert for two seconds
                        alert = Text(Point(200,200),"That’s two Hoosier Bummers. Game Over")
                        alert.draw(gameWin)
                        sleep(2)

                        # close the win and field window
                        gameWin.close()
                        win.close()
               
                

            #delay for 250ms
            sleep(.25)

        #loop through the difference between the click and
        #pete in increments of 40 (size of rects)
        for j in range(0, int(peteY1) - int(mouseY),40):

            #check if click is below pete and move pete up
            if(peteY1 > mouseY):

                #erase pete and redraw pete by increments of -40
                pete.undraw()
                pete.move(0,-40)
                pete.draw(gameWin)
                center = pete.getCenter()

                #create list of the columns that pete crosses 
                rowsIndex -= 10
                crossCols = cols[colsIndex]
                crossRows = rows[rowsIndex]
                colsIndex -= 1
                peteLocList = crossCols

                #check if pete crossed a sensor and update score
                #accordingly and set check var for sensor
                if(peteLocList in sensorList):
                    inputScore += 3
                    checkForSensor = 1

                #check if sensor is not crossed and update score
                #accordingly     
                if(checkForSensor != 1):
                    inputScore += 1

                #otherwise reset check var
                else:
                    checkForSensor = 0

                #check if pete moves into a Hoosier Bummer
                if str(center) in bummersList:
                    failIndex += 1

                    # if it is the first time
                    if failIndex==1:

                        # add 20 points to the total score
                        inputScore += 20

                        # display the first alert text
                        alert = Text(Point(200,200),"You’ve hit a Hidden Hoosier Bummer!")
                        alert.draw(gameWin)

                        # after 3 seconds, undraw the alert
                        sleep(3)
                        alert.undraw()
                        
                    # if it is the second time
                    if failIndex==2:

                        # display the alert for two seconds
                        alert = Text(Point(200,200),"That’s two Hoosier Bummers. Game Over")
                        alert.draw(gameWin)
                        sleep(2)

                        # close the win and field window
                        gameWin.close()
                        win.close()
               
            #delay for 250ms
            sleep(.25)

    #check if click is in the same row
    elif((peteY1 <= mouseY) and (peteY2 >= mouseY)):

        #loop through the difference between the click and
        #pete in increments of 40 (size of rects)
        for i in range(0,int(mouseX) - int(peteX2),40):

            #get x and y coords of pete
            peteX1 = pete.getP1().getX()
            peteX2 = pete.getP2().getX()
            peteY1 = pete.getP1().getY()
            peteY2 = pete.getP2().getY()

            #check if click is to the right of pete and move pete right
            if(peteX2 < mouseX):

                #erase pete and redraw pete by increments of 40
                pete.undraw()
                pete.move(40,0)
                pete.draw(gameWin)
                center = pete.getCenter()

                #create list of the columns that pete crosses 
                colsIndex += 10
                rowsIndex += 1
                crossCols = cols[colsIndex]
                crossRows = rows[rowsIndex]
                peteLocList = crossRows

                #check if pete crossed a sensor and update score
                #accordingly and set check var for sensor
                if(peteLocList in sensorList):
                    inputScore += 3
                    checkForSensor = 1

                #check if sensor is not crossed and update score
                #accordingly    
                if(checkForSensor != 1):
                    inputScore += 1

                #otherwise reset check var 
                else:
                    checkForSensor = 0

                #check if pete moves into a Hoosier Bummer
                if str(center) in bummersList:
                    failIndex += 1

                    # if it is the first time
                    if failIndex==1:

                        # add 20 points to the total score
                        inputScore += 20

                        # display the first alert text
                        alert = Text(Point(200,200),"You’ve hit a Hidden Hoosier Bummer!")
                        alert.draw(gameWin)

                        # after 3 seconds, undraw the alert
                        sleep(3)
                        alert.undraw()
                        
                    # if it is the second time
                    if failIndex==2:

                        # display the alert for two seconds
                        alert = Text(Point(200,200),"That’s two Hoosier Bummers. Game Over")
                        alert.draw(gameWin)
                        sleep(2)

                        # close the win and field window
                        gameWin.close()
                        win.close()
               
            #delay for 250ms
            sleep(.25)

        #loop through the difference between the click and
        #pete in increments of 40 (size of rects)
        for j in range(0,int(peteX1) - int(mouseX),40):
            
            #check if click is to the left of pete and move pete left
            if(peteX1 > mouseX):

                #erase pete and redraw pete by increments of 40
                pete.undraw()
                pete.move(-40,0)
                pete.draw(gameWin)
                center = pete.getCenter()

                #create list of the columns that pete crosses 
                colsIndex -= 10
                rowsIndex -= 1
                crossCols = cols[colsIndex]
                crossRows = rows[rowsIndex]
                peteLocList = crossRows

                #check if pete crossed a sensor and update score
                #accordingly and set check var for sensor
                if(peteLocList in sensorList):
                    inputScore += 3
                    checkForSensor = 1

                #check if sensor is not crossed and update score
                #accordingly   
                if(checkForSensor != 1):
                    inputScore += 1

                #otherwise reset check var   
                else:
                    checkForSensor = 0

                #check if pete moves into a Hoosier Bummer
                if str(center) in bummersList:
                    failIndex += 1

                    # if it is the first time
                    if failIndex==1:

                        # add 20 points to the total score
                        inputScore += 20

                        # display the first alert text
                        alert = Text(Point(200,200),"You’ve hit a Hidden Hoosier Bummer!")
                        alert.draw(gameWin)

                        # after 3 seconds, undraw the alert
                        sleep(3)
                        alert.undraw()
                        
                    # if it is the second time
                    if failIndex==2:

                        # display the alert for two seconds
                        alert = Text(Point(200,200),"That’s two Hoosier Bummers. Game Over")
                        alert.draw(gameWin)
                        sleep(2)

                        # close the win and field window
                        gameWin.close()
                        win.close()
               
    #check if the click is up and to the right
    elif((peteX2 <= mouseX) and (peteY2 >= mouseY)):

        #initialize variables
        dy = -40
        dx = 40
        colsIndex += 11
        rowsIndex -= 11
        
        #move diagonal
        colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore = diagonal(dx,dy,pete,mouseX,mouseY,gameWin,colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore,bummersList,failIndex)

    #check if the click is up and to the left
    elif((peteX1 >= mouseX) and (peteY1 >= mouseY)):

        #initialize variables
        dy = -40
        dx = -40
        colsIndex -= 11
        rowsIndex -= 11
        
        #move diagonal
        colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore = diagonal(dx,dy,pete,mouseX,mouseY,gameWin,colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore,bummersList,failIndex)
        
    #check if the click is down and to the right
    elif((peteX2 <= mouseX) and (peteY1 <= mouseY)):

        #initialize variables
        dy = 40
        dx = 40
        colsIndex += 11
        rowsIndex += 11

        #move diagonal
        colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore = diagonal(dx,dy,pete,mouseX,mouseY,gameWin,colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore,bummersList,failIndex)

    #check if the click is down and to the left
    elif((peteX1 >= mouseX) and (peteY1 <= mouseY)):

        #initialize variables
        dy = 40
        dx = -40
        colsIndex -= 11
        rowsIndex += 11

        #move diagonal
        colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore = diagonal(dx,dy,pete,mouseX,mouseY,gameWin,colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore,bummersList,failIndex)

    #get center point coords for pete and warp circles
    px = pete.getCenter().getX()
    py = pete.getCenter().getY()
    c1x = circ1.getCenter().getX()
    c1y = circ1.getCenter().getY()
    c2x = circ2.getCenter().getX()
    c2y = circ2.getCenter().getY()

    #check if pete is on the first warp circle
    if(px == c1x and py == c1y):

        #continuously loop
        while True:

            #get pete and cricle1 and circle2 center coords
            px = pete.getCenter().getX()
            py = pete.getCenter().getY()
            c1x = circ1.getCenter().getX()
            c1y = circ1.getCenter().getY()
            c2x = circ2.getCenter().getX()
            c2y = circ2.getCenter().getY()

            #check if pete is to the left and move left
            if(px > c2x):
                dx = -40
                dy = 0
                colsIndex -= 10
                rowsIndex -= 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is to the right and move right
            if(px < c2x):
                dx = 40
                dy = 0
                colsIndex += 10
                rowsIndex += 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is to the up and move up
            if(py > c2y):
                dx = 0
                dy = -40
                rowsIndex -=10
                colsIndex -= 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)                

            #check if pete is to the down and move down
            if(py < c2y):
                dx = 0
                dy = 40
                colsIndex += 1
                rowsIndex += 10
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is at the other circle and draw pete and exit loop
            if(px == c2x and py == c2y):
                pete.draw(gameWin)
                break

    #check if pete is on the second warp circle   
    elif(px == c2x and py == c2y):

        #continuously loop
        while True:

            #get pete and cricle1 and circle2 center coords
            px = pete.getCenter().getX()
            py = pete.getCenter().getY()
            c1x = circ1.getCenter().getX()
            c1y = circ1.getCenter().getY()
            c2x = circ2.getCenter().getX()
            c2y = circ2.getCenter().getY()

            #check if pete is to the left and move left
            if(px > c1x):
                dx = -40
                dy = 0
                colsIndex -= 10
                rowsIndex -= 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is to the right and move right
            if(px < c1x):
                dx = 40
                dy = 0
                colsIndex += 10
                rowsIndex += 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is to the up and move up
            if(py > c1y):
                dx = 0
                dy = -40
                rowsIndex -=10
                colsIndex -= 1
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)                

            #check if pete is to the down and move down
            if(py < c1y):
                dx = 0
                dy = 40
                colsIndex += 1
                rowsIndex += 10
                gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList = movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList)

            #check if pete is at the other circle and draw pete and exit loop
            if(px == c1x and py == c1y):
                pete.draw(gameWin)
                break

    # check if there is a click in the game panel
    panelClick = windowName.checkMouse()
    if panelClick!=None:
        xPanel = panelClick.getX()
        yPanel = panelClick.getY()

        # if reset button is clicked
        if xPanel<50 and yPanel>160:

            # move pete back to its starting position
            pete.undraw()
            pete = Rectangle(Point(2,2),Point(38,38))
            pete.setFill("yellow")
            pete.draw(gameWin)

            # clear the score
            inputScore = 0

        # if exit button is clicked
        if xPanel>250 and yPanel>160:

            # close the game panel
            gameWin.close()
    
            # close the field panel
            windowName.close()
            

        # if chance button is clicked
        if (xPanel>230 and 60<yPanel<100):
            
            # randomly select a situation
            text = secrets.choice(possibility)

            # if chosing the first outcome
            if text==possibility[0]:
                for i in range(1,99):
                    gridList[i].setFill("yellow")
                condition1 = Text(pete.getCenter(),text)
                condition1.draw(gameWin)

                # sleep for 2 sec
                sleep(2)
                condition1.undraw()
                for i in range(1,99):
                    gridList[i].setFill("white")

                # reduce 10 points
                inputScore = inputScore-10

            # if choosing the second outcome
            if text==possibility[1]:
                for i in range(1,99):
                    gridList[i].setFill("blue")
                condition2 = Text(pete.getCenter(),text)
                condition2.draw(gameWin)

                # sleep for 2 sec
                sleep(2)
                condition2.undraw()
                for i in range(1,99):
                    gridList[i].setFill("white")

                # plus 3 points
                inputScore = inputScore+3

            # if choosing the third outcome
            if text==possibility[2]:
                for i in range(1,99):
                    gridList[i].setFill("red")
                condition3 = Text(pete.getCenter(),text)
                condition3.draw(gameWin)

                # sleep for 2 sec
                sleep(2)
                condition3.undraw()
                for i in range(1,99):
                    gridList[i].setFill("white")

                # plus 5 points
                inputScore += 5
            
    # check pete position again
    peteX1 = pete.getP1().getX()
    peteX2 = pete.getP2().getX()
    peteY1 = pete.getP1().getY()
    peteY2 = pete.getP2().getY()
    
    #return pete location and score
    return colsIndex, rowsIndex, peteLocList, inputScore, savedScore, failIndex

#define move function to move pete through portal
def movePete(gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList):
                
    #erase pete and redraw pete by increments of 40
    pete.undraw()
    pete.move(dx,dy)

    #create list of the columns that pete crosses 
    crossCols = cols[colsIndex]
    peteLocList = crossCols

    #create list of the rows that pete crosses
    crossRows = rows[rowsIndex]
    peteLocList = crossRows

    #return necessary pete information
    return gameWin,dx,dy,cols,rows,pete,colsIndex,rowsIndex,peteLocList

#define diagonal function to move pete diagonally
def diagonal(dx,dy,pete,mouseX,mouseY,gameWin,colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore,bummersList,failIndex):

    #get x and y coords of pete
    peteX1 = pete.getP1().getX()
    peteX2 = pete.getP2().getX()
    peteY1 = pete.getP1().getY()
    peteY2 = pete.getP2().getY()

    if(not((peteY1 <= mouseY) and (peteY2 >= mouseY))):
        if(not((peteX1 <= mouseX) and (peteX2 >= mouseX))):

            #create list of the columns that pete crosses 
            crossCols = cols[colsIndex-10]
            peteLocList = crossCols

            #check if pete crossed a sensor and update score
            #accordingly and set check var for sensor
            if(peteLocList in sensorList):
                inputScore += 3
                checkForSensor = 1

            crossRows = rows[rowsIndex-10]
            peteLocList = crossRows

            #check if pete crossed a sensor and update score
            #accordingly and set check var for sensor
            if(peteLocList in sensorList):
                inputScore += 3
                checkForSensor = 1

            #erase pete and redraw pete by increments of 40
            pete.undraw()
            pete.move(0,dy)
            pete.move(dx,0)
            pete.draw(gameWin)
            center = pete.getCenter()

            #get x coords of pete
            peteY1 = pete.getP1().getY()
            peteY2 = pete.getP2().getY()
            peteX1 = pete.getP1().getX()
            peteX2 = pete.getP2().getX()
            
            #delay for 250ms
            sleep(.25)

            #create list of the columns that pete crosses 
            crossCols = cols[colsIndex]
            peteLocList = crossCols

            #check if pete crossed a sensor and update score
            #accordingly and set check var for sensor
            if(peteLocList in sensorList):
                inputScore += 3
                checkForSensor = 1

            crossRows = rows[rowsIndex]
            peteLocList = crossRows
            
            #check if pete crossed a sensor and update score
            #accordingly and set check var for sensor
            if(peteLocList in sensorList):
                inputScore += 3
                checkForSensor = 1

            #check if sensor is not crossed and update score
            #accordingly     
            if(checkForSensor != 1):
                inputScore += 1

            #otherwise reset check var
            else:
                checkForSensor = 0

            #check if pete moves into a Hoosier Bummer
            if str(center) in bummersList:
                failIndex += 1

                # if it is the first time
                if failIndex==1:

                    # add 20 points to the total score
                    inputScore += 20

                    # display the first alert text
                    alert = Text(Point(200,200),"You’ve hit a Hidden Hoosier Bummer!")
                    alert.draw(gameWin)

                    # after 3 seconds, undraw the alert
                    sleep(3)
                    alert.undraw()
                        
                # if it is the second time
                if failIndex==2:

                    # display the alert for two seconds
                    alert = Text(Point(200,200),"That’s two Hoosier Bummers. Game Over")
                    alert.draw(gameWin)
                    sleep(2)

                    # close the win and field window
                    gameWin.close()
                    win.close()

    return colsIndex,rowsIndex,cols,rows,checkForSensor,sensorList,peteLocList,inputScore
               
#define sensors function to create sensors in field
def sensors(gridList, gameWin):

    #initialize necessary variables
    columns = []
    rows = []
    sensorList = []
    nextCol = 0
    nextRow = 0
    prob = 0.4
    upperAlpha = string.ascii_uppercase
    lowerAlpha = string.ascii_lowercase
    cols = []
    rows = []
    colIndex = 0
    index = 2.0
    yindex = -2.5
    rxindex = -2.5
    ryindex = 2.0
    prevCol = ""
    locCol = ""
    randomNums = []

    #create list of uppercase alphanumeric vals,
    #col y coords, and col x vals
    for i in upperAlpha:
        for j in range(10):
            cols.append(i+str(j))
            cols.append(str(yindex))
            cols.append(str(index))
            yindex += 40.0
        index += 40.0
        yindex = -2.5

    #create list of lowercase alphanumeric vals,
    #row y coords, and row x vals
    for k in lowerAlpha:
        for l in range(10):
            rows.append(k+str(l))
            rows.append(str(rxindex))
            rows.append(str(ryindex))
            rxindex += 40.0
        ryindex += 40.0
        rxindex = -2.5

    #create a list of random numbers from 2 to 400
    #in increments of 40
    for i in range(2,400,40):
        randomNums.append(i)

    #loop through rows and columns of the field
    for row in range(2,400,40):
        for column in range(2,400,40):

                #constantly save a random number from
                #the random number list
                randCol = sample(randomNums,1)

                #check if a col or row will have a sensor
                #40% (prob) of the time it will
                if(random() < prob):

                    #create the 36x5 orange sensor
                    colRect = Rectangle(Point(randCol[0],nextCol-2.5),Point(randCol[0] + 36,2.5 + nextCol))
                    colRect.setFill("orange")

                    #check if the sensor is not on the top of the field
                    if(colRect.getP1().getY() != -2.5):

                        #draw the orange sensor in the field
                        colRect.draw(gameWin)

                        #loop through the list of columns
                        for col in cols:

                            #check if the location is in a column
                            if(col.upper().isupper() != True):

                                #check if the sensor x coord is equal to predefined x coord
                                #for each column border name (Ex: A1)
                                if(colRect.getP1().getX() == float(col)):

                                    #check if the sensor y coord is equal to the predefined y coord
                                    #for each column border name (Ex: A1)
                                    if(colRect.getP1().getY() == prevCol):

                                        #save border location pete crossed
                                        sensorList.append(locCol)

                                #save the current column as previous column
                                prevCol = float(col)

                            #otherwise location is not a column
                            else:

                                #set petes location as the current column
                                locCol = col
                                
        #increment the next column by 40 (length of a rect)                
        nextCol += 40

    #column reached the end of the field and is reset
    nextCol = 0

    #loop through columns and rows of the field
    for col in range(2,400,40):
        for row in range(2,400,40):

            #constantly save a random number from
            #the random number list
            randRow = sample(randomNums,1)

            #check if a col or row will have a sensor
            #40% (prob) of the time it will
            if(random() < prob):

                #create the 5x36 orange sensor
                rowRect = Rectangle(Point(nextRow-2.5,randRow[0]),Point(2.5 + nextRow,randRow[0] + 36))
                rowRect.setFill("orange")

                #check if the sensor is not on the top of the field
                if(rowRect.getP1().getX() != -2.5):

                    #draw the orange sensor in the field
                    rowRect.draw(gameWin)

                    #loop through the list of rows
                    for row in rows:

                        #check if the location is in a row
                        if(row.upper().isupper() != True):

                            #check if the sensor y coord is equal to predefined y coord
                            #for each row border name (Ex: A1)
                            if(rowRect.getP1().getY() == float(row)):

                                #check if the sensor x coord is equal to the predefined x coord
                                #for each column border name (Ex: A1)
                                if(rowRect.getP1().getX() == prevRow):

                                    #save border location pete crossed
                                    sensorList.append(locRow)

                            #save the current row as previous row  
                            prevRow = float(row)

                        #otherwise location is not a row
                        else:

                            #set petes location as the current row
                            locRow = row
                            
        #increment the next row by 40 (length of a rect)
        nextRow += 40

    #row reached the end of the field and is reset
    nextRow = 0

    #remove duplicates from list of sensors
    sensorList = list(dict.fromkeys(sensorList))

    #return list of sensor locations
    return sensorList

#define scoresOut function to save new user name and score
#in a given text file
def scoresOut(inputScore, inputName):

    #create string to save to file
    outNewScore = "\n" + inputName + "," + str(inputScore)

    #open file to write to and append string to it
    outFile = open("top_scores.txt", "a")
    outFile.write(outNewScore)

    #close output file
    outFile.close()

#define scoresIn function to read saved names and scores
#to update top scores panel
def scoresIn():

    #initialize necessary variables
    topScoresList = []
    savedScoresList = []
    scoresList = []
    numList = []
    lowerAlpha = string.ascii_lowercase
    prevScore = 0
    
    #open the txt file for reading
    inFile = open("top_scores.txt", "r")

    #save each line of text in a list
    for line in inFile.readlines():
        savedScoresList.append(line.rstrip('\n'))

    #close text file
    inFile.close()

    #create a list of each name and score list
    for score in savedScoresList:

        #split each line into a list of name and score        
        scoresList.append(score.split(","))

    #loop through scoreslist to create a list of the scores
    for num in scoresList:
        numList.append(int(num[1]))

    #sort the scores
    numList = selSort(numList)

    #loop through the sorted num list to find the name of scorer
    for num in numList:

        #loop through scores list to compare score nums and save
        #the correct name and score to top list
        for score in scoresList:

            #check find score num and compare with sorted num list
            if(int(score[1]) == num):
                
                #save lowest value to new list for top score panel
                topScoresList.append(score[0] + "," + score[1])

                #remove the score after appending it
                scoresList.remove(score)

    #return list of top scorers
    return topScoresList

#define function selSort to sort number list and return the list
#code used from Blackboard CS 177 Prof. McFall
def selSort(nums):
    
    # sort nums into ascending order
    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n-1):
        
        # find the smallest item in nums[bottom]..nums[n-1]

        mp = bottom                 # bottom is smallest initially
        for i in range(bottom+1, n):    # look at each position
            if nums[i] < nums[mp]:      # this one is smaller
                mp = i                  # remember its index

        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom]

    #return numList
    return nums

#define main function to run program
def main():

    #call the game panel function to start game
    gamePanel()

#call main function to start program
main()
