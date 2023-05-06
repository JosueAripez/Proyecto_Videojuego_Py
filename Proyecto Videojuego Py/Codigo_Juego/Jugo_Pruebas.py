# Main
import pygame

# Inicializando
pygame.init()

# Creando ventana del juego
ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))

# Titulo de la ventana
pygame.display.set_caption("4 Paises 1 Bandera") 

# Funcion para dibujado de texto

font = pygame.font.SysFont("arial", 50)

text_color = (0, 0, 255)

def escirbe_texto(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    ventana.blit(image,(x, y))

# Bucle principal, se comprube a si estan pasando los sucesos
jugando = True
while jugando: 
    
    for event in pygame.event.get():
        # Verificamos si se cerro la ventana
        if event.type == pygame.QUIT:  
            jugando = False
    
    # Borrando elemntos que se tenian 
    ventana.fill((255, 255, 255)) 
    
    # Escribiendo texto
    escirbe_texto("BIENVENIDO A NUESTRO JUEGO", font, text_color, 160, 250)
    
    # Dar color a la ventana
    ventana.fill("black") 
    
    # Fondo de la ventana
    fondo = pygame.image.load("Proyecto Videojuego Py/imagenes/fondo_banderas.jpg").convert()
    ventana.blit(fondo,(0,0))
    
    # Icono de la ventana 
    icono = pygame.image.load("Proyecto Videojuego Py/imagenes/icono2.png").convert()
    pygame.display.set_icon(icono)
    
    pygame.display.flip()
    
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60) 

pygame.quit()