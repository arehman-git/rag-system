# Modern RAG Assistant

A modern Retrieval-Augmented Generation (RAG) system with a sleek dark-themed interface, built with Flask and Groq's LLM API.

## Features

- 🔍 **Retrieval-Augmented Generation** - Answers questions based on your document knowledge base
- 🤖 **LLaMA-3 Integration** - Powered by Groq's high-performance LLaMA-3 70B model
- 🎨 **Modern Dark UI** - Sleek, responsive dark-themed interface
- 📱 **Fully Responsive** - Works on desktop, tablet, and mobile devices
- ✨ **Real-time Responses** - Fast and reliable query responses
- 🔄 **Markdown Support** - Properly formatted responses with code highlighting

## Tech Stack

- **Backend**: Flask (Python)
- **LLM**: Groq API (LLaMA-3 70B)
- **Embedding Model**: HuggingFace BAAI/bge-base-en-v1.5
- **RAG Framework**: LlamaIndex
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Code Highlighting**: highlight.js

## Installation

### Prerequisites

- Python 3.8+ 
- Groq API key
- Your document corpus (PDF, TXT, etc.)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-assistant.git
cd rag-assistant
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install flask llama-index groq markdown python-dotenv
```

4. Create a `.env` file for your API key:

```bash
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

5. Create a `data` directory and add your documents:

```bash
mkdir data
# Copy your PDF, TXT, or other document files into this directory
```

## Usage

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

3. Start asking questions about your document corpus!

## Project Structure

```
rag-assistant/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   └── index.html         # Main UI interface
├── static/                # Static assets (created automatically)
├── data/                  # Your document corpus goes here
└── README.md              # This documentation
```

## Customization

### Adding Your Documents

Place your documents (PDF, TXT, DOCX, etc.) in the `data` directory. The system will index them on startup.

### Changing the Model

To use a different model from Groq or change embedding model, edit the `initialize_models()` function in `app.py`:

```python
Settings.embed_model = HuggingFaceEmbedding(model_name="your-preferred-model")
Settings.llm = Groq(model="your-preferred-model", api_key="your-api-key")
```

### Modifying the UI

The UI is contained in a single HTML file (`templates/index.html`). You can customize the colors, layout, and behavior by editing the HTML, CSS, and JavaScript.

## Key Code Components

### Backend (app.py)

- **Flask Application**: Handles HTTP routes and requests
- **LlamaIndex Integration**: Sets up the RAG system with document indexing
- **Response Formatting**: Converts model responses to well-formatted HTML

### Frontend (index.html)

- **Modern Chat Interface**: Clean, responsive design with user/bot message bubbles
- **Dynamic Typing Indicator**: Shows when the system is generating a response
- **Code Syntax Highlighting**: Makes code snippets readable and attractive
- **Auto-resizing Input**: Text area that grows as you type longer messages

## Performance Tips

- For large document collections, the initial indexing might take some time
- Consider pre-processing your documents for better results (removing noise, etc.)
- Adjust the context window or retrieval parameters in LlamaIndex for different use cases

## Dependencies

- Flask
- LlamaIndex
- Groq Python SDK
- Markdown
- HuggingFace Transformers (for embeddings)

## License

[MIT License](LICENSE)

## Acknowledgements

- [LlamaIndex](https://www.llamaindex.ai/) - For the RAG framework
- [Groq](https://groq.com/) - For the fast LLM API
- [HuggingFace](https://huggingface.co/) - For the embedding models
- [highlight.js](https://highlightjs.org/) - For code syntax highlighting

---

Created with ❤️ by [Abdur Rehman]
