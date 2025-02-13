import pyautogui
import time 
import os 
from .models import Model_AutoGuiResponse, Model_Error

class GUIController:
    def find_image_on_screen(self, file_name:str, sleep_after=0, confidence=.9, timeout=30, pos=None) -> Model_AutoGuiResponse | Model_Error:
        """
        Procura uma imagem na tela\n
        args:
            file_name: str -> Nome do arquivo
            sleep: int -> Tempo de espera
            confidence: float -> Confiança
            timeout: int -> Tempo limite
            pos: tuple -> Posição
        return:
            Model_AutoGuiResponse | Model_Error
        """
        full_path = file_name  # Assume it's a full path initially
        if not os.path.exists(full_path): # Check if it's a full path
            # Try relative path in the same directory as the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, file_name)

            if not os.path.exists(full_path):
                return Model_Error(f"Arquivo {file_name} não encontrado!", 404)

        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                x, y = pyautogui.locateCenterOnScreen(file_name, confidence=confidence, region=pos)
                time_took = time.time() - start_time
                time.sleep(sleep_after)
                return Model_AutoGuiResponse(x, y, confidence, time_took)
            except TypeError as e:
                print(f"Erro ao procurar imagem: {file_name} Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            except BaseException as e:
                return Model_Error(f"Erro inesperado: {e}", 500)
        return Model_Error("Tempo excedido", 408)
    
    def click_on_image(self, file_name: str, sleep=0, clicks: int = 1, confidence=.9, timeout=30, pos=None) -> Model_AutoGuiResponse | Model_Error:
        """
        Clica em uma imagem\n
        args:
            file_name: str -> Nome do arquivo
            sleep: int -> Tempo de espera
            clicks: int -> Número de cliques
            confidence: float -> Confiança
            timeout: int -> Tempo limite
            pos: tuple -> Posição
        return:
            Model_AutoGuiResponse | Model_Error
        """
        response = self.find_image_on_screen(file_name, sleep, confidence, timeout, pos)
        if isinstance(response, Model_AutoGuiResponse):
            pyautogui.click(response.posistion_found, clicks=clicks)
        return response

    def click_on_position(self, x: int, y: int, clicks: int = 1) -> None | Model_Error:
        """
        Clica em uma posição\n
        args:
            x: int -> Posição x
            y: int -> Posição y
            clicks: int -> Número de cliques
        return:
            None | Model_Error
        """
        try:
            pyautogui.click(x, y, clicks=clicks)
            return None
        except Exception as e:
            return Model_Error(f"Erro ao clicar na posição {x}, {y}: {e}", 500)
    
    def get_mouse_position(self) -> tuple | Model_Error:
        """
        Pega a posição do mouse\n
        return:
            tuple | Model_Error
        """
        try:
            return pyautogui.position()
        except Exception as e:
            return Model_Error(f"Erro ao pegar posição do mouse: {e}", 500)