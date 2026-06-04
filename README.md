# 🔬 ResearchMind AI

### Multi-Agent Research & Analysis System

ResearchMind AI is an AI-powered multi-agent research platform that autonomously searches the web, extracts relevant information, generates structured research reports, and critiques its own output using specialized AI agents.

Built using **LangChain**, **Gemini/Mistral**, **Tavily Search**, **BeautifulSoup**, and **Streamlit**.

---

## 🌐 Live Demo

🚀 **Try ResearchMind AI Live**

👉 **Live Application:** [[Click here]](https://researchmindaii.streamlit.app/)

Experience the complete Multi-Agent Research workflow directly from your browser without any installation or setup.

### What You Can Do

* 🔍 Search the web for recent and reliable information
* 📄 Extract detailed insights from relevant sources
* ✍️ Generate structured AI-powered research reports
* 🧐 Receive automated report reviews and quality scores
* 📊 Explore results through an interactive dashboard

---

## ✨ Features

### 🔍 Search Agent

* Searches the web using Tavily Search API
* Retrieves recent and trustworthy information
* Collects sources, URLs, and summaries

### 📄 Reader Agent

* Analyzes search results
* Selects the most relevant source
* Scrapes and extracts detailed content from web pages

### ✍️ Writer Agent

* Generates structured research reports
* Creates:

  * Introduction
  * Key Findings
  * Conclusion
  * Sources

### 🧐 Critic Agent

* Reviews generated reports
* Assigns quality scores
* Identifies strengths and improvement areas

### 🎨 Modern Dashboard

* Streamlit-powered interface
* Dark AI-inspired theme
* Research metrics
* Downloadable reports
* Interactive source inspection

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
Search Agent
    │
    ▼
Reader Agent
    │
    ▼
Writer Agent
    │
    ▼
Critic Agent
    │
    ▼
Final Research Report
```

---

## 🛠️ Tech Stack

### AI & LLMs

* Google Gemini
* Mistral AI
* LangChain

### Research Tools

* Tavily Search API
* BeautifulSoup
* Requests

### Frontend

* Streamlit

### Utilities

* Python Dotenv
* Rich

---

## 📂 Project Structure

```text
ResearchMind-AI/
│
├── app.py
├── agents.py
├── tools.py
├── pipeline.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Mishra108/researchmind-ai.git
cd researchmind-ai
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Use only the API keys required for your selected model.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. User enters a research topic.
2. Search Agent gathers information from the web.
3. Reader Agent extracts detailed content from relevant sources.
4. Writer Agent generates a structured research report.
5. Critic Agent evaluates the report and provides feedback.
6. Results are displayed through the Streamlit dashboard.

---

## 💡 Example Research Topics

* Future of AI Agents in 2026
* Impact of Generative AI on Education
* Quantum Computing Applications
* Renewable Energy Trends
* AI in Healthcare
* Autonomous Vehicles and Safety

---

## 🎯 Skills Demonstrated

* Multi-Agent AI Systems
* LangChain Agent Development
* Prompt Engineering
* Tool Calling
* Web Search Integration
* Web Scraping
* Generative AI Applications
* Streamlit Development
* LLM Orchestration

---

## 👨‍💻 Author

### Prem Mishra

B.Tech CSE (AI & ML)

Passionate about:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Agentic AI Systems
* Natural Language Processing

📧 Feel free to connect and collaborate on AI projects.

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.

Your support helps the project reach more developers, students, and AI enthusiasts.
