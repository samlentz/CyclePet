import pygame
import pygame_gui
import apiworks
import pets
import requests
import webbrowser
import pickle

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
g = pet.getStatus()
print(g)
name=g[0]
age=g[1]
happy=g[2]
fill=g[3]
dollas = g[4]
pygame.init()





pygame.display.set_caption('CyclePet')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
coin = pygame.image.load('goldCoin1.png')
dog = pygame.image.load('Shepherd_default.png')

manager = pygame_gui.UIManager((800, 600))
pygame.draw.rect(background,pygame.Color('#96f97b'),((0,0),(800,70)))
shop = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 10), (80, 50)),text='SHOP',manager=manager)
text2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((280, 35), (90, 30)),text ='Hunger',manager = manager)
text1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((60, 35), (90, 30)),text ='Happiness',manager = manager)
text3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((475, 10), (100, 25)),text ='Miles banked',manager = manager)
text6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((475, 30), (100, 25)),text ='Age (Hours)',manager = manager)

background.blit(coin,(575,10))

dirt = pygame.image.load('grass.png')
clock = pygame.time.Clock()
is_running = True
shopopen = True

age = (pet.getStatus())[1]/3600


while is_running:
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
                    print('Hello World!')
        manager.process_events(event)

        manager.update(time_delta)
    pygame.draw.rect(background,pygame.Color('#929591'),((250,10),((150,20))))
    pygame.draw.rect(background,pygame.Color('#ffb07c'),((250,10),((150/10)*fill,20)))
    pygame.draw.rect(background,pygame.Color('#929591'),((30,10),((150,20))))
    pygame.draw.rect(background,pygame.Color('#cea2fd'),((30,10),((150/10)*happy,20)))
    text3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((610, 10), (60, 30)),text =str(dollas),manager = manager)
    text4 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((610, 30), (60, 30)),text =str(int(age)),manager = manager)

    
    
    window_surface.blit(background, (0, 0))
    window_surface.blit(dirt,(0,70))
    window_surface.blit(dog,(200,300))
    manager.draw_ui(window_surface)

    pygame.display.update()
    clock.tick(25)
