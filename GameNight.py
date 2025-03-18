from kivymd.app import MDApp
from kivy.lang.builder import Builder


class GameNightApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen_manager = Builder.load_file("GameNightScreenManager.kv")
        return screen_manager


if __name__ == "__main__":
    GameNightApp().run()
