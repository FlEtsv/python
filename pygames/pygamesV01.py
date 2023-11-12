"""
juego circuito

"""
import pygame

width = 626
height = 626


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circuito Camion')
Fondo = pygame.image.load('./images/fondo_circuito.jpg')


#tamaño rectangulo
rect_width = 20
rect_height = 20
# coordenadas del cuadrado
x = 45
y = 220

# velocidad de movimiento
vel = 1
#musica
pygame.mixer.music.load('./Music/locked_out_of_heaven.ogg')
pygame.mixer.music.set_volume(0.7 )
pygame.mixer.music.play()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    if event.type == pygame.KEYDOWN:
            print('Teca pulsada: '+event.unicode)

            if event.key == pygame.K_q: # salimos con la tecla q
                running == False

            if event.key == pygame.K_LEFT:
                print('Movmiento izda')
                x -= vel

            if event.key == pygame.K_RIGHT:
                print('Movmiento drcha')                
                x += vel

            if event.key == pygame.K_UP:
                print('Movmiento arriba')
                y -= vel

            if  event.key == pygame.K_DOWN:
                print('Movmiento abajo')        
                y += vel

    screen.blit(Fondo,(0,0))
    
    pygame.draw.rect(screen, (255, 70, 0), (x, y, rect_width, rect_height))

    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     