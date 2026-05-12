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

> **Initial State:**
> *   Inputs: $x_1 = 2.0$, $x_2 = 0.5$
> *   Target: $10.0$
> *   Learning Rate ($\alpha$): $0.05$
> *   Starting Weights: $w_1 = 0.5$, $w_2 = 0.5$, $b = 0.0$
> ---
> #### **Iteration 1**
> **1. Forward Pass (Prediction)**
> $P = (x_1 \cdot w_1) + (x_2 \cdot w_2) + b$
> $P = (2.0 \cdot 0.5) + (0.5 \cdot 0.5) + 0.0$
> $P = 1.0 + 0.25 + 0.0 = 1.25$
>
> **2. Error & Loss**
> $E = P - Target = 1.25 - 10.0 = -8.75$
> $Loss = E^2 = (-8.75)^2 = 76.5625$
>
> **3. Gradients (Backward Pass)**
> *   $\nabla_{w_1} = 2 \cdot E \cdot x_1 = 2 \cdot (-8.75) \cdot 2.0 = -35.0$
> *   $\nabla_{w_2} = 2 \cdot E \cdot x_2 = 2 \cdot (-8.75) \cdot 0.5 = -8.75$
> *   $\nabla_b = 2 \cdot E \cdot 1 = 2 \cdot (-8.75) = -17.5$
>
> **4. Weight Update (Gradient Descent)**
> *   $w_1 = w_1 - (\alpha \cdot \nabla_{w_1}) = 0.5 - (0.05 \cdot -35.0) = 0.5 + 1.75 = \mathbf{2.25}$
> *   $w_2 = w_2 - (\alpha \cdot \nabla_{w_2}) = 0.5 - (0.05 \cdot -8.75) = 0.5 + 0.4375 = \mathbf{0.9375}$
> *   $b = b - (\alpha \cdot \nabla_b) = 0.0 - (0.05 \cdot -17.5) = 0.0 + 0.875 = \mathbf{0.875}$
> ---
> #### **Iteration 2**
> *We take the new weights from Iteration 1 and start over.*
>
> **1. Forward Pass**
> $P = (2.0 \cdot 2.25) + (0.5 \cdot 0.9375) + 0.875$
> $P = 4.5 + 0.46875 + 0.875 = 5.84375$
>
> **2. Error & Loss**
> $E = 5.84375 - 10.0 = -4.15625$
> $Loss = (-4.15625)^2 = 17.2744$
>
> **3. Gradients**
> *   $\nabla_{w_1} = 2 \cdot (-4.15625) \cdot 2.0 = -16.625$
> *   $\nabla_{w_2} = 2 \cdot (-4.15625) \cdot 0.5 = -4.15625$
> *   $\nabla_b = 2 \cdot (-4.15625) = -8.3125$
>
> **4. Weight Update**
> *   $w_1 = 2.25 - (0.05 \cdot -16.625) = 2.25 + 0.83125 = \mathbf{3.08125}$
> *   $w_2 = 0.9375 - (0.05 \cdot -4.15625) = 0.9375 + 0.2078125 = \mathbf{1.1453125}$
> *   $b = 0.875 - (0.05 \cdot -8.3125) = 0.875 + 0.415625 = \mathbf{1.290625}$
> ---
> #### **Iteration 3**
>
> **1. Forward Pass**
> $P = (2.0 \cdot 3.08125) + (0.5 \cdot 1.1453125) + 1.290625$
> $P = 6.1625 + 0.57265625 + 1.290625 = 8.02578125$
>
> **2. Error & Loss**
> $E = 8.02578125 - 10.0 = -1.97421875$
> $Loss = (-1.97421875)^2 \approx 3.8975$
>
> **3. Gradients**
> *   $\nabla_{w_1} = 2 \cdot (-1.97421875) \cdot 2.0 = -7.896875$
> *   $\nabla_{w_2} = 2 \cdot (-1.97421875) \cdot 0.5 = -1.97421875$
> *   $\nabla_b = 2 \cdot (-1.97421875) = -3.9484375$
>
> **4. Weight Update**
> *   $w_1 = 3.08125 - (0.05 \cdot -7.896875) = 3.08125 + 0.39484375 = \mathbf{3.47609375}$
> *   $w_2 = 1.1453125 - (0.05 \cdot -1.97421875) = 1.1453125 + 0.0987109375 = \mathbf{1.2440234375}$
> *   $b = 1.290625 - (0.05 \cdot -3.9484375) = 1.290625 + 0.197421875 = \mathbf{1.488046875}$
---
### **MLP Architecture: 2 Inputs $\rightarrow$ [4, 4, 1]**
*   **Total Parameters:** 37
*   **Inputs:** $x_1, x_2$
---
> #### **Phase 1: Hidden Layer 1 (4 Neurons)**
> *Each neuron takes the 2 inputs, multiplies them by unique weights, adds a unique bias, and passes the result through a `tanh` activation.*
> *Parameters Used: 8 Weights ($w_1$ to $w_8$), 4 Biases ($b_1$ to $b_4$)*
>
> *   **Neuron 1.1:** $h_1 = \tanh((x_1 \cdot w_1) + (x_2 \cdot w_2) + b_1)$
> *   **Neuron 1.2:** $h_2 = \tanh((x_1 \cdot w_3) + (x_2 \cdot w_4) + b_2)$
> *   **Neuron 1.3:** $h_3 = \tanh((x_1 \cdot w_5) + (x_2 \cdot w_6) + b_3)$
> *   **Neuron 1.4:** $h_4 = \tanh((x_1 \cdot w_7) + (x_2 \cdot w_8) + b_4)$
>
> *Result:* The original inputs ($x_1, x_2$) are now discarded. The network moves forward using only $h_1, h_2, h_3,$ and $h_4$.
>
> <hr>
>
> #### **Phase 2: Hidden Layer 2 (4 Neurons)**
> *Each neuron in this layer takes all 4 outputs from Layer 1, applying 4 unique weights and 1 bias.*
> *Parameters Used: 16 Weights ($w_9$ to $w_{24}$), 4 Biases ($b_5$ to $b_8$)*
>
> *   **Neuron 2.1:** $k_1 = \tanh((h_1 \cdot w_9) + (h_2 \cdot w_{10}) + (h_3 \cdot w_{11}) + (h_4 \cdot w_{12}) + b_5)$
> *   **Neuron 2.2:** $k_2 = \tanh((h_1 \cdot w_{13}) + (h_2 \cdot w_{14}) + (h_3 \cdot w_{15}) + (h_4 \cdot w_{16}) + b_6)$
> *   **Neuron 2.3:** $k_3 = \tanh((h_1 \cdot w_{17}) + (h_2 \cdot w_{18}) + (h_3 \cdot w_{19}) + (h_4 \cdot w_{20}) + b_7)$
> *   **Neuron 2.4:** $k_4 = \tanh((h_1 \cdot w_{21}) + (h_2 \cdot w_{22}) + (h_3 \cdot w_{23}) + (h_4 \cdot w_{24}) + b_8)$
>
> *Result:* Layer 1's outputs are now discarded. The network moves forward using only $k_1, k_2, k_3,$ and $k_4$.
>
> <hr>
>
> #### **Phase 3: Output Layer (1 Neuron)**
> *The final neuron takes the 4 outputs from Layer 2, applies its final weights and bias, and generates the final prediction.*
> *Parameters Used: 4 Weights ($w_{25}$ to $w_{28}$), 1 Bias ($b_9$)*
>
> *   **Final Output:** $Prediction = \tanh((k_1 \cdot w_{25}) + (k_2 \cdot w_{26}) + (k_3 \cdot w_{27}) + (k_4 \cdot w_{28}) + b_9)$
> ---
> #### **The Backward Pass (Loss Minimization)**
> When we calculate the Loss ($Loss = (Prediction - Target)^2$) and call `.backward()`, the gradient flows in the exact reverse order:
> 1.  **Output Layer:** The gradient splits into 4 paths, calculating derivatives for $w_{25}$ to $w_{28}$ and $b_9$. It passes the remaining gradient back to $k_1, k_2, k_3, k_4$.
> 2.  **Hidden Layer 2:** Each of the 4 nodes receives its gradient, splits it 4 ways (updating $w_9$ through $w_{24}$ and $b_5$ through $b_8$), and passes the remainder back to $h_1, h_2, h_3, h_4$.
> 3.  **Hidden Layer 1:** Each node updates $w_1$ through $w_8$ and $b_1$ through $b_4$. The gradient stops here, as we do not update our input data ($x_1, x_2$).
---
 **Day 4:** Self-Attention Mechanics (Matrix math of Q, K, V)
 - Finished the course at https://www.deeplearning.ai/short-courses/how-transformer-llms-work
 - The Q, K, V is complex. Truly understanding it is taking time. Need to revisit again.

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
