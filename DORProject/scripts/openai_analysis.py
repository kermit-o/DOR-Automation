import openai

# Configura tu clave de API de OpenAI
openai.api_key = "tu_clave_de_api_aqui"

def analyze_code_with_openai(code, context="Fix any errors and improve the code."):
    """
    Envía el código a OpenAI GPT para análisis y corrección.
    :param code: El código a analizar.
    :param context: Instrucciones para GPT (opcional).
    :return: El código corregido o sugerencias.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Usa GPT-4 o GPT-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant that fixes and improves code."},
                {"role": "user", "content": f"{context}\n\n{code}"}
            ],
            max_tokens=1000,  # Ajusta según sea necesario
            temperature=0.5,  # Controla la creatividad (0 = más determinista, 1 = más creativo)
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error al comunicarse con OpenAI: {e}")
        return None