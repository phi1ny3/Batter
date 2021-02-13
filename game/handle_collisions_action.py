import random
from game import constants
from game.point import Point
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.da
        """
        brick = cast["brick"][0]
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        # if ball.get_position().equals(brick.get_position()):
        #         brick.remove(brick)
        #         ball.set_velocity(Point.reverse_y(ball.get_velocity))
        # if ball.get_position().get_y == paddle.get_position().get_y:
        #     if ball.get_position().get_x >= paddle.get_position().get_x and ball.get_position().get_x <= (paddle.get_position().get_x + 11):
        #         ball.set_velocity(Point.reverse_y(ball.get_velocity))