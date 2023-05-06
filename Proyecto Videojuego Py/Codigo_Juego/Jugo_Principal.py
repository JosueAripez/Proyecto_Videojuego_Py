import pygame

pygame.init() # Inicializando

ventana = pygame.display.set_mode((640,480)) # Crenado ventana de juego

pygame.display.set_caption("4 Paises Una Bandera") # Poniendo titulo a la ventana 

jugando = True
while jugando: # Bucle principal, se comprube a si estasn pasando los sucesos
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Verificamos si se cerro la ventana
            jugando = False
    
    
    ventana.fill((255, 255, 255)) # Borrando elemntos que se tenian 
    
    ventana.fill("black") # Dando color a la ventana
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(60) # Controlamos la frecuencia de refresco (FPS)

pygame.quit()