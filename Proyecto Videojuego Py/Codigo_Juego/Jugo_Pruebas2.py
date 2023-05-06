import pygame

pygame.init()

ancho_v= 1000
alto_v =600
v_juego = pygame.display.set_mode((ancho_v, alto_v))

pygame.display.set_caption("4 Paises Una Bandera (Pantalla Principal)")

font = pygame.font.SysFont('Arial', 40, bold = True)
surf = font.render('Jugar', True, 'white')
button = pygame.Rect(200, 200, 110, 60)

while True: 
    v_juego.fill('pink')
    for events in pygame.event.get():
        if events.type == pygame.QUIT:  
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pygame.draw.rect(v_juego, (180, 180, 180), button)
    else:
        pygame.draw.rect(v_juego, (110, 110, 110), button)
    v_juego.blit(surf, (button.x +5, button.y +5))
    
    pygame.display.update()
            