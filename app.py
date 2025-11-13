import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import PyPDF2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
GEMINI_API_KEY = "AIzaSyBtW3EGR3ORXazqo1rxz9V9GSIOFYnDrOY"  # Cole sua chave Gemini aqui

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

pdf_text = ""  # Variável global simples para exemplo
chat_history = []  # Lista global para armazenar o histórico

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_text
    file = request.files.get('pdf')
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        try:
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
            pdf_text = text  # Salva para uso no chat
            return jsonify({'status': 'sucesso', 'mensagem': 'PDF recebido e lido!'})
        except Exception as e:
            return jsonify({'status': 'erro', 'mensagem': f'Erro ao ler PDF: {str(e)}'})
    return jsonify({'status': 'erro', 'mensagem': 'Nenhum arquivo enviado.'})

@app.route('/chat', methods=['POST'])
def chat():
    global pdf_text, chat_history
    user_message = request.json.get('message')
    prompt = f"O seguinte texto foi extraído de um PDF:\n\n{pdf_text}\n\nPergunta do usuário: {user_message}\n\nResponda de forma clara e objetiva."
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        answer = response.text.strip()
        # Salva no histórico
        chat_history.append({"pergunta": user_message, "resposta": answer})
        return jsonify({'response': answer, 'history': chat_history})
    except Exception as e:
        return jsonify({'response': f"Erro ao consultar Gemini: {str(e)}", 'history': chat_history})

@app.route('/history', methods=['GET'])
def get_history():
    global chat_history
    return jsonify(chat_history)

if __name__ == '__main__':
    app.run(debug=True)