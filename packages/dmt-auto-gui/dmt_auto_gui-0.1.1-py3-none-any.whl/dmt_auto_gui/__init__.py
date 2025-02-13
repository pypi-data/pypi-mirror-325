from .gui_controller import GUIController
from .keyboard_controller import KeyboardController
from .screen_controller import ScreenController
from .system_controller import SystemController

# exemplo de uso
Gui = GUIController()
Keyboard = KeyboardController()
Screen = ScreenController()
System = SystemController()

__all__ = ['Gui', 'Keyboard', 'Screen', 'System']