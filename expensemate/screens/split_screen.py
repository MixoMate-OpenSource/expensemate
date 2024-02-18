from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class SplitScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = MDLabel(text="You are on Screen 2!", halign="center")
        self.add_widget(self.label)
