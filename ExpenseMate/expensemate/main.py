# main.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from expensemate.screens.expence_screen import ExpensesScreen
from expensemate.screens.menu_screen import MenuScreen
from expensemate.screens.split_screen import SplitScreen
from expensemate.screens.summery_screen import SummaryScreen


class ExpenseMateApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(SplitScreen(name="split"))
        return sm

if __name__ == '__main__':
    ExpenseMateApp().run()
