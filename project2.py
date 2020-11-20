#
# CS 177 – project2.py
# Wilson Huang - 00311-14130
# This program is to get the top 4 game player's names and their scores after they move
# the object to a target area. It will first displays a window containing previous top 4 scores, player names,and
# different functional buttons. Then it will display different contents as 
# the user clicks different buttons. If the user wants to play, it will display grids where
# user can click in the same column or row to make the object move. When the object
# hits the target area, the programme will calculate the score he gets and display it
# in the beginning window if it is among the new top 4 scores.

# import any library needed
from graphics import *
import random

# define graph function
def graph(topList):

    # initialize any necessary variable
    xValue1 = 0
    yValue1 = 0
    objects = []
    newInfo = ""
   
    # create a 300x200 Graphics window with grey background
    win = GraphWin("Game Panel",300,200)
    win.setBackground("grey")

    # create four rectangles containing title,EXIT,and NEW PLAYER
    recTitle = Rectangle(Point(0,0),Point(300,40))
    recExit = Rectangle(Point(250,160),Point(300,200))
    recPlayer = Rectangle(Point(75,160),Point(225,200))
    recScore = Rectangle(Point(50,60),Point(250,150))

    # draw them in the window
    recTitle.draw(win)
    recExit.draw(win)
    recPlayer.draw(win)
    recScore.draw(win)

    # set fill as required
    recTitle.setFill("white")
    recExit.setFill("red")
    recPlayer.setFill("green")
    recScore.setFill("white")

    # append them in the list
    objects.append(recTitle)
    objects.append(recExit)
    objects.append(recPlayer)
    objects.append(recScore)

    # generate text "Pete-A-Maze","EXIT","TOP SCORES","=" in the rectangles
    title = Text(Point(150,20), "Pete-A-Maze")
    EXIT = Text(Point(275,180), "EXIT")
    newPlayer = Text(Point(150,180), "NEW PLAYER")
    top = Text(Point(150,70),"TOP SCORES")
    symbol = Text(Point(150,80),"="*10)
    title.draw(win)
    EXIT.draw(win)
    newPlayer.draw(win)
    top.draw(win)
    symbol.draw(win)

    # append them into list
    objects.append(title)
    objects.append(EXIT)
    objects.append(newPlayer)
    objects.append(top)
    objects.append(symbol)

    # attach top 4 scores and their achievers to the window
    top1 = Text(Point(150,90),"".join(topList[0]))
    top2 = Text(Point(150,106),"".join(topList[1]))
    top3 = Text(Point(150,122),"".join(topList[2]))
    top4 = Text(Point(150,138),"".join(topList[3]))
    top1.draw(win)
    top2.draw(win)
    top3.draw(win)
    top4.draw(win)
        
    # define a while loop until EXIT control is clicked
    while not (xValue1<300 and xValue1>250 and yValue1<200 and yValue1>160):

        # append player and score information
        objects.append(top1)
        objects.append(top2)
        objects.append(top3)
        objects.append(top4)

        # get mouse click point
        clickPoint1 = win.checkMouse()
        if clickPoint1:
            xValue1 = clickPoint1.getX()
            yValue1 = clickPoint1.getY()

            # check if it is in the NEW PLAYER area
            if xValue1<225 and xValue1>75 and yValue1<200 and yValue1>160:

                # undraw the player names and scores
                recScore.undraw()
                top.undraw()
                symbol.undraw()
                top1.undraw()
                top2.undraw()
                top3.undraw()
                top4.undraw()
            
                # change the top 4 scores into player name and add an entry box
                playerName = Text(Point(75,80), "Player Name:")
                playerName.draw(win)
                inputBox = Entry(Point(175,80),10)
                inputBox.draw(win)
                inputBox.setFill("white")

                # append the input box and player name into the list
                objects.append(playerName)
                objects.append(inputBox)
            
                # change NEW PLAYER into START!
                newPlayer.undraw()
                start = Text(Point(150,180), "START!")
                start.draw(win)
                objects.append(start)

                # check mouse click again
                clickPoint1 = win.getMouse()
                xValue1 = clickPoint1.getX()
                yValue1 = clickPoint1.getY()
                
                # check if it is in the START! area and player name not blank
                if (xValue1<225 and xValue1>75 and yValue1<200 and yValue1>160) and (inputBox.getText()!=""):

                    # create reset box and reset text 
                    recReset = Rectangle(Point(0,160),Point(50,200))
                    recReset.draw(win)
                    recReset.setFill("yellow")
                    reset = Text(Point(25,180), "RESET")
                    reset.draw(win)

                    # append reset box and text into the list
                    objects.append(recReset)
                    objects.append(reset)

                    # display new button,user name and the score
                    start.undraw()
                    newPlayer.draw(win)
                    currentPlayer = Text(Point(140,80),inputBox.getText())
                    currentPlayer.draw(win)
                    inputBox.undraw()
                    scoreText = Text(Point(75,140),"Score")
                    scoreText.draw(win)
                    currentText = Text(Point(140,140),"0")
                    currentText.draw(win)

                    # append current player name and score into the list
                    objects.append(currentPlayer)
                    objects.append(scoreText)
                    objects.append(currentText)

                    # call the field function to play the game
                    gameWindow,pete = field()  
    
                    # call sensor function
                    senLocation = sensor(gameWindow)

                    # call move function
                    borderCross,finalGrade = move(gameWindow,pete,senLocation,win,currentText)

                    # call scoresOut function to update final score
                    scoresOut(inputBox.getText(),finalGrade)

                    # call scoresIN function again to get new top 4 information
                    topList = scoresIn("top_scores.txt")
    
                    # call finish function
                    finish(gameWindow,currentText)

                    # remove all the contents and display start window again
                    for obj in objects:
                        obj.undraw()
                    win.close()
                    main()
                
    # close the window
    win.close()

    # return all the objects drawn
    return objects
    
