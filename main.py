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
    pass

class ProductScreen(Screen):
    pass

class AdminLoginScreen(Screen):
    def login(self):
        self.manager.get_screen('order').ids.order_label.text = f'Welcome {self.ids.username_input.text}'
        self.manager.current = 'order'

class OrderScreen(Screen):
    pass

class SummaryScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name = 'home'))
        sm.add_widget(ProductScreen(name = 'product'))
        sm.add_widget(AdminLoginScreen(name = 'admin'))
        sm.add_widget(OrderScreen(name = 'order'))
        sm.add_widget(SummaryScreen(name = 'summary'))
        return sm


if __name__ == '__main__':
    MyApp().run()
