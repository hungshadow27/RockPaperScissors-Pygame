import pygame
class Skill():
    def __init__(self, screen_width, screen_height, normal_sprite_sheet, columns, scale):
        normal_sprite = pygame.image.load(normal_sprite_sheet)
        self.normal_sprite_sheet = pygame.transform.scale(normal_sprite,(normal_sprite.get_width() * scale, normal_sprite.get_height() * scale))

        self.rect = pygame.Rect(0, 0, self.normal_sprite_sheet.get_width() // columns, self.normal_sprite_sheet.get_height())
        self.rect.topleft = (screen_width // 2, screen_height // 2)
        self.frame_width = self.normal_sprite_sheet.get_width() // columns
        self.frame_height = self.normal_sprite_sheet.get_height()
        self.columns = columns
        self.current_frame = 0
        self.lifespan = 30  # Number of frames the particle will exist
        self.isdraw = False

    def update_animation(self, xval, yval):
        self.current_frame = (self.current_frame + 1) % self.columns
        self.lifespan -= 1
        self.rect = (self.rect[0] - xval, self.rect[1] - yval)  # Adjust the speed by changing the first value
        if self.lifespan <= 0:
            self.isdraw = False

    def play_skill_animation(self):
        self.isdraw = True
        self.lifespan = 30

    def draw(self, screen):
        if self.isdraw:
            sprite_sheet = self.normal_sprite_sheet
            frame_x = self.current_frame * self.frame_width
            frame_rect = pygame.Rect(frame_x, 0, self.frame_width, self.frame_height)
            screen.blit(sprite_sheet, self.rect, frame_rect)
            

        
