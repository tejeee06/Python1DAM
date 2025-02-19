import pygame
import random
import sys

# ========================
# Configuració inicial
# ========================
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Inicialitzar Pygame i la finestra
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc de Dispars")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
background_image = pygame.image.load("PythonGame/fons.png").convert()  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
shoot_sound = pygame.mixer.Sound("PythonGame/laserdef.wav")
meteorite_explosion_sound = pygame.mixer.Sound("PythonGame/explosionMeteorit.wav")
xwing_explosion_sound = pygame.mixer.Sound("PythonGame/explosionXwing.wav")
cruiser_explosion_sound = pygame.mixer.Sound("PythonGame/explosionCreuer.wav")
collision_sound = pygame.mixer.Sound("PythonGame/choque.wav")
meteorite_explosion_sound.set_volume(0.5)
xwing_explosion_sound.set_volume(0.7)
cruiser_explosion_sound.set_volume(1.0)
collision_sound.set_volume(0.8)
backgroundX = 0
backgroundSpeed = 3

# ========================
# Variables Globals del Joc
# ========================
score = 0
difficulty_level = 1
lives = 3
last_difficulty_update_time = pygame.time.get_ticks()
spawn_interval = 1500
ADD_OBSTACLE = pygame.USEREVENT + 1
obstacle_speed = 3
bullets = pygame.sprite.Group()
current_bullet_color = RED

