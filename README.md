# AI Engineering Capstone

A 6-week deep dive into AI/ML engineering, transitioning from neural network foundations to a production-grade multi-agent Information Retrieval system.

## Architecture
1. **Phase 1 (01_foundations/):** Manual backpropagation, Transformer architecture, and local SLM inference optimizations.
2. **Phase 2 (02_ir_and_agents/):** Hybrid search (BM25 + Vectors), stateful orchestration via LangGraph, and automated evaluations.
3. **Phase 3 (03_capstone_wiki_engine/):** An Autonomous Wikipedia Research Engine deployed on AWS.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
make setup
make jupyter
