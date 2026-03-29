<div align="center">

<br/>

```
███████╗██╗  ██╗███████╗██╗     ██╗         ██╗     ███████╗███╗   ██╗███████╗
██╔════╝██║  ██║██╔════╝██║     ██║         ██║     ██╔════╝████╗  ██║██╔════╝
███████╗███████║█████╗  ██║     ██║         ██║     █████╗  ██╔██╗ ██║███████╗
╚════██║██╔══██║██╔══╝  ██║     ██║         ██║     ██╔══╝  ██║╚██╗██║╚════██║
███████║██║  ██║███████╗███████╗███████╗    ███████╗███████╗██║ ╚████║███████║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝
```

### **Terminal-First Agentic AI Copilot for Machine Learning Engineers**

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-0A0A0A?style=for-the-badge&logo=python&logoColor=00FF88&labelColor=0A0A0A)](https://python.org)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-0A0A0A?style=for-the-badge&logoColor=00FF88&labelColor=0A0A0A)](https://langchain-ai.github.io/langgraph/)
[![Docker](https://img.shields.io/badge/Docker-Ready-0A0A0A?style=for-the-badge&logo=docker&logoColor=00FF88&labelColor=0A0A0A)](https://hub.docker.com/r/shivashish23/shellens-ai)
[![Groq](https://img.shields.io/badge/LLM-Groq%20Llama--3-0A0A0A?style=for-the-badge&logoColor=00FF88&labelColor=0A0A0A)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-0A0A0A?style=for-the-badge&logoColor=00FF88&labelColor=0A0A0A)](./LICENSE)

<br/>

> *Built for ML Engineers who want to move fast and break nothing.*

<br/>

---

</div>

<br/>

## ◈ What is Shell Lens?

**Shell Lens** is NOT a chatbot. NOT a simple code generator. NOT just another AutoML wrapper.

Shell Lens is a **terminal-first, agentic AI copilot** built specifically for Machine Learning Engineers who need to automate repetitive data science and data engineering work — securely, directly from the CLI.

Think of it as an **intelligent ML teammate** that can think, plan, execute, evaluate, and improve its own decisions — step by step — without ever leaving your terminal.

<br/>

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   Query  ──▶  Understand  ──▶  Plan  ──▶  Execute  ──▶  Reflect        │
│                                                              │           │
│                         Respond  ◀────────── Adapt  ◀───────┘           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## ⚡ Core Capabilities

Shell Lens empowers your terminal to **autonomously**:

<br/>

| Capability | Description |
|:---|:---|
| `📊` **Dataset Analysis** | Generate summaries, statistics, and distribution reports automatically |
| `🔗` **Feature Relationships** | Map correlations, dependencies, and inter-feature dynamics |
| `🧹` **Data Processing & Cleaning** | Impute missing values, drop nulls, format and normalize columns |
| `📉` **Visualization Engine** | Render matplotlib / seaborn plots from plain natural language |
| `🧠` **Intelligent Reasoning** | Evaluate skewness, recommend transformations (e.g. `log1p`), prepare data for training |

<br/>

---

<br/>

## 🚀 Quickstart — Docker (Recommended)

> No Python installs. No virtual environments. No dependency hell.
> The fastest and safest way to run Shell Lens is inside its **pre-built, isolated Docker container**.

<br/>

### Step 1 — Configure your control plane

Create a `.env` file in your working directory and add your Groq API key.
Get one free at [console.groq.com](https://console.groq.com).

```bash
GROQ_API_KEY=gsk_your_api_key_here
```

<br/>

### Step 2 — Ingest your data

Mount your local directory into the container and load your dataset (CSV or Parquet) into system memory:

```bash
# Load a dataset named 'test_data.csv' from your current folder
docker run -it \
  --env-file .env \
  -v "$(pwd):/app" \
  shivashish23/shellens-ai:latest \
  load-data test_data.csv
```

<br/>

### Step 3 — Initiate the Agentic Chat

Start the interactive session. The LangGraph orchestration engine will wake up and connect to your data:

```bash
docker run -it \
  --env-file .env \
  -v "$(pwd):/app" \
  shivashish23/shellens-ai:latest \
  chat
```

<br/>

---

<br/>

## 🧠 Example Prompt

Once inside the Shell Lens interface, issue complex, multi-step natural language operations:

```
$ shellens chat

◈ Shell Lens v1.0 — Agentic ML Copilot Initialized
◈ Dataset loaded: test_data.csv  [2,340 rows × 18 cols]
◈ LangGraph agent ready.

You ▶  "Give me a brief summary of this dataset. Are there any missing values?
        If there are, fill the missing numeric values with the median,
        then plot a correlation matrix of the numerical columns."

Shell Lens ▶  [Profiling dataset...]
              [Planning 3-step execution...]
              [Step 1/3] Generating dataset summary ✓
              [Step 2/3] Filling 142 missing values with column medians ✓
              [Step 3/3] Rendering correlation matrix → correlation_matrix.png ✓

              Done. All tasks completed in 4.2s.
```

<br/>

---

<br/>

## 🏗️ Architecture

Shell Lens implements a **Stateful Multi-Agent Workflow** orchestrated via **LangGraph**. Unlike standard zero-shot LLM prompts, Shell Lens operates as a dynamic state machine that routes through specialized cognitive nodes:

<br/>

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        SHELL LENS — AGENT PIPELINE                           │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   │
│   │  PROFILER   │──▶│   PLANNER   │──▶│  EXECUTION  │──▶│ REFLECTION  │   │
│   │    NODE     │   │    NODE     │   │    NODE     │   │    NODE     │   │
│   │             │   │             │   │             │   │             │   │
│   │ Understands │   │  Builds     │   │  Runs safe  │   │  Evaluates  │   │
│   │ intent &    │   │  step-by-   │   │  Python in  │   │  output &   │   │
│   │ data shape  │   │  step plan  │   │  sandbox    │   │  self-heals │   │
│   └─────────────┘   └─────────────┘   └─────────────┘   └──────┬──────┘   │
│                                                                  │          │
│                                                         ┌────────▼──────┐   │
│                                                         │   RESPONSE    │   │
│                                                         │     NODE      │   │
│                                                         │               │   │
│                                                         │ Formats and   │   │
│                                                         │ delivers back │   │
│                                                         └───────────────┘   │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│   CONTROL PLANE  │  LangChain + Groq Llama-3 (reasoning, code generation)  │
│   DATA PLANE     │  pandas · scikit-learn · matplotlib (deterministic)      │
│   SECURITY MODEL │  Hardened Docker sandbox — exec() never touches host OS  │
└──────────────────────────────────────────────────────────────────────────────┘
```

<br/>

### Control Plane
Uses **LangChain** and **Groq's low-latency Llama-3 models** for reasoning, intent extraction, and dynamic Python code generation.

### Data Plane
Powered by **deterministic Python tools** — pandas, scikit-learn, matplotlib — to prevent AI hallucinations during data mutation.

### Security Model
Operates entirely within a **hardened Docker environment** to sandbox the `exec()` engine, preventing the LLM from interacting with your host operating system.

<br/>

---

<br/>

## 🛠️ Native Setup — For Developers

Want to modify the LangGraph architecture, add custom tools, or run locally without Docker? Follow the steps below.

<br/>

**Requirements**
- Python 3.10 or higher
- A local virtual environment manager

<br/>

```bash
# 1. Clone the repository
git clone https://github.com/shivashish23/shell-lens.git
cd shell-lens

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate

# 3. Install the package in editable mode
pip install -e .

# 4. Configure your environment variables
echo "GROQ_API_KEY=gsk_yourkeyhere" > .env

# 5. Verify the CLI is working
shellens --help
```

<br/>

---

<br/>

## 💻 Tech Stack

<br/>

| Layer | Technology |
|:---|:---|
| **Orchestration** | LangGraph, LangChain |
| **CLI Framework** | Typer, Rich |
| **Data Engine** | Pandas, NumPy, PyArrow |
| **Machine Learning** | Scikit-Learn, SciPy |
| **Visualization** | Matplotlib, Seaborn |
| **LLM Backend** | Groq — Llama-3 8b / 70b |
| **Deployment** | Docker |

<br/>

---

<br/>

## 🔮 Roadmap

<br/>

```
[▓▓▓▓▓▓▓▓▓░░]  v1.0  ·  Core agentic pipeline + Docker deployment     ✓ SHIPPED
[░░░░░░░░░░░]  v1.1  ·  DuckDB / Polars — lazy eval for large datasets   PLANNED
[░░░░░░░░░░░]  v1.2  ·  LangSmith Observability — token + flow tracing   PLANNED
[░░░░░░░░░░░]  v1.3  ·  AutoML-Lite — end-to-end training from CLI       PLANNED
[░░░░░░░░░░░]  v2.0  ·  VS Code Extension — Shell Lens in the IDE        PLANNED
```

<br/>

**DuckDB / Polars Integration** — Transitioning the data plane to lazy-evaluated query engines for larger-than-memory execution on real-world datasets.

**LangSmith Observability** — Visual flowcharts for tracking token usage, agent reasoning paths, and execution traces.

**AutoML-Lite** — Full end-to-end model training pipelines triggered entirely from natural language CLI commands.

**VS Code Extension** — Bringing Shell Lens directly into the IDE sidebar for engineers who prefer a hybrid workflow.

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

<br/>

---

<br/>

<div align="center">

**Shell Lens** — *Because your terminal deserves to think.*

<br/>

[![GitHub Stars](https://img.shields.io/github/stars/shivashish23/shell-lens?style=for-the-badge&color=00FF88&labelColor=0A0A0A&logo=github)](https://github.com/shivashish23/shell-lens)
[![Docker Pulls](https://img.shields.io/docker/pulls/shivashish23/shellens-ai?style=for-the-badge&color=00FF88&labelColor=0A0A0A&logo=docker)](https://hub.docker.com/r/shivashish23/shellens-ai)

<br/>

*Built for ML Engineers who want to move fast and break nothing.*

</div>
