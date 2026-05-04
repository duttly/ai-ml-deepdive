# AI/ML 5-Week Deep Dive Plan

## Overview

This is a 5-week, full-time plan to:

- Build neural networks and transformers from scratch
- Train a minimal GPT-style language model
- Develop deep intuition for embeddings and retrieval
- Build production-grade RAG systems and AI agents
- Design and deploy real-world AI systems

---

## Core References

### Foundations
- Karpathy micrograd: https://github.com/karpathy/micrograd
- Neural Networks: Zero to Hero (YouTube)

### Transformers
- Attention Is All You Need: https://arxiv.org/abs/1706.03762

### GPT / Training
- nanoGPT: https://github.com/karpathy/nanoGPT

### Retrieval
- FAISS: https://github.com/facebookresearch/faiss
- Elasticsearch docs: https://www.elastic.co/guide/index.html

### Systems
- Designing Machine Learning Systems — Chip Huyen

---

## Week 1 — Neural Networks from Scratch

### Goal
Understand and implement backpropagation and training loops from first principles.

### Plan

**Day 1 — Autograd Basics**
- Watch micrograd introduction
- Implement scalar autograd (addition, multiplication)

**Day 2 — Backpropagation**
- Implement backward pass
- Visualize computation graph

**Day 3 — Neural Network**
- Build a simple MLP (1 hidden layer)

**Day 4 — Training Loop**
- Add loss function (MSE)
- Implement gradient descent

**Day 5 — Optimization**
- Tune learning rate
- Track and plot loss

**Day 6 — Code Reading**
- Study micrograd source code

**Day 7 — Consolidation**
- Refactor code
- Write documentation
- Validate conceptual understanding

---

## Week 2 — Transformers

### Goal
Understand and implement transformer architecture.

### Plan

**Day 8 — Transformer Paper**
- Read and summarize key concepts

**Day 9 — Attention**
- Implement scaled dot-product attention

**Day 10 — Single-Head Attention**
- Wrap attention into module

**Day 11 — Multi-Head Attention**
- Extend to multi-head attention

**Day 12 — Positional Encoding**
- Implement sinusoidal positional encoding

**Day 13 — Transformer Block**
- Combine attention, feedforward, residuals, layer norm

**Day 14 — Consolidation**
- Test on toy sequence task
- Write explanation of attention

---

## Week 3 — GPT + Tokenization

### Goal
Train a minimal GPT-style language model.

### Plan

**Day 15 — Tokenization**
- Study BPE
- Implement simple tokenizer

**Day 16 — Dataset**
- Prepare dataset (e.g., Shakespeare)

**Day 17 — Training**
- Train small GPT model

**Day 18 — Logits**
- Inspect outputs and softmax behavior

**Day 19 — Sampling**
- Implement temperature, top-k, top-p

**Day 20 — Debugging**
- Overfit small dataset
- Analyze behavior

**Day 21 — Consolidation**
- Clean training pipeline
- Document results

---

## Week 4 — Embeddings, Retrieval, RAG

### Goal
Build a production-grade retrieval system.

### Plan

**Day 22 — Embeddings**
- Study embedding space and similarity metrics

**Day 23 — Vector Search**
- Build FAISS index

**Day 24 — Dense Retrieval**
- Implement semantic search pipeline

**Day 25 — Hybrid Search**
- Add BM25 using Elasticsearch

**Day 26 — Reranking**
- Implement second-stage ranking

**Day 27 — RAG Pipeline**
- Build full retrieval → generation pipeline

**Day 28 — Evaluation**
- Create evaluation dataset
- Measure retrieval and answer quality

---

## Week 5 — Agents, Systems, Deployment

### Goal
Build and deploy real-world AI systems.

### Plan

**Day 29 — Tool Use**
- Implement function calling

**Day 30 — Agents**
- Build multi-step agent

**Day 31 — Memory**
- Add retrieval-based memory

**Day 32 — Evaluation**
- Measure task success rates

**Day 33 — System Design**
- Write architecture document

**Day 34 — Deployment**
- Containerize with Docker
- Run locally or deploy

**Day 35 — Final Polish**
- Clean codebase
- Add diagrams
- Prepare demo

---

## Success Criteria

- Explain transformers and attention clearly
- Train a GPT-style model from scratch
- Build a production-grade RAG system
- Design and deploy an AI system end-to-end
- Debug model and retrieval failures effectively
