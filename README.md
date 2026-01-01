
# 🤖 Agentic AI & Automation Portfolio

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
├── marketing-crew/          # [PRIMARY] Automated Marketing Pipeline
│   ├── config/              # Agent and Task YAML definitions
│   ├── resources/           # Generated drafts and marketing assets
│   ├── crew.py              # Main execution logic (Groq/Cerebras Hybrid)
│   └── README.md            # Marketing-specific documentation
├── crew_with_tool.ipynb     # Research: Testing custom tools with CrewAI
├── email_agent_with_tool.py # Automation: Specialized email outreach agent
├── my_crew.py               # Prototype: Baseline multi-agent configuration
└── requirements.txt         # Global dependencies

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

1. **Clone the repository**:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)

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
