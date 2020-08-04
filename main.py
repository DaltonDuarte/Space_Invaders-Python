#Define onde a tela vai aparecer quando iniciar
x = 800
y = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Importações
import pygame
import random
from shotAlien import ShotAlien
from shotShip import ShotShip
from alien1 import Alien1
from alien2 import Alien2
from alien3 import Alien3
from alien4 import Alien4
from wall import Wall
from ship import Ship

#Inicializando pygame
pygame.init()

#Setando o tamanho e nome da janela do jogo
diplay = pygame.display.set_mode([900, 950])
pygame.display.set_caption("Space Invaders")

#Criando grupos
shotAlienGroup = pygame.sprite.Group()
shotShipGroup = pygame.sprite.Group()
objectGroup = pygame.sprite.Group()
alienGroup = pygame.sprite.Group()
wallGroup = pygame.sprite.Group()

#Inicializando fundo do jogo
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/fundo.png")
bg.image = pygame.transform.scale(bg.image, [900, 950])
bg.rect = bg.image.get_rect()

#Inicializando variavel para setar o FPS do jogo
clock = pygame.time.Clock()

#Inicializando variaveis do jogo
ListAliens = []
ListWalls = []
gameloop = True
rodadaB = True
inicio = True
pause = True
mexer = True
fim = False
tiro = True
randomAlien = 0
timerAlien4 = 0
maxPontos = 0
timerAl4 = 0
vidaWall = 0
pontos1 = 0
pontos2 = 0
rodada = 1
count = 0
speed = 1
vidas = 3
timer = 0

#Inicializando sons do jogo
shot_sound = pygame.mixer.Sound("data/shot.wav")
explosion_ship_sound = pygame.mixer.Sound("data/explosion_ship.ogg")
explosion_alien_sound = pygame.mixer.Sound("data/explosion_alien.wav")

#Pega a fonte da pasta e define o tamanho dela
ship_image = pygame.image.load("data/ship.png").convert()
fontText = pygame.font.Font('font/space-invaders-regular.ttf', 30)
fontPontos = pygame.font.Font('font/space-invaders-regular.ttf', 30)
fontLifes = pygame.font.Font('font/space-invaders-regular.ttf', 30)
fontGameOver = pygame.font.Font('font/space-invaders-regular.ttf', 50)
#Define os textos
textScore = fontText.render("SCORE< 1 >  HI-SCORE  SCORE< 2 >", True, (255, 255, 255), (0, 0, 0))
textGameOver = fontGameOver.render("GAME OVER", True, (255, 255, 255), (0, 0, 0))
textLifes = fontText.render(str(vidas), True, (255, 255, 255), (0, 0, 0))
textPonits = fontPontos.render(str(pontos1) + "                        " + str(maxPontos)
                               + "                        " + str(pontos2),
                               False, (255, 255, 255), (0, 0, 0))
textRodada = fontLifes.render("Rodada: " + str(rodada), True, (255, 255, 255), (0, 0, 0))
#Define a posição dos textos
textRectScore = textScore.get_rect()
textRectPontos = textPonits.get_rect()
textRectGameOver = textGameOver.get_rect()
textRectLifes = textLifes.get_rect()
textRectRodada = textLifes.get_rect()
textRectScore.center = (450, 20)
textRectPontos.center = (450, 70)
textRectGameOver.center = (450, 450)
textRectLifes.center = (30, 940)
textRectRodada.center = (720, 940)

#Inicializando alguns objetos
shotShip = ShotShip()
shotAlien = ShotAlien()
ship = Ship()

