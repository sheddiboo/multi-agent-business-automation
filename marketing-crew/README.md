# 🚀 Marketing Crew: Multi-Agent AI Pipeline

An automated marketing orchestration system built with **CrewAI**. This project leverages high-performance LLMs (**Cerebras** for complex reasoning and **Groq** for rapid content generation) to handle everything from market research to SEO-optimized blog drafts.

## 🛠 Features
- **Dual-LLM Architecture**: 
    - **Cerebras (Llama 3.3 70B)**: Used for high-logic tasks like strategy, research, and SEO.
    - **Groq (Llama 3.3 70B Versatile)**: Used for high-speed creative writing and social media drafts.
- **Structured Output**: Uses Pydantic schemas to ensure content is returned in valid JSON format for easy integration.
- **Sequential Workflow**: Ensures data flows logically from research -> strategy -> calendar -> content creation.

## 📁 Project Structure
```text
marketing_crew/
├── crew.py                # Core CrewAI logic and agent definitions
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API Keys)
└── config/
    ├── agents.yaml        # Agent personas and backstories
    └── tasks.yaml         # Task descriptions and expected outputs

```

## ⚙️ Setup & Installation

1. **Clone the Repository**:
Navigate to your project directory.
2. **Install Dependencies**:
```bash
pip install -r requirements.txt

```


3. **Environment Configuration**:
Create a `.env` file in the root directory and add your API keys:
```env
CEREBRAS_API_KEY=your_cerebras_key_here
GROQ_API_KEY=your_groq_key_here
SERPER_API_KEY=your_serper_dev_key_here

```



## 🚀 Usage

The pipeline is currently configured to market an **AI-Powered Excel Automation Tool**. To run the crew, execute:

```bash
python crew.py

```

### Input Parameters

You can modify the `inputs` dictionary in `main.py` to target different products:

* `product_name`: The name of the service/tool.
* `target_audience`: The specific niche (e.g., SMEs, Data Analysts).
* `budget`: Marketing budget for context.

## 🤖 Agent Roles

* **Head of Marketing**: Orchestrates research and high-level strategy.
* **Social Media Creator**: High-speed generation of Reel scripts and post drafts.
* **Content Writer**: Specialized in deep-dive technical blog posts.
* **SEO Specialist**: Final pass optimization for search engine ranking.


```
📄 Credits & License
Original framework logic inspired by Codebasics. Modified for Groq/Cerebras hybrid orchestration.