import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.options = ["Gravitation", "Pendel"]
        self.hover_index = 0

    def run(self, event):
        pygame.display.set_caption("PyPhySim - Menü")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.hover_index = (self.hover_index + 1) % len(self.options)
        elif keys[pygame.K_UP]:
            self.hover_index = (self.hover_index - 1) % len(self.options)
        elif keys[pygame.K_RETURN]:
            return self.options[self.hover_index]

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i != self.hover_index else (0, 255, 0)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (100, 100 + i * 60))

        return None