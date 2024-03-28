import pygame as pygame

Rainbow = [255, 255, 255]

Red = True
Green = True
Blue = True
onlyRed = True

def rainbowColor():
    global Red, Green, Blue, onlyRed
    if Red == True:
        if Green == True:
            if Blue == True:
                if Rainbow[0] == 0:
                    Red = False
                else:
                    Rainbow[0] = Rainbow[0] - col
    if Red == False:
        if Green == True:
            if Blue == True:
                if Rainbow[1] == 0:
                    Green = False
                else:
                    Rainbow[1] = Rainbow[1] - col
    if Red == False:
        if Green == False:
            if Blue == True:
                if Rainbow[0] == 255:
                    Red = True
                else:
                    Rainbow[0] = Rainbow[0] + col
    if Red == True:
        if Green == False:
            if Blue == True:
                if Rainbow[2] == 0:
                    Blue = False
                else:
                    Rainbow[2] = Rainbow[2] - col
    if Red == True:
        if Green == False:
            if Blue == False:
                if Rainbow[1] == 255:
                    Green = True
                else:
                    Rainbow[1] = Rainbow[1] + col
    if onlyRed == True:
        if Red == True:
            if Green == True:
                if Blue == False:
                    if Rainbow[0] == 0:
                        Red = False
                        onlyRed = False
                    else:
                        Rainbow[0] = Rainbow[0] - col
    if Red == False:
        if Green == True:
            if Blue == False:
                if Rainbow[0] == 255:
                    Red = True
                else:
                    Rainbow[0] = Rainbow[0] + col
    if onlyRed == False:
        if Red == True:
            if Green == True:
                if Blue == False:
                    if Rainbow[2] == 255:
                        Blue = True
                        onlyRed = True
                    else:
                        Rainbow[2] = Rainbow[2] + col
            
            
            

def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball, scoreA, scoreB, radius, scoreUp, count, color, gameStop, okStart, AScored, BScored

    if ballLocation[0] > screenWidth-radius:
        ballSpeedx=-ballSpeedx
        scoreA = scoreA + 1
        scoreUp = True
        count = 0
        gameStop = True
        okStart = True
        AScored = True
    if ballLocation[1] > screenHeight-radius:
        ballSpeedy=-ballSpeedy
    if ballLocation[0] < 0+radius:
        ballSpeedx=-ballSpeedx
        scoreB = scoreB+ 1
        scoreUp = True
        count = 0
        gameStop = True
        okStart = True
        BScored = True
    if ballLocation[1] < 0+radius:
        ballSpeedy=-ballSpeedy
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, color, ballLocation, radius, 0)

def MovePaddle():
    global PadA, PadASpeed, PadAU, PadAD
    PadA = PadA.move(0, PadASpeed)
    PadAU = PadAU + PadASpeed
    PadAD = PadAD + PadASpeed
    serveA[1] = PadAU - 75
    pygame.draw.rect(window, color, PadA)
    
def MovePaddleB():
    global PadB, PadBSpeed, PadBU, PadBD
    PadB = PadB.move(0, PadBSpeed)
    PadBU = PadBU + PadBSpeed
    PadBD = PadBD + PadBSpeed
    serveB[1] = PadBU - 75
    pygame.draw.rect(window, color, PadB)

