import subprocess 
from .models import Model_Error

class SystemController:
    def open_program(self, path: str) -> subprocess.Popen | Model_Error: # More specific return type
        """Opens a program."""
        try:
            return subprocess.Popen(path, shell=True) # Return the Popen object
        except FileNotFoundError: # Catch specific exception
            return Model_Error(f"Programa não encontrado em: {path}", 404)
        except Exception as e:
            return Model_Error(f"Erro ao abrir programa: {e}", 500)
        
    def close_program(self, name: str) -> int | Model_Error:
        """Closes a program by name."""
        try:
            return subprocess.call(f"taskkill /f /im {name}.exe", shell=True)
        except Exception as e:
            return Model_Error(f"Erro ao fechar programa: {e}", 500)