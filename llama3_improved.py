
import logging
import ollama

def requestllama3(query, rol_context='', memory_context=''):
    """Envía una consulta al modelo llama3 usando la instacia local Ollama, usando opcionalmente un contexto para respuestas enriquecidas."""
    # Combinar el contexto y la consulta si el contexto está disponible
    if memory_context:
        content = f"{rol_context}. {memory_context}. {query}"
    else:
        content = query

    try:
        # Realizar la solicitud a la ollama para usar llama3
        """  response = ollama.chat(model='llama3', messages=[
        {
        'role': 'user',
        'content': content,
        },
        ])  """    
        response = ollama.generate(model='llama3', prompt=content)
        # Devuelve el mensaje generado por el modelo
        return response
    except Exception as e:
        # Registrar errores si la solicitud falla
        logging.error("Error al obtener respuesta del modelo GPT: %s", e)
        return None
