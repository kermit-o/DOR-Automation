#!/bin/bash

# Variables
REPO_URL="https://github.com/kermit-o/DOR-Automation.git"
PROJECT_DIR="DOR-Automation"

# Paso 1: Clonar el repositorio
echo "🚀 Clonando el repositorio desde GitHub..."
if [ ! -d "$PROJECT_DIR" ]; then
    git clone $REPO_URL
else
    echo "⚠️ El directorio '$PROJECT_DIR' ya existe. Saltando clonación."
fi

cd $PROJECT_DIR || { echo "❌ Error: No se pudo acceder al directorio $PROJECT_DIR"; exit 1; }

echo "✅ Repositorio clonado correctamente."

# Paso 2: Crear entorno virtual
echo "🐍 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate  # Para Windows usa: venv\Scripts\activate

# Paso 3: Instalar dependencias
if [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependencias..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "⚠️ Advertencia: No se encontró requirements.txt, verifica las dependencias manualmente."
fi

# Paso 4: Configurar variables de entorno
echo "🔧 Configurando variables de entorno..."
export FLASK_APP="run.py"
export FLASK_ENV="development"

# Paso 5: Inicializar base de datos
echo "🗄️ Inicializando la base de datos..."
flask db upgrade || echo "⚠️ Advertencia: No se pudo inicializar la base de datos."

# Paso 6: Mensaje final
echo "🎉 ¡Instalación completada! Puedes iniciar el servidor con:"
echo "   source venv/bin/activate  # (Para activar el entorno virtual)"
echo "   flask run"

exit 0
