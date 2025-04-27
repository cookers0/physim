import pygame
from Menu import Menu
from Gravitation import Simulation1
from test import Simulation2

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
icon=pygame.image.load("IconSkaliert.png")
pygame.display.set_icon(icon)

# States
menu = Menu(screen)
simulations = {
    "Gravitation": Simulation1(screen),
    "Pendel": Simulation2(screen),
}
current_scene = "menu"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if current_scene == "menu":
        selected = menu.run(event)
        if selected in simulations:
            current_scene = selected
    else:
        sim = simulations[current_scene]
        back_to_menu = sim.run(event)
        if back_to_menu:
            current_scene = "menu"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()