from kivymd.app import MDApp
from kivy.lang.builder import Builder


class GameNightApp(MDApp):
    def build(self):
        screen_manager = Builder.load_file("GameNightScreenManager.kv")
        self.theme_cls.theme_style = "Dark"
        return screen_manager


if __name__ == "__main__":
    GameNightApp().run()
