import pygame

pygame.init()

LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))


largura_tijolo = 60
altura_tijolo = 20 
colunas = 8 
linhas = 4
tijolos = []

raquete = pygame.Rect(250,360, 100, 15)
velocidade_raquete = 4

bola = pygame.Rect(LARGURA// 2, ALTURA// 2,10,10)
bola_dx = 1
bola_dy = -1

for linha in range(linhas):
    for coluna in range(colunas) :
        x = coluna *(largura_tijolo + 5) + 35
        y = linha * (altura_tijolo + 5) +50 
       
        novo_tijolo = pygame.Rect(x, y, largura_tijolo, altura_tijolo)
        tijolos.append(novo_tijolo)
pygame.display.set_caption("Breakout")

relogio = pygame.time.Clock()

rodando = True
while rodando: 
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
 
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and raquete.left > 0:
        raquete.x -= velocidade_raquete
    
    if teclas[pygame.K_RIGHT] and raquete.right < LARGURA: 
        raquete.x += velocidade_raquete

    bola.x += bola_dx
    bola.y += bola_dy

    if bola.left <=0 or bola.right >= LARGURA:
        bola_dx *= -1

    
    if bola.top <= 0:
        bola_dy *= -1
 
    if bola.colliderect(raquete):
        bola_dy *= -1
        bola.bottom = raquete.top

    for t in tijolos [:] :
     if bola.colliderect(t):
         tijolos.remove(t)
         bola_dy *= -1
         break

    tela.fill((0, 0, 0))



    for t in tijolos: 
     
     pygame.draw.rect(tela, (255, 0, 0), t)
    pygame.draw.rect(tela, (255, 255, 255), raquete)
    pygame.draw.ellipse(tela, (255, 255, 255), bola)
    pygame.display.flip() 

pygame.quit()