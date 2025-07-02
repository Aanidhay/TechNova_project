# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# xAI Grok API configuration
# XAI_API_KEY = 'xai-05Fv4kTUeUgZBNKLyX1CMkmYXVDNHcLC1POIY2zjhk9QpQQUOOjRGIr3IyAKqHzpnuxuoEFEGhlTCd3I'  # Your API key
# XAI_API_URL = 'https://api.x.ai/grok'  # Replace with actual Grok API endpoint (check https://x.ai/api)

# Google Gemini/PaLM API configuration
GOOGLE_API_KEY = "AIzaSyBTliuZfUGNCZJ90Q7KBVekNNBMJqYTM8E"
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json['message']
        
        # # Send request to xAI Grok API
        # headers = {
        #     'Authorization': f'Bearer {XAI_API_KEY}',
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     'message': message
        #     # Add other required fields as per xAI API documentation
        # }
        
        # response = requests.post(XAI_API_URL, json=data, headers=headers)
        # response_data = response.json()
        
        # # Extract the chatbot's response (adjust based on actual API response structure)
        # bot_response = response_data.get('response', 'Sorry, something went wrong.')
        
        # Use Gemini/PaLM to generate a response
        model = genai.GenerativeModel("models/gemini-2.0-flash-exp")
        response = model.generate_content([message])
        bot_response = response.text

        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)