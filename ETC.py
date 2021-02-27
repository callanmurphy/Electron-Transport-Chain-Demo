#Electron Transport Chain – Callan Murphy
#June 17, 2018
'''
This program will allow the user to observe an animated process of the ETC,
including all of the various steps from NADH and FADH2 to the creation of ATP.
'''

import pygame, random, time #imports pygame and random modules
pygame.init() #initializes pygame with all its included components

global clock
clock = pygame.time.Clock()

def menu():
    '''
    Main menu function to display the menu upon beginnning the game. Allows
    the player to navigate and choose either 'controls' or 'play game',
    running the corresponding function to display the menu item.
    '''
    menuSelectImage = pygame.image.load("MenuSelect.gif")
    select = menuSelectImage.get_rect()
    menuScreen = pygame.display.set_mode((1280, 705))
    font1 = pygame.font.SysFont('Arial', 30)
    font4 = pygame.font.SysFont('Arial', 50)
    font5 = pygame.font.SysFont('Arial', 45)
    menuText = font4.render('Electron Transport Chain Simulation - Callan Murphy', False, (255, 255, 255))
    menuOption1Text = font5.render('Begin', False, (0, 0, 0))
    menuOption2Text = font5.render('Controls', False, (0, 0, 0))
    instructionText = font1.render("Use the UP and DOWN keys to scroll through the menu and 'enter' to select", False, (255,255,255))
    closeText = font1.render("Press ESC to exit", False, (255,255,255))
    select.centerx = 485
    select.centery = 325
    option1 = True #which menu option is selected
    close = 0 #used to exit main loop
    while True: #main menu loop
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit() #closes window
                    close = 1
                    break
                if event.key == pygame.K_UP: #moves selector up
                    option1 = True
                    select.centerx = 485
                    select.centery = 325
                if event.key == pygame.K_DOWN: #moves selector down
                    option1 = False
                    select.centery = 425
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        close = 1
                        pygame.display.quit() #closes window
                        main()
                        break
                    elif option1 == False:
                        close = 1
                        pygame.display.quit() #closes window
                        controls()
                        break
        if close == 1:
            break
        else:
            menuScreen.fill((190,0,190))
            menuScreen.blit(menuText,(120,130))
            menuScreen.blit(menuOption1Text,(550,300))
            menuScreen.blit(menuOption2Text,(550,400))
            menuScreen.blit(instructionText,(15,610))
            menuScreen.blit(closeText,(15,650))
            menuScreen.blit(menuSelectImage, select)
            pygame.display.flip() #allows colour/other graphics to be displayed
            clock.tick(30)
            
def controls():
    controlScreen = pygame.display.set_mode((1280, 705))
    close = 0
    font7 = pygame.font.SysFont('Calibri', 60)
    font6 = pygame.font.SysFont('Calibri', 35)
    controlsText = font7.render('CONTROLS', False, (255, 255, 255))
    text1 = font6.render("n key: add NADH molecule", False, (255, 255, 255))
    text2 = font6.render("f key: add FADH₂ molecule", False, (255, 255, 255))
    text3 = font6.render("ESC key: exit the program", False, (255, 255, 255))
    exitScreenText = font6.render("Press ESC to return to the menu", False, (255, 255, 255))
    while True:
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit() #closes window
                    close = 1
                    break
        if close == 1:
            break
        
        controlScreen.fill((190,0,190))
        controlScreen.blit(controlsText,(495, 100))
        controlScreen.blit(exitScreenText,(405, 600))
        controlScreen.blit(text1,(441, 300))
        controlScreen.blit(text2,(443, 360))
        controlScreen.blit(text3,(445, 420))
        pygame.display.flip()
        clock.tick(30)
    menu()
        
    
