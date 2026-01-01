
# 🤖 Agentic AI & Automation

Welcome to my repository for advanced AI agent orchestration and automation workflows. This project showcases the implementation of multi-agent systems designed for business intelligence, marketing, and data automation, with a focus on high-performance execution.

## 💡 Inspiration & Attribution
This repository is heavily inspired by the **Codebasics** agentic AI framework. The core logic has been re-engineered and optimized to move from a standard single-LLM setup (Gemini) to a high-performance **Hybrid Architecture** (Cerebras + Groq), specifically tailored for low-latency business automation.

## 🌟 Featured Project: Hybrid Marketing Crew
The flagship project in this repository is the **Marketing Crew**, which implements a state-of-the-art hybrid LLM architecture.

### Key Innovations:
- **Cerebras Integration**: Utilizing `llama-3.3-70b` for deep reasoning, technical SEO, and market research.
- **Groq Acceleration**: Leveraging `llama-3.3-70b-versatile` for near-instant creative writing and social media content generation.
- **Structured Logic**: Built on the **CrewAI** framework, transitioning to a performance-optimized model.

---

## 📂 Repository Structure

```text
.
├── marketing-crew/              # Primary Automated Marketing Pipeline
│   ├── config/                  # YAML files defining Agent personas and Task details
│   ├── resources/               # Directory for generated marketing outputs
│   │   └── drafts/              # Specific storage for strategy and calendar .md files
│   ├── crew.py                  # Main execution logic (Cerebras/Groq Hybrid)
│   ├── README.md                # Project-specific documentation for the Marketing Crew
│   └── requirements.txt         # Dependencies specific to the marketing pipeline
├── config/                      # Global configuration files for root-level crews
├── .env                         # [HIDDEN] API keys for Cerebras, Groq, and Serper
├── .gitignore                   # Instructions for Git to ignore .env and cache files
├── .python-version              # Local Python version specification
├── crew.ipynb                   # Interactive notebook for testing general crew logic
├── crew_with_tool.ipynb         # Research: Testing custom tool integrations with CrewAI
├── email_agent_with_tool.py     # Specialized agent script for automated email outreach
├── email_agent.ipynb            # Notebook for prototyping email automation workflows
├── my_crew.py                   # Simplified "BlogCrew" prototype and baseline testing
├── pyproject.toml               # Modern Python packaging and dependency configuration
├── requirements.txt             # Global dependencies for the entire repository
└── README.md                    # Main portfolio documentation (this file)
```

---

## 🚀 Performance Comparison

| Feature | Codebasics Original | My Hybrid Implementation |
| --- | --- | --- |
| **LLM Provider** | Google Gemini | **Cerebras + Groq** |
| **Speed (Creative)** | Standard | **Ultra-Low Latency (Groq)** |
| **Reasoning (Depth)** | Balanced | **High-Throughput (Cerebras 70B)** |
| **Target Market** | General | **SMEs / Tech-Adjacent (NGN Context)** |

---

## 🛠 Tech Stack

* **Frameworks**: CrewAI, LangChain
* **LLMs**: Llama 3.3 70B (via Cerebras & Groq)
* **Tools**: Serper Dev (Search), ScrapeWebsite, FileSystem Tools
* **Environment**: Python 3.10+, Pydantic (Structured Data)

---

## 📖 How to Use

## 📖 How to Use

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/sheddiboo/multi-agent-business-automation.git](https://github.com/sheddiboo/multi-agent-business-automation.git)
```


2. **Setup Environment**:
Create a `.env` file with your `CEREBRAS_API_KEY`, `GROQ_API_KEY`, and `SERPER_API_KEY`.
3. **Run a Crew**:
Navigate to a specific project folder and execute the main script:
```bash
cd marketing-crew
python crew.py

```



---

## 📄 License

This project is for educational and portfolio purposes.
Original framework logic inspired by Codebasics. Modified for hybrid performance.
