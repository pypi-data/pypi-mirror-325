import pyautogui
import pyperclip
import time 
from .models import Model_Error

class KeyboardController:
    def press_keys(self, *keys, tempo=0) -> bool | Model_Error:
        """
        Pressiona teclas\n
        args:
            keys: str -> Teclas a serem pressionadas
            tempo: int -> Tempo de espera
        return:
            bool | Model_Error
        """
        try:
            if not keys:
                raise ValueError("At least one key must be specified")
            pyautogui.hotkey(*keys)
            time.sleep(tempo)
            return True
        except Exception as e:
            return Model_Error(f"Erro ao pressionar teclas: {e}", 500)
    
    def write_text(self, text:str, tempo=0) -> bool | Model_Error:
        """
        Escreve um texto\n
        args:
            text: str -> Texto a ser escrito
            tempo: int -> Tempo de espera
        return:
            bool | Model_Error
        """
        try:
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(tempo)
            return True
        except Exception as e:
            return Model_Error(f"Erro ao escrever texto: {e}", 500)