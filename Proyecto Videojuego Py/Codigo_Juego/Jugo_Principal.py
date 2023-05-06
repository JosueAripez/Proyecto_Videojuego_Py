# Main
import pygame

# Inicializando
pygame.init()

# Creando ventana del juego
ventana = pygame.display.set_mode((640,480))

# Titulo de la ventana
pygame.display.set_caption("4 Paises 1 Bandera") 

# Bucle principal, se comprube a si estan pasando los sucesos
jugando = True
while jugando: 
    
    for event in pygame.event.get():
        # Verificamos si se cerro la ventana
        if event.type == pygame.QUIT:  
            jugando = False
    
    # Borrando elemntos que se tenian 
    ventana.fill((255, 255, 255)) 
    
    # Dar color a la ventana
    ventana.fill("black") 
    
    # Fondo de la ventana
    fondo = pygame.image.load("Proyecto Videojuego Py/imagenes/fondo_banderas.jpg").convert()
    ventana.blit(fondo,(0,0))
    
    # Icono de la ventana 
    icono = pygame.image.load("Proyecto Videojuego Py/imagenes/icono.png").convert()
    pygame.display.set_icon(icono)
    
    pygame.display.flip()
    
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60) 

pygame.quit()