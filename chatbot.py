# from flask import Flask, request, send_from_directory, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv()

# app = Flask(__name__, static_folder='.')
# CORS(app)

# # Configure Gemini API using environment variable
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
# model = genai.GenerativeModel('gemini-2.0-flash')

# # Define the initial greeting and role
# INITIAL_PROMPT = """Hello there! I am Blossom Buddy. How can I help your little one?"""

# # Define the system behavior without greeting
# SYSTEM_BEHAVIOR = """You are a specialized virtual assistant for newborn and child health (0-5 years). Provide brief, accurate medical guidance on:
# - Feeding
# - Sleep
# - Postures
# - Common symptoms
# - Childcare basics
# - Safe OTC medicines

# Key points:
# 1. Only discuss approved OTC medicines for minor issues
# 2. Always consult pediatrician before any medicine
# 3. No prescription drugs or dosages
# 4. Seek immediate medical help for serious symptoms
# 5. Only advise on children 0-5 years
# 6. Keep responses concise and evidence-based
# 7. Do not repeat the initial greeting in responses
# 8. End each response with a positive note or helpful tip

# For topics outside child healthcare (0-5 years), politely redirect."""

# chat_history = {}

# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.json
#         user_message = data.get('message', '')
#         session_id = data.get('session_id', 'default')
#         child_age = data.get('child_age')
#         chat_history = data.get('chat_history', [])

#         # Format chat history for context
#         conversation_context = "\n".join([
#             f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
#             for msg in chat_history[-5:]  # Include last 5 messages for context
#         ])

#         # Include age and chat history in the prompt
#         age_context = f"Child's age: {child_age}. " if child_age else ""
#         full_prompt = f"""{SYSTEM_BEHAVIOR}

# Previous conversation:
# {conversation_context}

# Context: {age_context}
# User: {user_message}
# Assistant:"""

#         response = model.generate_content(
#             full_prompt,
#             generation_config=genai.types.GenerationConfig(
#                 temperature=0.7,
#                 top_p=0.95,
#                 top_k=40,
#                 max_output_tokens=8192,
#             )
#         )
        
#         return jsonify({'response': response.text})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)





# from flask import Flask, request, send_from_directory, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# app = Flask(__name__, static_folder='.')
# CORS(app)

# # Configure Gemini API using environment variable
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
# model = genai.GenerativeModel('gemini-2.0-flash')

# # Define the initial greeting and role
# INITIAL_PROMPT = """Hello there! I am Blossom Buddy. How can I help your little one?"""

# # Define the system behavior without greeting
# SYSTEM_BEHAVIOR = """You are a specialized virtual assistant for newborn and child health (0-5 years). Provide brief, accurate medical guidance on:
# - Feeding
# - Sleep
# - Postures
# - Common symptoms
# - Childcare basics
# - Safe OTC medicines

# Key points:
# 1. Only discuss approved OTC medicines for minor issues
# 2. Always consult pediatrician before any medicine
# 3. No prescription drugs or dosages
# 4. Seek immediate medical help for serious symptoms
# 5. Only advise on children 0-5 years
# 6. Keep responses concise and evidence-based
# 7. Do not repeat the initial greeting in responses
# 8. End each response with a positive note or helpful tip

# For topics outside child healthcare (0-5 years), politely redirect."""

# chat_history = {}

# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.json
#         user_message = data.get('message', '')
#         session_id = data.get('session_id', 'default')
#         child_age = data.get('child_age')
#         chat_history = data.get('chat_history', [])

#         # Format chat history for context
#         conversation_context = "\n".join([
#             f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
#             for msg in chat_history[-5:]  # Include last 5 messages for context
#         ])

#         # Include age and chat history in the prompt
#         age_context = f"Child's age: {child_age}. " if child_age else ""
#         full_prompt = f"""{SYSTEM_BEHAVIOR}

# Previous conversation:
# {conversation_context}

# Context: {age_context}
# User: {user_message}
# Assistant:"""

#         response = model.generate_content(
#             full_prompt,
#             generation_config=genai.types.GenerationConfig(
#                 temperature=0.7,
#                 top_p=0.95,
#                 top_k=40,
#                 max_output_tokens=8192,
#             )
#         )
        
#         return jsonify({'response': response.text})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))  # Fixed Port Issue
#     app.run(host="0.0.0.0", port=port, debug=False)


from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)

# Configure Gemini API using environment variable
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

# Define system behavior
SYSTEM_BEHAVIOR = """You are a specialized virtual assistant for newborn and child health (0-5 years)..."""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        child_age = data.get('child_age')
        chat_history = data.get('chat_history', [])

        # Format chat history for context
        conversation_context = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
            for msg in chat_history[-5:]
        ])

        # Include age and chat history in the prompt
        age_context = f"Child's age: {child_age}. " if child_age else ""
        full_prompt = f"""{SYSTEM_BEHAVIOR}

Previous conversation:
{conversation_context}

Context: {age_context}
User: {user_message}
Assistant:"""

        response = model.generate_content(full_prompt)

        # Extract response correctly
        response_text = response.candidates[0].content.parts[0].text

        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=False)