import pygame
# Bucle de Inico (Pantalla Principal)

def Pantalla_Inicio():
    pygame.init()

    ancho_v= 1000
    alto_v =600
    v_juego = pygame.display.set_mode((ancho_v, alto_v))

    pygame.display.set_caption("4 Paises Una Bandera (Pantalla Principal)")

    font = pygame.font.SysFont('Arial', 40, bold = True)
    surf = font.render('Jugar', True, 'white')
    button = pygame.Rect(200, 200, 110, 60)

    while True: 
        # v_juego.fill('pink') Pinar el fondo
        
        fondo = pygame.image.load("Proyecto Videojuego Py/imagenes/fondo_banderas.jpg").convert()
        v_juego.blit(fondo,(0,0))
        icono = pygame.image.load("Proyecto Videojuego Py/imagenes/icono2.png").convert()
        pygame.display.set_icon(icono)
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:  
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(events.pos):
                    Pantalla_Inicio() 
                    pygame.quit()
        a,b = pygame.mouse.get_pos()
        if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
            pygame.draw.rect(v_juego, (180, 180, 180), button)
        else:
            pygame.draw.rect(v_juego, (110, 110, 110), button)
        v_juego.blit(surf, (button.x +5, button.y +5))

        
    
        pygame.display.update()
Pantalla_Inicio()
 
# Inicio Menu (Selector de continentes)

def Inicio_Menu():
    pygame.init()
    
    ancho_v= 1000
    alto_v =600
    ventana = pygame.display.set_mode((ancho_v, alto_v))

    pygame.display.set_caption("4 Paises Una Bandera (Inicio Menu)")
 
    jugando = True
    while jugando: 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                jugando = False
    
        ventana.fill((255, 255, 255)) 
    
        ventana.fill("black") 
    
        icono = pygame.image.load("Proyecto Videojuego Py/imagenes/icono2.png").convert()
        pygame.display.set_icon(icono)
        fondo = pygame.image.load("Proyecto Videojuego Py/imagenes/fondo_banderas.jpg").convert()
        ventana.blit(fondo,(0,0))
    
        pygame.display.flip()

        pygame.quit()