import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().equals(paddle.get_position()):
            if ball.get_position().get_x >= paddle.get_position().get_x and ball.get_position().get_x <= (paddle.get_position().get_x + 11):
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().get_y == constants.MAX_Y:
            ball.set_velocity(Point.reverse_y(ball.get_velocity()))
        
        if ball.get_position().get_x == 0 or ball.get_position().get_x == constants.MAX_X:
            ball.set_velocity(Point.reverse_x(ball.get_velocity()))
        



    