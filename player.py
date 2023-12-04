import pygame

class Player:
    def __init__(self, screen_width, screen_height, normal_sprite_sheet, hurt_sprite_sheet, run_sprite_sheet, jump_sprite_sheet, columns, scale):
        normal_sprite = pygame.image.load(normal_sprite_sheet)
        hurt_sprite = pygame.image.load(hurt_sprite_sheet)
        run_sprite = pygame.image.load(run_sprite_sheet)
        jump_sprite = pygame.image.load(jump_sprite_sheet)
        self.normal_sprite_sheet = pygame.transform.scale(normal_sprite,(normal_sprite.get_width() * scale, normal_sprite.get_height() * scale))
        self.hurt_sprite_sheet = pygame.transform.scale(hurt_sprite,(hurt_sprite.get_width() * scale, hurt_sprite.get_height() * scale))
        self.run_sprite_sheet = pygame.transform.scale(run_sprite, (run_sprite.get_width() * scale, run_sprite.get_height() * scale))
        self.jump_sprite_sheet = pygame.transform.scale(jump_sprite, (jump_sprite.get_width() * scale, jump_sprite.get_height() * scale))

        self.rect = pygame.Rect(0, 0, self.normal_sprite_sheet.get_width() // columns, self.normal_sprite_sheet.get_height())
        self.rect.topleft = (screen_width // 2, screen_height // 2)

        self.frame_width = self.normal_sprite_sheet.get_width() // columns
        self.frame_height = self.normal_sprite_sheet.get_height()
        self.columns = columns
        self.current_frame = 0

        self.is_hurt = False
        self.hurt_duration = 20
        self.is_run = False
        self.run_duration = 50
        self.is_jump = False
        self.jump_duration = 30
    def update_animation(self):
        self.current_frame = (self.current_frame + 1) % self.columns

        if self.is_hurt:
            self.hurt_duration -= 1
            if self.hurt_duration <= 0:
                self.is_hurt = False
                self.hurt_duration = 20    
        if self.is_run:
            self.run_duration -= 1
            self.rect = (self.rect[0] + 10, self.rect[1])
            if self.run_duration <= 0:
                self.is_run = False
                self.run_duration = 50
        if self.is_jump:
            self.is_run = False
            self.jump_duration -= 1
            self.rect = (self.rect[0], self.rect[1] - 1)
            if self.jump_duration <= 0:
                self.is_jump = False
                self.jump_duration = 30
                self.rect = (self.rect[0], self.rect[1] + 30)

    def play_hurt_animation(self):
        self.is_hurt = True
        self.hurt_duration = 20
    def play_run_animation(self):
        self.is_run = True
        self.run_duration = 50
    def play_jump_animation(self):
        self.is_jump = True

    def draw(self, screen):
        if self.is_hurt:
            sprite_sheet = self.hurt_sprite_sheet
        elif self.is_run:
            sprite_sheet = self.run_sprite_sheet
        elif self.is_jump:
            sprite_sheet = self.jump_sprite_sheet
        else:
            sprite_sheet = self.normal_sprite_sheet
        frame_x = self.current_frame * self.frame_width
        frame_rect = pygame.Rect(frame_x, 0, self.frame_width, self.frame_height)
        screen.blit(sprite_sheet, self.rect, frame_rect)
