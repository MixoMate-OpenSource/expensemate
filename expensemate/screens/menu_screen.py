from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

from expensemate.screens.split_screen import SplitScreen


class MenuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDCard()
        label = MDLabel(text="Welcome to Screen 1!", halign="center")
        button = MDIconButton(
            icon="arrow-right",
            on_press=lambda btn: self.manager.switch_to(SplitScreen(name="split")),
        )
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)
