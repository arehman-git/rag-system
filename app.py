from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import os
import markdown
import re

app = Flask(__name__, static_folder='static')

# Initialize the LLM and embedding model
def initialize_models():
    # Settings control global defaults
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Groq(model="llama3-70b-8192", api_key="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")
    
    # Create a RAG tool using LlamaIndex
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(
        documents,
    )
    query_engine = index.as_query_engine()
    return query_engine

# Initialize the query engine
query_engine = None

# Replace the deprecated before_first_request with a setup function
def setup_query_engine():
    global query_engine
    if query_engine is None:
        query_engine = initialize_models()

def format_response(response_text):
    # Convert markdown to HTML
    html = markdown.markdown(str(response_text))
    
    # Enhance code blocks with syntax highlighting
    html = re.sub(r'<code>(.*?)</code>', r'<code class="highlight">\1</code>', html, flags=re.DOTALL)
    
    return html

@app.route('/')
def index():
    # Initialize models when the first request comes in
    setup_query_engine()
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    global query_engine
    
    # If models haven't been initialized yet
    setup_query_engine()
    
    data = request.json
    user_message = data.get('message', '')
    
    # Generate response using the query engine
    response = query_engine.query(user_message)
    
    # Format the response
    formatted_response = format_response(response)
    
    return jsonify({
        'response': formatted_response,
        'raw_response': str(response)
    })

if __name__ == '__main__':
    # Create static folder if it doesn't exist
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)