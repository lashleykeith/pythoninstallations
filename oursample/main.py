from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_random_color

class Calculator(BoxLayout):
    label = ''

    def on_kv_post(self, _):
        # Called when all the widgets have been created
        # We will do the first color change here
        self.change_colors()
    
    def delete(self, instance):
        self.display.text = instance[:0]
    
    def del1(self, instance):
        self.display.text = instance[:-1]
    
    def calc(self, instance):
        try:
            self.display.text = str(eval(instance))
            self.result.text = str(eval(instance))
        except Exception:
            self.display.text = '0'
            self.result.text = 'ERROR'

        self.change_colors()

    def change_colors(self):
        # Walk through the widget tree
        for wg in self.walk():
            # Check if the widget is a button
            if isinstance(wg, Button):
                # CHange the color
                wg.background_color = get_random_color()
        
class CalculatorApp(App):
    trigger = False
    triggerC = False
    triggerD = False
    
    def build(self):
        return Calculator()
        
if __name__ == '__main__':
    CalculatorApp().run()