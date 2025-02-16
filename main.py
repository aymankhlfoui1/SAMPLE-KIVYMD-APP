from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.spell_screen import SpellScreen
from screens.settings_screen import SettingsScreen

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SpellScreen(name="spell"))
        sm.add_widget(SettingsScreen(name="settings"))
        return sm

if __name__ == "__main__":
    MyApp().run()
