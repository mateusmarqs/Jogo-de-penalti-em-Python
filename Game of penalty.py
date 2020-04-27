import pygame, time, math, random

class nao_gol(pygame.sprite.Sprite):
    def __init__(self, top, left, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top

class Placar():
    def __init__(self):
        self.display = pygame.image.load('img/Placar.png')
        self.placardireito = pygame.image.load('img/saldo00.png')
        self.placaresquerdo = pygame.image.load('img/saldo00.png')
        
    def updatePlacarDireito(self, valor):
        if valor == 0:
            self.placardireito = pygame.image.load('img/saldo00.png') 
        if valor == 1:
            self.placardireito = pygame.image.load('img/saldo01.png')
        if valor == 2:
            self.placardireito = pygame.image.load('img/saldo02.png')
        if valor == 3:
            self.placardireito = pygame.image.load('img/saldo03.png')
        if valor == 4:
            self.placardireito = pygame.image.load('img/saldo04.png')
        if valor == 5:
            self.placardireito = pygame.image.load('img/saldo05.png')
            
    def updatePlacarEsquerdo(self, valor):
        if valor == 0:
            self.placaresquerdo = pygame.image.load('img/saldo00.png')
        if valor == 1:
            self.placaresquerdo = pygame.image.load('img/saldo01.png')
        if valor == 2:
            self.placaresquerdo = pygame.image.load('img/saldo02.png')
        if valor == 3:
            self.placaresquerdo = pygame.image.load('img/saldo03.png')
        if valor == 4:
            self.placaresquerdo = pygame.image.load('img/saldo04.png')
        if valor == 5:
            self.placaresquerdo = pygame.image.load('img/saldo05.png')
                                    
                                                     
class Humano(pygame.sprite.Sprite):
    def __init__(self, lista, posicaox, posicaoy, anim_colisao):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for x in range(0, len(lista)):
            self.images.append(pygame.image.load(lista[x]))
        self.rect = self.images[anim_colisao].get_rect()
        self.rect.x = posicaox
        self.rect.y = posicaoy
                    
class Goleiro(Humano):
    def __init__(self, lista, posicaox, posicaoy, anim_colisao):
        super().__init__(lista, posicaox, posicaoy, anim_colisao)
        self.index = 0
        self.image = self.images[self.index]

    def update(self, avancox, avancoy):
        self.index += 1
        self.rect.x += avancox
        self.rect.y += avancoy
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]     


class Jogador(Humano):
    def __init__(self, lista, posicaox, posicaoy, anim_colisao):
        super().__init__(lista, posicaox, posicaoy, anim_colisao)
        self.index = 0
        self.image = self.images[self.index]

    def update(self, avancox, avancoy):
        self.index += 1
        self.rect.x += avancox
        self.rect.y += avancoy
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index] 