#Inicando o jogo
if __name__ == "__main__":

    #Loop principal
    while gameloop:
        #Definindo FPS do jogo
        clock.tick(60)

        #if para reiniciar o jogo
        if inicio:
            inicio = False
            # Inicializando todos os objetos
            ship = Ship(objectGroup)
            wall1 = Wall(objectGroup, wallGroup)
            wall2 = Wall(objectGroup, wallGroup)
            wall3 = Wall(objectGroup, wallGroup)
            wall4 = Wall(objectGroup, wallGroup)
            alien1_1 = Alien1(objectGroup, alienGroup)
            alien1_2 = Alien1(objectGroup, alienGroup)
            alien1_3 = Alien1(objectGroup, alienGroup)
            alien1_4 = Alien1(objectGroup, alienGroup)
            alien1_5 = Alien1(objectGroup, alienGroup)
            alien1_6 = Alien1(objectGroup, alienGroup)
            alien1_7 = Alien1(objectGroup, alienGroup)
            alien1_8 = Alien1(objectGroup, alienGroup)
            alien1_9 = Alien1(objectGroup, alienGroup)
            alien1_10 = Alien1(objectGroup, alienGroup)
            alien1_11 = Alien1(objectGroup, alienGroup)
            alien2_12 = Alien2(objectGroup, alienGroup)
            alien2_13 = Alien2(objectGroup, alienGroup)
            alien2_14 = Alien2(objectGroup, alienGroup)
            alien2_15 = Alien2(objectGroup, alienGroup)
            alien2_16 = Alien2(objectGroup, alienGroup)
            alien2_17 = Alien2(objectGroup, alienGroup)
            alien2_18 = Alien2(objectGroup, alienGroup)
            alien2_19 = Alien2(objectGroup, alienGroup)
            alien2_20 = Alien2(objectGroup, alienGroup)
            alien2_21 = Alien2(objectGroup, alienGroup)
            alien2_22 = Alien2(objectGroup, alienGroup)
            alien2_23 = Alien2(objectGroup, alienGroup)
            alien2_24 = Alien2(objectGroup, alienGroup)
            alien2_25 = Alien2(objectGroup, alienGroup)
            alien2_26 = Alien2(objectGroup, alienGroup)
            alien2_27 = Alien2(objectGroup, alienGroup)
            alien2_28 = Alien2(objectGroup, alienGroup)
            alien2_29 = Alien2(objectGroup, alienGroup)
            alien2_30 = Alien2(objectGroup, alienGroup)
            alien2_31 = Alien2(objectGroup, alienGroup)
            alien2_32 = Alien2(objectGroup, alienGroup)
            alien2_33 = Alien2(objectGroup, alienGroup)
            alien3_34 = Alien3(objectGroup, alienGroup)
            alien3_35 = Alien3(objectGroup, alienGroup)
            alien3_36 = Alien3(objectGroup, alienGroup)
            alien3_37 = Alien3(objectGroup, alienGroup)
            alien3_38 = Alien3(objectGroup, alienGroup)
            alien3_39 = Alien3(objectGroup, alienGroup)
            alien3_40 = Alien3(objectGroup, alienGroup)
            alien3_41 = Alien3(objectGroup, alienGroup)
            alien3_42 = Alien3(objectGroup, alienGroup)
            alien3_43 = Alien3(objectGroup, alienGroup)
            alien3_44 = Alien3(objectGroup, alienGroup)
            alien3_45 = Alien3(objectGroup, alienGroup)
            alien3_46 = Alien3(objectGroup, alienGroup)
            alien3_47 = Alien3(objectGroup, alienGroup)
            alien3_48 = Alien3(objectGroup, alienGroup)
            alien3_49 = Alien3(objectGroup, alienGroup)
            alien3_50 = Alien3(objectGroup, alienGroup)
            alien3_51 = Alien3(objectGroup, alienGroup)
            alien3_52 = Alien3(objectGroup, alienGroup)
            alien3_53 = Alien3(objectGroup, alienGroup)
            alien3_54 = Alien3(objectGroup, alienGroup)
            alien3_55 = Alien3(objectGroup, alienGroup)

            #Botando os objetos em listas
            ListAliens = [alien1_1, alien1_2, alien1_3, alien1_4, alien1_5, alien1_6, alien1_7, alien1_8, alien1_9,
                          alien1_10, alien1_11, alien2_12, alien2_13, alien2_14, alien2_15, alien2_16, alien2_17,
                          alien2_18, alien2_19, alien2_20, alien2_21, alien2_22, alien2_23, alien2_24, alien2_25,
                          alien2_26, alien2_27, alien2_28, alien2_29, alien2_30, alien2_31, alien2_32, alien2_33,
                          alien3_34, alien3_35, alien3_36, alien3_37, alien3_38, alien3_39, alien3_40, alien3_41,
                          alien3_42, alien3_43, alien3_44, alien3_45, alien3_46, alien3_47, alien3_48, alien3_49,
                          alien3_50, alien3_51, alien3_52, alien3_53, alien3_54, alien3_55]
            ListWalls = [wall1, wall2, wall3, wall4]

        #Pegando teclas pressionadas
        for event in pygame.event.get():
            #Sair do jogo
            if event.type == pygame.QUIT:
                gameloop = False

            if event.type == pygame.KEYDOWN:
                # Reiniciar o jogo
                if event.key == pygame.K_r and fim or len(ListAliens) == 0:
                    for i in ListWalls:
                        ListWalls.remove(i)
                        i.kill()
                    for i in ListAliens:
                        ListAliens.remove(i)
                        i.kill()
                    ship.kill()
                    inicio = True
                    fim = False
                    vidas = 3
                    timerAlien4 = 0
                    textLifes = fontText.render(str(vidas), True, (255, 255, 255), (0, 0, 0))

                # Tiro da nave
                if event.key == pygame.K_SPACE and pause:
                    if tiro and ship.alive():
                        shot_sound.set_volume(0.1)
                        shot_sound.play()
                        shotShip = ShotShip(objectGroup, shotShipGroup)
                        shotShip.rect.center = ship.rect.center
                    if shotShip.alive():
                        tiro = False

                #Pause do jogo
                if event.key == pygame.K_p:
                    if pause:
                        mexer = False
                        pause = False
                        ship.speed = 0
                        timerAl4 = 0
                    else:
                        mexer = True
                        pause = True
                        ship.speed = 5
                        timerAl4 = 1

                #Esquema para testar partes do jogo
                # if event.key == pygame.K_t:
                #     for i in ListAliens:
                #         ListAliens.remove(i)
                #         i.kill()
                #     for x in ListWalls:
                #         ListWalls.remove(x)
                #         x.kill()



        #Impede do tiro sair caso a nave esteja morta
        if not shotShip.alive():
            tiro = True

        #Acionando as funções "update" das classes
        objectGroup.update()
        #Desenhando as classes que tiverem no "objectGroup"
        objectGroup.draw(diplay)

        if mexer:
            #Aumentar a velocidade dos aliens depois de alguns destruidos
            if len(ListAliens) == 55:
                speed = rodada
            elif len(ListAliens) < 30:
                speed = rodada + 1
            elif len(ListAliens) < 10:
                speed = rodada + 2
            #Move os aliens a cada 3 quadros a nave se move na velocidade do "speed"
            count += 1
            if count % 3 == 0:
                for i in ListAliens:
                     if i.turn:
                         i.timer = speed
                     else:
                         i.timer = -speed
            else:
                for i in ListAliens:
                     if i.turn:
                         i.timer = 0
                     else:
                         i.timer = 0
            if count == 61:
                count = 0

        #Faz um alien aleatorio atirar
        if not len(ListAliens) == 0 and not fim and ship.alive() and pause:
            timer += 1
            for i in ListAliens:
                if i.alive():
                    if timer > 60:
                        timer = 0
                        randomAlien = random.choice(ListAliens)
                        shotAlien = ShotAlien(objectGroup, shotAlienGroup)
                        shotAlien.rect.center = randomAlien.rect.center


        #Caso o tiro do alien acerte a nave ela perde uma vida
        shipShotAlien = pygame.sprite.spritecollide(ship, shotAlienGroup, True, pygame.sprite.collide_mask)
        if shipShotAlien:
            explosion_ship_sound.set_volume(0.05)
            explosion_ship_sound.play()
            vidas -= 1
            textLifes = fontText.render(str(vidas), True, (255, 255, 255), (0, 0, 0))

        #Inicializa o quarto tipo de alien depois de um tempo
        timerAlien4 += timerAl4
        if timerAlien4 > 800 and not fim and not len(ListAliens) < 5 and pause:
            timerAlien4 = 0
            alien4_56 = Alien4(objectGroup, alienGroup)

        #Se a quantidade de vidas for igual a zero, a nave, os aliens e os muros são destruidos,
        #e caso a pontuação dessa rodada seja maior que a de antes ela vai para o "HighScore",
        #e tbm aciona o fim
        if vidas == 0:
            vidas = 3
            ship.kill()
            for i in ListAliens:
                i.kill()
            if pontos1 > maxPontos:
                maxPontos = pontos1
            pontos1 = 0
            textPonits = fontPontos.render(str(pontos1) + "                        " + str(maxPontos) +
                                           "                        " + str(pontos2),False, (255, 255, 255), (0, 0, 0))
            fim = True

        #Esquema para mostrar em qual rodade esta
        if len(ListAliens) == 55:
            rodadaB = True
        if len(ListAliens) == 0 and rodadaB:
            rodadaB = False
            rodada += 1
            textRodada = fontLifes.render("Rodada: " + str(rodada), True, (255, 255, 255), (0, 0, 0))

        #Caso a variavel "fim" seja True, o jogo acaba
        #e caso a pontuação dessa rodada seja maior que a de antes ela vai para o "HighScore",
        if fim:
            diplay.blit(textGameOver, textRectGameOver)
            for i in ListWalls:
                i.kill()
            for i in ListAliens:
                i.kill()
            ship.kill()
            rodada = 1
            textRodada = fontLifes.render("Rodada: " + str(rodada), True, (255, 255, 255), (0, 0, 0))
            if pontos1 > maxPontos:
                maxPontos = pontos1
            pontos1 = 0
            textPonits = fontPontos.render(str(pontos1) + "                        " + str(maxPontos)
                                           + "                        " + str(pontos2),
                                           False, (255, 255, 255), (0, 0, 0))

        #Caso o tiro da nave e o tiro do alien se colidam, eles são destuidos
        pygame.sprite.groupcollide(shotShipGroup, shotAlienGroup, True, True, pygame.sprite.collide_mask)

        #Esquema para ver se a parede leva tiro da nave ou dos aliens, caso ela receba 10 tiros ela é destruida
        if not len(ListWalls) == 0:
            for i in ListWalls:
                wallShotShip = pygame.sprite.spritecollide(i, shotShipGroup, True, pygame.sprite.collide_mask)
                wallShotAlien = pygame.sprite.spritecollide(i, shotAlienGroup, True, pygame.sprite.collide_mask)
                if wallShotShip or wallShotAlien:
                    i.vida -= 1
                    if i.vida == 0:
                        i.kill()
                        ListWalls.remove(i)

        #Esquema para ver se o alien colide com a parede, caso colida, ambos são destruidos
        if not len(ListWalls) == 0:
            for i in ListWalls:
                wallAlien = pygame.sprite.spritecollide(i, alienGroup, True, pygame.sprite.collide_mask)
                if wallAlien:
                    ListWalls.remove(i)
                    i.kill()

        #Esquema para ver se o alien colide com a nave, caso colida, o jogo acaba
        ShipAlienGroup = pygame.sprite.spritecollide(ship, alienGroup, True, pygame.sprite.collide_mask)
        if ShipAlienGroup:
            fim = True

        #Esquema para ver se o tiro da nave acerta os aliens, caso acerte, o alien é destruido e recebe ponto pela morte
        ShipShot = pygame.sprite.groupcollide(shotShipGroup, alienGroup, True, True, pygame.sprite.collide_mask)
        if ShipShot:
            explosion_alien_sound.set_volume(0.05)
            explosion_alien_sound.play()
            for i in ListAliens:
                if not i.alive():
                    pontos1 += i.valorponto
                    textPonits = fontPontos.render(str(pontos1) + "                        " + str(maxPontos)
                                                   + "                        " + str(pontos2),
                                                   False, (255, 255, 255), (0, 0, 0))
                    ListAliens.remove(i)

        #Esquema para mostrar imagem da nave no canto inferior esquerdo, para representar as vidas que restam
        if vidas == 3:
            diplay.blit(ship_image, [60, 925])
            diplay.blit(ship_image, [120, 925])
        elif vidas == 2:
            diplay.blit(ship_image, [60, 925])

        #Desenha os textos defenidos la em cima
        diplay.blit(textRodada, textRectRodada)
        diplay.blit(textLifes, textRectLifes)
        diplay.blit(textScore, textRectScore)
        diplay.blit(textPonits, textRectPontos)

        #Atualiza a tela
        pygame.display.update()

