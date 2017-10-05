from scene import *
import time

from game_scene import *
from help_scene import *
from splash_scene import *

class MainMenuScreen(Scene):
    def setup(self):
        
        
		    self.background=SpriteNode(position = self.size/2,
		                               color = ('white'),
		                               parent = self,
		                               size = self.size)
		                               
		    self.start_button = SpriteNode('./assets/sprites/start_button.png',
		                                   parent=self,
		                                   position=self.size/2)
		                                   
		    help_button_position=self.size/2
		    help_button_position.y=help_button_position.y-200
		    self.help_button = SpriteNode('./assets/sprites/help_button.png',
		                                  parent=self,
		                                  position=help_button_position)
		                                  
		    self.start_time = time.time()
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        #after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScreen())
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
