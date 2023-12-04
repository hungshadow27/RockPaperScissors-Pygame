import pygame
import sys
import random
import time
from player import Player
from skill import Skill


class RockSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\rock.png",
            columns=1,
            scale=1,
        )


class PaperSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\paper.png",
            columns=1,
            scale=1,
        )


class ScissorSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\scissor.png",
            columns=1,
            scale=1,
        )


class RockBotSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\rock_bot.png",
            columns=1,
            scale=1,
        )


class PaperBotSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\paper_bot.png",
            columns=1,
            scale=1,
        )


class ScissorBotSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\scissor_bot.png",
            columns=1,
            scale=1,
        )


class BotSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\botskill.png",
            columns=4,
            scale=5,
        )


class PlayerSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\playerskill.png",
            columns=4,
            scale=5,
        )


class SawSkill(Skill):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\On (38x38).png",
            columns=8,
            scale=5,
        )


class MainPlayer(Player):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\Idle (32x32).png",
            hurt_sprite_sheet=r"img\Hit (32x32).png",
            run_sprite_sheet=r"img\Run (32x32).png",
            jump_sprite_sheet=r"img\Wall Jump (32x32).png",
            columns=11,
            scale=5,
        )


class BotEasyPlayer(Player):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\Idle (36x36).png",
            hurt_sprite_sheet=r"img\Hit (36x36).png",
            run_sprite_sheet=r"img\On (38x38).png",
            jump_sprite_sheet=r"img\Jump Anticipation (36x36).png",
            columns=10,
            scale=5,
        )
class BotNormalPlayer(Player):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\Idle (34x44).png",
            hurt_sprite_sheet=r"img\Hit (34x44).png",
            run_sprite_sheet=r"img\On (38x38).png",
            jump_sprite_sheet=r"img\Run (34x44).png",
            columns=8,
            scale=5,
        )        
class BotHardPlayer(Player):
    def __init__(self, screen_width, screen_height):
        super().__init__(
            screen_width,
            screen_height,
            normal_sprite_sheet=r"img\Idle (36x30).png",
            hurt_sprite_sheet=r"img\Hit 2 (36x30).png",
            run_sprite_sheet=r"img\On (38x38).png",
            jump_sprite_sheet=r"img\Run (36x30).png",
            columns=9,
            scale=5,
        )   


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (199, 220, 167)

# Game states
MENU = 0
PLAYING = 1
VICTORY = 2
DEFEAT = 3

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Core Game")
clock = pygame.time.Clock()
heart_img = pygame.image.load(r"img\heart.png")
#load sound
pygame.mixer.init()
hand = pygame.mixer.Sound(r"sound\hand.wav")
playerhurt = pygame.mixer.Sound(r"sound\hurtplayer.wav")
bothurt = pygame.mixer.Sound(r"sound\bosshurt.wav")
win = pygame.mixer.Sound(r"sound\yes.wav")
lose = pygame.mixer.Sound(r"sound\lose.wav")
pygame.mixer.music.load(
    r"sound\backgroundsound.mp3"
)  # Replace 'your_background_music.mp3' with the actual file path

