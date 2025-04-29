import pygame
from Menu import Menu
from Gravitation import Simulation1
from Pendel import Simulation2

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
cdtransition = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if cdtransition == 0:
            if current_scene == "menu":
                selected = menu.run(event)
                if selected in simulations:
                    current_scene = selected
                    cdtransition = 15

    screen.fill((0, 0, 0))

    if current_scene == "menu":
        menu.run(None)
    else:
        if cdtransition == 0:
            back_to_menu = simulations[current_scene].run(event)
            if back_to_menu:
                current_scene = "menu"
                cdtransition = 15

    if cdtransition > 0:
        cdtransition -= 1

    pygame.display.update()
    clock.tick(60)

pygame.quit()