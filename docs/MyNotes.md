# My Notes/Questions :

## Architecture

**Day 1:** Learn Scalar Autograd (Understand `Value` & backprop) | [Micrograd Video](https://www.youtube.com/watch?v=VMj-3S1tku0)
- Qn1
- Qn2
---
**Day 2:** The Chain Rule in Code (Implement `_backward()`) | [Micrograd Source](https://github.com/karpathy/micrograd/blob/master/micrograd/engine.py)
- Qn3
- Qn4
---
 **Day 3:** Building an MLP (Neuron to Multi-Layer Perceptron)
- How do I determine the topology of an MLP ?
- How many layers ? How many neurons per layer ?
- Can I connect only a subset between layer1 and layer2 ?
- Can I directly connect from layer1 to layer3 ?

- nn.py only talks about 1 fwd and 1 bwd pass. The exact loss minimization is in demo.ipynb
---
### **Nice Example:**

#### **Initial State:**
*   Inputs: $x_1 = 2.0$, $x_2 = 0.5$
*   Target: $10.0$
*   Learning Rate ($\alpha$): $0.05$
*   Starting Weights: $w_1 = 0.5$, $w_2 = 0.5$, $b = 0.0$
---
#### **Iteration 1**
**1. Forward Pass (Prediction)**
$P = (x_1 \cdot w_1) + (x_2 \cdot w_2) + b$
$P = (2.0 \cdot 0.5) + (0.5 \cdot 0.5) + 0.0$
$P = 1.0 + 0.25 + 0.0 = 1.25$

**2. Error & Loss**
$E = P - Target = 1.25 - 10.0 = -8.75$
$Loss = E^2 = (-8.75)^2 = 76.5625$

**3. Gradients (Backward Pass)**
*   $grad\_w_1 = 2 \cdot E \cdot x_1 = 2 \cdot (-8.75) \cdot 2.0 = -35.0$
*   $grad\_w_2 = 2 \cdot E \cdot x_2 = 2 \cdot (-8.75) \cdot 0.5 = -8.75$
*   $grad\_b = 2 \cdot E \cdot 1 = 2 \cdot (-8.75) = -17.5$

**4. Weight Update (Gradient Descent)**
*   $w_1 = w_1 - (\alpha \cdot grad\_w_1) = 0.5 - (0.05 \cdot -35.0) = 0.5 + 1.75 = \mathbf{2.25}$
*   $w_2 = w_2 - (\alpha \cdot grad\_w_2) = 0.5 - (0.05 \cdot -8.75) = 0.5 + 0.4375 = \mathbf{0.9375}$
*   $b = b - (\alpha \cdot grad\_b) = 0.0 - (0.05 \cdot -17.5) = 0.0 + 0.875 = \mathbf{0.875}$
---
#### **Iteration 2**
*We take the new weights from Iteration 1 and start over.*

**1. Forward Pass**
$P = (2.0 \cdot 2.25) + (0.5 \cdot 0.9375) + 0.875$
$P = 4.5 + 0.46875 + 0.875 = 5.84375$

**2. Error & Loss**
$E = 5.84375 - 10.0 = -4.15625$
$Loss = (-4.15625)^2 = 17.2744$

**3. Gradients**
*   $grad\_w_1 = 2 \cdot (-4.15625) \cdot 2.0 = -16.625$
*   $grad\_w_2 = 2 \cdot (-4.15625) \cdot 0.5 = -4.15625$
*   $grad\_b = 2 \cdot (-4.15625) = -8.3125$

**4. Weight Update**
*   $w_1 = 2.25 - (0.05 \cdot -16.625) = 2.25 + 0.83125 = \mathbf{3.08125}$
*   $w_2 = 0.9375 - (0.05 \cdot -4.15625) = 0.9375 + 0.2078125 = \mathbf{1.1453125}$
*   $b = 0.875 - (0.05 \cdot -8.3125) = 0.875 + 0.415625 = \mathbf{1.290625}$
---
#### **Iteration 3**

**1. Forward Pass**
$P = (2.0 \cdot 3.08125) + (0.5 \cdot 1.1453125) + 1.290625$
$P = 6.1625 + 0.57265625 + 1.290625 = 8.02578125$

**2. Error & Loss**
$E = 8.02578125 - 10.0 = -1.97421875$
$Loss = (-1.97421875)^2 \approx 3.8975$

**3. Gradients**
*   $grad\_w_1 = 2 \cdot (-1.97421875) \cdot 2.0 = -7.896875$
*   $grad\_w_2 = 2 \cdot (-1.97421875) \cdot 0.5 = -1.97421875$
*   $grad\_b = 2 \cdot (-1.97421875) = -3.9484375$

**4. Weight Update**
*   $w_1 = 3.08125 - (0.05 \cdot -7.896875) = 3.08125 + 0.39484375 = \mathbf{3.47609375}$
*   $w_2 = 1.1453125 - (0.05 \cdot -1.97421875) = 1.1453125 + 0.0987109375 = \mathbf{1.2440234375}$
*   $b = 1.290625 - (0.05 \cdot -3.9484375) = 1.290625 + 0.197421875 = \mathbf{1.488046875}$
---
 **Day 4:** Self-Attention Mechanics (Matrix math of Q, K, V) 
 **Day 5:** Building a Transformer Block (Multi-Head & FF) 
 **Day 6:** Training on Shakespeare (Run loop & observe loss) 
 **Day 7:** Tokenization (Understand BPE & vocabulary) 
 **Day 8:** Local SLMs (Setting up Llama 3 locally) 
 **Day 9:** Quantization Theory (VRAM calc, 4-bit vs 8-bit) 
 **Day 10:** High-Throughput Serving (Deploy model) 
 **Day 11:** Vector Math in Numpy (Cosine Sim / Dot Product) 
 **Day 12:** Vector Databases (Install & index via Docker) 
 **Day 13:** Chunking Strategies (Fixed vs. Recursive vs. Semantic)
 **Day 14:** Metadata Filtering (HNSW indexing with payloads) 
 **Phase 2: Building & Systems** 
 **Day 15:** BM25 vs. Vector (Keyword vs. Semantic search) 
 **Day 16:** Hybrid Search & RRF (Reciprocal Rank Fusion) 
 **Day 17:** Cross-Encoders (Re-ranking top 100 results) 
 **Day 18:** Sparse Embeddings (Lexical-semantic hybridity) 
 **Day 19:** Structured Output (Pydantic validation) 
 **Day 20:** Query Transformation (Hypothetical Doc Embeddings) 
 **Day 21:** IR Evaluation (nDCG, MRR, Precision@K) 
 **Day 22:** LangGraph Foundations (Nodes, Edges, State) 
 **Day 23:** Cyclic Graphs (Plan-Execute-Review loops) 
 **Day 24:** Tool Use (Binding external APIs via functions) 
 **Day 25:** Error Handling (Retries/fallback logic in graphs) 
 **Day 26:** Agentic Persistence (Redis state check-pointing) 
 **Day 27:** Human-in-the-loop (Graph interruption for approval)
 **Day 28:** Self-Correction Loops (Agent reflection patterns) 
 **Day 29:** RAG Evaluation Frameworks 
 **Day 30:** LLM-as-a-Judge (Writing rubrics for auto-grading)
 **Day 31:** Multi-Agent Architectures (Framework comparison) 
 **Day 32:** Task Decomposition (Manager to Sub-tasks) 
 **Day 33:** Inter-Agent Communication (Messaging protocols) 
 **Day 34:** Cost Monitoring (Token usage logging per step) 
 **Day 35:** System Security (Prompt injection mitigation) 
 **Phase 3: The Production Capstone** 
 **Day 36:** Wiki Dump Pipeline (XML to structured JSON) 
 **Day 37:** OpenSearch Serverless (Hybrid index on AWS) 
 **Day 38:** Multi-Hop Retrieval (Iterative agent research loops)
 **Day 39:** Bedrock Orchestration (Connecting Claude/Titan) 
 **Day 40:** The Hybrid Gateway (Routing between local & Bedrock)
 **Day 41:** Docker & Deployment (Containerizing LangGraph) 
 **Day 42:** Final Stress Test (Load testing & tracing) 
