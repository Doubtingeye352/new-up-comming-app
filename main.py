from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import random

screen_helper = """
ScreenManager:
    MenuScreen:
   
<MenuScreen>:
    name: 'menu'



    MDLabel:
        text: "Welcome, please choose your password type:"
        pos_hint: {'center_x':0.8,'center_y':0.9}
    MDRoundFlatButton:
        text: "2 digit"
        pos_hint: {'center_x':0.1,'center_y':0.8}

    MDRoundFlatButton:
        text: "3 digit"
        pos_hint: {'center_x':0.5,'center_y':0.8}

    MDRoundFlatButton:
        text: "4 digit"
        pos_hint: {'center_x':0.9,'center_y':0.8}


    MDRoundFlatButton:
        text: "5 digit"
        pos_hint: {'center_x':0.1,'center_y':0.6}

    MDRoundFlatButton:
        text: "6 digit"
        pos_hint: {'center_x':0.5,'center_y':0.6}

    MDRoundFlatButton:
        text: "7 digit"
        pos_hint: {'center_x':0.9,'center_y':0.6}

    MDRoundFlatButton:
        text: "8 digit"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: app.do_action()
    

    Label:
        id: my_custom_label
        label_wid: my_custom_label
        text: 'Before'
        color: 0,0,0,1 
        pos_hint: {'center_x':0.5,'center_y':0.2}

        
    
"""

class MenuScreen(Screen):
    pass




# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))




class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def do_action(self):
        self.label_wid.text = 'After'
    
        



DemoApp().run()
