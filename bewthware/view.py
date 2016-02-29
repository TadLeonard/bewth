from collections import defaultdict

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window


class BewthView(Widget):

    _keymap = {}

    def __init__(self, watch_dir=".", session_dir=".", **kwargs):
        Widget.__init__(self, **kwargs)
        self.watch_dir = watch_dir
        self.session_dir = session_dir
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keymap = defaultdict(list)
        self._keyboard.bind(on_key_down=self._handle_keypress)
        self.bind(pos=self.redraw, size=self.redraw)

    def add_keyboard_handler(self, key, handler):
        self._keymap[key].append(handler)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._handle_keypress)
        self._keyboard = None

    def _handle_keypress(self, keyboard, keycode, text, modifiers):
        _, key = keycode
        if key == "escape":
            keyboard.release()
        elif key in self._keymap:
            handlers = self._keymap[key]
            for handler in handlers:
                handle(modifiers)

    def redraw(self, *_):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos


def update_img(view, path=None):
    with view.canvas:
        view.bg_rect = Image(source=path,
                             pos=view.pos, size=view.size)


def clear_img(view):
    view.bg_rect = Image(pos=view.pos, size=view.size)
 
