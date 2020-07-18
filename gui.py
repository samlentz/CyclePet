import pygame
import pygame_gui
import apiworks
import pets
import requests
import webbrowser
import pickle
import time

xloc = 200
yloc = 400
desx = 200
desy = 400
framecount=1

def dogani():
    global framecount
    if framecount > 10000:
        framecount = 1
    global xloc
    global yloc
    diffx = 1 + int(abs((xloc - desx)/15))
    diffy = 1+ int(abs((yloc-desy)/15))
    
    if xloc == desx and desy == yloc:
        window_surface.blit((dog),(xloc,yloc))
    elif(desx >= xloc):
        if (framecount%60 ==0 ):
            pet.playWith()
        if(diffx < 3 and (diffy <3)):
            window_surface.blit(walksright[framecount%5],(xloc,yloc))
        else:
            window_surface.blit(runright[framecount%4],(xloc,yloc))

        xloc +=diffx
    else:
        if(diffx<3 and (diffy <3)):
            window_surface.blit(walksleft[framecount%5],(xloc,yloc))
        else:
            window_surface.blit(runleft[framecount%5],(xloc,yloc))

        xloc -=diffx
    if (desy > yloc):
        yloc += diffy
    elif(desy < yloc):
        yloc -= diffy
    #print((xloc,yloc,desx,desy))






print('1. New Game : 2. Load Save')
i = input()
if(i == '1'):
    f = apiworks.api()
    f.refresh()

    print("Pet Name:")
    name = input()
    pet = pets.pet(name,f.getMiles())
else:
    pet = pickle.load(open('save.p','rb'))
    f = pickle.load(open('f.p','rb'))
f.refresh()
miles = f.getMiles()
pet.refresh(miles)
pet.timePass()

pygame.init()
runleft = []
for i in range(1,6):
    runleft.append(pygame.image.load('shep/Shepherd_run_'+str(i)+'.png'))
runright = []
for i in runleft:
    runright.append(pygame.transform.flip(i,True,False))
walksleft =[]
for i in range(1,7):
    walksleft.append(pygame.image.load('shep/Shepherd_walk_'+str(i)+'.png'))
walksright =[]
for i in walksleft:
    walksright.append(pygame.transform.flip(i,True,False))


pygame.display.set_caption('CyclePet')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
coin = pygame.image.load('goldCoin1.png')
dog = pygame.image.load('shep/Shepherd_default.png')

manager = pygame_gui.UIManager((800, 600))
pygame.draw.rect(background,pygame.Color('#96f97b'),((0,0),(800,70)))
shop = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 10), (80, 50)),text='SHOP',manager=manager)
text2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((280, 35), (90, 30)),text ='Hunger',manager = manager)
text1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((60, 35), (90, 30)),text ='Happiness',manager = manager)
text3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((475, 10), (100, 25)),text ='Miles banked',manager = manager)
text6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((475, 30), (100, 25)),text ='Age (Hours)',manager = manager)

background.blit(coin,(575,8))
bgs = []
for i in pet.background:
    bgs.append(pygame.image.load(i))
clock = pygame.time.Clock()
is_running = True
shopopen = True



while is_running:
    framecount+=1
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = open( "save.p", "wb" ) 
            pickle.dump(pet,q)
            q.close()
            q = open('f.p','wb')
            pickle.dump(f,q)
            q.close()
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == shop:
                    pet.runStore()
        if event.type == pygame.MOUSEBUTTONUP:
            desx,desy = pygame.mouse.get_pos()

        manager.process_events(event)

        manager.update(time_delta)
    g = pet.getStatus()
    name=g[0]
    age = (g[1]/3600)
    happy=g[2]
    fill=g[3]
    dollas = g[4]
    bglevel = g[5]
    if(g[6]):
        is_running = False
    pygame.draw.rect(background,pygame.Color('#929591'),((250,10),((150,20))))
    pygame.draw.rect(background,pygame.Color('#ffb07c'),((250,10),((150/10)*fill,20)))
    pygame.draw.rect(background,pygame.Color('#929591'),((30,10),((150,20))))
    pygame.draw.rect(background,pygame.Color('#cea2fd'),((30,10),((150/10)*happy,20)))
    text3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((610, 10), (60, 30)),text =str(dollas),manager = manager)
    text4 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((610, 30), (60, 30)),text =str(int(age)),manager = manager)

    
    window_surface.blit(background, (0, 0))
    window_surface.blit(bgs[bglevel],(0,70))
    dogani()

    manager.draw_ui(window_surface)

    pygame.display.update()
    clock.tick(10)