class Bola(pygame.sprite.Sprite):  
    def __init__(self, imgbola):
        pygame.sprite.Sprite.__init__(self)
        self.imgbola = pygame.image.load(imgbola)
        self.rect = self.imgbola.get_rect()
        self.rect.x = 426
        self.rect.y = 365

    def move(self, passo):
        self.rect = self.rect.move(passo)

    def dist_euclidiana(self, pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

pygame.init()

#_________CONFIGURAÇÕES___________
tela = pygame.display.set_mode([900, 459])
pygame.display.set_caption("Game of penalty")
campo = pygame.image.load('img/campo.png')
torcidas = pygame.mixer.Sound('torcida.ogg')
cuadrado = pygame.mixer.Sound('cuadrado.ogg')
ronaldo = pygame.mixer.Sound('ronaldo.ogg')
robben = pygame.mixer.Sound('robben.ogg')
messi = pygame.mixer.Sound('messi.ogg')

#_________MENUS___________
foto_menu = pygame.image.load('img/menuprincipal.png')
escolha_time = pygame.image.load('img/escolhajogador.png')
escolhajogador1 = pygame.image.load('img/escolhaJogador1.png')
escolhajogador2 = pygame.image.load('img/escolhaJogador2.png')
        
        #_________MEUS SPRITES___________
retangulo1 = nao_gol(0, 0, 'img/ret1.png')
retangulo2 = nao_gol(0, 718, 'img/ret2.png')
retangulo3 = nao_gol(0, 168, 'img/ret3.png')
sprite_goleiro_sup_direito = ['img/sprites/goleiro.png','img/sprites/goleirosupdireito.png', 'img/sprites/goleirosupdireito2.png', 'img/sprites/goleirosupdireito3.png']
sprite_goleiro_sup_esquerdo = ['img/sprites/goleiro.png','img/sprites/goleirosupesquerdo.png', 'img/sprites/goleirosupesquerdo2.png', 'img/sprites/goleirosupesquerdo3.png']
sprite_goleiro_inf_direito = ['img/sprites/goleiro.png','img/sprites/goleiroinfdireito.png', 'img/sprites/goleiroinfdireito2.png', 'img/sprites/goleiroinfdireito3.png']
sprite_goleiro_inf_esquerdo = ['img/sprites/goleiro.png','img/sprites/goleiroinfesquerdo.png', 'img/sprites/goleiroinfesquerdo2.png', 'img/sprites/goleiroinfesquerdo3.png']
sprite_goleiro_meio_alto = ['img/sprites/goleiro.png','img/sprites/goleiromeioalto.png', 'img/sprites/goleiromeioalto.png', 'img/sprites/goleiromeioalto.png']
sprite_goleiro_meio_baixo = ['img/sprites/goleiro.png','img/sprites/goleiromeiobaixo.png', 'img/sprites/goleiromeiobaixo.png', 'img/sprites/goleiromeiobaixo.png']
sprite_messi = ['img/messi1.png', 'img/messi2.png', 'img/messi3.png']
sprite_robben = ['img/robben1.png', 'img/robben2.png', 'img/robben3.png']
sprite_cuadrado = ['img/cuadrado1.png', 'img/cuadrado2.png', 'img/cuadrado3.png']
sprite_cristiano = ['img/cristiano1.png', 'img/cristiano2.png', 'img/cristiano3.png']
mov_goleiro = [sprite_goleiro_sup_direito, sprite_goleiro_sup_esquerdo, sprite_goleiro_inf_direito, sprite_goleiro_inf_esquerdo, sprite_goleiro_meio_alto,sprite_goleiro_meio_baixo]

#_________MEUS OBJETOS___________
placar = Placar()

#_______EVENTOS (IMAGENS)______
gritoGol = pygame.image.load('img/gol.png')
gritoErrou = pygame.image.load('img/errou.png')
empate = pygame.image.load('img/empate.png')
winJogador1 = pygame.image.load('img/winjogador1.png')
winJogador2 = pygame.image.load('img/winjogador2.png')

#_________LISTA COLISÃO___________
block_list = pygame.sprite.Group()
block_list.add(retangulo1)
block_list.add(retangulo2)
block_list.add(retangulo3)

#_________MINHAS VARIAVEIS___________
sair = True
clique_play = False
clock = pygame.time.Clock()

#_________JOGO___________
while sair:
    escolha1 = False
    escolha2 = False
    player1 = 0
    player2 = 0
    escolha_goleiro = []
    goleiro_updateX = 0
    goleiro_updateY = 0
    attPlacarDireito = 0
    attPlacarEsquerdo = 0
    jogarnovamente = False
    torcidas.play()
    while not clique_play:
        for event in pygame.event.get():
            tela.blit(foto_menu, (0, 0))
            pygame.display.update()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos_clique = pygame.mouse.get_pos()
                if ((pos_clique[0] >= 346 and pos_clique[0] <= 553) and (pos_clique[1] >= 148 and pos_clique[1] <= 198)):
                    clique_play = True
                elif ((pos_clique[0] >= 346 and pos_clique[0] <= 553) and (pos_clique[1] >= 230 and pos_clique[1] <= 280)):
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
    torcidas.stop()               
    while (not escolha1):
        for event in pygame.event.get():
            tela.blit(escolha_time, (0, 0))
            tela.blit(escolhajogador1, (311, 42))
            pygame.display.update()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos_clique = pygame.mouse.get_pos()
                #_________CUADRADO___________
                if ((pos_clique[0] >= 136 and pos_clique[0] <= 230) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    cuadrado.play()
                    jogador = Jogador(sprite_cuadrado, 380, 200, 0)
                    animJogador = pygame.sprite.Group(jogador)
                    escolha1 = True
                #_________CRISTIANO RONALDO___________
                if ((pos_clique[0] >= 315 and pos_clique[0] <= 409) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    ronaldo.play()
                    jogador = Jogador(sprite_cristiano, 380, 200, 0)
                    animJogador = pygame.sprite.Group(jogador)
                    escolha1 = True
                #_________ROBBEN___________
                if ((pos_clique[0] >= 492 and pos_clique[0] <= 592) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    robben.play()
                    jogador = Jogador(sprite_robben, 380, 200, 0)
                    animJogador = pygame.sprite.Group(jogador)
                    escolha1 = True
                #_________MESSI___________
                if ((pos_clique[0] >= 673 and pos_clique[0] <= 770) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    messi.play()
                    jogador = Jogador(sprite_messi, 380, 200, 0)
                    animJogador = pygame.sprite.Group(jogador)
                    escolha1 = True
                if event.type == pygame.QUIT:
                    pygame.quit()

    while (not escolha2):
        for event in pygame.event.get():
            tela.blit(escolha_time, (0, 0))
            tela.blit(escolhajogador2, (311, 42))
            pygame.display.update()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos_clique = pygame.mouse.get_pos()
                #_________CUADRADO___________
                if ((pos_clique[0] >= 136 and pos_clique[0] <= 230) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    cuadrado.play()
                    jogador2 = Jogador(sprite_cuadrado, 380, 200, 0)
                    animJogador2 = pygame.sprite.Group(jogador2)
                    escolha2 = True
                #_________CRISTIANO RONALDO___________
                if ((pos_clique[0] >= 315 and pos_clique[0] <= 409) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    ronaldo.play()
                    jogador2 = Jogador(sprite_cristiano, 380, 200, 0)
                    animJogador2 = pygame.sprite.Group(jogador2)
                    escolha2 = True
                #_________ROBBEN___________
                if ((pos_clique[0] >= 492 and pos_clique[0] <= 592) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    robben.play()
                    jogador2 = Jogador(sprite_robben, 380, 200, 0)
                    animJogador2 = pygame.sprite.Group(jogador2)
                    escolha2 = True
                #_________MESSI___________
                if ((pos_clique[0] >= 673 and pos_clique[0] <= 770) and (pos_clique[1] >= 127 and pos_clique[1] <= 300)):
                    messi.play()
                    jogador2 = Jogador(sprite_messi, 380, 200, 0)
                    animJogador2 = pygame.sprite.Group(jogador2)
                    escolha2 = True
                if event.type == pygame.QUIT:
                    pygame.quit()
    #________________________________________JOGADOR 1_________________________________________________#
    for x in range(1, 6):
        clique_gol = False
        pos = [0, 0]
        bola = Bola('img/bola.png')
        gol = False
        fim_bola = False
        goleiro = False
        while not fim_bola:
            clock.tick(5)
            #_______RANDOMICO GOLEIRO_________
            if not goleiro:
                escolha_goleiro = random.choice(mov_goleiro)
                goleiro = Goleiro(escolha_goleiro, 398, 60, 3)
                goleiro_colid = goleiro
                animGoleiro = pygame.sprite.Group(goleiro)
                if escolha_goleiro == mov_goleiro[0]:
                    goleiro_updateX = 40
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[1]:
                    goleiro_updateX = -63
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[2]:
                    goleiro_updateX = 40
                    goleiro_updateY = 18
                if escolha_goleiro == mov_goleiro[3]:
                    goleiro_updateX = -63
                    goleiro_updateY = 18
                if escolha_goleiro == mov_goleiro[4]:
                    goleiro_updateX = -5
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[5]:
                    goleiro_updateX = -5
                    goleiro_updateY = 10
                block_list.add(goleiro_colid)
                print(block_list)
                goleiro = True
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if (event.type == pygame.MOUSEBUTTONDOWN) and (not clique_gol):
                    pos = pygame.mouse.get_pos()
                    if pos[1] >= 0 and pos[1] <= 178:
                        passo = []
                        passo.append(pos[0] - bola.rect.x)
                        passo.append(pos[1] - bola.rect.y)
                        passo[0] /= 3
                        passo[1] /= 3
                        clique_gol = True
            if (clique_gol) and (bola.dist_euclidiana([bola.rect.x,bola.rect.y],pos) > 20.5):
                bola.move(passo)
                #_________ATUALIZANDO O SPRITE__________
                animGoleiro.update(goleiro_updateX, goleiro_updateY)
                animJogador.update(0, 0)
            elif ((bola.dist_euclidiana([bola.rect.x,bola.rect.y],pos) <= 20.5)):
                fim_bola = True
                blocks_hit_list = pygame.sprite.spritecollide(bola, block_list, False)
                if blocks_hit_list == []:
                    player1 = 1 + player1
                    gol = True
                    blocks_hit_list = []
                    
            #_________DESENHANDO NA TELA________
            tela.blit(campo, (0, 0))
            tela.blit(retangulo1.image, retangulo1.rect)
            tela.blit(retangulo2.image, retangulo2.rect)
            tela.blit(retangulo3.image, retangulo3.rect)
            tela.blit(placar.display, (24, 307))
            tela.blit(placar.placardireito , (70, 372))
            tela.blit(placar.placaresquerdo, (147, 372))
            placar.updatePlacarEsquerdo(attPlacarEsquerdo)
            placar.updatePlacarDireito(attPlacarDireito)
            animGoleiro.draw(tela)
            tela.blit(bola.imgbola, bola.rect)
            animJogador.draw(tela)
            
            #_________ATUALIZANDO O PLACAR________
            if gol:
                attPlacarDireito += 1
            pygame.display.update()
            if fim_bola:
                tela.blit(campo, (0, 0))
                tela.blit(retangulo1.image, retangulo1.rect)
                tela.blit(retangulo2.image, retangulo2.rect)
                tela.blit(retangulo3.image, retangulo3.rect)
                tela.blit(placar.display, (24, 307))
                placar.updatePlacarEsquerdo(attPlacarEsquerdo)
                placar.updatePlacarDireito(attPlacarDireito)
                tela.blit(placar.placardireito , (70, 372))
                tela.blit(placar.placaresquerdo, (147, 372))
                animGoleiro.draw(tela)
                tela.blit(bola.imgbola, bola.rect)
                animJogador.draw(tela)
                if gol:
                    tela.blit(gritoGol, (249, 136))
                else:
                    tela.blit(gritoErrou,(176, 152))
                block_list.remove(goleiro_colid)
                pygame.display.update()
                time.sleep(2)
#________________________________________JOGADOR 2_________________________________________________#
        clique_gol = False
        pos = [0, 0]
        bola = Bola('img/bola.png')
        gol = False
        fim_bola = False
        goleiro = False
        
        while not fim_bola:     
            clock.tick(5)
            #_______RANDOMICO GOLEIRO_________
            if not goleiro:
                escolha_goleiro = random.choice(mov_goleiro)
                goleiro = Goleiro(escolha_goleiro, 398, 60, 3)
                goleiro_colid = goleiro
                animGoleiro = pygame.sprite.Group(goleiro)
                if escolha_goleiro == mov_goleiro[0]:
                    goleiro_updateX = 40
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[1]:
                    goleiro_updateX = -63
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[2]:
                    goleiro_updateX = 40
                    goleiro_updateY = 18
                if escolha_goleiro == mov_goleiro[3]:
                    goleiro_updateX = -63
                    goleiro_updateY = 18
                if escolha_goleiro == mov_goleiro[4]:
                    goleiro_updateX = -5
                    goleiro_updateY = -10
                if escolha_goleiro == mov_goleiro[5]:
                    goleiro_updateX = -5
                    goleiro_updateY = 10
                block_list.add(goleiro_colid)
                goleiro = True
                            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if (event.type == pygame.MOUSEBUTTONDOWN) and (not clique_gol):
                    pos = pygame.mouse.get_pos()
                    if pos[1] >= 0 and pos[1] <= 178:
                        passo = []
                        passo.append(pos[0] - bola.rect.x)
                        passo.append(pos[1] - bola.rect.y)
                        passo[0] /= 3
                        passo[1] /= 3
                        clique_gol = True
            if (clique_gol) and (bola.dist_euclidiana([bola.rect.x,bola.rect.y],pos) > 20.5):
                bola.move(passo)
                #_________ATUALIZANDO O SPRITE__________
                animGoleiro.update(goleiro_updateX, goleiro_updateY)
                animJogador2.update(0, 0)
            elif ((bola.dist_euclidiana([bola.rect.x,bola.rect.y],pos) <= 20.5)):
                fim_bola = True
                blocks_hit_list = pygame.sprite.spritecollide(bola, block_list, False)
                if blocks_hit_list == []:
                    gol = True
                    player2 = 1 + player2
                else:
                    blocks_hit_list = []
            #_________DESENHANDO NA TELA________
            tela.blit(campo, (0, 0))
            tela.blit(retangulo1.image, retangulo1.rect)
            tela.blit(retangulo2.image, retangulo2.rect)
            tela.blit(retangulo3.image, retangulo3.rect)
            tela.blit(placar.display, (24, 307))
            tela.blit(placar.placardireito , (70, 372))
            tela.blit(placar.placaresquerdo, (147, 372))
            placar.updatePlacarEsquerdo(attPlacarEsquerdo)
            placar.updatePlacarDireito(attPlacarDireito)
            animGoleiro.draw(tela)
            tela.blit(bola.imgbola, bola.rect)
            animJogador2.draw(tela)
            #_________ATUALIZANDO O PLACAR________
            if gol:
                attPlacarEsquerdo += 1
            pygame.display.update()
            if fim_bola:
                tela.blit(campo, (0, 0))
                tela.blit(retangulo1.image, retangulo1.rect)
                tela.blit(retangulo2.image, retangulo2.rect)
                tela.blit(retangulo3.image, retangulo3.rect)
                tela.blit(placar.display, (24, 307))
                placar.updatePlacarEsquerdo(attPlacarEsquerdo)
                placar.updatePlacarDireito(attPlacarDireito)
                tela.blit(placar.placardireito , (70, 372))
                tela.blit(placar.placaresquerdo, (147, 372))
                animGoleiro.draw(tela)
                tela.blit(bola.imgbola, bola.rect)
                animJogador2.draw(tela)
                if gol:
                    tela.blit(gritoGol, (249, 136))
                else:
                    tela.blit(gritoErrou,(176, 152))
                block_list.remove(goleiro_colid)
                if player1 == player2 and x == 5:
                    tela.blit(empate, (0, 0))
                    jogarnovamente = True
                if player1 > player2 and x == 5:
                    tela.blit(winJogador1, (0, 0))
                    jogarnovamente = True
                if player1 < player2 and x == 5:
                    tela.blit(winJogador2, (0, 0))
                    jogarnovamente = True
                pygame.display.update()
                time.sleep(2)
                while jogarnovamente:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if (event.type == pygame.MOUSEBUTTONDOWN):
                            pos_clique = pygame.mouse.get_pos()
                            if (pos_clique[0] >= 311) and (pos_clique[0] <= 590) and (pos_clique[1] >= 278) and (pos_clique[1] <= 336):
                                jogarnovamente = False
                            if (pos_clique[0] >= 311) and (pos_clique[0] <= 590) and (pos_clique[1] >= 347) and (pos_clique[1] <= 405):
                                pygame.quit()                                        
    escolha1 = False
    escolha2 = False
pygame.quit()
