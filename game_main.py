import pygame
import sys #sys是python的标准库，提供Python运行时环境变量的操控

class AlienInvasion:
    """Game Main Class"""
    
    def __init__(self)->None:
        """Init the game"""
        pygame.init()
        
        self.screen =pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Game Main Loop"""
        while True:
            # handle user input 
            for event in pygame.event.get():
                
                # unit the game event
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # update the display
            pygame.display.flip()


if __name__=='__main__':
    # start the game
    ai = AlienInvasion()
    ai.run_game()




