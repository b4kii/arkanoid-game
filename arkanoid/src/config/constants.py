# Colors
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 143, 0)

# Assets

## Images 
FIELD_SPRITES = "assets/images/fields.png"
BACKGROUND_SPRITES = "assets/images/backgrounds.png"
VAUS_SPRITES = "assets/images/vaus.png"
POWERUP_SPRITES = "assets/images/powerups.png"
ENEMIES_SPRITES = "assets/images/enemies.png"

## Sounds
GAME_SCENE_SOUND = "assets/sounds/stage/game.mp3"
INTRO_SOUND = "assets/sounds/stage/intro.mp3"
LOSE_SOUND = "assets/sounds/stage/lose.mp3"
WIN_SOUND = "assets/sounds/stage/win.mp3"

BOUNCE_SOUND = "assets/sounds/effects/bounce.wav"
HEALTH_LOSE_SOUND = "assets/sounds/effects/health-lose.wav"
UPGRADE_SOUND = "assets/sounds/effects/upgrade.wav"
ENEMY_HIT_SOUND = "assets/sounds/effects/enemy-hit.wav"

BACKGROUND_SOUND_VOLUME = 0.02
EFFECTS_SOUND_VOLUME = 0.2

# Score
USER_DATA_JSON = "src/config/data.json"

# Window
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
SW_MID = SCREEN_WIDTH // 2
SH_MID = SCREEN_HEIGHT // 2
FPS = 60
BORDER_OFFSET = SCREEN_WIDTH * 0.036 + 3

# Player
PLAYER_SPEED = 10
PLAYER_HEALTH = 3

# Ball
BALL_SPEED = 10

# Upgrades
UPGRADES = ["speed", "size", "health"]

# Blocks
BLOCKS_HEALTH = [1, 2, 3, 4, 5, 6]

BLOCK_MAPS = [
    [
        "11111111111",
        "11111111111",
        "11111111111",
    ],
    [
        "22222222222",
        "22       22",
        "22       22",
        "22222222222",
    ],
    [
        "33333333333",
        "33       33",
        "22222222222",
        "22       22",
        "11111111111",
    ],
    [
        "  3333333  ",
        "  3333333  ",
        "22222442222",
        "22222442222",
        "  1111111  ",
        "  1111111  ",
    ],
    [
        "4444444444",
        "4444444444",
        "33  33  33",
        "33  33  33",
        "22  22  22",
        "1111111111",
        "1111111111",
    ],
    [
        "5555555555",
        "5555555555",
        "   4444   ",
        "   3333   ",
        "   2222   ",
        "1111111111",
        " 11111111 ",
    ],
    [
        "6666666666",
        "44  55  44",
        "44  55  44",
        "    33    ",
        "    22    ",
        "  111111  ",
        " 11111111 ",
    ],
    [
        "6666666666",
        "6666666666",
        "55  55  55",
        "44  44  44",
        "33  33  33 ",
        "22  22  22",
        "2222222222",
    ],
    [
        "6666666666",
        "66  66  66",
        "5555555555",
        "55  55  55",
        "4444444444",
        "44  44  44",
        "3333333333",
    ],
    [
        "6666666666",
        "6  6446  6",
        "5  5445  5",
        "5555445555",
        "4333443334",
        "4333443334",
        "333    333",
        "  333333  ",
    ],
    [
        "6666666666",
        "6 66  66 6",
        "6 66  66 6",
        "5 55  55 5",
        "5555  5555",
        "5  5  5  5",
        "4444  4444",
        "  444444  ",
    ],
    [
        " 66666666 ",
        "6666  6666",
        "6666  6666",
        "5 55  55 5",
        "5555  5555",
        "5555  5555",
        " 444  444 ",
        "  444444  ",
    ],
    [
        "6666666666",
        "6666666666",
        "6666666666",
        "5555555555",
        "5555555555",
        "5555555555",
        "          ",
        "          ",
    ],
    [
        "6666666666",
        "6666666666",
        "6666666666",
        "5555555555",
        "5555555555",
        "5555555555",
        "4444444444",
        "  444444  ",
    ],
]

GAP_SIZE = 5
GRID_HEIGHT = 30

FONT_TYPE = "minecraftregular"
FONT_PATH = "assets/fonts/minecraft.otf"

# Animation
ANIMATION_STEPS = 8
ANIMATION_COOLDOWN = 100