def drawCenterLine():
    global screenWidth, screenHeight
    
    pygame.draw.line(window, color,  (screenWidth//2, 0) ,(screenWidth//2, screenHeight)) 
    
def drawScore(font):
    global scoreA, scoreB, colorB
    
    text = font.render(str(scoreA), True, colorB)
    window.blit(text, (450, 30))
    text = font.render(str(scoreB), True, colorB)
    window.blit(text, (520, 30))
    
startGame = False
gameStop = True

def someoneScored():
    global ballSpeedx, ballSpeedy, ballLocation, startGame, AServe, BServe, serveA, serveB
    if gameStop == True:
        ballSpeedx = 0
        ballSpeedy = 0
        ballLocation = [500,300]
    elif startGame == True:
        ballSpeedx = -2
        ballSpeedy = 2
        startGame = False
    elif AServe == True:
        ballLocation[0] = serveA[0]
        ballLocation[1] = serveA[1]
        AServe = False
        ballSpeedx = 2
        ballSpeedy = 2
        BScored = False
        AServe = False
    elif BServe == True:
        ballLocation[0] = serveB[0]
        ballLocation[1] = serveB[1]
        BServe = False
        ballSpeedx = -2
        ballSpeedy = 2
        AScored = False
        
        
        
        
okStart = True

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600


window = pygame.display.set_mode([1000, 600])

ballSpeedx=-2
ballSpeedy=2
PadASpeed = 0

scoreA = 0
scoreB = 0

black = (0,0,0)
white = (255,255,255)

ballcounter = 0

radius = 10

ballLocation = [500,300]
ball = pygame.Rect(ballLocation, (radius, radius))

"has to be a factor of 255"
"1,3,5,15, or 17"
col = 15

color = "white"
colorB = "white"

PadAD = 100

PadAU = 250

PadBD = 100

PadBU = 250

count = 0
scoreUp = False





PadBSpeed = 0
PadA = pygame.Rect((15, 100), (20, 150) )

PadB = pygame.Rect(( 965, 100), (20, 150) )


serveB = [964 - radius ,PadBD - 75]
serveA = [36 + radius ,PadAD - 75]

BServe = False

AServe = False

BScored = False

AScored = False




pygame.font.init() 
font = pygame.font.Font(None, 80)

while True:
    if PadBD > 25:
        pass
    else:
        PadBSpeed = 0
    if PadBU < 575:
        pass
    else:
        PadBSpeed = 0
    if PadAD > 25:
        pass
    else:
        PadASpeed = 0
    if PadAU < 575:
        pass
    else:
        PadASpeed = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if PadBU < 575:
                        PadBSpeed = 4
                if event.key == pygame.K_UP:
                    if PadBD > 25:
                        PadBSpeed = -4
                if event.key == pygame.K_w:
                    if PadAD > 25:
                        PadASpeed = -4
                if event.key == pygame.K_s:
                    if PadAU < 575:
                        PadASpeed = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadBSpeed = 0
            if event.key == pygame.K_SPACE:
                if okStart == True:
                    gameStop = False
                    startGame = True
                    okStart = False
                    
            if event.key == pygame.K_d:
                if okStart == True:
                    if BScored == True:
                        AServe = True
                        okStart = False
                        gameStop = False
                
                
            if event.key == pygame.K_LEFT:
                if okStart == True:
                    if AScored == True:
                        BServe = True
                        okStart = False
                        gameStop = False
                
                
                
            if event.key == pygame.K_DOWN:
                PadBSpeed = 0
            if event.key == pygame.K_w:
                PadASpeed = 0
            if event.key == pygame.K_s:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
    timer.tick(60)
    rainbowColor()
    window.fill(black)
    MoveBall()
    MovePaddle()
    MovePaddleB()
    someoneScored()
    if gameStop == False:
        if ballcounter == 300:
            ballcounter = 0
            if ballSpeedx < 0:
                ballSpeedx = ballSpeedx + -1
            else:
                ballSpeedx = ballSpeedx + 1
            if ballSpeedy < 0:
                ballSpeedy = ballSpeedy + -1
            else:
                ballSpeedy = ballSpeedy + 1
        else:
            ballcounter = ballcounter + 1
    if scoreUp == True:
        colorB = Rainbow
        if count == 300:
            count = 0
            colorB = 'white'
            scoreUp = False
        else:
            count = count + 1
    else:
        pass
        
    drawCenterLine()
    drawScore(font)
    pygame.display.flip()
    #check quit event
    #check up, down, spacebar event