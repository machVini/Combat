import pygame

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
vermei = (134, 28,9)
amarelo = (212, 169, 65)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com suças")

largura = 970
altura = 640   
tamanho = 10
pos_x = largura/2
pos_y = altura/2

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Combat")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    fundo.fill(vermei)
    
    #BORDAS / CAMPO
    pygame.draw.rect(fundo, amarelo, [0, 50, largura, 20])
    pygame.draw.rect(fundo, amarelo, [0, 50, 20, altura])
    pygame.draw.rect(fundo, amarelo, [largura - 20, 50, 20, altura])
    pygame.draw.rect(fundo, amarelo, [0, altura - 20, largura, 20])

    pygame.draw.rect(fundo, amarelo, [largura/2 - 25, 70, 50, 50])
    pygame.draw.rect(fundo, amarelo, [largura/2 - 25, altura - 70, 50, 50])

    pygame.draw.rect(fundo, amarelo, [120, 150, 70, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 190, 150, 70, 20])
    pygame.draw.rect(fundo, amarelo, [120, altura - 120, 70, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 190, altura - 120, 70, 20])

    pygame.draw.rect(fundo, amarelo, [100, 240, 20, 20])
    pygame.draw.rect(fundo, amarelo, [100, 430, 20, 20])
    pygame.draw.rect(fundo, amarelo, [120, 240, 25, 210])
    pygame.draw.rect(fundo, amarelo, [largura - 120, 240, 20, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 120, 430, 20, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 145, 240, 25, 210])

    pygame.draw.rect(fundo, amarelo, [250, altura/2, 50, 50])
    pygame.draw.rect(fundo, amarelo, [largura - 295, altura/2, 50, 50])

    pygame.draw.rect(fundo, amarelo, [350, 200, 70, 20])
    pygame.draw.rect(fundo, amarelo, [350, 220, 20, 25])
    pygame.draw.rect(fundo, amarelo, [largura - 420, 200, 70, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 370, 220, 20, 25])
    pygame.draw.rect(fundo, amarelo, [350, altura - 180, 70, 20])
    pygame.draw.rect(fundo, amarelo, [350, altura - 200, 20, 25])
    pygame.draw.rect(fundo, amarelo, [largura - 420, altura - 180, 70, 20])
    pygame.draw.rect(fundo, amarelo, [largura - 370, altura - 200, 20, 25])

    pygame.display.update()

pygame.quit()
#quit()