# define field function
def field():

    # initialize any necessary variables
    recList = []

    # create a 400x400 pixel window with white background
    window = GraphWin("The Field",400,400)
    window.setBackground("white")

    # create 10x10 grid pattern with a light-grey outline
    for i in range(10):
        for j in range(10):
            r = Rectangle(Point(40*i,40*j),Point(40*(i+1),40*(j+1)))
            r.setFill("white")
            r.setOutline("grey")

            # append these rectangles into a list
            recList.append(r)    

    # fill the top-left grid with green and bottom-right grid with red
    recList[0].setFill("green")
    recList[99].setFill("red")

    # draw thhese rectangle into the field window
    for i in range(len(recList)):
        recList[i].draw(window)

    # draw a yellow 36x36 rectangle representing where Pete lives
    player = Rectangle(Point(2,2),Point(38,38))
    player.draw(window)
    player.setFill("yellow")

    # return Field and Pete objects
    return window,player


# define move function
def move(fieldName,rec,sensorName,windowName,scoreVariable):

    # initialize any necessary variables
    xPosition2 = 0
    yPosition2 = 0
    borderList = []
    grade = 0
    i = 0
    xPanel = 0
    yPanel = 0
    
    # create a while loop until Pete reach the bottom-right rectangle
    while not ((xPosition2>360 and xPosition2<400) and (yPosition2>360 and yPosition2<400)):

        # check a mouse click
        mousePosition = fieldName.checkMouse()
        if mousePosition:
            xClick = mousePosition.getX()
            yClick = mousePosition.getY()
            xPosition1 = rec.getP1().getX()
            yPosition1 = rec.getP1().getY()
            xPosition2 = rec.getP2().getX()
            yPosition2 = rec.getP2().getY()
    
            # if move rightward
            if xClick>xPosition2 and yClick>(yPosition1-2) and yClick<(yPosition2+2) :
                rec.move(40,0)

                # label each border it crosses
                letter = chr(97+int((yPosition1-2)//40))
                index = int((xPosition1+40-2)//40)
                borderList.append(str(letter)+str(index))
                i += 1

            # if move leftward
            if xClick<xPosition1 and yClick>(yPosition1-2) and yClick<(yPosition2+2) :
                rec.move(-40,0)

                # label each border it crosses
                letter = chr(97+int((yPosition1-2)//40))
                index = int((xPosition1-2)//40)
                borderList.append(str(letter)+str(index))
                i += 1

            # if move upward
            if yClick>yPosition2 and xClick>(xPosition1-2) and xClick<(xPosition2+2) :
                rec.move(0,40)

                # label each border it crosses
                letter = chr(65+int((xPosition1-2)//40))
                index = int((yPosition1+40-2)//40)
                borderList.append(str(letter)+str(index))
                i += 1

            # if move downward
            if yClick<yPosition1 and xClick>(xPosition1-2) and xClick<(xPosition2+2) :
                rec.move(0,-40)

                # label each border it crosses
                letter = chr(65+int((xPosition1-2)//40))
                index = int((yPosition1-2)//40)
                borderList.append(str(letter)+str(index))
                i += 1

            # use the clickIndex to compare overlapping in border and sensor
            if (sensorName.count(borderList[i-1])==0):
                grade += 1
            if (sensorName.count(borderList[i-1])==1):
                grade += 3
                    
            # calculate the score and store as string in a list
            scoreVariable.undraw()
            scoreVariable = Text(Point(140,140),grade)
            scoreVariable.draw(windowName)

            # check if there is a click in the game panel
            panelClick = windowName.checkMouse()
            if panelClick:
                xPanel = panelClick.getX()
                yPanel = panelClick.getY()

                # if reset button is clicked
                if xPanel<50 and yPanel>160:

                    # move pete back to its starting position
                    rec.undraw()
                    rec = Rectangle(Point(2,2),Point(38,38))
                    rec.setFill("yellow")
                    rec.draw(fieldName)

                    # clear the score
                    scoreVariable.undraw()
                    grade = 0
                    scoreVariable = Text(Point(140,140),grade)
                    scoreVariable.draw(windowName)

                # if exit button is clicked
                if xPanel>250 and yPanel>160:

                    # close the game panel
                    windowName.close()

                    # close the field panel
                    fieldName.close()

            # check pete position again
            xPosition1 = rec.getP1().getX()
            yPosition1 = rec.getP1().getY()
            xPosition2 = rec.getP2().getX()
            yPosition2 = rec.getP2().getY()

    # return border label list and final grade
    return borderList,grade


# define finish function
def finish(fieldName,scoreVariable):

    # display finish text as requested
    finish = Text(Point(200,200), "Finished!Click to Close")
    finish.draw(fieldName)

    #close the window
    fieldName.getMouse()
    scoreVariable.undraw()
    fieldName.close()

# define sensor function
def sensor(windowName):

    # initialize any necessary variables
    senList = []
    senCode = []

    # use two for loops to generate horizontal sensors
    for i in range(38,398,40):
        for j in range(10):

            # check 40% possibility
            if random.random() < 0.4:

                # create horizontal sensors
                horizontal = Rectangle(Point(2+40*j,i),Point(38+40*j,i+5))
                horizontal.setFill("orange")

                # append them into sensor list
                senList.append(horizontal)

                # label sensors using border code
                sensorXh = horizontal.getP1().getX()
                sensorYh = horizontal.getP1().getY()
                upper = chr(65+int((sensorXh-2)//40))
                upIndex = int((sensorYh+2)//40)

                # append sensor code into a list
                senCode.append(str(upper)+str(upIndex))

    # use two for loops to generate vertical sensors
    for i in range(38,398,40):
        for j in range(10):

            # check 40% possibility
            if random.random() < 0.4:

                # create vertical sensors
                vertical = Rectangle(Point(i,2+40*j),Point(i+5,38+40*j))
                vertical.setFill("orange")

                # append them into sensor list
                senList.append(vertical)

                # label sensors using border code
                sensorXv = vertical.getP1().getX()
                sensorYv = vertical.getP1().getY()
                lower = chr(97+int((sensorYv-2)//40))
                lowIndex = int((sensorXv+2)//40)
                senCode.append(str(lower)+str(lowIndex))

    # draw the entire sensor list in specified window
    for i in range(len(senList)):
        senList[i].draw(windowName)

    # return the list of sensor location
    return senCode

# define scoresOut function
def scoresOut(currentUser,userScore):

    # open top_scores file in append mode
    file1 = open("top_scores.txt","a")

    # write player name and score into it
    write = str(currentUser)+","+str(userScore)
    file1.writelines(write+"\n")

    # close the file
    file1.close()

# define scoresIn function
def scoresIn(fileName):

    # initialize any necessary variable
    detail = []
    nameAndScore = []

    # read the contents in the file
    file2 = open(fileName,"r")
    content = file2.read().splitlines()

    # append the splited list into a new list as list element
    for comb in content:
        nameAndScore = comb.split(",")
        detail.append(nameAndScore)
        
    # sort the name and score list in ascending order
    sortedDetail = sorted(detail,key=lambda Score:Score[1])

    # return the lowest 4 scores
    return sortedDetail[0:4]

# define main function
def main():
    
    # call scoresIN function
    lowest = scoresIn("top_scores.txt")

    # call graph function
    All = graph(lowest)           
      
# call main function
main()
