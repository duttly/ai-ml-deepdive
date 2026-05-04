# 30-Day AI/ML Engineering Upskill Tracker

## Week 1: Foundations & Local SLMs
**Objective:** Understand transformer mechanics at the code level and deploy quantized models locally.

- [ ] **Day 1: The Math & Micro-Autograd**
  - [ ] Watch: [The spell book of machine learning (Karpathy)](https://www.youtube.com/watch?v=VMj-3S1tku0)
  - [ ] Code: Clone and trace through [Micrograd](https://github.com/karpathy/micrograd) to see backpropagation implemented in pure Python.
- [ ] **Day 2: The Core Architecture**
  - [ ] Read: [Attention Is All You Need (Original Paper)](https://arxiv.org/abs/1706.03762)
  - [ ] Read: [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) for the visual intuition.
- [ ] **Day 3: Building a Transformer**
  - [ ] Watch & Code: [Let's build GPT: from scratch (Karpathy)](https://www.youtube.com/watch?v=kCc8FmEb1nY). Write the self-attention block yourself.
- [ ] **Day 4: Local Model Infrastructure**
  - [ ] Install: [Ollama](https://github.com/ollama/ollama).
  - [ ] Execute: Pull and run `llama3` locally via the CLI.
- [ ] **Day 5: High-Throughput Serving**
  - [ ] Read: [vLLM Documentation](https://docs.vllm.ai/en/latest/).
  - [ ] Execute: Serve a model using vLLM to understand PagedAttention and memory management.
- [ ] **Day 6: Quantization & Hardware Constraints**
  - [ ] Read: [Introduction to Weight Quantization](https://huggingface.co/blog/merve/quantization).
  - [ ] Execute: Compare the VRAM usage and inference speed of an 8-bit vs 4-bit quantized model locally.
- [ ] **Day 7: Week 1 Review & Environment Hardening**
  - [ ] Clean up your Python virtual environments (ensure PyTorch with CUDA/Metal support is properly configured).

## Week 2: Tool Orchestration & Action Models
**Objective:** Move from text generation to system execution using strict data contracts.

- [ ] **Day 8: Advanced RAG - Vector DBs**
  - [ ] Install: Spin up a local [ChromaDB](https://docs.trychroma.com/) or [Milvus](https://milvus.io/) instance.
  - [ ] Execute: Ingest a small dataset using OpenAI or local embeddings.
- [ ] **Day 9: Advanced RAG - Hybrid Search & Re-ranking**
  - [ ] Read: [Cohere's guide to Re-ranking](https://txt.cohere.com/rerank/).
  - [ ] Code: Implement a two-stage retrieval pipeline (BM25 for keywords + Vector for semantics, then re-rank).
- [ ] **Day 10: Function Calling (Tool Use) Basics**
  - [ ] Read: [OpenAI Function Calling Docs](https://platform.openai.com/docs/guides/function-calling).
  - [ ] Code: Define a Python function and force the LLM to output the exact JSON arguments required to execute it.
- [ ] **Day 11: Constrained Generation**
  - [ ] Read: [Outlines documentation](https://github.com/outlines-dev/outlines).
  - [ ] Code: Force a local SLM to generate output that strictly adheres to a complex JSON schema or Regex pattern.
- [ ] **Day 12: Building a Single-Agent Loop**
  - [ ] Code: Create a basic `while` loop script where an LLM is given a goal, decides on a tool, parses the tool's output, and decides if it is finished.
- [ ] **Day 13: Evals & Telemetry**
  - [ ] Install: [DeepEval](https://github.com/confident-ai/deepeval) or [Ragas](https://github.com/explodinggradients/ragas).
  - [ ] Code: Write a unit test for your RAG pipeline from Day 9 using an "LLM-as-a-judge" metric (e.g., Answer Relevance).
- [ ] **Day 14: Week 2 Review**
  - [ ] Refactor your agent loop to handle tool-execution failures gracefully (e.g., when the DB returns a timeout or NULL).

## Week 3: Multi-Agent Systems & Distributed State
**Objective:** Coordinate specialized models while managing global state and eventual consistency across nodes.

- [ ] **Day 15: Introduction to Graph Orchestration**
  - [ ] Read: [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/).
  - [ ] Code: Convert your Day 12 `while` loop into a formal State Graph.
- [ ] **Day 16: Managing Global State in AI**
  - [ ] Concept Check: Map how state is passed between nodes in LangGraph. Address how this mirrors distributed coordination models you are familiar with (like managing global values without violating CAP theorem constraints).
- [ ] **Day 17: Multi-Agent Collaboration**
  - [ ] Read: [CrewAI Documentation](https://docs.crewai.com/).
  - [ ] Code: Set up a two-agent system (e.g., a "Researcher" and a "Writer").
- [ ] **Day 18: Human-in-the-Loop (HITL)**
  - [ ] Code: Add an interrupt to your LangGraph state machine that pauses execution and requires manual terminal input before proceeding to a destructive action (like dropping a table or pushing code).
- [ ] **Day 19: Agentic Routing**
  - [ ] Code: Build a "Router" node that assesses a user query and decides whether to send it to an analytical agent or a creative agent.
- [ ] **Day 20: Memory & Persistence**
  - [ ] Code: Connect your LangGraph state to a persistent SQLite or Redis backend so a conversation/task can be paused and resumed later.
- [ ] **Day 21: Week 3 Review**
  - [ ] Break your multi-agent system on purpose to test the routing resilience.

## Week 4: The Hybrid Capstone (Production on AWS)
**Objective:** Build and deploy a resilient routing gateway bridging managed APIs and self-hosted open-weights models.

- [ ] **Day 22: Gateway Architecture & Bedrock Setup**
  - [ ] Docs: [Amazon Bedrock API Setup](https://docs.aws.amazon.com/bedrock/latest/userguide/api-setup.html).
  - [ ] Code: Write a FastAPI endpoint that successfully calls a Claude model via Bedrock.
- [ ] **Day 23: Deploying the Local Fleet**
  - [ ] Docs: [Deploy Llama 3 on Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/deploy-meta-llama-3-models-on-amazon-sagemaker/).
  - [ ] Code: Containerize your local model from Week 1 using Docker and deploy it to an AWS endpoint (ECS or SageMaker).
- [ ] **Day 24: Implementing the Traffic Cop**
  - [ ] Code: Expand your FastAPI gateway. Write logic to inspect the prompt length and complexity, routing simple requests to the SageMaker SLM and complex ones to Bedrock.
- [ ] **Day 25: Fallbacks and Retries**
  - [ ] Code: Implement exponential backoff and automatic failover. If Bedrock rate-limits you, the system should seamlessly retry using the internal SLM.
- [ ] **Day 26: Tracing & Observability**
  - [ ] Install: [Phoenix (Arize AI)](https://github.com/Arize-ai/phoenix) or setup LangSmith.
  - [ ] Code: Instrument your FastAPI app so you can visually trace the spans of every agent step and routing decision.
- [ ] **Day 27: Cost Optimization Logging**
  - [ ] Code: Add a middleware layer that calculates and logs the exact token cost of every request to a database, distinguishing between local hardware costs and external API costs.
- [ ] **Day 28: Security & Guardrails**
  - [ ] Read: [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails).
  - [ ] Code: Add a moderation layer that intercepts and blocks prompts attempting to jailbreak the system.
- [ ] **Day 29: End-to-End Testing**
  - [ ] Send 100 concurrent requests to your Gateway and monitor the routing behavior, cost logs, and error rates.
- [ ] **Day 30: System Review & Documentation**
  - [ ] Finalize the architecture diagram.
  - [ ] Document the endpoints and deployment steps.
