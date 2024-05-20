from flask import Flask, request, jsonify
from rag import process_directory, query_rag
from gpt_improved import request_gpt
from llama3_improved import requestllama3
app = Flask(__name__)

@app.route('/ask_llama3', methods=['POST'])
def ask_question_llama3():
    """Recibe una pregunta y opcionalmente un contexto de rol para el modelo, y obtiene una respuesta del modelo GPT."""
    data = request.get_json()
    question = data.get('question')
    rol_context = data.get('rol_context', None)
       
    if not question:
        return jsonify({'error': 'No se proporcionó una pregunta'}), 400
    
    """Recupera del rag los documentos relevantes para responder la consulta"""
    context_memory = query_rag(question)
   
    """Invoca al modelo con llama3_improved.py con el pregunta, el rol del asistente y el texto relevante del rag"""
    response = requestllama3(question, rol_context, context_memory)
    result= (str(response),200)
    return jsonify(result)

@app.route('/ask_gpt4', methods=['POST'])
def ask_question_gpt4():
    """Recibe una pregunta y opcionalmente un contexto de rol para el modelo, y obtiene una respuesta del modelo GPT."""
    data = request.get_json()
    question = data.get('question')
    rol_context = data.get('rol_context', None)
       
    if not question:
        return jsonify({'error': 'No se proporcionó una pregunta'}), 400
    
    """Recupera del rag los documentos relevantes para responder la consulta"""
    context_memory = query_rag(question)
   
    """Invoca al modelo con gpt_improved.py con el pregunta, el rol del asistente y el texto relevante del rag"""
    response = request_gpt(question, rol_context, context_memory)
    result= (str(response),200)
    return jsonify(result)


@app.route('/process-pdfs', methods=['POST'])
def handle_process_pdfs():
    """Endpoint que invoca el procesamiento de un directorio de PDFs."""
    data = request.get_json()
    directory_path = data['directory_path']
    chunk_size = data.get('chunk_size', 500)# Default chunk size to 500 if not specified
    
    if not directory_path:
        return jsonify({'error': 'No se proporcionó la ruta del directorio'}), 400
    
    """invoca al metodo de rag que procesa los pdfs de un directorio, le indica el path y el tamaño de los chunks"""
    result = process_directory(directory_path, chunk_size)
    if 'error' in result:
        return jsonify(result), 404
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)