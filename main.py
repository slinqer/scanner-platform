## Kivy dependencies
from kivy.app import App
from kivy.uix.button import Button

## Master Class
class GeoApp(App):
  def build(self):
    """
      Initialization of the graphic app
    """
    return Button(text='Hello World')

if __name__ == "__main__":
  GeoApp().run()