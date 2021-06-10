from pygame.locals import *

# game settings
TITLE = "Gun Mayhem"
HEIGHT = 720
WIDTH = 1280
FPS = 30

# game properties
VOID_HEIGHT = HEIGHT + 500  # where players die if they cross it

# colours
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# platform settings
PLATFORM_LIST = [
    ((WIDTH / 2, HEIGHT - 100), 16),
    ((200, HEIGHT - 200), 8),
    ((WIDTH - 200, HEIGHT - 200), 8),
    ((WIDTH / 2, HEIGHT - 310), 10)
]

# player properties
PLAYER_ACC = 1
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.3
PLAYER_JUMP_HEIGHT = -9
PLAYER_ANIMATION_FPS = 10
PLAYER_OFFSET = 12

# player 1 properties
PLAYER_1_COLOR = "green"
PLAYER_1_SPAWN_POINT = (WIDTH - 150, 0)
PLAYER_1_SPAWN_DIRECTION = "left"

# player 1 controls
PLAYER_1_UP = K_UP
PLAYER_1_DOWN = K_DOWN
PLAYER_1_LEFT = K_LEFT
PLAYER_1_RIGHT = K_RIGHT
PLAYER_1_SHOOT = K_PERIOD

# player 2 properties
PLAYER_2_COLOR = "red"
PLAYER_2_SPAWN_POINT = (150, 0)
PLAYER_2_SPAWN_DIRECTION = "right"

# player 2 controls
PLAYER_2_UP = K_w
PLAYER_2_DOWN = K_s
PLAYER_2_LEFT = K_a
PLAYER_2_RIGHT = K_d
PLAYER_2_SHOOT = K_g

# gun properties
GUN_RECOIL = 8
MUZZLE_FLASH_OFFSET_X = 40
MUZZLE_FLASH_OFFSET_Y = 17
MUZZLE_FLASH_RUNNING_OFFSET_Y = -2

# bullet properties
BULLET_SPEED = 22  # pixels per tick
BULLET_OFFSET_X = 16
BULLET_OFFSET_Y = -27
BULLET_RUNNING_OFFSET_Y = -2  # for running
KNOCKBACK_MULTIPLIER = 1
