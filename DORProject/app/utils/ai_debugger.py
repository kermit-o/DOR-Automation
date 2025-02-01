import openai
import os
import time
import watchdog.events
import watchdog.observers

from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

class FileEventHandler(watchdog.events.FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return
        print(f"🔍 Detectando cambios en: {event.src_path}")
        revisar_codigo(event.src_path)

def revisar_codigo(file_path):
    """Analiza el código, detecta errores y sugiere correcciones."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            codigo = file.read()

        prompt = f"Analiza el siguiente código de Flask y detecta posibles errores:\n\n{codigo}\n\nDevuelve SOLO el código corregido, sin explicaciones."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Eres un depurador experto en Python y Flask."},
                      {"role": "user", "content": prompt}]
        )

        nuevo_codigo = response["choices"][0]["message"]["content"]
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(nuevo_codigo)
        
        print(f"✅ Código corregido en {file_path}. Verifica los cambios.")
    
    except Exception as e:
        print(f"❌ Error analizando {file_path}: {e}")

def monitorear_proyecto():
    """Monitorea cambios en el directorio del proyecto y aplica correcciones."""
    path = os.path.abspath(os.path.dirname(__file__))
    observer = watchdog.observers.Observer()
    event_handler = FileEventHandler()
    
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("🚀 AI Debugger está monitoreando los archivos en busca de errores...")
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
