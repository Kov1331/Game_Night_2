from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file("screen_welcome.kv")


class WelcomeScreen(Screen):
    ...
