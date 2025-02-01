from static_analysis import run_flake8, run_pylint
from run_tests import run_pytest
from autocorrect import autocorrect
from openai_analysis import analyze_code_with_openai

def correction_loop(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        print(f"Attempt {attempts + 1} of {max_attempts}")
        
        # Ejecutar análisis estático
        flake8_output = run_flake8()
        pylint_output = run_pylint()
        
        # Si no hay errores, salir del bucle
        if not flake8_output and not pylint_output:
            print("No errors found. Exiting correction loop.")
            break
        
        # Autocorrección básica
        autocorrect()
        
        # Enviar código a OpenAI GPT para análisis y corrección
        with open("app/main/routes.py", "r") as file:
            code = file.read()
        
        print("Sending code to OpenAI GPT for analysis...")
        corrected_code = analyze_code_with_openai(code)
        
        if corrected_code:
            print("OpenAI GPT suggestions received. Applying corrections...")
            with open("app/main/routes.py", "w") as file:
                file.write(corrected_code)
        
        # Ejecutar pruebas
        pytest_output = run_pytest()
        if "failed" not in pytest_output:
            print("All tests passed. Exiting correction loop.")
            break
        
        attempts += 1
    else:
        print("Max attempts reached. Exiting correction loop.")