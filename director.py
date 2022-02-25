import random
from color import Color
from point import Point

MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
COLS = 60
ROWS = 40

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        #get the player (robot) and projectiles
        robot = cast.get_first_actor("player")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        #update rock and gem positions and see if the player collides with anything
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if robot.get_position().collides(artifact.get_position()):
                #adjust score
                if artifact.get_text() == '*':
                    self._score += 10
                elif artifact.get_text() == 'o':
                    self._score -= 10

                #remove the old artifact from the cast
                cast.remove_actor("artifacts", artifact)

                #reset the artifact to a random position/color
                x = random.randint(1, COLS - 1)
                y = MAX_Y
                position = Point(x, y)
                position = position.scale(CELL_SIZE)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)

                artifact.set_position(position)
                artifact.set_color(color)

                #add the artifact back into the cast
                cast.add_actor("artifacts", artifact)
                   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        self._video_service.print_score(self._score)