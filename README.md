# 🦜🔗 LangChain & LangGraph Bootcamp

> Notes, exercises, and implementations from my self-study of LangChain and LangGraph — the leading frameworks for building production-grade LLM applications in Python.

---

## 📁 Repository Structure

```
LangChain-LangGraph-Bootcamp/
│
├── LangChain_with_Python_Bootcamp_Part_II.ipynb   # Document loaders, RAG, vector stores
├── .env.example                                    # API key template
└── README.md
```

---

## 📓 Notebooks

### `LangChain_with_Python_Bootcamp_Part_II.ipynb`

A deep dive into data handling and Retrieval-Augmented Generation (RAG) with LangChain:

| Topic | Description |
|-------|-------------|
| **Document Loaders** | Load data from CSV, text files, PDFs using `CSVLoader`, `TextLoader` |
| **Text Splitting** | Chunk large documents with `CharacterTextSplitter` (tiktoken-based) |
| **Embeddings** | Generate semantic embeddings with `OpenAIEmbeddings` |
| **ChromaDB Vector Store** | Store, persist, and reload embeddings for semantic search |
| **Contextual Compression** | Retrieve the most relevant chunks using `ContextualCompressionRetriever` + `LLMChainExtractor` |
| **OpenAI Function Calling** | Use OpenAI's function-calling API directly within LangChain chains |

---

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Aniruddh-11-stack/LangChain-LangGraph-Bootcamp.git
cd LangChain-LangGraph-Bootcamp
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -U langchain langchain-community langchain-openai langchain-chroma langgraph
pip install chromadb tiktoken openai sentence-transformers
pip install jupyter
```

### 4. Set Up API Keys
```bash
cp .env.example .env
```
Edit `.env` with your actual keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

Load in notebooks:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 5. Launch Jupyter
```bash
jupyter notebook
```

---

## 🔑 API Keys Required

| Service | Where to Get |
|---------|-------------|
| OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| Google Gemini | [console.cloud.google.com](https://console.cloud.google.com) |

> ⚠️ **Never hardcode API keys.** Always use `.env` files and load via `python-dotenv`.

---

## 🧠 About

These notebooks are from my bootcamp study of the LangChain and LangGraph ecosystem, completed alongside the **Persistent Systems Mentorship Programme**.

LangChain is the backbone of most production LLM applications, enabling chaining of prompts, models, tools, and memory. LangGraph extends it to build stateful, multi-actor agent systems.

---

## 📄 License

Open-source under the [MIT License](LICENSE).
