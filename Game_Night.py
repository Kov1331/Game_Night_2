# from kivy.app import App
from kivymd.app import MDApp
from kivy.lang.builder import Builder


class GameNightApp(MDApp):
    def build(self):
        screen_manager = Builder.load_file("GameNightScreenManager.kv")
        return screen_manager


if __name__ == "__main__":
    GameNightApp().run()
