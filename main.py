from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label = Label(text='Привет!!!')
        name_txt = Label(text='Введите имя:')
        age_txt = Label(text='Введите возраст:')
        name_input = TextInput()
        age_input = TextInput()
        button1 = Button(text='Начать')
        layout_v = BoxLayout(orientation='vertical')
        layout_name = BoxLayout()
        layout_age = BoxLayout()
        layout_v.add_widget(label)
        layout_v.add_widget(layout_name)
        layout_v.add_widget(layout_age)
        layout_name.add_widget(name_txt)
        layout_name.add_widget(name_input)
        layout_age.add_widget(age_txt)
        layout_age.add_widget(age_input)
        layout_v.add_widget(button1)
        self.add_widget(layout_v)


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        screeeen = ScreenManager()
        screeeen.add_widget(FirstScreen(name='Экран 1'))
        screeeen.add_widget(SecondScreen(name='Экран 2'))
        return screeeen

app = MyApp()
app.run()