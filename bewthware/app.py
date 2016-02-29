from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
import tfatool
from . import view


Window.fullscreen = True


class Bewth(App):

    def __init__(self, *args, img_path=".", **kwargs):
        App.__init__(self, *args, **kwargs)
        self.img_path = img_path
        self.view = view.BewthView()
        view.clear_img(self.view)

    def build(self):
        return self.view

    def start_img_monitor(self):
        pass
           

    def run(self, *args, **kwargs):
        App.run(self, *args, **kwargs)


def sessionize_and_sync_images(
        path, remote_path=tfatool.info.DEFAULT_REMOTE_DIR):
    """Sync images on the FlashAir wireless SD card and
    break new images up into photoshoot sessions"""
    pass


def sessionze_images(path):
    """Watch `path` for new images and break them
    up into photoshoot sessions"""
    pass


def _sessionize(img_watcher):
    while True:
        for new_imgs, _ in img_watcher:
             

class Images:
    """Paths to images of a photo-taking session"""

    def __init__(self):
        self._selected_idx = 0
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)
        self.idx = -1  # change selection to most recent

    @property
    def idx(self):
        return self._selected_idx

    @idx.setter
    def idx(self, new_idx):
        self._selected_idx = new_idx % len(self.paths)

    @property
    def selected(self):
        return self._images[self.idx] if self._images else None
    
    def next(self):
        self.idx += 1
        return self.selected

    def prev(self): 
        self.idx -= 1
        return self.selected


def watch_for_images(path):
    jpg_filter = lambda f: f.filename.lower().endswith(".jpg")
    watcher = tfatool.sync.watch_local_files(jpg_filter, local_dir=path)
    yield from watcher
    