def main():
    '''
    Main function to operate the ETC
    '''
    font1 = pygame.font.SysFont('Calibri', 30)
    closeText = font1.render("Press 'ESC' to exit", False, (255,255,255))
    screen = pygame.display.set_mode((1280, 705))
    backgroundImage = pygame.image.load("ETC.gif").convert()
    e000 = pygame.image.load("ETC.gif").convert()
    e100 = pygame.image.load("ETC100.png").convert()
    e110 = pygame.image.load("ETC110.png").convert()
    e101 = pygame.image.load("ETC101.png").convert()
    e111 = pygame.image.load("ETC111.png").convert()
    e010 = pygame.image.load("ETC010.png").convert()
    e011 = pygame.image.load("ETC011.png").convert()
    e001 = pygame.image.load("ETC001.png").convert()
    background = backgroundImage.get_rect()
    nadhImage = pygame.image.load("greenCircle.gif")
    nadh = []
    nadImage = pygame.image.load("greyCircle.gif")
    nad = []
    fadh2Image = pygame.image.load("orangeCircle.gif")
    fadh2 = []
    fadImage = pygame.image.load("greyCircle.gif")
    fad = []
    hImage = pygame.image.load("lightBlueCircle.gif")
    eImage = pygame.image.load("whiteCircle.gif")
    adpImage = pygame.image.load("ADP.gif")
    atpImage = pygame.image.load("ATP.gif")
    atps = []
    adp = adpImage.get_rect()
    adp.centerx = 970
    adp.centery = 520
    h1 = [] #nadh hydrogens
    hx = 410#740
    for i in range(0,11):
        h1.append(eImage.get_rect())
        h1[i].centerx = hx
        h1[i].centery = 600
        hx += 30
    '''h2 = [] #fadh2 hydrogens
    hx = 410#740
    for i in range(0,11):
        h2.append(eImage.get_rect())
        h2[i].centerx = hx
        h2[i].centery = 570
        hx += 30'''
    
    e = []
    nadhE = []
    fadh2E = []
    qImage = pygame.image.load("Q.gif")
    q = qImage.get_rect()
    q.centerx = 280
    q.centery = 320
    cImage = pygame.image.load("C.gif")
    c = cImage.get_rect()
    c.centerx = 668
    c.centery = 280
    oImage = pygame.image.load("brownCircle.gif")
    o = []
    h2o = 0
    atp = 0

    titlesFont = pygame.font.SysFont('Calibri', 30)
    namesFont = pygame.font.SysFont('Calibri', 14)

    nadhText = namesFont.render('NADH', False, (0, 0, 0))
    nadText = namesFont.render('NAD+', False, (0, 0, 0))
    fadh2Text = namesFont.render('FADH2', False, (0, 0, 0))
    fadText = namesFont.render('FAD', False, (0, 0, 0))
    hText = namesFont.render('H+', False, (0, 0, 0))
    eText = namesFont.render('E-', False, (0, 0, 0))
    oText = namesFont.render('1/2 O₂', False, (0, 0, 0))
    adpText = namesFont.render('ADP', False, (0, 0, 0))
    pText = namesFont.render('P', False, (0, 0, 0))
    iText = namesFont.render('i', False, (0, 0, 0))
    atpsText = namesFont.render('ATP', False, (0, 0, 0))

    title1 = titlesFont.render('Intermembrane Space', False, (0, 0, 0))
    title2 = titlesFont.render('Inner Mitochondrial Membrane', False, (0, 0, 0))
    title3 = titlesFont.render('Mitochondrial Matrix', False, (0, 0, 0))
    c1Text = titlesFont.render('I', False, (0, 0, 0))
    c2Text = titlesFont.render('II', False, (0, 0, 0))
    c3Text = titlesFont.render('III', False, (0, 0, 0))
    c4Text = titlesFont.render('IV', False, (0, 0, 0))
    qText = titlesFont.render('Q', False, (0, 0, 0))
    cytCText = titlesFont.render('Cyt c', False, (0, 0, 0))
    atpText = titlesFont.render('ATP', False, (0, 0, 0))
    synthaseText = titlesFont.render('Synthase', False, (0, 0, 0))
    h2oMadeText = titlesFont.render(str(h2o) + '  H₂O made', False, (0, 0, 0))
    atpMadeText = titlesFont.render(str(atp) + '  ATP made', False, (0, 0, 0))

    exitLoop = False
    newNadh = False
    nadhMove1 = False
    nadhMove2 = False
    fadh2Move1 = False
    fadh2Move2 = False

    qPosition = 1
    qStart = True
    qInitial = False
    qMiddle = False
    movingElectrons = []

    cPosition = 1
    cStart = True
    cInitial = False
    movingElectrons2 = []

    movingElectrons3 = []
    finalElectrons = []
    moveO = False
    #h = [h1, h2]
    moveH = False
    newH = 0
    newH2 = 0
    startedMoveH = 0

    energy1 = 0
    energy2 = 0
    energy3 = 0

    hPath1 = False
    hPath2 = False
    hPath3 = False

    paths = [hPath1, hPath2, hPath3]

    movingH1 = []
    hMover1 = []
    movingH2 = []
    hMover2 = []
    movingH3 = []
    hMover3 = []
    addNadh = False
    addFadh2 = False
    allowNewNadh = True
    allowNewFadh2 = True

    newH1 = False
    newH2 = False

    moveBoth = False

    finished1 = False
    finished2 = False

    adpMoving = []
    adpMove = False

    atpMake = False
    atpMove = 0

    prevent1 = False
    prevent2 = False
    prevent3 = False

    while True:
        for event in pygame.event.get():     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exitLoop = True
                        pygame.display.quit() #closes window
                        break
                    if event.key == pygame.K_n and allowNewNadh == True:
                        addNadh = True
                        allowNewNadh = False
                    if event.key == pygame.K_f and allowNewFadh2 == True:
                        addFadh2 = True
                        allowNewFadh2 = False
                    
        if exitLoop == True:
            break         
        
        #if len(nadh) == 0:
        if addNadh == True:
            addNadh = False
            nadh.append(nadhImage.get_rect())
            nadh[-1].centerx = -30
            nadh[-1].centery = 600
            nadhMove1 = True

        if len(nadh) > 0:
            if nadhMove1 == True:
                nadh[-1].centerx += 2
            if nadh[-1].centerx == 20:
                nadhMove1 = False
                nadhMove2= True
            if nadhMove2 == True:
                nadh[-1].centery -= 2
                nadh[-1].centerx += 2
            if nadh[-1].centery == 430:
                nadhMove2 = False
                nad.append(nadImage.get_rect())
                nad[-1].centerx = nadh[-1].centerx
                nad[-1].centery = nadh[-1].centery
                h1.append(hImage.get_rect())
                newH1 = True
                h1[-1].centerx = nadh[-1].centerx + 60
                h1[-1].centery = nadh[-1].centery
                nadh.pop(-1)

                nadhE.append(eImage.get_rect())
                nadhE[-1].centerx = nad[-1].centerx
                nadhE[-1].centery = nad[-1].centery
                e.append(nadhE[-1])
                allowNewNadh = True
                

        if len(nad) > 0:
            for i in range(0, len(nad)):
                nad[i].centery += 2
                nad[i].centerx += 2
                if nad[i].centery == 725:
                    nad.pop(i)

        #if len(fadh2) == 0:
        if addFadh2 == True:
            addFadh2 = False
            fadh2.append(fadh2Image.get_rect())
            fadh2[-1].centerx = -80
            fadh2[-1].centery = 600
            fadh2Move1 = True

        if len(fadh2) > 0:
            if fadh2Move1 == True:
                fadh2[-1].centerx += 2
            if fadh2[-1].centerx == 220:
                fadh2Move1 = False
                fadh2Move2= True
            if fadh2Move2 == True:
                fadh2[-1].centery -= 2
                fadh2[-1].centerx += 2
            if fadh2[-1].centery == 430:
                fadh2Move2 = False
                fad.append(fadImage.get_rect())
                fad[-1].centerx = fadh2[-1].centerx
                fad[-1].centery = fadh2[-1].centery
                h1.append(hImage.get_rect())
                h1.append(hImage.get_rect())
                h1[-1].centerx = fadh2[-1].centerx + 60
                h1[-1].centery = fadh2[-1].centery
                h1[-2].centerx = fadh2[-1].centerx + 90
                h1[-2].centery = fadh2[-1].centery
                fadh2.pop(-1)

                fadh2E.append(eImage.get_rect())
                fadh2E[-1].centerx = fad[-1].centerx + 20
                fadh2E[-1].centery = fad[-1].centery
                e.append(fadh2E[-1])
                allowNewFadh2 = True

        if len(fad) > 0:
            for i in range(0, len(fad)):
                fad[i].centery += 2
                fad[i].centerx += 2
                if fad[i].centery == 725:
                    fad.pop(i)

        for i in h1:
            if i.centerx < 410 and i.centery >= 580:
                i.centery = 410
                newH1 = []
                newH1.append(i)
                for x in h1:
                    if x == h1[0]:
                        pass
                    elif x == i:
                        pass
                    else:
                        newH1.append(x)
                h1 = newH1
                    
        if len(h1) >= 1:
            if h1[0].centerx > 410:
                for x in h1:
                    x.centerx -= 2
                if len(h1) >= 2 and moveBoth == False:
                    if h1[-1].centerx < h1[-2].centerx + 30:
                        h1[-1].centerx += 2
                elif len(h1) >= 3 and moveBoth == True:
                    if h1[-1].centerx < h1[-3].centerx + 30:
                        h1[-1].centerx += 2
                    if h1[-2].centerx < h1[-3].centerx + 30:
                        h1[-2].centerx += 2

        if len(h1) >= 2:
            if h1[-2].centery == 600:
                if h1[-1].centerx < h1[-2].centerx + 30:
                    h1[-1].centerx += 2
                if h1[-1].centery < 550:
                    h1[-1].centery += 2
                if h1[-1].centerx >= h1[-2].centerx + 30:
                    willHMove = True
                    for x in hMover1:
                        if x == 7:
                            willHMove = False
                    for x in hMover2:
                        if x == 7:
                            willHMove = False
                    for x in hMover3:
                        if x == 7:
                            willHMove = False
                    if willHMove == True:
                        if h1[-1].centery < h1[-2].centery:
                                h1[-1].centery += 2
                        '''if h1[-2].centery == 600:
                            if h1[-1].centery < h1[-2].centery:
                                h1[-1].centery += 2
                        else:
                            if h1[-1].centery < h1[-3].centery:
                                h1[-1].centery += 2'''
                    
            else:
                if len(h1) >= 3:
                    moveBoth = True

        if moveBoth == True:
            try:
                if h1[-1].centerx < h1[-3].centerx + 30:
                    h1[-1].centerx += 4
                if h1[-1].centery < 550:
                    h1[-1].centery += 4
                if h1[-1].centerx >= h1[-3].centerx + 30:
                    willHMove = True
                    for x in hMover1:
                        if x == 7:
                            willHMove = False
                    for x in hMover2:
                        if x == 7:
                            willHMove = False
                    for x in hMover3:
                        if x == 7:
                            willHMove = False
                    if willHMove == True:
                        if h1[-1].centery < h1[-3].centery:
                            h1[-1].centery += 4
                        else:
                            finished1 = True
                if h1[-2].centerx < h1[-3].centerx + 30:
                    h1[-2].centerx += 4
                if h1[-2].centery < 550:
                    h1[-2].centery += 4
                if h1[-2].centerx >= h1[-3].centerx + 30:
                    willHMove = True
                    for x in hMover1:
                        if x == 7:
                            willHMove = False
                    for x in hMover2:
                        if x == 7:
                            willHMove = False
                    for x in hMover3:
                        if x == 7:
                            willHMove = False
                    if willHMove == True:
                        if h1[-2].centery < h1[-3].centery:
                            h1[-2].centery += 4
                        else:
                            finished2 = True
            except:
                pass

            if finished1 == True and finished2 == True:
                moveBoth = False

        for i in range(0,len(h1)):
            if h1[i].centerx >= 900:
                removeIndex = h1.index(h1[i])
                h1.pop(removeIndex)
                break

        for i in range(0,len(nadhE)):
            if nadhE[i].centerx < 240:
                nadhE[i].centerx += 2
            if nadhE[i].centery > 330:
                nadhE[i].centery -= 2

        for i in range(0,len(fadh2E)):
            if fadh2E[i].centery > 365:
                fadh2E[i].centery -= 2

        ###########################
        
        if qPosition == 1:
            if qInitial == True:
                movingElectrons = []
                qInitial = False
            if qStart == True:
                for i in nadhE:
                    if i.centerx > 239 and i.centerx < 242 and i.centery < 331:
                        removeIndex = nadhE.index(i)
                        nadhE.pop(removeIndex)
                        movingElectrons.append(i)
                        energy1 += 1
            if qMiddle == True:
                for i in fadh2E:
                    if i.centerx >= 400 and i.centerx <= 420 and i.centery <= 365:
                        removeIndex = fadh2E.index(i)
                        fadh2E.pop(removeIndex)
                        movingElectrons.append(i)
            q.centerx += 5
            for i in movingElectrons:
                if i.centerx < q.centerx:
                    i.centerx += 6
                if i.centery > q.centery:
                    i.centery -= 6
                else:
                    i.centerx += 5
            if q.centerx >= 510:
                qPosition = 2

        if q.centerx > 290:
            qStart = False
        if q.centerx > 390 and q.centerx < 420:
            qMiddle = True
        else:
            qMiddle = False

        for i in movingElectrons:
            if i.centerx > 510 and i.centerx < 600:
                i.centerx += 5
            if i.centerx > 510 and i.centery > 280:
                i.centery -= 5
            if i.centerx >= 600 and i.centery <= 280:
                removeIndex = movingElectrons.index(i)
                movingElectrons.pop(removeIndex)
                energy2 += 1

        if qPosition == 2:
            q.centerx -= 5
            if q.centerx == 280:
                qPosition = 1
                qInitial = True
                qStart = True
                
        #######################

        if cPosition == 1:
            if cInitial == True:
                movingElectrons2 = []
                cInitial = False
            if cStart == True:
                for i in e:
                    if i.centerx > 598 and i.centerx < 605 and i.centery <= 278:
                        movingElectrons2.append(i)
            c.centerx += 5
            for i in movingElectrons2:
                if i.centerx < c.centerx:
                    i.centerx += 6
                if i.centery > c.centery:
                    i.centery -= 6
                else:
                    i.centerx += 5
            if c.centerx >= 740:
                cPosition = 2

        if c.centerx > 680:
            cStart = False
            
        for i in movingElectrons2:
            if i.centerx > 730: #and eCounter == 0: 
                movingElectrons3.append(i)
                removeIndex = movingElectrons2.index(i)
                movingElectrons2.pop(removeIndex)
                energy3 += 1          

        for i in movingElectrons3:
            if i.centerx < 900:
                i.centerx += 4
            if i.centerx >= 900 and i.centery < 600:
                i.centery += 4
            if i.centery >= 600:
                finalElectrons.append(i)
                removeIndex = movingElectrons3.index(i)
                movingElectrons3.pop(removeIndex)

        if cPosition == 2:
            c.centerx -= 5
            if c.centerx == 668:
                cPosition = 1
                cInitial = True
                cStart = True

        if energy1 > 0:
            backgroundImage = e100
            if energy2 > 0:
                backgroundImage = e110
            '''elif energy3 > 0:
                backgroundImage = pygame.image.load("ETC111.png").convert()'''

        elif energy2 > 0:
            backgroundImage = e010
            if energy3 > 0:
                backgroundImage = e011

        elif energy3 > 0:
            backgroundImage = e001

        else:
            backgroundImage = e000

        if energy3 > 0 and energy1 > 0 and energy2 > 0:
            backgroundImage = e111

        if len(finalElectrons) >= 2 and len(o) == 0 and len(h1) >= 2:
            try:
                delElectrons = []
                moveO = True
                moveH = True
                o.append(oImage.get_rect())
                o[-1].centerx = 940
                o[-1].centery = 750
                for i in finalElectrons:
                    delElectrons.append(i)
                finalElectrons.pop(-1)
                finalElectrons.pop(-1)
            except:
                pass
            
        if moveO == True:
            try:
                if o[-1].centery <= 600:
                    moveO = False
                else:
                   o[-1].centery -= 3
            except:
                pass

        if moveH == True:
            while True:
                if len(h1) > 0:
                    break
            newH = h1[0]
            h1.pop(0)
            while True:
                if len(h1) > 0:
                    break
            newH2 = h1[0]
            h1.pop(0)
            moveH = False

        if newH != 0:
            if newH.centerx < 875:
                newH.centerx += 3
            elif newH.centery < e[0].centery:
                newH.centery += 3

        if newH2 != 0:
            if newH2.centerx < 850:
                newH2.centerx += 3
            elif newH2.centery < e[0].centery:
                newH2.centery += 3

        if len(o) > 0 and newH != 0 and newH2 != 0:
            try:
                if o[-1].centery <= 600 and newH.centery >= e[0].centery and newH2.centerx >= 848 and newH.centerx >= 873 and newH2.centery >= e[0].centery-10 and newH.centery >= e[0].centery-10:
                    for i in range(0,len(o)):
                        o.pop(i)
                    newH = 0
                    newH2 = 0
                    h2o += 1
                    e.pop(0)
                    e.pop(1)
            except:
                pass

        ###############

        if energy1 > 0 and len(h1) >= 2 and prevent1 == False:
            hPath1 = True
            prevent1 = True
            movingH1.append(h1[0])
            hMover1.append(1)
            h1.pop(0)

        if energy2 > 0 and len(h1) >= 2 and prevent2 == False:
            hPath2 = True
            prevent2 = True
            movingH2.append(h1[0])
            hMover2.append(1)
            h1.pop(0)

        if energy3 > 0 and len(h1) >= 2 and prevent3 == False:
            hPath3 = True
            prevent3 = True
            movingH3.append(h1[0])
            hMover3.append(1)
            h1.pop(0)

        if hPath1 == True:
            for hy in range(0,len(hMover1)):
                if hMover1[hy] == 1:
                    if movingH1[hy].centerx >= 200:
                        movingH1[hy].centerx -= 4
                    elif movingH1[hy].centery >= 450:
                        movingH1[hy].centery -= 4
                    else:
                        hMover1[hy] = 2
                if hMover1[hy] == 2:
                    if movingH1[hy].centery >= 300 and movingH1[hy].centery <= 303:
                        energy1 -= 1
                        prevent1 = False
                    if movingH1[hy].centery >= 100:
                        movingH1[hy].centery -= 4
                    else:
                        go = True
                        for i in movingH2:
                            if i != 0:
                                if movingH1[hy].colliderect(i):
                                    go = False
                        for i in movingH3:
                            if i != 0:
                                if movingH1[hy].colliderect(i):
                                    go = False
                        if go == True:
                            movingH1[hy].centerx -= 4
                            hMover1[hy] = 3
                        else:
                            pass
                if hMover1[hy] == 3:
                    if movingH1[hy].centerx <= 1090:
                        movingH1[hy].centerx += 4
                    else:
                        hMover1[hy] = 4
                if hMover1[hy] == 4:
                    if movingH1[hy].centery >= 547 and movingH1[hy].centery <= 550:
                        adpMoving.append(adpImage.get_rect())
                        adpMoving[-1].centerx = 970
                        adpMoving[-1].centery = 520
                        adpMove = True
                    if movingH1[hy].centery <= 650:
                        movingH1[hy].centery += 4
                    else:
                        hMover1[hy] = 5
                if hMover1[hy] == 5:
                    if movingH1[hy].centerx > 800:
                        movingH1[hy].centerx -= 4
                    else:
                        hMover1[hy] = 6
                if hMover1[hy] == 6:
                    if movingH1[hy].centery > 600:
                        movingH1[hy].centery -= 4
                    else:
                        hMover1[hy] = 7
                if hMover1[hy] == 7:
                    movingH1[hy].centerx -= 4
                    hitH = False
                    for i in h1:
                        if movingH1[hy].colliderect(i):
                            movingH1[hy].centerx += 4
                            hitH = True
                            break
                    if movingH1[hy].centerx < 410 and movingH1[hy].centery >= 580:
                            movingH1[hy].centerx = 410
                            hitH = True
                    if hitH == True:
                        h1.append(movingH1[hy])
                        hMover1[hy] = 8
                        #hMover3.pop(hy)
                        #movingH3.pop(hy)
                if hMover1[hy] == 8:
                    hMover1[hy] = 0
                    movingH1[hy] = 0

        if hPath2 == True:
            for hy in range(0,len(hMover2)):
                if hMover2[hy] == 1:
                    if movingH2[hy].centerx > 573:
                        movingH2[hy].centerx -= 4
                    if movingH2[hy].centerx < 570:
                        movingH2[hy].centerx += 4
                    elif movingH2[hy].centery >= 450:
                        movingH2[hy].centery -= 4
                    else:
                        hMover2[hy] = 2
                if hMover2[hy] == 2:
                    if movingH2[hy].centery >= 300 and movingH2[hy].centery <= 303:
                        energy2 -= 1
                        prevent2 = False
                    if movingH2[hy].centery >= 100:
                        movingH2[hy].centery -= 4
                    else:
                        go = True
                        for i in movingH1:
                            if i != 0:
                                if movingH2[hy].colliderect(i):
                                    go = False
                        for i in movingH3:
                            if i != 0:
                                if movingH2[hy].colliderect(i):
                                    go = False
                        if movingH2[hy].centerx < 410 and movingH2[hy].centery >= 580:
                            movingH2[hy].centerx = 410
                            hitH = True
                        if go == True:
                            movingH2[hy].centerx -= 4
                            hMover2[hy] = 3
                        else:
                            pass
                if hMover2[hy] == 3:
                    if movingH2[hy].centerx <= 1090:
                        movingH2[hy].centerx += 4
                    else:
                        hMover2[hy] = 4
                if hMover2[hy] == 4:
                    if movingH2[hy].centery >= 547 and movingH2[hy].centery <= 550:
                        adpMoving.append(adpImage.get_rect())
                        adpMoving[-1].centerx = 970
                        adpMoving[-1].centery = 520
                        adpMove = True
                    if movingH2[hy].centery <= 650:
                        movingH2[hy].centery += 4
                    else:
                        hMover2[hy] = 5
                if hMover2[hy] == 5:
                    if movingH2[hy].centerx > 800:
                        movingH2[hy].centerx -= 4
                    else:
                        hMover2[hy] = 6
                if hMover2[hy] == 6:
                    if movingH2[hy].centery > 600:
                        movingH2[hy].centery -= 4
                    else:
                        hMover2[hy] = 7
                if hMover2[hy] == 7:
                    movingH2[hy].centerx -= 4
                    hitH = False
                    for i in h1:
                        if movingH2[hy].colliderect(i):
                            movingH2[hy].centerx += 4
                            hitH = True
                            break
                    if movingH2[hy].centerx < 410 and movingH2[hy].centery >= 580:
                            movingH2[hy].centerx = 410
                            hitH = True
                    if hitH == True:
                        h1.append(movingH2[hy])
                        hMover2[hy] = 8
                        #hMover3.pop(hy)
                        #movingH3.pop(hy)
                if hMover2[hy] == 8:
                    hMover2[hy] = 0
                    movingH2[hy] = 0

        if hPath3 == True:
            for hy in range(0,len(hMover3)):
                if hMover3[hy] == 1:
                    if movingH3[hy].centerx <= 850:
                        movingH3[hy].centerx += 4
                    elif movingH3[hy].centery >= 450:
                        movingH3[hy].centery -= 4
                    else:
                        hMover3[hy] = 2
                if hMover3[hy] == 2:
                    if movingH3[hy].centery >= 300 and movingH3[hy].centery <= 303:
                        energy3 -= 1
                        prevent3 = False
                    if movingH3[hy].centery >= 100:
                        movingH3[hy].centery -= 4
                    else:
                        go = True
                        for i in movingH1:
                            if i != 0:
                                if movingH3[hy].colliderect(i):
                                    go = False
                        for i in movingH2:
                            if i != 0:
                                if movingH3[hy].colliderect(i):
                                    go = False
                        if go == True:
                            movingH3[hy].centerx -= 4
                            hMover3[hy] = 3
                        else:
                            pass
                if hMover3[hy] == 3:
                    if movingH3[hy].centerx <= 1090:
                        movingH3[hy].centerx += 4
                    else:
                        hMover3[hy] = 4
                if hMover3[hy] == 4:
                    if movingH3[hy].centery >= 547 and movingH3[hy].centery <= 550:
                        adpMoving.append(adpImage.get_rect())
                        adpMoving[-1].centerx = 970
                        adpMoving[-1].centery = 520
                        adpMove = True
                    if movingH3[hy].centery <= 650:
                        movingH3[hy].centery += 4
                    else:
                        hMover3[hy] = 5
                if hMover3[hy] == 5:
                    if movingH3[hy].centerx > 800:
                        movingH3[hy].centerx -= 4
                    else:
                        hMover3[hy] = 6
                if hMover3[hy] == 6:
                    if movingH3[hy].centery > 600:
                        movingH3[hy].centery -= 4
                    else:
                        hMover3[hy] = 7
                if hMover3[hy] == 7:
                    movingH3[hy].centerx -= 4
                    hitH = False
                    for i in h1:
                        if movingH3[hy].colliderect(i):
                            movingH3[hy].centerx += 4
                            hitH = True
                            break
                    if movingH3[hy].centerx < 410 and movingH3[hy].centery >= 580:
                            movingH3[hy].centerx = 410
                            hitH = True
                    if hitH == True:
                        h1.append(movingH3[hy])
                        hMover3[hy] = 8
                        #hMover3.pop(hy)
                        #movingH3.pop(hy)
                if hMover3[hy] == 8:
                    hMover3[hy] = 0
                    movingH3[hy] = 0

        if adpMove == True:
            for a in adpMoving:
                a.centerx += 3
                if a.centerx == 1150:
                    removeIndex = adpMoving.index(a)
                    adpMoving.pop(removeIndex)
                    atpMake = True
                    atpMove += 1

        if atpMake == True:
            for i in range(0, atpMove):
                atps.append(atpImage.get_rect())
                atps[-1].centerx = 1150
                atps[-1].centery = 520
            atpMake == False
            
        for i in range(0,atpMove):
            if atps[i] != 0:
                if atps[i].centerx == 1153:
                    atp += 1
                if atps[i].centerx >= 1310:
                    #atps.pop(i)
                    atps[i] = 0
                    break
                else:
                    atps[i].centerx += 3


        ###############

        h2oMadeText = titlesFont.render(str(h2o) + '  H₂O made', False, (0, 0, 0))
        atpMadeText = titlesFont.render(str(atp) + '  ATP made', False, (0, 0, 0))

        ###############
        
        screen.blit(backgroundImage, background)
        screen.blit(qImage, q)
        screen.blit(cImage, c)
        screen.blit(title1,(15,15))
        screen.blit(title2,(15,220))
        screen.blit(title3,(15,650))
        screen.blit(c1Text,(190,340))
        screen.blit(c2Text,(403,370))
        screen.blit(c3Text,(565,340))
        screen.blit(c4Text,(837,338))
        screen.blit(qText,(q.centerx-10,q.centery-18))
        screen.blit(cytCText,(c.centerx-30,c.centery-21))
        screen.blit(atpText,(1066,390))
        screen.blit(synthaseText,(1035,420))
        screen.blit(h2oMadeText,(1105,650))
        screen.blit(atpMadeText,(1105, 600))
        for i in range(0,len(nadh)):
            screen.blit(nadhImage, nadh[i])
            screen.blit(nadhText,(nadh[i].centerx-18,nadh[i].centery-9))
        for i in range(0,len(nad)):
            screen.blit(nadImage, nad[i])
            screen.blit(nadText,(nad[i].centerx-16,nad[i].centery-9))
        for i in range(0,len(fadh2)):
            screen.blit(fadh2Image, fadh2[i])
            screen.blit(fadh2Text,(fadh2[i].centerx-18,fadh2[i].centery-9))
        for i in range(0,len(fad)):
            screen.blit(fadImage, fad[i])
            screen.blit(fadText,(fad[i].centerx-11,fad[i].centery-9))
        for i in range(0,len(h1)):
            screen.blit(hImage, h1[i])
            screen.blit(hText,(h1[i].centerx-7,h1[i].centery-9))
        '''for i in range(0,len(h2)):
            screen.blit(hImage, h2[i])
            screen.blit(hText,(h2[i].centerx-7,h2[i].centery-9))'''
        for i in range(0,len(e)):
            screen.blit(eImage, e[i])
            screen.blit(eText,(e[i].centerx-7,e[i].centery-9))
        for i in range(0,len(o)):
            screen.blit(oImage, o[i])
            screen.blit(oText,(o[i].centerx-16,o[i].centery-9))
        if newH != 0:
            screen.blit(hImage, newH)
            screen.blit(hText,(newH.centerx-7,newH.centery-9))
        if newH2 != 0:
            screen.blit(hImage, newH2)
            screen.blit(hText,(newH2.centerx-7,newH2.centery-9))
        for i in range(0,len(movingH1)):
            if movingH1[i] != 0:
                screen.blit(hImage, movingH1[i])
                screen.blit(hText,(movingH1[i].centerx-7,movingH1[i].centery-9))
        for i in range(0,len(movingH2)):
            if movingH2[i] != 0:
                screen.blit(hImage, movingH2[i])
                screen.blit(hText,(movingH2[i].centerx-7,movingH2[i].centery-9))
        for i in range(0,len(movingH3)):
            if movingH3[i] != 0:
                screen.blit(hImage, movingH3[i])
                screen.blit(hText,(movingH3[i].centerx-7,movingH3[i].centery-9))
        screen.blit(adpImage, adp)
        screen.blit(adpText, (adp.centerx-37, adp.centery-10))
        screen.blit(pText, (adp.centerx+26, adp.centery-10))
        screen.blit(iText, (adp.centerx+42, adp.centery+3))
        for i in range(0, len(adpMoving)):
            screen.blit(adpImage, adpMoving[i])
            screen.blit(adpText, (adpMoving[i].centerx-37, adpMoving[i].centery-10))
            screen.blit(pText, (adpMoving[i].centerx+26, adpMoving[i].centery-10))
            screen.blit(iText, (adpMoving[i].centerx+42, adpMoving[i].centery+3))
        for i in range(0,atpMove):
            if atps[i] != 0:
                screen.blit(atpImage, atps[i])
                screen.blit(atpsText,(atps[i].centerx-10,atps[i].centery-13))
        screen.blit(closeText,(1050,5))
        pygame.display.flip()
        clock.tick(30)
    menu()

menu()