# Play background music in an infinite loop
pygame.mixer.music.play(-1)
# Load images btn
original_3_image = pygame.image.load(r"img\3btn.png")
image_width = original_3_image.get_width()
image_height = original_3_image.get_height()
scissor_btn = original_3_image.subsurface(0, 0, image_width // 3, image_height)
rock_btn = original_3_image.subsurface(
    image_width // 3, 0, image_width // 3, image_height
)
paper_btn = original_3_image.subsurface(
    image_width - image_width // 3, 0, image_width // 3, image_height
)
# Fonts
font = pygame.font.Font(None, 36)

# Game variables
game_state = MENU
difficulty = None

# Create players
main_player = MainPlayer(WIDTH, HEIGHT)
main_player.rect = (30, 250)

saw_skill = SawSkill(WIDTH, HEIGHT)
saw_skill.rect = (WIDTH // 2, HEIGHT // 2)
player_skill = PlayerSkill(WIDTH, HEIGHT)
player_skill.rect = (WIDTH // 2, HEIGHT // 2)
bot_skill = BotSkill(WIDTH, HEIGHT)
bot_skill.rect = (WIDTH // 2, HEIGHT // 2)

#vi tri cua hand skill player
player_hand_skill = (300, 100)
rock_skill = RockSkill(WIDTH, HEIGHT)
rock_skill.rect = player_hand_skill
paper_skill = PaperSkill(WIDTH, HEIGHT)
paper_skill.rect = player_hand_skill
scissor_skill = ScissorSkill(WIDTH, HEIGHT)
scissor_skill.rect = player_hand_skill

#vi tri cua hand skill bot
bot_hand_skill = (WIDTH - 500, 100)
rock_bot_skill = RockBotSkill(WIDTH, HEIGHT)
rock_bot_skill.rect = bot_hand_skill
paper_bot_skill = PaperBotSkill(WIDTH, HEIGHT)
paper_bot_skill.rect = bot_hand_skill
scissor_bot_skill = ScissorBotSkill(WIDTH, HEIGHT)
scissor_bot_skill.rect = bot_hand_skill

is_skill_animation_playing = False
skill_animation_start_time = 0
is_run_animation_playing = False
run_animation_start_time = 0

# Skill
skill_cooldown = 2000  # in milliseconds (2 seconds)
last_skill_time = 0

main_player_hp = 10
bot_player_hp = 10


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Trigger hurt animation when the space bar is pressed
                saw_skill.rect = (500, 300)
                saw_skill.play_skill_animation()
                rock_skill.rect = (120, 250)
                rock_skill.play_skill_animation()
                # Record the start time of skill animation
                is_skill_animation_playing = True
                skill_animation_start_time = pygame.time.get_ticks()

    if (
        is_skill_animation_playing
        and pygame.time.get_ticks() - skill_animation_start_time >= 2000
    ):
        main_player.play_hurt_animation()
        bot_player.play_hurt_animation()
        is_skill_animation_playing = False  # Reset the flag

    # Main menu
    if game_state == MENU:
        screen.fill(GREEN)

        # Draw menu text
        text = font.render("Press any key to start", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        # Draw difficulty options
        easy_text = font.render("1 - Easy", True, BLACK)
        easy_rect = easy_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(easy_text, easy_rect)

        medium_text = font.render("2 - Normal", True, BLACK)
        medium_rect = medium_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(medium_text, medium_rect)

        hard_text = font.render("3 - Hard", True, BLACK)
        hard_rect = hard_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(hard_text, hard_rect)

        pygame.display.flip()

        # Check for key press to set difficulty and start game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            difficulty = "Easy"
            bot_player = BotEasyPlayer(WIDTH, HEIGHT)
            bot_player.rect = (WIDTH - 200, 240)
            main_player_hp = 10
            bot_player_hp = 5
            game_state = PLAYING
        elif keys[pygame.K_2]:
            difficulty = "Normal"
            bot_player = BotNormalPlayer(WIDTH, HEIGHT)
            bot_player.rect = (WIDTH - 200, 200)
            main_player_hp = 10
            bot_player_hp = 10
            game_state = PLAYING
        elif keys[pygame.K_3]:
            difficulty = "Hard"
            bot_player = BotHardPlayer(WIDTH, HEIGHT)
            bot_player.rect = (WIDTH - 200, 250)
            main_player_hp = 10
            bot_player_hp = 15
            game_state = PLAYING

    # Playing state
    elif game_state == PLAYING:
        main_player.rect = (30, 250)
        player_choice = ""
        computer_choice = ""
        keys = pygame.key.get_pressed()
        # Check if enough time has passed for the skill cooldown
        current_time = pygame.time.get_ticks()
        if current_time - last_skill_time >= skill_cooldown:
            # Perform skill action (for example, print a message)
            if keys[pygame.K_q]:
                player_choice = "rock"
                computer_choice = random.choice(["rock", "paper", "scissors"])
                rock_skill.play_skill_animation()
                hand.play()
            elif keys[pygame.K_w]:
                player_choice = "paper"
                computer_choice = random.choice(["rock", "paper", "scissors"])
                paper_skill.play_skill_animation()
                hand.play()

            elif keys[pygame.K_e]:
                player_choice = "scissors"
                computer_choice = random.choice(["rock", "paper", "scissors"])
                scissor_skill.play_skill_animation()
                hand.play()

            # bot skill
            if computer_choice == "rock":
                rock_bot_skill.play_skill_animation()
                last_skill_time = current_time
            elif computer_choice == "paper":
                paper_bot_skill.play_skill_animation()
                last_skill_time = current_time
            elif computer_choice == "scissors":
                scissor_bot_skill.play_skill_animation()
                last_skill_time = current_time
            winner = ""
            if player_choice == computer_choice:
                winner = ""
            elif (
                (player_choice == "rock" and computer_choice == "scissors")
                or (player_choice == "paper" and computer_choice == "rock")
                or (player_choice == "scissors" and computer_choice == "paper")
            ):
                winner = "player"
                player_skill.rect = (100, 300)
                player_skill.play_skill_animation()
                # Record the start time of skill animation
                is_skill_animation_playing = True
                skill_animation_start_time = pygame.time.get_ticks()
            else:
                winner = "bot"
                bot_skill.rect = (WIDTH - 300, 300)
                bot_skill.play_skill_animation()
                # Record the start time of skill animation
                is_skill_animation_playing = True
                skill_animation_start_time = pygame.time.get_ticks()

        if (
            is_skill_animation_playing
            and pygame.time.get_ticks() - skill_animation_start_time >= 1000
        ):
            if winner == "player":
                bot_player_hp -= 1
                bot_player.play_hurt_animation()
                bothurt.play()
                is_skill_animation_playing = False  # Reset the flag
                if bot_player_hp <= 0:
                    game_state = VICTORY
                    run_animation_start_time = pygame.time.get_ticks()
            elif winner == "bot":
                main_player_hp -= 1
                main_player.play_hurt_animation()
                playerhurt.play()
                is_skill_animation_playing = False  # Reset the flag
                if main_player_hp <= 0:
                    game_state = DEFEAT
                    run_animation_start_time = pygame.time.get_ticks()

        screen.fill(GREEN)  # Change to a different background color if needed
        text = font.render("Q", True, (175, 38, 85))
        screen.blit(text, (50, 580))
        text = font.render("W", True, (175, 38, 85))
        screen.blit(text, (180, 580))
        text = font.render("E", True, (175, 38, 85))
        screen.blit(text, (310, 580))
        #heart img
        screen.blit(heart_img, (10, 10))
        text = font.render(str(main_player_hp), True, BLACK)
        screen.blit(text, (50, 10))

        screen.blit(heart_img, (WIDTH - 40, 10))
        text = font.render(str(bot_player_hp), True, BLACK)
        screen.blit(text, (WIDTH - 70, 10))
        # Btn Skill
        screen.blit(paper_btn, (0, 600))
        screen.blit(scissor_btn, (image_width // 3 + 10, 600))
        screen.blit(rock_btn, (image_width // 3 * 2, 600))
        # Draw difficulty level on the screen
        difficulty_text = font.render(f"Difficulty: {difficulty}", True, BLACK)
        difficulty_rect = difficulty_text.get_rect(topleft=(WIDTH // 2 - 50, 10))
        screen.blit(difficulty_text, difficulty_rect)
        # Update player animations
        main_player.update_animation()
        bot_player.update_animation()
        saw_skill.update_animation(10, 0)
        player_skill.update_animation(-30, 0)
        bot_skill.update_animation(30, 0)

        rock_skill.update_animation(0, 0)
        paper_skill.update_animation(0, 0)
        scissor_skill.update_animation(0, 0)

        rock_bot_skill.update_animation(0, 0)
        paper_bot_skill.update_animation(0, 0)
        scissor_bot_skill.update_animation(0, 0)
        # Your game logic goes here
        main_player.draw(screen)
        bot_player.draw(screen)
        saw_skill.draw(screen)
        player_skill.draw(screen)
        bot_skill.draw(screen)

        rock_skill.draw(screen)
        paper_skill.draw(screen)
        scissor_skill.draw(screen)

        rock_bot_skill.draw(screen)
        paper_bot_skill.draw(screen)
        scissor_bot_skill.draw(screen)

        # Draw cooldown timer
        if current_time - last_skill_time < skill_cooldown:
            remaining_time = (skill_cooldown - (current_time - last_skill_time)) // 1000
            cooldown_text = font.render(f"Cooldown: {remaining_time}s", True, BLACK)
            screen.blit(cooldown_text, (20, 550))
        pygame.display.flip()

    elif game_state == VICTORY:
        screen.fill(GREEN)
        
        if (pygame.time.get_ticks() - run_animation_start_time <= 2000
        ):
            main_player.play_run_animation()
        if (pygame.time.get_ticks() - run_animation_start_time >= 2200
        ):
            main_player.play_jump_animation()
            win.play()
        if (pygame.time.get_ticks() - run_animation_start_time >= 5000
        ):
            game_state = MENU
        text = font.render("VICTORY", True, BLACK)
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)   

        # Update player animations
        main_player.update_animation()
        main_player.draw(screen)
        pygame.display.flip()

        
    elif game_state == DEFEAT:
        screen.fill(GREEN)
        bot_player.play_jump_animation()
        main_player.play_hurt_animation()
        saw_skill.rect = (150, 300)
        saw_skill.play_skill_animation()
        lose.play()
        if (pygame.time.get_ticks() - run_animation_start_time >= 5000
        ):
            game_state = MENU
        text = font.render("DEFEAT", True, BLACK)
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)
        main_player.update_animation()
        bot_player.update_animation()
        saw_skill.update_animation(0, 0)
        bot_player.draw(screen)
        main_player.draw(screen)   
        saw_skill.draw(screen)
        pygame.display.flip()
    clock.tick(FPS)
