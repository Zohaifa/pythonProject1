import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, WipeTransition, SwapTransition
from kivy.animation import Animation

class HomeScreen(Screen):
    def on_enter(self):
        button = self.ids.animate_button
        anim = Animation(size_hint = (.5, .5), duration=1) + Animation(size_hint = (.2, .2), duration = 1)
        anim.start(button)

class ProductScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition = SlideTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProductScreen(name='product'))
        return sm





if __name__ == '__main__':
    MyApp().run()