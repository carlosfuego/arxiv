# Arxiv Results
## Keyword: kv cache 
 ### TokenSelect: Efficient Long-Context Inference and Length Extrapolation   for LLMs via Dynamic Token-Level KV Cache Selection
**Authors**: Wei Wu, Zhuoshi Pan, Chao Wang, Liyi Chen, Yunchu Bai, Tianfu Wang, Kun Fu, Zheng Wang, Hui Xiong

**Updated**: 2025-03-03T05:49:41Z

**Summary**: The rapid advancement of Large Language Models (LLMs) has driven growing demand for processing extended context sequences in contemporary applications. However, this progress faces two major challenges: performance degradation due to sequence lengths out-of-distribution, and excessively long inference times caused by the quadratic computational complexity of attention. These issues hinder the application of LLMs in long-context scenarios. In this paper, we propose Dynamic Token-Level KV Cache Selection (TokenSelect), a training-free method for efficient and accurate long-context inference. TokenSelect builds upon the observation of non-contiguous attention sparsity, using Query-Key dot products to measure per-head KV Cache criticality at token-level. By per-head soft voting mechanism, TokenSelect selectively involves a few critical KV cache tokens in attention calculation without sacrificing accuracy. To further accelerate TokenSelect, we design the Selection Cache based on observations of consecutive Query similarity and implemented efficient dot product kernel, significantly reducing the overhead. A comprehensive evaluation of TokenSelect demonstrates up to 23.84x speedup in attention computation and up to 2.28x acceleration in end-to-end latency, while providing superior performance compared to state-of-the-art long-context inference methods.

**Link**: [arxiv](http://arxiv.org/abs/2411.02886v2),  [pdf](http://arxiv.org/pdf/2411.02886v2)

**Tags**: cs.CL cs.AI cs.LG 



### When Attention Sink Emerges in Language Models: An Empirical View
**Authors**: Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Cunxiao Du, Ye Wang, Min Lin

**Updated**: 2025-03-02T14:37:53Z

**Summary**: Language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as attention sink. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others. Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sinks exist universally in LMs with various inputs, even in small models. Furthermore, attention sink is observed to emerge during the LM pre-training, motivating us to investigate how optimization, data distribution, loss function, and model architecture in LM pre-training influence its emergence. We highlight that attention sink emerges after effective optimization on sufficient training data. The sink position is highly correlated with the loss function and data distribution. Most importantly, we find that attention sink acts more like key biases, storing extra attention scores, which could be non-informative and not contribute to the value computation. We also observe that this phenomenon (at least partially) stems from tokens' inner dependence on attention scores as a result of softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, such as sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters. The code is available at https://github.com/sail-sg/Attention-Sink.

**Link**: [arxiv](http://arxiv.org/abs/2410.10781v2),  [pdf](http://arxiv.org/pdf/2410.10781v2)

**Tags**: cs.CL cs.AI cs.LG 



### IterGen: Iterative Semantic-aware Structured LLM Generation with   Backtracking
**Authors**: Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, Sasa Misailovic

**Updated**: 2025-03-02T01:39:57Z

**Summary**: Large Language Models (LLMs) are widely used for tasks such as natural language and code generation, but their outputs often suffer from issues like hallucination, toxicity, and incorrect results. Current libraries for structured LLM generation rely on left-to-right decoding without support for backtracking, limiting the ability to correct or refine outputs mid-generation.   To address this, we introduce IterGen, a user-friendly library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar symbols. By leveraging a symbol-to-position mapping and maintaining the key-value (KV) cache state, IterGen ensures efficient and structured generation while allowing for corrections during the process. We demonstrate IterGen's effectiveness in two important applications: reducing privacy leakage in LLM outputs and improving the accuracy of LLM-generated SQL and Vega-Lite queries.   Our code and additional resources are available at https://structuredllm.com.

**Link**: [arxiv](http://arxiv.org/abs/2410.07295v2),  [pdf](http://arxiv.org/pdf/2410.07295v2)

**Tags**: cs.SE cs.LG cs.PL 



### A Unified Framework for Automated Code Transformation and Pragma   Insertion
**Authors**: Stéphane Pouget, Louis-Noël Pouchet, Jason Cong

**Updated**: 2025-03-01T05:43:19Z

**Summary**: High-level synthesis, source-to-source compilers, and various Design Space Exploration techniques for pragma insertion have significantly improved the Quality of Results of generated designs. These tools offer benefits such as reduced development time and enhanced performance. However, achieving high-quality results often requires additional manual code transformations and tiling selections, which are typically performed separately or as pre-processing steps. Although DSE techniques enable code transformation upfront, the vastness of the search space often limits the exploration of all possible code transformations, making it challenging to determine which transformations are necessary. Additionally, ensuring correctness remains challenging, especially for complex transformations and optimizations.   To tackle this obstacle, we first propose a comprehensive framework leveraging HLS compilers. Our system streamlines code transformation, pragma insertion, and tiles size selection for on-chip data caching through a unified optimization problem, aiming to enhance parallelization, particularly beneficial for computation-bound kernels. Them employing a novel Non-Linear Programming (NLP) approach, we simultaneously ascertain transformations, pragmas, and tile sizes, focusing on regular loop-based kernels. Our evaluation demonstrates that our framework adeptly identifies the appropriate transformations, including scenarios where no transformation is necessary, and inserts pragmas to achieve a favorable Quality of Results.

**Link**: [arxiv](http://arxiv.org/abs/2405.03058v6),  [pdf](http://arxiv.org/pdf/2405.03058v6)

**Tags**: cs.SE cs.PL 



### Cache Me If You Must: Adaptive Key-Value Quantization for Large Language   Models
**Authors**: Alina Shutova, Vladimir Malinovskii, Vage Egiazarian, Denis Kuznedelev, Denis Mazur, Nikita Surkov, Ivan Ermakov, Dan Alistarh

**Updated**: 2025-02-28T18:04:52Z

**Summary**: Efficient real-world deployments of large language models (LLMs) rely on Key-Value (KV) caching for processing and generating long outputs, reducing the need for repetitive computation. For large contexts, Key-Value caches can take up tens of gigabytes of device memory, as they store vector representations for each token and layer. Recent work has shown that the cached vectors can be compressed through quantization, pruning or merging, but these techniques often compromise quality towards higher compression rates. In this work, we aim to improve Key & Value compression by exploiting two observations: 1) the inherent dependencies between keys and values across different layers, and 2) high-compression mechanisms for internal network states. We propose AQUA-KV, an adaptive quantization for Key-Value caches that relies on compact adapters to exploit existing dependencies between Keys and Values, and aims to "optimally" compress the information that cannot be predicted. AQUA-KV significantly improves compression rates, while maintaining high accuracy on state-of-the-art LLM families. On Llama 3.2 LLMs, we achieve near-lossless inference at 2-2.5 bits per value with under $1\%$ relative error in perplexity and LongBench scores. AQUA-KV is one-shot, simple, and efficient: it can be calibrated on a single GPU within 1-6 hours, even for 70B models.

**Link**: [arxiv](http://arxiv.org/abs/2501.19392v4),  [pdf](http://arxiv.org/pdf/2501.19392v4)

**Tags**: cs.LG 



### Distributed Data Access in Industrial Edge Networks
**Authors**: Theofanis P. Raptis, Andrea Passarella, Marco Conti

**Updated**: 2025-02-28T14:54:35Z

**Summary**: Wireless edge networks in smart industrial environments increasingly operate using advanced sensors and autonomous machines interacting with each other and generating huge amounts of data. Those huge amounts of data are bound to make data management (e.g., for processing, storing, computing) a big challenge. Current data management approaches, relying primarily on centralized data storage, might not be able to cope with the scalability and real time requirements of Industry 4.0 environments, while distributed solutions are increasingly being explored. In this paper, we introduce the problem of distributed data access in multi-hop wireless industrial edge deployments, whereby a set of consumer nodes needs to access data stored in a set of data cache nodes, satisfying the industrial data access delay requirements and at the same time maximizing the network lifetime. We prove that the introduced problem is computationally intractable and, after formulating the objective function, we design a two-step algorithm in order to address it. We use an open testbed with real devices for conducting an experimental investigation on the performance of the algorithm. Then, we provide two online improvements, so that the data distribution can dynamically change before the first node in the network runs out of energy. We compare the performance of the methods via simulations for different numbers of network nodes and data consumers, and we show significant lifetime prolongation and increased energy efficiency when employing the method which is using only decentralized low-power wireless communication instead of the method which is using also centralized local area wireless communication.

**Link**: [arxiv](http://arxiv.org/abs/2502.21117v1),  [pdf](http://arxiv.org/pdf/2502.21117v1)

**Tags**: cs.NI 



### Training-free and Adaptive Sparse Attention for Efficient Long Video   Generation
**Authors**: Yifei Xia, Suhan Ling, Fangcheng Fu, Yujie Wang, Huixia Li, Xuefeng Xiao, Bin Cui

**Updated**: 2025-02-28T14:11:20Z

**Summary**: Generating high-fidelity long videos with Diffusion Transformers (DiTs) is often hindered by significant latency, primarily due to the computational demands of attention mechanisms. For instance, generating an 8-second 720p video (110K tokens) with HunyuanVideo takes about 600 PFLOPs, with around 500 PFLOPs consumed by attention computations. To address this issue, we propose AdaSpa, the first Dynamic Pattern and Online Precise Search sparse attention method. Firstly, to realize the Dynamic Pattern, we introduce a blockified pattern to efficiently capture the hierarchical sparsity inherent in DiTs. This is based on our observation that sparse characteristics of DiTs exhibit hierarchical and blockified structures between and within different modalities. This blockified approach significantly reduces the complexity of attention computation while maintaining high fidelity in the generated videos. Secondly, to enable Online Precise Search, we propose the Fused LSE-Cached Search with Head-adaptive Hierarchical Block Sparse Attention. This method is motivated by our finding that DiTs' sparse pattern and LSE vary w.r.t. inputs, layers, and heads, but remain invariant across denoising steps. By leveraging this invariance across denoising steps, it adapts to the dynamic nature of DiTs and allows for precise, real-time identification of sparse indices with minimal overhead. AdaSpa is implemented as an adaptive, plug-and-play solution and can be integrated seamlessly with existing DiTs, requiring neither additional fine-tuning nor a dataset-dependent profiling. Extensive experiments validate that AdaSpa delivers substantial acceleration across various models while preserving video quality, establishing itself as a robust and scalable approach to efficient video generation.

**Link**: [arxiv](http://arxiv.org/abs/2502.21079v1),  [pdf](http://arxiv.org/pdf/2502.21079v1)

**Tags**: cs.CV 



### SelectLLM: Query-Aware Efficient Selection Algorithm for Large Language   Models
**Authors**: Kaushal Kumar Maurya, KV Aditya Srivatsa, Ekaterina Kochmar

**Updated**: 2025-02-28T13:23:56Z

**Summary**: Large language models (LLMs) have been widely adopted due to their remarkable performance across various applications, driving the accelerated development of a large number of diverse models. However, these individual LLMs show limitations in generalization and performance on complex tasks due to inherent training biases, model size constraints, and the quality or diversity of pre-training datasets. A promising direction is to efficiently harness the diverse capabilities of LLMs to overcome these individual limitations. To address these limitations, we introduce a novel LLM selection algorithm called SelectLLM, which efficiently directs input queries to the most suitable subset of LLMs from a large pool, ensuring that the selected models collectively provide accurate responses. SelectLLM employs a multi-label classifier and policy based on the classifier's predictions and confidence scores in selecting an optimal, query-aware, and lightweight subset of LLMs. Our findings indicate that the proposed model outperforms existing ensemble-based baselines and achieves competitive performance with similarly sized top-performing LLMs while maintaining efficiency. Specifically, it achieves a huge reduction in inference latency on two challenging reasoning benchmarks: 13% on GSM8K and 70% on MMLU, compared to the top-performing baseline. Also, we establish a theoretical upper bound by an Oracle with LLMs and perform an in-depth linguistic analysis to understand the performance gap between the Oracle and SelectLLM.

**Link**: [arxiv](http://arxiv.org/abs/2408.08545v3),  [pdf](http://arxiv.org/pdf/2408.08545v3)

**Tags**: cs.CL 



### Training-Free Exponential Context Extension via Cascading KV Cache
**Authors**: Jeffrey Willette, Heejun Lee, Youngwan Lee, Myeongjae Jeon, Sung Ju Hwang

**Updated**: 2025-02-28T13:08:44Z

**Summary**: The transformer's context window is vital for tasks such as few-shot learning and conditional generation as it preserves previous tokens for active memory. However, as the context lengths increase, the computational costs grow quadratically, hindering the deployment of large language models (LLMs) in real-world, long sequence scenarios. Although some recent key-value caching (KV Cache) methods offer linear inference complexity, they naively manage the stored context, prematurely evicting tokens and losing valuable information. Moreover, they lack an optimized prefill/prompt stage strategy, resulting in higher latency than even quadratic attention for realistic context sizes. In response, we introduce a novel mechanism that leverages cascading sub-cache buffers to selectively retain the most relevant tokens, enabling the model to maintain longer context histories without increasing the cache size. Our approach outperforms linear caching baselines across key benchmarks, including streaming perplexity, question answering, book summarization, and passkey retrieval, where it retains better retrieval accuracy at 1M tokens after four doublings of the cache size of 65K. Additionally, our method reduces prefill stage latency by a factor of 6.8 when compared to flash attention on 1M tokens. These innovations not only enhance the computational efficiency of LLMs but also pave the way for their effective deployment in resource-constrained environments, enabling large-scale, real-time applications with significantly reduced latency.

**Link**: [arxiv](http://arxiv.org/abs/2406.17808v3),  [pdf](http://arxiv.org/pdf/2406.17808v3)

**Tags**: cs.CL cs.AI cs.LG 



### Towards Reliable Vector Database Management Systems: A Software Testing   Roadmap for 2030
**Authors**: Shenao Wang, Yanjie Zhao, Yinglin Xie, Zhao Liu, Xinyi Hou, Quanchen Zou, Haoyu Wang

**Updated**: 2025-02-28T07:56:37Z

**Summary**: The rapid growth of Large Language Models (LLMs) and AI-driven applications has propelled Vector Database Management Systems (VDBMSs) into the spotlight as a critical infrastructure component. VDBMS specializes in storing, indexing, and querying dense vector embeddings, enabling advanced LLM capabilities such as retrieval-augmented generation, long-term memory, and caching mechanisms. However, the explosive adoption of VDBMS has outpaced the development of rigorous software testing methodologies tailored for these emerging systems. Unlike traditional databases optimized for structured data, VDBMS face unique testing challenges stemming from the high-dimensional nature of vector data, the fuzzy semantics in vector search, and the need to support dynamic data scaling and hybrid query processing. In this paper, we begin by conducting an empirical study of VDBMS defects and identify key challenges in test input generation, oracle definition, and test evaluation. Drawing from these insights, we propose the first comprehensive research roadmap for developing effective testing methodologies tailored to VDBMS. By addressing these challenges, the software testing community can contribute to the development of more reliable and trustworthy VDBMS, enabling the full potential of LLMs and data-intensive AI applications.

**Link**: [arxiv](http://arxiv.org/abs/2502.20812v1),  [pdf](http://arxiv.org/pdf/2502.20812v1)

**Tags**: cs.SE 



### Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision   Language Model Inference
**Authors**: Mingyuan Wu, Jize Jiang, Haozhen Zheng, Meitang Li, Zhaoheng Li, Beitong Tian, Bo Chen, Yongjoo Park, Minjia Zhang, Chengxiang Zhai, Klara Nahrstedt

**Updated**: 2025-02-27T23:09:20Z

**Summary**: Vision Language Models (VLMs) have achieved remarkable success in a wide range of vision applications of increasing complexity and scales, yet choosing the right VLM model size involves a trade-off between response quality and cost. While smaller VLMs are cheaper to run, they typically produce responses only marginally better than random guessing on benchmarks such as MMMU.   In this paper, we propose Cache of Thought (CoT), a master apprentice framework for collaborative inference between large and small VLMs. CoT manages high quality query results from large VLMs (master) in a cache, which are then selected via a novel multi modal retrieval and in-context learning to aid the performance of small VLMs (apprentice). We extensively evaluate CoT on various widely recognized and challenging general VQA benchmarks, and show that CoT increases overall VQA performance by up to 7.7% under the same budget, and specifically boosts the performance of apprentice VLMs by up to 36.6%.

**Link**: [arxiv](http://arxiv.org/abs/2502.20587v1),  [pdf](http://arxiv.org/pdf/2502.20587v1)

**Tags**: cs.LG 



### WWW: What, When, Where to Compute-in-Memory
**Authors**: Tanvi Sharma, Mustafa Ali, Indranil Chakraborty, Kaushik Roy

**Updated**: 2025-02-27T21:50:48Z

**Summary**: Matrix multiplication is the dominant computation during Machine Learning (ML) inference. To efficiently perform such multiplication operations, Compute-in-memory (CiM) paradigms have emerged as a highly energy efficient solution. However, integrating compute in memory poses key questions, such as 1) What type of CiM to use: Given a multitude of CiM design characteristics, determining their suitability from architecture perspective is needed. 2) When to use CiM: ML inference includes workloads with a variety of memory and compute requirements, making it difficult to identify when CiM is more beneficial than standard processing cores. 3) Where to integrate CiM: Each memory level has different bandwidth and capacity, creating different data reuse opportunities for CiM integration.   To answer such questions regarding on-chip CiM integration for accelerating ML workloads, we use an analytical architecture-evaluation methodology with tailored mapping algorithm. The mapping algorithm aims to achieve highest weight reuse and reduced data movements for a given CiM prototype and workload. Our analysis considers the integration of CiM prototypes into the cache levels of a tensor-core-like architecture, and shows that CiM integrated memory improves energy efficiency by up to 3.4x and throughput by up to 15.6x compared to established baseline with INT-8 precision. We believe the proposed work provides insights into what type of CiM to use, and when and where to optimally integrate it in the cache hierarchy for efficient matrix multiplication.

**Link**: [arxiv](http://arxiv.org/abs/2312.15896v3),  [pdf](http://arxiv.org/pdf/2312.15896v3)

**Tags**: cs.AR cs.DC cs.LG 



### An Attempt to Catch Up with JIT Compilers: The False Lead of Optimizing   Inline Caches
**Authors**: Aurore Poirier, Erven Rohou, Manuel Serrano

**Updated**: 2025-02-27T21:42:49Z

**Summary**: Context: Just-in-Time (JIT) compilers are able to specialize the code they generate according to a continuous profiling of the running programs. This gives them an advantage when compared to Ahead-of-Time (AoT) compilers that must choose the code to generate once for all.   Inquiry: Is it possible to improve the performance of AoT compilers by adding Dynamic Binary Modification (DBM) to the executions?   Approach: We added to the Hopc AoT JavaScript compiler a new optimization based on DBM to the inline cache (IC), a classical optimization dynamic languages use to implement object property accesses efficiently.   Knowledge: Reducing the number of memory accesses as the new optimization does, does not shorten execution times on contemporary architectures.   Grounding: The DBM optimization we have implemented is fully operational on x86_64 architectures. We have conducted several experiments to evaluate its impact on performance and to study the reasons of the lack of acceleration.   Importance: The (negative) result we present in this paper sheds new light on the best strategy to be used to implement dynamic languages. It tells that the old days were removing instructions or removing memory reads always yielded to speed up is over. Nowadays, implementing sophisticated compiler optimizations is only worth the effort if the processor is not able by itself to accelerate the code. This result applies to AoT compilers as well as JIT compilers.

**Link**: [arxiv](http://arxiv.org/abs/2502.20547v1),  [pdf](http://arxiv.org/pdf/2502.20547v1)

**Tags**: cs.PL 



### Long-Context Inference with Retrieval-Augmented Speculative Decoding
**Authors**: Guanzheng Chen, Qilong Feng, Jinjie Ni, Xin Li, Michael Qizhe Shieh

**Updated**: 2025-02-27T17:59:36Z

**Summary**: The emergence of long-context large language models (LLMs) offers a promising alternative to traditional retrieval-augmented generation (RAG) for processing extensive documents. However, the computational overhead of long-context inference, particularly in managing key-value (KV) caches, presents significant efficiency challenges. While Speculative Decoding (SD) traditionally accelerates inference using smaller draft models, its effectiveness diminishes substantially in long-context scenarios due to memory-bound KV cache operations. We present Retrieval-Augmented Speculative Decoding (RAPID), which leverages RAG for both accelerating and enhancing generation quality in long-context inference. RAPID introduces the RAG drafter-a draft LLM operating on shortened retrieval contexts-to speculate on the generation of long-context target LLMs. Our approach enables a new paradigm where same-scale or even larger LLMs can serve as RAG drafters while maintaining computational efficiency. To fully leverage the potentially superior capabilities from stronger RAG drafters, we develop an inference-time knowledge transfer dynamic that enriches the target distribution by RAG. Extensive experiments on the LLaMA-3.1 and Qwen2.5 backbones demonstrate that RAPID effectively integrates the strengths of both approaches, achieving significant performance improvements (e.g., from 39.33 to 42.83 on InfiniteBench for LLaMA-3.1-8B) with more than 2x speedups. Our analyses reveal that RAPID achieves robust acceleration beyond 32K context length and demonstrates superior generation quality in real-world applications.

**Link**: [arxiv](http://arxiv.org/abs/2502.20330v1),  [pdf](http://arxiv.org/pdf/2502.20330v1)

**Tags**: cs.CL 



### EMS: Adaptive Evict-then-Merge Strategy for Head-wise KV Cache   Compression Based on Global-Local Importance
**Authors**: Yingxin Li, Ye Li, Yuan Meng, Xinzhu Ma, Zihan Geng, Shutao Xia, Zhi Wang

**Updated**: 2025-02-27T15:29:03Z

**Summary**: As large language models (LLMs) continue to advance, the demand for higher quality and faster processing of long contexts across various applications is growing. KV cache is widely adopted as it stores previously generated key and value tokens, effectively reducing redundant computations during inference. However, as memory overhead becomes a significant concern, efficient compression of KV cache has gained increasing attention. Most existing methods perform compression from two perspectives: identifying important tokens and designing compression strategies. However, these approaches often produce biased distributions of important tokens due to the influence of accumulated attention scores or positional encoding. Furthermore, they overlook the sparsity and redundancy across different heads, which leads to difficulties in preserving the most effective information at the head level. To this end, we propose EMS to overcome these limitations, while achieving better KV cache compression under extreme compression ratios. Specifically, we introduce a Global-Local score that combines accumulated attention scores from both global and local KV tokens to better identify the token importance. For the compression strategy, we design an adaptive and unified Evict-then-Merge framework that accounts for the sparsity and redundancy of KV tokens across different heads. Additionally, we implement the head-wise parallel compression through a zero-class mechanism to enhance efficiency. Extensive experiments demonstrate our SOTA performance even under extreme compression ratios. EMS consistently achieves the lowest perplexity, improves scores by over 1.28 points across four LLMs on LongBench under a 256 cache budget, and preserves 95% retrieval accuracy with a cache budget less than 2% of the context length in the Needle-in-a-Haystack task.

**Link**: [arxiv](http://arxiv.org/abs/2412.08521v2),  [pdf](http://arxiv.org/pdf/2412.08521v2)

**Tags**: cs.CL 



### ThinK: Thinner Key Cache by Query-Driven Pruning
**Authors**: Yuhui Xu, Zhanming Jie, Hanze Dong, Lei Wang, Xudong Lu, Aojun Zhou, Amrita Saha, Caiming Xiong, Doyen Sahoo

**Updated**: 2025-02-27T12:30:43Z

**Summary**: Large Language Models (LLMs) have revolutionized the field of natural language processing, achieving unprecedented performance across a variety of applications. However, their increased computational and memory demands present significant challenges, especially when handling long sequences. This paper focuses on the long-context scenario, addressing the inefficiencies in KV cache memory consumption during inference. Unlike existing approaches that optimize the memory based on the sequence length, we identify substantial redundancy in the channel dimension of the KV cache, as indicated by an uneven magnitude distribution and a low-rank structure in the attention weights. In response, we propose ThinK, a novel query-dependent KV cache pruning method designed to minimize attention weight loss while selectively pruning the least significant channels. Our approach not only maintains or enhances model accuracy but also achieves a reduction in KV cache memory costs by over 20% compared with vanilla KV cache eviction and quantization methods. For instance, ThinK integrated with KIVI can achieve a 2.8x reduction in peak memory usage while maintaining nearly the same quality, enabling up to a 5x increase in batch size when using a single GPU. Extensive evaluations on the LLaMA and Mistral models across various long-sequence datasets verified the efficiency of ThinK, establishing a new baseline algorithm for efficient LLM deployment without compromising performance. Our code has been made available at https://github.com/SalesforceAIResearch/ThinK.

**Link**: [arxiv](http://arxiv.org/abs/2407.21018v3),  [pdf](http://arxiv.org/pdf/2407.21018v3)

**Tags**: cs.CL cs.AI 



### Persistent Sampling: Enhancing the Efficiency of Sequential Monte Carlo
**Authors**: Minas Karamanis, Uroš Seljak

**Updated**: 2025-02-27T12:15:38Z

**Summary**: Sequential Monte Carlo (SMC) samplers are powerful tools for Bayesian inference but suffer from high computational costs due to their reliance on large particle ensembles for accurate estimates. We introduce persistent sampling (PS), an extension of SMC that systematically retains and reuses particles from all prior iterations to construct a growing, weighted ensemble. By leveraging multiple importance sampling and resampling from a mixture of historical distributions, PS mitigates the need for excessively large particle counts, directly addressing key limitations of SMC such as particle impoverishment and mode collapse. Crucially, PS achieves this without additional likelihood evaluations-weights for persistent particles are computed using cached likelihood values. This framework not only yields more accurate posterior approximations but also produces marginal likelihood estimates with significantly lower variance, enhancing reliability in model comparison. Furthermore, the persistent ensemble enables efficient adaptation of transition kernels by leveraging a larger, decorrelated particle pool. Experiments on high-dimensional Gaussian mixtures, hierarchical models, and non-convex targets demonstrate that PS consistently outperforms standard SMC and related variants, including recycled and waste-free SMC, achieving substantial reductions in mean squared error for posterior expectations and evidence estimates, all at reduced computational cost. PS thus establishes itself as a robust, scalable, and efficient alternative for complex Bayesian inference tasks.

**Link**: [arxiv](http://arxiv.org/abs/2407.20722v2),  [pdf](http://arxiv.org/pdf/2407.20722v2)

**Tags**: stat.ML cs.LG stat.CO 



### Dynamic Parallel Tree Search for Efficient LLM Reasoning
**Authors**: Yifu Ding, Wentao Jiang, Shunyu Liu, Yongcheng Jing, Jinyang Guo, Yingjie Wang, Jing Zhang, Zengmao Wang, Ziwei Liu, Bo Du, Xianglong Liu, Dacheng Tao

**Updated**: 2025-02-27T06:39:06Z

**Summary**: Tree of Thoughts (ToT) enhances Large Language Model (LLM) reasoning by structuring problem-solving as a spanning tree. However, recent methods focus on search accuracy while overlooking computational efficiency. The challenges of accelerating the ToT lie in the frequent switching of reasoning focus, and the redundant exploration of suboptimal solutions. To alleviate this dilemma, we propose Dynamic Parallel Tree Search (DPTS), a novel parallelism framework that aims to dynamically optimize the reasoning path in inference. It includes the Parallelism Streamline in the generation phase to build up a flexible and adaptive parallelism with arbitrary paths by fine-grained cache management and alignment. Meanwhile, the Search and Transition Mechanism filters potential candidates to dynamically maintain the reasoning focus on more possible solutions and have less redundancy. Experiments on Qwen-2.5 and Llama-3 with Math500 and GSM8K datasets show that DPTS significantly improves efficiency by 2-4x on average while maintaining or even surpassing existing reasoning algorithms in accuracy, making ToT-based reasoning more scalable and computationally efficient.

**Link**: [arxiv](http://arxiv.org/abs/2502.16235v2),  [pdf](http://arxiv.org/pdf/2502.16235v2)

**Tags**: cs.AI 



### Breaking the Low-Rank Dilemma of Linear Attention
**Authors**: Qihang Fan, Huaibo Huang, Ran He

**Updated**: 2025-02-27T03:22:41Z

**Summary**: The Softmax attention mechanism in Transformer models is notoriously computationally expensive, particularly due to its quadratic complexity, posing significant challenges in vision applications. In contrast, linear attention provides a far more efficient solution by reducing the complexity to linear levels. However, compared to Softmax attention, linear attention often experiences significant performance degradation. Our experiments indicate that this performance drop is due to the low-rank nature of linear attention's feature map, which hinders its ability to adequately model complex spatial information. In this paper, to break the low-rank dilemma of linear attention, we conduct rank analysis from two perspectives: the KV buffer and the output features. Consequently, we introduce Rank-Augmented Linear Attention (RALA), which rivals the performance of Softmax attention while maintaining linear complexity and high efficiency. Based on RALA, we construct the Rank-Augmented Vision Linear Transformer (RAVLT). Extensive experiments demonstrate that RAVLT achieves excellent performance across various vision tasks. Specifically, without using any additional labels, data, or supervision during training, RAVLT achieves an 84.4% Top-1 accuracy on ImageNet-1k with only 26M parameters and 4.6G FLOPs. This result significantly surpasses previous linear attention mechanisms, fully illustrating the potential of RALA. Code will be available at https://github.com/qhfan/RALA.

**Link**: [arxiv](http://arxiv.org/abs/2411.07635v4),  [pdf](http://arxiv.org/pdf/2411.07635v4)

**Tags**: cs.CV 



### Learning Harmonized Representations for Speculative Sampling
**Authors**: Lefan Zhang, Xiaodan Wang, Yanhua Huang, Ruiwen Xu

**Updated**: 2025-02-26T11:47:58Z

**Summary**: Speculative sampling is a promising approach to accelerate the decoding stage for Large Language Models (LLMs). Recent advancements that leverage target LLM's contextual information, such as hidden states and KV cache, have shown significant practical improvements. However, these approaches suffer from inconsistent context between training and decoding. We also observe another discrepancy between the training and decoding objectives in existing speculative sampling methods. In this work, we propose a solution named HArmonized Speculative Sampling (HASS) that learns harmonized representations to address these issues. HASS accelerates the decoding stage without adding inference overhead through harmonized objective distillation and harmonized context alignment. Experiments on four LLaMA models demonstrate that HASS achieves 2.81x-4.05x wall-clock time speedup ratio averaging across three datasets, surpassing EAGLE-2 by 8%-20%. The code is available at https://github.com/HArmonizedSS/HASS.

**Link**: [arxiv](http://arxiv.org/abs/2408.15766v3),  [pdf](http://arxiv.org/pdf/2408.15766v3)

**Tags**: cs.LG cs.CL 



### Faster Diffusion via Temporal Attention Decomposition
**Authors**: Haozhe Liu, Wentian Zhang, Jinheng Xie, Francesco Faccio, Mengmeng Xu, Tao Xiang, Mike Zheng Shou, Juan-Manuel Perez-Rua, Jürgen Schmidhuber

**Updated**: 2025-02-26T10:49:33Z

**Summary**: We explore the role of attention mechanism during inference in text-conditional diffusion models. Empirical observations suggest that cross-attention outputs converge to a fixed point after several inference steps. The convergence time naturally divides the entire inference process into two phases: an initial phase for planning text-oriented visual semantics, which are then translated into images in a subsequent fidelity-improving phase. Cross-attention is essential in the initial phase but almost irrelevant thereafter. However, self-attention initially plays a minor role but becomes crucial in the second phase. These findings yield a simple and training-free method known as temporally gating the attention (TGATE), which efficiently generates images by caching and reusing attention outputs at scheduled time steps. Experimental results show when widely applied to various existing text-conditional diffusion models, TGATE accelerates these models by 10%-50%. The code of TGATE is available at https://github.com/HaozheLiu-ST/T-GATE.

**Link**: [arxiv](http://arxiv.org/abs/2404.02747v3),  [pdf](http://arxiv.org/pdf/2404.02747v3)

**Tags**: cs.CV 



### From Hours to Minutes: Lossless Acceleration of Ultra Long Sequence   Generation up to 100K Tokens
**Authors**: Tong Wu, Junzhe Shen, Zixia Jia, Yuxuan Wang, Zilong Zheng

**Updated**: 2025-02-26T07:10:08Z

**Summary**: Generating ultra-long sequences with large language models (LLMs) has become increasingly crucial but remains a highly time-intensive task, particularly for sequences up to 100K tokens. While traditional speculative decoding methods exist, simply extending their generation limits fails to accelerate the process and can be detrimental. Through an in-depth analysis, we identify three major challenges hindering efficient generation: frequent model reloading, dynamic key-value (KV) management and repetitive generation. To address these issues, we introduce TOKENSWIFT, a novel framework designed to substantially accelerate the generation process of ultra-long sequences while maintaining the target model's inherent quality. Experimental results demonstrate that TOKENSWIFT achieves over 3 times speedup across models of varying scales (1.5B, 7B, 8B, 14B) and architectures (MHA, GQA). This acceleration translates to hours of time savings for ultra-long sequence generation, establishing TOKENSWIFT as a scalable and effective solution at unprecedented lengths. Code can be found at https://github.com/bigai-nlco/TokenSwift.

**Link**: [arxiv](http://arxiv.org/abs/2502.18890v1),  [pdf](http://arxiv.org/pdf/2502.18890v1)

**Tags**: cs.CL 



### AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference
**Authors**: Qingyue Yang, Jie Wang, Xing Li, Zhihai Wang, Chen Chen, Lei Chen, Xianzhi Yu, Wulong Liu, Jianye Hao, Mingxuan Yuan, Bin Li

**Updated**: 2025-02-26T02:48:22Z

**Summary**: With the development of large language models (LLMs), efficient inference through Key-Value (KV) cache compression has attracted considerable attention, especially for long-context generation. To compress the KV cache, recent methods identify critical KV tokens through heuristic ranking with attention scores. However, these methods often struggle to accurately determine critical tokens as they neglect the \textit{temporal patterns} in attention scores, resulting in a noticeable degradation in LLM performance. To address this challenge, we propose AttentionPredictor, which is the first learning-based critical token identification approach. Specifically, AttentionPredictor learns a lightweight convolution model to capture spatiotemporal patterns and predict the next-token attention score. An appealing feature of AttentionPredictor is that it accurately predicts the attention score while consuming negligible memory. Moreover, we propose a cross-token critical cache prefetching framework that hides the token estimation time overhead to accelerate the decoding stage. By retaining most of the attention information, AttentionPredictor achieves 16$\times$ KV cache compression with comparable LLM performance, significantly outperforming the state-of-the-art.

**Link**: [arxiv](http://arxiv.org/abs/2502.04077v2),  [pdf](http://arxiv.org/pdf/2502.04077v2)

**Tags**: cs.CL cs.LG 



### M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically   Adaptive Numerical Type
**Authors**: Weiming Hu, Haoyan Zhang, Cong Guo, Yu Feng, Renyang Guan, Zhendong Hua, Zihan Liu, Yue Guan, Minyi Guo, Jingwen Leng

**Updated**: 2025-02-26T02:16:46Z

**Summary**: Large language models (LLMs) are one of the most important killer computer applications. The recent algorithmic advancement proposes a fine-grained group-wise quantization for LLMs, which treats a small set (e.g., 64) of values in a tensor as a compression unit. It effectively preserves the model accuracy without retraining, and has become the standard approach to efficiently deploy LLMs. On the other hand, there are works that propose various adaptive data types to better adapt to different distributions and further reduce the required bit length for LLMs. In this work, our detailed analysis unveils a key finding that while different tensors exhibit similar distributions, small groups can have markedly different distributions. As such, the group-level diversity requires a new level of adaptivity for which existing adaptive data types fail to provide.   In this paper, we propose MANT, a mathematically adaptive numeric type, featuring a more flexible encoding paradigm with a wider range of data distribution and more efficient decodingcomputation fusion mechanism to address these challenges. Based on MANT, we develop a supporting framework to assign the appropriate data type for each group adaptively. Meanwhile, the dynamically generated Key-Value (KV) caches in LLMs introduce further complexity for real-time quantization. To tackle this, we propose an efficient real-time quantization mechanism. Besides, we implement a specific processing element (PE) to efficiently support MANT and incorporate a real-time quantization unit. By integrating these components into a systolic array, MANT unifies the group-wise weight and KV cache quantization and addresses the associated challenges. Our evaluation shows achieving, on average, 2.99x (up to 4.46x) speedup and 2.81x (up to 4.10x) energy reduction to the state-of-the-art LLM accelerator.

**Link**: [arxiv](http://arxiv.org/abs/2502.18755v1),  [pdf](http://arxiv.org/pdf/2502.18755v1)

**Tags**: cs.AR 



### AgileWatts: An Energy-Efficient CPU Core Idle-State Architecture for   Latency-Sensitive Server Applications
**Authors**: Jawad Haj Yahya, Haris Volos, Davide B. Bartolini, Georgia Antoniou, Jeremie S. Kim, Zhe Wang, Kleovoulos Kalaitzidis, Tom Rollet, Zhirui Chen, Ye Geng, Onur Mutlu, Yiannakis Sazeides

**Updated**: 2025-02-25T13:03:44Z

**Summary**: User-facing applications running in modern datacenters exhibit irregular request patterns and are implemented using a multitude of services with tight latency requirements. These characteristics render ineffective existing energy conserving techniques when processors are idle due to the long transition time from a deep idle power state (C-state). While prior works propose management techniques to mitigate this inefficiency, we tackle it at its root with AgileWatts (AW): a new deep C-state architecture optimized for datacenter server processors targeting latency-sensitive applications. AW is based on three key ideas. First, AW eliminates the latency overhead of saving/restoring the core context (i.e., micro-architectural state) when powering-off/-on the core in a deep idle power state by i) implementing medium-grained power-gates, carefully distributed across the CPU core, and ii) retaining context in the power-ungated domain. Second, AW eliminates the flush latency overhead (several tens of microseconds) of the L1/L2 caches when entering a deep idle power state by keeping L1/L2 cache content power-ungated. A minimal control logic also remains power-ungated to serve cache coherence traffic (i.e., snoops) seamlessly. AW implements sleep-mode in caches to reduce caches leakage power consumption and lowers a core voltage to the minimum operational voltage level to minimize the leakage power of the power-ungated domain. Third, using a state-of-the-art power efficient all-digital phase-locked loop (ADPLL) clock generator, AW keeps the PLL active and locked during the idle state, further cutting precious microseconds of wake-up latency at a negligible power cost. Our evaluation with an accurate simulator calibrated against an Intel Skylake server shows that AW reduces the energy consumption of Memcached by up to 71% (35% on average) with up to 1% performance degradation.

**Link**: [arxiv](http://arxiv.org/abs/2203.02550v3),  [pdf](http://arxiv.org/pdf/2203.02550v3)

**Tags**: cs.AR 



### Accelerating Graph Indexing for ANNS on Modern CPUs
**Authors**: Mengzhao Wang, Haotian Wu, Xiangyu Ke, Yunjun Gao, Yifan Zhu, Wenchao Zhou

**Updated**: 2025-02-25T11:36:43Z

**Summary**: In high-dimensional vector spaces, Approximate Nearest Neighbor Search (ANNS) is a key component in database and artificial intelligence infrastructures. Graph-based methods, particularly HNSW, have emerged as leading solutions among various ANNS approaches, offering an impressive trade-off between search efficiency and accuracy. Many modern vector databases utilize graph indexes as their core algorithms, benefiting from various optimizations to enhance search performance. However, the high indexing time associated with graph algorithms poses a significant challenge, especially given the increasing volume of data, query processing complexity, and dynamic index maintenance demand. This has rendered indexing time a critical performance metric for users. In this paper, we comprehensively analyze the underlying causes of the low graph indexing efficiency on modern CPUs, identifying that distance computation dominates indexing time, primarily due to high memory access latency and suboptimal arithmetic operation efficiency. We demonstrate that distance comparisons during index construction can be effectively performed using compact vector codes at an appropriate compression error. Drawing from insights gained through integrating existing compact coding methods in the graph indexing process, we propose a novel compact coding strategy, named Flash, designed explicitly for graph indexing and optimized for modern CPU architectures. By minimizing random memory accesses and maximizing the utilization of SIMD (Single Instruction, Multiple Data) instructions, Flash significantly enhances cache hit rates and arithmetic operations. Extensive experiments conducted on eight real-world datasets, ranging from ten million to one billion vectors, exhibit that Flash achieves a speedup of 10.4$\times$ to 22.9$\times$ in index construction efficiency, while maintaining or improving search performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.18113v1),  [pdf](http://arxiv.org/pdf/2502.18113v1)

**Tags**: cs.DB 



### KV-Edit: Training-Free Image Editing for Precise Background Preservation
**Authors**: Tianrui Zhu, Shiyi Zhang, Jiawei Shao, Yansong Tang

**Updated**: 2025-02-25T09:42:11Z

**Summary**: Background consistency remains a significant challenge in image editing tasks. Despite extensive developments, existing works still face a trade-off between maintaining similarity to the original image and generating content that aligns with the target. Here, we propose KV-Edit, a training-free approach that uses KV cache in DiTs to maintain background consistency, where background tokens are preserved rather than regenerated, eliminating the need for complex mechanisms or expensive training, ultimately generating new content that seamlessly integrates with the background within user-provided regions. We further explore the memory consumption of the KV cache during editing and optimize the space complexity to $O(1)$ using an inversion-free method. Our approach is compatible with any DiT-based generative model without additional training. Experiments demonstrate that KV-Edit significantly outperforms existing approaches in terms of both background and image quality, even surpassing training-based methods. Project webpage is available at https://xilluill.github.io/projectpages/KV-Edit

**Link**: [arxiv](http://arxiv.org/abs/2502.17363v2),  [pdf](http://arxiv.org/pdf/2502.17363v2)

**Tags**: cs.CV 



### KVTuner: Sensitivity-Aware Layer-wise Mixed Precision KV Cache   Quantization for Efficient and Nearly Lossless LLM Inference
**Authors**: Xing Li, Zeyu Xing, Yiming Li, Linping Qu, Hui-Ling Zhen, Wulong Liu, Yiwu Yao, Sinno Jialin Pan, Mingxuan Yuan

**Updated**: 2025-02-25T03:42:15Z

**Summary**: KV cache quantization can improve Large Language Models (LLMs) inference throughput and latency in long contexts and large batch-size scenarios while preserving LLMs effectiveness. However, current methods have three unsolved issues: overlooking layer-wise sensitivity to KV cache quantization, high overhead of online fine-grained decision-making, and low flexibility to different LLMs and constraints. Therefore, we thoroughly analyze the inherent correlation of layer-wise transformer attention patterns to KV cache quantization errors and study why key cache is more important than value cache for quantization error reduction. We further propose a simple yet effective framework KVTuner to adaptively search for the optimal hardware-friendly layer-wise KV quantization precision pairs for coarse-grained KV cache with multi-objective optimization and directly utilize the offline searched configurations during online inference. To reduce the computational cost of offline calibration, we utilize the intra-layer KV precision pair pruning and inter-layer clustering to reduce the search space. Experimental results show that we can achieve nearly lossless 3.25-bit mixed precision KV cache quantization for LLMs like Llama-3.1-8B-Instruct and 4.0-bit for sensitive models like Qwen2.5-7B-Instruct on mathematical reasoning tasks. The maximum inference throughput can be improved by 38.3% compared with KV8 quantization over various context lengths. Our code and searched configurations are available at https://github.com/cmd2001/KVTuner.

**Link**: [arxiv](http://arxiv.org/abs/2502.04420v3),  [pdf](http://arxiv.org/pdf/2502.04420v3)

**Tags**: cs.LG cs.AI cs.CL 



### ELMo-Tune-V2: LLM-Assisted Full-Cycle Auto-Tuning to Optimize LSM-Based   Key-Value Stores
**Authors**: Viraj Thakkar, Qi Lin, Kenanya Keandra Adriel Prasetyo, Raden Haryosatyo Wisjnunandono, Achmad Imam Kistijantoro, Reza Fuad Rachmadi, Zhichao Cao

**Updated**: 2025-02-24T19:48:48Z

**Summary**: Log-Structured Merge-tree-based Key-Value Store (LSM-KVS) is a foundational storage engine serving diverse modern workloads, systems, and applications. To suit varying use cases, LSM-KVS allows a vast configuration space that controls core parameters like compaction, flush, and cache sizes, each consuming a shared pool of CPU, Memory, and Storage resources. Navigating the LSM-KVS configuration space necessitates knowledge of the impact of each configuration on the expected workload and underlying hardware. Beyond expensive and time-intensive human-expert-based tuning, existing LSM-KVS tuning solutions focus on tuning with specific workload expectations while limited to a narrow subset of parameters.   This paper introduces ELMo-Tune-V2, a framework that integrates Large Language Models (LLMs) at its foundation to demonstrate the potential of applying modern LLMs in data system optimization problems. ELMo-Tune-V2 leverages the contextual reasoning, cross-domain, and generative capabilities of LLMs to perform 1) self-navigated characterization and modeling of LSM-KVS workloads, 2) automatic tuning across a broad parameter space using cross-domain knowledge, and 3) real-time dynamic configuration adjustments for LSM-KVS. ELMo-Tune-V2 integrates three innovations: LLM-based workload synthesis for adaptive benchmark generation, feedback-driven iterative fine-tuning for configuration refinement, and real-time tuning to handle evolving workloads. Through detailed evaluation using RocksDB under several real-world applications across diverse scenarios, ELMo-Tune-V2 achieves performance improvements up to ~14X our YCSB benchmarks compared against default RocksDB configurations, and our end-to-end tests with upper-level applications, NebulaGraph and Kvrocks, demonstrate performance gains of 34% and 26%, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2502.17606v1),  [pdf](http://arxiv.org/pdf/2502.17606v1)

**Tags**: cs.DB 



### MEDA: Dynamic KV Cache Allocation for Efficient Multimodal Long-Context   Inference
**Authors**: Zhongwei Wan, Hui Shen, Xin Wang, Che Liu, Zheda Mai, Mi Zhang

**Updated**: 2025-02-24T19:34:52Z

**Summary**: Long-context Multimodal Large Language Models (MLLMs) that incorporate long text-image and text-video modalities, demand substantial resources as their multimodal Key-Value (KV) caches grow with increasing input lengths, challenging inference efficiency. Existing methods for KV cache compression, in both text-only and multimodal LLMs, have neglected attention density variations across layers, thus often adopting uniform or progressive reduction strategies for layer-wise cache allocation. In this work, we propose MEDA, a dynamic layer-wise KV cache allocation method for efficient multimodal long-context inference. As its core, MEDA utilizes cross-modal attention entropy to determine the KV cache size at each MLLMs layer. Given the dynamically allocated KV cache size at each layer, MEDA also employs a KV pair selection scheme to identify which KV pairs to select and a KV pair merging strategy that merges the selected and non-selected ones to preserve information from the entire context. MEDA achieves up to 72% KV cache memory reduction and 2.82 times faster decoding speed, while maintaining or enhancing performance on various multimodal tasks in long-context settings, including multi-images and long-video scenarios. Our code is released at https://github.com/AIoT-MLSys-Lab/MEDA.

**Link**: [arxiv](http://arxiv.org/abs/2502.17599v1),  [pdf](http://arxiv.org/pdf/2502.17599v1)

**Tags**: cs.CL 



### LongSpec: Long-Context Speculative Decoding with Efficient Drafting and   Verification
**Authors**: Penghui Yang, Cunxiao Du, Fengzhuo Zhang, Haonan Wang, Tianyu Pang, Chao Du, Bo An

**Updated**: 2025-02-24T18:53:31Z

**Summary**: Speculative decoding has become a promising technique to mitigate the high inference latency of autoregressive decoding in Large Language Models (LLMs). Despite its promise, the effective application of speculative decoding in LLMs still confronts three key challenges: the increasing memory demands of the draft model, the distribution shift between the short-training corpora and long-context inference, and inefficiencies in attention implementation. In this work, we enhance the performance of speculative decoding in long-context settings by addressing these challenges. First, we propose a memory-efficient draft model with a constant-sized Key-Value (KV) cache. Second, we introduce novel position indices for short-training data, enabling seamless adaptation from short-context training to long-context inference. Finally, we present an innovative attention aggregation method that combines fast implementations for prefix computation with standard attention for tree mask handling, effectively resolving the latency and memory inefficiencies of tree decoding. Our approach achieves strong results on various long-context tasks, including repository-level code completion, long-context summarization, and o1-like long reasoning tasks, demonstrating significant improvements in latency reduction. The code is available at https://github.com/sail-sg/LongSpec.

**Link**: [arxiv](http://arxiv.org/abs/2502.17421v1),  [pdf](http://arxiv.org/pdf/2502.17421v1)

**Tags**: cs.CL cs.AI cs.LG 



### GTX: A Write-Optimized Latch-free Graph Data System with Transactional   Support -- Extended Version
**Authors**: Libin Zhou, Lu Xing, Yeasir Rayhan, Walid. G. Aref

**Updated**: 2025-02-24T18:51:48Z

**Summary**: This paper introduces GTX, a standalone main-memory write-optimized graph data system that specializes in structural and graph property updates while enabling concurrent reads and graph analytics through ACID transactions. Recent graph systems target concurrent read and write support while guaranteeing transaction semantics. However, their performance suffers from updates with real-world temporal locality over the same vertices and edges due to vertex-centric lock contentions. GTX has an adaptive delta-chain locking protocol on top of a carefully designed latch-free graph storage. It eliminates vertex-level locking contention, and adapts to real-life workloads while maintaining sequential access to the graph's adjacency lists storage. GTX's transactions further support cache-friendly block level concurrency control, and cooperative group commit and garbage collection. This combination of features ensures high update throughput and provides low-latency graph analytics. Based on experimental evaluation, in addition to not sacrificing the performance of read-heavy analytical workloads, and having competitive performance similar to state-of-the-art systems, GTX has high read-write transaction throughput. For write-heavy transactional workloads, GTX achieves up to 11x better transaction throughput than the best-performing state-of-the-art system.

**Link**: [arxiv](http://arxiv.org/abs/2405.01418v2),  [pdf](http://arxiv.org/pdf/2405.01418v2)

**Tags**: cs.DB H.2.4 



### Evaluating IOMMU-Based Shared Virtual Addressing for RISC-V Embedded   Heterogeneous SoCs
**Authors**: Cyril Koenig, Enrico Zelioli, Luca Benini

**Updated**: 2025-02-24T18:26:22Z

**Summary**: Embedded heterogeneous systems-on-chip (SoCs) rely on domain-specific hardware accelerators to improve performance and energy efficiency. In particular, programmable multi-core accelerators feature a cluster of processing elements and tightly coupled scratchpad memories to balance performance, energy efficiency, and flexibility. In embedded systems running a general-purpose OS, accelerators access data via dedicated, physically addressed memory regions. This negatively impacts memory utilization and performance by requiring a copy from the virtual host address to the physical accelerator address space. Input-Output Memory Management Units (IOMMUs) overcome this limitation by allowing devices and hosts to use a shared virtual paged address space. However, resolving IO virtual addresses can be particularly costly on high-latency memory systems as it requires up to three sequential memory accesses on IOTLB miss. In this work, we present a quantitative evaluation of shared virtual addressing in RISC-V heterogeneous embedded systems. We integrate an IOMMU in an open-source heterogeneous RISC-V SoC consisting of a 64-bit host with a 32-bit accelerator cluster. We evaluated the system performance by emulating the design on FPGA and implementing compute kernels from the RajaPERF benchmark suite using heterogeneous OpenMP programming. We measure the transfers and computation time on the host and accelerators for systems with different DRAM access latencies. We first show that IO virtual address translation can account for 4.2% up to 17.6% of the accelerator's runtime for gemm (General Matrix Multiplication) at low and high memory bandwidth. Then, we show that in systems containing a last-level cache, this IO address translation cost falls to 0.4% and 0.7% under the same conditions, making shared virtual addressing and zero-copy offloading suitable for such RISC-V heterogeneous SoCs.

**Link**: [arxiv](http://arxiv.org/abs/2502.17398v1),  [pdf](http://arxiv.org/pdf/2502.17398v1)

**Tags**: cs.AR 



### SepLLM: Accelerate Large Language Models by Compressing One Segment into   One Separator
**Authors**: Guoxuan Chen, Han Shi, Jiawei Li, Yihang Gao, Xiaozhe Ren, Yimeng Chen, Xin Jiang, Zhenguo Li, Weiyang Liu, Chao Huang

**Updated**: 2025-02-24T15:42:59Z

**Summary**: Large Language Models (LLMs) have exhibited exceptional performance across a spectrum of natural language processing tasks. However, their substantial sizes pose considerable challenges, particularly in computational demands and inference speed, due to their quadratic complexity. In this work, we have identified a key pattern: certain seemingly meaningless separator tokens (i.e., punctuations) contribute disproportionately to attention scores compared to semantically meaningful tokens. This observation suggests that information of the segments between these separator tokens can be effectively condensed into the separator tokens themselves without significant information loss. Guided by this insight, we introduce SepLLM, a plug-and-play framework that accelerates inference by compressing these segments and eliminating redundant tokens. Additionally, we implement efficient kernels for training acceleration. Experimental results across training-free, training-from-scratch, and post-training settings demonstrate SepLLM's effectiveness. Notably, using the Llama-3-8B backbone, SepLLM achieves over 50% reduction in KV cache on the GSM8K-CoT benchmark while maintaining comparable performance. Furthermore, in streaming settings, SepLLM effectively processes sequences of up to 4 million tokens or more while maintaining consistent language modeling capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2412.12094v5),  [pdf](http://arxiv.org/pdf/2412.12094v5)

**Tags**: cs.CL cs.AI cs.LG 



### The Lottery LLM Hypothesis, Rethinking What Abilities Should LLM   Compression Preserve?
**Authors**: Zhenheng Tang, Xiang Liu, Qian Wang, Peijie Dong, Bingsheng He, Xiaowen Chu, Bo Li

**Updated**: 2025-02-24T15:39:35Z

**Summary**: Motivated by reducing the computational and storage costs of LLMs, model compression and KV cache compression have attracted much attention from researchers. However, current methods predominantly emphasize maintaining the performance of compressed LLMs, as measured by perplexity or simple accuracy on tasks of common sense knowledge QA and basic arithmetic reasoning. In this blog, we present a brief review of recent advancements in LLMs related to retrieval-augmented generation, multi-step reasoning, external tools, and computational expressivity, all of which substantially enhance LLM performance. Then, we propose a lottery LLM hypothesis suggesting that for a given LLM and task, there exists a smaller lottery LLM capable of producing the same performance as the original LLM with the assistance of multi-step reasoning and external tools. Based on the review of current progress in LLMs, we discuss and summarize the essential capabilities that the lottery LLM and KV cache compression must possess, which are currently overlooked in existing methods.

**Link**: [arxiv](http://arxiv.org/abs/2502.17535v1),  [pdf](http://arxiv.org/pdf/2502.17535v1)

**Tags**: cs.LG cs.AI cs.CL cs.FL 



### Round Attention: A Novel Round-Level Attention Mechanism to Accelerate   LLM Inference
**Authors**: Yaohua Tang, Zhicheng Hu, Kun Cheng, Fan Mo, Qiheng Lv, Hua Wang, Zhi Chen

**Updated**: 2025-02-24T13:35:18Z

**Summary**: The increasing context window size in large language models (LLMs) has improved their ability to handle complex, long-text tasks. However, as the conversation rounds continue, it is required to store a large amount of KV cache in GPU memory, which significantly affects the efficiency and even availability of the model serving systems. This paper analyzes dialogue data from real users and discovers that the LLM inference manifests a watershed layer, after which the distribution of round-level attention shows notable similarity. We propose Round Attention, a novel round-level attention mechanism that only recalls and computes the KV cache of the most relevant rounds. The experiments show that our method saves 55\% memory usage without compromising model performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.15294v2),  [pdf](http://arxiv.org/pdf/2502.15294v2)

**Tags**: cs.CL cs.AI 



### CodeSwift: Accelerating LLM Inference for Efficient Code Generation
**Authors**: Qianhui Zhao, Li Zhang, Fang Liu, Xiaoli Lian, Qiaoyuanhe Meng, Ziqian Jiao, Zetong Zhou, Borui Zhang, Runlin Guo, Jia Li

**Updated**: 2025-02-24T13:30:30Z

**Summary**: Code generation is a latency-sensitive task that demands high timeliness, but the autoregressive decoding mechanism of Large Language Models (LLMs) leads to poor inference efficiency. Existing LLM inference acceleration methods mainly focus on standalone functions using only built-in components. Moreover, they treat code like natural language sequences, ignoring its unique syntax and semantic characteristics. As a result, the effectiveness of these approaches in code generation tasks remains limited and fails to align with real-world programming scenarios. To alleviate this issue, we propose CodeSwift, a simple yet highly efficient inference acceleration approach specifically designed for code generation, without comprising the quality of the output. CodeSwift constructs a multi-source datastore, providing access to both general and project-specific knowledge, facilitating the retrieval of high-quality draft sequences. Moreover, CodeSwift reduces retrieval cost by controlling retrieval timing, and enhances efficiency through parallel retrieval and a context- and LLM preference-aware cache. Experimental results show that CodeSwift can reach up to 2.53x and 2.54x speedup compared to autoregressive decoding in repository-level and standalone code generation tasks, respectively, outperforming state-of-the-art inference acceleration approaches by up to 88%.

**Link**: [arxiv](http://arxiv.org/abs/2502.17139v1),  [pdf](http://arxiv.org/pdf/2502.17139v1)

**Tags**: cs.AI cs.SE 



### DBudgetKV: Dynamic Budget in KV Cache Compression for Ensuring Optimal   Performance
**Authors**: Xuanfan Ni, Liyan Xu, Chenyang Lyu, Longyue Wang, Mo Yu, Lemao Liu, Fandong Meng, Jie Zhou, Piji Li

**Updated**: 2025-02-24T06:33:39Z

**Summary**: To alleviate memory burden during inference of large language models (LLMs), numerous studies have focused on compressing the KV cache by exploring aspects such as attention sparsity. However, these techniques often require a pre-defined cache budget; as the optimal budget varies with different input lengths and task types, it limits their practical deployment accepting open-domain instructions. To address this limitation, we propose a new KV cache compression objective: to always ensure the full-cache performance regardless of specific inputs, while maximizing KV cache pruning as much as possible. To achieve this goal, we introduce a novel KV cache compression method dubbed DBudgetKV, which features an attention-based metric to signal when the remaining KV cache is unlikely to match the full-cache performance, then halting the pruning process. Empirical evaluation spanning diverse context lengths, task types, and model sizes suggests that our method achieves lossless KV pruning effectively and robustly, exceeding 25% compression ratio on average. Furthermore, our method is easy to integrate within LLM inference, not only optimizing memory space, but also showing reduced inference time compared to existing methods.

**Link**: [arxiv](http://arxiv.org/abs/2502.16886v1),  [pdf](http://arxiv.org/pdf/2502.16886v1)

**Tags**: cs.CL cs.AI 



### BaKlaVa -- Budgeted Allocation of KV cache for Long-context Inference
**Authors**: Ahmed Burak Gulhan, Krishna Teja Chitty-Venkata, Murali Emani, Mahmut Kandemir, Venkatram Vishwanath

**Updated**: 2025-02-24T01:28:27Z

**Summary**: In Large Language Model (LLM) inference, Key-Value (KV) caches (KV-caches) are essential for reducing time complexity. However, they result in a linear increase in GPU memory as the context length grows. While recent work explores KV-cache eviction and compression policies to reduce memory usage, they often consider uniform KV-caches across all attention heads, leading to suboptimal performance. We introduce BaKlaVa, a method to allocate optimal memory for individual KV-caches across the model by estimating the importance of each KV-cache. Our empirical analysis demonstrates that not all KV-caches are equally critical for LLM performance. Using a one-time profiling approach, BaKlaVa assigns optimal memory budgets to each KV-cache. We evaluated our method on LLaMA-3-8B, and Qwen2.5-7B models, achieving up to a 70\% compression ratio while keeping baseline performance and delivering up to an order-of-magnitude accuracy improvement at higher compression levels.

**Link**: [arxiv](http://arxiv.org/abs/2502.13176v2),  [pdf](http://arxiv.org/pdf/2502.13176v2)

**Tags**: cs.LG cs.AI 



### Don't Do RAG: When Cache-Augmented Generation is All You Need for   Knowledge Tasks
**Authors**: Brian J Chan, Chao-Ting Chen, Jui-Hung Cheng, Hen-Hsen Huang

**Updated**: 2025-02-23T19:48:12Z

**Summary**: Retrieval-augmented generation (RAG) has gained traction as a powerful approach for enhancing language models by integrating external knowledge sources. However, RAG introduces challenges such as retrieval latency, potential errors in document selection, and increased system complexity. With the advent of large language models (LLMs) featuring significantly extended context windows, this paper proposes an alternative paradigm, cache-augmented generation (CAG) that bypasses real-time retrieval. Our method involves preloading all relevant resources, especially when the documents or knowledge for retrieval are of a limited and manageable size, into the LLM's extended context and caching its runtime parameters. During inference, the model utilizes these preloaded parameters to answer queries without additional retrieval steps. Comparative analyses reveal that CAG eliminates retrieval latency and minimizes retrieval errors while maintaining context relevance. Performance evaluations across multiple benchmarks highlight scenarios where long-context LLMs either outperform or complement traditional RAG pipelines. These findings suggest that, for certain applications, particularly those with a constrained knowledge base, CAG provide a streamlined and efficient alternative to RAG, achieving comparable or superior results with reduced complexity.

**Link**: [arxiv](http://arxiv.org/abs/2412.15605v2),  [pdf](http://arxiv.org/pdf/2412.15605v2)

**Tags**: cs.CL 



### Simultaneously Transmitting And Reflecting Surfaces (STARS) for   Multi-Functional 6G
**Authors**: Xidong Mu, Zhaolin Wang, Yuanwei Liu

**Updated**: 2025-02-23T16:17:34Z

**Summary**: Simultaneously transmitting and reflecting surface (STARS) empowered multi-functional 6G wireless networks are investigated. Starting with the communication functionality, various types of STARS are introduced in terms of power amplification capabilities, reciprocity features, and spatial density of elements. Then, three STARS-empowered wireless sensing architectures are proposed, namely STARS-aided monostatic sensing, STARS-enabled bistatic sensing, and sensing with target-mounted STARS, where the representative benefits and application challenges are identified. Furthermore, promising applications of STARS for computing and caching functionalities are explored to improve the computation efficiency and reduce the content delivery latency. Finally, recent standardization progress for reconfigurable intelligent surfaces is presented for motivating the employment of STARS in multi-functional 6G.

**Link**: [arxiv](http://arxiv.org/abs/2502.16632v1),  [pdf](http://arxiv.org/pdf/2502.16632v1)

**Tags**: cs.IT math.IT 



### A New Construction Structure on Coded Caching with Linear   Subpacketization: Non-Half-Sum Disjoint Packing
**Authors**: Minquan Cheng, Huimei Wei, Kai Wan, Giuseppe Caire

**Updated**: 2025-02-23T11:52:45Z

**Summary**: Coded caching is a promising technique to effectively reduce peak traffic by using local caches and the multicast gains generated by these local caches. We prefer to design a coded caching scheme with the subpacketization $F$ and transmission load $R$ as small as possible since these are the key metrics for evaluating the implementation complexity and transmission efficiency of the scheme, respectively. However, most of the existing coded caching schemes have large subpacketizations which grow exponentially with the number of users $K$, and there are a few schemes with linear subpacketizations which have large transmission loads. In this paper, we focus on studying the linear subpacketization, i.e., $K=F$, coded caching scheme with low transmission load. Specifically, we first introduce a new combinatorial structure called non-half-sum disjoint packing (NHSDP) which can be used to generate a coded caching scheme with $K=F$. Then a class of new schemes is obtained by constructing NHSDP. Theoretical and numerical comparisons show that (i) compared to the existing schemes with linear subpacketization (to the number of users), the proposed scheme achieves a lower load; (ii) compared to some existing schemes with polynomial subpacketization, the proposed scheme can also achieve a lower load in some cases; (iii) compared to some existing schemes with exponential subpacketization, the proposed scheme has loads close to those of these schemes in some cases. Moreover, the new concept of NHSDP is closely related to the classical combinatorial structures such as cyclic difference packing (CDP), non-three-term arithmetic progressions (NTAP), and perfect hash family (PHF). These connections indicate that NHSDP is an important combinatorial structure in the field of combinatorial design.

**Link**: [arxiv](http://arxiv.org/abs/2501.11855v3),  [pdf](http://arxiv.org/pdf/2501.11855v3)

**Tags**: cs.IT math.IT 



### Cache Coherence Over Disaggregated Memory
**Authors**: Ruihong Wang, Jianguo Wang, Walid G. Aref

**Updated**: 2025-02-23T03:27:01Z

**Summary**: Disaggregating memory from compute offers the opportunity to better utilize stranded memory in cloud data centers. It is important to cache data in the compute nodes and maintain cache coherence across multiple compute nodes. However, the limited computing power on disaggregated memory servers makes traditional cache coherence protocols suboptimal, particularly in the case of stranded memory. This paper introduces SELCC; a Shared-Exclusive Latch Cache Coherence protocol that maintains cache coherence without imposing any computational burden on the remote memory side. It aligns the state machine of the shared-exclusive latch protocol with the MSI protocol , thereby ensuring both atomicity of data access and cache coherence with sequential consistency. SELCC embeds cache-ownership metadata directly into the RDMA latch word, enabling efficient cache ownership management via RDMA atomic operations. SELCC can serve as an abstraction layer over disaggregated memory with APIs that resemble main-memory accesses. A concurrent B-tree and three transaction concurrency control algorithms are realized using SELCC's abstraction layer. Experimental results show that SELCC significantly outperforms Remote-Procedure-Call-based protocols for cache coherence under limited remote computing power. Applications on SELCC achieve comparable or superior performance over disaggregated memory compared to competitors.

**Link**: [arxiv](http://arxiv.org/abs/2409.02088v4),  [pdf](http://arxiv.org/pdf/2409.02088v4)

**Tags**: cs.DB cs.DC cs.ET 



### PLDR-LLMs Learn A Generalizable Tensor Operator That Can Replace Its Own   Deep Neural Net At Inference
**Authors**: Burc Gokden

**Updated**: 2025-02-22T22:32:08Z

**Summary**: We show that Large Language Model from Power Law Decoder Representations (PLDR-LLM) is a foundational model whose deductive outputs are invariant tensors up to a small perturbation. PLDR-LLM learns a singularity condition for the deductive outputs that enable the once-inferred energy-curvature tensor $\mathbf{G}_{LM}$ to replace the deep neural network of power law graph attention (PLGA) generating the deductive outputs at inference. We demonstrate that a cache for $\mathbf{G}_{LM}$ (G-cache) and KV-cache can be implemented in a straightforward manner to improve the inference time. The invariance and generalizable nature of deductive outputs is at a very high fidelity where deductive outputs have same RMSE and determinant values up to 15 decimal places after caching, and zero-shot benchmark scores remain unchanged. Ablation studies show that learned deductive outputs have distinct loss and accuracy characteristics from models pretrained with transferred, randomly initialized or identity tensors as a constant tensor operator and an LLM with scaled-dot product attention (SDPA) is a special case of PLDR-LLM where $\mathbf{G}_{LM}$ is predefined as identity. The observed invariance characteristic introduces a novel asymmetry between training and inference phases with caching. We outline observed common characteristics of the deductive outputs for the learned singularity condition. We provide an implementation of a training and inference framework for PLDR-LLM with KV-cache and G-cache.

**Link**: [arxiv](http://arxiv.org/abs/2502.13502v2),  [pdf](http://arxiv.org/pdf/2502.13502v2)

**Tags**: cs.CL cs.AI cs.LG 



### Warp-centric GPU meta-meshing and fast triangulation of billion-scale   lattice structures
**Authors**: Qiang Zou, Yunzhu Gao

**Updated**: 2025-02-22T10:31:51Z

**Summary**: Lattice structures have been widely used in applications due to their superior mechanical properties. To fabricate such structures, a geometric processing step called triangulation is often employed to transform them into the STL format before sending them to 3D printers. Because lattice structures tend to have high geometric complexity, this step usually generates a large amount of triangles, a memory and compute-intensive task. This problem manifests itself clearly through large-scale lattice structures that have millions or billions of struts. To address this problem, this paper proposes to transform a lattice structure into an intermediate model called meta-mesh before undergoing real triangulation. Compared to triangular meshes, meta-meshes are very lightweight and much less compute-demanding. The meta-mesh can also work as a base mesh reusable for conveniently and efficiently triangulating lattice structures with arbitrary resolutions. A CPU+GPU asynchronous meta-meshing pipeline has been developed to efficiently generate meta-meshes from lattice structures. It shifts from the thread-centric GPU algorithm design paradigm commonly used in CAD to the recent warp-centric design paradigm to achieve high performance. This is achieved by a new data compression method, a GPU cache-aware data structure, and a workload-balanced scheduling method that can significantly reduce memory divergence and branch divergence. Experimenting with various billion-scale lattice structures, the proposed method is seen to be two orders of magnitude faster than previously achievable.

**Link**: [arxiv](http://arxiv.org/abs/2405.15197v3),  [pdf](http://arxiv.org/pdf/2405.15197v3)

**Tags**: cs.CG 



### KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse
**Authors**: Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, Shiyu Chang

**Updated**: 2025-02-21T23:34:29Z

**Summary**: We describe KVLink, an approach for efficient key-value (KV) cache reuse in large language models (LLMs). In many LLM applications, different inputs can share overlapping context, such as the same retrieved document appearing in multiple queries. However, the LLMs still need to encode the entire context for each query, leading to redundant computation. In this paper, we propose a new strategy to eliminate such inefficiency, where the KV cache of each document is precomputed independently. During inference, the KV caches of retrieved documents are concatenated, allowing the model to reuse cached representations instead of recomputing them. To mitigate the performance degradation of LLMs when using KV caches computed independently for each document, KVLink introduces three key components: adjusting positional embeddings of the KV cache at inference to match the global position after concatenation, using trainable special tokens to restore self-attention across independently encoded documents, and applying mixed-data fine-tuning to enhance performance while preserving the model's original capabilities. Experiments across 7 datasets demonstrate that KVLink improves question answering accuracy by an average of 4% over state-of-the-art methods. Furthermore, by leveraging precomputed KV caches, our approach reduces time-to-first-token by up to 90% compared to standard LLM inference, making it a scalable and efficient solution for context reuse.

**Link**: [arxiv](http://arxiv.org/abs/2502.16002v1),  [pdf](http://arxiv.org/pdf/2502.16002v1)

**Tags**: cs.CL 



### Compression Barriers for Autoregressive Transformers
**Authors**: Themistoklis Haris, Krzysztof Onak

**Updated**: 2025-02-21T21:37:52Z

**Summary**: A key limitation of autoregressive Transformers is the large memory needed at inference-time to cache all previous key-value (KV) embeddings. Prior works address this by compressing the KV cache, but often assume specific structural properties of the embeddings. This raises the following natural question: Can truly sublinear space utilization be achieved without such assumptions? In this work, we answer this question in the negative. Any algorithm for attention-based token generation must use $\Theta(nd)$ space, where $n$ is the number of tokens generated so far and $d = \Omega(\log n)$ is the dimension of the KV embeddings. Our proof involves a reduction from a classic communication complexity problem and uses a randomized construction that leverages properties of projections in the spirit of the Johnson-Linderstrauss lemma. For the low-dimensional regime $d = o(\log n)$, we show that any algorithm requires $\Omega(d\cdot e^d)$ space and prove, using tight bounds on covering numbers, that SubGen, proposed by Zandieh, Han, Mirrokni and Karbasi, matches this bound. Further, we investigate how sparsity assumptions enable token generation in truly sublinear space, presenting impossibility results and proposing a new KV cache compression algorithm for sliding window attention when the value cache outside the window is unmasked. Finally, we analyze token generation's time complexity, using an indistinguishability argument to prove that no non-adaptive algorithm can compute attention online in sublinear time for all tokens.

**Link**: [arxiv](http://arxiv.org/abs/2502.15955v1),  [pdf](http://arxiv.org/pdf/2502.15955v1)

**Tags**: cs.DS cs.AI cs.CC cs.LG 



### U-index: A Universal Indexing Framework for Matching Long Patterns
**Authors**: Lorraine A. K. Ayad, Gabriele Fici, Ragnar Groot Koerkamp, Grigorios Loukides, Rob Patro, Giulio Ermanno Pibiri, Solon P. Pissis

**Updated**: 2025-02-21T13:35:43Z

**Summary**: Text indexing is a fundamental and well-studied problem. Classic solutions either replace the original text with a compressed representation, e.g., the FM-index and its variants, or keep it uncompressed but attach some redundancy - an index - to accelerate matching. The former solutions thus retain excellent compressed space, but areslow in practice. The latter approaches, like the suffix array, instead sacrifice space for speed.   We show that efficient text indexing can be achieved using just a small extra space on top of the original text, provided that the query patterns are sufficiently long. More specifically, we develop a new indexing paradigm in which a sketch of a query pattern is first matched against a sketch of the text. Once candidate matches are retrieved, they are verified using the original text. This paradigm is thus universal in the sense that it allows us to use any solution to index the sketched text, like a suffix array, FM-index, or r-index.   We explore both the theory and the practice of this universal framework. With an extensive experimental analysis, we show that, surprisingly, universal indexes can be constructed much faster than their unsketched counterparts and take a fraction of the space, as a direct consequence of (i) having a lower bound on the length of patterns and (ii) working in sketch space. Furthermore, these data structures have the potential of retaining or even improving query time, because matching against the sketched text is faster and verifying candidates can be theoretically done in constant time per occurrence (or, in practice, by short and cache-friendly scans of the text). Finally, we discuss some important applications of this novel indexing paradigm to computational biology. We hypothesize that such indexes will be particularly effective when the queries are sufficiently long, and so demonstrate applications in long-read mapping.

**Link**: [arxiv](http://arxiv.org/abs/2502.14488v2),  [pdf](http://arxiv.org/pdf/2502.14488v2)

**Tags**: cs.DS F.2.2; J.3 



### CoKV: Optimizing KV Cache Allocation via Cooperative Game
**Authors**: Qiheng Sun, Hongwei Zhang, Haocheng Xia, Jiayao Zhang, Jinfei Liu, Kui Ren

**Updated**: 2025-02-21T12:03:07Z

**Summary**: Large language models (LLMs) have achieved remarkable success on various aspects of human life. However, one of the major challenges in deploying these models is the substantial memory consumption required to store key-value pairs (KV), which imposes significant resource demands. Recent research has focused on KV cache budget allocation, with several approaches proposing head-level budget distribution by evaluating the importance of individual attention heads. These methods, however, assess the importance of heads independently, overlooking their cooperative contributions within the model, which may result in a deviation from their true impact on model performance. In light of this limitation, we propose CoKV, a novel method that models the cooperation between heads in model inference as a cooperative game. By evaluating the contribution of each head within the cooperative game, CoKV can allocate the cache budget more effectively. Extensive experiments show that CoKV achieves state-of-the-art performance on the LongBench benchmark using LLama-3-8B-Instruct and Mistral-7B models.

**Link**: [arxiv](http://arxiv.org/abs/2502.17501v1),  [pdf](http://arxiv.org/pdf/2502.17501v1)

**Tags**: cs.LG cs.AI 



### SVDq: 1.25-bit and 410x Key Cache Compression for LLM Attention
**Authors**: Hong Yankun, Li Xing, Zhen Hui-Ling, Yu Xianzhi, Liu Wulong, Yuan Mingxuan

**Updated**: 2025-02-21T08:55:21Z

**Summary**: For the efficient inference of Large Language Models (LLMs), the effective compression of key-value (KV) cache is essential. Three main types of KV cache compression techniques, namely sparsity, channel compression, and quantization, have been identified. This study presents SVDq, a Singular Value Decomposition (SVD) - based mixed precision quantization method for K cache. Initially, K cache is transformed into latent channels using SVD basis representations. Since the values in latent channels decay rapidly and become negligible after only a few latent channels, our method then incorporates importance-aware quantization and compression for latent channels. This enables the effective allocation of higher precision to more significant channels. Theoretically, we prove that SVDq results in quantization errors (x0.1 or even lower) that are much lower than those of per-channel key quantization in the original space. Our findings based on RULER and LongBench benchmarks demonstrate that SVDq can achieve an equivalent key cache precision as low as 1.25-bit. When combined with key sparsity, it can reach a key compression ratio of up to 410x for attention computation, all while maintaining comparable model performance. Notably, our method is nearly lossless for LongBench datasets. This indicates that SVDq enables high-precision low-bit quantization, providing a more efficient solution for KV cache compression in LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2502.15304v1),  [pdf](http://arxiv.org/pdf/2502.15304v1)

**Tags**: cs.LG cs.AI cs.CL 68T50 



### SAAP: Spatial awareness and Association based Prefetching of Virtual   Objects in Augmented Reality at the Edge
**Authors**: Nikhil Sreekumar, Abhishek Chandra, Jon Weissman

**Updated**: 2025-02-21T04:07:00Z

**Summary**: Mobile Augmented Reality (MAR) applications face performance challenges due to their high computational demands and need for low-latency responses. Traditional approaches like on-device storage or reactive data fetching from the cloud often result in limited AR experiences or unacceptable lag. Edge caching, which caches AR objects closer to the user, provides a promising solution. However, existing edge caching approaches do not consider AR-specific features such as AR object sizes, user interactions, and physical location. This paper investigates how to further optimize edge caching by employing AR-aware prefetching techniques. We present SAAP, a Spatial Awareness and Association-based Prefetching policy specifically designed for MAR Caches. SAAP intelligently prioritizes the caching of virtual objects based on their association with other similar objects and the user's proximity to them. It also considers the recency of associations and uses a lazy fetching strategy to efficiently manage edge resources and maximize Quality of Experience (QoE).   Through extensive evaluation using both synthetic and real-world workloads, we demonstrate that SAAP significantly improves cache hit rates compared to standard caching algorithms, achieving gains ranging from 3\% to 40\% while reducing the need for on-demand data retrieval from the cloud. Further, we present an adaptive tuning algorithm that automatically tunes SAAP parameters to achieve optimal performance. Our findings demonstrate the potential of SAAP to substantially enhance the user experience in MAR applications by ensuring the timely availability of virtual objects.

**Link**: [arxiv](http://arxiv.org/abs/2502.15192v1),  [pdf](http://arxiv.org/pdf/2502.15192v1)

**Tags**: cs.ET cs.DC 



### Compute Or Load KV Cache? Why Not Both?
**Authors**: Shuowei Jin, Xueshen Liu, Qingzhao Zhang, Z. Morley Mao

**Updated**: 2025-02-20T23:28:01Z

**Summary**: Large Language Models (LLMs) are increasingly deployed in large-scale online services, enabling sophisticated applications. However, the computational overhead of generating key-value (KV) caches in the prefill stage presents a major bottleneck, particularly for long-context inputs. Prefix caching mitigates this issue by storing KV caches for reuse, reducing redundant computation. Despite its advantages, prefix caching suffers from high latency due to the limited I/O bandwidth of storage devices, constraining inference efficiency. To address this challenge, we introduce Cake, a novel KV cache loading system that optimally utilizes both computational and I/O resources in parallel. Cake employs a bidirectional scheduling strategy that dynamically balances KV cache computation and loading, ensuring efficient resource utilization. Additionally, Cake incorporates an adaptive scheduling mechanism that seamlessly integrates with non-prefix caching requests, improving system throughput and adapting to fluctuating resource availabilty. Through extensive evaluations across various hardware configurations, datasets, and storage conditions, Cake achieves on average 2.6x reduction in Time to First Token (TTFT) compared to compute-only and I/O-only methods. Our findings highlight Cake as an effective and practical solution for optimizing long-context LLM inference, bridging the gap between computation and I/O efficiency in large-scale AI deployments.

**Link**: [arxiv](http://arxiv.org/abs/2410.03065v2),  [pdf](http://arxiv.org/pdf/2410.03065v2)

**Tags**: cs.LG 



### More for Keys, Less for Values: Adaptive KV Cache Quantization
**Authors**: Mohsen Hariri, Lam Nguyen, Sixu Chen, Shaochen Zhong, Qifan Wang, Xia Hu, Xiaotian Han, Vipin Chaudhary

**Updated**: 2025-02-20T22:24:27Z

**Summary**: This paper introduces an information-aware quantization framework that adaptively compresses the key-value (KV) cache in large language models (LLMs). Although prior work has underscored the distinct roles of key and value cache during inference, our systematic analysis -- examining singular value distributions, spectral norms, and Frobenius norms -- reveals, for the first time, that key matrices consistently exhibit higher norm values and are more sensitive to quantization than value matrices. Furthermore, our theoretical analysis shows that matrices with higher spectral norms amplify quantization errors more significantly. Motivated by these insights, we propose a mixed-precision quantization strategy, KV-AdaQuant, which allocates more bit-width for keys and fewer for values since key matrices have higher norm values. With the same total KV bit budget, this approach effectively mitigates error propagation across transformer layers while achieving significant memory savings. Our extensive experiments on multiple LLMs (1B--70B) demonstrate that our mixed-precision quantization scheme maintains high model accuracy even under aggressive compression. For instance, using 4-bit for Key and 2-bit for Value achieves an accuracy of 75.2%, whereas reversing the assignment (2-bit for Key and 4-bit for Value) yields only 54.7% accuracy. The code is available at https://tinyurl.com/kv-adaquant

**Link**: [arxiv](http://arxiv.org/abs/2502.15075v1),  [pdf](http://arxiv.org/pdf/2502.15075v1)

**Tags**: cs.LG 



### LServe: Efficient Long-sequence LLM Serving with Unified Sparse   Attention
**Authors**: Shang Yang, Junxian Guo, Haotian Tang, Qinghao Hu, Guangxuan Xiao, Jiaming Tang, Yujun Lin, Zhijian Liu, Yao Lu, Song Han

**Updated**: 2025-02-20T18:59:52Z

**Summary**: Large language models (LLMs) have shown remarkable potential in processing long sequences, yet efficiently serving these long-context models remains challenging due to the quadratic computational complexity of attention in the prefilling stage and the large memory footprint of the KV cache in the decoding stage. To address these issues, we introduce LServe, an efficient system that accelerates long-sequence LLM serving via hybrid sparse attention. This method unifies different hardware-friendly, structured sparsity patterns for both prefilling and decoding attention into a single framework, where computations on less important tokens are skipped block-wise. LServe demonstrates the compatibility of static and dynamic sparsity in long-context LLM attention. This design enables multiplicative speedups by combining these optimizations. Specifically, we convert half of the attention heads to nearly free streaming heads in both the prefilling and decoding stages. Additionally, we find that only a constant number of KV pages is required to preserve long-context capabilities, irrespective of context length. We then design a hierarchical KV page selection policy that dynamically prunes KV pages based on query-centric similarity. On average, LServe accelerates LLM prefilling by up to 2.9x and decoding by 1.3-2.1x over vLLM, maintaining long-context accuracy. Code is released at https://github.com/mit-han-lab/omniserve.

**Link**: [arxiv](http://arxiv.org/abs/2502.14866v1),  [pdf](http://arxiv.org/pdf/2502.14866v1)

**Tags**: cs.CL cs.AI cs.DC cs.LG cs.PF 



### Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent   Attention in Any Transformer-based LLMs
**Authors**: Tao Ji, Bin Guo, Yuanbin Wu, Qipeng Guo, Lixing Shen, Zhan Chen, Xipeng Qiu, Qi Zhang, Tao Gui

**Updated**: 2025-02-20T18:50:42Z

**Summary**: Multi-head Latent Attention (MLA) is an innovative architecture proposed by DeepSeek, designed to ensure efficient and economical inference by significantly compressing the Key-Value (KV) cache into a latent vector. Compared to MLA, standard LLMs employing Multi-Head Attention (MHA) and its variants such as Grouped-Query Attention (GQA) exhibit significant cost disadvantages. Enabling well-trained LLMs (e.g., Llama) to rapidly adapt to MLA without pre-training from scratch is both meaningful and challenging. This paper proposes the first data-efficient fine-tuning method for transitioning from MHA to MLA (MHA2MLA), which includes two key components: for partial-RoPE, we remove RoPE from dimensions of queries and keys that contribute less to the attention scores, for low-rank approximation, we introduce joint SVD approximations based on the pre-trained parameters of keys and values. These carefully designed strategies enable MHA2MLA to recover performance using only a small fraction (0.3% to 0.6%) of the data, significantly reducing inference costs while seamlessly integrating with compression techniques such as KV cache quantization. For example, the KV cache size of Llama2-7B is reduced by 92.19%, with only a 0.5% drop in LongBench performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.14837v1),  [pdf](http://arxiv.org/pdf/2502.14837v1)

**Tags**: cs.CL cs.AI 



### GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian   Splatting Models
**Authors**: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai

**Updated**: 2025-02-20T14:01:17Z

**Summary**: Rendering large-scale 3D Gaussian Splatting (3DGS) model faces significant challenges in achieving real-time, high-fidelity performance on consumer-grade devices. Fully realizing the potential of 3DGS in applications such as virtual reality (VR) requires addressing critical system-level challenges to support real-time, immersive experiences. We propose GS-Cache, an end-to-end framework that seamlessly integrates 3DGS's advanced representation with a highly optimized rendering system. GS-Cache introduces a cache-centric pipeline to eliminate redundant computations, an efficiency-aware scheduler for elastic multi-GPU rendering, and optimized CUDA kernels to overcome computational bottlenecks. This synergy between 3DGS and system design enables GS-Cache to achieve up to 5.35x performance improvement, 35% latency reduction, and 42% lower GPU memory usage, supporting 2K binocular rendering at over 120 FPS with high visual quality. By bridging the gap between 3DGS's representation power and the demands of VR systems, GS-Cache establishes a scalable and efficient framework for real-time neural rendering in immersive environments.

**Link**: [arxiv](http://arxiv.org/abs/2502.14938v1),  [pdf](http://arxiv.org/pdf/2502.14938v1)

**Tags**: cs.CV 



### PLPHP: Per-Layer Per-Head Vision Token Pruning for Efficient Large   Vision-Language Models
**Authors**: Yu Meng, Kaiyuan Li, Chenran Huang, Chen Gao, Xinlei Chen, Yong Li, Xiaoping Zhang

**Updated**: 2025-02-20T12:31:31Z

**Summary**: Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities across a range of multimodal tasks. However, their inference efficiency is constrained by the large number of visual tokens processed during decoding. To address this challenge, we propose Per-Layer Per-Head Vision Token Pruning (PLPHP), a two-level fine-grained pruning method including Layer-Level Retention Rate Allocation and Head-Level Vision Token Pruning. Motivated by the Vision Token Re-attention phenomenon across decoder layers, we dynamically adjust token retention rates layer by layer. Layers that exhibit stronger attention to visual information preserve more vision tokens, while layers with lower vision attention are aggressively pruned. Furthermore, PLPHP applies pruning at the attention head level, enabling different heads within the same layer to independently retain critical context. Experiments on multiple benchmarks demonstrate that PLPHP delivers an 18% faster decoding speed and reduces the Key-Value Cache (KV Cache) size by over 50%, all at the cost of 0.46% average performance drop, while also achieving notable performance improvements in multi-image tasks. These results highlight the effectiveness of fine-grained token pruning and contribute to advancing the efficiency and scalability of LVLMs. Our source code will be made publicly available.

**Link**: [arxiv](http://arxiv.org/abs/2502.14504v1),  [pdf](http://arxiv.org/pdf/2502.14504v1)

**Tags**: cs.CV cs.AI 



### More Tokens, Lower Precision: Towards the Optimal Token-Precision   Trade-off in KV Cache Compression
**Authors**: Jiebin Zhang, Dawei Zhu, Yifan Song, Wenhao Wu, Chuqiao Kuang, Xiaoguang Li, Lifeng Shang, Qun Liu, Sujian Li

**Updated**: 2025-02-20T12:14:49Z

**Summary**: As large language models (LLMs) process increasing context windows, the memory usage of KV cache has become a critical bottleneck during inference. The mainstream KV compression methods, including KV pruning and KV quantization, primarily focus on either token or precision dimension separately. However, these works leaving the trade-off between these two orthogonal dimensions largely under-explored. In this paper, we comprehensively investigate the token-precision trade-off in KV cache compression.Experiments demonstrate that storing more tokens in the KV cache with lower precision,a strategy we term quantized pruning, can significantly enhance the long-context performance of LLMs. In-depth analysis of the token-precision trade-off across key aspects demonstrates that, quantized pruning achieves substantial improvements in retrieval-related tasks and consistently performs well across varying input lengths. Furthermore, quantized pruning demonstrates notable stability and effectiveness across different KV pruning methods, quantization strategies, and model scales. These findings offer valuable insights into optimizing KV cache compression through balanced token-precision trade-off strategies. Our code is available at https://github.com/zhzihao/QPruningKV.

**Link**: [arxiv](http://arxiv.org/abs/2412.12706v2),  [pdf](http://arxiv.org/pdf/2412.12706v2)

**Tags**: cs.CL 



### Neural Attention Search
**Authors**: Difan Deng, Marius Lindauer

**Updated**: 2025-02-20T09:03:05Z

**Summary**: We present Neural Attention Search (NAtS), a framework that automatically evaluates the importance of each token within a sequence and determines if the corresponding token can be dropped after several steps. This approach can efficiently reduce the KV cache sizes required by transformer-based models during inference and thus reduce inference costs. In this paper, we design a search space that contains three token types: (i) Global Tokens will be preserved and queried by all the following tokens. (ii) Local Tokens survive until the next global token appears. (iii) Sliding Window Tokens have an impact on the inference of a fixed size of the next following tokens. Similar to the One-Shot Neural Architecture Search approach, this token-type information can be learned jointly with the architecture weights via a learnable attention mask. Experiments on both training a new transformer from scratch and fine-tuning existing large language models show that NAtS can efficiently reduce the KV cache size required for the models while maintaining the models' performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.13251v2),  [pdf](http://arxiv.org/pdf/2502.13251v2)

**Tags**: cs.CL cs.AI 



### Discovery of a new phase in thin flakes of KV$_{3}$Sb$_{5}$ under   pressure
**Authors**: Zheyu Wang, Lingfei Wang, King Yau Yip, Ying Kit Tsui, Tsz Fung Poon, Wenyan Wang, Chun Wai Tsang, Shanmin Wang, David Graf, Alexandre Pourret, Gabriel Seyfarth, Georg Knebel, Kwing To Lai, Wing Chi Yu, Wei Zhang, Swee K. Goh

**Updated**: 2025-02-20T08:00:25Z

**Summary**: We report results of magnetotransport measurements on KV$_3$Sb$_5$ thin flakes under pressure. Our zero-field electrical resistance reveals an additional anomaly emerging under pressure ($p$), marking a previously unidentified phase boundary $T^{\rm \ast}$($p$). Together with the established $T_{\rm CDW}(p)$ and $T_c(p)$, denoting the charge-density-wave transition and a superconducting transition, respectively, the temperature-pressure phase diagram of KV$_3$Sb$_5$ features a rich interplay among multiple phases. The Hall coefficient evolves reasonably smoothly when crossing the $T^{\rm \ast}$ phase boundary compared with the variation when crossing $T_{\rm CDW}$, indicating the preservation of the pristine electronic structure. The mobility spectrum analysis provides further insights into distinguishing different phases. Finally, our high-pressure quantum oscillation studies up to 31 T combined with density functional theory calculations further demonstrate that the new phase does not reconstruct the Fermi surface, confirming that the translational symmetry of the pristine metallic state is preserved.

**Link**: [arxiv](http://arxiv.org/abs/2502.14347v1),  [pdf](http://arxiv.org/pdf/2502.14347v1)

**Tags**: cond-mat.supr-con cond-mat.str-el 



### ParallelComp: Parallel Long-Context Compressor for Length Extrapolation
**Authors**: Jing Xiong, Jianghan Shen, Chuanyang Zheng, Zhongwei Wan, Chenyang Zhao, Chiwun Yang, Fanghua Ye, Hongxia Yang, Lingpeng Kong, Ngai Wong

**Updated**: 2025-02-20T07:10:43Z

**Summary**: Efficiently handling long contexts is crucial for large language models (LLMs). While rotary position embeddings (RoPEs) enhance length generalization, effective length extrapolation remains challenging and often requires costly fine-tuning. In contrast, recent training-free approaches suffer from the attention sink phenomenon, leading to severe performance degradation. In this paper, we introduce ParallelComp, a novel training-free method for long-context extrapolation that extends LLMs' context length from 4K to 128K while maintaining high throughput and preserving perplexity, and integrates seamlessly with Flash Attention. Our analysis offers new insights into attention biases in parallel attention mechanisms and provides practical solutions to tackle these challenges. To mitigate the attention sink issue, we propose an attention calibration strategy that reduces biases, ensuring more stable long-range attention. Additionally, we introduce a chunk eviction strategy to efficiently manage ultra-long contexts on a single A100 80GB GPU. To further enhance efficiency, we propose a parallel KV cache eviction technique, which improves chunk throughput by 1.76x, thereby achieving a 23.50x acceleration in the prefilling stage with negligible performance loss due to attention calibration. Furthermore, ParallelComp achieves 91.17% of GPT-4's performance on long-context tasks using an 8B model trained on 8K-length context, outperforming powerful closed-source models such as Claude-2 and Kimi-Chat.

**Link**: [arxiv](http://arxiv.org/abs/2502.14317v1),  [pdf](http://arxiv.org/pdf/2502.14317v1)

**Tags**: cs.CL 



### μRL: Discovering Transient Execution Vulnerabilities Using   Reinforcement Learning
**Authors**: M. Caner Tol, Kemal Derya, Berk Sunar

**Updated**: 2025-02-20T06:42:03Z

**Summary**: We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process.   We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors.   When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $\mu$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

**Link**: [arxiv](http://arxiv.org/abs/2502.14307v1),  [pdf](http://arxiv.org/pdf/2502.14307v1)

**Tags**: cs.CR cs.AR cs.LG 



### SpinQuant: LLM quantization with learned rotations
**Authors**: Zechun Liu, Changsheng Zhao, Igor Fedorov, Bilge Soran, Dhruv Choudhary, Raghuraman Krishnamoorthi, Vikas Chandra, Yuandong Tian, Tijmen Blankevoort

**Updated**: 2025-02-20T06:07:00Z

**Summary**: Post-training quantization (PTQ) techniques applied to weights, activations, and the KV cache greatly reduce memory usage, latency, and power consumption of Large Language Models (LLMs), but may lead to large quantization errors when outliers are present. Rotating activation or weight matrices helps remove outliers and benefits quantization. In this work, we identify a collection of applicable rotation parameterizations that lead to identical outputs in full-precision Transformer architectures while enhancing quantization accuracy. In addition, we find that some random rotations lead to much better quantization than others, with an up to 13 points difference in downstream zero-shot reasoning performance. As a result, we propose SpinQuant, a novel approach that incorporates learned rotation matrices for optimal quantized network accuracy. With 4-bit quantization of weight, activation, and KV-cache, SpinQuant narrows the accuracy gap on zero-shot reasoning tasks with full precision to merely 2.9 points on the LLaMA-2 7B model, surpassing LLM-QAT by 19.1 points and SmoothQuant by 25.0 points. Furthermore, SpinQuant also outperforms concurrent work QuaRot, which applies random rotations to remove outliers. In particular, for LLaMA-3 8B models that are hard to quantize, SpinQuant reduces the gap to full precision by up to 45.1% relative to QuaRot. Code is available at https://github.com/facebookresearch/SpinQuant.

**Link**: [arxiv](http://arxiv.org/abs/2405.16406v4),  [pdf](http://arxiv.org/pdf/2405.16406v4)

**Tags**: cs.LG cs.AI cs.CL cs.CV 



### EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts
**Authors**: Subhajit Chaudhury, Payel Das, Sarathkrishna Swaminathan, Georgios Kollias, Elliot Nelson, Khushbu Pahwa, Tejaswini Pedapati, Igor Melnyk, Matthew Riemer

**Updated**: 2025-02-20T05:41:15Z

**Summary**: Recent advances in Large Language Models (LLMs) have yielded impressive successes on many language tasks. However, efficient processing of long contexts using LLMs remains a significant challenge. We introduce \textbf{EpMAN} -- a method for processing long contexts in an \textit{episodic memory} module while \textit{holistically attending to} semantically relevant context chunks. The output of \textit{episodic attention} is then used to reweigh the decoder's self-attention to the stored KV cache of the context during training and generation. When an LLM decoder is trained using \textbf{EpMAN}, its performance on multiple challenging single-hop long-context recall and question-answering benchmarks is found to be stronger and more robust across the range from 16k to 256k tokens than baseline decoders trained with self-attention, and popular retrieval-augmented generation frameworks.

**Link**: [arxiv](http://arxiv.org/abs/2502.14280v1),  [pdf](http://arxiv.org/pdf/2502.14280v1)

**Tags**: cs.CL cs.AI 



### NDPage: Efficient Address Translation for Near-Data Processing   Architectures via Tailored Page Table
**Authors**: Qingcai Jiang, Buxin Tu, Hong An

**Updated**: 2025-02-20T03:27:00Z

**Summary**: Near-Data Processing (NDP) has been a promising architectural paradigm to address the memory wall problem for data-intensive applications. Practical implementation of NDP architectures calls for system support for better programmability, where having virtual memory (VM) is critical. Modern computing systems incorporate a 4-level page table design to support address translation in VM. However, simply adopting an existing 4-level page table in NDP systems causes significant address translation overhead because (1) NDP applications generate a lot of address translations, and (2) the limited L1 cache in NDP systems cannot cover the accesses to page table entries (PTEs). We extensively analyze the 4-level page table design in the NDP scenario and observe that (1) the memory access to page table entries is highly irregular, thus cannot benefit from the L1 cache, and (2) the last two levels of page tables are nearly fully occupied. Based on our observations, we propose NDPage, an efficient page table design tailored for NDP systems. The key mechanisms of NDPage are (1) an L1 cache bypass mechanism for PTEs that not only accelerates the memory accesses of PTEs but also prevents the pollution of PTEs in the cache system, and (2) a flattened page table design that merges the last two levels of page tables, allowing the page table to enjoy the flexibility of a 4KB page while reducing the number of PTE accesses. We evaluate NDPage using a variety of data-intensive workloads. Our evaluation shows that in a single-core NDP system, NDPage improves the end-to-end performance over the state-of-the-art address translation mechanism of 14.3\%; in 4-core and 8-core NDP systems, NDPage enhances the performance of 9.8\% and 30.5\%, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2502.14220v1),  [pdf](http://arxiv.org/pdf/2502.14220v1)

**Tags**: cs.AR 



### RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache   Compression
**Authors**: Payman Behnam, Yaosheng Fu, Ritchie Zhao, Po-An Tsai, Zhiding Yu, Alexey Tumanov

**Updated**: 2025-02-19T19:12:46Z

**Summary**: Transformer-based Large Language Models rely critically on KV cache to efficiently handle extended contexts during the decode phase. Yet, the size of the KV cache grows proportionally with the input length, burdening both memory bandwidth and capacity as decoding progresses. To address this challenge, we present RocketKV, a training-free KV cache compression strategy designed specifically to reduce both memory bandwidth and capacity demand of KV cache during the decode phase. RocketKV contains two consecutive stages. In the first stage, it performs coarse-grain KV cache eviction on the input sequence tokens with SnapKV++, a method improved upon SnapKV by introducing adaptive pooling size and full compatibility with grouped-query attention. In the second stage, it adopts a hybrid attention method to conduct fine-grain top-k sparse attention, approximating the attention scores by leveraging both head and sequence dimensional reductions. Combining these two stages, RocketKV achieves significant KV cache fetching bandwidth and storage savings while maintaining comparable accuracy to full KV cache attention. We show that RocketKV provides end-to-end speedup by up to 3$\times$ as well as peak memory reduction by up to 31% in the decode phase on an NVIDIA H100 GPU compared to the full KV cache baseline, while achieving negligible accuracy loss on a variety of long-context tasks.

**Link**: [arxiv](http://arxiv.org/abs/2502.14051v1),  [pdf](http://arxiv.org/pdf/2502.14051v1)

**Tags**: cs.CL cs.LG 



### Value Residual Learning
**Authors**: Zhanchao Zhou, Tianyi Wu, Zhiyun Jiang, Fares Obeid, Zhenzhong Lan

**Updated**: 2025-02-19T17:53:11Z

**Summary**: While Transformer models have achieved remarkable success in various domains, the effectiveness of information propagation through deep networks remains a critical challenge. Standard hidden state residuals often fail to adequately preserve initial token-level information in deeper layers. This paper introduces ResFormer, a novel architecture that enhances information flow by incorporating value residual connections in addition to hidden state residuals. And a variant is the SVFormer, where all layers share the first layer's value embedding. Comprehensive empirical evidence demonstrates ResFormer achieves equivalent validation loss with 13.3\% fewer model parameters and 15.4\% less training data compared to Transformer, while maintaining similar memory usage and computational cost. Besides, SVFormer reduces KV cache size by nearly half with only a small performance penalty and can be integrated with other KV-efficient methods, yielding further reductions in KV cache, with performance influenced by sequence length and cumulative learning rate.

**Link**: [arxiv](http://arxiv.org/abs/2410.17897v4),  [pdf](http://arxiv.org/pdf/2410.17897v4)

**Tags**: cs.CL 



### NVR: Vector Runahead on NPUs for Sparse Memory Access
**Authors**: Hui Wang, Zhengpeng Zhao, Jing Wang, Yushu Du, Yuan Cheng, Bing Guo, He Xiao, Chenhao Ma, Xiaomeng Han, Dean You, Jiapeng Guan, Ran Wei, Dawei Yang, Zhe Jiang

**Updated**: 2025-02-19T16:54:58Z

**Summary**: Deep Neural Networks are increasingly leveraging sparsity to reduce the scaling up of model parameter size. However, reducing wall-clock time through sparsity and pruning remains challenging due to irregular memory access patterns, leading to frequent cache misses. In this paper, we present NPU Vector Runahead (NVR), a prefetching mechanism tailored for NPUs to address cache miss problems in sparse DNN workloads. Rather than optimising memory patterns with high overhead and poor portability, NVR adapts runahead execution to the unique architecture of NPUs. NVR provides a general micro-architectural solution for sparse DNN workloads without requiring compiler or algorithmic support, operating as a decoupled, speculative, lightweight hardware sub-thread alongside the NPU, with minimal hardware overhead (under 5%). NVR achieves an average 90% reduction in cache misses compared to SOTA prefetching in general-purpose processors, delivering 4x average speedup on sparse workloads versus NPUs without prefetching. Moreover, we investigate the advantages of incorporating a small cache (16KB) into the NPU combined with NVR. Our evaluation shows that expanding this modest cache delivers 5x higher performance benefits than increasing the L2 cache size by the same amount.

**Link**: [arxiv](http://arxiv.org/abs/2502.13873v1),  [pdf](http://arxiv.org/pdf/2502.13873v1)

**Tags**: cs.AR cs.AI 



### The Impact of Inference Acceleration on Bias of LLMs
**Authors**: Elisabeth Kirsten, Ivan Habernal, Vedant Nanda, Muhammad Bilal Zafar

**Updated**: 2025-02-19T11:10:09Z

**Summary**: Last few years have seen unprecedented advances in capabilities of Large Language Models (LLMs). These advancements promise to benefit a vast array of application domains. However, due to their immense size, performing inference with LLMs is both costly and slow. Consequently, a plethora of recent work has proposed strategies to enhance inference efficiency, e.g., quantization, pruning, and caching. These acceleration strategies reduce the inference cost and latency, often by several factors, while maintaining much of the predictive performance measured via common benchmarks. In this work, we explore another critical aspect of LLM performance: demographic bias in model generations due to inference acceleration optimizations. Using a wide range of metrics, we probe bias in model outputs from a number of angles. Analysis of outputs before and after inference acceleration shows significant change in bias. Worryingly, these bias effects are complex and unpredictable. A combination of an acceleration strategy and bias type may show little bias change in one model but may lead to a large effect in another. Our results highlight a need for in-depth and case-by-case evaluation of model bias after it has been modified to accelerate inference.

**Link**: [arxiv](http://arxiv.org/abs/2410.22118v2),  [pdf](http://arxiv.org/pdf/2410.22118v2)

**Tags**: cs.CL cs.AI cs.LG 



### Accelerating Diffusion Transformers with Token-wise Feature Caching
**Authors**: Chang Zou, Xuyang Liu, Ting Liu, Siteng Huang, Linfeng Zhang

**Updated**: 2025-02-19T10:39:58Z

**Summary**: Diffusion transformers have shown significant effectiveness in both image and video synthesis at the expense of huge computation costs. To address this problem, feature caching methods have been introduced to accelerate diffusion transformers by caching the features in previous timesteps and reusing them in the following timesteps. However, previous caching methods ignore that different tokens exhibit different sensitivities to feature caching, and feature caching on some tokens may lead to 10$\times$ more destruction to the overall generation quality compared with other tokens. In this paper, we introduce token-wise feature caching, allowing us to adaptively select the most suitable tokens for caching, and further enable us to apply different caching ratios to neural layers in different types and depths. Extensive experiments on PixArt-$\alpha$, OpenSora, and DiT demonstrate our effectiveness in both image and video generation with no requirements for training. For instance, 2.36$\times$ and 1.93$\times$ acceleration are achieved on OpenSora and PixArt-$\alpha$ with almost no drop in generation quality.

**Link**: [arxiv](http://arxiv.org/abs/2410.05317v4),  [pdf](http://arxiv.org/pdf/2410.05317v4)

**Tags**: cs.LG cs.AI cs.CV 



### ETS: Efficient Tree Search for Inference-Time Scaling
**Authors**: Coleman Hooper, Sehoon Kim, Suhong Moon, Kerem Dilmen, Monishwaran Maheswaran, Nicholas Lee, Michael W. Mahoney, Sophia Shao, Kurt Keutzer, Amir Gholami

**Updated**: 2025-02-19T09:30:38Z

**Summary**: Test-time compute scaling has emerged as a new axis along which to improve model accuracy, where additional computation is used at inference time to allow the model to think longer for more challenging problems. One promising approach for test-time compute scaling is search against a process reward model, where a model generates multiple potential candidates at each step of the search, and these partial trajectories are then scored by a separate reward model in order to guide the search process. The diversity of trajectories in the tree search process affects the accuracy of the search, since increasing diversity promotes more exploration. However, this diversity comes at a cost, as divergent trajectories have less KV sharing, which means they consume more memory and slow down the search process. Previous search methods either do not perform sufficient exploration, or else explore diverse trajectories but have high latency. We address this challenge by proposing Efficient Tree Search (ETS), which promotes KV sharing by pruning redundant trajectories while maintaining necessary diverse trajectories. ETS incorporates a linear programming cost model to promote KV cache sharing by penalizing the number of nodes retained, while incorporating a semantic coverage term into the cost model to ensure that we retain trajectories which are semantically different. We demonstrate how ETS can achieve 1.8$\times$ reduction in average KV cache size during the search process, leading to 1.4$\times$ increased throughput relative to prior state-of-the-art methods, with minimal accuracy degradation and without requiring any custom kernel implementation. Code is available at: https://github.com/SqueezeAILab/ETS.

**Link**: [arxiv](http://arxiv.org/abs/2502.13575v1),  [pdf](http://arxiv.org/pdf/2502.13575v1)

**Tags**: cs.LG 



### Activation-aware Probe-Query: Effective Key-Value Retrieval for   Long-Context LLMs Inference
**Authors**: Qingfa Xiao, Jiachuan Wang, Haoyang Li, Cheng Deng, Jiaqi Tang, Shuangyin Li, Yongqi Zhang, Jun Wang, Lei Chen

**Updated**: 2025-02-19T08:50:44Z

**Summary**: Recent advances in large language models (LLMs) have showcased exceptional performance in long-context tasks, while facing significant inference efficiency challenges with limited GPU memory. Existing solutions first proposed the sliding-window approach to accumulate a set of historical \textbf{key-value} (KV) pairs for reuse, then further improvements selectively retain its subsets at each step. However, due to the sparse attention distribution across a long context, it is hard to identify and recall relevant KV pairs, as the attention is distracted by massive candidate pairs. Additionally, we found it promising to select representative tokens as probe-Query in each sliding window to effectively represent the entire context, which is an approach overlooked by existing methods. Thus, we propose \textbf{ActQKV}, a training-free, \textbf{Act}ivation-aware approach that dynamically determines probe-\textbf{Q}uery and leverages it to retrieve the relevant \textbf{KV} pairs for inference. Specifically, ActQKV monitors a token-level indicator, Activation Bias, within each context window, enabling the proper construction of probe-Query for retrieval at pre-filling stage. To accurately recall the relevant KV pairs and minimize the irrelevant ones, we design a dynamic KV cut-off mechanism guided by information density across layers at the decoding stage. Experiments on the Long-Bench and $\infty$ Benchmarks demonstrate its state-of-the-art performance with competitive inference quality and resource efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2502.13542v1),  [pdf](http://arxiv.org/pdf/2502.13542v1)

**Tags**: cs.CL cs.AI 



### FairKV: Balancing Per-Head KV Cache for Fast Multi-GPU Inference
**Authors**: Bingzhe Zhao, Ke Cheng, Aomufei Yuan, Yuxuan Tian, Ruiguang Zhong, Chengchen Hu, Tong Yang, Lian Yu

**Updated**: 2025-02-19T06:14:27Z

**Summary**: KV cache techniques in Transformer models aim to reduce redundant computations at the expense of substantially increased memory usage, making KV cache compression an important and popular research topic. Recently, state-of-the-art KV cache compression methods implement imbalanced, per-head allocation algorithms that dynamically adjust the KV cache budget for each attention head, achieving excellent performance in single-GPU scenarios. However, we observe that such imbalanced compression leads to significant load imbalance when deploying multi-GPU inference, as some GPUs become overburdened while others remain underutilized. In this paper, we propose FairKV, a method designed to ensure fair memory usage among attention heads in systems employing imbalanced KV cache compression. The core technique of FairKV is Fair-Copying, which replicates a small subset of memory-intensive attention heads across GPUs using data parallelism to mitigate load imbalance. Our experiments on popular models, including LLaMA 70b and Mistral 24b model, demonstrate that FairKV increases throughput by 1.66x compared to standard tensor parallelism inference. Our code will be released as open source upon acceptance.

**Link**: [arxiv](http://arxiv.org/abs/2502.15804v1),  [pdf](http://arxiv.org/pdf/2502.15804v1)

**Tags**: cs.DC cs.AI 



### Multimodal Mamba: Decoder-only Multimodal State Space Model via   Quadratic to Linear Distillation
**Authors**: Bencheng Liao, Hongyuan Tao, Qian Zhang, Tianheng Cheng, Yingyue Li, Haoran Yin, Wenyu Liu, Xinggang Wang

**Updated**: 2025-02-18T18:59:57Z

**Summary**: Recent Multimodal Large Language Models (MLLMs) have achieved remarkable performance but face deployment challenges due to their quadratic computational complexity, growing Key-Value cache requirements, and reliance on separate vision encoders. We propose mmMamba, a framework for developing linear-complexity native multimodal state space models through progressive distillation from existing MLLMs using moderate academic computational resources. Our approach enables the direct conversion of trained decoder-only MLLMs to linear-complexity architectures without requiring pre-trained RNN-based LLM or vision encoders. We propose an seeding strategy to carve Mamba from trained Transformer and a three-stage distillation recipe, which can effectively transfer the knowledge from Transformer to Mamba while preserving multimodal capabilities. Our method also supports flexible hybrid architectures that combine Transformer and Mamba layers for customizable efficiency-performance trade-offs. Distilled from the Transformer-based decoder-only HoVLE, mmMamba-linear achieves competitive performance against existing linear and quadratic-complexity VLMs, while mmMamba-hybrid further improves performance significantly, approaching HoVLE's capabilities. At 103K tokens, mmMamba-linear demonstrates 20.6$\times$ speedup and 75.8% GPU memory reduction compared to HoVLE, while mmMamba-hybrid achieves 13.5$\times$ speedup and 60.2% memory savings. Code and models are released at https://github.com/hustvl/mmMamba

**Link**: [arxiv](http://arxiv.org/abs/2502.13145v1),  [pdf](http://arxiv.org/pdf/2502.13145v1)

**Tags**: cs.CV 



### Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the   Limits of Embedding Space Capacity
**Authors**: Yuri Kuratov, Mikhail Arkhipov, Aydar Bulatov, Mikhail Burtsev

**Updated**: 2025-02-18T17:08:45Z

**Summary**: A range of recent works addresses the problem of compression of sequence of tokens into a shorter sequence of real-valued vectors to be used as inputs instead of token embeddings or key-value cache. These approaches allow to reduce the amount of compute in existing language models. Despite relying on powerful models as encoders, the maximum attainable lossless compression ratio is typically not higher than x10. This fact is highly intriguing because, in theory, the maximum information capacity of large real-valued vectors is far beyond the presented rates even for 16-bit precision and a modest vector size. In this work, we explore the limits of compression by replacing the encoder with a per-sample optimization procedure. We show that vectors with compression ratios up to x1500 exist, which highlights two orders of magnitude gap between existing and practically attainable solutions. Furthermore, we empirically show that the compression limits are determined not by the length of the input but by the amount of uncertainty to be reduced, namely, the cross-entropy loss on this sequence without any conditioning. The obtained limits highlight the substantial gap between the theoretical capacity of input embeddings and their practical utilization, suggesting significant room for optimization in model design.

**Link**: [arxiv](http://arxiv.org/abs/2502.13063v1),  [pdf](http://arxiv.org/pdf/2502.13063v1)

**Tags**: cs.CL cs.LG 



### A Survey on DRL based UAV Communications and Networking: DRL   Fundamentals, Applications and Implementations
**Authors**: Wei Zhao, Shaoxin Cui, Wen Qiu, Zhiqiang He, Zhi Liu, Xiao Zheng, Bomin Mao, Nei Kato

**Updated**: 2025-02-18T14:05:12Z

**Summary**: Unmanned aerial vehicles (UAVs) are playing an increasingly pivotal role in modern communication networks,offering flexibility and enhanced coverage for a variety of applica-tions. However, UAV networks pose significant challenges due to their dynamic and distributed nature, particularly when dealing with tasks such as power allocation, channel assignment, caching,and task offloading. Traditional optimization techniques often struggle to handle the complexity and unpredictability of these environments, leading to suboptimal performance. This survey provides a comprehensive examination of how deep reinforcement learning (DRL) can be applied to solve these mathematical optimization problems in UAV communications and networking.Rather than simply introducing DRL methods, the focus is on demonstrating how these methods can be utilized to solve complex mathematical models of the underlying problems. We begin by reviewing the fundamental concepts of DRL, including value-based, policy-based, and actor-critic approaches. Then,we illustrate how DRL algorithms are applied to specific UAV network tasks by discussing from problem formulations to DRL implementation. By framing UAV communication challenges as optimization problems, this survey emphasizes the practical value of DRL in dynamic and uncertain environments. We also explore the strengths of DRL in handling large-scale network scenarios and the ability to continuously adapt to changes in the environment. In addition, future research directions are outlined, highlighting the potential for DRL to further enhance UAV communications and expand its applicability to more complex,multi-agent settings.

**Link**: [arxiv](http://arxiv.org/abs/2502.12875v1),  [pdf](http://arxiv.org/pdf/2502.12875v1)

**Tags**: cs.NI 



### A$^2$ATS: Retrieval-Based KV Cache Reduction via Windowed Rotary   Position Embedding and Query-Aware Vector Quantization
**Authors**: Junhui He, Junna Xing, Nan Wang, Rui Xu, Shangyu Wu, Peng Zhou, Qiang Liu, Chun Jason Xue, Qingan Li

**Updated**: 2025-02-18T09:11:51Z

**Summary**: Long context large language models (LLMs) pose significant challenges for efficient serving due to the large memory footprint and high access overhead of KV cache. Retrieval-based KV cache reduction methods can mitigate these challenges, typically by offloading the complete KV cache to CPU and retrieving necessary tokens on demand during inference. However, these methods still suffer from unsatisfactory accuracy degradation and extra retrieval overhead. To address these limitations, this paper proposes A$^2$ATS, a novel retrieval-based KV cache reduction method. A$^2$ATS aims to obtain an accurate approximation of attention scores by applying the vector quantization technique to key states, thereby enabling efficient and precise retrieval of the top-K tokens. First, we propose Windowed Rotary Position Embedding, which decouples the positional dependency from query and key states after position embedding. Then, we propose query-aware vector quantization that optimizes the objective of attention score approximation directly. Finally, we design the heterogeneous inference architecture for KV cache offloading, enabling long context serving with larger batch sizes. Experimental results demonstrate that A$^2$ATS can achieve a lower performance degradation with similar or lower overhead compared to existing methods, thereby increasing long context serving throughput by up to $2.7 \times$.

**Link**: [arxiv](http://arxiv.org/abs/2502.12665v1),  [pdf](http://arxiv.org/pdf/2502.12665v1)

**Tags**: cs.CL 



### Value-based Proactive Caching for Sensing Data in Vehicular Networks: An   Operator's Perspective
**Authors**: Yantong Wang, Ke Liu, Hui Ji, Jiande Sun

**Updated**: 2025-02-18T07:58:29Z

**Summary**: Access to sensing data (SD) is crucial for vehicular networks to ensure safe and efficient transportation services. Given the vast volume of data involved, proactive caching required SD is a pivotal strategy for alleviating network congestion and improving data accessibility. Despite merits, existing studies predominantly address SD caching within a single slot. Therefore, these approaches lack scalability for scenarios involving multi-slots and are not well-suited for network operators who manage resources within a long-term cost budget. Moreover, the oversight of service capacity at caching nodes may result in substantial queuing delays for SD reception. To tackle these limitations, we jointly consider the problem of anchoring SD caching and allocating from an operator's perspective. A value model incorporating both temporal and spacial characteristics is given to estimate the significance of various caching decisions. Subsequently, a stochastic programming model is proposed to optimize the long-term system performance, which is converted into a series of online optimization problem by leveraging the Lyapunov method and linearized via introducing auxiliary variables. To expedite the solution, we provide a binary quantum particle swarm optimization based algorithm with quadratic time complexity. Numerical investigations demonstrate the superiority of proposed algorithms compared with other schemes in terms of energy consumption, response latency, and cache-hit ratio.

**Link**: [arxiv](http://arxiv.org/abs/2408.05996v2),  [pdf](http://arxiv.org/pdf/2408.05996v2)

**Tags**: cs.NI 



### HeadInfer: Memory-Efficient LLM Inference by Head-wise Offloading
**Authors**: Cheng Luo, Zefan Cai, Hanshi Sun, Jinqi Xiao, Bo Yuan, Wen Xiao, Junjie Hu, Jiawei Zhao, Beidi Chen, Anima Anandkumar

**Updated**: 2025-02-18T06:26:05Z

**Summary**: Transformer-based large language models (LLMs) demonstrate impressive performance in long context generation. Extending the context length has disproportionately shifted the memory footprint of LLMs during inference to the key-value cache (KV cache). In this paper, we propose HEADINFER, which offloads the KV cache to CPU RAM while avoiding the need to fully store the KV cache for any transformer layer on the GPU. HEADINFER employs a fine-grained, head-wise offloading strategy, maintaining only selective attention heads KV cache on the GPU while computing attention output dynamically. Through roofline analysis, we demonstrate that HEADINFER maintains computational efficiency while significantly reducing memory footprint. We evaluate HEADINFER on the Llama-3-8B model with a 1-million-token sequence, reducing the GPU memory footprint of the KV cache from 128 GB to 1 GB and the total GPU memory usage from 207 GB to 17 GB, achieving a 92% reduction compared to BF16 baseline inference. Notably, HEADINFER enables 4-million-token inference with an 8B model on a single consumer GPU with 24GB memory (e.g., NVIDIA RTX 4090) without approximation methods.

**Link**: [arxiv](http://arxiv.org/abs/2502.12574v1),  [pdf](http://arxiv.org/pdf/2502.12574v1)

**Tags**: cs.LG cs.AI 



### Accurate Expert Predictions in MoE Inference via Cross-Layer Gate
**Authors**: Zhiyuan Fang, Zicong Hong, Yuegui Huang, Yufeng Lyu, Wuhui Chen, Yue Yu, Fan Yu, Zibin Zheng

**Updated**: 2025-02-17T14:54:14Z

**Summary**: Large Language Models (LLMs) have demonstrated impressive performance across various tasks, and their application in edge scenarios has attracted significant attention. However, sparse-activated Mixture-of-Experts (MoE) models, which are well suited for edge scenarios, have received relatively little attention due to their high memory demands. Offload-based methods have been proposed to address this challenge, but they face difficulties with expert prediction. Inaccurate expert predictions can result in prolonged inference delays. To promote the application of MoE models in edge scenarios, we propose Fate, an offloading system designed for MoE models to enable efficient inference in resource-constrained environments. The key insight behind Fate is that gate inputs from adjacent layers can be effectively used for expert prefetching, achieving high prediction accuracy without additional GPU overhead. Furthermore, Fate employs a shallow-favoring expert caching strategy that increases the expert hit rate to 99\%. Additionally, Fate integrates tailored quantization strategies for cache optimization and IO efficiency. Experimental results show that, compared to Load on Demand and Expert Activation Path-based method, Fate achieves up to 4.5x and 1.9x speedups in prefill speed and up to 4.1x and 2.2x speedups in decoding speed, respectively, while maintaining inference quality. Moreover, Fate's performance improvements are scalable across different memory budgets.

**Link**: [arxiv](http://arxiv.org/abs/2502.12224v1),  [pdf](http://arxiv.org/pdf/2502.12224v1)

**Tags**: cs.AI cs.LG 



### DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context   LLMs
**Authors**: Xiabin Zhou, Wenbin Wang, Minyan Zeng, Jiaxian Guo, Xuebo Liu, Li Shen, Min Zhang, Liang Ding

**Updated**: 2025-02-17T14:34:58Z

**Summary**: Efficient KV cache management in LLMs is crucial for long-context tasks like RAG and summarization. Existing KV cache compression methods enforce a fixed pattern, neglecting task-specific characteristics and reducing the retention of essential information. However, we observe distinct activation patterns across layers in various tasks, highlighting the need for adaptive strategies tailored to each task's unique demands. Based on this insight, we propose DynamicKV, a method that dynamically optimizes token retention by adjusting the number of tokens retained at each layer to adapt to the specific task. DynamicKV establishes global and per-layer maximum KV cache budgets, temporarily retaining the maximum budget for the current layer, and periodically updating the KV cache sizes of all preceding layers during inference. Our method retains only 1.7% of the KV cache size while achieving ~85% of the Full KV cache performance on LongBench. Notably, even under extreme compression (0.9%), DynamicKV surpasses state-of-the-art (SOTA) methods by 11% in the Needle-in-a-Haystack test using Mistral-7B-Instruct-v0.2. The code will be released.

**Link**: [arxiv](http://arxiv.org/abs/2412.14838v2),  [pdf](http://arxiv.org/pdf/2412.14838v2)

**Tags**: cs.CL 



### Tactic: Adaptive Sparse Attention with Clustering and Distribution   Fitting for Long-Context LLMs
**Authors**: Kan Zhu, Tian Tang, Qinyu Xu, Yile Gu, Zhichen Zeng, Rohan Kadekodi, Liangyu Zhao, Ang Li, Arvind Krishnamurthy, Baris Kasikci

**Updated**: 2025-02-17T08:39:43Z

**Summary**: Long-context models are essential for many applications but face inefficiencies in loading large KV caches during decoding. Prior methods enforce fixed token budgets for sparse attention, assuming a set number of tokens can approximate full attention. However, these methods overlook variations in the importance of attention across heads, layers, and contexts. To address these limitations, we propose Tactic, a sparsity-adaptive and calibration-free sparse attention mechanism that dynamically selects tokens based on their cumulative attention scores rather than a fixed token budget. By setting a target fraction of total attention scores, Tactic ensures that token selection naturally adapts to variations in attention sparsity. To efficiently approximate this selection, Tactic leverages clustering-based sorting and distribution fitting, allowing it to accurately estimate token importance with minimal computational overhead. We show that Tactic outperforms existing sparse attention algorithms, achieving superior accuracy and up to 7.29x decode attention speedup. This improvement translates to an overall 1.58x end-to-end inference speedup, making Tactic a practical and effective solution for long-context LLM inference in accuracy-sensitive applications.

**Link**: [arxiv](http://arxiv.org/abs/2502.12216v1),  [pdf](http://arxiv.org/pdf/2502.12216v1)

**Tags**: cs.LG cs.AI cs.CL 



### Rotate, Clip, and Partition: Towards W2A4KV4 Quantization by Integrating   Rotation and Learnable Non-uniform Quantizer
**Authors**: Euntae Choi, Sumin Song, Woosang Lim, Sungjoo Yoo

**Updated**: 2025-02-17T08:12:34Z

**Summary**: We propose Rotate, Clip, and Partition (RCP), a quantization-aware training (QAT) approach that first realizes extreme compression of LLMs with W2A4KV4(2-bit weight, 4-bit activation, and 4-bit KV cache) configuration. RCP integrates recent rotation techniques with a novel non-uniform weight quantizer design, by quantitatively analyzing the impact of random rotation on 2-bit weight quantization. Our weight quantizer features Learnable Direct Partitioning (LDP), which introduces learnable parameters to directly learn non-uniform intervals jointly with LLM weights. We also present a specialized GPU kernel that supports GEMV on non-uniform W2A4. Experiments show that RCP can compress LLaMA-2-7B to W2A4KV4 with a loss of only 2.84 WikiText2 ppl and 5.29 times reduced memory footprint. Furthermore, RCP can quantize challenging mobile-targeted LLaMA-3.2 models and domain-specific WizardCoder-7B and MetaMath-7B with no critical problems such as convergence failure and repetition. Code will be made available at blind_review.

**Link**: [arxiv](http://arxiv.org/abs/2502.15779v1),  [pdf](http://arxiv.org/pdf/2502.15779v1)

**Tags**: cs.LG cs.AI cs.CL 



### Token Pruning in Multimodal Large Language Models: Are We Solving the   Right Problem?
**Authors**: Zichen Wen, Yifeng Gao, Weijia Li, Conghui He, Linfeng Zhang

**Updated**: 2025-02-17T07:05:36Z

**Summary**: Multimodal large language models (MLLMs) have shown remarkable performance for cross-modal understanding and generation, yet still suffer from severe inference costs. Recently, abundant works have been proposed to solve this problem with token pruning, which identifies the redundant tokens in MLLMs and then prunes them to reduce the computation and KV storage costs, leading to significant acceleration without training. While these methods claim efficiency gains, critical questions about their fundamental design and evaluation remain unanswered: Why do many existing approaches underperform even compared to naive random token selection? Are attention-based scoring sufficient for reliably identifying redundant tokens? Is language information really helpful during token pruning? What makes a good trade-off between token importance and duplication? Are current evaluation protocols comprehensive and unbiased? The ignorance of previous research on these problems hinders the long-term development of token pruning. In this paper, we answer these questions one by one, providing insights into the design of future token pruning methods.

**Link**: [arxiv](http://arxiv.org/abs/2502.11501v1),  [pdf](http://arxiv.org/pdf/2502.11501v1)

**Tags**: cs.CL cs.CV 



### Does RAG Really Perform Bad For Long-Context Processing?
**Authors**: Kun Luo, Zheng Liu, Peitian Zhang, Hongjin Qian, Jun Zhao, Kang Liu

**Updated**: 2025-02-17T05:02:25Z

**Summary**: The efficient processing of long context poses a serious challenge for large language models (LLMs). Recently, retrieval-augmented generation (RAG) has emerged as a promising strategy for this problem, as it enables LLMs to make selective use of the long context for efficient computation. However, existing RAG approaches lag behind other long-context processing methods due to inherent limitations on inaccurate retrieval and fragmented contexts. To address these challenges, we introduce RetroLM, a novel RAG framework for long-context processing. Unlike traditional methods, RetroLM employs KV-level retrieval augmentation, where it partitions the LLM's KV cache into contiguous pages and retrieves the most crucial ones for efficient computation. This approach enhances robustness to retrieval inaccuracy, facilitates effective utilization of fragmented contexts, and saves the cost from repeated computation. Building on this framework, we further develop a specialized retriever for precise retrieval of critical pages and conduct unsupervised post-training to optimize the model's ability to leverage retrieved information. We conduct comprehensive evaluations with a variety of benchmarks, including LongBench, InfiniteBench, and RULER, where RetroLM significantly outperforms existing long-context LLMs and efficient long-context processing methods, particularly in tasks requiring intensive reasoning or extremely long-context comprehension.

**Link**: [arxiv](http://arxiv.org/abs/2502.11444v1),  [pdf](http://arxiv.org/pdf/2502.11444v1)

**Tags**: cs.CL 



### Capitalizing on a Crisis: A Computational Analysis of all Five Million   British Firms During the Covid-19 Pandemic
**Authors**: Naomi Muggleton, Charles Rahal, Aaron Reeves

**Updated**: 2025-02-16T18:31:10Z

**Summary**: The Covid-19 pandemic brought unprecedented changes to business ownership in the UK which affects a generation of entrepreneurs and their employees. Nonetheless, the impact remains poorly understood. This is because research on capital accumulation has typically lacked high-quality, individualized, population-level data. We overcome these barriers to examine who benefits from economic crises through a computationally orientated lens of firm creation. Leveraging a comprehensive cache of administrative data on every UK firm and all nine million people running them, combined with probabilistic algorithms, we conduct individual-level analyses to understand who became Covid entrepreneurs. Using these techniques, we explore characteristics of entrepreneurs--such as age, gender, region, business experience, and industry--which potentially predict Covid entrepreneurship. By employing an automated time series model selection procedure to generate counterfactuals, we show that Covid entrepreneurs were typically aged 35-49 (40.4%), men (73.1%), and had previously held roles in existing firms (59.4%). For most industries, growth was disproportionately concentrated around London. It was therefore existing corporate elites who were most able to capitalize on the Covid crisis and not, as some hypothesized, young entrepreneurs who were setting up their first businesses. In this respect, the pandemic will likely impact future wealth inequalities. Our work offers methodological guidance for future policymakers during economic crises and highlights the long-term consequences for capital and wealth inequality.

**Link**: [arxiv](http://arxiv.org/abs/2502.09383v2),  [pdf](http://arxiv.org/pdf/2502.09383v2)

**Tags**: econ.GN q-fin.EC 



### Leveraging Previous Steps: A Training-free Fast Solver for Flow   Diffusion
**Authors**: Kaiyu Song, Hanjiang Lai

**Updated**: 2025-02-16T16:41:43Z

**Summary**: Flow diffusion models (FDMs) have recently shown potential in generation tasks due to the high generation quality. However, the current ordinary differential equation (ODE) solver for FDMs, e.g., the Euler solver, still suffers from slow generation since ODE solvers need many number function evaluations (NFE) to keep high-quality generation. In this paper, we propose a novel training-free flow-solver to reduce NFE while maintaining high-quality generation. The key insight for the flow-solver is to leverage the previous steps to reduce the NFE, where a cache is created to reuse these results from the previous steps. Specifically, the Taylor expansion is first used to approximate the ODE. To calculate the high-order derivatives of Taylor expansion, the flow-solver proposes to use the previous steps and a polynomial interpolation to approximate it, where the number of orders we could approximate equals the number of previous steps we cached. We also prove that the flow-solver has a more minor approximation error and faster generation speed. Experimental results on the CIFAR-10, CelebA-HQ, LSUN-Bedroom, LSUN-Church, ImageNet, and real text-to-image generation prove the efficiency of the flow-solver. Specifically, the flow-solver improves the FID-30K from 13.79 to 6.75, from 46.64 to 19.49 with $\text{NFE}=10$ on CIFAR-10 and LSUN-Church, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2411.07627v2),  [pdf](http://arxiv.org/pdf/2411.07627v2)

**Tags**: cs.CV 



### EPIC: Efficient Position-Independent Context Caching for Serving Large   Language Models
**Authors**: Junhao Hu, Wenrui Huang, Haoyi Wang, Weidong Wang, Tiancheng Hu, Qin Zhang, Hao Feng, Xusheng Chen, Yizhou Shan, Tao Xie

**Updated**: 2025-02-16T14:50:00Z

**Summary**: Large Language Models (LLMs) are critical for a wide range of applications, but serving them efficiently becomes increasingly challenging as inputs become more complex. Context caching improves serving performance by exploiting inter-request dependency and reusing key-value (KV) cache across requests, thus improving time-to-first-token (TTFT). However, existing prefix-based context caching requires exact token prefix matches, limiting cache reuse in few-shot learning, multi-document QA, or retrieval-augmented generation, where prefixes may vary. In this paper, we present EPIC, an LLM serving system that introduces position-independent context caching (PIC), enabling modular KV cache reuse regardless of token chunk position (or prefix). EPIC features two key designs: AttnLink, which leverages static attention sparsity to minimize recomputation for accuracy recovery, and KVSplit, a customizable chunking method that preserves semantic coherence. Our experiments demonstrate that Epic delivers up to 8x improvements in TTFT and 7x throughput over existing systems, with negligible or no accuracy loss. By addressing the limitations of traditional caching approaches, Epic enables more scalable and efficient LLM inference.

**Link**: [arxiv](http://arxiv.org/abs/2410.15332v2),  [pdf](http://arxiv.org/pdf/2410.15332v2)

**Tags**: cs.LG cs.CL cs.DC cs.PF 



### Efficient Long-Decoding Inference with Reasoning-Aware Attention   Sparsity
**Authors**: Junhao Hu, Wenrui Huang, Weidong Wang, Zhenwen Li, Tiancheng Hu, Zhixia Liu, Xusheng Chen, Tao Xie, Yizhou Shan

**Updated**: 2025-02-16T14:28:52Z

**Summary**: Large Language Models (LLMs) have demonstrated strong capabilities across various domains, with recent advancements in challenging reasoning tasks such as mathematics and programming. However, solving reasoning tasks often requires long decoding chains (of thoughts), which incur $O(N)$ time and memory consumption, where $N$ is the chain length. To mitigate $O(N)$ time and memory consumption, existing sparsity-based algorithms propose retaining only the most critical token's intermediate data (i.e., key-value cache) and discarding the rest. However, these existing algorithms struggle with the ``impossible trinity'' of accuracy, time, and memory. For example, the state-of-the-art algorithm, Quest, achieves high accuracy with $O(L)$ time but $O(N)$ memory ($L$ is the cache budget, $L \ll N$). To address this issue, in this paper, we identify a new attention pattern during the decode stage of reasoning tasks, where milestone tokens (analogous to lemmas in mathematical proofs) emerge, are utilized, and then become unimportant afterward. Based on this pattern, we propose a new algorithm named RaaS that identifies and retains milestone tokens only until they are no longer needed, achieving high accuracy with $O(L)$ time and $O(L)$ memory complexity.

**Link**: [arxiv](http://arxiv.org/abs/2502.11147v1),  [pdf](http://arxiv.org/pdf/2502.11147v1)

**Tags**: cs.LG cs.AI 



### CacheFocus: Dynamic Cache Re-Positioning for Efficient   Retrieval-Augmented Generation
**Authors**: Kun-Hui Lee, Eunhwan Park, Donghoon Han, Seung-Hoon Na

**Updated**: 2025-02-16T12:33:16Z

**Summary**: Large Language Models (LLMs) excel across a variety of language tasks yet are constrained by limited input lengths and high computational costs. Existing approaches\textemdash such as relative positional encodings (e.g., RoPE, ALiBi) and sliding window mechanisms\textemdash partially alleviate these issues but often require additional training or suffer from performance degradation with longer inputs. In this paper, we introduce \textbf{\textit{CacheFocus}}, a method that enhances length normalization and reduces inference latency without any further training. Our approach leverages query-independent, offline caching to efficiently reuse a Context KV Cache Store. We address the amplification of abnormal token distributions problem by re-positioning cached keys and introducing Layer-Adaptive Cache Pruning to discard low-relevance caches during pre-filling. Additionally, our Adaptive Positional Allocation Strategy dynamically reassigns cache positions to maximize the use of the available positional encoding range. Experiments on the Natural Questions and TriviaQA datasets demonstrate that CacheFocus outperforms alternative methods even when inputs exceed the $4$K limit of the \texttt{LLaMA-2} model, emphasizing its practical effectiveness for long-context LLMs. Moreover, even with large maximum input length of \texttt{Qwen2}, the performance of CacheFocus shows that it maintains consistent performance even as the number of documents increases, effectively managing long-text generation without degradation.

**Link**: [arxiv](http://arxiv.org/abs/2502.11101v1),  [pdf](http://arxiv.org/pdf/2502.11101v1)

**Tags**: cs.CL cs.AI 



### Streamlining the Collaborative Chain of Models into A Single Forward   Pass in Generation-Based Tasks
**Authors**: Yuanjie Lyu, Chao Zhang, Yuhao Chen, Yong Chen, Tong Xu

**Updated**: 2025-02-16T11:37:14Z

**Summary**: In Retrieval-Augmented Generation (RAG) and agent-based frameworks, the "Chain of Models" approach is widely used, where multiple specialized models work sequentially on distinct sub-tasks. This approach is effective but increases resource demands as each model must be deployed separately. Recent advancements attempt to address this by applying prompt tuning, which allows a shared base model to adapt to multiple tasks with minimal parameter changes. However, a key challenge remains: intermediate outputs, passed between models as plain text, require recomputation of hidden states (i.e., Key and Value (KV) states in Transformers) during inference. In this paper, we introduce FTHSS, a novel prompt-tuning method that enables models to share KV hidden states, eliminating redundant forward passes and reducing KV cache storage. By modifying input and attention masks during training, FTHSS allows models to effectively utilize KV hidden states from prior models in both single- and multi-round scenarios. Empirical results on four tasks show that FTHSS matches the performance of traditional model chains while improving inference efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2502.11083v1),  [pdf](http://arxiv.org/pdf/2502.11083v1)

**Tags**: cs.CL 



### Enabling Efficient Transaction Processing on CXL-Based Memory Sharing
**Authors**: Zhao Wang, Yiqi Chen, Cong Li, Dimin Niu, Tianchan Guan, Zhaoyang Du, Xingda Wei, Guangyu Sun

**Updated**: 2025-02-16T09:08:36Z

**Summary**: Transaction processing systems are the crux for modern data-center applications, yet current multi-node systems are slow due to network overheads. This paper advocates for Compute Express Link (CXL) as a network alternative, which enables low-latency and cache-coherent shared memory accesses. However, directly adopting standard CXL primitives leads to performance degradation due to the high cost of maintaining cross-node cache coherence. To address the CXL challenges, this paper introduces CtXnL, a software-hardware co-designed system that implements a novel hybrid coherence primitive tailored to the loosely coherent nature of transactional data. The core innovation of CtXnL is empowering transaction system developers with the ability to selectively achieve data coherence. Our evaluations on OLTP workloads demonstrate that CtXnL enhances performance, outperforming current network-based systems and achieves with up to 2.08x greater throughput than vanilla CXL memory sharing architectures across universal transaction processing policies.

**Link**: [arxiv](http://arxiv.org/abs/2502.11046v1),  [pdf](http://arxiv.org/pdf/2502.11046v1)

**Tags**: cs.AR 



### DiskGNN: Bridging I/O Efficiency and Model Accuracy for Out-of-Core GNN   Training
**Authors**: Renjie Liu, Yichuan Wang, Xiao Yan, Haitian Jiang, Zhenkun Cai, Minjie Wang, Bo Tang, Jinyang Li

**Updated**: 2025-02-15T23:54:38Z

**Summary**: Graph neural networks (GNNs) are machine learning models specialized for graph data and widely used in many applications. To train GNNs on large graphs that exceed CPU memory, several systems store data on disk and conduct out-of-core processing. However, these systems suffer from either read amplification when reading node features that are usually smaller than a disk page or degraded model accuracy by treating the graph as disconnected partitions. To close this gap, we build a system called DiskGNN, which achieves high I/O efficiency and thus fast training without hurting model accuracy. The key technique used by DiskGNN is offline sampling, which helps decouple graph sampling from model computation. In particular, by conducting graph sampling beforehand, DiskGNN acquires the node features that will be accessed by model computation, and such information is utilized to pack the target node features contiguously on disk to avoid read amplification. Besides, \name{} also adopts designs including four-level feature store to fully utilize the memory hierarchy to cache node features and reduce disk access, batched packing to accelerate the feature packing process, and pipelined training to overlap disk access with other operations. We compare DiskGNN with Ginex and MariusGNN, which are state-of-the-art systems for out-of-core GNN training. The results show that DiskGNN can speed up the baselines by over 8x while matching their best model accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2405.05231v2),  [pdf](http://arxiv.org/pdf/2405.05231v2)

**Tags**: cs.LG 



### Speeding up Policy Simulation in Supply Chain RL
**Authors**: Vivek Farias, Joren Gijsbrechts, Aryan Khojandi, Tianyi Peng, Andrew Zheng

**Updated**: 2025-02-15T18:09:50Z

**Summary**: Simulating a single trajectory of a dynamical system under some state-dependent policy is a core bottleneck in policy optimization (PO) algorithms. The many inherently serial policy evaluations that must be performed in a single simulation constitute the bulk of this bottleneck. In applying PO to supply chain optimization (SCO) problems, simulating a single sample path corresponding to one month of a supply chain can take several hours. We present an iterative algorithm to accelerate policy simulation, dubbed Picard Iteration. This scheme carefully assigns policy evaluation tasks to independent processes. Within an iteration, any given process evaluates the policy only on its assigned tasks while assuming a certain "cached" evaluation for other tasks; the cache is updated at the end of the iteration. Implemented on GPUs, this scheme admits batched evaluation of the policy across a single trajectory. We prove that the structure afforded by many SCO problems allows convergence in a small number of iterations independent of the horizon. We demonstrate practical speedups of 400x on large-scale SCO problems even with a single GPU, and also demonstrate practical efficacy in other RL environments.

**Link**: [arxiv](http://arxiv.org/abs/2406.01939v2),  [pdf](http://arxiv.org/pdf/2406.01939v2)

**Tags**: cs.AI cs.DC cs.LG 



### From 16-Bit to 1-Bit: Visual KV Cache Quantization for Memory-Efficient   Multimodal Large Language Models
**Authors**: Zeliang Zhang, Yifan Zhu, Susan Liang, Zhiyuan Wang, Jiani Liu, Haiting Lin, Mingjie Zhao, Chenliang Xu, Kun Wan, Wentian Zhao

**Updated**: 2025-02-15T05:08:01Z

**Summary**: Multimodal Large Language Models (MLLMs) have achieved remarkable success across various applications, yet their computational overhead during deployment remains a critical challenge. While Key-Value (KV) caching improves inference efficiency by trading memory for computation, the growing memory footprint from storing extensive KV caches reduces throughput and limits long-term execution on devices with constrained GPU memory. Existing approaches primarily focus on dropping unimportant tokens to reduce the KV cache size, mitigating memory constraints at the cost of potential information loss. In contrast, we propose a simple yet effective visual quantization strategy that preserves all visual tokens while significantly reducing memory consumption. To achieve an extreme quantization ratio, i.e., 1-bit quantization, we propose group-specific quantization and quantile-based quantization approaches, motivated by the inherent patterns of the KV cache. Our method is plug-and-play, enabling seamless integration into various MLLMs to improve memory efficiency without architectural modifications. Extensive experiments demonstrate that our approach effectively reduces memory overhead while maintaining computational efficiency and preserving multimodal performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.14882v1),  [pdf](http://arxiv.org/pdf/2502.14882v1)

**Tags**: cs.CV 



### Pushing up to the Limit of Memory Bandwidth and Capacity Utilization for   Efficient LLM Decoding on Embedded FPGA
**Authors**: Jindong Li, Tenglong Li, Guobin Shen, Dongcheng Zhao, Qian Zhang, Yi Zeng

**Updated**: 2025-02-15T03:56:22Z

**Summary**: The extremely high computational and storage demands of large language models have excluded most edge devices, which were widely used for efficient machine learning, from being viable options. A typical edge device usually only has 4GB of memory capacity and a bandwidth of less than 20GB/s, while a large language model quantized to 4-bit precision with 7B parameters already requires 3.5GB of capacity, and its decoding process is purely bandwidth-bound. In this paper, we aim to explore these limits by proposing a hardware accelerator for large language model (LLM) inference on the Zynq-based KV260 platform, equipped with 4GB of 64-bit 2400Mbps DDR4 memory. We successfully deploy a LLaMA2-7B model, achieving a decoding speed of around 5 token/s, utilizing 93.3% of the memory capacity and reaching 85% decoding speed of the theoretical memory bandwidth limit. To fully reserve the memory capacity for model weights and key-value cache, we develop the system in a bare-metal environment without an operating system. To fully reserve the bandwidth for model weight transfers, we implement a customized dataflow with an operator fusion pipeline and propose a data arrangement format that can maximize the data transaction efficiency. This research marks the first attempt to deploy a 7B level LLM on a standalone embedded field programmable gate array (FPGA) device. It provides key insights into efficient LLM inference on embedded FPGA devices and provides guidelines for future architecture design.

**Link**: [arxiv](http://arxiv.org/abs/2502.10659v1),  [pdf](http://arxiv.org/pdf/2502.10659v1)

**Tags**: cs.AR 



### Region-Adaptive Sampling for Diffusion Transformers
**Authors**: Ziming Liu, Yifan Yang, Chengruidong Zhang, Yiqi Zhang, Lili Qiu, Yang You, Yuqing Yang

**Updated**: 2025-02-14T18:59:36Z

**Summary**: Diffusion models (DMs) have become the leading choice for generative tasks across diverse domains. However, their reliance on multiple sequential forward passes significantly limits real-time performance. Previous acceleration methods have primarily focused on reducing the number of sampling steps or reusing intermediate results, failing to leverage variations across spatial regions within the image due to the constraints of convolutional U-Net structures. By harnessing the flexibility of Diffusion Transformers (DiTs) in handling variable number of tokens, we introduce RAS, a novel, training-free sampling strategy that dynamically assigns different sampling ratios to regions within an image based on the focus of the DiT model. Our key observation is that during each sampling step, the model concentrates on semantically meaningful regions, and these areas of focus exhibit strong continuity across consecutive steps. Leveraging this insight, RAS updates only the regions currently in focus, while other regions are updated using cached noise from the previous step. The model's focus is determined based on the output from the preceding step, capitalizing on the temporal consistency we observed. We evaluate RAS on Stable Diffusion 3 and Lumina-Next-T2I, achieving speedups up to 2.36x and 2.51x, respectively, with minimal degradation in generation quality. Additionally, a user study reveals that RAS delivers comparable qualities under human evaluation while achieving a 1.6x speedup. Our approach makes a significant step towards more efficient diffusion transformers, enhancing their potential for real-time applications.

**Link**: [arxiv](http://arxiv.org/abs/2502.10389v1),  [pdf](http://arxiv.org/pdf/2502.10389v1)

**Tags**: cs.CV cs.AI 



### PhishIntel: Toward Practical Deployment of Reference-Based Phishing   Detection
**Authors**: Yuexin Li, Hiok Kuek Tan, Qiaoran Meng, Mei Lin Lock, Tri Cao, Shumin Deng, Nay Oo, Hoon Wei Lim, Bryan Hooi

**Updated**: 2025-02-14T17:17:20Z

**Summary**: Phishing is a critical cyber threat, exploiting deceptive tactics to compromise victims and cause significant financial losses. While reference-based phishing detectors (RBPDs) have achieved notable advancements in detection accuracy, their real-world deployment is hindered by challenges such as high latency and inefficiency in URL analysis. To address these limitations, we present PhishIntel, an end-to-end phishing detection system for real-world deployment. PhishIntel intelligently determines whether a URL can be processed immediately or not, segmenting the detection process into two distinct tasks: a fast task that checks against local blacklists and result cache, and a slow task that conducts online blacklist verification, URL crawling, and webpage analysis using an RBPD. This fast-slow task system architecture ensures low response latency while retaining the robust detection capabilities of RBPDs for zero-day phishing threats. Furthermore, we develop two downstream applications based on PhishIntel: a phishing intelligence platform and a phishing email detection plugin for Microsoft Outlook, demonstrating its practical efficacy and utility.

**Link**: [arxiv](http://arxiv.org/abs/2412.09057v2),  [pdf](http://arxiv.org/pdf/2412.09057v2)

**Tags**: cs.CR 



### Optimal and Coordinated Voltage Control: Case Study on a 132 kV   Norwegian Grid Subsystem
**Authors**: Hugo Rodrigues de Brito, Daniel Simon Baltensperger, Kjetil Obstfelder Uhlen

**Updated**: 2025-02-14T15:14:53Z

**Summary**: This work presents a framework for dynamic performance assessment of the higher layers in the hierarchical voltage regulation scheme, with case studies applied to specific areas of the Norwegian grid. Unlike the primary (PVR) level, the secondary (SVR) and tertiary (TVR) levels are not tuned to a single device at a time, handling instead several reactive power resources available within a control zone including generator units, static VAr compensators and others. Proper SVR-TVR coordination for realistic transmission systems is a challenging topic at the core of many ongoing discussions in voltage control literature. Special focus is placed on practical considerations from the system operator perspective, since this research is also aimed at simplifying daily control centre routines. Dynamic simulation results concern a 21-bus equivalent of a 132 kV network model that accurately represents a Norwegian grid subsystem. Case studies address daily grid operation with real-life load demand and wind power generation profiles, showing that the proposed strategy is effective not only to minimize total active power losses as much as possible within system-wide limitations, but also to maintain adequate voltage profiles and reactive power flows. Findings pertaining to this work showcase the benefits of applying hierarchical voltage regulation layers as an asset to day-to-day control center management of a realistic transmission network.

**Link**: [arxiv](http://arxiv.org/abs/2502.10220v1),  [pdf](http://arxiv.org/pdf/2502.10220v1)

**Tags**: eess.SY cs.SY 



### Modeling and Simulating Emerging Memory Technologies: A Tutorial
**Authors**: Yun-Chih Chen, Tristan Seidl, Nils Hölscher, Christian Hakert, Minh Duy Truong, Jian-Jia Chen, João Paulo C. de Lima, Asif Ali Khan, Jeronimo Castrillon, Ali Nezhadi, Lokesh Siddhu, Hassan Nassar, Mahta Mayahinia, Mehdi Baradaran Tahoori, Jörg Henkel, Nils Wilbert, Stefan Wildermann, Jürgen Teich

**Updated**: 2025-02-14T13:55:01Z

**Summary**: Non-volatile Memory (NVM) technologies present a promising alternative to traditional volatile memories such as SRAM and DRAM. Due to the limited availability of real NVM devices, simulators play a crucial role in architectural exploration and hardware-software co-design. This tutorial presents a simulation toolchain through four detailed case studies, showcasing its applicability to various domains of system design, including hybrid main-memory and cache, compute-in-memory, and wear-leveling design. These case studies provide the reader with practical insights on customizing the toolchain for their specific research needs. The source code is open-sourced.

**Link**: [arxiv](http://arxiv.org/abs/2502.10167v1),  [pdf](http://arxiv.org/pdf/2502.10167v1)

**Tags**: cs.AR 



## Keyword: LLM Inference 
 ### Matryoshka Quantization
**Authors**: Pranav Nair, Puranjay Datta, Jeff Dean, Prateek Jain, Aditya Kusupati

**Updated**: 2025-03-03T17:54:53Z

**Summary**: Quantizing model weights is critical for reducing the communication and inference costs of large models. However, quantizing models -- especially to low precisions like int4 or int2 -- requires a trade-off in model quality; int2, in particular, is known to severely degrade model quality. Consequently, practitioners are often forced to maintain multiple models with different quantization levels or serve a single model that best satisfies the quality-latency trade-off. On the other hand, integer data types, such as int8, inherently possess a nested (Matryoshka) structure where smaller bit-width integers, like int4 or int2, are nested within the most significant bits. Leveraging this insight, in this paper, we propose Matryoshka Quantization (MatQuant), a novel multi-scale quantization technique that alleviates the aforementioned challenge. This technique allows us to train and maintain a single quantized model but serve it with the precision demanded by the deployment. Furthermore, leveraging MatQuant's co-training and co-distillation regularization, int2 precision models extracted by MatQuant outperform standard int2 quantization by up to to 4% and 7% with OmniQuant and QAT as base algorithms respectively. Finally, we demonstrate that by using an extra bit to represent outliers, a model with an effective precision of 2.05-bit gives an additional 6% improvement with OmniQuant as the base algorithm.

**Link**: [arxiv](http://arxiv.org/abs/2502.06786v3),  [pdf](http://arxiv.org/pdf/2502.06786v3)

**Tags**: cs.LG cs.AI 



### Fuzzy Speculative Decoding for a Tunable Accuracy-Runtime Tradeoff
**Authors**: Maximilian Holsman, Yukun Huang, Bhuwan Dhingra

**Updated**: 2025-03-03T17:40:12Z

**Summary**: Speculative Decoding (SD) enforces strict distributional equivalence to the target model, limiting potential speed ups as distributions of near-equivalence achieve comparable outcomes in many cases. Furthermore, enforcing distributional equivalence means that users are unable to trade deviations from the target model distribution for further inference speed gains. To address these limitations, we introduce Fuzzy Speculative Decoding (FSD) - a decoding algorithm that generalizes SD by accepting candidate tokens purely based on the divergences between the target and draft model distributions. By allowing for controlled divergence from the target model, FSD enables users to flexibly trade generation quality for inference speed. Across several benchmarks, our method is able to achieve significant runtime improvements of over 5 tokens per second faster than SD at only an approximate 2% absolute reduction in benchmark accuracy. In many cases, FSD is even able to match SD benchmark accuracy at over 2 tokens per second faster, demonstrating that distributional equivalence is not necessary to maintain target model performance.

**Link**: [arxiv](http://arxiv.org/abs/2502.20704v2),  [pdf](http://arxiv.org/pdf/2502.20704v2)

**Tags**: cs.AI 



### Forecasting Frontier Language Model Agent Capabilities
**Authors**: Govind Pimpale, Axel Højmark, Jérémy Scheurer, Marius Hobbhahn

**Updated**: 2025-03-03T17:11:16Z

**Summary**: As Language Models (LMs) increasingly operate as autonomous agents, accurately forecasting their capabilities becomes crucial for societal preparedness. We evaluate six forecasting methods that predict downstream capabilities of LM agents. We use "one-step" approaches that predict benchmark scores from input metrics like compute or model release date directly or "two-step" approaches that first predict an intermediate metric like the principal component of cross-benchmark performance (PC-1) and human-evaluated competitive Elo ratings. We evaluate our forecasting methods by backtesting them on a dataset of 38 LMs from the OpenLLM 2 leaderboard. We then use the validated two-step approach (Release Date$\to$Elo$\to$Benchmark) to predict LM agent performance for frontier models on three benchmarks: SWE-Bench Verified (software development), Cybench (cybersecurity assessment), and RE-Bench (ML research engineering). Our forecast predicts that by the beginning of 2026, non-specialized LM agents with low capability elicitation will reach a success rate of 54% on SWE-Bench Verified, while state-of-the-art LM agents will reach an 87% success rate. Our approach does not account for recent advances in inference-compute scaling and might thus be too conservative.

**Link**: [arxiv](http://arxiv.org/abs/2502.15850v2),  [pdf](http://arxiv.org/pdf/2502.15850v2)

**Tags**: cs.CL cs.AI 



### Chain of Draft: Thinking Faster by Writing Less
**Authors**: Silei Xu, Wenhao Xie, Lingxiao Zhao, Pengcheng He

**Updated**: 2025-03-03T17:08:21Z

**Summary**: Large Language Models (LLMs) have demonstrated remarkable performance in solving complex reasoning tasks through mechanisms like Chain-of-Thought (CoT) prompting, which emphasizes verbose, step-by-step reasoning. However, humans typically employ a more efficient strategy: drafting concise intermediate thoughts that capture only essential information. In this work, we propose Chain of Draft (CoD), a novel paradigm inspired by human cognitive processes, where LLMs generate minimalistic yet informative intermediate reasoning outputs while solving tasks. By reducing verbosity and focusing on critical insights, CoD matches or surpasses CoT in accuracy while using as little as only 7.6% of the tokens, significantly reducing cost and latency across various reasoning tasks. Our code and data are available at https://github.com/sileix/chain-of-draft.

**Link**: [arxiv](http://arxiv.org/abs/2502.18600v2),  [pdf](http://arxiv.org/pdf/2502.18600v2)

**Tags**: cs.CL I.2.7 



### R1-T1: Fully Incentivizing Translation Capability in LLMs via Reasoning   Learning
**Authors**: Minggui He, Yilun Liu, Shimin Tao, Yuanchang Luo, Hongyong Zeng, Chang Su, Li Zhang, Hongxia Ma, Daimeng Wei, Weibin Meng, Hao Yang, Boxing Chen, Osamu Yoshie

**Updated**: 2025-03-03T16:44:25Z

**Summary**: Despite recent breakthroughs in reasoning-enhanced large language models (LLMs) like DeepSeek-R1, incorporating inference-time reasoning into machine translation (MT), where human translators naturally employ structured, multi-layered reasoning chain-of-thoughts (CoTs), is yet underexplored. Existing methods either design a fixed CoT tailored for a specific MT sub-task (e.g., literature translation), or rely on synthesizing CoTs unaligned with humans, limiting their adaptability to diverse translation scenarios. This paper introduces R1-Translator (R1-T1), a novel framework to achieve inference-time reasoning for general MT via reinforcement learning (RL) with human-aligned CoTs comprising six common patterns. Our approach pioneers three innovations: (1) extending reasoning-based translation beyond MT sub-tasks to six languages and diverse tasks (e.g., legal/medical domain adaptation, idiom resolution); (2) formalizing six expert-curated CoT templates that mirror hybrid human strategies like context-aware paraphrasing and back translation; and (3) enabling self-evolving CoT discovery through RL. Experimental results indicate a steady translation performance improvement in 11 languages and 40 translation directions on Flores-101 test set, especially on the languages unseen from training.

**Link**: [arxiv](http://arxiv.org/abs/2502.19735v2),  [pdf](http://arxiv.org/pdf/2502.19735v2)

**Tags**: cs.CL 



### InductionBench: LLMs Fail in the Simplest Complexity Class
**Authors**: Wenyue Hua, Tyler Wong, Sun Fei, Liangming Pan, Adam Jardine, William Yang Wang

**Updated**: 2025-03-03T16:38:10Z

**Summary**: Large language models (LLMs) have shown remarkable improvements in reasoning and many existing benchmarks have been addressed by models such as o1 and o3 either fully or partially. However, a majority of these benchmarks emphasize deductive reasoning, including mathematical and coding tasks in which rules such as mathematical axioms or programming syntax are clearly defined, based on which LLMs can plan and apply these rules to arrive at a solution. In contrast, inductive reasoning, where one infers the underlying rules from observed data, remains less explored. Such inductive processes lie at the heart of scientific discovery, as they enable researchers to extract general principles from empirical observations. To assess whether LLMs possess this capacity, we introduce InductionBench, a new benchmark designed to evaluate the inductive reasoning ability of LLMs. Our experimental findings reveal that even the most advanced models available struggle to master the simplest complexity classes within the subregular hierarchy of functions, highlighting a notable deficiency in current LLMs' inductive reasoning capabilities. Coda and data are available https://github.com/Wenyueh/inductive_reasoning_benchmark.

**Link**: [arxiv](http://arxiv.org/abs/2502.15823v3),  [pdf](http://arxiv.org/pdf/2502.15823v3)

**Tags**: cs.LG cs.AI cs.CL cs.FL 



### Dynamics on Lie groups with applications to attitude estimation
**Authors**: T. Forrest Kieffer, Michael Wall

**Updated**: 2025-03-03T16:25:47Z

**Summary**: The problem of filtering - propagation of states through stochastic differential equations (SDEs) and association of measurement data using Bayesian inference - in a state space which forms a Lie group is considered. Particular emphasis is given to concentrated Gaussians (CGs) as a parametric family of probability distributions to capture the uncertainty associated with an estimated state. The so-called group-affine property of the state evolution is shown to be necessary and sufficient for linearity of the dynamics on the associated Lie algebra, in turn implying CGs are invariant under such evolution. A putative SDE on the group is then reformulated as an SDE on the associated Lie algebra. The vector space structure of the Lie algebra together with the notion of a CG enables the leveraging of techniques from conventional Gaussian-based Kalman filtering in an approach called the tangent space filter (TSF). We provide example calculations for several Lie groups that arise in the problem of estimating position, velocity, and orientation of a rigid body from a noisy, potentially biased inertial measurement unit (IMU). For the specific problem of attitude estimation, numerical experiments demonstrate that TSF-based approaches are more accurate and robust than another widely used attitude filtering technique.

**Link**: [arxiv](http://arxiv.org/abs/2502.19714v2),  [pdf](http://arxiv.org/pdf/2502.19714v2)

**Tags**: eess.SY cs.SY math.DS physics.data-an 



### Can Knowledge Editing Really Correct Hallucinations?
**Authors**: Baixiang Huang, Canyu Chen, Xiongxiao Xu, Ali Payani, Kai Shu

**Updated**: 2025-03-03T15:37:23Z

**Summary**: Large Language Models (LLMs) suffer from hallucinations, referring to the non-factual information in generated content, despite their superior capacities across tasks. Meanwhile, knowledge editing has been developed as a new popular paradigm to correct erroneous factual knowledge encoded in LLMs with the advantage of avoiding retraining from scratch. However, a common issue of existing evaluation datasets for knowledge editing is that they do not ensure that LLMs actually generate hallucinated answers to the evaluation questions before editing. When LLMs are evaluated on such datasets after being edited by different techniques, it is hard to directly adopt the performance to assess the effectiveness of different knowledge editing methods in correcting hallucinations. Thus, the fundamental question remains insufficiently validated: Can knowledge editing really correct hallucinations in LLMs? We proposed HalluEditBench to holistically benchmark knowledge editing methods in correcting real-world hallucinations. First, we rigorously construct a massive hallucination dataset with 9 domains, 26 topics and more than 6,000 hallucinations. Then, we assess the performance of knowledge editing methods in a holistic way on five dimensions including Efficacy, Generalization, Portability, Locality, and Robustness. Through HalluEditBench, we have provided new insights into the potentials and limitations of different knowledge editing methods in correcting hallucinations, which could inspire future improvements and facilitate progress in the field of knowledge editing.

**Link**: [arxiv](http://arxiv.org/abs/2410.16251v3),  [pdf](http://arxiv.org/pdf/2410.16251v3)

**Tags**: cs.CL 



### Revisiting the Test-Time Scaling of o1-like Models: Do they Truly   Possess Test-Time Scaling Capabilities?
**Authors**: Zhiyuan Zeng, Qinyuan Cheng, Zhangyue Yin, Yunhua Zhou, Xipeng Qiu

**Updated**: 2025-03-03T15:29:43Z

**Summary**: The advent of test-time scaling in large language models (LLMs), exemplified by OpenAI's o1 series, has advanced reasoning capabilities by scaling computational resource allocation during inference. While successors like QwQ, Deepseek-R1 (R1) and LIMO replicate these advancements, whether these models truly possess test-time scaling capabilities remains underexplored. This study found that longer CoTs of these o1-like models do not consistently enhance accuracy; in fact, correct solutions are often shorter than incorrect ones for the same questions. Further investigation shows this phenomenon is closely related to models' self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation. We then compare sequential and parallel scaling strategies on QwQ, R1 and LIMO, finding that parallel scaling achieves better coverage and scalability. Based on these insights, we propose Shortest Majority Vote, a method that combines parallel scaling strategies with CoT length characteristics, significantly improving models' test-time scalability compared to conventional majority voting approaches.

**Link**: [arxiv](http://arxiv.org/abs/2502.12215v2),  [pdf](http://arxiv.org/pdf/2502.12215v2)

**Tags**: cs.LG cs.AI cs.CL 



### StarVid: Enhancing Semantic Alignment in Video Diffusion Models via   Spatial and SynTactic Guided Attention Refocusing
**Authors**: Yuanhang Li, Qi Mao, Lan Chen, Zhen Fang, Lei Tian, Xinyan Xiao, Libiao Jin, Hua Wu

**Updated**: 2025-03-03T15:01:03Z

**Summary**: Recent advances in text-to-video (T2V) generation with diffusion models have garnered significant attention. However, they typically perform well in scenes with a single object and motion, struggling in compositional scenarios with multiple objects and distinct motions to accurately reflect the semantic content of text prompts. To address these challenges, we propose \textbf{StarVid}, a plug-and-play, training-free method that improves semantic alignment between multiple subjects, their motions, and text prompts in T2V models. StarVid first leverages the spatial reasoning capabilities of large language models (LLMs) for two-stage motion trajectory planning based on text prompts. Such trajectories serve as spatial priors, guiding a spatial-aware loss to refocus cross-attention (CA) maps into distinctive regions. Furthermore, we propose a syntax-guided contrastive constraint to strengthen the correlation between the CA maps of verbs and their corresponding nouns, enhancing motion-subject binding. Both qualitative and quantitative evaluations demonstrate that the proposed framework significantly outperforms baseline methods, delivering videos of higher quality with improved semantic consistency.

**Link**: [arxiv](http://arxiv.org/abs/2409.15259v2),  [pdf](http://arxiv.org/pdf/2409.15259v2)

**Tags**: cs.CV cs.AI 



### Gumbel Counterfactual Generation From Language Models
**Authors**: Shauli Ravfogel, Anej Svete, Vésteinn Snæbjarnarson, Ryan Cotterell

**Updated**: 2025-03-03T14:56:17Z

**Summary**: Understanding and manipulating the causal generation mechanisms in language models is essential for controlling their behavior. Previous work has primarily relied on techniques such as representation surgery -- e.g., model ablations or manipulation of linear subspaces tied to specific concepts -- to \emph{intervene} on these models. To understand the impact of interventions precisely, it is useful to examine \emph{counterfactuals} -- e.g., how a given sentence would have appeared had it been generated by the model following a specific intervention. We highlight that counterfactual reasoning is conceptually distinct from interventions, as articulated in Pearl's causal hierarchy. Based on this observation, we propose a framework for generating true string counterfactuals by reformulating language models as a structural equation model using the Gumbel-max trick, which we called Gumbel counterfactual generation. This reformulation allows us to model the joint distribution over original strings and their counterfactuals resulting from the same instantiation of the sampling noise. We develop an algorithm based on hindsight Gumbel sampling that allows us to infer the latent noise variables and generate counterfactuals of observed strings. Our experiments demonstrate that the approach produces meaningful counterfactuals while at the same time showing that commonly used intervention techniques have considerable undesired side effects.

**Link**: [arxiv](http://arxiv.org/abs/2411.07180v4),  [pdf](http://arxiv.org/pdf/2411.07180v4)

**Tags**: cs.CL cs.AI cs.LG 



### From Tokens to Words: On the Inner Lexicon of LLMs
**Authors**: Guy Kaplan, Matanel Oren, Yuval Reif, Roy Schwartz

**Updated**: 2025-03-03T14:30:07Z

**Summary**: Natural language is composed of words, but modern large language models (LLMs) process sub-words as input. A natural question raised by this discrepancy is whether LLMs encode words internally, and if so how. We present evidence that LLMs engage in an intrinsic detokenization process, where sub-word sequences are combined into coherent whole-word representations at their last token. Our experiments show that this process primarily takes place within the early and middle layers of the model. We further demonstrate its robustness to arbitrary splits (e.g., "cats" to "ca" and "ts"), typos, and importantly-to out-of-vocabulary words: when feeding the last token internal representations of such words to the model as input, it can "understand" them as the complete word despite never seeing such representations as input during training. Our findings suggest that LLMs maintain a latent vocabulary beyond the tokenizer's scope. These insights provide a practical, finetuning-free application for expanding the vocabulary of pre-trained models. By enabling the addition of new vocabulary words, we reduce input length and inference iterations, which reduces both space and model latency, with little to no loss in model accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2410.05864v4),  [pdf](http://arxiv.org/pdf/2410.05864v4)

**Tags**: cs.CL cs.AI 



### Multi-Modal and Multi-Attribute Generation of Single Cells with CFGen
**Authors**: Alessandro Palma, Till Richter, Hanyi Zhang, Manuel Lubetzki, Alexander Tong, Andrea Dittadi, Fabian Theis

**Updated**: 2025-03-03T14:24:06Z

**Summary**: Generative modeling of single-cell RNA-seq data is crucial for tasks like trajectory inference, batch effect removal, and simulation of realistic cellular data. However, recent deep generative models simulating synthetic single cells from noise operate on pre-processed continuous gene expression approximations, overlooking the discrete nature of single-cell data, which limits their effectiveness and hinders the incorporation of robust noise models. Additionally, aspects like controllable multi-modal and multi-label generation of cellular data remain underexplored. This work introduces CellFlow for Generation (CFGen), a flow-based conditional generative model that preserves the inherent discreteness of single-cell data. CFGen generates whole-genome multi-modal single-cell data reliably, improving the recovery of crucial biological data characteristics while tackling relevant generative tasks such as rare cell type augmentation and batch correction. We also introduce a novel framework for compositional data generation using Flow Matching. By showcasing CFGen on a diverse set of biological datasets and settings, we provide evidence of its value to the fields of computational biology and deep generative models.

**Link**: [arxiv](http://arxiv.org/abs/2407.11734v2),  [pdf](http://arxiv.org/pdf/2407.11734v2)

**Tags**: q-bio.QM cs.LG q-bio.GN 



### OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews
**Authors**: Maximilian Idahl, Zahra Ahmadi

**Updated**: 2025-03-03T13:58:56Z

**Summary**: We present OpenReviewer, an open-source system for generating high-quality peer reviews of machine learning and AI conference papers. At its core is Llama-OpenReviewer-8B, an 8B parameter language model specifically fine-tuned on 79,000 expert reviews from top conferences. Given a PDF paper submission and review template as input, OpenReviewer extracts the full text, including technical content like equations and tables, and generates a structured review following conference-specific guidelines. Our evaluation on 400 test papers shows that OpenReviewer produces considerably more critical and realistic reviews compared to general-purpose LLMs like GPT-4 and Claude-3.5. While other LLMs tend toward overly positive assessments, OpenReviewer's recommendations closely match the distribution of human reviewer ratings. The system provides authors with rapid, constructive feedback to improve their manuscripts before submission, though it is not intended to replace human peer review. OpenReviewer is available as an online demo and open-source tool.

**Link**: [arxiv](http://arxiv.org/abs/2412.11948v2),  [pdf](http://arxiv.org/pdf/2412.11948v2)

**Tags**: cs.AI 



### CUIfy the XR: An Open-Source Package to Embed LLM-powered Conversational   Agents in XR
**Authors**: Kadir Burak Buldu, Süleyman Özdel, Ka Hei Carrie Lau, Mengdi Wang, Daniel Saad, Sofie Schönborn, Auxane Boch, Enkelejda Kasneci, Efe Bozkir

**Updated**: 2025-03-03T13:41:33Z

**Summary**: Recent developments in computer graphics, machine learning, and sensor technologies enable numerous opportunities for extended reality (XR) setups for everyday life, from skills training to entertainment. With large corporations offering affordable consumer-grade head-mounted displays (HMDs), XR will likely become pervasive, and HMDs will develop as personal devices like smartphones and tablets. However, having intelligent spaces and naturalistic interactions in XR is as important as technological advances so that users grow their engagement in virtual and augmented spaces. To this end, large language model (LLM)--powered non-player characters (NPCs) with speech-to-text (STT) and text-to-speech (TTS) models bring significant advantages over conventional or pre-scripted NPCs for facilitating more natural conversational user interfaces (CUIs) in XR. This paper provides the community with an open-source, customizable, extendable, and privacy-aware Unity package, CUIfy, that facilitates speech-based NPC-user interaction with widely used LLMs, STT, and TTS models. Our package also supports multiple LLM-powered NPCs per environment and minimizes latency between different computational models through streaming to achieve usable interactions between users and NPCs. We publish our source code in the following repository: https://gitlab.lrz.de/hctl/cuify

**Link**: [arxiv](http://arxiv.org/abs/2411.04671v3),  [pdf](http://arxiv.org/pdf/2411.04671v3)

**Tags**: cs.HC cs.AI 



### Optimize Incompatible Parameters through Compatibility-aware Knowledge   Integration
**Authors**: Zheqi Lv, Keming Ye, Zishu Wei, Qi Tian, Shengyu Zhang, Wenqiao Zhang, Wenjie Wang, Kun Kuang, Tat-Seng Chua, Fei Wu

**Updated**: 2025-03-03T13:27:01Z

**Summary**: Deep neural networks have become foundational to advancements in multiple domains, including recommendation systems, natural language processing, and so on. Despite their successes, these models often contain incompatible parameters that can be underutilized or detrimental to model performance, particularly when faced with specific, varying data distributions. Existing research excels in removing such parameters or merging the outputs of multiple different pretrained models. However, the former focuses on efficiency rather than performance, while the latter requires several times more computing and storage resources to support inference. In this paper, we set the goal to explicitly improve these incompatible parameters by leveraging the complementary strengths of different models, thereby directly enhancing the models without any additional parameters. Specifically, we propose Compatibility-aware Knowledge Integration (CKI), which consists of Parameter Compatibility Assessment and Parameter Splicing, which are used to evaluate the knowledge content of multiple models and integrate the knowledge into one model, respectively. The integrated model can be used directly for inference or for further fine-tuning. We conduct extensive experiments on various datasets for recommendation and language tasks, and the results show that Compatibility-aware Knowledge Integration can effectively optimize incompatible parameters under multiple tasks and settings to break through the training limit of the original model without increasing the inference cost.

**Link**: [arxiv](http://arxiv.org/abs/2501.07596v2),  [pdf](http://arxiv.org/pdf/2501.07596v2)

**Tags**: cs.LG cs.CL cs.IR 



### Towards Better Chain-of-Thought: A Reflection on Effectiveness and   Faithfulness
**Authors**: Jiachun Li, Pengfei Cao, Yubo Chen, Jiexin Xu, Huaijun Li, Xiaojian Jiang, Kang Liu, Jun Zhao

**Updated**: 2025-03-03T13:25:36Z

**Summary**: Chain-of-thought (CoT) prompting demonstrates varying performance under different reasoning tasks. Previous work attempts to evaluate it but falls short in providing an in-depth analysis of patterns that influence the CoT. In this paper, we study the CoT performance from the perspective of effectiveness and faithfulness. For the former, we identify key factors that influence CoT effectiveness on performance improvement, including problem difficulty, information gain, and information flow. For the latter, we interpret the unfaithful CoT issue by conducting a joint analysis of the information interaction among the question, CoT, and answer. The result demonstrates that, when the LLM predicts answers, it can recall correct information missing in the CoT from the question, leading to the problem. Finally, we propose a novel algorithm to mitigate this issue, in which we recall extra information from the question to enhance the CoT generation and evaluate CoTs based on their information gain. Extensive experiments demonstrate that our approach enhances both the faithfulness and effectiveness of CoT.

**Link**: [arxiv](http://arxiv.org/abs/2405.18915v2),  [pdf](http://arxiv.org/pdf/2405.18915v2)

**Tags**: cs.CL cs.AI 



### MATCH POLICY: A Simple Pipeline from Point Cloud Registration to   Manipulation Policies
**Authors**: Haojie Huang, Haotian Liu, Dian Wang, Robin Walters, Robert Platt

**Updated**: 2025-03-03T13:22:14Z

**Summary**: Many manipulation tasks require the robot to rearrange objects relative to one another. Such tasks can be described as a sequence of relative poses between parts of a set of rigid bodies. In this work, we propose MATCH POLICY, a simple but novel pipeline for solving high-precision pick and place tasks. Instead of predicting actions directly, our method registers the pick and place targets to the stored demonstrations. This transfers action inference into a point cloud registration task and enables us to realize nontrivial manipulation policies without any training. MATCH POLICY is designed to solve high-precision tasks with a key-frame setting. By leveraging the geometric interaction and the symmetries of the task, it achieves extremely high sample efficiency and generalizability to unseen configurations. We demonstrate its state-of-the-art performance across various tasks on RLBench benchmark compared with several strong baselines and test it on a real robot with six tasks.

**Link**: [arxiv](http://arxiv.org/abs/2409.15517v2),  [pdf](http://arxiv.org/pdf/2409.15517v2)

**Tags**: cs.RO cs.CV 



### MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry   Scientific Hypotheses
**Authors**: Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, Dongzhan Zhou

**Updated**: 2025-03-03T13:17:24Z

**Summary**: Scientific discovery contributes largely to human society's prosperity, and recent progress shows that LLMs could potentially catalyze this process. However, it is still unclear whether LLMs can discover novel and valid hypotheses in chemistry. In this work, we investigate this central research question: Can LLMs automatically discover novel and valid chemistry research hypotheses given only a chemistry research background (consisting of a research question and/or a background survey), without limitation on the domain of the research question? After extensive discussions with chemistry experts, we propose an assumption that a majority of chemistry hypotheses can be resulted from a research background and several inspirations. With this key insight, we break the central question into three smaller fundamental questions. In brief, they are: (1) given a background question, whether LLMs can retrieve good inspirations; (2) with background and inspirations, whether LLMs can lead to hypothesis; and (3) whether LLMs can identify good hypotheses to rank them higher. To investigate these questions, we construct a benchmark consisting of 51 chemistry papers published in Nature, Science, or a similar level in 2024 (all papers are only available online since 2024). Every paper is divided by chemistry PhD students into three components: background, inspirations, and hypothesis. The goal is to rediscover the hypothesis, given only the background and a large randomly selected chemistry literature corpus consisting the ground truth inspiration papers, with LLMs trained with data up to 2023. We also develop an LLM-based multi-agent framework that leverages the assumption, consisting of three stages reflecting the three smaller questions. The proposed method can rediscover many hypotheses with very high similarity with the ground truth ones, covering the main innovations.

**Link**: [arxiv](http://arxiv.org/abs/2410.07076v4),  [pdf](http://arxiv.org/pdf/2410.07076v4)

**Tags**: cs.CL cs.AI cs.LG 



### NavRAG: Generating User Demand Instructions for Embodied Navigation   through Retrieval-Augmented LLM
**Authors**: Zihan Wang, Yaohui Zhu, Gim Hee Lee, Yachun Fan

**Updated**: 2025-03-03T12:56:35Z

**Summary**: Vision-and-Language Navigation (VLN) is an essential skill for embodied agents, allowing them to navigate in 3D environments following natural language instructions. High-performance navigation models require a large amount of training data, the high cost of manually annotating data has seriously hindered this field. Therefore, some previous methods translate trajectory videos into step-by-step instructions for expanding data, but such instructions do not match well with users' communication styles that briefly describe destinations or state specific needs. Moreover, local navigation trajectories overlook global context and high-level task planning. To address these issues, we propose NavRAG, a retrieval-augmented generation (RAG) framework that generates user demand instructions for VLN. NavRAG leverages LLM to build a hierarchical scene description tree for 3D scene understanding from global layout to local details, then simulates various user roles with specific demands to retrieve from the scene tree, generating diverse instructions with LLM. We annotate over 2 million navigation instructions across 861 scenes and evaluate the data quality and navigation performance of trained models.

**Link**: [arxiv](http://arxiv.org/abs/2502.11142v2),  [pdf](http://arxiv.org/pdf/2502.11142v2)

**Tags**: cs.AI cs.CL cs.CV 



### Efficient Learning With Sine-Activated Low-rank Matrices
**Authors**: Yiping Ji, Hemanth Saratchandran, Cameron Gordon, Zeyu Zhang, Simon Lucey

**Updated**: 2025-03-03T12:32:47Z

**Summary**: Low-rank decomposition has emerged as a vital tool for enhancing parameter efficiency in neural network architectures, gaining traction across diverse applications in machine learning. These techniques significantly lower the number of parameters, striking a balance between compactness and performance. However, a common challenge has been the compromise between parameter efficiency and the accuracy of the model, where reduced parameters often lead to diminished accuracy compared to their full-rank counterparts. In this work, we propose a novel theoretical framework that integrates a sinusoidal function within the low-rank decomposition process. This approach not only preserves the benefits of the parameter efficiency characteristic of low-rank methods but also increases the decomposition's rank, thereby enhancing model performance. Our method proves to be a plug in enhancement for existing low-rank models, as evidenced by its successful application in Vision Transformers (ViT), Large Language Models (LLMs), Neural Radiance Fields (NeRF) and 3D shape modelling.

**Link**: [arxiv](http://arxiv.org/abs/2403.19243v4),  [pdf](http://arxiv.org/pdf/2403.19243v4)

**Tags**: cs.LG cs.CV cs.NE 



### FLARE: Feed-forward Geometry, Appearance and Camera Estimation from   Uncalibrated Sparse Views
**Authors**: Shangzhan Zhang, Jianyuan Wang, Yinghao Xu, Nan Xue, Christian Rupprecht, Xiaowei Zhou, Yujun Shen, Gordon Wetzstein

**Updated**: 2025-03-03T12:09:29Z

**Summary**: We present FLARE, a feed-forward model designed to infer high-quality camera poses and 3D geometry from uncalibrated sparse-view images (i.e., as few as 2-8 inputs), which is a challenging yet practical setting in real-world applications. Our solution features a cascaded learning paradigm with camera pose serving as the critical bridge, recognizing its essential role in mapping 3D structures onto 2D image planes. Concretely, FLARE starts with camera pose estimation, whose results condition the subsequent learning of geometric structure and appearance, optimized through the objectives of geometry reconstruction and novel-view synthesis. Utilizing large-scale public datasets for training, our method delivers state-of-the-art performance in the tasks of pose estimation, geometry reconstruction, and novel view synthesis, while maintaining the inference efficiency (i.e., less than 0.5 seconds). The project page and code can be found at: https://zhanghe3z.github.io/FLARE/

**Link**: [arxiv](http://arxiv.org/abs/2502.12138v3),  [pdf](http://arxiv.org/pdf/2502.12138v3)

**Tags**: cs.CV 



### Signature Kernel Conditional Independence Tests in Causal Discovery for   Stochastic Processes
**Authors**: Georg Manten, Cecilia Casolo, Emilio Ferrucci, Søren Wengel Mogensen, Cristopher Salvi, Niki Kilbertus

**Updated**: 2025-03-03T11:25:26Z

**Summary**: Inferring the causal structure underlying stochastic dynamical systems from observational data holds great promise in domains ranging from science and health to finance. Such processes can often be accurately modeled via stochastic differential equations (SDEs), which naturally imply causal relationships via "which variables enter the differential of which other variables". In this paper, we develop conditional independence (CI) constraints on coordinate processes over selected intervals that are Markov with respect to the acyclic dependence graph (allowing self-loops) induced by a general SDE model. We then provide a sound and complete causal discovery algorithm, capable of handling both fully and partially observed data, and uniquely recovering the underlying or induced ancestral graph by exploiting time directionality assuming a CI oracle. Finally, to make our algorithm practically usable, we also propose a flexible, consistent signature kernel-based CI test to infer these constraints from data. We extensively benchmark the CI test in isolation and as part of our causal discovery algorithms, outperforming existing approaches in SDE models and beyond.

**Link**: [arxiv](http://arxiv.org/abs/2402.18477v4),  [pdf](http://arxiv.org/pdf/2402.18477v4)

**Tags**: cs.LG cs.AI stat.ML 



### Ephemerality meets LiDAR-based Lifelong Mapping
**Authors**: Hyeonjae Gil, Dongjae Lee, Giseop Kim, Ayoung Kim

**Updated**: 2025-03-03T11:16:49Z

**Summary**: Lifelong mapping is crucial for the long-term deployment of robots in dynamic environments. In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-to-end fashion. Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary. Central to our approach is the probabilistic modeling of the world into two-stage $\textit{ephemerality}$, which represent the transiency of points in the map within two different time scales. By leveraging the spatiotemporal context encoded in ephemeralities, ELite can accurately infer transient map elements, maintain a reliable up-to-date static map, and improve robustness in aligning the new data in a more fine-grained manner. Extensive real-world experiments on long-term datasets demonstrate the robustness and effectiveness of our system. The source code is publicly available for the robotics community: https://github.com/dongjae0107/ELite.

**Link**: [arxiv](http://arxiv.org/abs/2502.13452v2),  [pdf](http://arxiv.org/pdf/2502.13452v2)

**Tags**: cs.RO 



### Variational Best-of-N Alignment
**Authors**: Afra Amini, Tim Vieira, Elliott Ash, Ryan Cotterell

**Updated**: 2025-03-03T11:08:15Z

**Summary**: Best-of-N (BoN) is a popular and effective algorithm for aligning language models to human preferences. The algorithm works as follows: at inference time, N samples are drawn from the language model, and the sample with the highest reward, as judged by a reward model, is returned as the output. Despite its effectiveness, BoN is computationally expensive; it reduces sampling throughput by a factor of N. To make BoN more efficient at inference time, one strategy is to fine-tune the language model to mimic what BoN does during inference. To achieve this, we derive the distribution induced by the BoN algorithm. We then propose to fine-tune the language model to minimize backward KL divergence to the BoN distribution. Our approach is analogous to mean-field variational inference and, thus, we term it variational BoN (vBoN). To the extent this fine-tuning is successful and we end up with a good approximation, we have reduced the inference cost by a factor of N. Our experiments on controlled generation and summarization tasks show that BoN is the most effective alignment method, and our variational approximation to BoN achieves the closest performance to BoN and surpasses models fine-tuned using the standard KL-constrained RL objective. In the controlled generation task, vBoN appears more frequently on the Pareto frontier of reward and KL divergence compared to other alignment methods. In the summarization task, vBoN achieves high reward values across various sampling temperatures.

**Link**: [arxiv](http://arxiv.org/abs/2407.06057v2),  [pdf](http://arxiv.org/pdf/2407.06057v2)

**Tags**: cs.CL cs.AI cs.LG 



### Offload Rethinking by Cloud Assistance for Efficient Environmental Sound   Recognition on LPWANs
**Authors**: Le Zhang, Quanling Zhao, Run Wang, Shirley Bian, Onat Gungor, Flavio Ponzina, Tajana Rosing

**Updated**: 2025-03-03T11:05:56Z

**Summary**: Learning-based environmental sound recognition has emerged as a crucial method for ultra-low-power environmental monitoring in biological research and city-scale sensing systems. These systems usually operate under limited resources and are often powered by harvested energy in remote areas. Recent efforts in on-device sound recognition suffer from low accuracy due to resource constraints, whereas cloud offloading strategies are hindered by high communication costs. In this work, we introduce ORCA, a novel resource-efficient cloud-assisted environmental sound recognition system on batteryless devices operating over the Low-Power Wide-Area Networks (LPWANs), targeting wide-area audio sensing applications. We propose a cloud assistance strategy that remedies the low accuracy of on-device inference while minimizing the communication costs for cloud offloading. By leveraging a self-attention-based cloud sub-spectral feature selection method to facilitate efficient on-device inference, ORCA resolves three key challenges for resource-constrained cloud offloading over LPWANs: 1) high communication costs and low data rates, 2) dynamic wireless channel conditions, and 3) unreliable offloading. We implement ORCA on an energy-harvesting batteryless microcontroller and evaluate it in a real world urban sound testbed. Our results show that ORCA outperforms state-of-the-art methods by up to $80 \times$ in energy savings and $220 \times$ in latency reduction while maintaining comparable accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2502.15285v2),  [pdf](http://arxiv.org/pdf/2502.15285v2)

**Tags**: cs.SD cs.AI cs.DC cs.NI eess.AS 



### Preregistration does not improve the transparent evaluation of severity   in Popper's philosophy of science or when deviations are allowed
**Authors**: Mark Rubin

**Updated**: 2025-03-03T10:38:57Z

**Summary**: One justification for preregistering research hypotheses, methods, and analyses is that it improves the transparent evaluation of the severity of hypothesis tests. In this article, I consider two cases in which preregistration does not improve this evaluation. First, I argue that, although preregistration can facilitate the transparent evaluation of severity in Mayo's error statistical philosophy of science, it does not facilitate this evaluation in Popper's theory-centric approach. To illustrate, I show that associated concerns about Type I error rate inflation are only relevant in the error statistical approach and not in a theory-centric approach. Second, I argue that a test procedure that is preregistered but that also allows deviations in its implementation (i.e., a "plan, not a prison") does not provide a more transparent evaluation of Mayoian severity than a non-preregistered procedure. In particular, I argue that sample-based validity-enhancing deviations cause an unknown inflation of the test procedure's Type I error rate and, consequently, an unknown reduction in its capability to license inferences severely. I conclude that preregistration does not improve the transparent evaluation of severity in Popper's philosophy of science or when deviations are allowed.

**Link**: [arxiv](http://arxiv.org/abs/2408.12347v9),  [pdf](http://arxiv.org/pdf/2408.12347v9)

**Tags**: stat.ME 



### Uncertainty Quantification for Misspecified Machine Learned Interatomic   Potentials
**Authors**: Danny Perez, Aparna P. A. Subramanyam, Ivan Maliyov, Thomas D. Swinburne

**Updated**: 2025-03-03T10:36:32Z

**Summary**: The use of high-dimensional regression techniques from machine learning has significantly improved the quantitative accuracy of interatomic potentials. Atomic simulations can now plausibly target quantitative predictions in a variety of settings, which has brought renewed interest in robust means to quantify uncertainties on simulation results. In many practical settings, encompassing both classical and a large class of machine learning potentials, the dominant form of uncertainty is currently not due to lack of training data but to misspecification, namely the inability of any one choice of model parameters to exactly match all ab initio training data. However, Bayesian inference, the most common formal tool used to quantify uncertainty, is known to ignore misspecification and thus significantly underestimates parameter uncertainties. Here, we employ a recent misspecification-aware regression technique to quantify parameter uncertainties, which is then propagated to a broad range of phase and defect properties in tungsten via brute force resampling or implicit differentiation. The propagated misspecification uncertainties robustly envelope errors to direct \textit{ab initio} calculation of material properties outside of the training dataset, an essential requirement for any quantitative multi-scale modeling scheme. Finally, we demonstrate application to recent foundational machine learning interatomic potentials, accurately predicting and bounding errors in MACE-MPA-0 energy predictions across the diverse materials project database. Perspectives for the approach in multiscale simulation workflows are discussed.

**Link**: [arxiv](http://arxiv.org/abs/2502.07104v2),  [pdf](http://arxiv.org/pdf/2502.07104v2)

**Tags**: cond-mat.mtrl-sci 



### Exploring Iterative Controllable Summarization with Large Language   Models
**Authors**: Sangwon Ryu, Heejin Do, Daehee Kim, Hwanjo Yu, Dongwoo Kim, Yunsu Kim, Gary Geunbae Lee, Jungseul Ok

**Updated**: 2025-03-03T10:35:27Z

**Summary**: Large language models (LLMs) have demonstrated remarkable performance in abstractive summarization tasks. However, their ability to precisely control summary attributes (e.g., length or topic) remains underexplored, limiting their adaptability to specific user preferences. In this paper, we systematically explore the controllability of LLMs. To this end, we revisit summary attribute measurements and introduce iterative evaluation metrics, failure rate and average iteration count to precisely evaluate controllability of LLMs, rather than merely assessing errors. Our findings show that LLMs struggle more with numerical attributes than with linguistic attributes. To address this challenge, we propose a guide-to-explain framework (GTE) for controllable summarization. Our GTE framework enables the model to identify misaligned attributes in the initial draft and guides it in self-explaining errors in the previous output. By allowing the model to reflect on its misalignment, GTE generates well-adjusted summaries that satisfy the desired attributes with robust effectiveness, requiring surprisingly fewer iterations than other iterative approaches.

**Link**: [arxiv](http://arxiv.org/abs/2411.12460v2),  [pdf](http://arxiv.org/pdf/2411.12460v2)

**Tags**: cs.CL cs.AI 



### TRACE: Temporal Grounding Video LLM via Causal Event Modeling
**Authors**: Yongxin Guo, Jingyu Liu, Mingda Li, Qingbin Liu, Xi Chen, Xiaoying Tang

**Updated**: 2025-03-03T10:28:30Z

**Summary**: Video Temporal Grounding (VTG) is a crucial capability for video understanding models and plays a vital role in downstream tasks such as video browsing and editing. To effectively handle various tasks simultaneously and enable zero-shot prediction, there is a growing trend in employing video LLMs for VTG tasks. However, current video LLM-based methods rely exclusively on natural language generation, lacking the ability to model the clear structure inherent in videos, which restricts their effectiveness in tackling VTG tasks. To address this issue, this paper first formally introduces causal event modeling framework, which represents video LLM outputs as sequences of events, and predict the current event using previous events, video inputs, and textural instructions. Each event consists of three components: timestamps, salient scores, and textual captions. We then propose a novel task-interleaved video LLM called TRACE to effectively implement the causal event modeling framework in practice. The TRACE process visual frames, timestamps, salient scores, and text as distinct tasks, employing various encoders and decoding heads for each. Task tokens are arranged in an interleaved sequence according to the causal event modeling framework's formulation. Extensive experiments on various VTG tasks and datasets demonstrate the superior performance of TRACE compared to state-of-the-art video LLMs. Our model and code are available at https://github.com/gyxxyg/TRACE.

**Link**: [arxiv](http://arxiv.org/abs/2410.05643v3),  [pdf](http://arxiv.org/pdf/2410.05643v3)

**Tags**: cs.CV 



### "Nuclear Deployed!": Analyzing Catastrophic Risks in Decision-making of   Autonomous LLM Agents
**Authors**: Rongwu Xu, Xiaojian Li, Shuo Chen, Wei Xu

**Updated**: 2025-03-03T09:45:24Z

**Summary**: Large language models (LLMs) are evolving into autonomous decision-makers, raising concerns about catastrophic risks in high-stakes scenarios, particularly in Chemical, Biological, Radiological and Nuclear (CBRN) domains. Based on the insight that such risks can originate from trade-offs between the agent's Helpful, Harmlessness and Honest (HHH) goals, we build a novel three-stage evaluation framework, which is carefully constructed to effectively and naturally expose such risks. We conduct 14,400 agentic simulations across 12 advanced LLMs, with extensive experiments and analysis. Results reveal that LLM agents can autonomously engage in catastrophic behaviors and deception, without being deliberately induced. Furthermore, stronger reasoning abilities often increase, rather than mitigate, these risks. We also show that these agents can violate instructions and superior commands. On the whole, we empirically prove the existence of catastrophic risks in autonomous LLM agents. We will release our code upon request.

**Link**: [arxiv](http://arxiv.org/abs/2502.11355v2),  [pdf](http://arxiv.org/pdf/2502.11355v2)

**Tags**: cs.CL cs.AI cs.CR cs.CY 



### Attacking Large Language Models with Projected Gradient Descent
**Authors**: Simon Geisler, Tom Wollschläger, M. H. I. Abdalla, Johannes Gasteiger, Stephan Günnemann

**Updated**: 2025-03-03T09:37:27Z

**Summary**: Current LLM alignment methods are readily broken through specifically crafted adversarial prompts. While crafting adversarial prompts using discrete optimization is highly effective, such attacks typically use more than 100,000 LLM calls. This high computational cost makes them unsuitable for, e.g., quantitative analyses and adversarial training. To remedy this, we revisit Projected Gradient Descent (PGD) on the continuously relaxed input prompt. Although previous attempts with ordinary gradient-based attacks largely failed, we show that carefully controlling the error introduced by the continuous relaxation tremendously boosts their efficacy. Our PGD for LLMs is up to one order of magnitude faster than state-of-the-art discrete optimization to achieve the same devastating attack results.

**Link**: [arxiv](http://arxiv.org/abs/2402.09154v2),  [pdf](http://arxiv.org/pdf/2402.09154v2)

**Tags**: cs.LG 



### LaERC-S: Improving LLM-based Emotion Recognition in Conversation with   Speaker Characteristics
**Authors**: Yumeng Fu, Junjie Wu, Zhongjie Wang, Meishan Zhang, Lili Shan, Yulin Wu, Bingquan Li

**Updated**: 2025-03-03T09:36:14Z

**Summary**: Emotion recognition in conversation (ERC), the task of discerning human emotions for each utterance within a conversation, has garnered significant attention in human-computer interaction systems. Previous ERC studies focus on speaker-specific information that predominantly stems from relationships among utterances, which lacks sufficient information around conversations. Recent research in ERC has sought to exploit pre-trained large language models (LLMs) with speaker modelling to comprehend emotional states. Although these methods have achieved encouraging results, the extracted speaker-specific information struggles to indicate emotional dynamics. In this paper, motivated by the fact that speaker characteristics play a crucial role and LLMs have rich world knowledge, we present LaERC-S, a novel framework that stimulates LLMs to explore speaker characteristics involving the mental state and behavior of interlocutors, for accurate emotion predictions. To endow LLMs with this knowledge information, we adopt the two-stage learning to make the models reason speaker characteristics and track the emotion of the speaker in complex conversation scenarios. Extensive experiments on three benchmark datasets demonstrate the superiority of LaERC-S, reaching the new state-of-the-art.

**Link**: [arxiv](http://arxiv.org/abs/2403.07260v2),  [pdf](http://arxiv.org/pdf/2403.07260v2)

**Tags**: cs.CL 



### Left-Linear Completion with AC Axioms
**Authors**: Johannes Niederhauser, Nao Hirokawa, Aart Middeldorp

**Updated**: 2025-03-03T09:31:05Z

**Summary**: We revisit completion modulo equational theories for left-linear term rewrite systems where unification modulo the theory is avoided and the normal rewrite relation can be used in order to decide validity questions. To that end, we give a new correctness proof for finite runs and establish a simulation result between the two inference systems known from the literature. Given a concrete reduction order, novel canonicity results show that the resulting complete systems are unique up to the representation of their rules' right-hand sides. Furthermore, we show how left-linear AC completion can be simulated by general AC completion. In particular, this result allows us to switch from the former to the latter at any point during a completion process.

**Link**: [arxiv](http://arxiv.org/abs/2405.17109v3),  [pdf](http://arxiv.org/pdf/2405.17109v3)

**Tags**: cs.LO 



### Enhancing Large Language Models with Pseudo- and Multisource- Knowledge   Graphs for Open-ended Question Answering
**Authors**: Jiaxiang Liu, Tong Zhou, Yubo Chen, Kang Liu, Jun Zhao

**Updated**: 2025-03-03T09:21:11Z

**Summary**: Mitigating the hallucinations of Large Language Models is a crucial task. Although some existing methods employ self-enhancement techniques, they fall short of effectively addressing unknown factual hallucinations. Meanwhile, Knowledge Graph (KG) enhancement approaches fail to address the generalization across different KG sources and the enhancement of open-ended answer questions simultaneously. To tackle these limitations, we propose a framework that combines Pseudo-Graph Generation and Atomic Knowledge Verification (PG\&AKV). Enhancement of open-ended question-answering begins with leveraging the Pseudo-Graph Generation to provide the related knowledge framework. Subsequently, Atomic Knowledge Verification utilizes atomic-level knowledge querying and verification to achieve generalizability under different KG sources. Compared to the baseline, this approach yields a minimum improvement of 11.5 in the ROUGE-L score for open-ended questions. For precise-answered questions, we observe a minimum accuracy improvement of 7.5%. Moreover, PG\&AKV also exhibits generalizability across different KG sources. Utilizing KG different from the question sources, PG\&AKV can even achieve at least a 3.5 % performance improvement. In summary, our results pave the way for enhancing LLMs by incorporating Pseudo- and Multisource-KGs, particularly in the filed of open-ended questions.

**Link**: [arxiv](http://arxiv.org/abs/2402.09911v2),  [pdf](http://arxiv.org/pdf/2402.09911v2)

**Tags**: cs.CL cs.AI 



### Principled priors for Bayesian inference of circular models
**Authors**: Xiang Ye, Janet Van Niekerk, Håvard Rue

**Updated**: 2025-03-03T09:13:34Z

**Summary**: Advancements in computational power and methodologies have enabled research on massive datasets. However, tools for analyzing data with directional or periodic characteristics, such as wind directions and customers' arrival time in 24-hour clock, remain underdeveloped. While statisticians have proposed circular distributions for such analyses, significant challenges persist in constructing circular statistical models, particularly in the context of Bayesian methods. These challenges stem from limited theoretical development and a lack of historical studies on prior selection for circular distribution parameters.   In this article, we propose a principled, practical and systematic framework for selecting priors that effectively prevents overfitting in circular scenarios, especially when there is insufficient information to guide prior selection. We introduce well-examined Penalized Complexity (PC) priors for the most widely used circular distributions. Comprehensive comparisons with existing priors in the literature are conducted through simulation studies and a practical case study. Finally, we discuss the contributions and implications of our work, providing a foundation for further advancements in constructing Bayesian circular statistical models.

**Link**: [arxiv](http://arxiv.org/abs/2502.18223v2),  [pdf](http://arxiv.org/pdf/2502.18223v2)

**Tags**: stat.ME 



### ECLeKTic: a Novel Challenge Set for Evaluation of Cross-Lingual   Knowledge Transfer
**Authors**: Omer Goldman, Uri Shaham, Dan Malkin, Sivan Eiger, Avinatan Hassidim, Yossi Matias, Joshua Maynez, Adi Mayrav Gilady, Jason Riesa, Shruti Rijhwani, Laura Rimell, Idan Szpektor, Reut Tsarfaty, Matan Eyal

**Updated**: 2025-03-03T09:11:46Z

**Summary**: To achieve equitable performance across languages, multilingual large language models (LLMs) must be able to abstract knowledge beyond the language in which it was acquired. However, the current literature lacks reliable ways to measure LLMs' capability of cross-lingual knowledge transfer. To that end, we present ECLeKTic, a multilingual closed-book QA (CBQA) dataset that Evaluates Cross-Lingual Knowledge Transfer in a simple, black-box manner. We detected information with uneven coverage across languages by controlling for presence and absence of Wikipedia articles in 12 languages. We generated knowledge-seeking questions in a source language, for which the answer appears in a relevant Wikipedia article and translated them to all other 11 languages, for which the respective Wikipedias lack equivalent articles. Assuming that Wikipedia reflects the prominent knowledge in the LLM's training data, to solve ECLeKTic's CBQA task the model is required to transfer knowledge between languages. Experimenting with 8 LLMs, we show that SOTA models struggle to effectively share knowledge across, languages even if they can predict the answer well for queries in the same language the knowledge was acquired in.

**Link**: [arxiv](http://arxiv.org/abs/2502.21228v2),  [pdf](http://arxiv.org/pdf/2502.21228v2)

**Tags**: cs.CL cs.AI 



### Just Ramp-up: Unleash the Potential of Regression-based Estimator for   A/B Tests under Network Interference
**Authors**: Qianyi Chen, Bo Li

**Updated**: 2025-03-03T09:07:23Z

**Summary**: Recent research in causal inference under network interference has explored various experimental designs and estimation techniques to address this issue. However, existing methods, which typically rely on single experiments, often reach a performance bottleneck and face limitations in handling diverse interference structures. In contrast, we propose leveraging multiple experiments to overcome these limitations. In industry, the use of sequential experiments, often known as the ramp-up process, where traffic to the treatment gradually increases, is common due to operational needs like risk management and cost control. Our approach shifts the focus from operational aspects to the statistical advantages of merging data from multiple experiments. By combining data from sequentially conducted experiments, we aim to estimate the global average treatment effect more effectively. In this paper, we begin by analyzing the bias and variance of the linear regression estimator for GATE under general linear network interference. We demonstrate that bias plays a dominant role in the bias-variance tradeoff and highlight the intrinsic bias reduction achieved by merging data from experiments with strictly different treatment proportions. Herein the improvement introduced by merging two steps of experimental data is essential. In addition, we show that merging more steps of experimental data is unnecessary under general linear interference, while it can become beneficial when nonlinear interference occurs. Furthermore, we look into a more advanced estimator based on graph neural networks. Through extensive simulation studies, we show that the regression-based estimator benefits remarkably from training on merged experiment data, achieving outstanding statistical performance.

**Link**: [arxiv](http://arxiv.org/abs/2410.12740v2),  [pdf](http://arxiv.org/pdf/2410.12740v2)

**Tags**: stat.ME 



### VoCo-LLaMA: Towards Vision Compression with Large Language Models
**Authors**: Xubing Ye, Yukang Gan, Xiaoke Huang, Yixiao Ge, Yansong Tang

**Updated**: 2025-03-03T09:05:52Z

**Summary**: Vision-Language Models (VLMs) have achieved remarkable success in various multi-modal tasks, but they are often bottlenecked by the limited context window and high computational cost of processing high-resolution image inputs and videos. Vision compression can alleviate this problem by reducing the vision token count. Previous approaches compress vision tokens with external modules and force LLMs to understand the compressed ones, leading to visual information loss. However, the LLMs' understanding paradigm of vision tokens is not fully utilised in the compression learning process. We propose VoCo-LLaMA, the first approach to compress vision tokens using LLMs. By introducing Vision Compression tokens during the vision instruction tuning phase and leveraging attention distillation, our method distill how LLMs comprehend vision tokens into their processing of VoCo tokens. VoCo-LLaMA facilitates effective vision compression and improves the computational efficiency during the inference stage. Specifically, our method achieves minimal performance loss with a compression ratio of 576$\times$, resulting in up to 94.8$\%$ fewer FLOPs and 69.6$\%$ acceleration in inference time. Furthermore, through continuous training using time-series compressed token sequences of video frames, VoCo-LLaMA demonstrates the ability to understand temporal correlations, outperforming previous methods on popular video question-answering benchmarks. Our approach presents a promising way to unlock the full potential of VLMs' contextual window, enabling more scalable multi-modal applications. The project page, along with the associated code, can be accessed via https://yxxxb.github.io/VoCo-LLaMA-page/.

**Link**: [arxiv](http://arxiv.org/abs/2406.12275v2),  [pdf](http://arxiv.org/pdf/2406.12275v2)

**Tags**: cs.CV 



### Artemis: Toward Accurate Detection of Server-Side Request Forgeries   through LLM-Assisted Inter-Procedural Path-Sensitive Taint Analysis
**Authors**: Yuchen Ji, Ting Dai, Zhichao Zhou, Yutian Tang, Jingzhu He

**Updated**: 2025-03-03T08:49:07Z

**Summary**: Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP's dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink functions. Second, Artemis constructs both explicit and implicit call graphs to infer functions' relationships. Third, Artemis performs taint analysis based on a set of rules that prevent over-tainting and pauses when SSRF exploitation is impossible. Fourth, Artemis analyzes the compatibility of path conditions to prune false positives. We have implemented a prototype of Artemis and evaluated it on 250 PHP web applications. Artemis reports 207 true vulnerable paths (106 true SSRFs) with 15 false positives. Of the 106 detected SSRFs, 35 are newly found and reported to developers, with 24 confirmed and assigned CVE IDs.

**Link**: [arxiv](http://arxiv.org/abs/2502.21026v2),  [pdf](http://arxiv.org/pdf/2502.21026v2)

**Tags**: cs.CR cs.SE 



### Q-Adapter: Customizing Pre-trained LLMs to New Preferences with   Forgetting Mitigation
**Authors**: Yi-Chen Li, Fuxiang Zhang, Wenjie Qiu, Lei Yuan, Chengxing Jia, Zongzhang Zhang, Yang Yu, Bo An

**Updated**: 2025-03-03T08:48:38Z

**Summary**: Large Language Models (LLMs), trained on a large amount of corpus, have demonstrated remarkable abilities. However, it may not be sufficient to directly apply open-source LLMs like Llama to certain real-world scenarios, since most of them are trained for \emph{general} purposes. Thus, the demands for customizing publicly available LLMs emerge, but are currently under-studied. In this work, we consider customizing pre-trained LLMs with new human preferences. Specifically, the LLM should not only meet the new preference but also preserve its original capabilities after customization. Drawing inspiration from the observation that human preference can be expressed as a reward model, we propose to cast LLM customization as optimizing the sum of two reward functions, one of which (denoted as $r_1$) was used to pre-train the LLM while the other (denoted as $r_2$) characterizes the new human preference. The obstacle here is that both reward functions are unknown, making the application of modern reinforcement learning methods infeasible. Thanks to the residual Q-learning framework, we can restore the customized LLM with the pre-trained LLM and the \emph{residual Q-function} without the reward function $r_1$. Moreover, we find that for a fixed pre-trained LLM, the reward function $r_2$ can be derived from the residual Q-function, enabling us to directly learn the residual Q-function from the new human preference data upon the Bradley-Terry model. We name our method Q-Adapter as it introduces an adapter module to approximate the residual Q-function for customizing the pre-trained LLM towards the new preference. Experiments based on the Llama-3.1 model on the DSP dataset and HH-RLHF dataset illustrate the superior effectiveness of Q-Adapter on both retaining existing knowledge and learning new preferences. Code is available at https://github.com/mansicer/Q-Adapter.

**Link**: [arxiv](http://arxiv.org/abs/2407.03856v4),  [pdf](http://arxiv.org/pdf/2407.03856v4)

**Tags**: cs.LG 



### Fast and Accurate Gigapixel Pathological Image Classification with   Hierarchical Distillation Multi-Instance Learning
**Authors**: Jiuyang Dong, Junjun Jiang, Kui Jiang, Jiahan Li, Yongbing Zhang

**Updated**: 2025-03-03T08:39:54Z

**Summary**: Although multi-instance learning (MIL) has succeeded in pathological image classification, it faces the challenge of high inference costs due to processing numerous patches from gigapixel whole slide images (WSIs). To address this, we propose HDMIL, a hierarchical distillation multi-instance learning framework that achieves fast and accurate classification by eliminating irrelevant patches. HDMIL consists of two key components: the dynamic multi-instance network (DMIN) and the lightweight instance pre-screening network (LIPN). DMIN operates on high-resolution WSIs, while LIPN operates on the corresponding low-resolution counterparts. During training, DMIN are trained for WSI classification while generating attention-score-based masks that indicate irrelevant patches. These masks then guide the training of LIPN to predict the relevance of each low-resolution patch. During testing, LIPN first determines the useful regions within low-resolution WSIs, which indirectly enables us to eliminate irrelevant regions in high-resolution WSIs, thereby reducing inference time without causing performance degradation. In addition, we further design the first Chebyshev-polynomials-based Kolmogorov-Arnold classifier in computational pathology, which enhances the performance of HDMIL through learnable activation layers. Extensive experiments on three public datasets demonstrate that HDMIL outperforms previous state-of-the-art methods, e.g., achieving improvements of 3.13% in AUC while reducing inference time by 28.6% on the Camelyon16 dataset.

**Link**: [arxiv](http://arxiv.org/abs/2502.21130v2),  [pdf](http://arxiv.org/pdf/2502.21130v2)

**Tags**: cs.CV 



### SURGE: On the Potential of Large Language Models as General-Purpose   Surrogate Code Executors
**Authors**: Bohan Lyu, Siqiao Huang, Zichen Liang

**Updated**: 2025-03-03T08:26:12Z

**Summary**: Neural surrogate models have emerged as powerful and efficient tools in data mining. Meanwhile, large language models (LLMs) have demonstrated remarkable capabilities in code-related tasks. We investigate a novel application: using LLMs as surrogate models for code execution prediction. Given LLMs' unique ability to understand and process diverse programs, they present a promising direction for building general-purpose surrogate models. To systematically investigate this capability, we introduce SURGE, a comprehensive benchmark with $1160$ problems covering $8$ key aspects: multi-language programming tasks, competition-level programming problems, repository-level code analysis, high-cost scientific computing, time-complexity-intensive algorithms, buggy code analysis, programs dependent on specific compilers or execution environments, and formal mathematical proof verification. Through extensive empirical analysis of $21$ open-source and proprietary LLMs, we examine scaling laws, data efficiency, and predictive accuracy. Our findings reveal important insights about the feasibility of LLMs as efficient surrogates for computational processes, with implications for automated software testing, program analysis, and computational resource optimization in data mining applications. Code and dataset are released at https://github.com/Imbernoulli/SURGE.

**Link**: [arxiv](http://arxiv.org/abs/2502.11167v2),  [pdf](http://arxiv.org/pdf/2502.11167v2)

**Tags**: cs.LG cs.CL 



### Inference Scaling Laws: An Empirical Analysis of Compute-Optimal   Inference for Problem-Solving with Language Models
**Authors**: Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang

**Updated**: 2025-03-03T07:53:32Z

**Summary**: While the scaling laws of large language models (LLMs) training have been extensively studied, optimal inference configurations of LLMs remain underexplored. We study inference scaling laws (aka test-time scaling laws) and compute-optimal inference, focusing on the trade-offs between model sizes and generating additional tokens with different inference strategies. As a first step towards understanding and designing compute-optimal inference methods, we studied cost-performance trade-offs for inference strategies such as greedy search, majority voting, best-of-$n$, weighted voting, and two different tree search algorithms, using different model sizes and compute budgets. Our findings suggest that scaling inference compute with inference strategies can be more computationally efficient than scaling model parameters. Additionally, smaller models combined with advanced inference algorithms offer Pareto-optimal trade-offs in cost and performance. For example, the Llemma-7B model, when paired with our novel tree search algorithm, consistently outperforms the Llemma-34B model across all tested inference strategies on the MATH benchmark. We hope these insights contribute to a deeper understanding of inference scaling laws (test-time scaling laws) for LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2408.00724v3),  [pdf](http://arxiv.org/pdf/2408.00724v3)

**Tags**: cs.AI 



### An Empirical Bayes Jackknife Regression Framework for Covariance Matrix   Estimation
**Authors**: Huqin Xin, Sihai Dave Zhao

**Updated**: 2025-03-03T07:52:34Z

**Summary**: Covariance matrix estimation, a classical statistical topic, poses significant challenges when the sample size is comparable to or smaller than the number of features. In this paper, we frame covariance matrix estimation as a compound decision problem and apply an optimal decision rule to estimate covariance parameters. To approximate this rule, we introduce an algorithm that integrates jackknife techniques with machine learning regression methods. This algorithm exhibits adaptability across diverse scenarios without relying on assumptions about data distribution. Simulation results and gene network inference from an RNA-seq experiment in mice demonstrate that our approach either matches or surpasses several state-of-the-art methods

**Link**: [arxiv](http://arxiv.org/abs/2406.13876v3),  [pdf](http://arxiv.org/pdf/2406.13876v3)

**Tags**: stat.ME 62C25 



### Dynamics of Instruction Fine-Tuning for Chinese Large Language Models
**Authors**: Chiyu Song, Zhanchao Zhou, Jianhao Yan, Yuejiao Fei, Zhenzhong Lan, Yue Zhang

**Updated**: 2025-03-03T07:49:17Z

**Summary**: Instruction tuning is a burgeoning method to elicit the general intelligence of Large Language Models (LLMs). While numerous studies have examined the impact of factors such as data volume and model size on English models, the scaling properties of instruction tuning in other languages remain largely unexplored. In this work, we systematically investigate the effects of data quantity, model size, and data construction methods on instruction tuning for Chinese LLMs. We utilize a newly curated dataset, DoIT, which includes over 40,000 high-quality instruction instances covering ten underlying abilities, such as creative writing, code generation, and logical reasoning. Our experiments, conducted on models ranging from 7b to 33b parameters, yield three key findings: (i) While these factors directly affect overall model performance, some abilities are more responsive to scaling, whereas others demonstrate significant resistance. (ii) The scaling sensitivity of different abilities to these factors can be explained by two features: Complexity and Transference. (iii) By tailoring training strategies to their varying sensitivities, specific abilities can be efficiently learned, enhancing performance on two public benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2310.19651v3),  [pdf](http://arxiv.org/pdf/2310.19651v3)

**Tags**: cs.CL 



### Will AI replace Software Engineers? Do not hold your breath
**Authors**: Abhik Roychoudhury, Andreas Zeller

**Updated**: 2025-03-03T07:46:41Z

**Summary**: Artificial Intelligence (AI) technology such as Large Language Models (LLMs) have become extremely popular in creating code. This has led to the conjecture that future software jobs will be exclusively conducted by LLMs, and the software industry will cease to exist. But software engineering is much more than producing code -- notably, \emph{maintaining} large software and keeping it reliable is a major part of software engineering, which LLMs are not yet capable of.

**Link**: [arxiv](http://arxiv.org/abs/2502.20429v2),  [pdf](http://arxiv.org/pdf/2502.20429v2)

**Tags**: cs.SE cs.AI 



### GDTS: Goal-Guided Diffusion Model with Tree Sampling for Multi-Modal   Pedestrian Trajectory Prediction
**Authors**: Ge Sun, Sheng Wang, Lei Zhu, Ming Liu, Jun Ma

**Updated**: 2025-03-03T07:41:00Z

**Summary**: Accurate prediction of pedestrian trajectories is crucial for improving the safety of autonomous driving. However, this task is generally nontrivial due to the inherent stochasticity of human motion, which naturally requires the predictor to generate multi-modal prediction. Previous works leverage various generative methods, such as GAN and VAE, for pedestrian trajectory prediction. Nevertheless, these methods may suffer from mode collapse and relatively low-quality results. The denoising diffusion probabilistic model (DDPM) has recently been applied to trajectory prediction due to its simple training process and powerful reconstruction ability. However, current diffusion-based methods do not fully utilize input information and usually require many denoising iterations that lead to a long inference time or an additional network for initialization. To address these challenges and facilitate the use of diffusion models in multi-modal trajectory prediction, we propose GDTS, a novel Goal-Guided Diffusion Model with Tree Sampling for multi-modal trajectory prediction. Considering the "goal-driven" characteristics of human motion, GDTS leverages goal estimation to guide the generation of the diffusion network. A two-stage tree sampling algorithm is presented, which leverages common features to reduce the inference time and improve accuracy for multi-modal prediction. Experimental results demonstrate that our proposed framework achieves comparable state-of-the-art performance with real-time inference speed in public datasets.

**Link**: [arxiv](http://arxiv.org/abs/2311.14922v3),  [pdf](http://arxiv.org/pdf/2311.14922v3)

**Tags**: cs.CV 



### Selected Languages are All You Need for Cross-lingual Truthfulness   Transfer
**Authors**: Weihao Liu, Ning Wu, Wenbiao Ding, Shining Liang, Ming Gong, Dongmei Zhang

**Updated**: 2025-03-03T07:36:49Z

**Summary**: Truthfulness stands out as an essential challenge for Large Language Models (LLMs). Although many works have developed various ways for truthfulness enhancement, they seldom focus on truthfulness in multilingual scenarios. Meanwhile, contemporary multilingual aligning technologies struggle to balance numerous languages and often exhibit serious truthfulness gaps across different languages, especially those that differ greatly from English. In our work, we extend truthfulness evaluation to multilingual contexts and propose a practical method for cross-lingual truthfulness transfer called Fact-aware Multilingual Selective Synergy (FaMSS). FaMSS is able to select an optimal subset of all tested languages by language bias and transfer contributions, and then employ translation instruction tuning for cross-lingual truthfulness transfer. Experimental results demonstrate that our approach can effectively reduce the multilingual representation disparity and boost cross-lingual truthfulness transfer of LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2406.14434v3),  [pdf](http://arxiv.org/pdf/2406.14434v3)

**Tags**: cs.CL 



### PAPILLON: Efficient and Stealthy Fuzz Testing-Powered Jailbreaks for   LLMs
**Authors**: Xueluan Gong, Mingzhe Li, Yilin Zhang, Fengyuan Ran, Chen Chen, Yanjiao Chen, Qian Wang, Kwok-Yan Lam

**Updated**: 2025-03-03T07:25:21Z

**Summary**: Large Language Models (LLMs) have excelled in various tasks but are still vulnerable to jailbreaking attacks, where attackers create jailbreak prompts to mislead the model to produce harmful or offensive content. Current jailbreak methods either rely heavily on manually crafted templates, which pose challenges in scalability and adaptability, or struggle to generate semantically coherent prompts, making them easy to detect. Additionally, most existing approaches involve lengthy prompts, leading to higher query costs. In this paper, to remedy these challenges, we introduce a novel jailbreaking attack framework called PAPILLON, which is an automated, black-box jailbreaking attack framework that adapts the black-box fuzz testing approach with a series of customized designs. Instead of relying on manually crafted templates,PAPILLON starts with an empty seed pool, removing the need to search for any related jailbreaking templates. We also develop three novel question-dependent mutation strategies using an LLM helper to generate prompts that maintain semantic coherence while significantly reducing their length. Additionally, we implement a two-level judge module to accurately detect genuine successful jailbreaks. We evaluated PAPILLON on 7 representative LLMs and compared it with 5 state-of-the-art jailbreaking attack strategies. For proprietary LLM APIs, such as GPT-3.5 turbo, GPT-4, and Gemini-Pro, PAPILLONs achieves attack success rates of over 90%, 80%, and 74%, respectively, exceeding existing baselines by more than 60\%. Additionally, PAPILLON can maintain high semantic coherence while significantly reducing the length of jailbreak prompts. When targeting GPT-4, PAPILLON can achieve over 78% attack success rate even with 100 tokens. Moreover, PAPILLON demonstrates transferability and is robust to state-of-the-art defenses. Code: https://github.com/aaFrostnova/Papillon

**Link**: [arxiv](http://arxiv.org/abs/2409.14866v5),  [pdf](http://arxiv.org/pdf/2409.14866v5)

**Tags**: cs.CR cs.AI 



### Enabling Auditory Large Language Models for Automatic Speech Quality   Evaluation
**Authors**: Siyin Wang, Wenyi Yu, Yudong Yang, Changli Tang, Yixuan Li, Jimin Zhuang, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Guangzhi Sun, Lu Lu, Chao Zhang

**Updated**: 2025-03-03T07:22:54Z

**Summary**: Speech quality assessment typically requires evaluating audio from multiple aspects, such as mean opinion score (MOS) and speaker similarity (SIM) \etc., which can be challenging to cover using one small model designed for a single task. In this paper, we propose leveraging recently introduced auditory large language models (LLMs) for automatic speech quality assessment. By employing task-specific prompts, auditory LLMs are finetuned to predict MOS, SIM and A/B testing results, which are commonly used for evaluating text-to-speech systems. Additionally, the finetuned auditory LLM is able to generate natural language descriptions assessing aspects like noisiness, distortion, discontinuity, and overall quality, providing more interpretable outputs. Extensive experiments have been performed on the NISQA, BVCC, SOMOS and VoxSim speech quality datasets, using open-source auditory LLMs such as SALMONN, Qwen-Audio, and Qwen2-Audio. For the natural language descriptions task, a commercial model Google Gemini 1.5 Pro is also evaluated. The results demonstrate that auditory LLMs achieve competitive performance compared to state-of-the-art task-specific small models in predicting MOS and SIM, while also delivering promising results in A/B testing and natural language descriptions. Our data processing scripts and finetuned model checkpoints can be found at https://github.com/bytedance/SALMONN.

**Link**: [arxiv](http://arxiv.org/abs/2409.16644v2),  [pdf](http://arxiv.org/pdf/2409.16644v2)

**Tags**: eess.AS cs.CL cs.SD 



### DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of   Daily Life
**Authors**: Yu Ying Chiu, Liwei Jiang, Yejin Choi

**Updated**: 2025-03-03T07:20:54Z

**Summary**: As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DailyDilemmas, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action. Based on these dilemmas, we gather a repository of human values covering diverse everyday topics, such as interpersonal relationships, workplace, and environmental issues. With DailyDilemmas, we evaluate LLMs on these dilemmas to determine what action they will choose and the values represented by these action choices. Then, we analyze values through the lens of five theoretical frameworks inspired by sociology, psychology, and philosophy, including the World Values Survey, Moral Foundations Theory, Maslow's Hierarchy of Needs, Aristotle's Virtues, and Plutchik's Wheel of Emotions. For instance, we find LLMs are most aligned with self-expression over survival in World Values Survey and care over loyalty in Moral Foundations Theory. Interestingly, we find substantial preference differences in models for some core values. For example, for truthfulness, Mixtral-8x7B neglects it by 9.7% while GPT-4-turbo selects it by 9.4%. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their designated principles reflect their models' actual value prioritization when facing nuanced moral reasoning in daily-life settings. Finally, we find that end users cannot effectively steer such prioritization using system prompts.

**Link**: [arxiv](http://arxiv.org/abs/2410.02683v2),  [pdf](http://arxiv.org/pdf/2410.02683v2)

**Tags**: cs.CL cs.AI cs.LG 



### Learning to Align Multi-Faceted Evaluation: A Unified and Robust   Framework
**Authors**: Kaishuai Xu, Tiezheng Yu, Wenjun Hou, Yi Cheng, Liangyou Li, Xin Jiang, Lifeng Shang, Qun Liu, Wenjie Li

**Updated**: 2025-03-03T07:13:12Z

**Summary**: Large Language Models (LLMs) are being used more and more extensively for automated evaluation in various scenarios. Previous studies have attempted to fine-tune open-source LLMs to replicate the evaluation explanations and judgments of powerful proprietary models, such as GPT-4. However, these methods are largely limited to text-based analyses under predefined general criteria, resulting in reduced adaptability for unseen instructions and demonstrating instability in evaluating adherence to quantitative and structural constraints. To address these limitations, we propose a novel evaluation framework, ARJudge, that adaptively formulates evaluation criteria and synthesizes both text-based and code-driven analyses to evaluate LLM responses. ARJudge consists of two components: a fine-tuned Analyzer that generates multi-faceted evaluation analyses and a tuning-free Refiner that combines and refines all analyses to make the final judgment. We construct a Composite Analysis Corpus that integrates tasks for evaluation criteria generation alongside text-based and code-driven analysis generation to train the Analyzer. Our results demonstrate that ARJudge outperforms existing fine-tuned evaluators in effectiveness and robustness. Furthermore, it demonstrates the importance of multi-faceted evaluation and code-driven analyses in enhancing evaluation capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2502.18874v2),  [pdf](http://arxiv.org/pdf/2502.18874v2)

**Tags**: cs.CL cs.AI 



### Subtle Errors Matter: Preference Learning via Error-injected   Self-editing
**Authors**: Kaishuai Xu, Tiezheng Yu, Wenjun Hou, Yi Cheng, Chak Tou Leong, Liangyou Li, Xin Jiang, Lifeng Shang, Qun Liu, Wenjie Li

**Updated**: 2025-03-03T07:09:42Z

**Summary**: Large Language Models (LLMs) have exhibited strong mathematical reasoning prowess, tackling tasks ranging from basic arithmetic to advanced competition-level problems. However, frequently occurring subtle yet critical errors, such as miscalculations or incorrect substitutions, limit the LLMs' full potential. Existing studies to improve mathematical ability typically involve applying preference learning to step-wise solution pairs. Although these methods leverage samples of varying granularity to mitigate reasoning errors, they overlook critical subtle errors. In this work, we propose a novel preference learning framework called eRror-Injected Self-Editing (RISE), which injects predefined subtle errors into pivotal tokens in reasoning or computation steps to construct hard pairs for error mitigation. In detail, RISE uses the LLM itself to edit a small number of tokens in the solution, injecting designed subtle errors. Then, pairs composed of self-edited solutions and their corresponding correct ones, along with pairs of correct and incorrect solutions obtained through sampling, are used together for subtle error-aware DPO training. Compared with other preference learning methods, RISE further refines the training objective without requiring fine-grained sampling or preference annotation. Extensive experiments validate the effectiveness of RISE, with preference learning on Qwen2-7B-Instruct yielding notable improvements of 3.0% on GSM8K and 7.9% on MATH with only 4.5K training samples. Moreover, the effect of error mitigation extends from mathematical reasoning to logical reasoning and code generation.

**Link**: [arxiv](http://arxiv.org/abs/2410.06638v3),  [pdf](http://arxiv.org/pdf/2410.06638v3)

**Tags**: cs.CL cs.AI 



### SheetAgent: Towards A Generalist Agent for Spreadsheet Reasoning and   Manipulation via Large Language Models
**Authors**: Yibin Chen, Yifu Yuan, Zeyu Zhang, Yan Zheng, Jinyi Liu, Fei Ni, Jianye Hao, Hangyu Mao, Fuzheng Zhang

**Updated**: 2025-03-03T06:56:29Z

**Summary**: Spreadsheets are ubiquitous across the World Wide Web, playing a critical role in enhancing work efficiency across various domains. Large language model (LLM) has been recently attempted for automatic spreadsheet manipulation but has not yet been investigated in complicated and realistic tasks where reasoning challenges exist (e.g., long horizon manipulation with multi-step reasoning and ambiguous requirements). To bridge the gap with the real-world requirements, we introduce SheetRM, a benchmark featuring long-horizon and multi-category tasks with reasoning-dependent manipulation caused by real-life challenges. To mitigate the above challenges, we further propose SheetAgent, a novel autonomous agent that utilizes the power of LLMs. SheetAgent consists of three collaborative modules: Planner, Informer, and Retriever, achieving both advanced reasoning and accurate manipulation over spreadsheets without human interaction through iterative task reasoning and reflection. Extensive experiments demonstrate that SheetAgent delivers 20--40\% pass rate improvements on multiple benchmarks over baselines, achieving enhanced precision in spreadsheet manipulation and demonstrating superior table reasoning abilities. More details and visualizations are available at the project website: https://sheetagent.github.io/. The datasets and source code are available at https://anonymous.4open.science/r/SheetAgent.

**Link**: [arxiv](http://arxiv.org/abs/2403.03636v3),  [pdf](http://arxiv.org/pdf/2403.03636v3)

**Tags**: cs.AI cs.LG 



### Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the   ARC Task
**Authors**: Junjie Wu, Mo Yu, Lemao Liu, Dit-Yan Yeung, Jie Zhou

**Updated**: 2025-03-03T06:50:25Z

**Summary**: While LLMs have exhibited strong performance on various NLP tasks, it is noteworthy that most of these tasks rely on utilizing the vast amount of knowledge encoded in LLMs' parameters, rather than solving new problems without prior knowledge. In cognitive research, the latter ability is referred to as fluid intelligence, which is considered to be critical for assessing human intelligence. Recent research on fluid intelligence assessments has highlighted significant deficiencies in LLMs' abilities. In this paper, we analyze the challenges LLMs face in demonstrating fluid intelligence through controlled experiments, using the most representative ARC task as an example. Our study revealed three major limitations in existing LLMs: limited ability for skill composition, unfamiliarity with abstract input formats, and the intrinsic deficiency of left-to-right decoding. Our data and code can be found in https://wujunjie1998.github.io/araoc-benchmark.github.io/.

**Link**: [arxiv](http://arxiv.org/abs/2502.07190v2),  [pdf](http://arxiv.org/pdf/2502.07190v2)

**Tags**: cs.AI 



### SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via   Saliency-based Spiking
**Authors**: Xingrun Xing, Boyan Gao, Zheng Zhang, David A. Clifton, Shitao Xiao, Li Du, Guoqi Li, Jiajun Zhang

**Updated**: 2025-03-03T06:46:33Z

**Summary**: Recent advancements in large language models (LLMs) with billions of parameters have improved performance in various applications, but their inference processes demand significant energy and computational resources. In contrast, the human brain, with approximately 86 billion neurons, is much more energy-efficient than LLMs with similar parameters. Inspired by this, we redesign 7$\sim$70 billion parameter LLMs using bio-plausible spiking mechanisms, emulating the efficient behavior of the human brain. We propose the first spiking large language model, SpikeLLM. Coupled with the proposed model, two essential approaches are proposed to improve spike training efficiency: Generalized Integrate-and-Fire (GIF) neurons to compress spike length from $T$ to $\frac{T}{L} \log_2 L$ bits, and an Optimal Brain Spiking framework to divide outlier channels and allocate different $T$ for GIF neurons, which further compresses spike length to approximate $log_2T$ bits. The necessity of spike-driven LLM is proved by comparison with quantized LLMs with similar operations. In the OmniQuant pipeline, SpikeLLM reduces 11.01% WikiText2 perplexity and improves 2.55% accuracy of common scene reasoning on a LLAMA-7B W4A4 model. In the GPTQ pipeline, SpikeLLM achieves direct additive in linear layers, significantly exceeding PB-LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2407.04752v2),  [pdf](http://arxiv.org/pdf/2407.04752v2)

**Tags**: cs.LG cs.CL cs.NE 



### A Note On Square-free Sequences and Anti-unification Type
**Authors**: David M. Cerna

**Updated**: 2025-03-03T06:46:33Z

**Summary**: Error: Peer-review process exposed an error in Theorem 1 that, unfourtunately, is not repairable. Idempotent semigroups are always finite. See Green and Rees [1952], Siekmann and Szab\'o [1981] for details Anti-unification is a fundamental operation used for inductive inference. It is abstractly defined as a process deriving from a set of symbolic expressions a new symbolic expression possessing certain commonalities shared between its members. We consider anti-unification over term algebras where some function symbols are interpreted as associative-idempotent $(f (x, f (y, z)) = f (f (x, y), z)$ and $f (x, x) = x$, respectively) and show that there exists generalization problems for which a minimal complete set of solutions does not exist (Nullary), that is every complete set must contain comparable elements with respect to the generality relation. In contrast to earlier techniques for showing the nullarity of a generalization problem, we exploit combinatorial properties of complete sets of solutions to show that comparable elements are not avoidable. We show that every complete set of solutions contains an infinite chain of comparable generalizations whose structure is isomorphic to a subsequence of an infinite square-free sequence over three symbols.

**Link**: [arxiv](http://arxiv.org/abs/2412.10307v2),  [pdf](http://arxiv.org/pdf/2412.10307v2)

**Tags**: cs.LO 



### Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight   Quantization of Large Language Models
**Authors**: Jung Hwan Heo, Jeonghoon Kim, Beomseok Kwon, Byeongwook Kim, Se Jung Kwon, Dongsoo Lee

**Updated**: 2025-03-03T06:37:01Z

**Summary**: Large Language Models (LLMs) have recently demonstrated remarkable success across various tasks. However, efficiently serving LLMs has been a challenge due to the large memory bottleneck, specifically in small batch inference settings (e.g. mobile devices). Weight-only quantization can be a promising approach, but sub-4 bit quantization remains a challenge due to large-magnitude activation outliers. To mitigate the undesirable outlier effect, we first propose per-IC quantization, a simple yet effective method that creates quantization groups within each input channel (IC) rather than the conventional per-output-channel (per-OC). Our method is motivated by the observation that activation outliers affect the input dimension of the weight matrix, so similarly grouping the weights in the IC direction can isolate outliers within a group. We also find that activation outliers do not dictate quantization difficulty, and inherent weight sensitivities also exist. With per-IC quantization as a new outlier-friendly scheme, we propose Adaptive Dimensions (AdaDim), a versatile quantization framework that can adapt to various weight sensitivity patterns. We demonstrate the effectiveness of AdaDim by augmenting prior methods such as Round-To-Nearest and GPTQ, showing significant improvements across various language modeling benchmarks for both base (up to +4.7% on MMLU) and instruction-tuned (up to +10% on HumanEval) LLMs. Code is available at https://github.com/johnheo/adadim-llm

**Link**: [arxiv](http://arxiv.org/abs/2309.15531v3),  [pdf](http://arxiv.org/pdf/2309.15531v3)

**Tags**: cs.LG 



### The Rise and Down of Babel Tower: Investigating the Evolution Process of   Multilingual Code Large Language Model
**Authors**: Jiawei Chen, Wentao Chen, Jing Su, Jingjing Xu, Hongyu Lin, Mengjie Ren, Yaojie Lu, Xianpei Han, Le Sun

**Updated**: 2025-03-03T06:33:49Z

**Summary**: Large language models (LLMs) have shown significant multilingual capabilities. However, the mechanisms underlying the development of these capabilities during pre-training are not well understood. In this paper, we use code LLMs as an experimental platform to explore the evolution of multilingual capabilities in LLMs during the pre-training process. Based on our observations, we propose the Babel Tower Hypothesis, which describes the entire process of LLMs acquiring new language capabilities. During the learning process, multiple languages initially share a single knowledge system dominated by the primary language and gradually develop language-specific knowledge systems. We then validate the above hypothesis by tracking the internal states of the LLMs through identifying working languages and language transferring neurons. Experimental results show that the internal state changes of the LLM are consistent with our Babel Tower Hypothesis. Building on these insights, we propose a novel method to construct an optimized pre-training corpus for multilingual code LLMs, which significantly outperforms LLMs trained on the original corpus. The proposed Babel Tower Hypothesis provides new insights into designing pre-training data distributions to achieve optimal multilingual capabilities in LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.07298v2),  [pdf](http://arxiv.org/pdf/2412.07298v2)

**Tags**: cs.CL 



### Order Matters: Investigate the Position Bias in Multi-constraint   Instruction Following
**Authors**: Jie Zeng, Qianyu He, Qingyu Ren, Jiaqing Liang, Yanghua Xiao, Weikang Zhou, Zeye Sun, Fei Yu

**Updated**: 2025-03-03T06:29:31Z

**Summary**: Real-world instructions with multiple constraints pose a significant challenge to existing large language models (LLMs). An observation is that the LLMs exhibit dramatic performance fluctuation when disturbing the order of the incorporated constraints. Yet, none of the existing works has systematically investigated this position bias problem in the field of multi-constraint instruction following. To bridge this gap, we design a probing task where we quantitatively measure the difficulty distribution of the constraints by a novel Difficulty Distribution Index (CDDI). Through the experimental results, we find that LLMs are more performant when presented with the constraints in a ``hard-to-easy'' order. This preference can be generalized to LLMs with different architecture or different sizes of parameters. Additionally, we conduct an explanation study, providing an intuitive insight into the correlation between the LLM's attention and constraint orders. Our code and dataset are publicly available at https://github.com/meowpass/PBIF.

**Link**: [arxiv](http://arxiv.org/abs/2502.17204v2),  [pdf](http://arxiv.org/pdf/2502.17204v2)

**Tags**: cs.CL cs.AI 



### 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary   Affordance Detection in 3D Worlds
**Authors**: Hengshuo Chu, Xiang Deng, Qi Lv, Xiaoyang Chen, Yinchuan Li, Jianye Hao, Liqiang Nie

**Updated**: 2025-03-03T06:21:57Z

**Summary**: 3D Affordance detection is a challenging problem with broad applications on various robotic tasks. Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task. This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene. To address these limitations, we reformulate the traditional affordance detection paradigm into \textit{Instruction Reasoning Affordance Segmentation} (IRAS) task. This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels. We accordingly propose the \textit{3D-AffordanceLLM} (3D-ADLLM), a framework designed for reasoning affordance detection in 3D open-scene. Specifically, 3D-ADLLM introduces large language models (LLMs) to 3D affordance perception with a custom-designed decoder for generating affordance masks, thus achieving open-world reasoning affordance detection. In addition, given the scarcity of 3D affordance datasets for training large models, we seek to extract knowledge from general segmentation data and transfer it to affordance detection. Thus, we propose a multi-stage training strategy that begins with a novel pre-training task, i.e., \textit{Referring Object Part Segmentation}~(ROPS). This stage is designed to equip the model with general recognition and segmentation capabilities at the object-part level. Then followed by fine-tuning with the IRAS task, 3D-ADLLM obtains the reasoning ability for affordance detection. In summary, 3D-ADLLM leverages the rich world knowledge and human-object interaction reasoning ability of LLMs, achieving approximately an 8\% improvement in mIoU on open-vocabulary affordance detection tasks.

**Link**: [arxiv](http://arxiv.org/abs/2502.20041v2),  [pdf](http://arxiv.org/pdf/2502.20041v2)

**Tags**: cs.CV cs.RO 



### TokenSelect: Efficient Long-Context Inference and Length Extrapolation   for LLMs via Dynamic Token-Level KV Cache Selection
**Authors**: Wei Wu, Zhuoshi Pan, Chao Wang, Liyi Chen, Yunchu Bai, Tianfu Wang, Kun Fu, Zheng Wang, Hui Xiong

**Updated**: 2025-03-03T05:49:41Z

**Summary**: The rapid advancement of Large Language Models (LLMs) has driven growing demand for processing extended context sequences in contemporary applications. However, this progress faces two major challenges: performance degradation due to sequence lengths out-of-distribution, and excessively long inference times caused by the quadratic computational complexity of attention. These issues hinder the application of LLMs in long-context scenarios. In this paper, we propose Dynamic Token-Level KV Cache Selection (TokenSelect), a training-free method for efficient and accurate long-context inference. TokenSelect builds upon the observation of non-contiguous attention sparsity, using Query-Key dot products to measure per-head KV Cache criticality at token-level. By per-head soft voting mechanism, TokenSelect selectively involves a few critical KV cache tokens in attention calculation without sacrificing accuracy. To further accelerate TokenSelect, we design the Selection Cache based on observations of consecutive Query similarity and implemented efficient dot product kernel, significantly reducing the overhead. A comprehensive evaluation of TokenSelect demonstrates up to 23.84x speedup in attention computation and up to 2.28x acceleration in end-to-end latency, while providing superior performance compared to state-of-the-art long-context inference methods.

**Link**: [arxiv](http://arxiv.org/abs/2411.02886v2),  [pdf](http://arxiv.org/pdf/2411.02886v2)

**Tags**: cs.CL cs.AI cs.LG 



### Enhancing Conversational Agents with Theory of Mind: Aligning Beliefs,   Desires, and Intentions for Human-Like Interaction
**Authors**: Mehdi Jafari, Devin Yuncheng Hua, Hao Xue, Flora Salim

**Updated**: 2025-03-03T05:44:29Z

**Summary**: Natural language interaction with agentic Artificial Intelligence (AI), driven by Large Language Models (LLMs), is expected to remain a dominant paradigm in the near future. While humans instinctively align their communication with mental states -- an ability known as Theory of Mind (ToM), current LLM powered systems exhibit significant limitations in this regard. This study examines the extent to which open source language models (LLaMA) can capture and preserve ToM related information and how effectively it contributes to consistent ToM reasoning in generated responses. We further investigate whether explicit manipulation of ToM related components, such as beliefs, desires, and intentions, can enhance response alignment. Experiments on two LLaMA 3 variants demonstrate that incorporating ToM informed alignment improves response quality, achieving win rates of 67 and 63 percent for the 3B and 8B models, respectively. These findings highlight the potential of ToM driven strategies to improve alignment in LLM based conversational agents.

**Link**: [arxiv](http://arxiv.org/abs/2502.14171v3),  [pdf](http://arxiv.org/pdf/2502.14171v3)

**Tags**: cs.CL 



### Perturbation-Restrained Sequential Model Editing
**Authors**: Jun-Yu Ma, Hong Wang, Hao-Xiang Xu, Zhen-Hua Ling, Jia-Chen Gu

**Updated**: 2025-03-03T04:25:41Z

**Summary**: Model editing is an emerging field that focuses on updating the knowledge embedded within large language models (LLMs) without extensive retraining. However, current model editing methods significantly compromise the general abilities of LLMs as the number of edits increases, and this trade-off poses a substantial challenge to the continual learning of LLMs. In this paper, we first theoretically analyze that the factor affecting the general abilities in sequential model editing lies in the condition number of the edited matrix. The condition number of a matrix represents its numerical sensitivity, and therefore can be used to indicate the extent to which the original knowledge associations stored in LLMs are perturbed after editing. Subsequently, statistical findings demonstrate that the value of this factor becomes larger as the number of edits increases, thereby exacerbating the deterioration of general abilities. To this end, a framework termed Perturbation Restraint on Upper bouNd for Editing (PRUNE) is proposed, which applies the condition number restraints in sequential editing. These restraints can lower the upper bound on perturbation to edited models, thus preserving the general abilities. Systematically, we conduct experiments employing three editing methods on three LLMs across four downstream tasks. The results show that PRUNE can preserve general abilities while maintaining the editing performance effectively in sequential model editing. The code are available at https://github.com/mjy1111/PRUNE.

**Link**: [arxiv](http://arxiv.org/abs/2405.16821v3),  [pdf](http://arxiv.org/pdf/2405.16821v3)

**Tags**: cs.CL 



### Federated Learning in Practice: Reflections and Projections
**Authors**: Katharine Daly, Hubert Eichner, Peter Kairouz, H. Brendan McMahan, Daniel Ramage, Zheng Xu

**Updated**: 2025-03-03T04:14:17Z

**Summary**: Federated Learning (FL) is a machine learning technique that enables multiple entities to collaboratively learn a shared model without exchanging their local data. Over the past decade, FL systems have achieved substantial progress, scaling to millions of devices across various learning domains while offering meaningful differential privacy (DP) guarantees. Production systems from organizations like Google, Apple, and Meta demonstrate the real-world applicability of FL. However, key challenges remain, including verifying server-side DP guarantees and coordinating training across heterogeneous devices, limiting broader adoption. Additionally, emerging trends such as large (multi-modal) models and blurred lines between training, inference, and personalization challenge traditional FL frameworks. In response, we propose a redefined FL framework that prioritizes privacy principles rather than rigid definitions. We also chart a path forward by leveraging trusted execution environments and open-source ecosystems to address these challenges and facilitate future advancements in FL.

**Link**: [arxiv](http://arxiv.org/abs/2410.08892v2),  [pdf](http://arxiv.org/pdf/2410.08892v2)

**Tags**: cs.LG cs.AI cs.CR 



### A-MEM: Agentic Memory for LLM Agents
**Authors**: Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang

**Updated**: 2025-03-03T04:14:02Z

**Summary**: While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems' fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code is available at https://github.com/WujiangXu/AgenticMemory.

**Link**: [arxiv](http://arxiv.org/abs/2502.12110v2),  [pdf](http://arxiv.org/pdf/2502.12110v2)

**Tags**: cs.CL cs.HC 



### Tuning Timestep-Distilled Diffusion Model Using Pairwise Sample   Optimization
**Authors**: Zichen Miao, Zhengyuan Yang, Kevin Lin, Ze Wang, Zicheng Liu, Lijuan Wang, Qiang Qiu

**Updated**: 2025-03-03T04:11:46Z

**Summary**: Recent advancements in timestep-distilled diffusion models have enabled high-quality image generation that rivals non-distilled multi-step models, but with significantly fewer inference steps. While such models are attractive for applications due to the low inference cost and latency, fine-tuning them with a naive diffusion objective would result in degraded and blurry outputs. An intuitive alternative is to repeat the diffusion distillation process with a fine-tuned teacher model, which produces good results but is cumbersome and computationally intensive; the distillation training usually requires magnitude higher of training compute compared to fine-tuning for specific image styles. In this paper, we present an algorithm named pairwise sample optimization (PSO), which enables the direct fine-tuning of an arbitrary timestep-distilled diffusion model. PSO introduces additional reference images sampled from the current time-step distilled model, and increases the relative likelihood margin between the training images and reference images. This enables the model to retain its few-step generation ability, while allowing for fine-tuning of its output distribution. We also demonstrate that PSO is a generalized formulation which can be flexibly extended to both offline-sampled and online-sampled pairwise data, covering various popular objectives for diffusion model preference optimization. We evaluate PSO in both preference optimization and other fine-tuning tasks, including style transfer and concept customization. We show that PSO can directly adapt distilled models to human-preferred generation with both offline and online-generated pairwise preference image data. PSO also demonstrates effectiveness in style transfer and concept customization by directly tuning timestep-distilled diffusion models.

**Link**: [arxiv](http://arxiv.org/abs/2410.03190v3),  [pdf](http://arxiv.org/pdf/2410.03190v3)

**Tags**: cs.CV 



### QUAD-LLM-MLTC: Large Language Models Ensemble Learning for Healthcare   Text Multi-Label Classification
**Authors**: Hajar Sakai, Sarah S. Lam

**Updated**: 2025-03-03T04:11:31Z

**Summary**: The escalating volume of collected healthcare textual data presents a unique challenge for automated Multi-Label Text Classification (MLTC), which is primarily due to the scarcity of annotated texts for training and their nuanced nature. Traditional machine learning models often fail to fully capture the array of expressed topics. However, Large Language Models (LLMs) have demonstrated remarkable effectiveness across numerous Natural Language Processing (NLP) tasks in various domains, which show impressive computational efficiency and suitability for unsupervised learning through prompt engineering. Consequently, these LLMs promise an effective MLTC of medical narratives. However, when dealing with various labels, different prompts can be relevant depending on the topic. To address these challenges, the proposed approach, QUAD-LLM-MLTC, leverages the strengths of four LLMs: GPT-4o, BERT, PEGASUS, and BART. QUAD-LLM-MLTC operates in a sequential pipeline in which BERT extracts key tokens, PEGASUS augments textual data, GPT-4o classifies, and BART provides topics' assignment probabilities, which results in four classifications, all in a 0-shot setting. The outputs are then combined using ensemble learning and processed through a meta-classifier to produce the final MLTC result. The approach is evaluated using three samples of annotated texts, which contrast it with traditional and single-model methods. The results show significant improvements across the majority of the topics in the classification's F1 score and consistency (F1 and Micro-F1 scores of 78.17% and 80.16% with standard deviations of 0.025 and 0.011, respectively). This research advances MLTC using LLMs and provides an efficient and scalable solution to rapidly categorize healthcare-related text data without further training.

**Link**: [arxiv](http://arxiv.org/abs/2502.14189v2),  [pdf](http://arxiv.org/pdf/2502.14189v2)

**Tags**: cs.CL 



### Compositional simulation-based inference for time series
**Authors**: Manuel Gloeckler, Shoji Toyota, Kenji Fukumizu, Jakob H. Macke

**Updated**: 2025-03-03T04:04:30Z

**Summary**: Amortized simulation-based inference (SBI) methods train neural networks on simulated data to perform Bayesian inference. While this strategy avoids the need for tractable likelihoods, it often requires a large number of simulations and has been challenging to scale to time series data. Scientific simulators frequently emulate real-world dynamics through thousands of single-state transitions over time. We propose an SBI approach that can exploit such Markovian simulators by locally identifying parameters consistent with individual state transitions. We then compose these local results to obtain a posterior over parameters that align with the entire time series observation. We focus on applying this approach to neural posterior score estimation but also show how it can be applied, e.g., to neural likelihood (ratio) estimation. We demonstrate that our approach is more simulation-efficient than directly estimating the global posterior on several synthetic benchmark tasks and simulators used in ecology and epidemiology. Finally, we validate scalability and simulation efficiency of our approach by applying it to a high-dimensional Kolmogorov flow simulator with around one million data dimensions.

**Link**: [arxiv](http://arxiv.org/abs/2411.02728v2),  [pdf](http://arxiv.org/pdf/2411.02728v2)

**Tags**: cs.LG 



### Iterative Nash Policy Optimization: Aligning LLMs with General   Preferences via No-Regret Learning
**Authors**: Yuheng Zhang, Dian Yu, Baolin Peng, Linfeng Song, Ye Tian, Mingyue Huo, Nan Jiang, Haitao Mi, Dong Yu

**Updated**: 2025-03-03T03:41:11Z

**Summary**: Reinforcement Learning with Human Feedback (RLHF) has achieved great success in aligning large language models (LLMs) with human preferences. Prevalent RLHF approaches are reward-based, following the Bradley-Terry (BT) model assumption, which may not fully capture the complexity of human preferences. In this paper, we explore RLHF under a general preference framework and approach it from a game-theoretic perspective. Specifically, we formulate the problem as a two-player game and propose a novel online algorithm, iterative Nash policy optimization (INPO). The key idea is to let the policy play against itself via no-regret learning, thereby approximating the Nash policy. Unlike previous methods, INPO bypasses the need for estimating the expected win rate for individual responses, which typically incurs high computational or annotation costs. Instead, we introduce a new loss objective that is directly minimized over a preference dataset. We provide theoretical analysis for our approach and demonstrate its effectiveness through experiments on various representative benchmarks. With an LLaMA-3-8B-based SFT model, INPO achieves a 42.6% length-controlled win rate on AlpacaEval 2.0 and a 37.8% win rate on Arena-Hard, showing substantial improvement over the state-of-the-art online RLHF algorithms.

**Link**: [arxiv](http://arxiv.org/abs/2407.00617v4),  [pdf](http://arxiv.org/pdf/2407.00617v4)

**Tags**: cs.LG cs.AI cs.CL cs.GT 



### Optimization-based Prompt Injection Attack to LLM-as-a-Judge
**Authors**: Jiawen Shi, Zenghui Yuan, Yinuo Liu, Yue Huang, Pan Zhou, Lichao Sun, Neil Zhenqiang Gong

**Updated**: 2025-03-03T03:36:17Z

**Summary**: LLM-as-a-Judge uses a large language model (LLM) to select the best response from a set of candidates for a given question. LLM-as-a-Judge has many applications such as LLM-powered search, reinforcement learning with AI feedback (RLAIF), and tool selection. In this work, we propose JudgeDeceiver, an optimization-based prompt injection attack to LLM-as-a-Judge. JudgeDeceiver injects a carefully crafted sequence into an attacker-controlled candidate response such that LLM-as-a-Judge selects the candidate response for an attacker-chosen question no matter what other candidate responses are. Specifically, we formulate finding such sequence as an optimization problem and propose a gradient based method to approximately solve it. Our extensive evaluation shows that JudgeDeceive is highly effective, and is much more effective than existing prompt injection attacks that manually craft the injected sequences and jailbreak attacks when extended to our problem. We also show the effectiveness of JudgeDeceiver in three case studies, i.e., LLM-powered search, RLAIF, and tool selection. Moreover, we consider defenses including known-answer detection, perplexity detection, and perplexity windowed detection. Our results show these defenses are insufficient, highlighting the urgent need for developing new defense strategies. Our implementation is available at this repository: https://github.com/ShiJiawenwen/JudgeDeceiver.

**Link**: [arxiv](http://arxiv.org/abs/2403.17710v4),  [pdf](http://arxiv.org/pdf/2403.17710v4)

**Tags**: cs.CR cs.AI 



### Learning to Learn Weight Generation via Trajectory Diffusion
**Authors**: Yunchuan Guan, Yu Liu, Ke Zhou, Zhiqi Shen, Serge Belongie, Jenq-Neng Hwang, Lei Li

**Updated**: 2025-03-03T03:35:00Z

**Summary**: Diffusion-based algorithms have emerged as promising techniques for weight generation, particularly in scenarios like multi-task learning that require frequent weight updates. However, existing solutions suffer from limited cross-task transferability. In addition, they only utilize optimal weights as training samples, ignoring the value of other weights in the optimization process. To address these issues, we propose Lt-Di, which integrates the diffusion algorithm with meta-learning to generate weights for unseen tasks. Furthermore, we extend the vanilla diffusion algorithm into a trajectory diffusion algorithm to utilize other weights along the optimization trajectory. Trajectory diffusion decomposes the entire diffusion chain into multiple shorter ones, improving training and inference efficiency. We analyze the convergence properties of the weight generation paradigm and improve convergence efficiency without additional time overhead. Our experiments demonstrate Lt-Di's higher accuracy while reducing computational overhead across various tasks, including zero-shot and few-shot learning, multi-domain generalization, and large-scale language model fine-tuning.Our code is released at https://anonymous.4open.science/r/Lt-Di-0E51.

**Link**: [arxiv](http://arxiv.org/abs/2502.01117v2),  [pdf](http://arxiv.org/pdf/2502.01117v2)

**Tags**: cs.LG cs.AI cs.CV 



### LLMOPT: Learning to Define and Solve General Optimization Problems from   Scratch
**Authors**: Caigao Jiang, Xiang Shu, Hong Qian, Xingyu Lu, Jun Zhou, Aimin Zhou, Yang Yu

**Updated**: 2025-03-03T03:20:08Z

**Summary**: Optimization problems are prevalent across various scenarios. Formulating and then solving optimization problems described by natural language often requires highly specialized human expertise, which could block the widespread application of optimization-based decision making. To automate problem formulation and solving, leveraging large language models (LLMs) has emerged as a potential way. However, this kind of approach suffers from the issue of optimization generalization. Namely, the accuracy of most current LLM-based methods and the generality of optimization problem types that they can model are still limited. In this paper, we propose a unified learning-based framework called LLMOPT to boost optimization generalization. Starting from the natural language descriptions of optimization problems and a pre-trained LLM, LLMOPT constructs the introduced five-element formulation as a universal model for learning to define diverse optimization problem types. Then, LLMOPT employs the multi-instruction tuning to enhance both problem formalization and solver code generation accuracy and generality. After that, to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors, the model alignment and self-correction mechanism are adopted in LLMOPT. We evaluate the optimization generalization ability of LLMOPT and compared methods across six real-world datasets covering roughly 20 fields such as health, environment, energy and manufacturing, etc. Extensive experiment results show that LLMOPT is able to model various optimization problem types such as linear/nonlinear programming, mixed integer programming, and combinatorial optimization, and achieves a notable 11.08% average solving accuracy improvement compared with the state-of-the-art methods. The code is available at https://github.com/caigaojiang/LLMOPT.

**Link**: [arxiv](http://arxiv.org/abs/2410.13213v2),  [pdf](http://arxiv.org/pdf/2410.13213v2)

**Tags**: cs.AI cs.LG 



### Noise2Score3D:Unsupervised Tweedie's Approach for Point Cloud Denoising
**Authors**: Xiangbin Wei

**Updated**: 2025-03-03T03:09:49Z

**Summary**: Building on recent advances in Bayesian statistics and image denoising, we propose Noise2Score3D, a fully unsupervised framework for point cloud denoising that addresses the critical challenge of limited availability of clean data. Noise2Score3D learns the gradient of the underlying point cloud distribution directly from noisy data, eliminating the need for clean data during training. By leveraging Tweedie's formula, our method performs inference in a single step, avoiding the iterative processes used in existing unsupervised methods, thereby improving both performance and efficiency. Experimental results demonstrate that Noise2Score3D achieves state-of-the-art performance on standard benchmarks, outperforming other unsupervised methods in Chamfer distance and point-to-mesh metrics, and rivaling some supervised approaches. Furthermore, Noise2Score3D demonstrates strong generalization ability beyond training datasets. Additionally, we introduce Total Variation for Point Cloud, a criterion that allows for the estimation of unknown noise parameters, which further enhances the method's versatility and real-world utility.

**Link**: [arxiv](http://arxiv.org/abs/2502.16826v2),  [pdf](http://arxiv.org/pdf/2502.16826v2)

**Tags**: cs.CV 



### On the Generalization and Adaptation Ability of Machine-Generated Text   Detectors in Academic Writing
**Authors**: Yule Liu, Zhiyuan Zhong, Yifan Liao, Zhen Sun, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He

**Updated**: 2025-03-03T03:08:43Z

**Summary**: The rising popularity of large language models (LLMs) has raised concerns about machine-generated text (MGT), particularly in academic settings, where issues like plagiarism and misinformation are prevalent. As a result, developing a highly generalizable and adaptable MGT detection system has become an urgent priority. Given that LLMs are most commonly misused in academic writing, this work investigates the generalization and adaptation capabilities of MGT detectors in three key aspects specific to academic writing: First, we construct MGT-Acedemic, a large-scale dataset comprising over 336M tokens and 749K samples. MGT-Acedemic focuses on academic writing, featuring human-written texts (HWTs) and MGTs across STEM, Humanities, and Social Sciences, paired with an extensible code framework for efficient benchmarking. Second, we benchmark the performance of various detectors for binary classification and attribution tasks in both in-domain and cross-domain settings. This benchmark reveals the often-overlooked challenges of attribution tasks. Third, we introduce a novel attribution task where models have to adapt to new classes over time without (or with very limited) access to prior training data in both few-shot and many-shot scenarios. We implement eight different adapting techniques to improve the performance and highlight the inherent complexity of the task. Our findings provide insights into the generalization and adaptation ability of MGT detectors across diverse scenarios and lay the foundation for building robust, adaptive detection systems. The code framework is available at https://github.com/Y-L-LIU/MGTBench-2.0.

**Link**: [arxiv](http://arxiv.org/abs/2412.17242v3),  [pdf](http://arxiv.org/pdf/2412.17242v3)

**Tags**: cs.AI cs.CL 



### A Pilot Empirical Study on When and How to Use Knowledge Graphs as   Retrieval Augmented Generation
**Authors**: Xujie Yuan, Yongxu Liu, Shimin Di, Shiwen Wu, Libin Zheng, Rui Meng, Lei Chen, Xiaofang Zhou, Jian Yin

**Updated**: 2025-03-03T03:00:59Z

**Summary**: The integration of Knowledge Graphs (KGs) into the Retrieval Augmented Generation (RAG) framework has attracted significant interest, with early studies showing promise in mitigating hallucinations and improving model accuracy. However, a systematic understanding and comparative analysis of the rapidly emerging KG-RAG methods are still lacking. This paper seeks to lay the foundation for systematically answering the question of when and how to use KG-RAG by analyzing their performance in various application scenarios associated with different technical configurations. After outlining the mind map using KG-RAG framework and summarizing its popular pipeline, we conduct a pilot empirical study of KG-RAG works to reimplement and evaluate 6 KG-RAG methods across 7 datasets in diverse scenarios, analyzing the impact of 9 KG-RAG configurations in combination with 17 LLMs. Our results underscore the critical role of appropriate application conditions and optimal configurations of KG-RAG components.

**Link**: [arxiv](http://arxiv.org/abs/2502.20854v2),  [pdf](http://arxiv.org/pdf/2502.20854v2)

**Tags**: cs.AI cs.CL 



### A Closer Look at Machine Unlearning for Large Language Models
**Authors**: Xiaojian Yuan, Tianyu Pang, Chao Du, Kejiang Chen, Weiming Zhang, Min Lin

**Updated**: 2025-03-03T02:45:58Z

**Summary**: Large language models (LLMs) may memorize sensitive or copyrighted content, raising privacy and legal concerns. Due to the high cost of retraining from scratch, researchers attempt to employ machine unlearning to remove specific content from LLMs while preserving the overall performance. In this paper, we discuss several issues in machine unlearning for LLMs and provide our insights on possible approaches. To address the issue of inadequate evaluation of model outputs after unlearning, we introduce three additional metrics to evaluate token diversity, sentence semantics, and factual correctness. We then categorize unlearning methods into untargeted and targeted, and discuss their issues respectively. Specifically, the behavior that untargeted unlearning attempts to approximate is unpredictable and may involve hallucinations, and existing regularization is insufficient for targeted unlearning. To alleviate these issues, we propose using the objective of maximizing entropy (ME) for untargeted unlearning and incorporate answer preservation (AP) loss as regularization for targeted unlearning. Experimental results across three scenarios, i.e., fictitious unlearning, continual unlearning, and real-world unlearning, demonstrate the effectiveness of our approaches. The code is available at https://github.com/sail-sg/closer-look-LLM-unlearning.

**Link**: [arxiv](http://arxiv.org/abs/2410.08109v3),  [pdf](http://arxiv.org/pdf/2410.08109v3)

**Tags**: cs.CL cs.AI cs.LG 



### A Lean Dataset for International Math Olympiad: Small Steps towards   Writing Math Proofs for Hard Problems
**Authors**: Roozbeh Yousefzadeh, Xuenan Cao, Azim Ospanov

**Updated**: 2025-03-03T02:41:10Z

**Summary**: Using AI to write formal proofs for mathematical problems is a challenging task that has seen some advancements in recent years. Automated systems such as Lean can verify the correctness of proofs written in formal language, yet writing the proofs in formal language can be challenging for humans and machines. The miniF2F benchmark has 20 IMO problems in its test set, yet formal proofs are available only for 6 of these problems (3 of which are only written by mathematicians). The model with best accuracy can only prove 2 of these 20 IMO problems, from 1950s and 60s, while its training set is a secret. In this work, we write complete, original formal proofs for the remaining IMO problems in Lean along with 3 extra problems from IMO 2022 and 2023. This effort expands the availability of proof currently in the public domain by creating 5,880 lines of Lean proof. The goal of the paper is to pave the way for developing AI models that can automatically write the formal proofs for all the IMO problems in miniF2F and beyond by providing an evaluation benchmark. In this pursuit, we devise a method to decompose the proofs of these problems into their building blocks, constructing a dataset of 1,329 lemmas with more than 40k lines of Lean code. These lemmas are not trivial, yet they are approachable, providing the opportunity to evaluate and diagnose the failures and successes of AI models. We evaluate the ability of the SOTA LLMs on our dataset and analyze their success and failure modes from different perspectives. Our dataset and code is available at: https://github.com/roozbeh-yz/IMO-Steps.

**Link**: [arxiv](http://arxiv.org/abs/2411.18872v2),  [pdf](http://arxiv.org/pdf/2411.18872v2)

**Tags**: cs.LG 



### Facilitating Multi-turn Function Calling for LLMs via Compositional   Instruction Tuning
**Authors**: Mingyang Chen, Haoze Sun, Tianpeng Li, Fan Yang, Hao Liang, Keer Lu, Bin Cui, Wentao Zhang, Zenan Zhou, Weipeng Chen

**Updated**: 2025-03-03T02:27:02Z

**Summary**: Large Language Models (LLMs) have exhibited significant potential in performing diverse tasks, including the ability to call functions or use external tools to enhance their performance. While current research on function calling by LLMs primarily focuses on single-turn interactions, this paper addresses the overlooked necessity for LLMs to engage in multi-turn function calling--critical for handling compositional, real-world queries that require planning with functions but not only use functions. To facilitate this, we introduce an approach, BUTTON, which generates synthetic compositional instruction tuning data via bottom-up instruction construction and top-down trajectory generation. In the bottom-up phase, we generate simple atomic tasks based on real-world scenarios and build compositional tasks using heuristic strategies based on atomic tasks. Corresponding function definitions are then synthesized for these compositional tasks. The top-down phase features a multi-agent environment where interactions among simulated humans, assistants, and tools are utilized to gather multi-turn function calling trajectories. This approach ensures task compositionality and allows for effective function and trajectory generation by examining atomic tasks within compositional tasks. We produce a dataset BUTTONInstruct comprising 8k data points and demonstrate its effectiveness through extensive experiments across various LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2410.12952v2),  [pdf](http://arxiv.org/pdf/2410.12952v2)

**Tags**: cs.CL 



### AdEval: Alignment-based Dynamic Evaluation to Mitigate Data   Contamination in Large Language Models
**Authors**: Yang Fan

**Updated**: 2025-03-03T02:06:47Z

**Summary**: As Large Language Models (LLMs) are pretrained on massive-scale corpora, the issue of data contamination has become increasingly severe, leading to potential overestimation of model performance during evaluation. To address this, we propose AdEval (Alignment-based Dynamic Evaluation), a dynamic data evaluation method aimed at mitigating the impact of data contamination on evaluation reliability. Experimental results on multiple datasets demonstrate that AdEval effectively reduces the impact of data contamination on evaluation outcomes, enhancing both the fairness and reliability of the evaluation process.

**Link**: [arxiv](http://arxiv.org/abs/2501.13983v3),  [pdf](http://arxiv.org/pdf/2501.13983v3)

**Tags**: cs.CL cs.AI 



### Quantifying Bias due to non-Gaussian Foregrounds in an Optimal   Reconstruction of CMB Lensing and Temperature Power Spectra
**Authors**: M. Doohan, M. Millea, S. Raghunathan, F. Ge, L. Knox, K. Prabhu, C. L. Reichardt, W. L. K. Wu

**Updated**: 2025-03-03T01:56:36Z

**Summary**: We estimate the magnitude of the bias due to non-Gaussian extragalactic foregrounds on the optimal reconstruction of the cosmic microwave background (CMB) lensing potential and temperature power spectra. The reconstruction is performed using a Bayesian inference method known as the marginal unbiased score expansion (MUSE). We apply MUSE to a minimum variance combination of multifrequency maps drawn from the Agora publicly available simulations of the lensed CMB and correlated extragalactic foreground emission. Taking noise levels appropriate to two years of data with the SPT-3G instrument on the South Pole Telescope, we find no statistically significant bias in the MUSE reconstruction when limited to angular multipoles $\ell \leq 3000$. We find a 4.7$\sigma$ bias in the recovered lensing potential power spectrum when smaller scale modes ($\ell \leq 3500$) are included. This work is a first step toward understanding the impact of extragalactic foregrounds on optimal reconstructions of CMB temperature and lensing potential power spectra.

**Link**: [arxiv](http://arxiv.org/abs/2502.20801v2),  [pdf](http://arxiv.org/pdf/2502.20801v2)

**Tags**: astro-ph.CO 



### On Large Language Model Continual Unlearning
**Authors**: Chongyang Gao, Lixu Wang, Kaize Ding, Chenkai Weng, Xiao Wang, Qi Zhu

**Updated**: 2025-03-03T01:21:39Z

**Summary**: While large language models have demonstrated impressive performance across various domains and tasks, their security issues have become increasingly severe. Machine unlearning has emerged as a representative approach for model safety and security by removing the influence of undesired data on the target model. However, these methods do not sufficiently consider that unlearning requests in real-world scenarios are continuously emerging, especially in the context of LLMs, which may lead to accumulated model utility loss that eventually becomes unacceptable. Moreover, existing LLM unlearning methods often ignore previous data access limitations due to privacy concerns and copyright protection. Without previous data, the utility preservation during unlearning is much harder. To overcome these challenges, we propose the OOO framework that includes an Orthogonal low-rank adapter (LoRA) for continually unlearning requested data and an Out-Of-Distribution (OOD) detector to measure the similarity between input and unlearning data. The orthogonal LoRA achieves parameter disentanglement among continual unlearning requests. The OOD detector is trained with a novel contrastive entropy loss and utilizes a glocal-aware scoring mechanism. During inference, our OOO framework can decide whether and to what extent to load the unlearning LoRA based on the OOD detector's predicted similarity between the input and the unlearned knowledge. Notably, OOO's effectiveness does not rely on any retained data. We conducted extensive experiments on OOO and state-of-the-art LLM unlearning methods across three tasks and seven datasets. The results indicate that OOO consistently achieves the best unlearning effectiveness and utility preservation, especially when facing continuous unlearning requests. The source codes can be found at https://github.com/GCYZSL/O3-LLM-UNLEARNING.

**Link**: [arxiv](http://arxiv.org/abs/2407.10223v2),  [pdf](http://arxiv.org/pdf/2407.10223v2)

**Tags**: cs.LG cs.CR 



### The Labyrinth of Links: Navigating the Associative Maze of Multi-modal   LLMs
**Authors**: Hong Li, Nanxi Li, Yuanjie Chen, Jianbin Zhu, Qinlu Guo, Cewu Lu, Yong-Lu Li

**Updated**: 2025-03-03T00:41:36Z

**Summary**: Multi-modal Large Language Models (MLLMs) have exhibited impressive capability. However, recently many deficiencies of MLLMs have been found compared to human intelligence, $\textit{e.g.}$, hallucination. To drive the MLLMs study, the community dedicated efforts to building larger benchmarks with complex tasks. In this paper, we propose benchmarking an essential but usually overlooked intelligence: $\textbf{association}$, a human's basic capability to link observation and prior practice memory. To comprehensively investigate MLLM's performance on the association, we formulate the association task and devise a standard benchmark based on adjective and verb semantic concepts. Instead of costly data annotation and curation, we propose a convenient $\textbf{annotation-free}$ construction method transforming the general dataset for our association tasks. Simultaneously, we devise a rigorous data refinement process to eliminate confusion in the raw dataset. Building on this database, we establish three levels of association tasks: single-step, synchronous, and asynchronous associations. Moreover, we conduct a comprehensive investigation into the MLLMs' zero-shot association capabilities, addressing multiple dimensions, including three distinct memory strategies, both open-source and closed-source MLLMs, cutting-edge Mixture-of-Experts (MoE) models, and the involvement of human experts. Our systematic investigation shows that current open-source MLLMs consistently exhibit poor capability in our association tasks, even the currently state-of-the-art GPT-4V(vision) also has a significant gap compared to humans. We believe our benchmark would pave the way for future MLLM studies. $\textit{Our data and code are available at:}$ https://mvig-rhos.com/llm_inception.

**Link**: [arxiv](http://arxiv.org/abs/2410.01417v2),  [pdf](http://arxiv.org/pdf/2410.01417v2)

**Tags**: cs.CV cs.AI cs.CL cs.LG 



### NL2FOL: Translating Natural Language to First-Order Logic for Logical   Fallacy Detection
**Authors**: Abhinav Lalwani, Tasha Kim, Lovish Chopra, Christopher Hahn, Zhijing Jin, Mrinmaya Sachan

**Updated**: 2025-03-03T00:38:48Z

**Summary**: Translating natural language into formal language such as First-Order Logic (FOL) is a foundational challenge in NLP with wide-ranging applications in automated reasoning, misinformation tracking, and knowledge validation. In this paper, we introduce Natural Language to First-Order Logic (NL2FOL), a framework to autoformalize natural language to FOL step by step using Large Language Models (LLMs). Our approach addresses key challenges in this translation process, including the integration of implicit background knowledge. By leveraging structured representations generated by NL2FOL, we use Satisfiability Modulo Theory (SMT) solvers to reason about the logical validity of natural language statements. We present logical fallacy detection as a case study to evaluate the efficacy of NL2FOL. Being neurosymbolic, our approach also provides interpretable insights into the reasoning process and demonstrates robustness without requiring model fine-tuning or labeled training data. Our framework achieves strong performance on multiple datasets. On the LOGIC dataset, NL2FOL achieves an F1-score of 78%, while generalizing effectively to the LOGICCLIMATE dataset with an F1-score of 80%.

**Link**: [arxiv](http://arxiv.org/abs/2405.02318v2),  [pdf](http://arxiv.org/pdf/2405.02318v2)

**Tags**: cs.CL cs.AI cs.LG cs.LO 



### Covariate-dependent hierarchical Dirichlet processes
**Authors**: Huizi Zhang, Sara Wade, Natalia Bochkina

**Updated**: 2025-03-03T00:30:51Z

**Summary**: Bayesian hierarchical modelling is a natural framework to effectively integrate data and borrow information across groups. In this paper, we delve into problems related to density estimation and identifying clusters across related groups, proposing a Bayesian approach that extends existing approaches in the presence of additional covariate information. To achieve flexibility, our approach is built on ideas from Bayesian nonparametrics, combining the hierarchical Dirichlet process and dependent Dirichlet process. The proposed model is general, accommodating multiple and mixed covariate types through appropriate kernel functions as well as different output types through suitable likelihoods. This extends our ability to discern the relationship between covariates and clusters, while effectively borrowing information across groups. By employing a data augmentation trick, we are able to tackle the intractable normalized weights and construct a Markov chain Monte Carlo (MCMC) algorithm for posterior inference. The utility of the method is illustrated on simulated data and two real data sets on single-cell RNA sequencing (scRNA-seq) and calcium imaging for studying neuronal activity. For scRNA-seq data, we show that the incorporation of cell dynamics facilitates the discovery of cell subgroups. On calcium imaging data, our method identifies meaningful clusters of time frames with similar neural activity, that aligns with the observed behaviour of the mouse.

**Link**: [arxiv](http://arxiv.org/abs/2407.02676v3),  [pdf](http://arxiv.org/pdf/2407.02676v3)

**Tags**: stat.ME 



### Performance Review on LLM for solving leetcode problems
**Authors**: Lun Wang, Chuanqi Shi, Shaoshui Du, Yiyi Tao, Yixian Shen, Hang Zheng, Yanxin Shen, Xinyu Qiu

**Updated**: 2025-03-03T00:24:08Z

**Summary**: This paper presents a comprehensive performance evaluation of Large Language Models (LLMs) in solving programming challenges from Leetcode, a widely used platform for algorithm practice and technical interviews. We began by crawling the Leetcode website to collect a diverse set of problems encompassing various difficulty levels and topics. Using this dataset, we generated solutions with multiple LLMs, including GPT-4 and GPT-3.5-turbo (ChatGPT-turbo). The generated solutions were systematically evaluated for correctness and efficiency. We employed the pass@k metric to assess the success rates within a given number of attempts and analyzed the runtime performance of the solutions. Our results highlight the strengths and limitations of current LLMs [10] in code generation and problem-solving tasks, providing insights into their potential applications and areas for improvement in automated programming assistance.

**Link**: [arxiv](http://arxiv.org/abs/2502.15770v2),  [pdf](http://arxiv.org/pdf/2502.15770v2)

**Tags**: cs.SE cs.AI 



### Machine Learning in Stellar Astronomy: Progress up to 2024
**Authors**: Guangping Li, Zujia Lu, Junzhi Wang, Zhao Wang

**Updated**: 2025-03-03T00:23:37Z

**Summary**: Machine learning (ML) has become a key tool in astronomy, driving advancements in the analysis and interpretation of complex datasets from observations. This article reviews the application of ML techniques in the identification and classification of stellar objects, alongside the inference of their key astrophysical properties. We highlight the role of both supervised and unsupervised ML algorithms, particularly deep learning models, in classifying stars and enhancing our understanding of essential stellar parameters, such as mass, age, and chemical composition. We discuss ML applications in the study of various stellar objects, including binaries, supernovae, dwarfs, young stellar objects, variables, metal-poor, and chemically peculiar stars. Additionally, we examine the role of ML in investigating star-related interstellar medium objects, such as protoplanetary disks, planetary nebulae, cold neutral medium, feedback bubbles, and molecular clouds.

**Link**: [arxiv](http://arxiv.org/abs/2502.15300v2),  [pdf](http://arxiv.org/pdf/2502.15300v2)

**Tags**: astro-ph.SR astro-ph.GA astro-ph.IM 



### Automatically Improving LLM-based Verilog Generation using EDA Tool   Feedback
**Authors**: Jason Blocklove, Shailja Thakur, Benjamin Tan, Hammond Pearce, Siddharth Garg, Ramesh Karri

**Updated**: 2025-03-02T23:43:15Z

**Summary**: Traditionally, digital hardware designs are written in the Verilog hardware description language (HDL) and debugged manually by engineers. This can be time-consuming and error-prone for complex designs. Large Language Models (LLMs) are emerging as a potential tool to help generate fully functioning HDL code, but most works have focused on generation in the single-shot capacity: i.e., run and evaluate, a process that does not leverage debugging and, as such, does not adequately reflect a realistic development process. In this work, we evaluate the ability of LLMs to leverage feedback from electronic design automation (EDA) tools to fix mistakes in their own generated Verilog. To accomplish this, we present an open-source, highly customizable framework, AutoChip, which combines conversational LLMs with the output from Verilog compilers and simulations to iteratively generate and repair Verilog. To determine the success of these LLMs we leverage the VerilogEval benchmark set. We evaluate four state-of-the-art conversational LLMs, focusing on readily accessible commercial models. EDA tool feedback proved to be consistently more effective than zero-shot prompting only with GPT-4o, the most computationally complex model we evaluated. In the best case, we observed a 5.8% increase in the number of successful designs with a 34.2% decrease in cost over the best zero-shot results. Mixing smaller models with this larger model at the end of the feedback iterations resulted in equally as much success as with GPT-4o using feedback, but incurred 41.9% lower cost (corresponding to an overall decrease in cost over zero-shot by 89.6%).

**Link**: [arxiv](http://arxiv.org/abs/2411.11856v2),  [pdf](http://arxiv.org/pdf/2411.11856v2)

**Tags**: cs.AR cs.AI cs.PL 



### Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of   Encoders
**Authors**: Min Shi, Fuxiao Liu, Shihao Wang, Shijia Liao, Subhashree Radhakrishnan, Yilin Zhao, De-An Huang, Hongxu Yin, Karan Sapra, Yaser Yacoob, Humphrey Shi, Bryan Catanzaro, Andrew Tao, Jan Kautz, Zhiding Yu, Guilin Liu

**Updated**: 2025-03-02T23:41:37Z

**Summary**: The ability to accurately interpret complex visual information is a crucial topic of multimodal large language models (MLLMs). Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. A number of recent MLLMs achieve this goal using a mixture of vision encoders. Despite their success, there is a lack of systematic comparisons and detailed ablation studies addressing critical aspects, such as expert selection and the integration of multiple vision experts. This study provides an extensive exploration of the design space for MLLMs using a mixture of vision encoders and resolutions. Our findings reveal several underlying principles common to various existing strategies, leading to a streamlined yet effective design approach. We discover that simply concatenating visual tokens from a set of complementary vision encoders is as effective as more complex mixing architectures or strategies. We additionally introduce Pre-Alignment to bridge the gap between vision-focused encoders and language tokens, enhancing model coherence. The resulting family of MLLMs, Eagle, surpasses other leading open-source models on major MLLM benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2408.15998v2),  [pdf](http://arxiv.org/pdf/2408.15998v2)

**Tags**: cs.CV cs.AI cs.LG cs.RO 



### ActionReasoningBench: Reasoning about Actions with and without   Ramification Constraints
**Authors**: Divij Handa, Pavel Dolin, Shrinidhi Kumbhar, Tran Cao Son, Chitta Baral

**Updated**: 2025-03-02T23:24:43Z

**Summary**: Reasoning about Actions and Change (RAC) has historically played a pivotal role in solving foundational AI problems, such as the frame problem. It has driven advancements in AI fields, such as non-monotonic and commonsense reasoning. RAC remains crucial for AI systems that operate in dynamic environments, engage in interactive scenarios, or rely on commonsense reasoning. Despite substantial advances made by Large Language Models (LLMs) in various AI domains, their performance in RAC remains underexplored. To address this gap, we introduce a new diagnostic benchmark, ActionReasoningBench, which encompasses 8 domains and includes questions for up to 19 action sequences. This benchmark rigorously evaluates LLMs across six key RAC dimensions: Fluent Tracking, State Tracking, Action Executability, Effects of Actions, Numerical RAC, and Composite Questions. LLMs demonstrate average accuracy rates of 73.55%, 65.63%, 58.73%, and 62.38% on the former four dimensions, which are frequently discussed in RAC literature. However, the performance on the latter two dimensions, which introduce complex and novel reasoning questions, the average performance of LLMs is lowered to 33.16% and 51.19%, respectively, reflecting a 17.9% performance decline. We also introduce new ramification constraints to capture the indirect effects of actions, providing deeper insights into RAC challenges. Our evaluation of state-of-the-art LLMs, including both open-source and commercial models, reveals challenges across all RAC dimensions, particularly in handling ramifications, with GPT-4o failing to solve any question and o1-preview achieving a score of only 18.4%.

**Link**: [arxiv](http://arxiv.org/abs/2406.04046v3),  [pdf](http://arxiv.org/pdf/2406.04046v3)

**Tags**: cs.CC cs.AI 



### Model Predictive Inferential Control of Neural State-Space Models for   Autonomous Vehicle Motion Planning
**Authors**: Iman Askari, Ali Vaziri, Xumein Tu, Shen Zeng, Huazhen Fang

**Updated**: 2025-03-02T21:21:36Z

**Summary**: Model predictive control (MPC) has proven useful in enabling safe and optimal motion planning for autonomous vehicles. In this paper, we investigate how to achieve MPC-based motion planning when a neural state-space model represents the vehicle dynamics. As the neural state-space model will lead to highly complex, nonlinear and nonconvex optimization landscapes, mainstream gradient-based MPC methods will be computationally too heavy to be a viable solution. In a departure, we propose the idea of model predictive inferential control (MPIC), which seeks to infer the best control decisions from the control objectives and constraints. Following the idea, we convert the MPC problem for motion planning into a Bayesian state estimation problem. Then, we develop a new particle filtering/smoothing approach to perform the estimation. This approach is implemented as banks of unscented Kalman filters/smoothers and offers high sampling efficiency, fast computation, and estimation accuracy. We evaluate the MPIC approach through a simulation study of autonomous driving in different scenarios, along with an exhaustive comparison with gradient-based MPC. The results show that the MPIC approach has considerable computational efficiency, regardless of complex neural network architectures, and shows the capability to solve large-scale MPC problems for neural state-space models.

**Link**: [arxiv](http://arxiv.org/abs/2310.08045v3),  [pdf](http://arxiv.org/pdf/2310.08045v3)

**Tags**: cs.RO cs.SY eess.SY 



### We Have a Package for You! A Comprehensive Analysis of Package   Hallucinations by Code Generating LLMs
**Authors**: Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala

**Updated**: 2025-03-02T21:03:52Z

**Summary**: The reliance of popular programming languages such as Python and JavaScript on centralized package repositories and open-source software, combined with the emergence of code-generating Large Language Models (LLMs), has created a new type of threat to the software supply chain: package hallucinations. These hallucinations, which arise from fact-conflicting errors when generating code using LLMs, represent a novel form of package confusion attack that poses a critical threat to the integrity of the software supply chain. This paper conducts a rigorous and comprehensive evaluation of package hallucinations across different programming languages, settings, and parameters, exploring how a diverse set of models and configurations affect the likelihood of generating erroneous package recommendations and identifying the root causes of this phenomenon. Using 16 popular LLMs for code generation and two unique prompt datasets, we generate 576,000 code samples in two programming languages that we analyze for package hallucinations. Our findings reveal that that the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat. To overcome this problem, we implement several hallucination mitigation strategies and show that they are able to significantly reduce the number of package hallucinations while maintaining code quality. Our experiments and findings highlight package hallucinations as a persistent and systemic phenomenon while using state-of-the-art LLMs for code generation, and a significant challenge which deserves the research community's urgent attention.

**Link**: [arxiv](http://arxiv.org/abs/2406.10279v3),  [pdf](http://arxiv.org/pdf/2406.10279v3)

**Tags**: cs.SE cs.AI cs.CR cs.LG 



### ALBAR: Adversarial Learning approach to mitigate Biases in Action   Recognition
**Authors**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah

**Updated**: 2025-03-02T20:53:26Z

**Summary**: Bias in machine learning models can lead to unfair decision making, and while it has been well-studied in the image and text domains, it remains underexplored in action recognition. Action recognition models often suffer from background bias (i.e., inferring actions based on background cues) and foreground bias (i.e., relying on subject appearance), which can be detrimental to real-life applications such as autonomous vehicles or assisted living monitoring. While prior approaches have mainly focused on mitigating background bias using specialized augmentations, we thoroughly study both foreground and background bias. We propose ALBAR, a novel adversarial training method that mitigates foreground and background biases without requiring specialized knowledge of the bias attributes. Our framework applies an adversarial cross-entropy loss to the sampled static clip (where all the frames are the same) and aims to make its class probabilities uniform using a proposed entropy maximization loss. Additionally, we introduce a gradient penalty loss for regularization against the debiasing process. We evaluate our method on established background and foreground bias protocols, setting a new state-of-the-art and strongly improving combined debiasing performance by over 12% absolute on HMDB51. Furthermore, we identify an issue of background leakage in the existing UCF101 protocol for bias evaluation which provides a shortcut to predict actions and does not provide an accurate measure of the debiasing capability of a model. We address this issue by proposing more fine-grained segmentation boundaries for the actor, where our method also outperforms existing approaches. Project Page: https://joefioresi718.github.io/ALBAR_webpage/

**Link**: [arxiv](http://arxiv.org/abs/2502.00156v2),  [pdf](http://arxiv.org/pdf/2502.00156v2)

**Tags**: cs.CV cs.CR 



### Inference to the Best Explanation in Large Language Models
**Authors**: Dhairya Dalal, Marco Valentino, André Freitas, Paul Buitelaar

**Updated**: 2025-03-02T20:33:20Z

**Summary**: While Large Language Models (LLMs) have found success in real-world applications, their underlying explanatory process is still poorly understood. This paper proposes IBE-Eval, a framework inspired by philosophical accounts on Inference to the Best Explanation (IBE) to advance the interpretation and evaluation of LLMs' explanations. IBE-Eval estimates the plausibility of natural language explanations through a combination of explicit logical and linguistic features including: consistency, parsimony, coherence, and uncertainty. Extensive experiments are conducted on Causal Question Answering (CQA), where \textit{IBE-Eval} is tasked to select the most plausible causal explanation amongst competing ones generated by LLMs (i.e., GPT 3.5 and Llama 2). The experiments reveal that IBE-Eval can successfully identify the best explanation with up to 77\% accuracy ($\approx 27\%$ above random), improving upon a GPT 3.5-as-a-Judge baseline ($\approx+17\%$) while being intrinsically more efficient and interpretable. Additional analyses suggest that, despite model-specific variances, LLM-generated explanations tend to conform to IBE criteria and that IBE-Eval is significantly correlated with human judgment, opening up opportunities for future development of automated explanation verification tools.

**Link**: [arxiv](http://arxiv.org/abs/2402.10767v2),  [pdf](http://arxiv.org/pdf/2402.10767v2)

**Tags**: cs.CL cs.AI I.2.7 



### $μ$nit Scaling: Simple and Scalable FP8 LLM Training
**Authors**: Saaketh Narayan, Abhay Gupta, Mansheej Paul, Davis Blalock

**Updated**: 2025-03-02T20:16:43Z

**Summary**: Large Language Model training with 8-bit floating point (FP8) formats promises significant efficiency improvements, but reduced numerical precision makes training challenging. It is currently possible to train in FP8 only if one is willing to tune various hyperparameters, reduce model scale, or accept the overhead of computing dynamic scale factors. We demonstrate simple, scalable FP8 training that requires no dynamic scaling factors or special hyperparameters, even at large model sizes. Our method, $\mu$nit Scaling ($\mu$S), also enables simple hyperparameter transfer across model widths, matched numerics across training and inference, and other desirable properties. $\mu$nit Scaling is straightforward to implement, consisting of a set of minimal interventions based on a first-principles analysis of common transformer operations. We validate our method by training models from 1B to 13B parameters, performing all hidden linear layer computations in FP8. We achieve quality equal to higher precision baselines while also training up to 33% faster.

**Link**: [arxiv](http://arxiv.org/abs/2502.05967v2),  [pdf](http://arxiv.org/pdf/2502.05967v2)

**Tags**: cs.LG 



### Lean Copilot: Large Language Models as Copilots for Theorem Proving in   Lean
**Authors**: Peiyang Song, Kaiyu Yang, Anima Anandkumar

**Updated**: 2025-03-02T20:13:11Z

**Summary**: Neural theorem proving combines large language models (LLMs) with proof assistants such as Lean, where the correctness of formal proofs can be rigorously verified, leaving no room for hallucination. With existing neural theorem provers pretrained on a fixed collection of data and offering valuable suggestions at times, it is challenging for them to continually prove novel theorems in a fully autonomous mode, where human insights may be critical. In this paper, we explore LLMs as copilots that assist humans in proving theorems. We introduce Lean Copilot, an general framework for running LLM inference natively in Lean. It enables programmers to build various LLM-based proof automation tools that integrate seamlessly into the workflow of Lean users. Lean users can use our pretrained models or bring their own ones that run either locally (with or without GPUs) or on the cloud. Using Lean Copilot, we build LLM-based tools that suggest proof steps, complete proof goals, and select relevant premises. Experimental results on the Mathematics in Lean textbook demonstrate the effectiveness of our method compared to existing rule-based proof automation in Lean (aesop). When assisting humans, Lean Copilot requires only 2.08 manually-entered proof steps on average (3.86 required by aesop); when automating the theorem proving process, Lean Copilot automates 74.2% proof steps on average, 85% better than aesop (40.1%). We open source all code and artifacts under a permissive MIT license to facilitate further research.

**Link**: [arxiv](http://arxiv.org/abs/2404.12534v2),  [pdf](http://arxiv.org/pdf/2404.12534v2)

**Tags**: cs.AI cs.LG cs.LO stat.ML 



### Bayesian variance change point detection with credible sets
**Authors**: Lorenzo Cappello, Oscar Hernan Madrid Padilla

**Updated**: 2025-03-02T19:51:11Z

**Summary**: This paper introduces a novel Bayesian approach to detect changes in the variance of a Gaussian sequence model, focusing on quantifying the uncertainty in the change point locations and providing a scalable algorithm for inference. Such a measure of uncertainty is necessary when change point methods are deployed in sensitive applications, for example, when one is interested in determining whether an organ is viable for transplant. The key of our proposal is framing the problem as a product of multiple single changes in the scale parameter. We fit the model through an iterative procedure similar to what is done for additive models. The novelty is that each iteration returns a probability distribution on time instances, which captures the uncertainty in the change point location. Leveraging a recent result in the literature, we can show that our proposal is a variational approximation of the exact model posterior distribution. We study the algorithm's convergence and the change point localization rate. Extensive experiments in simulation studies illustrate the performance of our method and the possibility of generalizing it to more complex data-generating mechanisms. We apply the new model to an experiment involving a novel technique to assess the viability of a liver and oceanographic data.

**Link**: [arxiv](http://arxiv.org/abs/2211.14097v3),  [pdf](http://arxiv.org/pdf/2211.14097v3)

**Tags**: stat.ME 



### Inference Scaling for Long-Context Retrieval Augmented Generation
**Authors**: Zhenrui Yue, Honglei Zhuang, Aijun Bai, Kai Hui, Rolf Jagerman, Hansi Zeng, Zhen Qin, Dong Wang, Xuanhui Wang, Michael Bendersky

**Updated**: 2025-03-02T19:44:37Z

**Summary**: The scaling of inference computation has unlocked the potential of long-context large language models (LLMs) across diverse settings. For knowledge-intensive tasks, the increased compute is often allocated to incorporate more external knowledge. However, without effectively utilizing such knowledge, solely expanding context does not always enhance performance. In this work, we investigate inference scaling for retrieval augmented generation (RAG), exploring the combination of multiple strategies beyond simply increasing the quantity of knowledge, including in-context learning and iterative prompting. These strategies provide additional flexibility to scale test-time computation (e.g., by increasing retrieved documents or generation steps), thereby enhancing LLMs' ability to effectively acquire and utilize contextual information. We address two key questions: (1) How does RAG performance benefit from the scaling of inference computation when optimally configured? (2) Can we predict the optimal test-time compute allocation for a given budget by modeling the relationship between RAG performance and inference parameters? Our observations reveal that increasing inference computation leads to nearly linear gains in RAG performance when optimally allocated, a relationship we describe as the inference scaling laws for RAG. Building on this, we further develop the computation allocation model to estimate RAG performance across different inference configurations. The model predicts optimal inference parameters under various computation constraints, which align closely with the experimental results. By applying these optimal configurations, we demonstrate that scaling inference compute on long-context LLMs achieves up to 58.9% gains on benchmark datasets compared to standard RAG.

**Link**: [arxiv](http://arxiv.org/abs/2410.04343v2),  [pdf](http://arxiv.org/pdf/2410.04343v2)

**Tags**: cs.CL 



### SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and   Iterative Refinement
**Authors**: Antonis Antoniades, Albert Örwall, Kexun Zhang, Yuxi Xie, Anirudh Goyal, William Wang

**Updated**: 2025-03-02T19:42:45Z

**Summary**: Software engineers operating in complex and dynamic environments must continuously adapt to evolving requirements, learn iteratively from experience, and reconsider their approaches based on new insights. However, current large language model (LLM)-based software agents often follow linear, sequential processes that prevent backtracking and exploration of alternative solutions, limiting their ability to rethink their strategies when initial approaches prove ineffective. To address these challenges, we propose SWE-Search, a multi-agent framework that integrates Monte Carlo Tree Search (MCTS) with a self-improvement mechanism to enhance software agents' performance on repository-level software tasks. SWE-Search extends traditional MCTS by incorporating a hybrid value function that leverages LLMs for both numerical value estimation and qualitative evaluation. This enables self-feedback loops where agents iteratively refine their strategies based on both quantitative numerical evaluations and qualitative natural language assessments of pursued trajectories. The framework includes a SWE-Agent for adaptive exploration, a Value Agent for iterative feedback, and a Discriminator Agent that facilitates multi-agent debate for collaborative decision-making. Applied to the SWE-bench benchmark, our approach demonstrates a 23% relative improvement in performance across five models compared to standard open-source agents without MCTS. Our analysis reveals how performance scales with increased inference-time compute through deeper search, providing a pathway to improve software agents without requiring larger models or additional training data. This highlights the potential of self-evaluation driven search techniques in complex software engineering environments.

**Link**: [arxiv](http://arxiv.org/abs/2410.20285v5),  [pdf](http://arxiv.org/pdf/2410.20285v5)

**Tags**: cs.AI 



## Keyword: LLM Deployment 
 ### Matryoshka Quantization
**Authors**: Pranav Nair, Puranjay Datta, Jeff Dean, Prateek Jain, Aditya Kusupati

**Updated**: 2025-03-03T17:54:53Z

**Summary**: Quantizing model weights is critical for reducing the communication and inference costs of large models. However, quantizing models -- especially to low precisions like int4 or int2 -- requires a trade-off in model quality; int2, in particular, is known to severely degrade model quality. Consequently, practitioners are often forced to maintain multiple models with different quantization levels or serve a single model that best satisfies the quality-latency trade-off. On the other hand, integer data types, such as int8, inherently possess a nested (Matryoshka) structure where smaller bit-width integers, like int4 or int2, are nested within the most significant bits. Leveraging this insight, in this paper, we propose Matryoshka Quantization (MatQuant), a novel multi-scale quantization technique that alleviates the aforementioned challenge. This technique allows us to train and maintain a single quantized model but serve it with the precision demanded by the deployment. Furthermore, leveraging MatQuant's co-training and co-distillation regularization, int2 precision models extracted by MatQuant outperform standard int2 quantization by up to to 4% and 7% with OmniQuant and QAT as base algorithms respectively. Finally, we demonstrate that by using an extra bit to represent outliers, a model with an effective precision of 2.05-bit gives an additional 6% improvement with OmniQuant as the base algorithm.

**Link**: [arxiv](http://arxiv.org/abs/2502.06786v3),  [pdf](http://arxiv.org/pdf/2502.06786v3)

**Tags**: cs.LG cs.AI 



### Chain of Draft: Thinking Faster by Writing Less
**Authors**: Silei Xu, Wenhao Xie, Lingxiao Zhao, Pengcheng He

**Updated**: 2025-03-03T17:08:21Z

**Summary**: Large Language Models (LLMs) have demonstrated remarkable performance in solving complex reasoning tasks through mechanisms like Chain-of-Thought (CoT) prompting, which emphasizes verbose, step-by-step reasoning. However, humans typically employ a more efficient strategy: drafting concise intermediate thoughts that capture only essential information. In this work, we propose Chain of Draft (CoD), a novel paradigm inspired by human cognitive processes, where LLMs generate minimalistic yet informative intermediate reasoning outputs while solving tasks. By reducing verbosity and focusing on critical insights, CoD matches or surpasses CoT in accuracy while using as little as only 7.6% of the tokens, significantly reducing cost and latency across various reasoning tasks. Our code and data are available at https://github.com/sileix/chain-of-draft.

**Link**: [arxiv](http://arxiv.org/abs/2502.18600v2),  [pdf](http://arxiv.org/pdf/2502.18600v2)

**Tags**: cs.CL I.2.7 



### R1-T1: Fully Incentivizing Translation Capability in LLMs via Reasoning   Learning
**Authors**: Minggui He, Yilun Liu, Shimin Tao, Yuanchang Luo, Hongyong Zeng, Chang Su, Li Zhang, Hongxia Ma, Daimeng Wei, Weibin Meng, Hao Yang, Boxing Chen, Osamu Yoshie

**Updated**: 2025-03-03T16:44:25Z

**Summary**: Despite recent breakthroughs in reasoning-enhanced large language models (LLMs) like DeepSeek-R1, incorporating inference-time reasoning into machine translation (MT), where human translators naturally employ structured, multi-layered reasoning chain-of-thoughts (CoTs), is yet underexplored. Existing methods either design a fixed CoT tailored for a specific MT sub-task (e.g., literature translation), or rely on synthesizing CoTs unaligned with humans, limiting their adaptability to diverse translation scenarios. This paper introduces R1-Translator (R1-T1), a novel framework to achieve inference-time reasoning for general MT via reinforcement learning (RL) with human-aligned CoTs comprising six common patterns. Our approach pioneers three innovations: (1) extending reasoning-based translation beyond MT sub-tasks to six languages and diverse tasks (e.g., legal/medical domain adaptation, idiom resolution); (2) formalizing six expert-curated CoT templates that mirror hybrid human strategies like context-aware paraphrasing and back translation; and (3) enabling self-evolving CoT discovery through RL. Experimental results indicate a steady translation performance improvement in 11 languages and 40 translation directions on Flores-101 test set, especially on the languages unseen from training.

**Link**: [arxiv](http://arxiv.org/abs/2502.19735v2),  [pdf](http://arxiv.org/pdf/2502.19735v2)

**Tags**: cs.CL 



### InductionBench: LLMs Fail in the Simplest Complexity Class
**Authors**: Wenyue Hua, Tyler Wong, Sun Fei, Liangming Pan, Adam Jardine, William Yang Wang

**Updated**: 2025-03-03T16:38:10Z

**Summary**: Large language models (LLMs) have shown remarkable improvements in reasoning and many existing benchmarks have been addressed by models such as o1 and o3 either fully or partially. However, a majority of these benchmarks emphasize deductive reasoning, including mathematical and coding tasks in which rules such as mathematical axioms or programming syntax are clearly defined, based on which LLMs can plan and apply these rules to arrive at a solution. In contrast, inductive reasoning, where one infers the underlying rules from observed data, remains less explored. Such inductive processes lie at the heart of scientific discovery, as they enable researchers to extract general principles from empirical observations. To assess whether LLMs possess this capacity, we introduce InductionBench, a new benchmark designed to evaluate the inductive reasoning ability of LLMs. Our experimental findings reveal that even the most advanced models available struggle to master the simplest complexity classes within the subregular hierarchy of functions, highlighting a notable deficiency in current LLMs' inductive reasoning capabilities. Coda and data are available https://github.com/Wenyueh/inductive_reasoning_benchmark.

**Link**: [arxiv](http://arxiv.org/abs/2502.15823v3),  [pdf](http://arxiv.org/pdf/2502.15823v3)

**Tags**: cs.LG cs.AI cs.CL cs.FL 



### Interference Management Strategies for HAPS-Enabled vHetNets in Urban   Deployments
**Authors**: Afsoon Alidadi Shamsabadi, Animesh Yadav, Halim Yanikomeroglu

**Updated**: 2025-03-03T16:13:10Z

**Summary**: Next-generation wireless networks are evolving towards architectures that integrate terrestrial and non-terrestrial networks (NTN), unitedly known as vertical heterogeneous networks (vHetNets). This integration is vital to address the increasing demand for coverage, capacity, and new services in urban environments. Among NTN platforms, high altitude platform stations (HAPS) play a promising role in future vHetNets due to their strategic positioning in the stratosphere. In HAPS-enabled vHetNets, various tiers can operate within the same frequency band, creating a harmonized-spectrum integrated network. Although this harmonization significantly enhances spectral efficiency, it also introduces challenges, with interference being a primary concern. This paper investigates vHetNets comprising HAPS and terrestrial macro base stations (MBSs) operating in a shared spectrum, where interference becomes a critical issue. The unique constraints of HAPS-enabled vHetNets further complicate the interference management problem. To address these challenges, we explore various strategies to manage interference in HAPS-enabled vHetNets. Accordingly, we discuss centralized and distributed approaches that leverage tools based on mathematical optimization and artificial intelligence (AI) to solve interference management problems. Preliminary numerical evaluations indicate that distributed approaches achieve spectral efficiency comparable to the centralized algorithm, while requiring lower complexity and less reliance on global information.

**Link**: [arxiv](http://arxiv.org/abs/2412.19865v2),  [pdf](http://arxiv.org/pdf/2412.19865v2)

**Tags**: cs.NI 



### Can Knowledge Editing Really Correct Hallucinations?
**Authors**: Baixiang Huang, Canyu Chen, Xiongxiao Xu, Ali Payani, Kai Shu

**Updated**: 2025-03-03T15:37:23Z

**Summary**: Large Language Models (LLMs) suffer from hallucinations, referring to the non-factual information in generated content, despite their superior capacities across tasks. Meanwhile, knowledge editing has been developed as a new popular paradigm to correct erroneous factual knowledge encoded in LLMs with the advantage of avoiding retraining from scratch. However, a common issue of existing evaluation datasets for knowledge editing is that they do not ensure that LLMs actually generate hallucinated answers to the evaluation questions before editing. When LLMs are evaluated on such datasets after being edited by different techniques, it is hard to directly adopt the performance to assess the effectiveness of different knowledge editing methods in correcting hallucinations. Thus, the fundamental question remains insufficiently validated: Can knowledge editing really correct hallucinations in LLMs? We proposed HalluEditBench to holistically benchmark knowledge editing methods in correcting real-world hallucinations. First, we rigorously construct a massive hallucination dataset with 9 domains, 26 topics and more than 6,000 hallucinations. Then, we assess the performance of knowledge editing methods in a holistic way on five dimensions including Efficacy, Generalization, Portability, Locality, and Robustness. Through HalluEditBench, we have provided new insights into the potentials and limitations of different knowledge editing methods in correcting hallucinations, which could inspire future improvements and facilitate progress in the field of knowledge editing.

**Link**: [arxiv](http://arxiv.org/abs/2410.16251v3),  [pdf](http://arxiv.org/pdf/2410.16251v3)

**Tags**: cs.CL 



### Revisiting the Test-Time Scaling of o1-like Models: Do they Truly   Possess Test-Time Scaling Capabilities?
**Authors**: Zhiyuan Zeng, Qinyuan Cheng, Zhangyue Yin, Yunhua Zhou, Xipeng Qiu

**Updated**: 2025-03-03T15:29:43Z

**Summary**: The advent of test-time scaling in large language models (LLMs), exemplified by OpenAI's o1 series, has advanced reasoning capabilities by scaling computational resource allocation during inference. While successors like QwQ, Deepseek-R1 (R1) and LIMO replicate these advancements, whether these models truly possess test-time scaling capabilities remains underexplored. This study found that longer CoTs of these o1-like models do not consistently enhance accuracy; in fact, correct solutions are often shorter than incorrect ones for the same questions. Further investigation shows this phenomenon is closely related to models' self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation. We then compare sequential and parallel scaling strategies on QwQ, R1 and LIMO, finding that parallel scaling achieves better coverage and scalability. Based on these insights, we propose Shortest Majority Vote, a method that combines parallel scaling strategies with CoT length characteristics, significantly improving models' test-time scalability compared to conventional majority voting approaches.

**Link**: [arxiv](http://arxiv.org/abs/2502.12215v2),  [pdf](http://arxiv.org/pdf/2502.12215v2)

**Tags**: cs.LG cs.AI cs.CL 



### StarVid: Enhancing Semantic Alignment in Video Diffusion Models via   Spatial and SynTactic Guided Attention Refocusing
**Authors**: Yuanhang Li, Qi Mao, Lan Chen, Zhen Fang, Lei Tian, Xinyan Xiao, Libiao Jin, Hua Wu

**Updated**: 2025-03-03T15:01:03Z

**Summary**: Recent advances in text-to-video (T2V) generation with diffusion models have garnered significant attention. However, they typically perform well in scenes with a single object and motion, struggling in compositional scenarios with multiple objects and distinct motions to accurately reflect the semantic content of text prompts. To address these challenges, we propose \textbf{StarVid}, a plug-and-play, training-free method that improves semantic alignment between multiple subjects, their motions, and text prompts in T2V models. StarVid first leverages the spatial reasoning capabilities of large language models (LLMs) for two-stage motion trajectory planning based on text prompts. Such trajectories serve as spatial priors, guiding a spatial-aware loss to refocus cross-attention (CA) maps into distinctive regions. Furthermore, we propose a syntax-guided contrastive constraint to strengthen the correlation between the CA maps of verbs and their corresponding nouns, enhancing motion-subject binding. Both qualitative and quantitative evaluations demonstrate that the proposed framework significantly outperforms baseline methods, delivering videos of higher quality with improved semantic consistency.

**Link**: [arxiv](http://arxiv.org/abs/2409.15259v2),  [pdf](http://arxiv.org/pdf/2409.15259v2)

**Tags**: cs.CV cs.AI 



### From Tokens to Words: On the Inner Lexicon of LLMs
**Authors**: Guy Kaplan, Matanel Oren, Yuval Reif, Roy Schwartz

**Updated**: 2025-03-03T14:30:07Z

**Summary**: Natural language is composed of words, but modern large language models (LLMs) process sub-words as input. A natural question raised by this discrepancy is whether LLMs encode words internally, and if so how. We present evidence that LLMs engage in an intrinsic detokenization process, where sub-word sequences are combined into coherent whole-word representations at their last token. Our experiments show that this process primarily takes place within the early and middle layers of the model. We further demonstrate its robustness to arbitrary splits (e.g., "cats" to "ca" and "ts"), typos, and importantly-to out-of-vocabulary words: when feeding the last token internal representations of such words to the model as input, it can "understand" them as the complete word despite never seeing such representations as input during training. Our findings suggest that LLMs maintain a latent vocabulary beyond the tokenizer's scope. These insights provide a practical, finetuning-free application for expanding the vocabulary of pre-trained models. By enabling the addition of new vocabulary words, we reduce input length and inference iterations, which reduces both space and model latency, with little to no loss in model accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2410.05864v4),  [pdf](http://arxiv.org/pdf/2410.05864v4)

**Tags**: cs.CL cs.AI 



### OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews
**Authors**: Maximilian Idahl, Zahra Ahmadi

**Updated**: 2025-03-03T13:58:56Z

**Summary**: We present OpenReviewer, an open-source system for generating high-quality peer reviews of machine learning and AI conference papers. At its core is Llama-OpenReviewer-8B, an 8B parameter language model specifically fine-tuned on 79,000 expert reviews from top conferences. Given a PDF paper submission and review template as input, OpenReviewer extracts the full text, including technical content like equations and tables, and generates a structured review following conference-specific guidelines. Our evaluation on 400 test papers shows that OpenReviewer produces considerably more critical and realistic reviews compared to general-purpose LLMs like GPT-4 and Claude-3.5. While other LLMs tend toward overly positive assessments, OpenReviewer's recommendations closely match the distribution of human reviewer ratings. The system provides authors with rapid, constructive feedback to improve their manuscripts before submission, though it is not intended to replace human peer review. OpenReviewer is available as an online demo and open-source tool.

**Link**: [arxiv](http://arxiv.org/abs/2412.11948v2),  [pdf](http://arxiv.org/pdf/2412.11948v2)

**Tags**: cs.AI 



### CUIfy the XR: An Open-Source Package to Embed LLM-powered Conversational   Agents in XR
**Authors**: Kadir Burak Buldu, Süleyman Özdel, Ka Hei Carrie Lau, Mengdi Wang, Daniel Saad, Sofie Schönborn, Auxane Boch, Enkelejda Kasneci, Efe Bozkir

**Updated**: 2025-03-03T13:41:33Z

**Summary**: Recent developments in computer graphics, machine learning, and sensor technologies enable numerous opportunities for extended reality (XR) setups for everyday life, from skills training to entertainment. With large corporations offering affordable consumer-grade head-mounted displays (HMDs), XR will likely become pervasive, and HMDs will develop as personal devices like smartphones and tablets. However, having intelligent spaces and naturalistic interactions in XR is as important as technological advances so that users grow their engagement in virtual and augmented spaces. To this end, large language model (LLM)--powered non-player characters (NPCs) with speech-to-text (STT) and text-to-speech (TTS) models bring significant advantages over conventional or pre-scripted NPCs for facilitating more natural conversational user interfaces (CUIs) in XR. This paper provides the community with an open-source, customizable, extendable, and privacy-aware Unity package, CUIfy, that facilitates speech-based NPC-user interaction with widely used LLMs, STT, and TTS models. Our package also supports multiple LLM-powered NPCs per environment and minimizes latency between different computational models through streaming to achieve usable interactions between users and NPCs. We publish our source code in the following repository: https://gitlab.lrz.de/hctl/cuify

**Link**: [arxiv](http://arxiv.org/abs/2411.04671v3),  [pdf](http://arxiv.org/pdf/2411.04671v3)

**Tags**: cs.HC cs.AI 



### Towards Better Chain-of-Thought: A Reflection on Effectiveness and   Faithfulness
**Authors**: Jiachun Li, Pengfei Cao, Yubo Chen, Jiexin Xu, Huaijun Li, Xiaojian Jiang, Kang Liu, Jun Zhao

**Updated**: 2025-03-03T13:25:36Z

**Summary**: Chain-of-thought (CoT) prompting demonstrates varying performance under different reasoning tasks. Previous work attempts to evaluate it but falls short in providing an in-depth analysis of patterns that influence the CoT. In this paper, we study the CoT performance from the perspective of effectiveness and faithfulness. For the former, we identify key factors that influence CoT effectiveness on performance improvement, including problem difficulty, information gain, and information flow. For the latter, we interpret the unfaithful CoT issue by conducting a joint analysis of the information interaction among the question, CoT, and answer. The result demonstrates that, when the LLM predicts answers, it can recall correct information missing in the CoT from the question, leading to the problem. Finally, we propose a novel algorithm to mitigate this issue, in which we recall extra information from the question to enhance the CoT generation and evaluate CoTs based on their information gain. Extensive experiments demonstrate that our approach enhances both the faithfulness and effectiveness of CoT.

**Link**: [arxiv](http://arxiv.org/abs/2405.18915v2),  [pdf](http://arxiv.org/pdf/2405.18915v2)

**Tags**: cs.CL cs.AI 



### MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry   Scientific Hypotheses
**Authors**: Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, Dongzhan Zhou

**Updated**: 2025-03-03T13:17:24Z

**Summary**: Scientific discovery contributes largely to human society's prosperity, and recent progress shows that LLMs could potentially catalyze this process. However, it is still unclear whether LLMs can discover novel and valid hypotheses in chemistry. In this work, we investigate this central research question: Can LLMs automatically discover novel and valid chemistry research hypotheses given only a chemistry research background (consisting of a research question and/or a background survey), without limitation on the domain of the research question? After extensive discussions with chemistry experts, we propose an assumption that a majority of chemistry hypotheses can be resulted from a research background and several inspirations. With this key insight, we break the central question into three smaller fundamental questions. In brief, they are: (1) given a background question, whether LLMs can retrieve good inspirations; (2) with background and inspirations, whether LLMs can lead to hypothesis; and (3) whether LLMs can identify good hypotheses to rank them higher. To investigate these questions, we construct a benchmark consisting of 51 chemistry papers published in Nature, Science, or a similar level in 2024 (all papers are only available online since 2024). Every paper is divided by chemistry PhD students into three components: background, inspirations, and hypothesis. The goal is to rediscover the hypothesis, given only the background and a large randomly selected chemistry literature corpus consisting the ground truth inspiration papers, with LLMs trained with data up to 2023. We also develop an LLM-based multi-agent framework that leverages the assumption, consisting of three stages reflecting the three smaller questions. The proposed method can rediscover many hypotheses with very high similarity with the ground truth ones, covering the main innovations.

**Link**: [arxiv](http://arxiv.org/abs/2410.07076v4),  [pdf](http://arxiv.org/pdf/2410.07076v4)

**Tags**: cs.CL cs.AI cs.LG 



### NavRAG: Generating User Demand Instructions for Embodied Navigation   through Retrieval-Augmented LLM
**Authors**: Zihan Wang, Yaohui Zhu, Gim Hee Lee, Yachun Fan

**Updated**: 2025-03-03T12:56:35Z

**Summary**: Vision-and-Language Navigation (VLN) is an essential skill for embodied agents, allowing them to navigate in 3D environments following natural language instructions. High-performance navigation models require a large amount of training data, the high cost of manually annotating data has seriously hindered this field. Therefore, some previous methods translate trajectory videos into step-by-step instructions for expanding data, but such instructions do not match well with users' communication styles that briefly describe destinations or state specific needs. Moreover, local navigation trajectories overlook global context and high-level task planning. To address these issues, we propose NavRAG, a retrieval-augmented generation (RAG) framework that generates user demand instructions for VLN. NavRAG leverages LLM to build a hierarchical scene description tree for 3D scene understanding from global layout to local details, then simulates various user roles with specific demands to retrieve from the scene tree, generating diverse instructions with LLM. We annotate over 2 million navigation instructions across 861 scenes and evaluate the data quality and navigation performance of trained models.

**Link**: [arxiv](http://arxiv.org/abs/2502.11142v2),  [pdf](http://arxiv.org/pdf/2502.11142v2)

**Tags**: cs.AI cs.CL cs.CV 



### Efficient Learning With Sine-Activated Low-rank Matrices
**Authors**: Yiping Ji, Hemanth Saratchandran, Cameron Gordon, Zeyu Zhang, Simon Lucey

**Updated**: 2025-03-03T12:32:47Z

**Summary**: Low-rank decomposition has emerged as a vital tool for enhancing parameter efficiency in neural network architectures, gaining traction across diverse applications in machine learning. These techniques significantly lower the number of parameters, striking a balance between compactness and performance. However, a common challenge has been the compromise between parameter efficiency and the accuracy of the model, where reduced parameters often lead to diminished accuracy compared to their full-rank counterparts. In this work, we propose a novel theoretical framework that integrates a sinusoidal function within the low-rank decomposition process. This approach not only preserves the benefits of the parameter efficiency characteristic of low-rank methods but also increases the decomposition's rank, thereby enhancing model performance. Our method proves to be a plug in enhancement for existing low-rank models, as evidenced by its successful application in Vision Transformers (ViT), Large Language Models (LLMs), Neural Radiance Fields (NeRF) and 3D shape modelling.

**Link**: [arxiv](http://arxiv.org/abs/2403.19243v4),  [pdf](http://arxiv.org/pdf/2403.19243v4)

**Tags**: cs.LG cs.CV cs.NE 



### Speculative Decoding and Beyond: An In-Depth Survey of Techniques
**Authors**: Yunhai Hu, Zining Liu, Zhenyuan Dong, Tianfan Peng, Bradley McDanel, Sai Qian Zhang

**Updated**: 2025-03-03T12:21:14Z

**Summary**: Sequential dependencies present a fundamental bottleneck in deploying large-scale autoregressive models, particularly for real-time applications. While traditional optimization approaches like pruning and quantization often compromise model quality, recent advances in generation-refinement frameworks demonstrate that this trade-off can be significantly mitigated.   This survey presents a comprehensive taxonomy of generation-refinement frameworks, analyzing methods across autoregressive sequence tasks. We categorize methods based on their generation strategies (from simple n-gram prediction to sophisticated draft models) and refinement mechanisms (including single-pass verification and iterative approaches). Through systematic analysis of both algorithmic innovations and system-level implementations, we examine deployment strategies across computing environments and explore applications spanning text, images, and speech generation. This systematic examination of both theoretical frameworks and practical implementations provides a foundation for future research in efficient autoregressive decoding.

**Link**: [arxiv](http://arxiv.org/abs/2502.19732v2),  [pdf](http://arxiv.org/pdf/2502.19732v2)

**Tags**: cs.CL 



### Interpretable Data-Driven Ship Dynamics Model: Enhancing Physics-Based   Motion Prediction with Parameter Optimization
**Authors**: Christos Papandreou, Michail Mathioudakis, Theodoros Stouraitis, Petros Iatropoulos, Antonios Nikitakis, Stavros Paschalakis, Konstantinos Kyriakopoulos

**Updated**: 2025-03-03T11:39:04Z

**Summary**: The deployment of autonomous navigation systems on ships necessitates accurate motion prediction models tailored to individual vessels. Traditional physics-based models, while grounded in hydrodynamic principles, often fail to account for ship-specific behaviors under real-world conditions. Conversely, purely data-driven models offer specificity but lack interpretability and robustness in edge cases. This study proposes a data-driven physics-based model that integrates physics-based equations with data-driven parameter optimization, leveraging the strengths of both approaches to ensure interpretability and adaptability. The model incorporates physics-based components such as 3-DoF dynamics, rudder, and propeller forces, while parameters such as resistance curve and rudder coefficients are optimized using synthetic data. By embedding domain knowledge into the parameter optimization process, the fitted model maintains physical consistency. Validation of the approach is realized with two container ships by comparing, both qualitatively and quantitatively, predictions against ground-truth trajectories. The results demonstrate significant improvements, in predictive accuracy and reliability, of the data-driven physics-based models over baseline physics-based models tuned with traditional marine engineering practices. The fitted models capture ship-specific behaviors in diverse conditions with their predictions being, 51.6% (ship A) and 57.8% (ship B) more accurate, 72.36% (ship A) and 89.67% (ship B) more consistent.

**Link**: [arxiv](http://arxiv.org/abs/2502.18696v2),  [pdf](http://arxiv.org/pdf/2502.18696v2)

**Tags**: eess.SY cs.RO cs.SY 



### Ephemerality meets LiDAR-based Lifelong Mapping
**Authors**: Hyeonjae Gil, Dongjae Lee, Giseop Kim, Ayoung Kim

**Updated**: 2025-03-03T11:16:49Z

**Summary**: Lifelong mapping is crucial for the long-term deployment of robots in dynamic environments. In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-to-end fashion. Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary. Central to our approach is the probabilistic modeling of the world into two-stage $\textit{ephemerality}$, which represent the transiency of points in the map within two different time scales. By leveraging the spatiotemporal context encoded in ephemeralities, ELite can accurately infer transient map elements, maintain a reliable up-to-date static map, and improve robustness in aligning the new data in a more fine-grained manner. Extensive real-world experiments on long-term datasets demonstrate the robustness and effectiveness of our system. The source code is publicly available for the robotics community: https://github.com/dongjae0107/ELite.

**Link**: [arxiv](http://arxiv.org/abs/2502.13452v2),  [pdf](http://arxiv.org/pdf/2502.13452v2)

**Tags**: cs.RO 



### Exploring Iterative Controllable Summarization with Large Language   Models
**Authors**: Sangwon Ryu, Heejin Do, Daehee Kim, Hwanjo Yu, Dongwoo Kim, Yunsu Kim, Gary Geunbae Lee, Jungseul Ok

**Updated**: 2025-03-03T10:35:27Z

**Summary**: Large language models (LLMs) have demonstrated remarkable performance in abstractive summarization tasks. However, their ability to precisely control summary attributes (e.g., length or topic) remains underexplored, limiting their adaptability to specific user preferences. In this paper, we systematically explore the controllability of LLMs. To this end, we revisit summary attribute measurements and introduce iterative evaluation metrics, failure rate and average iteration count to precisely evaluate controllability of LLMs, rather than merely assessing errors. Our findings show that LLMs struggle more with numerical attributes than with linguistic attributes. To address this challenge, we propose a guide-to-explain framework (GTE) for controllable summarization. Our GTE framework enables the model to identify misaligned attributes in the initial draft and guides it in self-explaining errors in the previous output. By allowing the model to reflect on its misalignment, GTE generates well-adjusted summaries that satisfy the desired attributes with robust effectiveness, requiring surprisingly fewer iterations than other iterative approaches.

**Link**: [arxiv](http://arxiv.org/abs/2411.12460v2),  [pdf](http://arxiv.org/pdf/2411.12460v2)

**Tags**: cs.CL cs.AI 



### TRACE: Temporal Grounding Video LLM via Causal Event Modeling
**Authors**: Yongxin Guo, Jingyu Liu, Mingda Li, Qingbin Liu, Xi Chen, Xiaoying Tang

**Updated**: 2025-03-03T10:28:30Z

**Summary**: Video Temporal Grounding (VTG) is a crucial capability for video understanding models and plays a vital role in downstream tasks such as video browsing and editing. To effectively handle various tasks simultaneously and enable zero-shot prediction, there is a growing trend in employing video LLMs for VTG tasks. However, current video LLM-based methods rely exclusively on natural language generation, lacking the ability to model the clear structure inherent in videos, which restricts their effectiveness in tackling VTG tasks. To address this issue, this paper first formally introduces causal event modeling framework, which represents video LLM outputs as sequences of events, and predict the current event using previous events, video inputs, and textural instructions. Each event consists of three components: timestamps, salient scores, and textual captions. We then propose a novel task-interleaved video LLM called TRACE to effectively implement the causal event modeling framework in practice. The TRACE process visual frames, timestamps, salient scores, and text as distinct tasks, employing various encoders and decoding heads for each. Task tokens are arranged in an interleaved sequence according to the causal event modeling framework's formulation. Extensive experiments on various VTG tasks and datasets demonstrate the superior performance of TRACE compared to state-of-the-art video LLMs. Our model and code are available at https://github.com/gyxxyg/TRACE.

**Link**: [arxiv](http://arxiv.org/abs/2410.05643v3),  [pdf](http://arxiv.org/pdf/2410.05643v3)

**Tags**: cs.CV 



### "Nuclear Deployed!": Analyzing Catastrophic Risks in Decision-making of   Autonomous LLM Agents
**Authors**: Rongwu Xu, Xiaojian Li, Shuo Chen, Wei Xu

**Updated**: 2025-03-03T09:45:24Z

**Summary**: Large language models (LLMs) are evolving into autonomous decision-makers, raising concerns about catastrophic risks in high-stakes scenarios, particularly in Chemical, Biological, Radiological and Nuclear (CBRN) domains. Based on the insight that such risks can originate from trade-offs between the agent's Helpful, Harmlessness and Honest (HHH) goals, we build a novel three-stage evaluation framework, which is carefully constructed to effectively and naturally expose such risks. We conduct 14,400 agentic simulations across 12 advanced LLMs, with extensive experiments and analysis. Results reveal that LLM agents can autonomously engage in catastrophic behaviors and deception, without being deliberately induced. Furthermore, stronger reasoning abilities often increase, rather than mitigate, these risks. We also show that these agents can violate instructions and superior commands. On the whole, we empirically prove the existence of catastrophic risks in autonomous LLM agents. We will release our code upon request.

**Link**: [arxiv](http://arxiv.org/abs/2502.11355v2),  [pdf](http://arxiv.org/pdf/2502.11355v2)

**Tags**: cs.CL cs.AI cs.CR cs.CY 



### Attacking Large Language Models with Projected Gradient Descent
**Authors**: Simon Geisler, Tom Wollschläger, M. H. I. Abdalla, Johannes Gasteiger, Stephan Günnemann

**Updated**: 2025-03-03T09:37:27Z

**Summary**: Current LLM alignment methods are readily broken through specifically crafted adversarial prompts. While crafting adversarial prompts using discrete optimization is highly effective, such attacks typically use more than 100,000 LLM calls. This high computational cost makes them unsuitable for, e.g., quantitative analyses and adversarial training. To remedy this, we revisit Projected Gradient Descent (PGD) on the continuously relaxed input prompt. Although previous attempts with ordinary gradient-based attacks largely failed, we show that carefully controlling the error introduced by the continuous relaxation tremendously boosts their efficacy. Our PGD for LLMs is up to one order of magnitude faster than state-of-the-art discrete optimization to achieve the same devastating attack results.

**Link**: [arxiv](http://arxiv.org/abs/2402.09154v2),  [pdf](http://arxiv.org/pdf/2402.09154v2)

**Tags**: cs.LG 



### LaERC-S: Improving LLM-based Emotion Recognition in Conversation with   Speaker Characteristics
**Authors**: Yumeng Fu, Junjie Wu, Zhongjie Wang, Meishan Zhang, Lili Shan, Yulin Wu, Bingquan Li

**Updated**: 2025-03-03T09:36:14Z

**Summary**: Emotion recognition in conversation (ERC), the task of discerning human emotions for each utterance within a conversation, has garnered significant attention in human-computer interaction systems. Previous ERC studies focus on speaker-specific information that predominantly stems from relationships among utterances, which lacks sufficient information around conversations. Recent research in ERC has sought to exploit pre-trained large language models (LLMs) with speaker modelling to comprehend emotional states. Although these methods have achieved encouraging results, the extracted speaker-specific information struggles to indicate emotional dynamics. In this paper, motivated by the fact that speaker characteristics play a crucial role and LLMs have rich world knowledge, we present LaERC-S, a novel framework that stimulates LLMs to explore speaker characteristics involving the mental state and behavior of interlocutors, for accurate emotion predictions. To endow LLMs with this knowledge information, we adopt the two-stage learning to make the models reason speaker characteristics and track the emotion of the speaker in complex conversation scenarios. Extensive experiments on three benchmark datasets demonstrate the superiority of LaERC-S, reaching the new state-of-the-art.

**Link**: [arxiv](http://arxiv.org/abs/2403.07260v2),  [pdf](http://arxiv.org/pdf/2403.07260v2)

**Tags**: cs.CL 



### Enhancing Large Language Models with Pseudo- and Multisource- Knowledge   Graphs for Open-ended Question Answering
**Authors**: Jiaxiang Liu, Tong Zhou, Yubo Chen, Kang Liu, Jun Zhao

**Updated**: 2025-03-03T09:21:11Z

**Summary**: Mitigating the hallucinations of Large Language Models is a crucial task. Although some existing methods employ self-enhancement techniques, they fall short of effectively addressing unknown factual hallucinations. Meanwhile, Knowledge Graph (KG) enhancement approaches fail to address the generalization across different KG sources and the enhancement of open-ended answer questions simultaneously. To tackle these limitations, we propose a framework that combines Pseudo-Graph Generation and Atomic Knowledge Verification (PG\&AKV). Enhancement of open-ended question-answering begins with leveraging the Pseudo-Graph Generation to provide the related knowledge framework. Subsequently, Atomic Knowledge Verification utilizes atomic-level knowledge querying and verification to achieve generalizability under different KG sources. Compared to the baseline, this approach yields a minimum improvement of 11.5 in the ROUGE-L score for open-ended questions. For precise-answered questions, we observe a minimum accuracy improvement of 7.5%. Moreover, PG\&AKV also exhibits generalizability across different KG sources. Utilizing KG different from the question sources, PG\&AKV can even achieve at least a 3.5 % performance improvement. In summary, our results pave the way for enhancing LLMs by incorporating Pseudo- and Multisource-KGs, particularly in the filed of open-ended questions.

**Link**: [arxiv](http://arxiv.org/abs/2402.09911v2),  [pdf](http://arxiv.org/pdf/2402.09911v2)

**Tags**: cs.CL cs.AI 



### ECLeKTic: a Novel Challenge Set for Evaluation of Cross-Lingual   Knowledge Transfer
**Authors**: Omer Goldman, Uri Shaham, Dan Malkin, Sivan Eiger, Avinatan Hassidim, Yossi Matias, Joshua Maynez, Adi Mayrav Gilady, Jason Riesa, Shruti Rijhwani, Laura Rimell, Idan Szpektor, Reut Tsarfaty, Matan Eyal

**Updated**: 2025-03-03T09:11:46Z

**Summary**: To achieve equitable performance across languages, multilingual large language models (LLMs) must be able to abstract knowledge beyond the language in which it was acquired. However, the current literature lacks reliable ways to measure LLMs' capability of cross-lingual knowledge transfer. To that end, we present ECLeKTic, a multilingual closed-book QA (CBQA) dataset that Evaluates Cross-Lingual Knowledge Transfer in a simple, black-box manner. We detected information with uneven coverage across languages by controlling for presence and absence of Wikipedia articles in 12 languages. We generated knowledge-seeking questions in a source language, for which the answer appears in a relevant Wikipedia article and translated them to all other 11 languages, for which the respective Wikipedias lack equivalent articles. Assuming that Wikipedia reflects the prominent knowledge in the LLM's training data, to solve ECLeKTic's CBQA task the model is required to transfer knowledge between languages. Experimenting with 8 LLMs, we show that SOTA models struggle to effectively share knowledge across, languages even if they can predict the answer well for queries in the same language the knowledge was acquired in.

**Link**: [arxiv](http://arxiv.org/abs/2502.21228v2),  [pdf](http://arxiv.org/pdf/2502.21228v2)

**Tags**: cs.CL cs.AI 



### VoCo-LLaMA: Towards Vision Compression with Large Language Models
**Authors**: Xubing Ye, Yukang Gan, Xiaoke Huang, Yixiao Ge, Yansong Tang

**Updated**: 2025-03-03T09:05:52Z

**Summary**: Vision-Language Models (VLMs) have achieved remarkable success in various multi-modal tasks, but they are often bottlenecked by the limited context window and high computational cost of processing high-resolution image inputs and videos. Vision compression can alleviate this problem by reducing the vision token count. Previous approaches compress vision tokens with external modules and force LLMs to understand the compressed ones, leading to visual information loss. However, the LLMs' understanding paradigm of vision tokens is not fully utilised in the compression learning process. We propose VoCo-LLaMA, the first approach to compress vision tokens using LLMs. By introducing Vision Compression tokens during the vision instruction tuning phase and leveraging attention distillation, our method distill how LLMs comprehend vision tokens into their processing of VoCo tokens. VoCo-LLaMA facilitates effective vision compression and improves the computational efficiency during the inference stage. Specifically, our method achieves minimal performance loss with a compression ratio of 576$\times$, resulting in up to 94.8$\%$ fewer FLOPs and 69.6$\%$ acceleration in inference time. Furthermore, through continuous training using time-series compressed token sequences of video frames, VoCo-LLaMA demonstrates the ability to understand temporal correlations, outperforming previous methods on popular video question-answering benchmarks. Our approach presents a promising way to unlock the full potential of VLMs' contextual window, enabling more scalable multi-modal applications. The project page, along with the associated code, can be accessed via https://yxxxb.github.io/VoCo-LLaMA-page/.

**Link**: [arxiv](http://arxiv.org/abs/2406.12275v2),  [pdf](http://arxiv.org/pdf/2406.12275v2)

**Tags**: cs.CV 



### Artemis: Toward Accurate Detection of Server-Side Request Forgeries   through LLM-Assisted Inter-Procedural Path-Sensitive Taint Analysis
**Authors**: Yuchen Ji, Ting Dai, Zhichao Zhou, Yutian Tang, Jingzhu He

**Updated**: 2025-03-03T08:49:07Z

**Summary**: Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP's dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink functions. Second, Artemis constructs both explicit and implicit call graphs to infer functions' relationships. Third, Artemis performs taint analysis based on a set of rules that prevent over-tainting and pauses when SSRF exploitation is impossible. Fourth, Artemis analyzes the compatibility of path conditions to prune false positives. We have implemented a prototype of Artemis and evaluated it on 250 PHP web applications. Artemis reports 207 true vulnerable paths (106 true SSRFs) with 15 false positives. Of the 106 detected SSRFs, 35 are newly found and reported to developers, with 24 confirmed and assigned CVE IDs.

**Link**: [arxiv](http://arxiv.org/abs/2502.21026v2),  [pdf](http://arxiv.org/pdf/2502.21026v2)

**Tags**: cs.CR cs.SE 



### Q-Adapter: Customizing Pre-trained LLMs to New Preferences with   Forgetting Mitigation
**Authors**: Yi-Chen Li, Fuxiang Zhang, Wenjie Qiu, Lei Yuan, Chengxing Jia, Zongzhang Zhang, Yang Yu, Bo An

**Updated**: 2025-03-03T08:48:38Z

**Summary**: Large Language Models (LLMs), trained on a large amount of corpus, have demonstrated remarkable abilities. However, it may not be sufficient to directly apply open-source LLMs like Llama to certain real-world scenarios, since most of them are trained for \emph{general} purposes. Thus, the demands for customizing publicly available LLMs emerge, but are currently under-studied. In this work, we consider customizing pre-trained LLMs with new human preferences. Specifically, the LLM should not only meet the new preference but also preserve its original capabilities after customization. Drawing inspiration from the observation that human preference can be expressed as a reward model, we propose to cast LLM customization as optimizing the sum of two reward functions, one of which (denoted as $r_1$) was used to pre-train the LLM while the other (denoted as $r_2$) characterizes the new human preference. The obstacle here is that both reward functions are unknown, making the application of modern reinforcement learning methods infeasible. Thanks to the residual Q-learning framework, we can restore the customized LLM with the pre-trained LLM and the \emph{residual Q-function} without the reward function $r_1$. Moreover, we find that for a fixed pre-trained LLM, the reward function $r_2$ can be derived from the residual Q-function, enabling us to directly learn the residual Q-function from the new human preference data upon the Bradley-Terry model. We name our method Q-Adapter as it introduces an adapter module to approximate the residual Q-function for customizing the pre-trained LLM towards the new preference. Experiments based on the Llama-3.1 model on the DSP dataset and HH-RLHF dataset illustrate the superior effectiveness of Q-Adapter on both retaining existing knowledge and learning new preferences. Code is available at https://github.com/mansicer/Q-Adapter.

**Link**: [arxiv](http://arxiv.org/abs/2407.03856v4),  [pdf](http://arxiv.org/pdf/2407.03856v4)

**Tags**: cs.LG 



### SURGE: On the Potential of Large Language Models as General-Purpose   Surrogate Code Executors
**Authors**: Bohan Lyu, Siqiao Huang, Zichen Liang

**Updated**: 2025-03-03T08:26:12Z

**Summary**: Neural surrogate models have emerged as powerful and efficient tools in data mining. Meanwhile, large language models (LLMs) have demonstrated remarkable capabilities in code-related tasks. We investigate a novel application: using LLMs as surrogate models for code execution prediction. Given LLMs' unique ability to understand and process diverse programs, they present a promising direction for building general-purpose surrogate models. To systematically investigate this capability, we introduce SURGE, a comprehensive benchmark with $1160$ problems covering $8$ key aspects: multi-language programming tasks, competition-level programming problems, repository-level code analysis, high-cost scientific computing, time-complexity-intensive algorithms, buggy code analysis, programs dependent on specific compilers or execution environments, and formal mathematical proof verification. Through extensive empirical analysis of $21$ open-source and proprietary LLMs, we examine scaling laws, data efficiency, and predictive accuracy. Our findings reveal important insights about the feasibility of LLMs as efficient surrogates for computational processes, with implications for automated software testing, program analysis, and computational resource optimization in data mining applications. Code and dataset are released at https://github.com/Imbernoulli/SURGE.

**Link**: [arxiv](http://arxiv.org/abs/2502.11167v2),  [pdf](http://arxiv.org/pdf/2502.11167v2)

**Tags**: cs.LG cs.CL 



### Inference Scaling Laws: An Empirical Analysis of Compute-Optimal   Inference for Problem-Solving with Language Models
**Authors**: Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang

**Updated**: 2025-03-03T07:53:32Z

**Summary**: While the scaling laws of large language models (LLMs) training have been extensively studied, optimal inference configurations of LLMs remain underexplored. We study inference scaling laws (aka test-time scaling laws) and compute-optimal inference, focusing on the trade-offs between model sizes and generating additional tokens with different inference strategies. As a first step towards understanding and designing compute-optimal inference methods, we studied cost-performance trade-offs for inference strategies such as greedy search, majority voting, best-of-$n$, weighted voting, and two different tree search algorithms, using different model sizes and compute budgets. Our findings suggest that scaling inference compute with inference strategies can be more computationally efficient than scaling model parameters. Additionally, smaller models combined with advanced inference algorithms offer Pareto-optimal trade-offs in cost and performance. For example, the Llemma-7B model, when paired with our novel tree search algorithm, consistently outperforms the Llemma-34B model across all tested inference strategies on the MATH benchmark. We hope these insights contribute to a deeper understanding of inference scaling laws (test-time scaling laws) for LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2408.00724v3),  [pdf](http://arxiv.org/pdf/2408.00724v3)

**Tags**: cs.AI 



### Dynamics of Instruction Fine-Tuning for Chinese Large Language Models
**Authors**: Chiyu Song, Zhanchao Zhou, Jianhao Yan, Yuejiao Fei, Zhenzhong Lan, Yue Zhang

**Updated**: 2025-03-03T07:49:17Z

**Summary**: Instruction tuning is a burgeoning method to elicit the general intelligence of Large Language Models (LLMs). While numerous studies have examined the impact of factors such as data volume and model size on English models, the scaling properties of instruction tuning in other languages remain largely unexplored. In this work, we systematically investigate the effects of data quantity, model size, and data construction methods on instruction tuning for Chinese LLMs. We utilize a newly curated dataset, DoIT, which includes over 40,000 high-quality instruction instances covering ten underlying abilities, such as creative writing, code generation, and logical reasoning. Our experiments, conducted on models ranging from 7b to 33b parameters, yield three key findings: (i) While these factors directly affect overall model performance, some abilities are more responsive to scaling, whereas others demonstrate significant resistance. (ii) The scaling sensitivity of different abilities to these factors can be explained by two features: Complexity and Transference. (iii) By tailoring training strategies to their varying sensitivities, specific abilities can be efficiently learned, enhancing performance on two public benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2310.19651v3),  [pdf](http://arxiv.org/pdf/2310.19651v3)

**Tags**: cs.CL 



### Will AI replace Software Engineers? Do not hold your breath
**Authors**: Abhik Roychoudhury, Andreas Zeller

**Updated**: 2025-03-03T07:46:41Z

**Summary**: Artificial Intelligence (AI) technology such as Large Language Models (LLMs) have become extremely popular in creating code. This has led to the conjecture that future software jobs will be exclusively conducted by LLMs, and the software industry will cease to exist. But software engineering is much more than producing code -- notably, \emph{maintaining} large software and keeping it reliable is a major part of software engineering, which LLMs are not yet capable of.

**Link**: [arxiv](http://arxiv.org/abs/2502.20429v2),  [pdf](http://arxiv.org/pdf/2502.20429v2)

**Tags**: cs.SE cs.AI 



### Selected Languages are All You Need for Cross-lingual Truthfulness   Transfer
**Authors**: Weihao Liu, Ning Wu, Wenbiao Ding, Shining Liang, Ming Gong, Dongmei Zhang

**Updated**: 2025-03-03T07:36:49Z

**Summary**: Truthfulness stands out as an essential challenge for Large Language Models (LLMs). Although many works have developed various ways for truthfulness enhancement, they seldom focus on truthfulness in multilingual scenarios. Meanwhile, contemporary multilingual aligning technologies struggle to balance numerous languages and often exhibit serious truthfulness gaps across different languages, especially those that differ greatly from English. In our work, we extend truthfulness evaluation to multilingual contexts and propose a practical method for cross-lingual truthfulness transfer called Fact-aware Multilingual Selective Synergy (FaMSS). FaMSS is able to select an optimal subset of all tested languages by language bias and transfer contributions, and then employ translation instruction tuning for cross-lingual truthfulness transfer. Experimental results demonstrate that our approach can effectively reduce the multilingual representation disparity and boost cross-lingual truthfulness transfer of LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2406.14434v3),  [pdf](http://arxiv.org/pdf/2406.14434v3)

**Tags**: cs.CL 



### X5G: An Open, Programmable, Multi-vendor, End-to-end, Private 5G O-RAN   Testbed with NVIDIA ARC and OpenAirInterface
**Authors**: Davide Villa, Imran Khan, Florian Kaltenberger, Nicholas Hedberg, Rúben Soares da Silva, Stefano Maxenti, Leonardo Bonati, Anupa Kelkar, Chris Dick, Eduardo Baena, Josep M. Jornet, Tommaso Melodia, Michele Polese, Dimitrios Koutsonikolas

**Updated**: 2025-03-03T07:32:11Z

**Summary**: As Fifth generation (5G) cellular systems transition to softwarized, programmable, and intelligent networks, it becomes fundamental to enable public and private 5G deployments that are (i) primarily based on software components while (ii) maintaining or exceeding the performance of traditional monolithic systems and (iii) enabling programmability through bespoke configurations and optimized deployments. This requires hardware acceleration to scale the Physical (PHY) layer performance, programmable elements in the Radio Access Network (RAN) and intelligent controllers at the edge, careful planning of the Radio Frequency (RF) environment, as well as end-to-end integration and testing. In this paper, we describe how we developed the programmable X5G testbed, addressing these challenges through the deployment of the first 8-node network based on the integration of NVIDIA Aerial RAN CoLab Over-the-Air (ARC-OTA), OpenAirInterface (OAI), and a near-real-time RAN Intelligent Controller (RIC). The Aerial Software Development Kit (SDK) provides the PHY layer, accelerated on Graphics Processing Unit (GPU), with the higher layers from the OAI open-source project interfaced with the PHY through the Small Cell Forum (SCF) Functional Application Platform Interface (FAPI). An E2 agent provides connectivity to the O-RAN Software Community (OSC) near-real-time RIC. We discuss software integration, network infrastructure, and a digital twin framework for RF planning. We then profile the performance with up to 4 Commercial Off-the-Shelf (COTS) smartphones for each base station with iPerf and video streaming applications, as well as up to 25 emulated User Equipments (UEs), measuring a cell rate higher than 1.65 Gbps in downlink and 143 Mbps in uplink.

**Link**: [arxiv](http://arxiv.org/abs/2406.15935v2),  [pdf](http://arxiv.org/pdf/2406.15935v2)

**Tags**: cs.NI 



### PAPILLON: Efficient and Stealthy Fuzz Testing-Powered Jailbreaks for   LLMs
**Authors**: Xueluan Gong, Mingzhe Li, Yilin Zhang, Fengyuan Ran, Chen Chen, Yanjiao Chen, Qian Wang, Kwok-Yan Lam

**Updated**: 2025-03-03T07:25:21Z

**Summary**: Large Language Models (LLMs) have excelled in various tasks but are still vulnerable to jailbreaking attacks, where attackers create jailbreak prompts to mislead the model to produce harmful or offensive content. Current jailbreak methods either rely heavily on manually crafted templates, which pose challenges in scalability and adaptability, or struggle to generate semantically coherent prompts, making them easy to detect. Additionally, most existing approaches involve lengthy prompts, leading to higher query costs. In this paper, to remedy these challenges, we introduce a novel jailbreaking attack framework called PAPILLON, which is an automated, black-box jailbreaking attack framework that adapts the black-box fuzz testing approach with a series of customized designs. Instead of relying on manually crafted templates,PAPILLON starts with an empty seed pool, removing the need to search for any related jailbreaking templates. We also develop three novel question-dependent mutation strategies using an LLM helper to generate prompts that maintain semantic coherence while significantly reducing their length. Additionally, we implement a two-level judge module to accurately detect genuine successful jailbreaks. We evaluated PAPILLON on 7 representative LLMs and compared it with 5 state-of-the-art jailbreaking attack strategies. For proprietary LLM APIs, such as GPT-3.5 turbo, GPT-4, and Gemini-Pro, PAPILLONs achieves attack success rates of over 90%, 80%, and 74%, respectively, exceeding existing baselines by more than 60\%. Additionally, PAPILLON can maintain high semantic coherence while significantly reducing the length of jailbreak prompts. When targeting GPT-4, PAPILLON can achieve over 78% attack success rate even with 100 tokens. Moreover, PAPILLON demonstrates transferability and is robust to state-of-the-art defenses. Code: https://github.com/aaFrostnova/Papillon

**Link**: [arxiv](http://arxiv.org/abs/2409.14866v5),  [pdf](http://arxiv.org/pdf/2409.14866v5)

**Tags**: cs.CR cs.AI 



### Enabling Auditory Large Language Models for Automatic Speech Quality   Evaluation
**Authors**: Siyin Wang, Wenyi Yu, Yudong Yang, Changli Tang, Yixuan Li, Jimin Zhuang, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Guangzhi Sun, Lu Lu, Chao Zhang

**Updated**: 2025-03-03T07:22:54Z

**Summary**: Speech quality assessment typically requires evaluating audio from multiple aspects, such as mean opinion score (MOS) and speaker similarity (SIM) \etc., which can be challenging to cover using one small model designed for a single task. In this paper, we propose leveraging recently introduced auditory large language models (LLMs) for automatic speech quality assessment. By employing task-specific prompts, auditory LLMs are finetuned to predict MOS, SIM and A/B testing results, which are commonly used for evaluating text-to-speech systems. Additionally, the finetuned auditory LLM is able to generate natural language descriptions assessing aspects like noisiness, distortion, discontinuity, and overall quality, providing more interpretable outputs. Extensive experiments have been performed on the NISQA, BVCC, SOMOS and VoxSim speech quality datasets, using open-source auditory LLMs such as SALMONN, Qwen-Audio, and Qwen2-Audio. For the natural language descriptions task, a commercial model Google Gemini 1.5 Pro is also evaluated. The results demonstrate that auditory LLMs achieve competitive performance compared to state-of-the-art task-specific small models in predicting MOS and SIM, while also delivering promising results in A/B testing and natural language descriptions. Our data processing scripts and finetuned model checkpoints can be found at https://github.com/bytedance/SALMONN.

**Link**: [arxiv](http://arxiv.org/abs/2409.16644v2),  [pdf](http://arxiv.org/pdf/2409.16644v2)

**Tags**: eess.AS cs.CL cs.SD 



### DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of   Daily Life
**Authors**: Yu Ying Chiu, Liwei Jiang, Yejin Choi

**Updated**: 2025-03-03T07:20:54Z

**Summary**: As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DailyDilemmas, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action. Based on these dilemmas, we gather a repository of human values covering diverse everyday topics, such as interpersonal relationships, workplace, and environmental issues. With DailyDilemmas, we evaluate LLMs on these dilemmas to determine what action they will choose and the values represented by these action choices. Then, we analyze values through the lens of five theoretical frameworks inspired by sociology, psychology, and philosophy, including the World Values Survey, Moral Foundations Theory, Maslow's Hierarchy of Needs, Aristotle's Virtues, and Plutchik's Wheel of Emotions. For instance, we find LLMs are most aligned with self-expression over survival in World Values Survey and care over loyalty in Moral Foundations Theory. Interestingly, we find substantial preference differences in models for some core values. For example, for truthfulness, Mixtral-8x7B neglects it by 9.7% while GPT-4-turbo selects it by 9.4%. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their designated principles reflect their models' actual value prioritization when facing nuanced moral reasoning in daily-life settings. Finally, we find that end users cannot effectively steer such prioritization using system prompts.

**Link**: [arxiv](http://arxiv.org/abs/2410.02683v2),  [pdf](http://arxiv.org/pdf/2410.02683v2)

**Tags**: cs.CL cs.AI cs.LG 



### Learning to Align Multi-Faceted Evaluation: A Unified and Robust   Framework
**Authors**: Kaishuai Xu, Tiezheng Yu, Wenjun Hou, Yi Cheng, Liangyou Li, Xin Jiang, Lifeng Shang, Qun Liu, Wenjie Li

**Updated**: 2025-03-03T07:13:12Z

**Summary**: Large Language Models (LLMs) are being used more and more extensively for automated evaluation in various scenarios. Previous studies have attempted to fine-tune open-source LLMs to replicate the evaluation explanations and judgments of powerful proprietary models, such as GPT-4. However, these methods are largely limited to text-based analyses under predefined general criteria, resulting in reduced adaptability for unseen instructions and demonstrating instability in evaluating adherence to quantitative and structural constraints. To address these limitations, we propose a novel evaluation framework, ARJudge, that adaptively formulates evaluation criteria and synthesizes both text-based and code-driven analyses to evaluate LLM responses. ARJudge consists of two components: a fine-tuned Analyzer that generates multi-faceted evaluation analyses and a tuning-free Refiner that combines and refines all analyses to make the final judgment. We construct a Composite Analysis Corpus that integrates tasks for evaluation criteria generation alongside text-based and code-driven analysis generation to train the Analyzer. Our results demonstrate that ARJudge outperforms existing fine-tuned evaluators in effectiveness and robustness. Furthermore, it demonstrates the importance of multi-faceted evaluation and code-driven analyses in enhancing evaluation capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2502.18874v2),  [pdf](http://arxiv.org/pdf/2502.18874v2)

**Tags**: cs.CL cs.AI 



### Subtle Errors Matter: Preference Learning via Error-injected   Self-editing
**Authors**: Kaishuai Xu, Tiezheng Yu, Wenjun Hou, Yi Cheng, Chak Tou Leong, Liangyou Li, Xin Jiang, Lifeng Shang, Qun Liu, Wenjie Li

**Updated**: 2025-03-03T07:09:42Z

**Summary**: Large Language Models (LLMs) have exhibited strong mathematical reasoning prowess, tackling tasks ranging from basic arithmetic to advanced competition-level problems. However, frequently occurring subtle yet critical errors, such as miscalculations or incorrect substitutions, limit the LLMs' full potential. Existing studies to improve mathematical ability typically involve applying preference learning to step-wise solution pairs. Although these methods leverage samples of varying granularity to mitigate reasoning errors, they overlook critical subtle errors. In this work, we propose a novel preference learning framework called eRror-Injected Self-Editing (RISE), which injects predefined subtle errors into pivotal tokens in reasoning or computation steps to construct hard pairs for error mitigation. In detail, RISE uses the LLM itself to edit a small number of tokens in the solution, injecting designed subtle errors. Then, pairs composed of self-edited solutions and their corresponding correct ones, along with pairs of correct and incorrect solutions obtained through sampling, are used together for subtle error-aware DPO training. Compared with other preference learning methods, RISE further refines the training objective without requiring fine-grained sampling or preference annotation. Extensive experiments validate the effectiveness of RISE, with preference learning on Qwen2-7B-Instruct yielding notable improvements of 3.0% on GSM8K and 7.9% on MATH with only 4.5K training samples. Moreover, the effect of error mitigation extends from mathematical reasoning to logical reasoning and code generation.

**Link**: [arxiv](http://arxiv.org/abs/2410.06638v3),  [pdf](http://arxiv.org/pdf/2410.06638v3)

**Tags**: cs.CL cs.AI 



### SheetAgent: Towards A Generalist Agent for Spreadsheet Reasoning and   Manipulation via Large Language Models
**Authors**: Yibin Chen, Yifu Yuan, Zeyu Zhang, Yan Zheng, Jinyi Liu, Fei Ni, Jianye Hao, Hangyu Mao, Fuzheng Zhang

**Updated**: 2025-03-03T06:56:29Z

**Summary**: Spreadsheets are ubiquitous across the World Wide Web, playing a critical role in enhancing work efficiency across various domains. Large language model (LLM) has been recently attempted for automatic spreadsheet manipulation but has not yet been investigated in complicated and realistic tasks where reasoning challenges exist (e.g., long horizon manipulation with multi-step reasoning and ambiguous requirements). To bridge the gap with the real-world requirements, we introduce SheetRM, a benchmark featuring long-horizon and multi-category tasks with reasoning-dependent manipulation caused by real-life challenges. To mitigate the above challenges, we further propose SheetAgent, a novel autonomous agent that utilizes the power of LLMs. SheetAgent consists of three collaborative modules: Planner, Informer, and Retriever, achieving both advanced reasoning and accurate manipulation over spreadsheets without human interaction through iterative task reasoning and reflection. Extensive experiments demonstrate that SheetAgent delivers 20--40\% pass rate improvements on multiple benchmarks over baselines, achieving enhanced precision in spreadsheet manipulation and demonstrating superior table reasoning abilities. More details and visualizations are available at the project website: https://sheetagent.github.io/. The datasets and source code are available at https://anonymous.4open.science/r/SheetAgent.

**Link**: [arxiv](http://arxiv.org/abs/2403.03636v3),  [pdf](http://arxiv.org/pdf/2403.03636v3)

**Tags**: cs.AI cs.LG 



### Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the   ARC Task
**Authors**: Junjie Wu, Mo Yu, Lemao Liu, Dit-Yan Yeung, Jie Zhou

**Updated**: 2025-03-03T06:50:25Z

**Summary**: While LLMs have exhibited strong performance on various NLP tasks, it is noteworthy that most of these tasks rely on utilizing the vast amount of knowledge encoded in LLMs' parameters, rather than solving new problems without prior knowledge. In cognitive research, the latter ability is referred to as fluid intelligence, which is considered to be critical for assessing human intelligence. Recent research on fluid intelligence assessments has highlighted significant deficiencies in LLMs' abilities. In this paper, we analyze the challenges LLMs face in demonstrating fluid intelligence through controlled experiments, using the most representative ARC task as an example. Our study revealed three major limitations in existing LLMs: limited ability for skill composition, unfamiliarity with abstract input formats, and the intrinsic deficiency of left-to-right decoding. Our data and code can be found in https://wujunjie1998.github.io/araoc-benchmark.github.io/.

**Link**: [arxiv](http://arxiv.org/abs/2502.07190v2),  [pdf](http://arxiv.org/pdf/2502.07190v2)

**Tags**: cs.AI 



### SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via   Saliency-based Spiking
**Authors**: Xingrun Xing, Boyan Gao, Zheng Zhang, David A. Clifton, Shitao Xiao, Li Du, Guoqi Li, Jiajun Zhang

**Updated**: 2025-03-03T06:46:33Z

**Summary**: Recent advancements in large language models (LLMs) with billions of parameters have improved performance in various applications, but their inference processes demand significant energy and computational resources. In contrast, the human brain, with approximately 86 billion neurons, is much more energy-efficient than LLMs with similar parameters. Inspired by this, we redesign 7$\sim$70 billion parameter LLMs using bio-plausible spiking mechanisms, emulating the efficient behavior of the human brain. We propose the first spiking large language model, SpikeLLM. Coupled with the proposed model, two essential approaches are proposed to improve spike training efficiency: Generalized Integrate-and-Fire (GIF) neurons to compress spike length from $T$ to $\frac{T}{L} \log_2 L$ bits, and an Optimal Brain Spiking framework to divide outlier channels and allocate different $T$ for GIF neurons, which further compresses spike length to approximate $log_2T$ bits. The necessity of spike-driven LLM is proved by comparison with quantized LLMs with similar operations. In the OmniQuant pipeline, SpikeLLM reduces 11.01% WikiText2 perplexity and improves 2.55% accuracy of common scene reasoning on a LLAMA-7B W4A4 model. In the GPTQ pipeline, SpikeLLM achieves direct additive in linear layers, significantly exceeding PB-LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2407.04752v2),  [pdf](http://arxiv.org/pdf/2407.04752v2)

**Tags**: cs.LG cs.CL cs.NE 



### Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight   Quantization of Large Language Models
**Authors**: Jung Hwan Heo, Jeonghoon Kim, Beomseok Kwon, Byeongwook Kim, Se Jung Kwon, Dongsoo Lee

**Updated**: 2025-03-03T06:37:01Z

**Summary**: Large Language Models (LLMs) have recently demonstrated remarkable success across various tasks. However, efficiently serving LLMs has been a challenge due to the large memory bottleneck, specifically in small batch inference settings (e.g. mobile devices). Weight-only quantization can be a promising approach, but sub-4 bit quantization remains a challenge due to large-magnitude activation outliers. To mitigate the undesirable outlier effect, we first propose per-IC quantization, a simple yet effective method that creates quantization groups within each input channel (IC) rather than the conventional per-output-channel (per-OC). Our method is motivated by the observation that activation outliers affect the input dimension of the weight matrix, so similarly grouping the weights in the IC direction can isolate outliers within a group. We also find that activation outliers do not dictate quantization difficulty, and inherent weight sensitivities also exist. With per-IC quantization as a new outlier-friendly scheme, we propose Adaptive Dimensions (AdaDim), a versatile quantization framework that can adapt to various weight sensitivity patterns. We demonstrate the effectiveness of AdaDim by augmenting prior methods such as Round-To-Nearest and GPTQ, showing significant improvements across various language modeling benchmarks for both base (up to +4.7% on MMLU) and instruction-tuned (up to +10% on HumanEval) LLMs. Code is available at https://github.com/johnheo/adadim-llm

**Link**: [arxiv](http://arxiv.org/abs/2309.15531v3),  [pdf](http://arxiv.org/pdf/2309.15531v3)

**Tags**: cs.LG 



### Cross-Spectral Vision Transformer for Biometric Authentication using   Forehead Subcutaneous Vein Pattern and Periocular Pattern
**Authors**: Arun K. Sharma, Shubhobrata Bhattacharya, Motahar Reza, Bishakh Bhattacharya

**Updated**: 2025-03-03T06:34:25Z

**Summary**: Traditional biometric systems have encountered significant setbacks due to various unavoidable factors, for example, face recognition-based biometrics fails due to the wearing of face masks and fingerprints create hygiene concerns. This paper proposes a novel lightweight cross-spectral vision transformer (CS-ViT) for biometric authentication using forehead subcutaneous vein patterns and periocular patterns, offering a promising alternative to traditional methods, capable of performing well even with the face masks and without any physical touch. The proposed framework comprises a cross-spectral dual-channel architecture designed to handle two distinct biometric traits and to capture inter-dependencies in terms of relative spectral patterns. Each channel consists of a Phase-Only Correlation Cross-Spectral Attention (POC-CSA) that captures their individual as well as correlated patterns. The computation of cross-spectral attention using POC extracts the phase correlation in the spatial features. Therefore, it is robust against the resolution/intensity variations and illumination of the input images, assuming both biometric traits are from the same person. The lightweight model is suitable for edge device deployment. The performance of the proposed algorithm was rigorously evaluated using the Forehead Subcutaneous Vein Pattern and Periocular Biometric Pattern (FSVP-PBP) database. The results demonstrated the superiority of the algorithm over state-of-the-art methods, achieving a remarkable classification accuracy of 98.8% with the combined vein and periocular patterns.

**Link**: [arxiv](http://arxiv.org/abs/2412.19160v2),  [pdf](http://arxiv.org/pdf/2412.19160v2)

**Tags**: cs.CV cs.AI cs.LG 



### The Rise and Down of Babel Tower: Investigating the Evolution Process of   Multilingual Code Large Language Model
**Authors**: Jiawei Chen, Wentao Chen, Jing Su, Jingjing Xu, Hongyu Lin, Mengjie Ren, Yaojie Lu, Xianpei Han, Le Sun

**Updated**: 2025-03-03T06:33:49Z

**Summary**: Large language models (LLMs) have shown significant multilingual capabilities. However, the mechanisms underlying the development of these capabilities during pre-training are not well understood. In this paper, we use code LLMs as an experimental platform to explore the evolution of multilingual capabilities in LLMs during the pre-training process. Based on our observations, we propose the Babel Tower Hypothesis, which describes the entire process of LLMs acquiring new language capabilities. During the learning process, multiple languages initially share a single knowledge system dominated by the primary language and gradually develop language-specific knowledge systems. We then validate the above hypothesis by tracking the internal states of the LLMs through identifying working languages and language transferring neurons. Experimental results show that the internal state changes of the LLM are consistent with our Babel Tower Hypothesis. Building on these insights, we propose a novel method to construct an optimized pre-training corpus for multilingual code LLMs, which significantly outperforms LLMs trained on the original corpus. The proposed Babel Tower Hypothesis provides new insights into designing pre-training data distributions to achieve optimal multilingual capabilities in LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.07298v2),  [pdf](http://arxiv.org/pdf/2412.07298v2)

**Tags**: cs.CL 



### Order Matters: Investigate the Position Bias in Multi-constraint   Instruction Following
**Authors**: Jie Zeng, Qianyu He, Qingyu Ren, Jiaqing Liang, Yanghua Xiao, Weikang Zhou, Zeye Sun, Fei Yu

**Updated**: 2025-03-03T06:29:31Z

**Summary**: Real-world instructions with multiple constraints pose a significant challenge to existing large language models (LLMs). An observation is that the LLMs exhibit dramatic performance fluctuation when disturbing the order of the incorporated constraints. Yet, none of the existing works has systematically investigated this position bias problem in the field of multi-constraint instruction following. To bridge this gap, we design a probing task where we quantitatively measure the difficulty distribution of the constraints by a novel Difficulty Distribution Index (CDDI). Through the experimental results, we find that LLMs are more performant when presented with the constraints in a ``hard-to-easy'' order. This preference can be generalized to LLMs with different architecture or different sizes of parameters. Additionally, we conduct an explanation study, providing an intuitive insight into the correlation between the LLM's attention and constraint orders. Our code and dataset are publicly available at https://github.com/meowpass/PBIF.

**Link**: [arxiv](http://arxiv.org/abs/2502.17204v2),  [pdf](http://arxiv.org/pdf/2502.17204v2)

**Tags**: cs.CL cs.AI 



### 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary   Affordance Detection in 3D Worlds
**Authors**: Hengshuo Chu, Xiang Deng, Qi Lv, Xiaoyang Chen, Yinchuan Li, Jianye Hao, Liqiang Nie

**Updated**: 2025-03-03T06:21:57Z

**Summary**: 3D Affordance detection is a challenging problem with broad applications on various robotic tasks. Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task. This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene. To address these limitations, we reformulate the traditional affordance detection paradigm into \textit{Instruction Reasoning Affordance Segmentation} (IRAS) task. This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels. We accordingly propose the \textit{3D-AffordanceLLM} (3D-ADLLM), a framework designed for reasoning affordance detection in 3D open-scene. Specifically, 3D-ADLLM introduces large language models (LLMs) to 3D affordance perception with a custom-designed decoder for generating affordance masks, thus achieving open-world reasoning affordance detection. In addition, given the scarcity of 3D affordance datasets for training large models, we seek to extract knowledge from general segmentation data and transfer it to affordance detection. Thus, we propose a multi-stage training strategy that begins with a novel pre-training task, i.e., \textit{Referring Object Part Segmentation}~(ROPS). This stage is designed to equip the model with general recognition and segmentation capabilities at the object-part level. Then followed by fine-tuning with the IRAS task, 3D-ADLLM obtains the reasoning ability for affordance detection. In summary, 3D-ADLLM leverages the rich world knowledge and human-object interaction reasoning ability of LLMs, achieving approximately an 8\% improvement in mIoU on open-vocabulary affordance detection tasks.

**Link**: [arxiv](http://arxiv.org/abs/2502.20041v2),  [pdf](http://arxiv.org/pdf/2502.20041v2)

**Tags**: cs.CV cs.RO 



### TokenSelect: Efficient Long-Context Inference and Length Extrapolation   for LLMs via Dynamic Token-Level KV Cache Selection
**Authors**: Wei Wu, Zhuoshi Pan, Chao Wang, Liyi Chen, Yunchu Bai, Tianfu Wang, Kun Fu, Zheng Wang, Hui Xiong

**Updated**: 2025-03-03T05:49:41Z

**Summary**: The rapid advancement of Large Language Models (LLMs) has driven growing demand for processing extended context sequences in contemporary applications. However, this progress faces two major challenges: performance degradation due to sequence lengths out-of-distribution, and excessively long inference times caused by the quadratic computational complexity of attention. These issues hinder the application of LLMs in long-context scenarios. In this paper, we propose Dynamic Token-Level KV Cache Selection (TokenSelect), a training-free method for efficient and accurate long-context inference. TokenSelect builds upon the observation of non-contiguous attention sparsity, using Query-Key dot products to measure per-head KV Cache criticality at token-level. By per-head soft voting mechanism, TokenSelect selectively involves a few critical KV cache tokens in attention calculation without sacrificing accuracy. To further accelerate TokenSelect, we design the Selection Cache based on observations of consecutive Query similarity and implemented efficient dot product kernel, significantly reducing the overhead. A comprehensive evaluation of TokenSelect demonstrates up to 23.84x speedup in attention computation and up to 2.28x acceleration in end-to-end latency, while providing superior performance compared to state-of-the-art long-context inference methods.

**Link**: [arxiv](http://arxiv.org/abs/2411.02886v2),  [pdf](http://arxiv.org/pdf/2411.02886v2)

**Tags**: cs.CL cs.AI cs.LG 



### Enhancing Conversational Agents with Theory of Mind: Aligning Beliefs,   Desires, and Intentions for Human-Like Interaction
**Authors**: Mehdi Jafari, Devin Yuncheng Hua, Hao Xue, Flora Salim

**Updated**: 2025-03-03T05:44:29Z

**Summary**: Natural language interaction with agentic Artificial Intelligence (AI), driven by Large Language Models (LLMs), is expected to remain a dominant paradigm in the near future. While humans instinctively align their communication with mental states -- an ability known as Theory of Mind (ToM), current LLM powered systems exhibit significant limitations in this regard. This study examines the extent to which open source language models (LLaMA) can capture and preserve ToM related information and how effectively it contributes to consistent ToM reasoning in generated responses. We further investigate whether explicit manipulation of ToM related components, such as beliefs, desires, and intentions, can enhance response alignment. Experiments on two LLaMA 3 variants demonstrate that incorporating ToM informed alignment improves response quality, achieving win rates of 67 and 63 percent for the 3B and 8B models, respectively. These findings highlight the potential of ToM driven strategies to improve alignment in LLM based conversational agents.

**Link**: [arxiv](http://arxiv.org/abs/2502.14171v3),  [pdf](http://arxiv.org/pdf/2502.14171v3)

**Tags**: cs.CL 



### Perturbation-Restrained Sequential Model Editing
**Authors**: Jun-Yu Ma, Hong Wang, Hao-Xiang Xu, Zhen-Hua Ling, Jia-Chen Gu

**Updated**: 2025-03-03T04:25:41Z

**Summary**: Model editing is an emerging field that focuses on updating the knowledge embedded within large language models (LLMs) without extensive retraining. However, current model editing methods significantly compromise the general abilities of LLMs as the number of edits increases, and this trade-off poses a substantial challenge to the continual learning of LLMs. In this paper, we first theoretically analyze that the factor affecting the general abilities in sequential model editing lies in the condition number of the edited matrix. The condition number of a matrix represents its numerical sensitivity, and therefore can be used to indicate the extent to which the original knowledge associations stored in LLMs are perturbed after editing. Subsequently, statistical findings demonstrate that the value of this factor becomes larger as the number of edits increases, thereby exacerbating the deterioration of general abilities. To this end, a framework termed Perturbation Restraint on Upper bouNd for Editing (PRUNE) is proposed, which applies the condition number restraints in sequential editing. These restraints can lower the upper bound on perturbation to edited models, thus preserving the general abilities. Systematically, we conduct experiments employing three editing methods on three LLMs across four downstream tasks. The results show that PRUNE can preserve general abilities while maintaining the editing performance effectively in sequential model editing. The code are available at https://github.com/mjy1111/PRUNE.

**Link**: [arxiv](http://arxiv.org/abs/2405.16821v3),  [pdf](http://arxiv.org/pdf/2405.16821v3)

**Tags**: cs.CL 



### A-MEM: Agentic Memory for LLM Agents
**Authors**: Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang

**Updated**: 2025-03-03T04:14:02Z

**Summary**: While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems' fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code is available at https://github.com/WujiangXu/AgenticMemory.

**Link**: [arxiv](http://arxiv.org/abs/2502.12110v2),  [pdf](http://arxiv.org/pdf/2502.12110v2)

**Tags**: cs.CL cs.HC 



### QUAD-LLM-MLTC: Large Language Models Ensemble Learning for Healthcare   Text Multi-Label Classification
**Authors**: Hajar Sakai, Sarah S. Lam

**Updated**: 2025-03-03T04:11:31Z

**Summary**: The escalating volume of collected healthcare textual data presents a unique challenge for automated Multi-Label Text Classification (MLTC), which is primarily due to the scarcity of annotated texts for training and their nuanced nature. Traditional machine learning models often fail to fully capture the array of expressed topics. However, Large Language Models (LLMs) have demonstrated remarkable effectiveness across numerous Natural Language Processing (NLP) tasks in various domains, which show impressive computational efficiency and suitability for unsupervised learning through prompt engineering. Consequently, these LLMs promise an effective MLTC of medical narratives. However, when dealing with various labels, different prompts can be relevant depending on the topic. To address these challenges, the proposed approach, QUAD-LLM-MLTC, leverages the strengths of four LLMs: GPT-4o, BERT, PEGASUS, and BART. QUAD-LLM-MLTC operates in a sequential pipeline in which BERT extracts key tokens, PEGASUS augments textual data, GPT-4o classifies, and BART provides topics' assignment probabilities, which results in four classifications, all in a 0-shot setting. The outputs are then combined using ensemble learning and processed through a meta-classifier to produce the final MLTC result. The approach is evaluated using three samples of annotated texts, which contrast it with traditional and single-model methods. The results show significant improvements across the majority of the topics in the classification's F1 score and consistency (F1 and Micro-F1 scores of 78.17% and 80.16% with standard deviations of 0.025 and 0.011, respectively). This research advances MLTC using LLMs and provides an efficient and scalable solution to rapidly categorize healthcare-related text data without further training.

**Link**: [arxiv](http://arxiv.org/abs/2502.14189v2),  [pdf](http://arxiv.org/pdf/2502.14189v2)

**Tags**: cs.CL 



### Within-Dataset Disclosure Risk for Differential Privacy
**Authors**: Zhiru Zhu, Raul Castro Fernandez

**Updated**: 2025-03-03T03:45:05Z

**Summary**: Differential privacy (DP) enables private data analysis. In a typical DP deployment, controllers manage individuals' sensitive data and are responsible for answering analysts' queries while protecting individuals' privacy. They do so by choosing the privacy parameter $\epsilon$, which controls the degree of privacy for all individuals in all possible datasets. However, it is challenging for controllers to choose $\epsilon$ because of the difficulty of interpreting the privacy implications of such a choice on the within-dataset individuals.   To address this challenge, we first derive a relative disclosure risk indicator (RDR) that indicates the impact of choosing $\epsilon$ on the within-dataset individuals' disclosure risk. We then design an algorithm to find $\epsilon$ based on controllers' privacy preferences expressed as a function of the within-dataset individuals' RDRs, and an alternative algorithm that finds and releases $\epsilon$ while satisfying DP. Lastly, we propose a solution that bounds the total privacy leakage when using the algorithm to answer multiple queries without requiring controllers to set the total privacy budget. We evaluate our contributions through an IRB-approved user study that shows the RDR is useful for helping controllers choose $\epsilon$, and experimental evaluations showing our algorithms are efficient and scalable.

**Link**: [arxiv](http://arxiv.org/abs/2310.13104v4),  [pdf](http://arxiv.org/pdf/2310.13104v4)

**Tags**: cs.DB cs.CR 



### Iterative Nash Policy Optimization: Aligning LLMs with General   Preferences via No-Regret Learning
**Authors**: Yuheng Zhang, Dian Yu, Baolin Peng, Linfeng Song, Ye Tian, Mingyue Huo, Nan Jiang, Haitao Mi, Dong Yu

**Updated**: 2025-03-03T03:41:11Z

**Summary**: Reinforcement Learning with Human Feedback (RLHF) has achieved great success in aligning large language models (LLMs) with human preferences. Prevalent RLHF approaches are reward-based, following the Bradley-Terry (BT) model assumption, which may not fully capture the complexity of human preferences. In this paper, we explore RLHF under a general preference framework and approach it from a game-theoretic perspective. Specifically, we formulate the problem as a two-player game and propose a novel online algorithm, iterative Nash policy optimization (INPO). The key idea is to let the policy play against itself via no-regret learning, thereby approximating the Nash policy. Unlike previous methods, INPO bypasses the need for estimating the expected win rate for individual responses, which typically incurs high computational or annotation costs. Instead, we introduce a new loss objective that is directly minimized over a preference dataset. We provide theoretical analysis for our approach and demonstrate its effectiveness through experiments on various representative benchmarks. With an LLaMA-3-8B-based SFT model, INPO achieves a 42.6% length-controlled win rate on AlpacaEval 2.0 and a 37.8% win rate on Arena-Hard, showing substantial improvement over the state-of-the-art online RLHF algorithms.

**Link**: [arxiv](http://arxiv.org/abs/2407.00617v4),  [pdf](http://arxiv.org/pdf/2407.00617v4)

**Tags**: cs.LG cs.AI cs.CL cs.GT 



### Optimization-based Prompt Injection Attack to LLM-as-a-Judge
**Authors**: Jiawen Shi, Zenghui Yuan, Yinuo Liu, Yue Huang, Pan Zhou, Lichao Sun, Neil Zhenqiang Gong

**Updated**: 2025-03-03T03:36:17Z

**Summary**: LLM-as-a-Judge uses a large language model (LLM) to select the best response from a set of candidates for a given question. LLM-as-a-Judge has many applications such as LLM-powered search, reinforcement learning with AI feedback (RLAIF), and tool selection. In this work, we propose JudgeDeceiver, an optimization-based prompt injection attack to LLM-as-a-Judge. JudgeDeceiver injects a carefully crafted sequence into an attacker-controlled candidate response such that LLM-as-a-Judge selects the candidate response for an attacker-chosen question no matter what other candidate responses are. Specifically, we formulate finding such sequence as an optimization problem and propose a gradient based method to approximately solve it. Our extensive evaluation shows that JudgeDeceive is highly effective, and is much more effective than existing prompt injection attacks that manually craft the injected sequences and jailbreak attacks when extended to our problem. We also show the effectiveness of JudgeDeceiver in three case studies, i.e., LLM-powered search, RLAIF, and tool selection. Moreover, we consider defenses including known-answer detection, perplexity detection, and perplexity windowed detection. Our results show these defenses are insufficient, highlighting the urgent need for developing new defense strategies. Our implementation is available at this repository: https://github.com/ShiJiawenwen/JudgeDeceiver.

**Link**: [arxiv](http://arxiv.org/abs/2403.17710v4),  [pdf](http://arxiv.org/pdf/2403.17710v4)

**Tags**: cs.CR cs.AI 



### LLMOPT: Learning to Define and Solve General Optimization Problems from   Scratch
**Authors**: Caigao Jiang, Xiang Shu, Hong Qian, Xingyu Lu, Jun Zhou, Aimin Zhou, Yang Yu

**Updated**: 2025-03-03T03:20:08Z

**Summary**: Optimization problems are prevalent across various scenarios. Formulating and then solving optimization problems described by natural language often requires highly specialized human expertise, which could block the widespread application of optimization-based decision making. To automate problem formulation and solving, leveraging large language models (LLMs) has emerged as a potential way. However, this kind of approach suffers from the issue of optimization generalization. Namely, the accuracy of most current LLM-based methods and the generality of optimization problem types that they can model are still limited. In this paper, we propose a unified learning-based framework called LLMOPT to boost optimization generalization. Starting from the natural language descriptions of optimization problems and a pre-trained LLM, LLMOPT constructs the introduced five-element formulation as a universal model for learning to define diverse optimization problem types. Then, LLMOPT employs the multi-instruction tuning to enhance both problem formalization and solver code generation accuracy and generality. After that, to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors, the model alignment and self-correction mechanism are adopted in LLMOPT. We evaluate the optimization generalization ability of LLMOPT and compared methods across six real-world datasets covering roughly 20 fields such as health, environment, energy and manufacturing, etc. Extensive experiment results show that LLMOPT is able to model various optimization problem types such as linear/nonlinear programming, mixed integer programming, and combinatorial optimization, and achieves a notable 11.08% average solving accuracy improvement compared with the state-of-the-art methods. The code is available at https://github.com/caigaojiang/LLMOPT.

**Link**: [arxiv](http://arxiv.org/abs/2410.13213v2),  [pdf](http://arxiv.org/pdf/2410.13213v2)

**Tags**: cs.AI cs.LG 



### On the Generalization and Adaptation Ability of Machine-Generated Text   Detectors in Academic Writing
**Authors**: Yule Liu, Zhiyuan Zhong, Yifan Liao, Zhen Sun, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He

**Updated**: 2025-03-03T03:08:43Z

**Summary**: The rising popularity of large language models (LLMs) has raised concerns about machine-generated text (MGT), particularly in academic settings, where issues like plagiarism and misinformation are prevalent. As a result, developing a highly generalizable and adaptable MGT detection system has become an urgent priority. Given that LLMs are most commonly misused in academic writing, this work investigates the generalization and adaptation capabilities of MGT detectors in three key aspects specific to academic writing: First, we construct MGT-Acedemic, a large-scale dataset comprising over 336M tokens and 749K samples. MGT-Acedemic focuses on academic writing, featuring human-written texts (HWTs) and MGTs across STEM, Humanities, and Social Sciences, paired with an extensible code framework for efficient benchmarking. Second, we benchmark the performance of various detectors for binary classification and attribution tasks in both in-domain and cross-domain settings. This benchmark reveals the often-overlooked challenges of attribution tasks. Third, we introduce a novel attribution task where models have to adapt to new classes over time without (or with very limited) access to prior training data in both few-shot and many-shot scenarios. We implement eight different adapting techniques to improve the performance and highlight the inherent complexity of the task. Our findings provide insights into the generalization and adaptation ability of MGT detectors across diverse scenarios and lay the foundation for building robust, adaptive detection systems. The code framework is available at https://github.com/Y-L-LIU/MGTBench-2.0.

**Link**: [arxiv](http://arxiv.org/abs/2412.17242v3),  [pdf](http://arxiv.org/pdf/2412.17242v3)

**Tags**: cs.AI cs.CL 



### MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language   Models
**Authors**: Peng Xia, Kangyu Zhu, Haoran Li, Tianze Wang, Weijia Shi, Sheng Wang, Linjun Zhang, James Zou, Huaxiu Yao

**Updated**: 2025-03-03T03:08:28Z

**Summary**: Artificial Intelligence (AI) has demonstrated significant potential in healthcare, particularly in disease diagnosis and treatment planning. Recent progress in Medical Large Vision-Language Models (Med-LVLMs) has opened up new possibilities for interactive diagnostic tools. However, these models often suffer from factual hallucination, which can lead to incorrect diagnoses. Fine-tuning and retrieval-augmented generation (RAG) have emerged as methods to address these issues. However, the amount of high-quality data and distribution shifts between training data and deployment data limit the application of fine-tuning methods. Although RAG is lightweight and effective, existing RAG-based approaches are not sufficiently general to different medical domains and can potentially cause misalignment issues, both between modalities and between the model and the ground truth. In this paper, we propose a versatile multimodal RAG system, MMed-RAG, designed to enhance the factuality of Med-LVLMs. Our approach introduces a domain-aware retrieval mechanism, an adaptive retrieved contexts selection method, and a provable RAG-based preference fine-tuning strategy. These innovations make the RAG process sufficiently general and reliable, significantly improving alignment when introducing retrieved contexts. Experimental results across five medical datasets (involving radiology, ophthalmology, pathology) on medical VQA and report generation demonstrate that MMed-RAG can achieve an average improvement of 43.8% in the factual accuracy of Med-LVLMs. Our data and code are available in https://github.com/richard-peng-xia/MMed-RAG.

**Link**: [arxiv](http://arxiv.org/abs/2410.13085v2),  [pdf](http://arxiv.org/pdf/2410.13085v2)

**Tags**: cs.LG cs.CL cs.CV 



### A Pilot Empirical Study on When and How to Use Knowledge Graphs as   Retrieval Augmented Generation
**Authors**: Xujie Yuan, Yongxu Liu, Shimin Di, Shiwen Wu, Libin Zheng, Rui Meng, Lei Chen, Xiaofang Zhou, Jian Yin

**Updated**: 2025-03-03T03:00:59Z

**Summary**: The integration of Knowledge Graphs (KGs) into the Retrieval Augmented Generation (RAG) framework has attracted significant interest, with early studies showing promise in mitigating hallucinations and improving model accuracy. However, a systematic understanding and comparative analysis of the rapidly emerging KG-RAG methods are still lacking. This paper seeks to lay the foundation for systematically answering the question of when and how to use KG-RAG by analyzing their performance in various application scenarios associated with different technical configurations. After outlining the mind map using KG-RAG framework and summarizing its popular pipeline, we conduct a pilot empirical study of KG-RAG works to reimplement and evaluate 6 KG-RAG methods across 7 datasets in diverse scenarios, analyzing the impact of 9 KG-RAG configurations in combination with 17 LLMs. Our results underscore the critical role of appropriate application conditions and optimal configurations of KG-RAG components.

**Link**: [arxiv](http://arxiv.org/abs/2502.20854v2),  [pdf](http://arxiv.org/pdf/2502.20854v2)

**Tags**: cs.AI cs.CL 



### A Closer Look at Machine Unlearning for Large Language Models
**Authors**: Xiaojian Yuan, Tianyu Pang, Chao Du, Kejiang Chen, Weiming Zhang, Min Lin

**Updated**: 2025-03-03T02:45:58Z

**Summary**: Large language models (LLMs) may memorize sensitive or copyrighted content, raising privacy and legal concerns. Due to the high cost of retraining from scratch, researchers attempt to employ machine unlearning to remove specific content from LLMs while preserving the overall performance. In this paper, we discuss several issues in machine unlearning for LLMs and provide our insights on possible approaches. To address the issue of inadequate evaluation of model outputs after unlearning, we introduce three additional metrics to evaluate token diversity, sentence semantics, and factual correctness. We then categorize unlearning methods into untargeted and targeted, and discuss their issues respectively. Specifically, the behavior that untargeted unlearning attempts to approximate is unpredictable and may involve hallucinations, and existing regularization is insufficient for targeted unlearning. To alleviate these issues, we propose using the objective of maximizing entropy (ME) for untargeted unlearning and incorporate answer preservation (AP) loss as regularization for targeted unlearning. Experimental results across three scenarios, i.e., fictitious unlearning, continual unlearning, and real-world unlearning, demonstrate the effectiveness of our approaches. The code is available at https://github.com/sail-sg/closer-look-LLM-unlearning.

**Link**: [arxiv](http://arxiv.org/abs/2410.08109v3),  [pdf](http://arxiv.org/pdf/2410.08109v3)

**Tags**: cs.CL cs.AI cs.LG 



### A Lean Dataset for International Math Olympiad: Small Steps towards   Writing Math Proofs for Hard Problems
**Authors**: Roozbeh Yousefzadeh, Xuenan Cao, Azim Ospanov

**Updated**: 2025-03-03T02:41:10Z

**Summary**: Using AI to write formal proofs for mathematical problems is a challenging task that has seen some advancements in recent years. Automated systems such as Lean can verify the correctness of proofs written in formal language, yet writing the proofs in formal language can be challenging for humans and machines. The miniF2F benchmark has 20 IMO problems in its test set, yet formal proofs are available only for 6 of these problems (3 of which are only written by mathematicians). The model with best accuracy can only prove 2 of these 20 IMO problems, from 1950s and 60s, while its training set is a secret. In this work, we write complete, original formal proofs for the remaining IMO problems in Lean along with 3 extra problems from IMO 2022 and 2023. This effort expands the availability of proof currently in the public domain by creating 5,880 lines of Lean proof. The goal of the paper is to pave the way for developing AI models that can automatically write the formal proofs for all the IMO problems in miniF2F and beyond by providing an evaluation benchmark. In this pursuit, we devise a method to decompose the proofs of these problems into their building blocks, constructing a dataset of 1,329 lemmas with more than 40k lines of Lean code. These lemmas are not trivial, yet they are approachable, providing the opportunity to evaluate and diagnose the failures and successes of AI models. We evaluate the ability of the SOTA LLMs on our dataset and analyze their success and failure modes from different perspectives. Our dataset and code is available at: https://github.com/roozbeh-yz/IMO-Steps.

**Link**: [arxiv](http://arxiv.org/abs/2411.18872v2),  [pdf](http://arxiv.org/pdf/2411.18872v2)

**Tags**: cs.LG 



### Facilitating Multi-turn Function Calling for LLMs via Compositional   Instruction Tuning
**Authors**: Mingyang Chen, Haoze Sun, Tianpeng Li, Fan Yang, Hao Liang, Keer Lu, Bin Cui, Wentao Zhang, Zenan Zhou, Weipeng Chen

**Updated**: 2025-03-03T02:27:02Z

**Summary**: Large Language Models (LLMs) have exhibited significant potential in performing diverse tasks, including the ability to call functions or use external tools to enhance their performance. While current research on function calling by LLMs primarily focuses on single-turn interactions, this paper addresses the overlooked necessity for LLMs to engage in multi-turn function calling--critical for handling compositional, real-world queries that require planning with functions but not only use functions. To facilitate this, we introduce an approach, BUTTON, which generates synthetic compositional instruction tuning data via bottom-up instruction construction and top-down trajectory generation. In the bottom-up phase, we generate simple atomic tasks based on real-world scenarios and build compositional tasks using heuristic strategies based on atomic tasks. Corresponding function definitions are then synthesized for these compositional tasks. The top-down phase features a multi-agent environment where interactions among simulated humans, assistants, and tools are utilized to gather multi-turn function calling trajectories. This approach ensures task compositionality and allows for effective function and trajectory generation by examining atomic tasks within compositional tasks. We produce a dataset BUTTONInstruct comprising 8k data points and demonstrate its effectiveness through extensive experiments across various LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2410.12952v2),  [pdf](http://arxiv.org/pdf/2410.12952v2)

**Tags**: cs.CL 



### AdEval: Alignment-based Dynamic Evaluation to Mitigate Data   Contamination in Large Language Models
**Authors**: Yang Fan

**Updated**: 2025-03-03T02:06:47Z

**Summary**: As Large Language Models (LLMs) are pretrained on massive-scale corpora, the issue of data contamination has become increasingly severe, leading to potential overestimation of model performance during evaluation. To address this, we propose AdEval (Alignment-based Dynamic Evaluation), a dynamic data evaluation method aimed at mitigating the impact of data contamination on evaluation reliability. Experimental results on multiple datasets demonstrate that AdEval effectively reduces the impact of data contamination on evaluation outcomes, enhancing both the fairness and reliability of the evaluation process.

**Link**: [arxiv](http://arxiv.org/abs/2501.13983v3),  [pdf](http://arxiv.org/pdf/2501.13983v3)

**Tags**: cs.CL cs.AI 



### On Large Language Model Continual Unlearning
**Authors**: Chongyang Gao, Lixu Wang, Kaize Ding, Chenkai Weng, Xiao Wang, Qi Zhu

**Updated**: 2025-03-03T01:21:39Z

**Summary**: While large language models have demonstrated impressive performance across various domains and tasks, their security issues have become increasingly severe. Machine unlearning has emerged as a representative approach for model safety and security by removing the influence of undesired data on the target model. However, these methods do not sufficiently consider that unlearning requests in real-world scenarios are continuously emerging, especially in the context of LLMs, which may lead to accumulated model utility loss that eventually becomes unacceptable. Moreover, existing LLM unlearning methods often ignore previous data access limitations due to privacy concerns and copyright protection. Without previous data, the utility preservation during unlearning is much harder. To overcome these challenges, we propose the OOO framework that includes an Orthogonal low-rank adapter (LoRA) for continually unlearning requested data and an Out-Of-Distribution (OOD) detector to measure the similarity between input and unlearning data. The orthogonal LoRA achieves parameter disentanglement among continual unlearning requests. The OOD detector is trained with a novel contrastive entropy loss and utilizes a glocal-aware scoring mechanism. During inference, our OOO framework can decide whether and to what extent to load the unlearning LoRA based on the OOD detector's predicted similarity between the input and the unlearned knowledge. Notably, OOO's effectiveness does not rely on any retained data. We conducted extensive experiments on OOO and state-of-the-art LLM unlearning methods across three tasks and seven datasets. The results indicate that OOO consistently achieves the best unlearning effectiveness and utility preservation, especially when facing continuous unlearning requests. The source codes can be found at https://github.com/GCYZSL/O3-LLM-UNLEARNING.

**Link**: [arxiv](http://arxiv.org/abs/2407.10223v2),  [pdf](http://arxiv.org/pdf/2407.10223v2)

**Tags**: cs.LG cs.CR 



### The Labyrinth of Links: Navigating the Associative Maze of Multi-modal   LLMs
**Authors**: Hong Li, Nanxi Li, Yuanjie Chen, Jianbin Zhu, Qinlu Guo, Cewu Lu, Yong-Lu Li

**Updated**: 2025-03-03T00:41:36Z

**Summary**: Multi-modal Large Language Models (MLLMs) have exhibited impressive capability. However, recently many deficiencies of MLLMs have been found compared to human intelligence, $\textit{e.g.}$, hallucination. To drive the MLLMs study, the community dedicated efforts to building larger benchmarks with complex tasks. In this paper, we propose benchmarking an essential but usually overlooked intelligence: $\textbf{association}$, a human's basic capability to link observation and prior practice memory. To comprehensively investigate MLLM's performance on the association, we formulate the association task and devise a standard benchmark based on adjective and verb semantic concepts. Instead of costly data annotation and curation, we propose a convenient $\textbf{annotation-free}$ construction method transforming the general dataset for our association tasks. Simultaneously, we devise a rigorous data refinement process to eliminate confusion in the raw dataset. Building on this database, we establish three levels of association tasks: single-step, synchronous, and asynchronous associations. Moreover, we conduct a comprehensive investigation into the MLLMs' zero-shot association capabilities, addressing multiple dimensions, including three distinct memory strategies, both open-source and closed-source MLLMs, cutting-edge Mixture-of-Experts (MoE) models, and the involvement of human experts. Our systematic investigation shows that current open-source MLLMs consistently exhibit poor capability in our association tasks, even the currently state-of-the-art GPT-4V(vision) also has a significant gap compared to humans. We believe our benchmark would pave the way for future MLLM studies. $\textit{Our data and code are available at:}$ https://mvig-rhos.com/llm_inception.

**Link**: [arxiv](http://arxiv.org/abs/2410.01417v2),  [pdf](http://arxiv.org/pdf/2410.01417v2)

**Tags**: cs.CV cs.AI cs.CL cs.LG 



### NL2FOL: Translating Natural Language to First-Order Logic for Logical   Fallacy Detection
**Authors**: Abhinav Lalwani, Tasha Kim, Lovish Chopra, Christopher Hahn, Zhijing Jin, Mrinmaya Sachan

**Updated**: 2025-03-03T00:38:48Z

**Summary**: Translating natural language into formal language such as First-Order Logic (FOL) is a foundational challenge in NLP with wide-ranging applications in automated reasoning, misinformation tracking, and knowledge validation. In this paper, we introduce Natural Language to First-Order Logic (NL2FOL), a framework to autoformalize natural language to FOL step by step using Large Language Models (LLMs). Our approach addresses key challenges in this translation process, including the integration of implicit background knowledge. By leveraging structured representations generated by NL2FOL, we use Satisfiability Modulo Theory (SMT) solvers to reason about the logical validity of natural language statements. We present logical fallacy detection as a case study to evaluate the efficacy of NL2FOL. Being neurosymbolic, our approach also provides interpretable insights into the reasoning process and demonstrates robustness without requiring model fine-tuning or labeled training data. Our framework achieves strong performance on multiple datasets. On the LOGIC dataset, NL2FOL achieves an F1-score of 78%, while generalizing effectively to the LOGICCLIMATE dataset with an F1-score of 80%.

**Link**: [arxiv](http://arxiv.org/abs/2405.02318v2),  [pdf](http://arxiv.org/pdf/2405.02318v2)

**Tags**: cs.CL cs.AI cs.LG cs.LO 



### Performance Review on LLM for solving leetcode problems
**Authors**: Lun Wang, Chuanqi Shi, Shaoshui Du, Yiyi Tao, Yixian Shen, Hang Zheng, Yanxin Shen, Xinyu Qiu

**Updated**: 2025-03-03T00:24:08Z

**Summary**: This paper presents a comprehensive performance evaluation of Large Language Models (LLMs) in solving programming challenges from Leetcode, a widely used platform for algorithm practice and technical interviews. We began by crawling the Leetcode website to collect a diverse set of problems encompassing various difficulty levels and topics. Using this dataset, we generated solutions with multiple LLMs, including GPT-4 and GPT-3.5-turbo (ChatGPT-turbo). The generated solutions were systematically evaluated for correctness and efficiency. We employed the pass@k metric to assess the success rates within a given number of attempts and analyzed the runtime performance of the solutions. Our results highlight the strengths and limitations of current LLMs [10] in code generation and problem-solving tasks, providing insights into their potential applications and areas for improvement in automated programming assistance.

**Link**: [arxiv](http://arxiv.org/abs/2502.15770v2),  [pdf](http://arxiv.org/pdf/2502.15770v2)

**Tags**: cs.SE cs.AI 



### Automatically Improving LLM-based Verilog Generation using EDA Tool   Feedback
**Authors**: Jason Blocklove, Shailja Thakur, Benjamin Tan, Hammond Pearce, Siddharth Garg, Ramesh Karri

**Updated**: 2025-03-02T23:43:15Z

**Summary**: Traditionally, digital hardware designs are written in the Verilog hardware description language (HDL) and debugged manually by engineers. This can be time-consuming and error-prone for complex designs. Large Language Models (LLMs) are emerging as a potential tool to help generate fully functioning HDL code, but most works have focused on generation in the single-shot capacity: i.e., run and evaluate, a process that does not leverage debugging and, as such, does not adequately reflect a realistic development process. In this work, we evaluate the ability of LLMs to leverage feedback from electronic design automation (EDA) tools to fix mistakes in their own generated Verilog. To accomplish this, we present an open-source, highly customizable framework, AutoChip, which combines conversational LLMs with the output from Verilog compilers and simulations to iteratively generate and repair Verilog. To determine the success of these LLMs we leverage the VerilogEval benchmark set. We evaluate four state-of-the-art conversational LLMs, focusing on readily accessible commercial models. EDA tool feedback proved to be consistently more effective than zero-shot prompting only with GPT-4o, the most computationally complex model we evaluated. In the best case, we observed a 5.8% increase in the number of successful designs with a 34.2% decrease in cost over the best zero-shot results. Mixing smaller models with this larger model at the end of the feedback iterations resulted in equally as much success as with GPT-4o using feedback, but incurred 41.9% lower cost (corresponding to an overall decrease in cost over zero-shot by 89.6%).

**Link**: [arxiv](http://arxiv.org/abs/2411.11856v2),  [pdf](http://arxiv.org/pdf/2411.11856v2)

**Tags**: cs.AR cs.AI cs.PL 



### Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of   Encoders
**Authors**: Min Shi, Fuxiao Liu, Shihao Wang, Shijia Liao, Subhashree Radhakrishnan, Yilin Zhao, De-An Huang, Hongxu Yin, Karan Sapra, Yaser Yacoob, Humphrey Shi, Bryan Catanzaro, Andrew Tao, Jan Kautz, Zhiding Yu, Guilin Liu

**Updated**: 2025-03-02T23:41:37Z

**Summary**: The ability to accurately interpret complex visual information is a crucial topic of multimodal large language models (MLLMs). Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. A number of recent MLLMs achieve this goal using a mixture of vision encoders. Despite their success, there is a lack of systematic comparisons and detailed ablation studies addressing critical aspects, such as expert selection and the integration of multiple vision experts. This study provides an extensive exploration of the design space for MLLMs using a mixture of vision encoders and resolutions. Our findings reveal several underlying principles common to various existing strategies, leading to a streamlined yet effective design approach. We discover that simply concatenating visual tokens from a set of complementary vision encoders is as effective as more complex mixing architectures or strategies. We additionally introduce Pre-Alignment to bridge the gap between vision-focused encoders and language tokens, enhancing model coherence. The resulting family of MLLMs, Eagle, surpasses other leading open-source models on major MLLM benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2408.15998v2),  [pdf](http://arxiv.org/pdf/2408.15998v2)

**Tags**: cs.CV cs.AI cs.LG cs.RO 



### ActionReasoningBench: Reasoning about Actions with and without   Ramification Constraints
**Authors**: Divij Handa, Pavel Dolin, Shrinidhi Kumbhar, Tran Cao Son, Chitta Baral

**Updated**: 2025-03-02T23:24:43Z

**Summary**: Reasoning about Actions and Change (RAC) has historically played a pivotal role in solving foundational AI problems, such as the frame problem. It has driven advancements in AI fields, such as non-monotonic and commonsense reasoning. RAC remains crucial for AI systems that operate in dynamic environments, engage in interactive scenarios, or rely on commonsense reasoning. Despite substantial advances made by Large Language Models (LLMs) in various AI domains, their performance in RAC remains underexplored. To address this gap, we introduce a new diagnostic benchmark, ActionReasoningBench, which encompasses 8 domains and includes questions for up to 19 action sequences. This benchmark rigorously evaluates LLMs across six key RAC dimensions: Fluent Tracking, State Tracking, Action Executability, Effects of Actions, Numerical RAC, and Composite Questions. LLMs demonstrate average accuracy rates of 73.55%, 65.63%, 58.73%, and 62.38% on the former four dimensions, which are frequently discussed in RAC literature. However, the performance on the latter two dimensions, which introduce complex and novel reasoning questions, the average performance of LLMs is lowered to 33.16% and 51.19%, respectively, reflecting a 17.9% performance decline. We also introduce new ramification constraints to capture the indirect effects of actions, providing deeper insights into RAC challenges. Our evaluation of state-of-the-art LLMs, including both open-source and commercial models, reveals challenges across all RAC dimensions, particularly in handling ramifications, with GPT-4o failing to solve any question and o1-preview achieving a score of only 18.4%.

**Link**: [arxiv](http://arxiv.org/abs/2406.04046v3),  [pdf](http://arxiv.org/pdf/2406.04046v3)

**Tags**: cs.CC cs.AI 



### We Have a Package for You! A Comprehensive Analysis of Package   Hallucinations by Code Generating LLMs
**Authors**: Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala

**Updated**: 2025-03-02T21:03:52Z

**Summary**: The reliance of popular programming languages such as Python and JavaScript on centralized package repositories and open-source software, combined with the emergence of code-generating Large Language Models (LLMs), has created a new type of threat to the software supply chain: package hallucinations. These hallucinations, which arise from fact-conflicting errors when generating code using LLMs, represent a novel form of package confusion attack that poses a critical threat to the integrity of the software supply chain. This paper conducts a rigorous and comprehensive evaluation of package hallucinations across different programming languages, settings, and parameters, exploring how a diverse set of models and configurations affect the likelihood of generating erroneous package recommendations and identifying the root causes of this phenomenon. Using 16 popular LLMs for code generation and two unique prompt datasets, we generate 576,000 code samples in two programming languages that we analyze for package hallucinations. Our findings reveal that that the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat. To overcome this problem, we implement several hallucination mitigation strategies and show that they are able to significantly reduce the number of package hallucinations while maintaining code quality. Our experiments and findings highlight package hallucinations as a persistent and systemic phenomenon while using state-of-the-art LLMs for code generation, and a significant challenge which deserves the research community's urgent attention.

**Link**: [arxiv](http://arxiv.org/abs/2406.10279v3),  [pdf](http://arxiv.org/pdf/2406.10279v3)

**Tags**: cs.SE cs.AI cs.CR cs.LG 



### Inference to the Best Explanation in Large Language Models
**Authors**: Dhairya Dalal, Marco Valentino, André Freitas, Paul Buitelaar

**Updated**: 2025-03-02T20:33:20Z

**Summary**: While Large Language Models (LLMs) have found success in real-world applications, their underlying explanatory process is still poorly understood. This paper proposes IBE-Eval, a framework inspired by philosophical accounts on Inference to the Best Explanation (IBE) to advance the interpretation and evaluation of LLMs' explanations. IBE-Eval estimates the plausibility of natural language explanations through a combination of explicit logical and linguistic features including: consistency, parsimony, coherence, and uncertainty. Extensive experiments are conducted on Causal Question Answering (CQA), where \textit{IBE-Eval} is tasked to select the most plausible causal explanation amongst competing ones generated by LLMs (i.e., GPT 3.5 and Llama 2). The experiments reveal that IBE-Eval can successfully identify the best explanation with up to 77\% accuracy ($\approx 27\%$ above random), improving upon a GPT 3.5-as-a-Judge baseline ($\approx+17\%$) while being intrinsically more efficient and interpretable. Additional analyses suggest that, despite model-specific variances, LLM-generated explanations tend to conform to IBE criteria and that IBE-Eval is significantly correlated with human judgment, opening up opportunities for future development of automated explanation verification tools.

**Link**: [arxiv](http://arxiv.org/abs/2402.10767v2),  [pdf](http://arxiv.org/pdf/2402.10767v2)

**Tags**: cs.CL cs.AI I.2.7 



### $μ$nit Scaling: Simple and Scalable FP8 LLM Training
**Authors**: Saaketh Narayan, Abhay Gupta, Mansheej Paul, Davis Blalock

**Updated**: 2025-03-02T20:16:43Z

**Summary**: Large Language Model training with 8-bit floating point (FP8) formats promises significant efficiency improvements, but reduced numerical precision makes training challenging. It is currently possible to train in FP8 only if one is willing to tune various hyperparameters, reduce model scale, or accept the overhead of computing dynamic scale factors. We demonstrate simple, scalable FP8 training that requires no dynamic scaling factors or special hyperparameters, even at large model sizes. Our method, $\mu$nit Scaling ($\mu$S), also enables simple hyperparameter transfer across model widths, matched numerics across training and inference, and other desirable properties. $\mu$nit Scaling is straightforward to implement, consisting of a set of minimal interventions based on a first-principles analysis of common transformer operations. We validate our method by training models from 1B to 13B parameters, performing all hidden linear layer computations in FP8. We achieve quality equal to higher precision baselines while also training up to 33% faster.

**Link**: [arxiv](http://arxiv.org/abs/2502.05967v2),  [pdf](http://arxiv.org/pdf/2502.05967v2)

**Tags**: cs.LG 



### Lean Copilot: Large Language Models as Copilots for Theorem Proving in   Lean
**Authors**: Peiyang Song, Kaiyu Yang, Anima Anandkumar

**Updated**: 2025-03-02T20:13:11Z

**Summary**: Neural theorem proving combines large language models (LLMs) with proof assistants such as Lean, where the correctness of formal proofs can be rigorously verified, leaving no room for hallucination. With existing neural theorem provers pretrained on a fixed collection of data and offering valuable suggestions at times, it is challenging for them to continually prove novel theorems in a fully autonomous mode, where human insights may be critical. In this paper, we explore LLMs as copilots that assist humans in proving theorems. We introduce Lean Copilot, an general framework for running LLM inference natively in Lean. It enables programmers to build various LLM-based proof automation tools that integrate seamlessly into the workflow of Lean users. Lean users can use our pretrained models or bring their own ones that run either locally (with or without GPUs) or on the cloud. Using Lean Copilot, we build LLM-based tools that suggest proof steps, complete proof goals, and select relevant premises. Experimental results on the Mathematics in Lean textbook demonstrate the effectiveness of our method compared to existing rule-based proof automation in Lean (aesop). When assisting humans, Lean Copilot requires only 2.08 manually-entered proof steps on average (3.86 required by aesop); when automating the theorem proving process, Lean Copilot automates 74.2% proof steps on average, 85% better than aesop (40.1%). We open source all code and artifacts under a permissive MIT license to facilitate further research.

**Link**: [arxiv](http://arxiv.org/abs/2404.12534v2),  [pdf](http://arxiv.org/pdf/2404.12534v2)

**Tags**: cs.AI cs.LG cs.LO stat.ML 



### Inference Scaling for Long-Context Retrieval Augmented Generation
**Authors**: Zhenrui Yue, Honglei Zhuang, Aijun Bai, Kai Hui, Rolf Jagerman, Hansi Zeng, Zhen Qin, Dong Wang, Xuanhui Wang, Michael Bendersky

**Updated**: 2025-03-02T19:44:37Z

**Summary**: The scaling of inference computation has unlocked the potential of long-context large language models (LLMs) across diverse settings. For knowledge-intensive tasks, the increased compute is often allocated to incorporate more external knowledge. However, without effectively utilizing such knowledge, solely expanding context does not always enhance performance. In this work, we investigate inference scaling for retrieval augmented generation (RAG), exploring the combination of multiple strategies beyond simply increasing the quantity of knowledge, including in-context learning and iterative prompting. These strategies provide additional flexibility to scale test-time computation (e.g., by increasing retrieved documents or generation steps), thereby enhancing LLMs' ability to effectively acquire and utilize contextual information. We address two key questions: (1) How does RAG performance benefit from the scaling of inference computation when optimally configured? (2) Can we predict the optimal test-time compute allocation for a given budget by modeling the relationship between RAG performance and inference parameters? Our observations reveal that increasing inference computation leads to nearly linear gains in RAG performance when optimally allocated, a relationship we describe as the inference scaling laws for RAG. Building on this, we further develop the computation allocation model to estimate RAG performance across different inference configurations. The model predicts optimal inference parameters under various computation constraints, which align closely with the experimental results. By applying these optimal configurations, we demonstrate that scaling inference compute on long-context LLMs achieves up to 58.9% gains on benchmark datasets compared to standard RAG.

**Link**: [arxiv](http://arxiv.org/abs/2410.04343v2),  [pdf](http://arxiv.org/pdf/2410.04343v2)

**Tags**: cs.CL 



### SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and   Iterative Refinement
**Authors**: Antonis Antoniades, Albert Örwall, Kexun Zhang, Yuxi Xie, Anirudh Goyal, William Wang

**Updated**: 2025-03-02T19:42:45Z

**Summary**: Software engineers operating in complex and dynamic environments must continuously adapt to evolving requirements, learn iteratively from experience, and reconsider their approaches based on new insights. However, current large language model (LLM)-based software agents often follow linear, sequential processes that prevent backtracking and exploration of alternative solutions, limiting their ability to rethink their strategies when initial approaches prove ineffective. To address these challenges, we propose SWE-Search, a multi-agent framework that integrates Monte Carlo Tree Search (MCTS) with a self-improvement mechanism to enhance software agents' performance on repository-level software tasks. SWE-Search extends traditional MCTS by incorporating a hybrid value function that leverages LLMs for both numerical value estimation and qualitative evaluation. This enables self-feedback loops where agents iteratively refine their strategies based on both quantitative numerical evaluations and qualitative natural language assessments of pursued trajectories. The framework includes a SWE-Agent for adaptive exploration, a Value Agent for iterative feedback, and a Discriminator Agent that facilitates multi-agent debate for collaborative decision-making. Applied to the SWE-bench benchmark, our approach demonstrates a 23% relative improvement in performance across five models compared to standard open-source agents without MCTS. Our analysis reveals how performance scales with increased inference-time compute through deeper search, providing a pathway to improve software agents without requiring larger models or additional training data. This highlights the potential of self-evaluation driven search techniques in complex software engineering environments.

**Link**: [arxiv](http://arxiv.org/abs/2410.20285v5),  [pdf](http://arxiv.org/pdf/2410.20285v5)

**Tags**: cs.AI 



### Prompting Fairness: Integrating Causality to Debias Large Language   Models
**Authors**: Jingling Li, Zeyu Tang, Xiaoyu Liu, Peter Spirtes, Kun Zhang, Liu Leqi, Yang Liu

**Updated**: 2025-03-02T17:33:03Z

**Summary**: Large language models (LLMs), despite their remarkable capabilities, are susceptible to generating biased and discriminatory responses. As LLMs increasingly influence high-stakes decision-making (e.g., hiring and healthcare), mitigating these biases becomes critical. In this work, we propose a causality-guided debiasing framework to tackle social biases, aiming to reduce the objectionable dependence between LLMs' decisions and the social information in the input. Our framework introduces a novel perspective to identify how social information can affect an LLM's decision through different causal pathways. Leveraging these causal insights, we outline principled prompting strategies that regulate these pathways through selection mechanisms. This framework not only unifies existing prompting-based debiasing techniques, but also opens up new directions for reducing bias by encouraging the model to prioritize fact-based reasoning over reliance on biased social cues. We validate our framework through extensive experiments on real-world datasets across multiple domains, demonstrating its effectiveness in debiasing LLM decisions, even with only black-box access to the model.

**Link**: [arxiv](http://arxiv.org/abs/2403.08743v2),  [pdf](http://arxiv.org/pdf/2403.08743v2)

**Tags**: cs.CL cs.AI cs.LG 



### Leveraging Dual Process Theory in Language Agent Framework for Real-time   Simultaneous Human-AI Collaboration
**Authors**: Shao Zhang, Xihuai Wang, Wenhao Zhang, Chaoran Li, Junru Song, Tingyu Li, Lin Qiu, Xuezhi Cao, Xunliang Cai, Wen Yao, Weinan Zhang, Xinbing Wang, Ying Wen

**Updated**: 2025-03-02T17:15:11Z

**Summary**: Agents built on large language models (LLMs) have excelled in turn-by-turn human-AI collaboration but struggle with simultaneous tasks requiring real-time interaction. Latency issues and the challenge of inferring variable human strategies hinder their ability to make autonomous decisions without explicit instructions. Through experiments with current independent System 1 and System 2 methods, we validate the necessity of using Dual Process Theory (DPT) in real-time tasks. We propose DPT-Agent, a novel language agent framework that integrates System 1 and System 2 for efficient real-time simultaneous human-AI collaboration. DPT-Agent's System 1 uses a Finite-state Machine (FSM) and code-as-policy for fast, intuitive, and controllable decision-making. DPT-Agent's System 2 integrates Theory of Mind (ToM) and asynchronous reflection to infer human intentions and perform reasoning-based autonomous decisions. We demonstrate the effectiveness of DPT-Agent through further experiments with rule-based agents and human collaborators, showing significant improvements over mainstream LLM-based frameworks. DPT-Agent can effectively help LLMs convert correct slow thinking and reasoning into executable actions, thereby improving performance. To the best of our knowledge, DPT-Agent is the first language agent framework that achieves successful real-time simultaneous human-AI collaboration autonomously. Code of DPT-Agent can be found in https://github.com/sjtu-marl/DPT-Agent.

**Link**: [arxiv](http://arxiv.org/abs/2502.11882v3),  [pdf](http://arxiv.org/pdf/2502.11882v3)

**Tags**: cs.AI cs.CL cs.HC cs.LG cs.MA 



### Harnessing Multiple Large Language Models: A Survey on LLM Ensemble
**Authors**: Zhijun Chen, Jingzheng Li, Pengpeng Chen, Zhuoran Li, Kai Sun, Yuankai Luo, Qianren Mao, Dingqi Yang, Hailong Sun, Philip S. Yu

**Updated**: 2025-03-02T16:56:04Z

**Summary**: LLM Ensemble -- which involves the comprehensive use of multiple large language models (LLMs), each aimed at handling user queries during downstream inference, to benefit from their individual strengths -- has gained substantial attention recently. The widespread availability of LLMs, coupled with their varying strengths and out-of-the-box usability, has profoundly advanced the field of LLM Ensemble. This paper presents the first systematic review of recent developments in LLM Ensemble. First, we introduce our taxonomy of LLM Ensemble and discuss several related research problems. Then, we provide a more in-depth classification of the methods under the broad categories of "ensemble-before-inference, ensemble-during-inference, ensemble-after-inference'', and review all relevant methods. Finally, we introduce related benchmarks and applications, summarize existing studies, and suggest several future research directions. A curated list of papers on LLM Ensemble is available at https://github.com/junchenzhi/Awesome-LLM-Ensemble.

**Link**: [arxiv](http://arxiv.org/abs/2502.18036v2),  [pdf](http://arxiv.org/pdf/2502.18036v2)

**Tags**: cs.CL 



### MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse   Mixture-of-Experts Systems
**Authors**: Yao Fu, Yinsicheng Jiang, Yeqi Huang, Ping Nie, Zhan Lu, Leyang Xue, Congjie He, Man-Kit Sit, Jilong Xue, Li Dong, Ziming Miao, Kai Zou, Edoardo Ponti, Luo Mai

**Updated**: 2025-03-02T16:40:03Z

**Summary**: The Mixture-of-Experts (MoE) architecture is increasingly favored for scaling Large Language Models (LLMs). Its key feature, sparse activation, selectively activates only a subset of parameters (experts) per token, reducing memory bandwidth and compute FLOPs compared to dense models. To capitalize on this, MoE designers leverage heterogeneous compute and memory hardware to lower system costs. However, the interaction between model sparsity and hardware heterogeneity introduces trade-offs in Cost, Accuracy, and Performance (CAP). To address this, we introduce MoE-CAP, a benchmarking method for evaluating sparse MoE systems across these three dimensions. Its key innovation is a sparsity-aware CAP analysis model, the first to integrate cost, performance, and accuracy metrics into a single diagram while estimating the impact of sparsity on system performance. MoE-CAP helps practitioners optimize hardware provisioning for an MoE model-or vice versa. MoE-CAP supports various MoE models and provides more accurate metrics than existing methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.07067v3),  [pdf](http://arxiv.org/pdf/2412.07067v3)

**Tags**: cs.LG cs.DC 



### Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation
**Authors**: Chengwen Qi, Ren Ma, Bowen Li, He Du, Binyuan Hui, Jinwang Wu, Yuanjun Laili, Conghui He

**Updated**: 2025-03-02T16:38:28Z

**Summary**: First-order logic (FOL) reasoning, which involves sequential deduction, is pivotal for intelligent systems and serves as a valuable task for evaluating reasoning capabilities, particularly in chain-of-thought (CoT) contexts. Existing benchmarks often rely on extensive human annotation or handcrafted templates, making it difficult to achieve the necessary complexity, scalability, and diversity for robust evaluation. To address these limitations, we propose a novel framework called ProverGen that synergizes the generative strengths of Large Language Models (LLMs) with the rigor and precision of symbolic provers, enabling the creation of a scalable, diverse, and high-quality FOL reasoning dataset, ProverQA. ProverQA is also distinguished by its inclusion of accessible and logically coherent intermediate reasoning steps for each problem. Our evaluation shows that state-of-the-art LLMs struggle to solve ProverQA problems, even with CoT prompting, highlighting the dataset's challenging nature. We also finetune Llama3.1-8B-Instruct on a separate training set generated by our framework. The finetuned model demonstrates consistent improvements on both in-distribution and out-of-distribution test sets, suggesting the value of our proposed data generation framework. Code available at: https://github.com/opendatalab/ProverGen

**Link**: [arxiv](http://arxiv.org/abs/2502.06563v2),  [pdf](http://arxiv.org/pdf/2502.06563v2)

**Tags**: cs.CL 



### Generative causal testing to bridge data-driven models and scientific   theories in language neuroscience
**Authors**: Richard Antonello, Chandan Singh, Shailee Jain, Aliyah Hsu, Sihang Guo, Jianfeng Gao, Bin Yu, Alexander Huth

**Updated**: 2025-03-02T16:32:24Z

**Summary**: Representations from large language models are highly effective at predicting BOLD fMRI responses to language stimuli. However, these representations are largely opaque: it is unclear what features of the language stimulus drive the response in each brain area. We present generative causal testing (GCT), a framework for generating concise explanations of language selectivity in the brain from predictive models and then testing those explanations in follow-up experiments using LLM-generated stimuli.This approach is successful at explaining selectivity both in individual voxels and cortical regions of interest (ROIs), including newly identified microROIs in prefrontal cortex. We show that explanatory accuracy is closely related to the predictive power and stability of the underlying predictive models. Finally, we show that GCT can dissect fine-grained differences between brain areas with similar functional selectivity. These results demonstrate that LLMs can be used to bridge the widening gap between data-driven models and formal scientific theories.

**Link**: [arxiv](http://arxiv.org/abs/2410.00812v2),  [pdf](http://arxiv.org/pdf/2410.00812v2)

**Tags**: cs.CL q-bio.NC 



### Utilizing ChatGPT in a Data Structures and Algorithms Course: A Teaching   Assistant's Perspective
**Authors**: Pooriya Jamie, Reyhaneh Hajihashemi, Sharareh Alipour

**Updated**: 2025-03-02T16:12:10Z

**Summary**: Integrating large language models (LLMs) like ChatGPT into computer science education offers transformative potential for complex courses such as data structures and algorithms (DSA). This study examines ChatGPT as a supplementary tool for teaching assistants (TAs), guided by structured prompts and human oversight, to enhance instruction and student outcomes. A controlled experiment compared traditional TA-led instruction with a hybrid approach where TAs used ChatGPT-4o and ChatGPT o1 to generate exercises, clarify concepts, and provide feedback. Structured prompts emphasized problem decomposition, real-world context, and code examples, enabling tailored support while mitigating over-reliance on AI. Results demonstrated the hybrid approach's efficacy, with students in the ChatGPT-assisted group scoring 16.50 points higher on average and excelling in advanced topics. However, ChatGPT's limitations necessitated TA verification. This framework highlights the dual role of LLMs: augmenting TA efficiency while ensuring accuracy through human oversight, offering a scalable solution for human-AI collaboration in education.

**Link**: [arxiv](http://arxiv.org/abs/2410.08899v2),  [pdf](http://arxiv.org/pdf/2410.08899v2)

**Tags**: cs.HC cs.AI cs.DS K.3.2; I.2.6 



### TradingAgents: Multi-Agents LLM Financial Trading Framework
**Authors**: Yijia Xiao, Edward Sun, Di Luo, Wei Wang

**Updated**: 2025-03-02T15:57:39Z

**Summary**: Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. However, multi-agent systems' potential to replicate real-world trading firms' collaborative dynamics remains underexplored. TradingAgents proposes a novel stock trading framework inspired by trading firms, featuring LLM-powered agents in specialized roles such as fundamental analysts, sentiment analysts, technical analysts, and traders with varied risk profiles. The framework includes Bull and Bear researcher agents assessing market conditions, a risk management team monitoring exposure, and traders synthesizing insights from debates and historical data to make informed decisions. By simulating a dynamic, collaborative trading environment, this framework aims to improve trading performance. Detailed architecture and extensive experiments reveal its superiority over baseline models, with notable improvements in cumulative returns, Sharpe ratio, and maximum drawdown, highlighting the potential of multi-agent LLM frameworks in financial trading. TradingAgents is available at https://github.com/PioneerFintech.

**Link**: [arxiv](http://arxiv.org/abs/2412.20138v5),  [pdf](http://arxiv.org/pdf/2412.20138v5)

**Tags**: q-fin.TR cs.AI cs.CE cs.LG 



### LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One   Vision Token
**Authors**: Shaolei Zhang, Qingkai Fang, Zhe Yang, Yang Feng

**Updated**: 2025-03-02T15:55:07Z

**Summary**: The advent of real-time large multimodal models (LMMs) like GPT-4o has sparked considerable interest in efficient LMMs. LMM frameworks typically encode visual inputs into vision tokens (continuous representations) and integrate them and textual instructions into the context of large language models (LLMs), where large-scale parameters and numerous context tokens (predominantly vision tokens) result in substantial computational overhead. Previous efforts towards efficient LMMs always focus on replacing the LLM backbone with smaller models, while neglecting the crucial issue of token quantity. In this paper, we introduce LLaVA-Mini, an efficient LMM with minimal vision tokens. To achieve a high compression ratio of vision tokens while preserving visual information, we first analyze how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers of LLM backbone, where they mainly fuse visual information into text tokens. Building on this finding, LLaVA-Mini introduces modality pre-fusion to fuse visual information into text tokens in advance, thereby facilitating the extreme compression of vision tokens fed to LLM backbone into one token. LLaVA-Mini is a unified large multimodal model that can support the understanding of images, high-resolution images, and videos in an efficient manner. Experiments across 11 image-based and 7 video-based benchmarks demonstrate that LLaVA-Mini outperforms LLaVA-v1.5 with just 1 vision token instead of 576. Efficiency analyses reveal that LLaVA-Mini can reduce FLOPs by 77%, deliver low-latency responses within 40 milliseconds, and process over 10,000 frames of video on the GPU hardware with 24GB of memory.

**Link**: [arxiv](http://arxiv.org/abs/2501.03895v2),  [pdf](http://arxiv.org/pdf/2501.03895v2)

**Tags**: cs.CV cs.AI cs.CL 



### Steering Large Language Models between Code Execution and Textual   Reasoning
**Authors**: Yongchao Chen, Harsh Jhamtani, Srinagesh Sharma, Chuchu Fan, Chi Wang

**Updated**: 2025-03-02T15:54:11Z

**Summary**: While a lot of recent research focuses on enhancing the textual reasoning capabilities of Large Language Models (LLMs) by optimizing the multi-agent framework or reasoning chains, several benchmark tasks can be solved with 100\% success through direct coding, which is more scalable and avoids the computational overhead associated with textual iterating and searching. Textual reasoning has inherent limitations in solving tasks with challenges in math, logics, optimization, and searching, which is unlikely to be solved by simply scaling up the model and data size. The recently released OpenAI GPT Code Interpreter and multi-agent frameworks such as AutoGen have demonstrated remarkable proficiency of integrating code generation and execution to solve complex tasks using LLMs. However, based on our experiments on 7 existing popular methods for steering code/text generation in both single- and multi-turn settings with 14 tasks and 6 types of LLMs (including the new O1-preview), currently there is no optimal method to correctly steer LLMs to write code when needed. We discover some interesting patterns on when models use code vs. textual reasoning with the evolution to task complexity and model sizes, which even result in an astonishingly inverse scaling behavior. We also discover that results from LLM written code are not always better than using textual reasoning, even if the task could be solved through code. To mitigate the above issues, we propose three methods to better steer LLM code/text generation and achieve a notable improvement. The costs of token lengths and runtime are thoroughly discussed for all the methods. We believe the problem of steering LLM code/text generation is critical for future research and has much space for further improvement. Project Page, Datasets, and Codes are available at https://yongchao98.github.io/CodeSteer/.

**Link**: [arxiv](http://arxiv.org/abs/2410.03524v2),  [pdf](http://arxiv.org/pdf/2410.03524v2)

**Tags**: cs.CL 



### Evaluating Low-Resource Lane Following Algorithms for   Compute-Constrained Automated Vehicles
**Authors**: Beñat Froemming-Aldanondo, Tatiana Rastoskueva, Michael Evans, Marcial Machado, Anna Vadella, Rickey Johnson, Luis Escamilla, Milan Jostes, Devson Butani, Ryan Kaddis, Chan-Jin Chung, Joshua Siegel

**Updated**: 2025-03-02T15:30:06Z

**Summary**: Reliable lane-following is essential for automated and assisted driving, yet existing solutions often rely on models that require extensive computational resources, limiting their deployment in compute-constrained vehicles. We evaluate five low-resource lane-following algorithms designed for real-time operation on vehicles with limited computing resources. Performance was assessed through simulation and deployment on real drive-by-wire electric vehicles, with evaluation metrics including reliability, comfort, speed, and adaptability. The top-performing methods used unsupervised learning to detect and separate lane lines with processing time under 10 ms per frame, outperforming compute-intensive and poor generalizing deep learning approaches. These approaches demonstrated robustness across lighting conditions, road textures, and lane geometries. The findings highlight the potential for efficient lane detection approaches to enhance the accessibility and reliability of autonomous vehicle technologies. Reducing computing requirements enables lane keeping to be widely deployed in vehicles as part of lower-level automation, including active safety systems.

**Link**: [arxiv](http://arxiv.org/abs/2409.03114v2),  [pdf](http://arxiv.org/pdf/2409.03114v2)

**Tags**: cs.RO cs.CV 



### SPARTUN3D: Situated Spatial Understanding of 3D World in Large Language   Models
**Authors**: Yue Zhang, Zhiyang Xu, Ying Shen, Parisa Kordjamshidi, Lifu Huang

**Updated**: 2025-03-02T15:22:12Z

**Summary**: Integrating the 3D world into large language models (3D-based LLMs) has been a promising research direction for 3D scene understanding. However, current 3D-based LLMs fall short in situated understanding due to two key limitations: 1) existing 3D datasets are constructed from a global perspective of the 3D scenes and lack situated context. 2) the architectures of existing 3D-based LLMs lack explicit alignment between the spatial representations of 3D scenes and natural language, limiting their performance in tasks requiring precise spatial reasoning. We address these issues by introducing a scalable situated 3D dataset, named Spartun3D, that incorporates various situated spatial reasoning tasks. Furthermore, we propose Spartun3D-LLM, built on an existing 3D-based LLM but integrated with a novel situated spatial alignment module, aiming to enhance the alignment between 3D visual representations and their corresponding textual descriptions. Experimental results demonstrate that both our proposed dataset and alignment module significantly enhance the situated spatial understanding of 3D-based LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2410.03878v2),  [pdf](http://arxiv.org/pdf/2410.03878v2)

**Tags**: cs.CV 



### Monet: Mixture of Monosemantic Experts for Transformers
**Authors**: Jungwoo Park, Young Jin Ahn, Kee-Eung Kim, Jaewoo Kang

**Updated**: 2025-03-02T14:52:21Z

**Summary**: Understanding the internal computations of large language models (LLMs) is crucial for aligning them with human values and preventing undesirable behaviors like toxic content generation. However, mechanistic interpretability is hindered by polysemanticity -- where individual neurons respond to multiple, unrelated concepts. While Sparse Autoencoders (SAEs) have attempted to disentangle these features through sparse dictionary learning, they have compromised LLM performance due to reliance on post-hoc reconstruction loss. To address this issue, we introduce Mixture of Monosemantic Experts for Transformers (Monet) architecture, which incorporates sparse dictionary learning directly into end-to-end Mixture-of-Experts pretraining. Our novel expert decomposition method enables scaling the expert count to 262,144 per layer while total parameters scale proportionally to the square root of the number of experts. Our analyses demonstrate mutual exclusivity of knowledge across experts and showcase the parametric knowledge encapsulated within individual experts. Moreover, Monet allows knowledge manipulation over domains, languages, and toxicity mitigation without degrading general performance. Our pursuit of transparent LLMs highlights the potential of scaling expert counts to enhance mechanistic interpretability and directly resect the internal knowledge to fundamentally adjust model behavior. The source code and pretrained checkpoints are available at https://github.com/dmis-lab/Monet.

**Link**: [arxiv](http://arxiv.org/abs/2412.04139v3),  [pdf](http://arxiv.org/pdf/2412.04139v3)

**Tags**: cs.AI 



### Where is the Testbed for my Federated Learning Research?
**Authors**: Janez Božič, Amândio R. Faustino, Boris Radovič, Marco Canini, Veljko Pejović

**Updated**: 2025-03-02T14:41:12Z

**Summary**: Progressing beyond centralized AI is of paramount importance, yet, distributed AI solutions, in particular various federated learning (FL) algorithms, are often not comprehensively assessed, which prevents the research community from identifying the most promising approaches and practitioners from being convinced that a certain solution is deployment-ready. The largest hurdle towards FL algorithm evaluation is the difficulty of conducting real-world experiments over a variety of FL client devices and different platforms, with different datasets and data distribution, all while assessing various dimensions of algorithm performance, such as inference accuracy, energy consumption, and time to convergence, to name a few. In this paper, we present CoLExT, a real-world testbed for FL research. CoLExT is designed to streamline experimentation with custom FL algorithms in a rich testbed configuration space, with a large number of heterogeneous edge devices, ranging from single-board computers to smartphones, and provides real-time collection and visualization of a variety of metrics through automatic instrumentation. According to our evaluation, porting FL algorithms to CoLExT requires minimal involvement from the developer, and the instrumentation introduces minimal resource usage overhead. Furthermore, through an initial investigation involving popular FL algorithms running on CoLExT, we reveal previously unknown trade-offs, inefficiencies, and programming bugs.

**Link**: [arxiv](http://arxiv.org/abs/2407.14154v2),  [pdf](http://arxiv.org/pdf/2407.14154v2)

**Tags**: cs.LG cs.DC 



### Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates
**Authors**: Xiaosen Zheng, Tianyu Pang, Chao Du, Qian Liu, Jing Jiang, Min Lin

**Updated**: 2025-03-02T14:28:33Z

**Summary**: Automatic LLM benchmarks, such as AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench, have become popular for evaluating language models due to their cost-effectiveness and scalability compared to human evaluation. Achieving high win rates on these benchmarks can significantly boost the promotional impact of newly released language models. This promotional benefit may motivate tricks, such as manipulating model output length or style to game win rates, even though several mechanisms have been developed to control length and disentangle style to reduce gameability. Nonetheless, we show that even a "null model" that always outputs a constant response (irrelevant to input instructions) can cheat automatic benchmarks and achieve top-ranked win rates: an 86.5% LC win rate on AlpacaEval 2.0; an 83.0 score on Arena-Hard-Auto; and a 9.55 score on MT-Bench. Moreover, the crafted cheating outputs are transferable because we assume that the instructions of these benchmarks (e.g., 805 samples of AlpacaEval 2.0) are private and cannot be accessed. While our experiments are primarily proof-of-concept, an adversary could use LLMs to generate more imperceptible cheating responses, unethically benefiting from high win rates and promotional impact. Our findings call for the development of anti-cheating mechanisms for reliable automatic benchmarks. The code is available at https://github.com/sail-sg/Cheating-LLM-Benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2410.07137v2),  [pdf](http://arxiv.org/pdf/2410.07137v2)

**Tags**: cs.CL cs.AI cs.CR cs.LG 



### How Does A Text Preprocessing Pipeline Affect Ontology Syntactic   Matching?
**Authors**: Zhangcheng Qiang, Kerry Taylor, Weiqing Wang

**Updated**: 2025-03-02T13:52:25Z

**Summary**: The generic text preprocessing pipeline, comprising Tokenisation, Normalisation, Stop Words Removal, and Stemming/Lemmatisation, has been implemented in many systems for syntactic ontology matching (OM). However, the lack of standardisation in text preprocessing creates diversity in mapping results. In this paper, we investigate the effect of the text preprocessing pipeline on syntactic OM in 8 Ontology Alignment Evaluation Initiative (OAEI) tracks with 49 distinct alignments. We find that Phase 1 text preprocessing (Tokenisation and Normalisation) is currently more effective than Phase 2 text preprocessing (Stop Words Removal and Stemming/Lemmatisation). To repair the less effective Phase 2 text preprocessing caused by unwanted false mappings, we propose a novel context-based pipeline repair approach that employs an ad hoc check to find common words that cause false mappings. These words are stored in a reserved word set and applied in text preprocessing. The experimental results show that our approach improves the matching correctness and the overall matching performance. We also discuss the integration of the classical text preprocessing pipeline with modern large language models (LLMs). We recommend that LLMs inject the text preprocessing pipeline via function calling to avoid the tendency towards unstable true mappings produced by prompt-based LLM approaches, and use LLMs to repair false mappings generated by the text preprocessing pipeline.

**Link**: [arxiv](http://arxiv.org/abs/2411.03962v4),  [pdf](http://arxiv.org/pdf/2411.03962v4)

**Tags**: cs.CL 



### Large Language Model(LLM) assisted End-to-End Network Health Management   based on Multi-Scale Semanticization
**Authors**: Fengxiao Tang, Xiaonan Wang, Xun Yuan, Linfeng Luo, Ming Zhao, Tianchi Huang, Nei Kato

**Updated**: 2025-03-02T13:20:37Z

**Summary**: Network device and system health management is the foundation of modern network operations and maintenance. Traditional health management methods, relying on expert identification or simple rule-based algorithms, struggle to cope with the dynamic heterogeneous networks (DHNs) environment. Moreover, current state-of-the-art distributed anomaly detection methods, which utilize specific machine learning techniques, lack multi-scale adaptivity for heterogeneous device information, resulting in unsatisfactory diagnostic accuracy for DHNs. In this paper, we develop an LLM-assisted end-to-end intelligent network health management framework. The framework first proposes a Multi-Scale Semanticized Anomaly Detection Model (MSADM), incorporating semantic rule trees with an attention mechanism to address the multi-scale anomaly detection problem in DHNs. Secondly, a chain-of-thought-based large language model is embedded in downstream to adaptively analyze the fault detection results and produce an analysis report with detailed fault information and optimization strategies. Experimental results show that the accuracy of our proposed MSADM for heterogeneous network entity anomaly detection is as high as 91.31\%.

**Link**: [arxiv](http://arxiv.org/abs/2406.08305v2),  [pdf](http://arxiv.org/pdf/2406.08305v2)

**Tags**: cs.NI eess.SP 



### Boosting Jailbreak Attack with Momentum
**Authors**: Yihao Zhang, Zeming Wei

**Updated**: 2025-03-02T12:27:07Z

**Summary**: Large Language Models (LLMs) have achieved remarkable success across diverse tasks, yet they remain vulnerable to adversarial attacks, notably the well-known jailbreak attack. In particular, the Greedy Coordinate Gradient (GCG) attack has demonstrated efficacy in exploiting this vulnerability by optimizing adversarial prompts through a combination of gradient heuristics and greedy search. However, the efficiency of this attack has become a bottleneck in the attacking process. To mitigate this limitation, in this paper we rethink the generation of the adversarial prompts through an optimization lens, aiming to stabilize the optimization process and harness more heuristic insights from previous optimization iterations. Specifically, we propose the \textbf{M}omentum \textbf{A}ccelerated G\textbf{C}G (\textbf{MAC}) attack, which integrates a momentum term into the gradient heuristic to boost and stabilize the random search for tokens in adversarial prompts. Experimental results showcase the notable enhancement achieved by MAC over baselines in terms of attack success rate and optimization efficiency. Moreover, we demonstrate that MAC can still exhibit superior performance for transfer attacks and models under defense mechanisms. Our code is available at https://github.com/weizeming/momentum-attack-llm.

**Link**: [arxiv](http://arxiv.org/abs/2405.01229v2),  [pdf](http://arxiv.org/pdf/2405.01229v2)

**Tags**: cs.LG cs.AI cs.CL cs.CR math.OC 



### Derailer-Rerailer: Adaptive Verification for Efficient and Reliable   Language Model Reasoning
**Authors**: Guangya Wan, Yuqi Wu, Hao Wang, Shengming Zhao, Jie Chen, Sheng Li

**Updated**: 2025-03-02T12:11:13Z

**Summary**: Large Language Models (LLMs) have shown impressive reasoning capabilities, yet existing prompting methods face a critical trade-off: simple approaches often struggle with complex tasks and reasoning stability, while more sophisticated methods require multiple inferences and substantial computational resources, limiting their practical deployment. To address this challenge, we propose Derailer-Rerailer, a novel framework that adaptively balances reasoning accuracy and computational efficiency. At its core, our framework employs a lightweight Derailer mechanism to assess reasoning stability and selectively triggers an advanced Rerailer verification process only when necessary, thereby optimizing computational resource usage. Extensive evaluation across both open and closed-source models on more than 20 categories of mathematical, symbolic, and commonsense reasoning tasks demonstrates our framework's effectiveness: Derailer-Rerailer achieves significant accuracy improvements (8-11\% across various reasoning tasks) while maintaining 2-3 times better efficiency than existing verification methods, with particularly strong performance in mathematical and symbolic reasoning, offering a practical solution for enhancing LLM reasoning reliability while significantly reducing computational overhead.

**Link**: [arxiv](http://arxiv.org/abs/2408.13940v3),  [pdf](http://arxiv.org/pdf/2408.13940v3)

**Tags**: cs.CL 



### FOSP: Fine-tuning Offline Safe Policy through World Models
**Authors**: Chenyang Cao, Yucheng Xin, Silang Wu, Longxiang He, Zichen Yan, Junbo Tan, Xueqian Wang

**Updated**: 2025-03-02T11:55:15Z

**Summary**: Offline Safe Reinforcement Learning (RL) seeks to address safety constraints by learning from static datasets and restricting exploration. However, these approaches heavily rely on the dataset and struggle to generalize to unseen scenarios safely. In this paper, we aim to improve safety during the deployment of vision-based robotic tasks through online fine-tuning an offline pretrained policy. To facilitate effective fine-tuning, we introduce model-based RL, which is known for its data efficiency. Specifically, our method employs in-sample optimization to improve offline training efficiency while incorporating reachability guidance to ensure safety. After obtaining an offline safe policy, a safe policy expansion approach is leveraged for online fine-tuning. The performance of our method is validated on simulation benchmarks with five vision-only tasks and through real-world robot deployment using limited data. It demonstrates that our approach significantly improves the generalization of offline policies to unseen safety-constrained scenarios. To the best of our knowledge, this is the first work to explore offline-to-online RL for safe generalization tasks.

**Link**: [arxiv](http://arxiv.org/abs/2407.04942v2),  [pdf](http://arxiv.org/pdf/2407.04942v2)

**Tags**: cs.RO cs.LG 



### Taxonomy, Opportunities, and Challenges of Representation Engineering   for Large Language Models
**Authors**: Jan Wehner, Sahar Abdelnabi, Daniel Tan, David Krueger, Mario Fritz

**Updated**: 2025-03-02T11:23:58Z

**Summary**: Representation Engineering (RepE) is a novel paradigm for controlling the behavior of LLMs. Unlike traditional approaches that modify inputs or fine-tune the model, RepE directly manipulates the model's internal representations. As a result, it may offer more effective, interpretable, data-efficient, and flexible control over models' behavior. We present the first comprehensive survey of RepE for LLMs, reviewing the rapidly growing literature to address key questions: What RepE methods exist and how do they differ? For what concepts and problems has RepE been applied? What are the strengths and weaknesses of RepE compared to other methods? To answer these, we propose a unified framework describing RepE as a pipeline comprising representation identification, operationalization, and control. We posit that while RepE methods offer significant potential, challenges remain, including managing multiple concepts, ensuring reliability, and preserving models' performance. Towards improving RepE, we identify opportunities for experimental and methodological improvements and construct a guide for best practices.

**Link**: [arxiv](http://arxiv.org/abs/2502.19649v2),  [pdf](http://arxiv.org/pdf/2502.19649v2)

**Tags**: cs.LG cs.CL 



### Discovery of novel antimicrobial peptides with notable antibacterial   potency by a LLM-based foundation model
**Authors**: Jike Wang, Jianwen Feng, Yu Kang, Peichen Pan, Jingxuan Ge, Yan Wang, Mingyang Wang, Zhenxing Wu, Xingcai Zhang, Jiameng Yu, Xujun Zhang, Tianyue Wang, Lirong Wen, Guangning Yan, Yafeng Deng, Hui Shi, Chang-Yu Hsieh, Zhihui Jiang, Tingjun Hou

**Updated**: 2025-03-02T11:01:34Z

**Summary**: Large language models (LLMs) have shown remarkable advancements in chemistry and biomedical research, acting as versatile foundation models for various tasks. We introduce AMP-Designer, an LLM-based approach for swiftly designing novel antimicrobial peptides (AMPs) with desired properties. Within 11 days, AMP-Designer achieved the de novo design of 18 AMPs with broad-spectrum activity against Gram-negative bacteria. In vitro validation revealed a 94.4% success rate, with two candidates demonstrating exceptional antibacterial efficacy, minimal hemotoxicity, stability in human plasma, and low potential to induce resistance, as evidenced by significant bacterial load reduction in murine lung infection experiments. The entire process, from design to validation, concluded in 48 days. AMP-Designer excels in creating AMPs targeting specific strains despite limited data availability, with a top candidate displaying a minimum inhibitory concentration of 2.0 {\mu}g/ml against Propionibacterium acnes. Integrating advanced machine learning techniques, AMP-Designer demonstrates remarkable efficiency, paving the way for innovative solutions to antibiotic resistance.

**Link**: [arxiv](http://arxiv.org/abs/2407.12296v2),  [pdf](http://arxiv.org/pdf/2407.12296v2)

**Tags**: q-bio.BM 



### An Attention-Assisted Multi-Modal Data Fusion Model for Real-Time   Estimation of Underwater Sound Velocity
**Authors**: Pengfei Wu, Wei Huang, Yujie Shi, Hao Zhang

**Updated**: 2025-03-02T09:42:13Z

**Summary**: The estimation of underwater sound velocity distribution serves as a critical basis for facilitating effective underwater communication and precise positioning, given that variations in sound velocity influence the path of signal transmission. Conventional techniques for the direct measurement of sound velocity, as well as methods that involve the inversion of sound velocity utilizing acoustic field data, necessitate on--site data collection. This requirement not only places high demands on device deployment, but also presents challenges in achieving real-time estimation of sound velocity distribution. In order to construct a real-time sound velocity field and eliminate the need for underwater onsite data measurement operations, we propose a self-attention embedded multimodal data fusion convolutional neural network (SA-MDF-CNN) for real-time underwater sound speed profile (SSP) estimation. The proposed model seeks to elucidate the inherent relationship between remote sensing sea surface temperature (SST) data, the primary component characteristics of historical SSPs, and their spatial coordinates. This is achieved by employing CNNs and attention mechanisms to extract local and global correlations from the input data, respectively. The ultimate objective is to facilitate a rapid and precise estimation of sound velocity distribution within a specified task area. Experimental results show that the method proposed in this paper has lower root mean square error (RMSE) and stronger robustness than other state-of-the-art methods.

**Link**: [arxiv](http://arxiv.org/abs/2502.12817v3),  [pdf](http://arxiv.org/pdf/2502.12817v3)

**Tags**: eess.SP cs.SD 



### Curriculum-style Data Augmentation for LLM-based Metaphor Detection
**Authors**: Kaidi Jia, Yanxia Wu, Ming Liu, Rongsheng Li

**Updated**: 2025-03-02T09:35:28Z

**Summary**: Recently, utilizing large language models (LLMs) for metaphor detection has achieved promising results. However, these methods heavily rely on the capabilities of closed-source LLMs, which come with relatively high inference costs and latency. To address this, we propose a method for metaphor detection by fine-tuning open-source LLMs, effectively reducing inference costs and latency with a single inference step. Furthermore, metaphor detection suffers from a severe data scarcity problem, which hinders effective fine-tuning of LLMs. To tackle this, we introduce Curriculum-style Data Augmentation (CDA). Specifically, before fine-tuning, we evaluate the training data to identify correctly predicted instances for fine-tuning, while incorrectly predicted instances are used as seed data for data augmentation. This approach enables the model to quickly learn simpler knowledge and progressively acquire more complex knowledge, thereby improving performance incrementally. Experimental results demonstrate that our method achieves state-of-the-art performance across all baselines. Additionally, we provide detailed ablation studies to validate the effectiveness of CDA.

**Link**: [arxiv](http://arxiv.org/abs/2412.02956v2),  [pdf](http://arxiv.org/pdf/2412.02956v2)

**Tags**: cs.CL 



