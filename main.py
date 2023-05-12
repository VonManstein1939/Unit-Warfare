import pygame, sys

pygame.init()

screen = pygame.display.set_mode((715, 400))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill(pygame.Color('black'))
test_rect = test_surface.get_rect(center=(200, 250))
class Button(pygame.sprite.Sprite):
    def_

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    screen.blit(test_surface, test_rect)

    pygame.display.update()
    clock.tick(60)
    img = pygame.image.load("Start_button_for_email-removebg-preview.png")