from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
     objects is use an output service to draw all actors on the screen.
    
     Stereotype:
         Controller

     Attributes:
         _output_service (OutputService): An instance of OutputService.
     """

    '''
        This class will draw all actors on the screen.
    '''

    def __init__(self, output_service):
        '''
            The class constructor. An instance of OutputService.
        '''
        self._output_service = output_service
    def execute(self, cast):
        '''
            Execute action with the given actors.
        '''
        self._output_service.clear_screen()
        for actors in cast.values():
           self._output_service.draw_actors(actors)
        self._output_service.flush_buffer()