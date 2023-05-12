import pygame
pygame.init()

screen = pygame.display.set_mode((715, 400))
clock = pygame.time.Clock()


menu_surf = pygame.Surface((100, 200))
menu_surf.fill(pygame.Color(''))
menu_rect = menu_surf.get_rect(center = (200, 250))

start_button = pygame.image.load('start_image_button.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

  
    screen.fill((175, 215, 70))
    screen.blit(menu_surf, menu_rect)
    screen.blit("start_button.png", (200, 500))

  
    pygame.display.update()
    clock.tick(60)
