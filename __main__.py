import random

from keyboard_service import KeyboardService
from video_service import VideoService
from director import Director
from cast import Cast
from actor import Actor
from gem import Gem
from rock import Rock

from color import Color
from point import Point

PROJECTILE_SPEED = 10
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "CSE210 - GREED"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

# director = Director()
# director.start_game()

def main():
    #create the cast
    cast = Cast()

    #create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    #create the rocks and gems
    for n in range(DEFAULT_ARTIFACTS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        #if n is even make a gem, else make a rock
        if n%2 == 0:
            text = '*'
            gem = Gem()
            gem.set_text(text)
            gem.set_font_size(FONT_SIZE)
            gem.set_color(color)
            gem.set_position(position)
            down = Point(0,random.randint(3, PROJECTILE_SPEED))
            gem.set_velocity(down)
            cast.add_actor("artifacts", gem)
        else:
            text = 'o'
            rock = Rock()
            rock.set_text(text)
            rock.set_font_size(FONT_SIZE)
            rock.set_color(color)
            rock.set_position(position)
            down = Point(0,random.randint(3, PROJECTILE_SPEED))
            rock.set_velocity(down)
            cast.add_actor("artifacts", rock)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

        
if __name__ == "__main__":
    main()