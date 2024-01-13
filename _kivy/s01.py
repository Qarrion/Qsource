from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SplitScreenApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # 위에 있는 노란색 박스
        yellow_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))
        yellow_box.add_widget(Label(text='Yellow', background_color=(1, 1, 0, 1)))
        
        # 아래에 있는 파란색 박스
        blue_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))
        blue_box.add_widget(Label(text='Blue', background_color=(0, 0, 1, 1)))

        layout.add_widget(yellow_box)
        layout.add_widget(blue_box)

        return layout

if __name__ == '__main__':
    SplitScreenApp().run()