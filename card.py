import pygame
from random import randint
pygame.init()
x = 500        #meio 500, min 230
y = 100
pos_x=275
pos_y=800
pos_y_a = 800
pos_y_c =800
timer =0
tempo_segundo=0

velocidade = 20
velocidade_outros =12

fundo = pygame.image.load('jogo_carro/img/painel.png')
carro = pygame.image.load('jogo_carro/img/carro.png')
policia = pygame.image.load('jogo_carro/img/policia.png')
car_azul = pygame.image.load('jogo_carro/img/car_blue.png')
car_vermelho = pygame.image.load('jogo_carro/img/car_red.png')
car_verde = pygame.image.load('jogo_carro/img/car_green.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)



janela = pygame.display.set_mode((1069,600))
pygame.display.set_caption("Criando um jogo de carros com python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade

    if comandos[pygame.K_RIGHT] and x < 750:
        x += velocidade+3
    if comandos[pygame.K_LEFT] and x > 240:
        x -= velocidade+3

    if(pos_y <= -180)and(pos_y_a <= -180 )and(pos_y_c <= -180):
        pos_y = randint(800,2000)
        pos_y_a = randint(800,2000)
        pos_y_c = randint(800,2000)


    pos_y -= velocidade_outros+10
    pos_y_a -= velocidade_outros+15
    pos_y_c -= velocidade_outros +20
    if(timer < 20):
        timer +=1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer =0


    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia,(pos_x,pos_y))
    janela.blit(car_azul,(pos_x+252,pos_y_c))
    janela.blit(car_vermelho,(pos_x+450,pos_y_a))
    janela.blit(texto,pos_texto)
    #pygame.draw.circle(janela,(0,255,0), (x,y),50)
    pygame.display.update()
pygame.quit()