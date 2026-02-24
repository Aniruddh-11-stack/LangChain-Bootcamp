# 🦜🔗 LangChain & LangGraph Bootcamp

> Notes, exercises, and implementations from my self-study of LangChain and LangGraph — the leading frameworks for building production-grade LLM applications in Python.

---

## 📁 Repository Structure

```
LangChain-LangGraph-Bootcamp/
│
├── LangChain_with_Python_Bootcamp_Part_I.ipynb      # LLMs, Prompt Templates, Output Parsers
├── LangChain_with_Python_Bootcamp_Part_II.ipynb     # Document Loaders, RAG, Chains, Vector Stores
├── Langchain_with_Python_Bootcamp_Part_III.ipynb    # Function Calling, Memory, Agents & Tools
├── .env.example                                      # API key template
└── README.md
```

---

## 📓 Notebooks

### `LangChain_with_Python_Bootcamp_Part_I.ipynb`

Foundations of building LLM-powered applications with LangChain:

| Topic | Description |
|-------|-------------|
| **LLMs & Chat Models** | Interact with language models via `LLM` and `ChatModel` interfaces |
| **Prompt Templates** | Structure dynamic prompts using `PromptTemplate` and `ChatPromptTemplate` |
| **Few-Shot Prompting** | Guide model behaviour using `FewShotPromptTemplate` with curated examples |
| **Output Parsers** | Parse and structure model responses using LangChain's output parser utilities |

---

### `LangChain_with_Python_Bootcamp_Part_II.ipynb`

Deep dive into data handling, Retrieval-Augmented Generation (RAG), and LangChain chains:

| Topic | Description |
|-------|-------------|
| **Document Loaders** | Load data from CSV, text files, and PDFs using `CSVLoader`, `TextLoader`, and integrations |
| **Text Splitting** | Chunk large documents with `CharacterTextSplitter` (tiktoken-based) |
| **Text Embeddings** | Generate semantic embeddings with `OpenAIEmbeddings` |
| **ChromaDB Vector Store** | Store, persist, and reload embeddings for semantic search |
| **Legal Research Bot** | Build a Q&A bot on the US Constitution using RAG |
| **LLMChain** | Combine prompt templates and models into reusable chains |
| **Sequential Chains** | Build multi-step pipelines with `SimpleSequentialChain` and `SequentialChain` |
| **Transform Chain** | Preprocess inputs with custom transformation logic before passing to a model |

---

### `Langchain_with_Python_Bootcamp_Part_III.ipynb`

Advanced LangChain: agents, tool use, and conversation memory:

| Topic | Description |
|-------|-------------|
| **OpenAI Function Calling** | Use OpenAI's function-calling API within LangChain chains without Pydantic |
| **MathChain** | Solve mathematical problems using LangChain's `LLMMathChain` |
| **ChatMessageHistory** | Track conversation history with the `ChatMessageHistory` object |
| **ConversationBufferMemory** | Maintain full conversation history in memory |
| **ConversationBufferWindowMemory** | Keep only the most recent N exchanges in memory |
| **ConversationSummaryMemory** | Condense long conversation histories into summaries using an LLM |
| **Agent Basics** | Understand how LangChain agents reason and decide which tools to use |
| **Agent Tools** | Equip agents with tools (search, calculators, APIs) for real-world task solving |

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

## 🧠 Learning Path

The three notebooks follow a structured progression:

```
Part I  →  LLM Fundamentals, Prompt Engineering, Output Parsers
Part II →  RAG Pipeline, Vector Stores, Document Loaders, Chains
Part III → Function Calling, Conversation Memory, Agents & Tools
```

These notebooks are from my bootcamp study of the LangChain and LangGraph ecosystem, completed alongside the **Persistent Systems Mentorship Programme**.

LangChain is the backbone of most production LLM applications, enabling chaining of prompts, models, tools, and memory. LangGraph extends it to build stateful, multi-actor agent systems.

---

## 📄 License

Open-source under the [MIT License](LICENSE).
