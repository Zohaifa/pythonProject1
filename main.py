import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'Go to Product Screen', on_press = self.go_to_product))

    def go_to_product(self, instance):
        self.manager.current = 'product'

class ProductScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'Go back to Home Screen', on_press = self.go_to_home))

    def go_to_admin(self, instance):
        self.manager.current = 'admin'

class AdminLoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = TextInput(hint_text = 'Enter username', multiline = False)
        self.add_widget(self.username)
        self.add_widget(Button(text = 'Login', on_press = self.login))


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name = 'home'))
        sm.add_widget(ProductScreen(name = 'product'))
        return sm


if __name__ == '__main__':
    MyApp().run()
