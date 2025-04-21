from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv
from userdata import get

# 載入環境變數
load_dotenv()

# 創建 Flask 應用程式實例
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

# 配置 Gemini API
GEMINI_API_KEY = get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY 環境變數未設置")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': '請提供有效的訊息'}), 400
        
    user_message = data.get('message', '')
    
    try:
        response = model.generate_content(user_message)
        return jsonify({
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 