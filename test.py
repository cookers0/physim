import pygame
    
class Simulation2:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def run(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True  # Signal to return to menu

        text = self.font.render("ich bin ein fan von eier", True, (255, 255, 255))
        self.screen.blit(text, (50, 50))
        return False