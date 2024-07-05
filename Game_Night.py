from kivy.app import App
from kivy.lang.builder import Builder


class GameNightApp(App):
    def build(self):
        screen_manager = Builder.load_file("GameNightScreenManager.kv")
        return screen_manager


if __name__ == "__main__":
    GameNightApp().run()
