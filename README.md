
# Aplicación RAG con LLMs y Extracción de Texto PDF

## Descripción
Esta aplicación integra la generación de texto con modelos (gpt y llama), y un sistema de extracción de texto de documentos PDF para crear respuestas enriquecidas basadas en información relevante extraída en tiempo real.

## Funcionalidades
- **Procesamiento de directorios PDF**: Procesa directorios enteros para extraer texto y cargarlo en una base de datos.
- **Generación de respuestas con GPT**: Utiliza el modelo GPT para generar respuestas basadas en consultas y el contexto proporcionado por los textos extraídos.
- **Generación de respuestas con Llama3**: Utiliza el modelo llama3 para generar respuestas basadas en consultas y el contexto proporcionado por los textos extraídos.
## Instrucciones de Instalación y Uso

### Creación de un entorno virtual
```bash
python -m venv venv
```
```bash
source python -m venv venv
  # En Windows use `venv\Scripts\activate`
```

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Ejecución del Servidor Flask con debug activado
```bash
flask run --debug 
```

## Uso (La consulta de llama3 requiere tener ollama instalado y el modelo llama 3 corriendo ver https://ollama.com/)
Realice solicitudes POST a los endpoints definidos para procesar PDFs o para pedir respuestas a GPT basadas en el texto de los PDFs.

## /process-pdfs
### body
```bash
{
  "directory_path": "files's path",
  "chunk_size": 2000 #optional default 500
}
```
## /ask_gpt4 
### body
```bash
{
  "question": "Consulta",
  "rol_context": "Rol del asistente"
}
```
## /ask_llama3 
### body
```bash
{
  "question": "Consulta",
  "rol_context": "Rol del asistente"
}
```
