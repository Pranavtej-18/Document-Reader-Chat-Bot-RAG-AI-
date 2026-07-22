# 🤖 Document Reader Chatbot (RAG AI)

An AI-powered Document Reader Chatbot built using **LangChain, Google Gemini, FAISS, and Streamlit**. This application allows users to upload PDF documents and ask natural language questions. The chatbot retrieves the most relevant information from the uploaded document using **Retrieval-Augmented Generation (RAG)** and generates accurate responses with source references.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text extraction and chunking
- 🧠 Semantic search using Google Gemini Embeddings
- ⚡ Fast retrieval using FAISS Vector Store
- 🤖 AI-powered question answering using Gemini 2.5 Flash
- 💬 Interactive Streamlit chat interface
- 📚 Displays retrieved source chunks
- 📁 Shows source document information
- 🗑️ Clear chat functionality
- 🔄 Local vector database for faster responses

---

## 🏗️ Project Architecture

```
                PDF Upload
                     │
                     ▼
              Text Extraction
                     │
                     ▼
                Text Chunking
                     │
                     ▼
          Gemini Embeddings
                     │
                     ▼
             FAISS Vector Store
                     │
                     ▼
          Similarity Search (RAG)
                     │
                     ▼
              Gemini 2.5 Flash
                     │
                     ▼
              AI Generated Answer
                     │
                     ▼
            Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & LLM
- Google Gemini 2.5 Flash
- Gemini Embedding Model

### Frameworks & Libraries
- LangChain
- FAISS
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
Document-Reader-Chat-Bot-RAG-AI/
│
├── app.py                 # Streamlit Application
├── chatbot.py             # RAG Question Answering
├── ingest.py              # PDF Processing & Vector Store Creation
├── utils.py               # Utility Functions
├── requirements.txt
├── README.md
│
├── data/
│   └── Sample PDF
│
└── vectorstore/
    ├── index.faiss
    └── index.pkl
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/Document-Reader-Chat-Bot-RAG-AI.git

cd Document-Reader-Chat-Bot-RAG-AI
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📋 How It Works

1. Upload a PDF document.
2. Click **Process PDF**.
3. The document is:
   - Extracted
   - Split into chunks
   - Converted into embeddings
   - Stored inside a FAISS vector database
4. Ask any question related to the uploaded document.
5. The chatbot retrieves the most relevant chunks and sends them to Gemini for answer generation.
6. The application also displays the retrieved source chunks for transparency.

---

## 📸 Screenshots

> Add screenshots here after deployment.

Example:

```
screenshots/
    home.png
    upload.png
    chat.png
```

---

## 🎯 Future Enhancements

- ✅ Page-level source citations
- 📄 Multiple PDF support
- 🖼️ Image OCR support
- 📑 DOCX & TXT support
- 💾 Persistent chat history
- 🌐 Cloud deployment
- 🔍 Hybrid Search (BM25 + Dense Retrieval)
- 📊 Similarity score visualization

---

## 💡 Learning Outcomes

Through this project, I learned:

- Retrieval-Augmented Generation (RAG)
- Vector Databases (FAISS)
- Embedding Models
- Prompt Engineering
- Semantic Search
- LangChain Pipelines
- Streamlit Application Development
- Large Language Model Integration
- Document Question Answering Systems

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pranav**

If you found this project helpful, consider giving it a ⭐ on GitHub!
