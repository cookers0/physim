import pygame

class Button:
    def __init__(self, text, pos, size, font, color_normal, color_hover):
        self.text = text
        self.pos = pos
        self.size = size
        self.font = font
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.rect = pygame.Rect(pos, size)
        self.hovered = False

    def draw(self, screen):

        color = self.color_normal
        if self.hovered:
            color = self.color_hover
        else:
            color = self.color_normal
        
        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            return self.rect.collidepoint(event.pos)
        return False

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.title_font = pygame.font.SysFont(None, 72)
        self.options = ["Gravitation", "Pendel"]
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        start_y = 200
        for i, option in enumerate(self.options):
            button = Button(
                text=option,
                pos=(300, start_y + i * 80),
                size=(200, 50),
                font=self.font,
                color_normal=(200, 200, 200),
                color_hover=(100, 255, 100),
            )
            self.buttons.append(button)
    
    def draw_title(self):
        title_rect = pygame.Rect(200, 50, 400, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), title_rect, border_radius=12)

        title_surf = self.title_font.render("PyPhySim", True, (255, 255, 255))
        title_text_rect = title_surf.get_rect(center=title_rect.center)
        self.screen.blit(title_surf, title_text_rect)

    def run(self, event):
        pygame.display.set_caption("PyPhySim - Menü")
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            button.update(mouse_pos)
            if event and button.is_clicked(event):
                return button.text
        
        self.draw_title()

        for button in self.buttons:
            button.draw(self.screen)

        return None