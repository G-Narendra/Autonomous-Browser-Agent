
# 🤖 Autonomous Browser Agent
### LLM-Driven Web Automation & Intelligent Task Execution

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai">
<img src="https://img.shields.io/badge/Playwright-Automation-2EAD33?style=for-the-badge&logo=playwright">
<img src="https://img.shields.io/badge/Framework-AsyncIO-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge">
</p>

---

## 🚀 Project Overview

The **Autonomous Browser Agent** is a sophisticated AI system that bridges the gap between LLM reasoning and web interaction. It interprets natural language commands, breaks them into executable steps, and navigates the live web to achieve complex goals without human oversight.

**Example Task:**
> "Find the top 3 trending AI news stories today and save a summary of each."

### Core Capabilities:
- **Natural Language Understanding:** Deciphering intent from complex instructions.
- **Dynamic Planning:** Creating and adjusting step-by-step action sequences.
- **Full Browser Control:** Clicking, typing, form-filling, and navigating via Playwright.
- **Data Extraction:** Scraping and structuring unstructured web data.

---

## 🧠 Tech Stack

| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Orchestration** | Asyncio / Nest_Asyncio |
| **Brain (LLM)** | OpenAI GPT / Google Gemini |
| **Automation** | Playwright |
| **Environment** | Virtualenv / Conda |
| **OS Support** | Windows, macOS, Linux |

---

## 📁 Project Structure

```text
autonomous_browser_agent/
├── agent/
│   ├── planner.py        # Task decomposition logic
│   ├── executor.py       # Action dispatcher
│   ├── memory.py         # Context & state management
│   └── tools.py          # LLM tool definitions
├── browser/
│   ├── controller.py     # Browser session management
│   └── actions.py        # Low-level interaction scripts
├── prompts/
│   └── system_prompt.txt # Core agent instructions
├── logs/                 # Execution & error logs
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
└── README.md             # Documentation

```



## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/G-Narendra/autonomous_browser_agent.git](https://github.com/G-Narendra/autonomous_browser_agent.git)
cd autonomous_browser_agent

```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv

```

### 3️⃣ Activate the Environment

**Windows:**

```bash
venv\Scripts\activate

```

**Mac/Linux:**

```bash
source venv/bin/activate

```

### 4️⃣ Install Dependencies & Playwright

```bash
pip install -r requirements.txt
playwright install

```

### 5️⃣ Set OpenAI API Key

**Windows (CMD):**

```bash
setx OPENAI_API_KEY "your_api_key_here"

```

**PowerShell:**

```bash
$env:OPENAI_API_KEY="your_api_key_here"

```

---

## ▶️ Run the Project

```bash
python main.py

```

**Workflow:**

1. **Planner:** Maps out the necessary steps for the task.
2. **Controller:** Launches a Playwright browser instance.
3. **Executor:** Performs real-time clicks, searches, and navigation.
4. **Output:** Results are logged and printed to the console.

---

## ⚠️ Important Notes

### 🔸 GPU & API

* This agent requires a valid **OpenAI API Key**.
* Async execution is handled using `asyncio` and `nest_asyncio` for non-blocking operations.

### 🔸 Browser Behavior

* By default, Playwright may open a visible browser window.
* Ensure you have a stable internet connection for the LLM to process web content live.

---

## 🧪 Example Task

**Input Prompt:** > "Search for the latest Python 3.12 features and summarize them in bullet points."

---

## 🚀 Future Improvements

* [ ] **Advanced Memory:** Persistent storage for multi-session tasks.
* [ ] **Visual Reasoning:** Using GPT-4V to interpret UI elements visually.
* [ ] **Error Handling:** Robust retry logic for dynamic website changes.
* [ ] **UI Dashboard:** Integration with Gradio or Streamlit for monitoring.

---

## 👨‍💻 Author

**Narendra (G‑Narendra)** AI | ML | Python | Full Stack | GenAI Enthusiast

GitHub: [https://github.com/G-Narendra](https://www.google.com/search?q=https://github.com/G-Narendra)