# ========================
# Funcions Auxiliars
# ========================
def draw_text(surface, text, font, color, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def draw_background(screen, background_image, backgroundX):
    screen.blit(background_image, (backgroundX, 0))
    screen.blit(background_image, (backgroundX + WIDTH, 0))
    backgroundX -= backgroundSpeed
    if backgroundX <= -WIDTH:
        backgroundX = 0
    return backgroundX

# ========================
# Classes del Joc
# ========================
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size=(100, 100)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load("PythonGame/explosion.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=center)
        self.frame = 0
        self.max_frames = 15

    def update(self):
        self.frame += 1
        if self.frame >= self.max_frames:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("PythonGame/2.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5
        self.shots_fired = 0
        self.is_reloading = False
        self.reload_duration = 150 
        self.last_reload_time = 0 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
        
        if self.is_reloading:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_reload_time >= self.reload_duration:
                self.is_reloading = False
                self.shots_fired = 0

    def shoot(self, all_sprites, bullets):
        if self.is_reloading:
            return

        global current_bullet_color
        bullet = Bullet(self.rect.right, self.rect.centery, current_bullet_color)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()

        current_bullet_color = GREEN if current_bullet_color == RED else RED
        self.shots_fired += 1
        if self.shots_fired >= 2:
            self.is_reloading = True
            self.last_reload_time = pygame.time.get_ticks()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, difficulty_level):
        super().__init__()
        self.type = type
        self.difficulty_level = difficulty_level

        types = {
            "meteorite": ("PythonGame/meteorit.png", (50, 50), (3, 6), 2, 1),
            "xwing": ("PythonGame/xwing.png", (80, 80), (6, 9), 4, 2),
            "cruiser": ("PythonGame/crucero.png", (120, 120), (3, 6), 6, 4)
        }

        img_path, size, speed_range, points, hits = types[type]
        self.width, self.height = size
        self.speed = random.randint(speed_range[0] + difficulty_level, speed_range[1] + difficulty_level)
        self.points = points
        self.hits_to_destroy = hits

        self.image = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - self.height)
        self.hits_received = 0

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def hit(self):
        self.hits_received += 1
        if self.hits_received >= self.hits_to_destroy:
            explosion_size = {
                "meteorite": (50, 50),
                "xwing": (80, 80),
                "cruiser": (120, 120)
            }[self.type]
            
            explosion = Explosion(self.rect.center, explosion_size)
            all_sprites.add(explosion)
            
            {
                "meteorite": meteorite_explosion_sound,
                "xwing": xwing_explosion_sound,
                "cruiser": cruiser_explosion_sound
            }[self.type].play()
            
            self.kill()
            return True
        return False

# ========================
# Funciones del juego
# ========================
def new_game():
    global score, difficulty_level, lives, last_difficulty_update_time, spawn_interval, all_sprites, obstacles, player, bullets, backgroundX, current_bullet_color
    score = 0
    difficulty_level = 1
    lives = 3
    last_difficulty_update_time = pygame.time.get_ticks()
    spawn_interval = 1500
    pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    backgroundX = 0
    current_bullet_color = RED

def show_menu():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

        screen.blit(background_image, (0, 0))
        draw_text(screen, "Joc de disparar", font, YELLOW, 300, 200)
        draw_text(screen, "Prem qualsevol tecla per començar", font, YELLOW, 220, 250)
        pygame.display.flip()

def game_loop():
    global difficulty_level, last_difficulty_update_time, spawn_interval, lives, score, backgroundX
    new_game()
    game_state = "playing"
    running = True
    pause_start_time = 0
    max_obstacles_on_screen = 5
    base_spawn_interval = 1500

    while running:
        clock.tick(FPS)
        
        if game_state == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == ADD_OBSTACLE:
                    if score >= 30:
                        max_obstacles_on_screen = min(10, max_obstacles_on_screen + 1)
                        base_spawn_interval = max(500, base_spawn_interval - 100)

                    if len(obstacles) < max_obstacles_on_screen:
                        if score >= 20 and random.random() < 0.3:
                            obstacle = Obstacle("cruiser", difficulty_level)
                        elif score >= 10 and random.random() < 0.5:
                            obstacle = Obstacle("xwing", difficulty_level)
                        else:
                            obstacle = Obstacle("meteorite", difficulty_level)

                        all_sprites.add(obstacle)
                        obstacles.add(obstacle)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot(all_sprites, bullets)

            all_sprites.update()

            hits = pygame.sprite.groupcollide(obstacles, bullets, False, True)
            for obstacle, bullets_list in hits.items():
                if obstacle.hit():
                    score += obstacle.points

            if pygame.sprite.spritecollideany(player, obstacles):
                collided_obstacle = pygame.sprite.spritecollideany(player, obstacles)
                explosion = Explosion(player.rect.center, (100, 100))
                all_sprites.add(explosion)
                
                if collided_obstacle.type == "cruiser":
                    cruiser_explosion_sound.play()
                    lives = 0
                    game_state = "game_over"
                else:
                    collision_sound.play()
                    lives -= 1
                    collided_obstacle.kill()
                    game_state = "paused"
                    pause_start_time = pygame.time.get_ticks()

                if lives <= 0:
                    game_state = "game_over"

        elif game_state == "paused":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if pygame.time.get_ticks() - pause_start_time >= 3000:
                game_state = "playing"

        elif game_state == "game_over":
            running = False

        backgroundX = draw_background(screen, background_image, backgroundX)
        all_sprites.draw(screen)
        
        draw_text(screen, f"Puntuació: {score}", font, YELLOW, 10, 10)
        draw_text(screen, f"Vides: {lives}", font, YELLOW, 10, 70)
        
        if game_state == "paused":
            draw_text(screen, "¡Impacte!", font, RED, WIDTH//2-50, HEIGHT//2-20)
        
        pygame.display.flip()

    return score

def show_game_over(final_score):
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

        screen.blit(background_image, (0, 0))
        draw_text(screen, "Game Over!", font, RED, 350, 200)
        draw_text(screen, f"Puntuació Final: {final_score}", font, YELLOW, 320, 250)
        draw_text(screen, "Prem qualsevol tecla per reiniciar", font, YELLOW, 250, 300)
        pygame.display.flip()

# ========================
# Bucle principal
# ========================
while True:
    show_menu()
    final_score = game_loop()
    show_game_over(final_score)