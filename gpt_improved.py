
from openai import OpenAI
import logging

# Configura tu clave de API de OpenAI
client = OpenAI(api_key="tu api key aca, ej: sk-xxxx-XXXXXgUOSRqPpjZymxxxxxxxxxLgh6MTyjwrOccccccccc")

def request_gpt(query, rol_context='', memory_context='',temperature=0.5, max_tokens=1000, top_p=1):
    """Envía una consulta al modelo GPT, usando opcionalmente un contexto para respuestas enriquecidas."""
    # Combinar el contexto y la consulta si el contexto está disponible
    if memory_context:
        content = f"{rol_context}. {memory_context}. {query}"
    else:
        content = query

    try:
        # Realizar la solicitud a la API de OpenAI, configurando los parámetros de generación
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": content}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        # Devuelve el mensaje generado por el modelo
        return response.choices[0].message 
    except Exception as e:
        # Registrar errores si la solicitud falla
        logging.error("Error al obtener respuesta del modelo GPT: %s", e)
        return None

if __name__ == "__main__":
    # Uso de ejemplo, imprime una respuesta de GPT basada en una consulta y contexto dados
    print(request_gpt("¿Cómo funciona el mercado de valores?", context="Hablando de mercados financieros"))
