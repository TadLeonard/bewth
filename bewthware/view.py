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
        self._keymap = dict(
            right=self._handle_key_right,
            left=self._handle_key_left,
        )
        self._keyboard.bind(on_key_down=self._handle_keypress)
        self.bind(pos=self.redraw, size=self.redraw)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._handle_keypress)
        self._keyboard = None

    def _handle_keypress(self, keyboard, keycode, text, modifiers):
        _, key = keycode
        if key == "escape":
            keyboard.release()
        else:
            handle = self._keymap.get(key, self._handle_key_noop)
            handle(modifiers)

    def _handle_key_right(self, modifiers):
        pass

    def _handle_key_left(self, modifiers):
        pass

    def _handle_key_noop(self, _):
        pass

    def redraw(self, *_):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos


def update_img(view, path=None):
    with view.canvas:
        view.bg_rect = Image(source=path,
                             pos=view.pos, size=view.size)


def clear_img(view):
    view.bg_rect = Image(pos=view.pos, size=view.size)
    
