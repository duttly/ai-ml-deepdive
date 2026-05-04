# AI/ML 5-Week Deep Dive — Execution Table (Annotated)

Legend:
- ⏱ = estimated focused hours
- 🎯 = difficulty
- ⚠️ = execution guidance

---

| Day | Area | Focus | Tasks | Output | References | ⏱ | 🎯 | Guidance |
|-----|------|------|------|--------|------------|----|----|----------|
| 1 | Foundations | Autograd | Karpathy micrograd intro; scalar autograd (add, mul) | Autograd engine | micrograd | 6h | High | ⚠️ Go deep: understand computation graph |
| 2 | Foundations | Backprop | Implement backward pass; graph visualization | Backprop engine | micrograd | 6h | High | ⚠️ Core concept: no shortcuts |
| 3 | Foundations | MLP | Build 1-hidden-layer NN | MLP | micrograd | 5h | Medium | ⚠️ Don’t optimize architecture |
| 4 | Foundations | Training | MSE loss + gradient descent loop | Training loop | Karpathy | 5h | Medium | ⚠️ Focus on correctness |
| 5 | Foundations | Optimization | Tune LR, plot loss curves | Stable training | — | 4h | Medium | ⚠️ Don’t over-tune |
| 6 | Foundations | Code Reading | Deep dive micrograd source | Understanding | micrograd | 4h | High | ⚠️ Go slow, trace execution |
| 7 | Foundations | Consolidation | Refactor + explain backprop | Clean repo | — | 3h | Low | ⚠️ Just clarity, not perfection |
| 8 | Transformers | Paper | Read Attention Is All You Need | Notes | arxiv | 4h | High | ⚠️ Focus intuition, skip math |
| 9 | Transformers | Attention | Implement scaled dot-product attention | Attention fn | paper | 6h | High | ⚠️ Must implement from scratch |
| 10 | Transformers | Single Head | Build attention module | Module | — | 5h | High | ⚠️ No libraries shortcuts |
| 11 | Transformers | Multi-Head | Extend to multi-head | Multi-head | — | 5h | High | ⚠️ Understand projections |
| 12 | Transformers | Positional Encoding | Implement sinusoidal encoding | Encoded input | paper | 3h | Medium | ⚠️ Straightforward |
| 13 | Transformers | Block | Build transformer block | Block | — | 6h | High | ⚠️ Critical integration point |
| 14 | Transformers | Consolidation | Toy task test + explanation | Mini transformer | — | 4h | Medium | ⚠️ Write intuition clearly |
| 15 | GPT | Tokenization | Study + implement BPE | Tokenizer | nanoGPT | 5h | High | ⚠️ Understand merges deeply |
| 16 | GPT | Dataset | Build dataset pipeline | Data loader | nanoGPT | 3h | Low | ⚠️ Don’t over-engineer |
| 17 | GPT | Training | Train mini GPT | Model | nanoGPT | 6h | High | ⚠️ Watch loss behavior |
| 18 | GPT | Logits | Inspect outputs | Debug insights | — | 3h | Medium | ⚠️ Focus interpretation |
| 19 | GPT | Sampling | Implement decoding strategies | Sampler | — | 4h | Medium | ⚠️ Explore behavior |
| 20 | GPT | Debugging | Overfit small dataset | Insights | — | 4h | High | ⚠️ Important learning moment |
| 21 | GPT | Consolidation | Clean pipeline | GPT repo | — | 3h | Low | ⚠️ Don’t refactor endlessly |
| 22 | Retrieval | Embeddings | Study embedding geometry | Notes | HF docs | 4h | Medium | ⚠️ Understand cosine meaning |
| 23 | Retrieval | Vector Search | Build FAISS index | Search system | FAISS | 5h | High | ⚠️ Core IR skill |
| 24 | Retrieval | Dense Retrieval | Semantic search pipeline | Search | — | 5h | High | ⚠️ Focus recall |
| 25 | Retrieval | Hybrid | Add BM25 (Elasticsearch) | Hybrid system | ES | 6h | High | ⚠️ Leverage IR expertise |
| 26 | Retrieval | Reranking | Add reranker | Better ranking | HF | 4h | Medium | ⚠️ Don’t over-model |
| 27 | Retrieval | RAG | Full pipeline | RAG system | — | 6h | High | ⚠️ System integration |
| 28 | Retrieval | Eval | Build eval set + metrics | Eval harness | IR metrics | 5h | High | ⚠️ Critical step |
| 29 | Systems | Tools | Function calling | Tool LLM | APIs | 4h | Medium | ⚠️ Keep simple |
| 30 | Systems | Agents | Multi-step agent | Agent | LangChain | 6h | High | ⚠️ Focus flow, not features |
| 31 | Systems | Memory | Add retrieval memory | Stateful agent | — | 4h | Medium | ⚠️ Avoid overcomplex memory |
| 32 | Systems | Eval | Measure task success | Metrics | — | 4h | High | ⚠️ Be rigorous |
| 33 | Systems | Design | Architecture doc | Design doc | Chip Huyen | 3h | Medium | ⚠️ Think systems |
| 34 | Systems | Deploy | Dockerize service | Running app | Docker | 5h | Medium | ⚠️ Keep deployment minimal |
| 35 | Systems | Polish | Clean + diagrams + demo | Portfolio | — | 4h | Low | ⚠️ Final polish only |
