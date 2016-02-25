from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from . import view


Window.fullscreen = True


class Bewth(App):

    def __init__(self, *args, **kwargs):
        App.__init__(self, *args, **kwargs)
        self.view = view.BewthView()
        view.clear_img(self.view)

    def build(self):
        return self.view


