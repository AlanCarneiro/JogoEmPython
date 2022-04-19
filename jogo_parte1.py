import pygame
from random import randint
pygame.init()
x = 450
y = 100
pos_x = 300
pos_y = 1200
pos_y_a = 800
pos_y_c = 2000
timer = 0
tempo_segundo = 0

velocidade = 10
velocidade_outros = 12

fundo = pygame.image.load('cenario1.png')
moto = pygame.image.load('moto.png')
moto2 = pygame.image.load('moto2.png')
moto3 = pygame.image.load('moto3.png')
moto4 = pygame.image.load('moto4.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo:",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    
    if comandos [pygame.K_RIGHT] and x<= 670:
            x+= velocidade
    if comandos [pygame.K_LEFT] and x >= 250:
            x-= velocidade 
    
    # detecta a colisao

    if(x + 80 > pos_x and y + 670 > pos_y): #colisao lado direito
        y = 1200

    if(x - 80 > pos_x and y - 200 and y + 180 > pos_y_a): #colisao lado esquerdo
        y = 1200

    if((x + 80 > pos_x - 330 and y + 180 > pos_y_c)) and ((x - 80 < pos_x - 330 and y + 180 > pos_y_c)):
        y = 1200

    if (pos_y <= -30):
        pos_y = randint(800,1000)

    if (pos_y_a <= -30): 
        pos_y_a = randint(1200,2000)

    if (pos_y_c <= -30):
        pos_y_c = randint(2200,3000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0


    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo, (0,0))
    janela.blit(moto,(x,y))
    janela.blit(moto2,(pos_x,pos_y))
    janela.blit(moto3,(pos_x + 200,pos_y_a))
    janela.blit(moto4,(pos_x + 330,pos_y_c))
    janela.blit(texto,pos_texto)

    pygame.display.update()      

pygame.QUIT()