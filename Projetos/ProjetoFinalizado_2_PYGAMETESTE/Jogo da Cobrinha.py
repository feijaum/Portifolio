import pygame as pg
import random as rd


largura = 640
altura = 480

tamanho = 10

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

try:
    pg.init()
    print("Deu tudo certo")
except:
    print("algo de errado nao esta certo")

relogio = pg.time.Clock()

fundo = pg.display.set_mode((largura,altura))
pg.display.set_caption("Jogo Do Cobrão")
font = pg.font.SysFont(None, 20, False)
fonte = pg.font.SysFont(None, 30, False)

def textogo(msg, cor):
    textogo= fonte.render(msg, True, cor)
    fundo.blit(textogo, (largura/2, 200))

def texto(msg, cor):
    texto1= font.render(msg, True, cor)
    fundo.blit(texto1, (largura/2, altura/2))

def cobra(CobraXY):
    for XY in CobraXY:
        pg.draw.rect(fundo, azul, (XY[0], XY[1], tamanho, tamanho))

def maca(pos_x,pos_y):
    pg.draw.rect(fundo, vermelho, (pos_x, pos_y, tamanho, tamanho))

def placar(pontos,cor):
    pontos = fonte.render(pontos, True, cor)
    fundo.blit(pontos, (largura / 2, 70))

def jogo():

    sair = True

    pos_x = rd.randrange(0,(largura - tamanho),10)
    pos_y = rd.randrange(0,(altura - tamanho), 10)
    pos_mx = rd.randrange(0, (largura - tamanho) , 10)
    pos_my = rd.randrange(0, (altura - tamanho) , 10)

    velocidade_x = 0
    velocidade_y = 0

    CobraXY = []
    CobraComp = 1

    fimdejogo = False
    pontostotal = 0



    while sair:



        while fimdejogo:
            fundo.fill(branco)
            textogo(f"FIM DE JOGO", vermelho)
            texto(f"Para continuar tecle C ou S para sair", preto)
            pg.display.update()
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    sair = False
                    fimdejogo= False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        sair = True

                        pos_x = rd.randrange(0, (largura - tamanho), 10)
                        pos_y = rd.randrange(0, (altura - tamanho), 10)
                        pos_mx = rd.randrange(0, (largura - tamanho), 10)
                        pos_my = rd.randrange(0, (altura - tamanho), 10)

                        velocidade_x = 0
                        velocidade_y = 0

                        CobraXY = []
                        CobraComp = 1
                        pontostotal = 0

                        fimdejogo = False
                    if event.key == pg.K_s:
                        sair= False
                        fimdejogo= False


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sair = False

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = + tamanho

                if event.key == pg.K_LEFT and velocidade_x != tamanho :
                    velocidade_y = 0
                    velocidade_x = - tamanho

                if event.key == pg.K_DOWN and velocidade_y != -tamanho :
                    velocidade_y = + tamanho
                    velocidade_x = 0

                if event.key == pg.K_UP and velocidade_y != tamanho :
                    velocidade_y = - tamanho
                    velocidade_x = 0
                if event.key == pg.K_SPACE :
                    velocidade_y = 0
                    velocidade_x = 0
                if event.key == pg.K_ESCAPE :
                    sair = False
        if pos_x == pos_mx and pos_y == pos_my:

            pontostotal +1
            pg.display.update()




        if sair:

            fundo.fill(preto)

            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x == pos_mx and pos_y == pos_my:
                pos_mx = rd.randrange(0, (largura - tamanho), 10)
                pos_my = rd.randrange(0, (altura - tamanho), 10)
                CobraComp += 1
                pontostotal +=1

            if pos_x + tamanho>= largura:
                pos_x = 0 + velocidade_x
            if pos_x <= 0:
                pos_x = largura + velocidade_x
            if pos_y +tamanho>= altura:
                pos_y = 0 + velocidade_y
            if pos_y <= 0:
                pos_y = 480 + velocidade_y


            CobraInicio = []
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo= True



            cobra(CobraXY)





            maca(pos_mx,pos_my)



            relogio.tick(15)

            placar("Placar:"+ str(pontostotal), branco)

            pg.display.update()


jogo()
pg.quit()