from kivy import Config
Config.set('graphics','resizable',0)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

from kivy.core.window import Window

from ui.view.drawable_widget import DrawableWidget
from ui.view.frame_texture import Cv2FrameTexture


class ConfigView(App):

    button_layout = None

    def __init__(self, video, fps: int, res, **kwargs):
        super().__init__(**kwargs)
        self.capture = video.video
        self.frame_texture = Cv2FrameTexture(fps=fps)
        self.drawable_widget = DrawableWidget()
        self.res = res

    def build(self):
        Window.size = (self.res[0], self.res[1])

        self.frame_texture.size = (self.res[0], self.res[1])

        self.frame_texture.add_widget(self.button_layout)
        self.frame_texture.add_widget(self.drawable_widget)
        return self.frame_texture

    def on_stop(self):
        self.capture.release()


def setup_button(controller, res):
    button_layout = GridLayout(pos=(0, -25))
    button_layout.rows = 2
    button_layout.row_force_default = True
    button_layout.row_default_height = 20
    button_layout.cols = 4
    button_layout.size = (res[0], 50)

    clear_button = Button(text='Clear', on_press=controller.delete_object)

    set_lights_button = Button(text='Set Lights', on_press=controller.set_rectangle)
    set_line_button = Button(text='Set Line', on_press=controller.set_line)
    capture_button = Button(text='Capture', on_press=controller.capture)

    button_layout.add_widget(clear_button)
    button_layout.add_widget(set_lights_button)
    button_layout.add_widget(set_line_button)
    button_layout.add_widget(capture_button)

    return button_layout
