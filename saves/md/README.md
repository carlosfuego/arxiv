# Arxiv Results
## Keyword: kv cache 
 ### Multi-Strided Access Patterns to Boost Hardware Prefetching
**Authors**: Miguel O. Blom, Kristian F. D. Rietveld, Rob V. van Nieuwpoort

**Updated**: 2024-12-20T15:51:42Z

**Summary**: Important memory-bound kernels, such as linear algebra, convolutions, and stencils, rely on SIMD instructions as well as optimizations targeting improved vectorized data traversal and data re-use to attain satisfactory performance. On on temporary CPU architectures, the hardware prefetcher is of key importance for efficient utilization of the memory hierarchy. In this paper, we demonstrate that transforming a memory access pattern consisting of a single stride to one that concurrently accesses multiple strides, can boost the utilization of the hardware prefetcher, and in turn improves the performance of memory-bound kernels significantly. Using a set of micro-benchmarks, we establish that accessing memory in a multi-strided manner enables more cache lines to be concurrently brought into the cache, resulting in improved cache hit ratios and higher effective memory bandwidth without the introduction of costly software prefetch instructions. Subsequently, we show that multi-strided variants of a collection of six memory-bound dense compute kernels outperform state-of-the-art counterparts on three different micro-architectures. More specifically, for kernels among which Matrix Vector Multiplication, Convolution Stencil and kernels from PolyBench, we achieve significant speedups of up to 12.55x over Polly, 2.99x over MKL, 1.98x over OpenBLAS, 1.08x over Halide and 1.87x over OpenCV. The code transformation to take advantage of multi-strided memory access is a natural extension of the loop unroll and loop interchange techniques, allowing this method to be incorporated into compiler pipelines in the future.

**Link**: [arxiv](http://arxiv.org/abs/2412.16001v1),  [pdf](http://arxiv.org/pdf/2412.16001v1)

**Tags**: cs.PF 



### Towards Projected and Incremental Pseudo-Boolean Model Counting
**Authors**: Suwei Yang, Kuldeep S. Meel

**Updated**: 2024-12-20T15:18:44Z

**Summary**: Model counting is a fundamental task that involves determining the number of satisfying assignments to a logical formula, typically in conjunctive normal form (CNF). While CNF model counting has received extensive attention over recent decades, interest in Pseudo-Boolean (PB) model counting is just emerging partly due to the greater flexibility of PB formulas. As such, we observed feature gaps in existing PB counters such as a lack of support for projected and incremental settings, which could hinder adoption. In this work, our main contribution is the introduction of the PB model counter PBCount2, the first exact PB model counter with support for projected and incremental model counting. Our counter, PBCount2, uses our Least Occurrence Weighted Min Degree (LOW-MD) computation ordering heuristic to support projected model counting and a cache mechanism to enable incremental model counting. In our evaluations, PBCount2 completed at least 1.40x the number of benchmarks of competing methods for projected model counting and at least 1.18x of competing methods in incremental model counting.

**Link**: [arxiv](http://arxiv.org/abs/2412.14485v2),  [pdf](http://arxiv.org/pdf/2412.14485v2)

**Tags**: cs.AI cs.LO 



### Don't Do RAG: When Cache-Augmented Generation is All You Need for   Knowledge Tasks
**Authors**: Brian J Chan, Chao-Ting Chen, Jui-Hung Cheng, Hen-Hsen Huang

**Updated**: 2024-12-20T06:58:32Z

**Summary**: Retrieval-augmented generation (RAG) has gained traction as a powerful approach for enhancing language models by integrating external knowledge sources. However, RAG introduces challenges such as retrieval latency, potential errors in document selection, and increased system complexity. With the advent of large language models (LLMs) featuring significantly extended context windows, this paper proposes an alternative paradigm, cache-augmented generation (CAG) that bypasses real-time retrieval. Our method involves preloading all relevant resources, especially when the documents or knowledge for retrieval are of a limited and manageable size, into the LLM's extended context and caching its runtime parameters. During inference, the model utilizes these preloaded parameters to answer queries without additional retrieval steps. Comparative analyses reveal that CAG eliminates retrieval latency and minimizes retrieval errors while maintaining context relevance. Performance evaluations across multiple benchmarks highlight scenarios where long-context LLMs either outperform or complement traditional RAG pipelines. These findings suggest that, for certain applications, particularly those with a constrained knowledge base, CAG provide a streamlined and efficient alternative to RAG, achieving comparable or superior results with reduced complexity.

**Link**: [arxiv](http://arxiv.org/abs/2412.15605v1),  [pdf](http://arxiv.org/pdf/2412.15605v1)

**Tags**: cs.CL 



### DroidSpeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM   Serving
**Authors**: Yuhan Liu, Yuyang Huang, Jiayi Yao, Zhuohan Gu, Kuntai Du, Hanchen Li, Yihua Cheng, Junchen Jiang, Shan Lu, Madan Musuvathi, Esha Choukse

**Updated**: 2024-12-19T23:52:16Z

**Summary**: Large Language Models (LLMs) are increasingly employed in complex workflows, where different LLMs and fine-tuned variants collaboratively address complex tasks. However, these systems face significant inefficiencies due to redundant context processing of the shared context. We propose DroidSpeak, a framework that optimizes context sharing between fine-tuned LLMs derived from the same foundational model. DroidSpeak identifies critical layers in the KV cache and selectively recomputes them, enabling effective reuse of intermediate data while maintaining high accuracy.   Our approach balances computational efficiency and task fidelity, significantly reducing inference latency and throughput bottlenecks. Experiments on diverse datasets and model pairs demonstrate that DroidSpeak achieves up to 3x higher throughputs and 2.6x faster prefill times with negligible accuracy loss compared to full recomputation.

**Link**: [arxiv](http://arxiv.org/abs/2411.02820v3),  [pdf](http://arxiv.org/pdf/2411.02820v3)

**Tags**: cs.MA cs.AI cs.CL cs.LG 



### Exposing Shadow Branches
**Authors**: Chrysanthos Pepi, Bhargav Reddy Godala, Krishnam Tibrewala, Gino Chacon, Paul V. Gratz, Daniel A. Jiménez, Gilles A. Pokam, David I. August

**Updated**: 2024-12-19T22:34:37Z

**Summary**: Modern processors implement a decoupled front-end in the form of Fetch Directed Instruction Prefetching (FDIP) to avoid front-end stalls. FDIP is driven by the Branch Prediction Unit (BPU), relying on the BPU's accuracy and branch target tracking structures to speculatively fetch instructions into the Instruction Cache (L1I). As data center applications become more complex, their code footprints also grow, resulting in an increase in Branch Target Buffer (BTB) misses. FDIP can alleviate L1I cache misses, but when it encounters a BTB miss, the BPU may not identify the current instruction as a branch to FDIP. This can prevent FDIP from prefetching or cause it to speculate down the wrong path, further polluting the L1I cache. We observe that the vast majority, 75%, of BTB-missing, unidentified branches are actually present in instruction cache lines that FDIP has previously fetched but, these missing branches have not yet been decoded and inserted into the BTB. This is because the instruction line is decoded from an entry point (which is the target of the previous taken branch) till an exit point (the taken branch). Branch instructions present in the ignored portion of the cache line we call them "Shadow Branches". Here we present Skeia, a novel shadow branch decoding technique that identifies and decodes unused bytes in cache lines fetched by FDIP, inserting them into a Shadow Branch Buffer (SBB). The SBB is accessed in parallel with the BTB, allowing FDIP to speculate despite a BTB miss. With a minimal storage state of 12.25KB, Skeia delivers a geomean speedup of ~5.7% over an 8K-entry BTB (78KB) and ~2% versus adding an equal amount of state to the BTB across 16 front-end bound applications. Since many branches stored in the SBB are unique compared to those in a similarly sized BTB, we consistently observe greater performance gains with Skeia across all examined sizes until saturation.

**Link**: [arxiv](http://arxiv.org/abs/2408.12592v2),  [pdf](http://arxiv.org/pdf/2408.12592v2)

**Tags**: cs.AR 



### DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context   LLMs
**Authors**: Xiabin Zhou, Wenbin Wang, Minyan Zeng, Jiaxian Guo, Xuebo Liu, Li Shen, Min Zhang, Liang Ding

**Updated**: 2024-12-19T13:28:42Z

**Summary**: Efficient KV cache management in LLMs is crucial for long-context tasks like RAG and summarization. Existing KV cache compression methods enforce a fixed pattern, neglecting task-specific characteristics and reducing the retention of essential information. However, we observe distinct activation patterns across layers in various tasks, highlighting the need for adaptive strategies tailored to each task's unique demands. Based on this insight, we propose DynamicKV, a method that dynamically optimizes token retention by adjusting the number of tokens retained at each layer to adapt to the specific task. DynamicKV establishes global and per-layer maximum KV cache budgets, temporarily retaining the maximum budget for the current layer, and periodically updating the KV cache sizes of all preceding layers during inference. Our method retains only 1.7% of the KV cache size while achieving ~85% of the Full KV cache performance on LongBench. Notably, even under extreme compression (0.9%), DynamicKV surpasses state-of-the-art (SOTA) methods by 11% in the Needle-in-a-Haystack test using Mistral-7B-Instruct-v0.2. The code will be released.

**Link**: [arxiv](http://arxiv.org/abs/2412.14838v1),  [pdf](http://arxiv.org/pdf/2412.14838v1)

**Tags**: cs.CL 



### Accelerating Diffusion Transformers with Token-wise Feature Caching
**Authors**: Chang Zou, Xuyang Liu, Ting Liu, Siteng Huang, Linfeng Zhang

**Updated**: 2024-12-19T12:38:23Z

**Summary**: Diffusion transformers have shown significant effectiveness in both image and video synthesis at the expense of huge computation costs. To address this problem, feature caching methods have been introduced to accelerate diffusion transformers by caching the features in previous timesteps and reusing them in the following timesteps. However, previous caching methods ignore that different tokens exhibit different sensitivities to feature caching, and feature caching on some tokens may lead to 10$\times$ more destruction to the overall generation quality compared with other tokens. In this paper, we introduce token-wise feature caching, allowing us to adaptively select the most suitable tokens for caching, and further enable us to apply different caching ratios to neural layers in different types and depths. Extensive experiments on PixArt-$\alpha$, OpenSora, and DiT demonstrate our effectiveness in both image and video generation with no requirements for training. For instance, 2.36$\times$ and 1.93$\times$ acceleration are achieved on OpenSora and PixArt-$\alpha$ with almost no drop in generation quality.

**Link**: [arxiv](http://arxiv.org/abs/2410.05317v3),  [pdf](http://arxiv.org/pdf/2410.05317v3)

**Tags**: cs.LG cs.AI cs.CV 



### Nemesis: Noise-randomized Encryption with Modular Efficiency and Secure   Integration in Machine Learning Systems
**Authors**: Dongfang Zhao

**Updated**: 2024-12-18T22:52:12Z

**Summary**: Machine learning (ML) systems that guarantee security and privacy often rely on Fully Homomorphic Encryption (FHE) as a cornerstone technique, enabling computations on encrypted data without exposing sensitive information. However, a critical limitation of FHE is its computational inefficiency, making it impractical for large-scale applications. In this work, we propose \textit{Nemesis}, a framework that accelerates FHE-based systems without compromising accuracy or security. The design of Nemesis is inspired by Rache (SIGMOD'23), which introduced a caching mechanism for encrypted integers and scalars. Nemesis extends this idea with more advanced caching techniques and mathematical tools, enabling efficient operations over multi-slot FHE schemes and overcoming Rache's limitations to support general plaintext structures. We formally prove the security of Nemesis under standard cryptographic assumptions and evaluate its performance extensively on widely used datasets, including MNIST, FashionMNIST, and CIFAR-10. Experimental results show that Nemesis significantly reduces the computational overhead of FHE-based ML systems, paving the way for broader adoption of privacy-preserving technologies.

**Link**: [arxiv](http://arxiv.org/abs/2412.14392v1),  [pdf](http://arxiv.org/pdf/2412.14392v1)

**Tags**: cs.CR cs.LG 



### ResQ: Mixed-Precision Quantization of Large Language Models with   Low-Rank Residuals
**Authors**: Utkarsh Saxena, Sayeh Sharify, Kaushik Roy, Xin Wang

**Updated**: 2024-12-18T22:01:55Z

**Summary**: Post-training quantization (PTQ) of large language models (LLMs) holds the promise in reducing the prohibitive computational cost at inference time. Quantization of all weight, activation and key-value (KV) cache tensors to 4-bit without significantly degrading generalizability is challenging, due to the high quantization error caused by extreme outliers in activations. To tackle this problem, we propose ResQ, a PTQ method that pushes further the state-of-the-art. By means of principal component analysis (PCA), it identifies a low-rank subspace (in practice 1/8 of the hidden dimension) in which activation variances are highest, and keep the coefficients within this subspace in high precision, e.g. 8-bit, while quantizing the rest to 4-bit. Within each subspace, invariant random rotation is applied to further suppress outliers. We show that this is a provably optimal mixed precision quantization scheme that minimizes error. With the Llama families of models, we demonstrate that ResQ outperforms recent uniform and mixed precision PTQ methods on a variety of benchmarks, achieving up to 33% lower perplexity on Wikitext than the next best method SpinQuant, and a 2.4x speedup over 16-bit baseline. Code is available at https://github.com/utkarsh-dmx/project-resq.

**Link**: [arxiv](http://arxiv.org/abs/2412.14363v1),  [pdf](http://arxiv.org/pdf/2412.14363v1)

**Tags**: cs.LG cs.CL 



### Optimizing ML Concurrent Computation and Communication with GPU DMA   Engines
**Authors**: Anirudha Agrawal, Shaizeen Aga, Suchita Pati, Mahzabeen Islam

**Updated**: 2024-12-18T21:09:08Z

**Summary**: Concurrent computation and communication (C3) is a pervasive paradigm in ML and other domains, making its performance optimization crucial. In this paper, we carefully characterize C3 in ML on GPUs, which are most widely deployed for ML training and inference. We observe that while C3 leads to performance uplifts, the uplifts are far lower than ideal speedups (serial computation and communication versus maximum of computation or communication; all times from isolated executions). C3 on average achieves only 21% of ideal speedup, this is due to known challenges of compute and memory interference between concurrent GPU kernels (that is, sharing of GPU's compute units, caches and HBM).   To attain better performance for C3, first, we evaluate dual strategies of schedule prioritization and careful resource partitioning of compute units on GPUs to push performance attained with C3 (on average 42% of ideal speedup). We also provide heuristics that can guide a runtime while employing these strategies. To further enhance C3 performance, we propose to mitigate C3 interference by offloading communication tasks to the GPU's DMA engines. To this end, we build Concurrent Communication CoLlectives (ConCCL) proof-of-concepts that harness DMA engines for communication. We show how ConCCL considerably closes the gap between realized and ideal speedup for C3 (on average 72% of ideal speedup is realized, up to 1.67x speedup). Overall, our work makes a strong case for GPU DMA engine advancements to better support C3 on GPUs.

**Link**: [arxiv](http://arxiv.org/abs/2412.14335v1),  [pdf](http://arxiv.org/pdf/2412.14335v1)

**Tags**: cs.AR cs.DC 



### MagicPIG: LSH Sampling for Efficient LLM Generation
**Authors**: Zhuoming Chen, Ranajoy Sadhukhan, Zihao Ye, Yang Zhou, Jianyu Zhang, Niklas Nolte, Yuandong Tian, Matthijs Douze, Leon Bottou, Zhihao Jia, Beidi Chen

**Updated**: 2024-12-18T17:36:36Z

**Summary**: Large language models (LLMs) with long context windows have gained significant attention. However, the KV cache, stored to avoid re-computation, becomes a bottleneck. Various dynamic sparse or TopK-based attention approximation methods have been proposed to leverage the common insight that attention is sparse. In this paper, we first show that TopK attention itself suffers from quality degradation in certain downstream tasks because attention is not always as sparse as expected. Rather than selecting the keys and values with the highest attention scores, sampling with theoretical guarantees can provide a better estimation for attention output. To make the sampling-based approximation practical in LLM generation, we propose MagicPIG, a heterogeneous system based on Locality Sensitive Hashing (LSH). MagicPIG significantly reduces the workload of attention computation while preserving high accuracy for diverse tasks. MagicPIG stores the LSH hash tables and runs the attention computation on the CPU, which allows it to serve longer contexts and larger batch sizes with high approximation accuracy. MagicPIG can improve decoding throughput by up to $5\times$ across various GPU hardware and achieve 54ms decoding latency on a single RTX 4090 for Llama-3.1-8B-Instruct model with a context of 96k tokens. The code is available at https://github.com/Infini-AI-Lab/MagicPIG.

**Link**: [arxiv](http://arxiv.org/abs/2410.16179v4),  [pdf](http://arxiv.org/pdf/2410.16179v4)

**Tags**: cs.CL cs.LG 



### Rehearsal-Free Continual Federated Learning with Synergistic   Regularization
**Authors**: Yichen Li, Yuying Wang, Tianzhe Xiao, Haozhao Wang, Yining Qi, Ruixuan Li

**Updated**: 2024-12-18T12:16:41Z

**Summary**: Continual Federated Learning (CFL) allows distributed devices to collaboratively learn novel concepts from continuously shifting training data while avoiding knowledge forgetting of previously seen tasks. To tackle this challenge, most current CFL approaches rely on extensive rehearsal of previous data. Despite effectiveness, rehearsal comes at a cost to memory, and it may also violate data privacy. Considering these, we seek to apply regularization techniques to CFL by considering their cost-efficient properties that do not require sample caching or rehearsal. Specifically, we first apply traditional regularization techniques to CFL and observe that existing regularization techniques, especially synaptic intelligence, can achieve promising results under homogeneous data distribution but fail when the data is heterogeneous. Based on this observation, we propose a simple yet effective regularization algorithm for CFL named FedSSI, which tailors the synaptic intelligence for the CFL with heterogeneous data settings. FedSSI can not only reduce computational overhead without rehearsal but also address the data heterogeneity issue. Extensive experiments show that FedSSI achieves superior performance compared to state-of-the-art methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.13779v1),  [pdf](http://arxiv.org/pdf/2412.13779v1)

**Tags**: cs.LG cs.DC 



### Semantic Convergence: Harmonizing Recommender Systems via Two-Stage   Alignment and Behavioral Semantic Tokenization
**Authors**: Guanghan Li, Xun Zhang, Yufei Zhang, Yifan Yin, Guojun Yin, Wei Lin

**Updated**: 2024-12-18T12:07:58Z

**Summary**: Large language models (LLMs), endowed with exceptional reasoning capabilities, are adept at discerning profound user interests from historical behaviors, thereby presenting a promising avenue for the advancement of recommendation systems. However, a notable discrepancy persists between the sparse collaborative semantics typically found in recommendation systems and the dense token representations within LLMs. In our study, we propose a novel framework that harmoniously merges traditional recommendation models with the prowess of LLMs. We initiate this integration by transforming ItemIDs into sequences that align semantically with the LLMs space, through the proposed Alignment Tokenization module. Additionally, we design a series of specialized supervised learning tasks aimed at aligning collaborative signals with the subtleties of natural language semantics. To ensure practical applicability, we optimize online inference by pre-caching the top-K results for each user, reducing latency and improving effciency. Extensive experimental evidence indicates that our model markedly improves recall metrics and displays remarkable scalability of recommendation systems.

**Link**: [arxiv](http://arxiv.org/abs/2412.13771v1),  [pdf](http://arxiv.org/pdf/2412.13771v1)

**Tags**: cs.IR cs.AI cs.CL 



### DyCoke: Dynamic Compression of Tokens for Fast Video Large Language   Models
**Authors**: Keda Tao, Can Qin, Haoxuan You, Yang Sui, Huan Wang

**Updated**: 2024-12-18T09:47:25Z

**Summary**: Video large language models (VLLMs) have significantly advanced recently in processing complex video content, yet their inference efficiency remains constrained because of the high computational cost stemming from the thousands of visual tokens generated from the video inputs. We empirically observe that, unlike single image inputs, VLLMs typically attend visual tokens from different frames at different decoding iterations, making a one-shot pruning strategy prone to removing important tokens by mistake. Motivated by this, we present DyCoke, a training-free token compression method to optimize token representation and accelerate VLLMs. DyCoke incorporates a plug-and-play temporal compression module to minimize temporal redundancy by merging redundant tokens across frames, and applies dynamic KV cache reduction to prune spatially redundant tokens selectively. It ensures high-quality inference by dynamically retaining the critical tokens at each decoding step. Extensive experimental results demonstrate that DyCoke can outperform the prior SoTA counterparts, achieving 1.5X inference speedup, 1.4X memory reduction against the baseline VLLM, while still improving the performance, with no training.

**Link**: [arxiv](http://arxiv.org/abs/2411.15024v2),  [pdf](http://arxiv.org/pdf/2411.15024v2)

**Tags**: cs.CV cs.LG 



### SCOPE: Optimizing Key-Value Cache Compression in Long-context Generation
**Authors**: Jialong Wu, Zhenglin Wang, Linhai Zhang, Yilong Lai, Yulan He, Deyu Zhou

**Updated**: 2024-12-18T09:27:33Z

**Summary**: Key-Value (KV) cache has become a bottleneck of LLMs for long-context generation. Despite the numerous efforts in this area, the optimization for the decoding phase is generally ignored. However, we believe such optimization is crucial, especially for long-output generation tasks based on the following two observations: (i) Excessive compression during the prefill phase, which requires specific full context impairs the comprehension of the reasoning task; (ii) Deviation of heavy hitters occurs in the reasoning tasks with long outputs. Therefore, SCOPE, a simple yet efficient framework that separately performs KV cache optimization during the prefill and decoding phases, is introduced. Specifically, the KV cache during the prefill phase is preserved to maintain the essential information, while a novel strategy based on sliding is proposed to select essential heavy hitters for the decoding phase. Memory usage and memory transfer are further optimized using adaptive and discontinuous strategies. Extensive experiments on LongGenBench show the effectiveness and generalization of SCOPE and its compatibility as a plug-in to other prefill-only KV compression methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.13649v1),  [pdf](http://arxiv.org/pdf/2412.13649v1)

**Tags**: cs.CL 



### ZipVL: Efficient Large Vision-Language Models with Dynamic Token   Sparsification
**Authors**: Yefei He, Feng Chen, Jing Liu, Wenqi Shao, Hong Zhou, Kaipeng Zhang, Bohan Zhuang

**Updated**: 2024-12-18T07:45:11Z

**Summary**: The efficiency of large vision-language models (LVLMs) is constrained by the computational bottleneck of the attention mechanism during the prefill phase and the memory bottleneck of fetching the key-value (KV) cache in the decoding phase, particularly in scenarios involving high-resolution images or videos. Visual content often exhibits substantial redundancy, resulting in highly sparse attention maps within LVLMs. This sparsity can be leveraged to accelerate attention computation or compress the KV cache through various approaches. However, most studies focus on addressing only one of these bottlenecks and do not adequately support dynamic adjustment of sparsity concerning distinct layers or tasks. In this paper, we present ZipVL, an efficient inference framework designed for LVLMs through a dynamic ratio allocation strategy of important tokens. This ratio is adaptively determined based on the layer-specific distribution of attention scores, rather than fixed hyper-parameters, thereby improving efficiency for less complex tasks while maintaining high performance for more challenging ones. Then we select important tokens based on their normalized attention scores and perform sparse attention mechanism solely on those important tokens, reducing the latency in the prefill phase. Tokens deemed less important will be discarded to reduce KV cache size, alleviating the memory bottleneck in the decoding phase. Our experiments demonstrate that ZipVL can accelerate the prefill phase by 2.3$\times$ and improve decoding throughput by 2.8$\times$, with a minimal accuracy reduction of only 0.5\% on VQAv2 benchmark over LLaVA-Next-13B model, effectively enhancing the generation efficiency of LVLMs.

**Link**: [arxiv](http://arxiv.org/abs/2410.08584v2),  [pdf](http://arxiv.org/pdf/2410.08584v2)

**Tags**: cs.CV cs.AI 



### Vivar: A Generative AR System for Intuitive Multi-Modal Sensor Data   Presentation
**Authors**: Yunqi Guo, Kaiyuan Hou, Heming Fu, Hongkai Chen, Zhenyu Yan, Guoliang Xing, Xiaofan Jiang

**Updated**: 2024-12-18T05:16:11Z

**Summary**: Understanding sensor data can be challenging for non-experts because of the complexity and unique semantic meanings of sensor modalities. This calls for intuitive and effective methods to present sensor information. However, creating intuitive sensor data visualizations presents three key challenges: the variability of sensor readings, gaps in domain comprehension, and the dynamic nature of sensor data. To address these issues, we develop Vivar, a novel AR system that integrates multi-modal sensor data and presents 3D volumetric content for visualization. In particular, we introduce a cross-modal embedding approach that maps sensor data into a pre-trained visual embedding space through barycentric interpolation. This allows for accurate and continuous integration of multi-modal sensor information. Vivar also incorporates sensor-aware AR scene generation using foundation models and 3D Gaussian Splatting (3DGS) without requiring domain expertise. In addition, Vivar leverages latent reuse and caching strategies to accelerate 2D and AR content generation. Our extensive experiments demonstrate that our system achieves 11$\times$ latency reduction without compromising quality. A user study involving over 485 participants, including domain experts, demonstrates Vivar's effectiveness in accuracy, consistency, and real-world applicability, paving the way for more intuitive sensor data visualization.

**Link**: [arxiv](http://arxiv.org/abs/2412.13509v1),  [pdf](http://arxiv.org/pdf/2412.13509v1)

**Tags**: cs.HC 



### Boosting Long-Context Management via Query-Guided Activation Refilling
**Authors**: Hongjin Qian, Zheng Liu, Peitian Zhang, Zhicheng Dou, Defu Lian

**Updated**: 2024-12-18T05:08:39Z

**Summary**: Processing long contexts poses a significant challenge for large language models (LLMs) due to their inherent context-window limitations and the computational burden of extensive key-value (KV) activations, which severely impact efficiency. For information-seeking tasks, full context perception is often unnecessary, as a query's information needs can dynamically range from localized details to a global perspective, depending on its complexity. However, existing methods struggle to adapt effectively to these dynamic information needs.   In the paper, we propose a method for processing long-context information-seeking tasks via query-guided Activation Refilling (ACRE). ACRE constructs a Bi-layer KV Cache for long contexts, where the layer-1 (L1) cache compactly captures global information, and the layer-2 (L2) cache provides detailed and localized information. ACRE establishes a proxying relationship between the two caches, allowing the input query to attend to the L1 cache and dynamically refill it with relevant entries from the L2 cache. This mechanism integrates global understanding with query-specific local details, thus improving answer decoding. Experiments on a variety of long-context information-seeking datasets demonstrate ACRE's effectiveness, achieving improvements in both performance and efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12486v2),  [pdf](http://arxiv.org/pdf/2412.12486v2)

**Tags**: cs.CL cs.AI cs.IR 



### SepLLM: Accelerate Large Language Models by Compressing One Segment into   One Separator
**Authors**: Guoxuan Chen, Han Shi, Jiawei Li, Yihang Gao, Xiaozhe Ren, Yimeng Chen, Xin Jiang, Zhenguo Li, Weiyang Liu, Chao Huang

**Updated**: 2024-12-17T20:41:59Z

**Summary**: Large Language Models (LLMs) have exhibited exceptional performance across a spectrum of natural language processing tasks. However, their substantial sizes pose considerable challenges, particularly in computational demands and inference speed, due to their quadratic complexity. In this work, we have identified a key pattern: certain seemingly meaningless special tokens (i.e., separators) contribute disproportionately to attention scores compared to semantically meaningful tokens. This observation suggests that information of the segments between these separator tokens can be effectively condensed into the separator tokens themselves without significant information loss. Guided by this insight, we introduce SepLLM, a plug-and-play framework that accelerates inference by compressing these segments and eliminating redundant tokens. Additionally, we implement efficient kernels for training acceleration. Experimental results across training-free, training-from-scratch, and post-training settings demonstrate SepLLM's effectiveness. Notably, using the Llama-3-8B backbone, SepLLM achieves over 50% reduction in KV cache on the GSM8K-CoT benchmark while maintaining comparable performance. Furthermore, in streaming settings, SepLLM effectively processes sequences of up to 4 million tokens or more while maintaining consistent language modeling capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2412.12094v2),  [pdf](http://arxiv.org/pdf/2412.12094v2)

**Tags**: cs.CL cs.AI cs.LG 



### Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic   Vision-language Context Sparsification
**Authors**: Wenxuan Huang, Zijie Zhai, Yunhang Shen, Shaosheng Cao, Fei Zhao, Xiangfeng Xu, Zheyu Ye, Shaohui Lin

**Updated**: 2024-12-17T14:45:12Z

**Summary**: Multimodal Large Language Models (MLLMs) have achieved remarkable success in vision understanding, reasoning, and interaction. However, the inference computation and memory increase progressively with the generation of output tokens during decoding, directly affecting the efficacy of MLLMs. Existing methods attempt to reduce the vision context redundancy to achieve efficient MLLMs. Unfortunately, the efficiency benefits of the vision context reduction in the prefill stage gradually diminish during the decoding stage. To address this problem, we proposed a dynamic vision-language context sparsification framework Dynamic-LLaVA, which dynamically reduces the redundancy of vision context in the prefill stage and decreases the memory and computation overhead of the generated language context during decoding. Dynamic-LLaVA designs a tailored sparsification inference scheme for different inference modes, i.e., prefill, decoding with and without KV cache, to achieve efficient inference of MLLMs. In practice, Dynamic-LLaVA can reduce computation consumption by $\sim$75\% in the prefill stage. Meanwhile, throughout the entire generation process of MLLMs, Dynamic-LLaVA reduces the $\sim$50\% computation consumption under decoding without KV cache, while saving $\sim$50\% GPU memory overhead when decoding with KV cache, due to the vision-language context sparsification. Extensive experiments also demonstrate that Dynamic-LLaVA achieves efficient inference for MLLMs with negligible understanding and generation ability degradation or even performance gains compared to the full-context inference baselines. Code is available at https://github.com/Osilly/dynamic_llava .

**Link**: [arxiv](http://arxiv.org/abs/2412.00876v3),  [pdf](http://arxiv.org/pdf/2412.00876v3)

**Tags**: cs.CV cs.AI cs.CL cs.LG 



### Efficient Diffusion Transformer Policies with Mixture of Expert   Denoisers for Multitask Learning
**Authors**: Moritz Reuss, Jyothish Pari, Pulkit Agrawal, Rudolf Lioutikov

**Updated**: 2024-12-17T14:34:51Z

**Summary**: Diffusion Policies have become widely used in Imitation Learning, offering several appealing properties, such as generating multimodal and discontinuous behavior. As models are becoming larger to capture more complex capabilities, their computational demands increase, as shown by recent scaling laws. Therefore, continuing with the current architectures will present a computational roadblock. To address this gap, we propose Mixture-of-Denoising Experts (MoDE) as a novel policy for Imitation Learning. MoDE surpasses current state-of-the-art Transformer-based Diffusion Policies while enabling parameter-efficient scaling through sparse experts and noise-conditioned routing, reducing both active parameters by 40% and inference costs by 90% via expert caching. Our architecture combines this efficient scaling with noise-conditioned self-attention mechanism, enabling more effective denoising across different noise levels. MoDE achieves state-of-the-art performance on 134 tasks in four established imitation learning benchmarks (CALVIN and LIBERO). Notably, by pretraining MoDE on diverse robotics data, we achieve 4.01 on CALVIN ABC and 0.95 on LIBERO-90. It surpasses both CNN-based and Transformer Diffusion Policies by an average of 57% across 4 benchmarks, while using 90% fewer FLOPs and fewer active parameters compared to default Diffusion Transformer architectures. Furthermore, we conduct comprehensive ablations on MoDE's components, providing insights for designing efficient and scalable Transformer architectures for Diffusion Policies. Code and demonstrations are available at https://mbreuss.github.io/MoDE_Diffusion_Policy/.

**Link**: [arxiv](http://arxiv.org/abs/2412.12953v1),  [pdf](http://arxiv.org/pdf/2412.12953v1)

**Tags**: cs.LG cs.RO 



### ZoRI: Towards Discriminative Zero-Shot Remote Sensing Instance   Segmentation
**Authors**: Shiqi Huang, Shuting He, Bihan Wen

**Updated**: 2024-12-17T11:00:56Z

**Summary**: Instance segmentation algorithms in remote sensing are typically based on conventional methods, limiting their application to seen scenarios and closed-set predictions. In this work, we propose a novel task called zero-shot remote sensing instance segmentation, aimed at identifying aerial objects that are absent from training data. Challenges arise when classifying aerial categories with high inter-class similarity and intra-class variance. Besides, the domain gap between vision-language models' pretraining datasets and remote sensing datasets hinders the zero-shot capabilities of the pretrained model when it is directly applied to remote sensing images. To address these challenges, we propose a $\textbf{Z}$ero-Sh$\textbf{o}$t $\textbf{R}$emote Sensing $\textbf{I}$nstance Segmentation framework, dubbed $\textbf{ZoRI}$. Our approach features a discrimination-enhanced classifier that uses refined textual embeddings to increase the awareness of class disparities. Instead of direct fine-tuning, we propose a knowledge-maintained adaptation strategy that decouples semantic-related information to preserve the pretrained vision-language alignment while adjusting features to capture remote sensing domain-specific visual cues. Additionally, we introduce a prior-injected prediction with cache bank of aerial visual prototypes to supplement the semantic richness of text embeddings and seamlessly integrate aerial representations, adapting to the remote sensing domain. We establish new experimental protocols and benchmarks, and extensive experiments convincingly demonstrate that ZoRI achieves the state-of-art performance on the zero-shot remote sensing instance segmentation task. Our code is available at https://github.com/HuangShiqi128/ZoRI.

**Link**: [arxiv](http://arxiv.org/abs/2412.12798v1),  [pdf](http://arxiv.org/pdf/2412.12798v1)

**Tags**: cs.CV 



### More Tokens, Lower Precision: Towards the Optimal Token-Precision   Trade-off in KV Cache Compression
**Authors**: Jiebin Zhang, Dawei Zhu, Yifan Song, Wenhao Wu, Chuqiao Kuang, Xiaoguang Li, Lifeng Shang, Qun Liu, Sujian Li

**Updated**: 2024-12-17T09:20:31Z

**Summary**: As large language models (LLMs) process increasing context windows, the memory usage of KV cache has become a critical bottleneck during inference. The mainstream KV compression methods, including KV pruning and KV quantization, primarily focus on either token or precision dimension and seldom explore the efficiency of their combination. In this paper, we comprehensively investigate the token-precision trade-off in KV cache compression. Experiments demonstrate that storing more tokens in the KV cache with lower precision, i.e., quantized pruning, can significantly enhance the long-context performance of LLMs. Furthermore, in-depth analysis regarding token-precision trade-off from a series of key aspects exhibit that, quantized pruning achieves substantial improvements in retrieval-related tasks and consistently performs well across varying input lengths. Moreover, quantized pruning demonstrates notable stability across different KV pruning methods, quantization strategies, and model scales. These findings provide valuable insights into the token-precision trade-off in KV cache compression. We plan to release our code in the near future.

**Link**: [arxiv](http://arxiv.org/abs/2412.12706v1),  [pdf](http://arxiv.org/pdf/2412.12706v1)

**Tags**: cs.CL 



### FiRST: Finetuning Router-Selective Transformers for Input-Adaptive   Latency Reduction
**Authors**: Akriti Jain, Saransh Sharma, Koyel Mukherjee, Soumyabrata Pal

**Updated**: 2024-12-17T09:11:47Z

**Summary**: Auto-regressive Large Language Models (LLMs) demonstrate remarkable performance across different domains such as vision and language processing. However, due to sequential processing through a stack of transformer layers, autoregressive decoding faces significant computation/latency challenges, particularly in resource-constrained environments like mobile and edge devices. Existing approaches in literature that aim to improve latency via skipping layers have two distinct flavors - 1) Early exit, and 2) Input-agnostic heuristics where tokens exit at pre-determined layers irrespective of input sequence. Both the above strategies have limitations - the former cannot be applied to handle KV Caching necessary for speed-ups in modern framework and the latter does not capture the variation in layer importance across tasks or more generally, across input sequences. To address both limitations, we propose FiRST, an algorithm that reduces inference latency by using layer-specific routers to select a subset of transformer layers adaptively for each input sequence - the prompt (during the prefill stage) decides which layers will be skipped during decoding. FiRST preserves compatibility with KV caching enabling faster inference while being quality-aware. FiRST is model-agnostic and can be easily enabled on any pre-trained LLM. Our approach reveals that input adaptivity is critical - indeed, different task-specific middle layers play a crucial role in evolving hidden representations depending on tasks. Extensive experiments show that FiRST significantly reduces latency while outperforming other layer selection strategies in quality metics. It retains competitive performance to base model (without layer skipping) and in some cases, even improves upon it. FiRST is thus a promising and efficient solution for LLM deployment in low-resource environments.

**Link**: [arxiv](http://arxiv.org/abs/2410.12513v2),  [pdf](http://arxiv.org/pdf/2410.12513v2)

**Tags**: cs.CL 



### TurboAttention: Efficient Attention Approximation For High Throughputs   LLMs
**Authors**: Hao Kang, Srikant Bharadwaj, James Hensman, Tushar Krishna, Victor Ruhle, Saravan Rajmohan

**Updated**: 2024-12-17T05:40:09Z

**Summary**: Large language model (LLM) inference demands significant amount of computation and memory, especially in the key attention mechanism. While techniques, such as quantization and acceleration algorithms, like FlashAttention, have improved efficiency of the overall inference, they address different aspects of the problem: quantization focuses on weight-activation operations, while FlashAttention improves execution but requires high-precision formats. Recent Key-value (KV) cache quantization reduces memory bandwidth but still needs floating-point dequantization for attention operation.   We present TurboAttention, a comprehensive approach to enable quantized execution of attention that simultaneously addresses both memory and computational efficiency. Our solution introduces two key innovations: FlashQ, a headwise attention quantization technique that enables both compression of KV cache and quantized execution of activation-activation multiplication, and Sparsity-based Softmax Approximation (SAS), which eliminates the need for dequantization to FP32 during exponentiation operation in attention. Experimental results demonstrate that TurboAttention achieves 1.2-1.8x speedup in attention, reduces the KV cache size by over 4.4x, and enables up to 2.37x maximum throughput over the FP16 baseline while outperforming state-of-the-art quantization and compression techniques across various datasets and models.

**Link**: [arxiv](http://arxiv.org/abs/2412.08585v3),  [pdf](http://arxiv.org/pdf/2412.08585v3)

**Tags**: cs.LG cs.AI cs.AR 



### Personalized Federated Deep Reinforcement Learning for Heterogeneous   Edge Content Caching Networks
**Authors**: Zhen Li, Tan Li, Hai Liu, Tse-Tin Chan

**Updated**: 2024-12-17T05:09:45Z

**Summary**: Proactive caching is essential for minimizing latency and improving Quality of Experience (QoE) in multi-server edge networks. Federated Deep Reinforcement Learning (FDRL) is a promising approach for developing cache policies tailored to dynamic content requests. However, FDRL faces challenges such as an expanding caching action space due to increased content numbers and difficulty in adapting global information to heterogeneous edge environments. In this paper, we propose a Personalized Federated Deep Reinforcement Learning framework for Caching, called PF-DRL-Ca, with the aim to maximize system utility while satisfying caching capability constraints. To manage the expanding action space, we employ a new DRL algorithm, Multi-head Deep Q-Network (MH-DQN), which reshapes the action output layers of DQN into a multi-head structure where each head generates a sub-dimensional action. We next integrate the proposed MH-DQN into a personalized federated training framework, employing a layer-wise approach for training to derive a personalized model that can adapt to heterogeneous environments while exploiting the global information to accelerate learning convergence. Our extensive experimental results demonstrate the superiority of MH-DQN over traditional DRL algorithms on a single server, as well as the advantages of the personal federated training architecture compared to other frameworks.

**Link**: [arxiv](http://arxiv.org/abs/2412.12543v1),  [pdf](http://arxiv.org/pdf/2412.12543v1)

**Tags**: cs.NI eess.SP 



### A System for Microserving of LLMs
**Authors**: Hongyi Jin, Ruihang Lai, Charlie F. Ruan, Yingcheng Wang, Todd C. Mowry, Xupeng Miao, Zhihao Jia, Tianqi Chen

**Updated**: 2024-12-17T02:44:43Z

**Summary**: The recent advances in LLMs bring a strong demand for efficient system support to improve overall serving efficiency. As LLM inference scales towards multiple GPUs and even multiple compute nodes, various coordination patterns, such as prefill-decode disaggregation and context migration, arise in serving systems. Most inference services today expose a coarse-grained request-level API with a pre-configured coordination strategy, limiting the ability to customize and dynamically reconfigure the coordination. In this paper, we propose LLM microserving, a multi-level architecture for structuring and programming LLM inference services. We introduces simple yet effective microserving APIs to support fine-grained sub-request level actions. A programmable router transforms user requests into sub-request calls, enabling the dynamic reconfiguration of serving patterns. To support diverse execution patterns, we develop a unified KV cache interface that handles various KV compute, transfer, and reuse scenarios. Our evaluation shows that LLM microserving can be reconfigured to support multiple disaggregation orchestration strategies in a few lines of Python code while maintaining state-of-the-art performance for LLM inference tasks. Additionally, it allows us to explore new strategy variants that reduce up to 47% of job completion time compared to the existing strategies.

**Link**: [arxiv](http://arxiv.org/abs/2412.12488v1),  [pdf](http://arxiv.org/pdf/2412.12488v1)

**Tags**: cs.DC 



### LazyDiT: Lazy Learning for the Acceleration of Diffusion Transformers
**Authors**: Xuan Shen, Zhao Song, Yufa Zhou, Bo Chen, Yanyu Li, Yifan Gong, Kai Zhang, Hao Tan, Jason Kuen, Henghui Ding, Zhihao Shu, Wei Niu, Pu Zhao, Yanzhi Wang, Jiuxiang Gu

**Updated**: 2024-12-17T01:12:35Z

**Summary**: Diffusion Transformers have emerged as the preeminent models for a wide array of generative tasks, demonstrating superior performance and efficacy across various applications. The promising results come at the cost of slow inference, as each denoising step requires running the whole transformer model with a large amount of parameters. In this paper, we show that performing the full computation of the model at each diffusion step is unnecessary, as some computations can be skipped by lazily reusing the results of previous steps. Furthermore, we show that the lower bound of similarity between outputs at consecutive steps is notably high, and this similarity can be linearly approximated using the inputs. To verify our demonstrations, we propose the \textbf{LazyDiT}, a lazy learning framework that efficiently leverages cached results from earlier steps to skip redundant computations. Specifically, we incorporate lazy learning layers into the model, effectively trained to maximize laziness, enabling dynamic skipping of redundant computations. Experimental results show that LazyDiT outperforms the DDIM sampler across multiple diffusion transformer models at various resolutions. Furthermore, we implement our method on mobile devices, achieving better performance than DDIM with similar latency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12444v1),  [pdf](http://arxiv.org/pdf/2412.12444v1)

**Tags**: cs.LG cs.AI 



### The Selection Problem in Multi-Query Optimization: a Comprehensive   Survey
**Authors**: Sergey Zinchenko, Denis Ponomaryov

**Updated**: 2024-12-16T14:49:32Z

**Summary**: View materialization, index selection, and plan caching are well-known techniques for optimization of query processing in database systems. The essence of these tasks is to select and save a subset of the most useful candidates (views/indexes/plans) for reuse within given space/time budget constraints. In this paper, based on the View Selection Problem, we propose a unified view on these problems. We identify the root causes of the complexity of these selection problems and provide a detailed analysis of techniques to cope with them. Our survey provides a modern classification of selection algorithms known in the literature, including the latest ones based on Machine Learning. We provide a ground for the reuse of the selection techniques between different optimization scenarios and highlight challenges and promising directions in the field.

**Link**: [arxiv](http://arxiv.org/abs/2412.11828v1),  [pdf](http://arxiv.org/pdf/2412.11828v1)

**Tags**: cs.DB cs.DM 



### CSR:Achieving 1 Bit Key-Value Cache via Sparse Representation
**Authors**: Hongxuan Zhang, Yao Zhao, Jiaqi Zheng, Chenyi Zhuang, Jinjie Gu, Guihai Chen

**Updated**: 2024-12-16T13:01:53Z

**Summary**: The emergence of long-context text applications utilizing large language models (LLMs) has presented significant scalability challenges, particularly in memory footprint. The linear growth of the Key-Value (KV) cache responsible for storing attention keys and values to minimize redundant computations can lead to substantial increases in memory consumption, potentially causing models to fail to serve with limited memory resources. To address this issue, we propose a novel approach called Cache Sparse Representation (CSR), which converts the KV cache by transforming the dense Key-Value cache tensor into sparse indexes and weights, offering a more memory-efficient representation during LLM inference. Furthermore, we introduce NeuralDict, a novel neural network-based method for automatically generating the dictionary used in our sparse representation. Our extensive experiments demonstrate that CSR achieves performance comparable to state-of-the-art KV cache quantization algorithms while maintaining robust functionality in memory-constrained environments.

**Link**: [arxiv](http://arxiv.org/abs/2412.11741v1),  [pdf](http://arxiv.org/pdf/2412.11741v1)

**Tags**: cs.CL 



### AsymRnR: Video Diffusion Transformers Acceleration with Asymmetric   Reduction and Restoration
**Authors**: Wenhao Sun, Rong-Cheng Tu, Jingyi Liao, Zhao Jin, Dacheng Tao

**Updated**: 2024-12-16T12:28:22Z

**Summary**: Video Diffusion Transformers (DiTs) have demonstrated significant potential for generating high-fidelity videos but are computationally intensive. Existing acceleration methods include distillation, which requires costly retraining, and feature caching, which is highly sensitive to network architecture. Recent token reduction methods are training-free and architecture-agnostic, offering greater flexibility and wider applicability. However, they enforce the same sequence length across different components, constraining their acceleration potential. We observe that intra-sequence redundancy in video DiTs varies across features, blocks, and denoising timesteps. Building on this observation, we propose Asymmetric Reduction and Restoration (AsymRnR), a training-free approach to accelerate video DiTs. It offers a flexible and adaptive strategy that reduces the number of tokens based on their redundancy to enhance both acceleration and generation quality. We further propose matching cache to facilitate faster processing. Integrated into state-of-the-art video DiTs, AsymRnR achieves a superior speedup without compromising the quality.

**Link**: [arxiv](http://arxiv.org/abs/2412.11706v1),  [pdf](http://arxiv.org/pdf/2412.11706v1)

**Tags**: cs.CV 



### Ultra-High-Definition Dynamic Multi-Exposure Image Fusion via Infinite   Pixel Learning
**Authors**: Xingchi Chen, Zhuoran Zheng, Xuerui Li, Yuying Chen, Shu Wang, Wenqi Ren

**Updated**: 2024-12-16T11:55:26Z

**Summary**: With the continuous improvement of device imaging resolution, the popularity of Ultra-High-Definition (UHD) images is increasing. Unfortunately, existing methods for fusing multi-exposure images in dynamic scenes are designed for low-resolution images, which makes them inefficient for generating high-quality UHD images on a resource-constrained device. To alleviate the limitations of extremely long-sequence inputs, inspired by the Large Language Model (LLM) for processing infinitely long texts, we propose a novel learning paradigm to achieve UHD multi-exposure dynamic scene image fusion on a single consumer-grade GPU, named Infinite Pixel Learning (IPL). The design of our approach comes from three key components: The first step is to slice the input sequences to relieve the pressure generated by the model processing the data stream; Second, we develop an attention cache technique, which is similar to KV cache for infinite data stream processing; Finally, we design a method for attention cache compression to alleviate the storage burden of the cache on the device. In addition, we provide a new UHD benchmark to evaluate the effectiveness of our method. Extensive experimental results show that our method maintains high-quality visual performance while fusing UHD dynamic multi-exposure images in real-time (>40fps) on a single consumer-grade GPU.

**Link**: [arxiv](http://arxiv.org/abs/2412.11685v1),  [pdf](http://arxiv.org/pdf/2412.11685v1)

**Tags**: cs.CV 



### The "Huh?" Button: Improving Understanding in Educational Videos with   Large Language Models
**Authors**: Boris Ruf, Marcin Detyniecki

**Updated**: 2024-12-15T21:02:16Z

**Summary**: We propose a simple way to use large language models (LLMs) in education. Specifically, our method aims to improve individual comprehension by adding a novel feature to online videos. We combine the low threshold for interactivity in digital experiences with the benefits of rephrased and elaborated explanations typical of face-to-face interactions, thereby supporting to close knowledge gaps at scale. To demonstrate the technical feasibility of our approach, we conducted a proof-of-concept experiment and implemented a prototype which is available for testing online. Through the use case, we also show how caching can be applied in LLM-powered applications to reduce their carbon footprint.

**Link**: [arxiv](http://arxiv.org/abs/2412.14201v1),  [pdf](http://arxiv.org/pdf/2412.14201v1)

**Tags**: cs.HC cs.CY 



### PULSE: Accelerating Distributed Pointer-Traversals on Disaggregated   Memory (Extended Version)
**Authors**: Yupeng Tang, Seung-seob Lee, Abhishek Bhattacharjee, Anurag Khandelwal

**Updated**: 2024-12-15T03:29:54Z

**Summary**: Caches at CPU nodes in disaggregated memory architectures amortize the high data access latency over the network. However, such caches are fundamentally unable to improve performance for workloads requiring pointer traversals across linked data structures. We argue for accelerating these pointer traversals closer to disaggregated memory in a manner that preserves expressiveness for supporting various linked structures, ensures energy efficiency and performance, and supports distributed execution. We design PULSE, a distributed pointer-traversal framework for rack-scale disaggregated memory to meet all the above requirements. Our evaluation of PULSE shows that it enables low-latency, high-throughput, and energy-efficient execution for a wide range of pointer traversal workloads on disaggregated memory that fare poorly with caching alone.

**Link**: [arxiv](http://arxiv.org/abs/2305.02388v3),  [pdf](http://arxiv.org/pdf/2305.02388v3)

**Tags**: cs.DC 



### SparseMap: Loop Mapping for Sparse CNNs on Streaming Coarse-grained   Reconfigurable Array
**Authors**: Xiaobing Ni, Mengke Ge, Jiaheng Ruan, Song Chen, Yi Kang

**Updated**: 2024-12-15T02:30:09Z

**Summary**: Streaming coarse-grained reconfgurable array (CGRA) is a promising architecture for data/computing-intensive applications because of its fexibility, high throughput and efcient memory system. However,when accelerating sparse CNNs, the irregular input data demands inside sparse CNNs would cause excessive caching operations (COPs) and multi-cycle internal dependencies (MCIDs) between operations, declining the throughput of the streaming CGRA. We propose a mapping method for sparse CNNs onto streaming CGRA, SparseMap, which incorporates an efcient I/O data management along with operation scheduling and binding, to reduce the COPs and MCIDs, thereby ensuring the optimal throughput of streaming CGRA.The experimental results show SparseMap reduces 92.5% COPs and 46.0 % MCIDs while achieves the same or even smaller initiation interval (II) compared to previous works.

**Link**: [arxiv](http://arxiv.org/abs/2412.11021v1),  [pdf](http://arxiv.org/pdf/2412.11021v1)

**Tags**: cs.DC 



### Accelerating Retrieval-Augmented Generation
**Authors**: Derrick Quinn, Mohammad Nouri, Neel Patel, John Salihu, Alireza Salemi, Sukhan Lee, Hamed Zamani, Mohammad Alian

**Updated**: 2024-12-14T06:47:56Z

**Summary**: An evolving solution to address hallucination and enhance accuracy in large language models (LLMs) is Retrieval-Augmented Generation (RAG), which involves augmenting LLMs with information retrieved from an external knowledge source, such as the web. This paper profiles several RAG execution pipelines and demystifies the complex interplay between their retrieval and generation phases. We demonstrate that while exact retrieval schemes are expensive, they can reduce inference time compared to approximate retrieval variants because an exact retrieval model can send a smaller but more accurate list of documents to the generative model while maintaining the same end-to-end accuracy. This observation motivates the acceleration of the exact nearest neighbor search for RAG.   In this work, we design Intelligent Knowledge Store (IKS), a type-2 CXL device that implements a scale-out near-memory acceleration architecture with a novel cache-coherent interface between the host CPU and near-memory accelerators. IKS offers 13.4-27.9x faster exact nearest neighbor search over a 512GB vector database compared with executing the search on Intel Sapphire Rapids CPUs. This higher search performance translates to 1.7-26.3x lower end-to-end inference time for representative RAG applications. IKS is inherently a memory expander; its internal DRAM can be disaggregated and used for other applications running on the server to prevent DRAM, which is the most expensive component in today's servers, from being stranded.

**Link**: [arxiv](http://arxiv.org/abs/2412.15246v1),  [pdf](http://arxiv.org/pdf/2412.15246v1)

**Tags**: cs.CL cs.AI cs.AR cs.DC cs.IR 



### RMCSA Algorithm for Congestion-Aware and Service Latency Aware Dynamic   Service Provisioning in Software-Defined SDM-EONs
**Authors**: Baljinder Singh Heera, Shrinivas Petale, Yatindra Nath Singh, Suresh Subramaniam

**Updated**: 2024-12-14T05:20:50Z

**Summary**: The implementation of 5G and the future deployment of 6G necessitate the utilization of optical networks that possess substantial capacity and exhibit minimal latency. The dynamic arrival and departure of connection requests in optical networks result in particular central links experiencing more traffic and congestion than non-central links. The occurrence of congested links leads to service blocking despite the availability of resources within the network, restricting the efficient utilization of network resources. The available algorithms in the literature that aim to balance load among network links offer a trade-off between blocking performance and algorithmic complexity, thus increasing service provisioning time. This work proposes a dynamic routing-based congestion-aware routing, modulation, core, and spectrum assignment (RMCSA) algorithm for space division multiplexing elastic optical networks (SDM-EONs). The algorithm finds alternative candidate paths based on real-time link occupancy metrics to minimize blocking due to link congestion under dynamic traffic scenarios. As a result, the algorithm reduces the formation of congestion hotspots in the network owing to link-betweenness centrality. We have performed extensive simulations using two realistic network topologies to compare the performance of the proposed algorithm with relevant RMCSA algorithms available in the literature. The simulation results verify the superior performance of our proposed algorithm compared to the benchmark Yen's K-shortest paths and K-Disjoint shortest paths RMCSA algorithms in connection blocking ratio and spectrum utilization efficiency. To expedite the route-finding process, we present a novel caching strategy that allows the proposed algorithm to demonstrate a much-reduced service delay time compared to the recently developed adaptive link weight-based load-balancing RMCSA algorithm.

**Link**: [arxiv](http://arxiv.org/abs/2412.10685v1),  [pdf](http://arxiv.org/pdf/2412.10685v1)

**Tags**: cs.NI 



### SCBench: A KV Cache-Centric Analysis of Long-Context Methods
**Authors**: Yucheng Li, Huiqiang Jiang, Qianhui Wu, Xufang Luo, Surin Ahn, Chengruidong Zhang, Amir H. Abdi, Dongsheng Li, Jianfeng Gao, Yuqing Yang, Lili Qiu

**Updated**: 2024-12-13T17:59:52Z

**Summary**: Long-context LLMs have enabled numerous downstream applications but also introduced significant challenges related to computational and memory efficiency. To address these challenges, optimizations for long-context inference have been developed, centered around the KV cache. However, existing benchmarks often evaluate in single-request, neglecting the full lifecycle of the KV cache in real-world use. This oversight is particularly critical, as KV cache reuse has become widely adopted in LLMs inference frameworks, such as vLLM and SGLang, as well as by LLM providers, including OpenAI, Microsoft, Google, and Anthropic. To address this gap, we introduce SCBench(SharedContextBench), a comprehensive benchmark for evaluating long-context methods from a KV cachecentric perspective: 1) KV cache generation, 2) KV cache compression, 3) KV cache retrieval, 4) KV cache loading. Specifically, SCBench uses test examples with shared context, ranging 12 tasks with two shared context modes, covering four categories of long-context capabilities: string retrieval, semantic retrieval, global information, and multi-task. With it, we provide an extensive KV cache-centric analysis of eight categories long-context solutions, including Gated Linear RNNs, Mamba-Attention hybrids, and efficient methods such as sparse attention, KV cache dropping, quantization, retrieval, loading, and prompt compression. The evaluation is conducted on 8 long-context LLMs. Our findings show that sub-O(n) memory methods suffer in multi-turn scenarios, while sparse encoding with O(n) memory and sub-O(n^2) pre-filling computation perform robustly. Dynamic sparsity yields more expressive KV caches than static patterns, and layer-level sparsity in hybrid architectures reduces memory usage with strong performance. Additionally, we identify attention distribution shift issues in long-generation scenarios. https://aka.ms/SCBench.

**Link**: [arxiv](http://arxiv.org/abs/2412.10319v1),  [pdf](http://arxiv.org/pdf/2412.10319v1)

**Tags**: cs.CL cs.LG 



### DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced   Multimodal Understanding
**Authors**: Zhiyu Wu, Xiaokang Chen, Zizheng Pan, Xingchao Liu, Wen Liu, Damai Dai, Huazuo Gao, Yiyang Ma, Chengyue Wu, Bingxuan Wang, Zhenda Xie, Yu Wu, Kai Hu, Jiawei Wang, Yaofeng Sun, Yukun Li, Yishi Piao, Kang Guan, Aixin Liu, Xin Xie, Yuxiang You, Kai Dong, Xingkai Yu, Haowei Zhang, Liang Zhao, Yisong Wang, Chong Ruan

**Updated**: 2024-12-13T17:37:48Z

**Summary**: We present DeepSeek-VL2, an advanced series of large Mixture-of-Experts (MoE) Vision-Language Models that significantly improves upon its predecessor, DeepSeek-VL, through two key major upgrades. For the vision component, we incorporate a dynamic tiling vision encoding strategy designed for processing high-resolution images with different aspect ratios. For the language component, we leverage DeepSeekMoE models with the Multi-head Latent Attention mechanism, which compresses Key-Value cache into latent vectors, to enable efficient inference and high throughput. Trained on an improved vision-language dataset, DeepSeek-VL2 demonstrates superior capabilities across various tasks, including but not limited to visual question answering, optical character recognition, document/table/chart understanding, and visual grounding. Our model series is composed of three variants: DeepSeek-VL2-Tiny, DeepSeek-VL2-Small and DeepSeek-VL2, with 1.0B, 2.8B and 4.5B activated parameters respectively. DeepSeek-VL2 achieves competitive or state-of-the-art performance with similar or fewer activated parameters compared to existing open-source dense and MoE-based models. Codes and pre-trained models are publicly accessible at https://github.com/deepseek-ai/DeepSeek-VL2.

**Link**: [arxiv](http://arxiv.org/abs/2412.10302v1),  [pdf](http://arxiv.org/pdf/2412.10302v1)

**Tags**: cs.CV cs.AI cs.CL 



### OASIS-UROS: Open Acquisition System for IEPE Sensors -- Upgraded,   Refined, and Overhauled Software
**Authors**: Oliver Maximilian Zobel, Johannes Maierhofer, Andreas Köstler, Daniel J. Rixen

**Updated**: 2024-12-13T16:13:39Z

**Summary**: OASIS-UROS continues the previously published Open Acquisition System for IEPE Sensors (OASIS). While still building on the ESP32 microcontroller, this version improves the overall performance by switching to an SD card caching system and upgrading the analog-digital converter to an AD7606C-18, which has a higher resolution, provides eight channels, oversampling, and software-adjustable voltage ranges. Also improved is the IEPE front-end and power supply, as well as the firmware of the acquisition system, which can now achieve a sample rate of up to 36 kHz while sampling all eight channels. This paper documents the hardware and software of OASIS-UROS and provides all materials required to reproduce the open acquisition system. Lastly, the system was validated against commercial hardware and software in an experimental modal analysis context. This showed that the system performs close to the commercial one in some aspects with respect to the utilized test case. While OASIS-UROS cannot match the full performance of the commercial system, the developed system can be a viable alternative for students, people in academia, or smaller companies that have a constrained budget or require complete insight as well as adaptability of the hardware and software.

**Link**: [arxiv](http://arxiv.org/abs/2411.18566v2),  [pdf](http://arxiv.org/pdf/2411.18566v2)

**Tags**: physics.ins-det 



### EVOS: Efficient Implicit Neural Training via EVOlutionary Selector
**Authors**: Weixiang Zhang, Shuzhao Xie, Chengwei Ren, Siyi Xie, Chen Tang, Shijia Ge, Mingzi Wang, Zhi Wang

**Updated**: 2024-12-13T14:11:42Z

**Summary**: We propose EVOlutionary Selector (EVOS), an efficient training paradigm for accelerating Implicit Neural Representation (INR). Unlike conventional INR training that feeds all samples through the neural network in each iteration, our approach restricts training to strategically selected points, reducing computational overhead by eliminating redundant forward passes. Specifically, we treat each sample as an individual in an evolutionary process, where only those fittest ones survive and merit inclusion in training, adaptively evolving with the neural network dynamics. While this is conceptually similar to Evolutionary Algorithms, their distinct objectives (selection for acceleration vs. iterative solution optimization) require a fundamental redefinition of evolutionary mechanisms for our context. In response, we design sparse fitness evaluation, frequency-guided crossover, and augmented unbiased mutation to comprise EVOS. These components respectively guide sample selection with reduced computational cost, enhance performance through frequency-domain balance, and mitigate selection bias from cached evaluation. Extensive experiments demonstrate that our method achieves approximately 48%-66% reduction in training time while ensuring superior convergence without additional cost, establishing state-of-the-art acceleration among recent sampling-based strategies.

**Link**: [arxiv](http://arxiv.org/abs/2412.10153v1),  [pdf](http://arxiv.org/pdf/2412.10153v1)

**Tags**: cs.CV cs.MM cs.NE 



### Optimal Offline ORAM with Perfect Security via Simple Oblivious Priority   Queues
**Authors**: Thore Thießen, Jan Vahrenhold

**Updated**: 2024-12-13T14:08:55Z

**Summary**: Oblivious RAM (ORAM) is a well-researched primitive to hide the memory access pattern of a RAM computation; it has a variety of applications in trusted computing, outsourced storage, and multiparty computation. In this paper, we study the so-called offline ORAM in which the sequence of memory access locations to be hidden is known in advance. Apart from their theoretical significance, offline ORAMs can be used to construct efficient oblivious algorithms.   We obtain the first optimal offline ORAM with perfect security from oblivious priority queues via time-forward processing. For this, we present a simple construction of an oblivious priority queue with perfect security. Our construction achieves an asymptotically optimal (amortized) runtime of $\Theta(\log N)$ per operation for a capacity of $N$ elements and is of independent interest.   Building on our construction, we additionally present efficient external-memory instantiations of our oblivious, perfectly-secure construction: For the cache-aware setting, we match the optimal I/O complexity of $\Theta(\frac{1}{B} \log \frac{N}{M})$ per operation (amortized), and for the cache-oblivious setting we achieve a near-optimal I/O complexity of $O(\frac{1}{B} \log \frac{N}{M} \log\log_M N)$ per operation (amortized).

**Link**: [arxiv](http://arxiv.org/abs/2409.12021v2),  [pdf](http://arxiv.org/pdf/2409.12021v2)

**Tags**: cs.DS cs.CR 



### Activation Sparsity Opportunities for Compressing General Large Language   Models
**Authors**: Nobel Dhar, Bobin Deng, Md Romyull Islam, Kazi Fahim Ahmad Nasif, Liang Zhao, Kun Suo

**Updated**: 2024-12-13T02:26:54Z

**Summary**: Deploying local AI models, such as Large Language Models (LLMs), to edge devices can substantially enhance devices' independent capabilities, alleviate the server's burden, and lower the response time. Owing to these tremendous potentials, many big tech companies have released several lightweight Small Language Models (SLMs) to bridge this gap. However, we still have huge motivations to deploy more powerful (LLMs) AI models on edge devices and enhance their smartness level. Unlike the conventional approaches for AI model compression, we investigate activation sparsity. The activation sparsity method is orthogonal and combinable with existing techniques to maximize compression rate while maintaining great accuracy. LLMs' Feed-Forward Network (FFN) components, which typically comprise a large proportion of parameters (around 3/2), ensure that our FFN optimizations would have a better chance of achieving effective compression. Moreover, our findings are beneficial to general LLMs and are not restricted to ReLU-based models. This work systematically investigates the tradeoff between enforcing activation sparsity and perplexity (accuracy) on state-of-the-art LLMs. Our empirical analysis demonstrates that we can obtain around 50% of main memory and computing reductions for critical FFN components with negligible accuracy degradation. This extra 50% sparsity does not naturally exist in the current LLMs, which require tuning LLMs' activation outputs by injecting zero-enforcing thresholds. To obtain the benefits of activation sparsity, we provide a guideline for the system architect for LLM prediction and prefetching. The success prediction allows the system to prefetch the necessary weights while omitting the inactive ones and their successors, therefore lowering cache and memory pollution and reducing LLM execution time on resource-constrained edge devices.

**Link**: [arxiv](http://arxiv.org/abs/2412.12178v1),  [pdf](http://arxiv.org/pdf/2412.12178v1)

**Tags**: cs.LG cs.AI 



### Optimizing CDN Architectures: Multi-Metric Algorithmic Breakthroughs for   Edge and Distributed Performance
**Authors**: Md Nurul Absur, Sourya Saha, Sifat Nawrin Nova, Kazi Fahim Ahmad Nasif, Md Rahat Ul Nasib

**Updated**: 2024-12-12T17:20:26Z

**Summary**: A Content Delivery Network (CDN) is a powerful system of distributed caching servers that aims to accelerate content delivery, like high-definition video, IoT applications, and ultra-low-latency services, efficiently and with fast velocity. This has become of paramount importance in the post-pandemic era. Challenges arise when exponential content volume growth and scalability across different geographic locations are required. This paper investigates data-driven evaluations of CDN algorithms in dynamic server selection for latency reduction, bandwidth throttling for efficient resource management, real-time Round Trip Time analysis for adaptive routing, and programmatic network delay simulation to emulate various conditions. Key performance metrics, such as round-trip time (RTT) and CPU usage, are carefully analyzed to evaluate scalability and algorithmic efficiency through two experimental setups: a constrained edge-like local system and a scalable FABRIC testbed. The statistical validation of RTT trends, alongside CPU utilization, is presented in the results. The optimization process reveals significant trade-offs between scalability and resource consumption, providing actionable insights for effectively deploying and enhancing CDN algorithms in edge and distributed computing environments.

**Link**: [arxiv](http://arxiv.org/abs/2412.09474v1),  [pdf](http://arxiv.org/pdf/2412.09474v1)

**Tags**: cs.DC 



### Unifying AI Tutor Evaluation: An Evaluation Taxonomy for Pedagogical   Ability Assessment of LLM-Powered AI Tutors
**Authors**: Kaushal Kumar Maurya, KV Aditya Srivatsa, Kseniia Petukhova, Ekaterina Kochmar

**Updated**: 2024-12-12T16:24:35Z

**Summary**: In this paper, we investigate whether current state-of-the-art large language models (LLMs) are effective as AI tutors and whether they demonstrate pedagogical abilities necessary for good AI tutoring in educational dialogues. Previous efforts towards evaluation have been limited to subjective protocols and benchmarks. To bridge this gap, we propose a unified evaluation taxonomy with eight pedagogical dimensions based on key learning sciences principles, which is designed to assess the pedagogical value of LLM-powered AI tutor responses grounded in student mistakes or confusion in the mathematical domain. We release MRBench -- a new evaluation benchmark containing 192 conversations and 1,596 responses from seven state-of-the-art LLM-based and human tutors, providing gold annotations for eight pedagogical dimensions. We assess reliability of the popular Prometheus2 LLM as an evaluator and analyze each tutor's pedagogical abilities, highlighting which LLMs are good tutors and which ones are more suitable as question-answering systems. We believe that the presented taxonomy, benchmark, and human-annotated labels will streamline the evaluation process and help track the progress in AI tutors' development.

**Link**: [arxiv](http://arxiv.org/abs/2412.09416v1),  [pdf](http://arxiv.org/pdf/2412.09416v1)

**Tags**: cs.CL 



### ZipCache: A DRAM/SSD Cache with Built-in Transparent Compression
**Authors**: Rui Xie, Linsen Ma, Alex Zhong, Feng Chen, Tong Zhang

**Updated**: 2024-12-12T15:39:48Z

**Summary**: As a core component in modern data centers, key-value cache provides high-throughput and low-latency services for high-speed data processing. The effectiveness of a key-value cache relies on its ability of accommodating the needed data. However, expanding the cache capacity is often more difficult than commonly expected because of many practical constraints, such as server costs, cooling issues, rack space, and even human resource expenses. A potential solution is compression, which virtually extends the cache capacity by condensing data in cache. In practice, this seemingly simple idea has not gained much traction in key-value cache system design, due to several critical issues: the compression-unfriendly index structure, severe read/write amplification, wasteful decompression operations, and heavy computing cost. This paper presents a hybrid DRAM-SSD cache design to realize a systematic integration of data compression in key-value cache. By treating compression as an essential component, we have redesigned the indexing structure, data management, and leveraged the emerging computational SSD hardware for collaborative optimizations. We have developed a prototype, called ZipCache. Our experimental results show that ZipCache can achieve up to 72.4% higher throughput and 42.4% lower latency, while reducing the write amplification by up to 26.2 times.

**Link**: [arxiv](http://arxiv.org/abs/2411.03174v3),  [pdf](http://arxiv.org/pdf/2411.03174v3)

**Tags**: cs.DB 



### Unlocking FedNL: Self-Contained Compute-Optimized Implementation
**Authors**: Konstantin Burlachenko, Peter Richtárik

**Updated**: 2024-12-12T14:43:48Z

**Summary**: Federated Learning (FL) is an emerging paradigm that enables intelligent agents to collaboratively train Machine Learning (ML) models in a distributed manner, eliminating the need for sharing their local data. The recent work (arXiv:2106.02969) introduces a family of Federated Newton Learn (FedNL) algorithms, marking a significant step towards applying second-order methods to FL and large-scale optimization. However, the reference FedNL prototype exhibits three serious practical drawbacks: (i) It requires 4.8 hours to launch a single experiment in a sever-grade workstation; (ii) The prototype only simulates multi-node setting; (iii) Prototype integration into resource-constrained applications is challenging. To bridge the gap between theory and practice, we present a self-contained implementation of FedNL, FedNL-LS, FedNL-PP for single-node and multi-node settings. Our work resolves the aforementioned issues and reduces the wall clock time by x1000. With this FedNL outperforms alternatives for training logistic regression in a single-node -- CVXPY (arXiv:1603.00943), and in a multi-node -- Apache Spark (arXiv:1505.06807), Ray/Scikit-Learn (arXiv:1712.05889). Finally, we propose two practical-orientated compressors for FedNL - adaptive TopLEK and cache-aware RandSeqK, which fulfill the theory of FedNL.

**Link**: [arxiv](http://arxiv.org/abs/2410.08760v2),  [pdf](http://arxiv.org/pdf/2410.08760v2)

**Tags**: cs.LG cs.AI cs.MS cs.PF math.OC G.4; C.3; I.2.11 



### PowerInfer-2: Fast Large Language Model Inference on a Smartphone
**Authors**: Zhenliang Xue, Yixin Song, Zeyu Mi, Xinrui Zheng, Yubin Xia, Haibo Chen

**Updated**: 2024-12-12T12:24:18Z

**Summary**: Large language models (LLMs) on smartphones enable real-time AI assistance and privacy-preserving, offline operation. However, resource constraints of smartphones limit current deployments to small language models (SLMs), significantly compromising their capabilities. This paper introduces PowerInfer-2, a smartphone-based framework that enables fast inference for LLMs exceeding the memory capacity. The key insight is decomposing matrix operations into neuron clusters as the basic processing unit, which enables flexible scheduling and efficient I/O-computation pipelining. PowerInfer-2 leverages this neuron-cluster-based design in both computation and storage. For computation, neuron clusters with dense activations are processed on NPU, while sparse clusters use CPU. The storage engine provides a fine-grained pipeline mechanism that coordinates cluster-level computation and I/O operations, enhanced by a segmented neuron cache to reduce I/O activities. PowerInfer-2 achieves up to a 27.8x speed increase compared to state-of-the-art frameworks. PowerInfer-2 is the first system to serve a 47B LLM on a smartphone, achieving 11.68 tokens/s. Notably, these performance improvements preserve model quality with negligible accuracy degradation.

**Link**: [arxiv](http://arxiv.org/abs/2406.06282v3),  [pdf](http://arxiv.org/pdf/2406.06282v3)

**Tags**: cs.LG 



### HEXA-MoE: Efficient and Heterogeneous-aware MoE Acceleration with ZERO   Computation Redundancy
**Authors**: Shuqing Luo, Jie Peng, Pingzhi Li, Tianlong Chen

**Updated**: 2024-12-12T12:03:19Z

**Summary**: Mixture-of-Experts (MoE) has emerged as a practical approach to scale up parameters for the Transformer model to achieve better generalization while maintaining a sub-linear increase in computation overhead. Current MoE models are mainly built with expert parallelism on distributed devices. However, it usually depends on homogeneous devices to deploy and suffers from heavy communication overhead and computation redundancy. In this paper, we explore developing a \texttt{H}eterogeneous-aware \texttt{EX}pert \texttt{A}llocation framework, \textbf{\texttt{HEXA-MoE}}, with significantly enhanced computing efficiency. It contains two components: ($1$) \textit{Expert-Specific Operators}. We replace the typical general matrix multiplication or grouped matrix multiplication interfaces with our operators, which allows the computing to be performed in an in-place manner with \textbf{ZERO} redundancy. ($2$) \textit{Adaptive Data- and Model-Centric Configurations} for different workload scales. Specifically, we introduce a pipeline-shared cache on each device to tackle the heavy memory consumption in the existing data-centric MoE library. Comprehensive experiments on the Swin-MoE benchmark consistently reveal the effectiveness of our \texttt{HEXA-MoE} framework, i.e., reducing $10\%\sim48\%$ memory consumption and achieving $0.5\sim4.3\times$ speed up compared to current state-of-the-art MoE libraries. Furthermore, we examine our \texttt{HEXA-MoE} with heterogeneous devices for both data- and model-centric settings. Promising results show that employing optimal parallel configuration with \texttt{HEXA-MoE} on heterogeneous devices can substantially minimize overall latency. Codes are available at https://github.com/UNITES-Lab/HEXA-MoE.

**Link**: [arxiv](http://arxiv.org/abs/2411.01288v3),  [pdf](http://arxiv.org/pdf/2411.01288v3)

**Tags**: cs.DC 



### Excitation of quasi-monochromotic waves by a high-voltage pulse in a   ferrite coaxial line with the periodic structure
**Authors**: A. B. Batrakov, S. Yu. Karelin, O. M. Lebedenko, V. S. Mukhin, I. N. Onishchenko, O. L. Rak, V. G. Sinitsin, M. V. Volovenko

**Updated**: 2024-12-12T10:07:17Z

**Summary**: Experimental data and results of numerical simulations are presented, concerning excitation of narrowband gigahertz-range wave trains in coaxial guiding structures that are partially filled with ferromagnetic material and may involve periodically arranged metal inserts. The experiments performed confirm the possibility of exciting weakly damped electromagnetic waves by feeding high voltage, unilateral electromagnetic pulses of short duration into the line. The coax line was of outer diameter 50.5 mm, filled with an isotropic dielectric (relative dielectric constant {\epsilon} = 2.25) and a set of ferrite rings with {\epsilon}=16 and saturated-state {\mu} about 4 to 5. With a peak voltage of the primary pulse close to 160 kV and a magnetizing field of 17.5 kA/m, the parameters of the waves excited reached magnitudes as: frequency 1.89 GHz to 2.1 GHz; bandwidth 16%; VHF power at the output about 20 MW.

**Link**: [arxiv](http://arxiv.org/abs/2412.01415v2),  [pdf](http://arxiv.org/pdf/2412.01415v2)

**Tags**: physics.acc-ph 



### PhishIntel: Toward Practical Deployment of Reference-based Phishing   Detection
**Authors**: Yuexin Li, Hiok Kuek Tan, Qiaoran Meng, Mei Lin Lock, Tri Cao, Shumin Deng, Nay Oo, Hoon Wei Lim, Bryan Hooi

**Updated**: 2024-12-12T08:33:39Z

**Summary**: Phishing is a critical cyber threat, exploiting deceptive tactics to compromise victims and cause significant financial losses. While reference-based phishing detectors (RBPDs) achieve high precision by analyzing brand-domain consistency, their real-world deployment is hindered by challenges such as high latency and inefficiency in URL analysis. To address these limitations, we present PhishIntel, an end-to-end phishing detection system for real-world deployment. PhishIntel intelligently determines whether a URL can be processed immediately or not, segmenting the detection process into two distinct tasks: a fast task that checks against local blacklists and result cache, and a slow task that conducts online blacklist verification, URL crawling, and webpage analysis using an RBPD. This fast-slow task system architecture ensures low response latency while retaining the robust detection capabilities of RBPDs for zero-day phishing threats. Furthermore, we develop two downstream applications based on PhishIntel: a phishing intelligence platform and a phishing email detection plugin for Microsoft Outlook, demonstrating its practical efficacy and utility.

**Link**: [arxiv](http://arxiv.org/abs/2412.09057v1),  [pdf](http://arxiv.org/pdf/2412.09057v1)

**Tags**: cs.CR 



### ZigZagkv: Dynamic KV Cache Compression for Long-context Modeling based   on Layer Uncertainty
**Authors**: Meizhi Zhong, Xikai Liu, Chen Zhang, Yikun Lei, Yan Gao, Yao Hu, Kehai Chen, Min Zhang

**Updated**: 2024-12-12T07:52:56Z

**Summary**: Large Language models (LLMs) have become a research hotspot. To accelerate the inference of LLMs, storing computed caches in memory has become the standard technique. However, as the inference length increases, growing KV caches might lead to out-of-memory issues. Many existing methods address this issue through KV cache compression, primarily by preserving key tokens throughout all layers to reduce information loss. Most of them allocate a uniform budget size for each layer to retain. However, we observe that the minimum budget sizes needed to retain essential information vary across layers and models based on the perspectives of attention and hidden state output. Building on this observation, this paper proposes a simple yet effective KV cache compression method that leverages layer uncertainty to allocate budget size for each layer. Experimental results show that the proposed method can reduce memory usage of the KV caches to only $\sim$20\% when compared to Full KV inference while achieving nearly lossless performance.

**Link**: [arxiv](http://arxiv.org/abs/2412.09036v1),  [pdf](http://arxiv.org/pdf/2412.09036v1)

**Tags**: cs.CL 



### Forecasting GPU Performance for Deep Learning Training and Inference
**Authors**: Seonho Lee, Amar Phanishayee, Divya Mahajan

**Updated**: 2024-12-12T03:21:13Z

**Summary**: Deep learning kernels exhibit predictable memory accesses and compute patterns, making GPUs' parallel architecture well-suited for their execution. Software and runtime systems for GPUs are optimized to better utilize the stream multiprocessors, on-chip cache, and off-chip high-bandwidth memory. As deep learning models and GPUs evolve, access to newer GPUs is often limited, raising questions about the performance of new model architectures on existing GPUs, existing models on new GPUs, and new model architectures on new GPUs. To address these questions, we introduce NeuSight, a framework to predict the performance of various deep learning models, for both training and inference, on unseen GPUs without requiring actual execution. The framework leverages both GPU hardware behavior and software library optimizations to estimate end-to-end performance. Previous work uses regression models that capture linear trends or multilayer perceptrons to predict the overall latency of deep learning kernels on GPUs. These approaches suffer from higher error percentages when forecasting performance on unseen models and new GPUs. Instead, NeuSight decomposes the prediction problem into smaller problems, bounding the prediction through fundamental performance laws. NeuSight decomposes a single deep learning kernel prediction into smaller working sets called tiles, which are executed independently on the GPU. Tile-granularity predictions are determined using a machine learning approach and aggregated to estimate end-to-end latency. NeuSight outperforms prior work across various deep learning workloads and the latest GPUs. It reduces the percentage error from 121.4% and 30.8% to 2.3% in predicting the latency of GPT3 model for training and inference on H100, compared to state-of-the-art prior work, where both GPT3 and H100 were not used to train the framework.

**Link**: [arxiv](http://arxiv.org/abs/2407.13853v3),  [pdf](http://arxiv.org/pdf/2407.13853v3)

**Tags**: cs.LG cs.PF 



### Lexico: Extreme KV Cache Compression via Sparse Coding over Universal   Dictionaries
**Authors**: Junhyuck Kim, Jongho Park, Jaewoong Cho, Dimitris Papailiopoulos

**Updated**: 2024-12-12T03:00:29Z

**Summary**: We introduce Lexico, a novel KV cache compression method that leverages sparse coding with a universal dictionary. Our key finding is that key-value cache in modern LLMs can be accurately approximated using sparse linear combination from a small, input-agnostic dictionary of ~4k atoms, enabling efficient compression across different input prompts, tasks and models. Using orthogonal matching pursuit for sparse approximation, Lexico achieves flexible compression ratios through direct sparsity control. On GSM8K, across multiple model families (Mistral, Llama 3, Qwen2.5), Lexico maintains 90-95% of the original performance while using only 15-25% of the full KV-cache memory, outperforming both quantization and token eviction methods. Notably, Lexico remains effective in low memory regimes where 2-bit quantization fails, achieving up to 1.7x better compression on LongBench and GSM8K while maintaining high accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2412.08890v1),  [pdf](http://arxiv.org/pdf/2412.08890v1)

**Tags**: cs.LG 



### EMS: Adaptive Evict-then-Merge Strategy for Head-wise KV Cache   Compression Based on Global-Local Importance
**Authors**: Yingxin Li, Ye Li, Yuan Meng, Xinzhu Ma, Zihan Geng, Shutao Xia, Zhi Wang

**Updated**: 2024-12-11T16:35:13Z

**Summary**: As large language models (LLMs) continue to advance, the demand for higher quality and faster processing of long contexts across various applications is growing. KV cache is widely adopted as it stores previously generated key and value tokens, effectively reducing redundant computations during inference. However, as memory overhead becomes a significant concern, efficient compression of KV cache has gained increasing attention. Most existing methods perform compression from two perspectives: identifying important tokens and designing compression strategies. However, these approaches often produce biased distributions of important tokens due to the influence of accumulated attention scores or positional encoding. Furthermore, they overlook the sparsity and redundancy across different heads, which leads to difficulties in preserving the most effective information at the head level. To this end, we propose EMS to overcome these limitations, while achieving better KV cache compression under extreme compression ratios. Specifically, we introduce a Global-Local score that combines accumulated attention scores from both global and local KV tokens to better identify the token importance. For the compression strategy, we design an adaptive and unified Evict-then-Merge framework that accounts for the sparsity and redundancy of KV tokens across different heads. Additionally, we implement the head-wise parallel compression through a zero-class mechanism to enhance efficiency. Extensive experiments demonstrate our SOTA performance even under extreme compression ratios. EMS consistently achieves the lowest perplexity, improves scores by over 1.28 points across four LLMs on LongBench under a 256 cache budget, and preserves 95% retrieval accuracy with a cache budget less than 2% of the context length in the Needle-in-a-Haystack task.

**Link**: [arxiv](http://arxiv.org/abs/2412.08521v1),  [pdf](http://arxiv.org/pdf/2412.08521v1)

**Tags**: cs.CL 



### Pushing the Limits of In-Network Caching for Key-Value Stores
**Authors**: Gyuyeong Kim

**Updated**: 2024-12-11T12:03:40Z

**Summary**: We present OrbitCache, a new in-network caching architecture that can cache variable-length items to balance a wide range of key-value workloads. Unlike existing works, OrbitCache does not cache hot items in the switch memory. Instead, we make hot items revisit the switch data plane continuously by exploiting packet recirculation. Our approach keeps cached key-value pairs in the switch data plane while freeing them from item size limitations caused by hardware constraints. We implement an OrbitCache prototype on an Intel Tofino switch. Our experimental results show that OrbitCache can balance highly skewed workloads and is robust to various system conditions.

**Link**: [arxiv](http://arxiv.org/abs/2407.21324v3),  [pdf](http://arxiv.org/pdf/2407.21324v3)

**Tags**: cs.NI 



### TextRefiner: Internal Visual Feature as Efficient Refiner for   Vision-Language Models Prompt Tuning
**Authors**: Jingjing Xie, Yuxin Zhang, Jun Peng, Zhaohong Huang, Liujuan Cao

**Updated**: 2024-12-11T08:07:12Z

**Summary**: Despite the efficiency of prompt learning in transferring vision-language models (VLMs) to downstream tasks, existing methods mainly learn the prompts in a coarse-grained manner where the learned prompt vectors are shared across all categories. Consequently, the tailored prompts often fail to discern class-specific visual concepts, thereby hindering the transferred performance for classes that share similar or complex visual attributes. Recent advances mitigate this challenge by leveraging external knowledge from Large Language Models (LLMs) to furnish class descriptions, yet incurring notable inference costs. In this paper, we introduce TextRefiner, a plug-and-play method to refine the text prompts of existing methods by leveraging the internal knowledge of VLMs. Particularly, TextRefiner builds a novel local cache module to encapsulate fine-grained visual concepts derivedfrom local tokens within the image branch. By aggregating and aligning the cached visual descriptions with the original output of the text branch, TextRefiner can efficiently refine and enrich the learned prompts from existing methods without relying on any external expertise. For example, it improves the performance of CoOp from 71.66 % to 76.94 % on 11 benchmarks, surpassing CoCoOp which introduces instance-wise features for text prompts. Equipped with TextRefiner, PromptKD achieves state-of-the-art performance and is efficient in inference. Our code is relesed at https://github.com/xjjxmu/TextRefiner

**Link**: [arxiv](http://arxiv.org/abs/2412.08176v1),  [pdf](http://arxiv.org/pdf/2412.08176v1)

**Tags**: cs.CV cs.MM 



### ContextModule: Improving Code Completion via Repository-level Contextual   Information
**Authors**: Zhanming Guan, Junlin Liu, Jierui Liu, Chao Peng, Dexin Liu, Ningyuan Sun, Bo Jiang, Wenchao Li, Jie Liu, Hang Zhu

**Updated**: 2024-12-11T03:15:49Z

**Summary**: Large Language Models (LLMs) have demonstrated impressive capabilities in code completion tasks, where they assist developers by predicting and generating new code in real-time. However, existing LLM-based code completion systems primarily rely on the immediate context of the file being edited, often missing valuable repository-level information, user behaviour and edit history that could improve suggestion accuracy. Additionally, challenges such as efficiently retrieving relevant code snippets from large repositories, incorporating user behavior, and balancing accuracy with low-latency requirements in production environments remain unresolved. In this paper, we propose ContextModule, a framework designed to enhance LLM-based code completion by retrieving and integrating three types of contextual information from the repository: user behavior-based code, similar code snippets, and critical symbol definitions. By capturing user interactions across files and leveraging repository-wide static analysis, ContextModule improves the relevance and precision of generated code. We implement performance optimizations, such as index caching, to ensure the system meets the latency constraints of real-world coding environments. Experimental results and industrial practise demonstrate that ContextModule significantly improves code completion accuracy and user acceptance rates.

**Link**: [arxiv](http://arxiv.org/abs/2412.08063v1),  [pdf](http://arxiv.org/pdf/2412.08063v1)

**Tags**: cs.SE cs.AI 



### Just Shift It: Test-Time Prototype Shifting for Zero-Shot Generalization   with Vision-Language Models
**Authors**: Elaine Sui, Xiaohan Wang, Serena Yeung-Levy

**Updated**: 2024-12-10T22:53:16Z

**Summary**: Advancements in vision-language models (VLMs) have propelled the field of computer vision, particularly in the zero-shot learning setting. Despite their promise, the effectiveness of these models often diminishes due to domain shifts in test environments. To address this, we introduce the Test-Time Prototype Shifting (TPS) framework, a pioneering approach designed to adapt VLMs to test datasets using unlabeled test inputs. Our method is based on the notion of modulating per-class prototypes in the shared embedding space. By pre-computing and caching prototypes generated with the pre-trained text encoder, TPS not only facilitates optimization-free prototype reuse for subsequent predictions but also enables seamless integration with current advancements in prompt engineering. At test-time, TPS dynamically learns shift vectors for each prototype based solely on the given test sample, effectively bridging the domain gap and enhancing classification accuracy. A notable aspect of our framework is its significantly reduced memory and computational demands when compared to conventional text-prompt tuning methods. Extensive evaluations across 15 image classification datasets involving natural distribution shifts and cross-dataset generalization, as well as in context-dependent visual reasoning, demonstrate TPS's superior performance, achieving state-of-the-art results while reducing resource requirements.

**Link**: [arxiv](http://arxiv.org/abs/2403.12952v2),  [pdf](http://arxiv.org/pdf/2403.12952v2)

**Tags**: cs.CV cs.AI cs.LG 



### From Slow Bidirectional to Fast Causal Video Generators
**Authors**: Tianwei Yin, Qiang Zhang, Richard Zhang, William T. Freeman, Fredo Durand, Eli Shechtman, Xun Huang

**Updated**: 2024-12-10T18:59:50Z

**Summary**: Current video diffusion models achieve impressive generation quality but struggle in interactive applications due to bidirectional attention dependencies. The generation of a single frame requires the model to process the entire sequence, including the future. We address this limitation by adapting a pretrained bidirectional diffusion transformer to a causal transformer that generates frames on-the-fly. To further reduce latency, we extend distribution matching distillation (DMD) to videos, distilling 50-step diffusion model into a 4-step generator. To enable stable and high-quality distillation, we introduce a student initialization scheme based on teacher's ODE trajectories, as well as an asymmetric distillation strategy that supervises a causal student model with a bidirectional teacher. This approach effectively mitigates error accumulation in autoregressive generation, allowing long-duration video synthesis despite training on short clips. Our model supports fast streaming generation of high quality videos at 9.4 FPS on a single GPU thanks to KV caching. Our approach also enables streaming video-to-video translation, image-to-video, and dynamic prompting in a zero-shot manner. We will release the code based on an open-source model in the future.

**Link**: [arxiv](http://arxiv.org/abs/2412.07772v1),  [pdf](http://arxiv.org/pdf/2412.07772v1)

**Tags**: cs.CV 



### FlashRNN: Optimizing Traditional RNNs on Modern Hardware
**Authors**: Korbinian Pöppel, Maximilian Beck, Sepp Hochreiter

**Updated**: 2024-12-10T18:50:37Z

**Summary**: While Transformers and other sequence-parallelizable neural network architectures seem like the current state of the art in sequence modeling, they specifically lack state-tracking capabilities. These are important for time-series tasks and logical reasoning. Traditional RNNs like LSTMs and GRUs, as well as modern variants like sLSTM do have these capabilities at the cost of strictly sequential processing. While this is often seen as a strong limitation, we show how fast these networks can get with our hardware-optimization FlashRNN in Triton and CUDA, optimizing kernels to the register level on modern GPUs. We extend traditional RNNs with a parallelization variant that processes multiple RNNs of smaller hidden state in parallel, similar to the head-wise processing in Transformers. To enable flexibility on different GPU variants, we introduce a new optimization framework for hardware-internal cache sizes, memory and compute handling. It models the hardware in a setting using polyhedral-like constraints, including the notion of divisibility. This speeds up the solution process in our ConstrINT library for general integer constraint satisfaction problems (integer CSPs). We show that our kernels can achieve 50x speed-ups over a vanilla PyTorch implementation and allow 40x larger hidden sizes compared to our Triton implementation. Our open-source kernels and the optimization library are released here to boost research in the direction of state-tracking enabled RNNs and sequence modeling: \url{https://github.com/NX-AI/flashrnn}

**Link**: [arxiv](http://arxiv.org/abs/2412.07752v1),  [pdf](http://arxiv.org/pdf/2412.07752v1)

**Tags**: cs.LG cs.AI 



### ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion   Transformer
**Authors**: Jinyi Hu, Shengding Hu, Yuxuan Song, Yufei Huang, Mingxuan Wang, Hao Zhou, Zhiyuan Liu, Wei-Ying Ma, Maosong Sun

**Updated**: 2024-12-10T18:13:20Z

**Summary**: The recent surge of interest in comprehensive multimodal models has necessitated the unification of diverse modalities. However, the unification suffers from disparate methodologies. Continuous visual generation necessitates the full-sequence diffusion-based approach, despite its divergence from the autoregressive modeling in the text domain. We posit that autoregressive modeling, i.e., predicting the future based on past deterministic experience, remains crucial in developing both a visual generation model and a potential unified multimodal model. In this paper, we explore an interpolation between the autoregressive modeling and full-parameters diffusion to model visual information. At its core, we present ACDiT, an Autoregressive blockwise Conditional Diffusion Transformer, where the block size of diffusion, i.e., the size of autoregressive units, can be flexibly adjusted to interpolate between token-wise autoregression and full-sequence diffusion. ACDiT is easy to implement, as simple as creating a Skip-Causal Attention Mask (SCAM) during training. During inference, the process iterates between diffusion denoising and autoregressive decoding that can make full use of KV-Cache. We verify the effectiveness of ACDiT on image and video generation tasks. We also demonstrate that benefitted from autoregressive modeling, ACDiT can be seamlessly used in visual understanding tasks despite being trained on the diffusion objective. The analysis of the trade-off between autoregressive modeling and diffusion demonstrates the potential of ACDiT to be used in long-horizon visual generation tasks. These strengths make it promising as the backbone of future unified models.

**Link**: [arxiv](http://arxiv.org/abs/2412.07720v1),  [pdf](http://arxiv.org/pdf/2412.07720v1)

**Tags**: cs.CV 



### Video-XL: Extra-Long Vision Language Model for Hour-Scale Video   Understanding
**Authors**: Yan Shu, Zheng Liu, Peitian Zhang, Minghao Qin, Junjie Zhou, Zhengyang Liang, Tiejun Huang, Bo Zhao

**Updated**: 2024-12-10T12:45:31Z

**Summary**: Long video understanding poses a significant challenge for current Multi-modal Large Language Models (MLLMs). Notably, the MLLMs are constrained by their limited context lengths and the substantial costs while processing long videos. Although several existing methods attempt to reduce visual tokens, their strategies encounter severe bottleneck, restricting MLLMs' ability to perceive fine-grained visual details. In this work, we propose Video-XL, a novel approach that leverages MLLMs' inherent key-value (KV) sparsification capacity to condense the visual input. Specifically, we introduce a new special token, the Visual Summarization Token (VST), for each interval of the video, which summarizes the visual information within the interval as its associated KV. The VST module is trained by instruction fine-tuning, where two optimizing strategies are offered. 1.Curriculum learning, where VST learns to make small (easy) and large compression (hard) progressively. 2. Composite data curation, which integrates single-image, multi-image, and synthetic data to overcome the scarcity of long-video instruction data. The compression quality is further improved by dynamic compression, which customizes compression granularity based on the information density of different video intervals. Video-XL's effectiveness is verified from three aspects. First, it achieves a superior long-video understanding capability, outperforming state-of-the-art models of comparable sizes across multiple popular benchmarks. Second, it effectively preserves video information, with minimal compression loss even at 16x compression ratio. Third, it realizes outstanding cost-effectiveness, enabling high-quality processing of thousands of frames on a single A100 GPU.

**Link**: [arxiv](http://arxiv.org/abs/2409.14485v4),  [pdf](http://arxiv.org/pdf/2409.14485v4)

**Tags**: cs.CV 



### GPT Semantic Cache: Reducing LLM Costs and Latency via Semantic   Embedding Caching
**Authors**: Sajal Regmi, Chetan Phakami Pun

**Updated**: 2024-12-09T01:44:10Z

**Summary**: Large Language Models (LLMs), such as GPT, have revolutionized artificial intelligence by enabling nuanced understanding and generation of human-like text across a wide range of applications. However, the high computational and financial costs associated with frequent API calls to these models present a substantial bottleneck, especially for applications like customer service chatbots that handle repetitive queries. In this paper, we introduce GPT Semantic Cache, a method that leverages semantic caching of query embeddings in in-memory storage (Redis). By storing embeddings of user queries, our approach efficiently identifies semantically similar questions, allowing for the retrieval of pre-generated responses without redundant API calls to the LLM. This technique achieves a notable reduction in operational costs while significantly enhancing response times, making it a robust solution for optimizing LLM-powered applications. Our experiments demonstrate that GPT Semantic Cache reduces API calls by up to 68.8% across various query categories, with cache hit rates ranging from 61.6% to 68.8%. Additionally, the system achieves high accuracy, with positive hit rates exceeding 97%, confirming the reliability of cached responses. This technique not only reduces operational costs, but also improves response times, enhancing the efficiency of LLM-powered applications.

**Link**: [arxiv](http://arxiv.org/abs/2411.05276v3),  [pdf](http://arxiv.org/pdf/2411.05276v3)

**Tags**: cs.LG 



### A Survey on Privacy-Preserving Caching at Network Edge: Classification,   Solutions, and Challenges
**Authors**: Xianzhi Zhang, Yipeng Zhou, Di Wu, Quan Z. Sheng, Shazia Riaz, Miao Hu, Linchang Xiao

**Updated**: 2024-12-09T01:39:15Z

**Summary**: Caching content at the edge network is a popular and effective technique widely deployed to alleviate the burden of network backhaul, shorten service delay and improve service quality. However, there has been some controversy over privacy violations in caching content at the edge network. On the one hand, the multi-access open edge network provides an ideal entrance or interface for external attackers to obtain private data from edge caches by extracting sensitive information. On the other hand, privacy can be infringed on by curious edge caching providers through caching trace analysis targeting the achievement of better caching performance or higher profits. Therefore, an in-depth understanding of privacy issues in edge caching networks is vital and indispensable for creating a privacy-preserving caching service at the edge network. In this article, we are among the first to fill this gap by examining privacy-preserving techniques for caching content at the edge network. Firstly, we provide an introduction to the background of privacy-preserving edge caching (PPEC). Next, we summarize the key privacy issues and present a taxonomy for caching at the edge network from the perspective of private information. Additionally, we conduct a retrospective review of the state-of-the-art countermeasures against privacy leakage from content caching at the edge network. Finally, we conclude the survey and envision challenges for future research.

**Link**: [arxiv](http://arxiv.org/abs/2405.01844v3),  [pdf](http://arxiv.org/pdf/2405.01844v3)

**Tags**: cs.NI cs.CR cs.DC 



### XKV: Personalized KV Cache Memory Reduction for Long-Context LLM   Inference
**Authors**: Weizhuo Li, Zhigang Wang, Yu Gu, Ge Yu

**Updated**: 2024-12-08T11:32:08Z

**Summary**: Recently the generative Large Language Model (LLM) has achieved remarkable success in numerous applications. Notably its inference generates output tokens one-by-one, leading to many redundant computations. The widely-used KV-Cache framework makes a compromise between time and space complexities. However, caching data generates the increasingly growing memory demand, that can quickly exhaust the limited memory capacity of the modern accelerator like GPUs, particularly in long-context inference tasks. Existing studies reduce memory consumption by evicting some of cached data that have less important impact on inference accuracy. But the benefit in practice is far from ideal due to the static cache allocation across different LLM network layers. This paper observes that the layer-specific cached data have very different impacts on accuracy. We quantify this difference, and give experimental and theoretical validation. We accordingly make a formal analysis and shows that customizing the cache size for each layer in a personalized manner can yield a significant memory reduction, while still providing comparable accuracy. We simulate the cache allocation as a combinatorial optimization problem and give a global optimal solution. In particular, we devise a mini- and sampling-based inference over a lightweight variant of the LLM model, so as to quickly capture the difference and then feed it into the personalized algorithms. Extensive experiments on real-world datasets demonstrate that our proposals can reduce KV cache memory consumption by 61.6% on average, improve computational efficiency by 2.1x and then increase the throughput by up to 5.5x.

**Link**: [arxiv](http://arxiv.org/abs/2412.05896v1),  [pdf](http://arxiv.org/pdf/2412.05896v1)

**Tags**: cs.LG cs.CL 



### Semi-Supervised Contrastive Learning for Controllable Video-to-Music   Retrieval
**Authors**: Shanti Stewart, Gouthaman KV, Lie Lu, Andrea Fanelli

**Updated**: 2024-12-08T06:37:27Z

**Summary**: Content creators often use music to enhance their videos, from soundtracks in movies to background music in video blogs and social media content. However, identifying the best music for a video can be a difficult and time-consuming task. To address this challenge, we propose a novel framework for automatically retrieving a matching music clip for a given video, and vice versa. Our approach leverages annotated music labels, as well as the inherent artistic correspondence between visual and music elements. Distinct from previous cross-modal music retrieval works, our method combines both self-supervised and supervised training objectives. We use self-supervised and label-supervised contrastive learning to train a joint embedding space between music and video. We show the effectiveness of our approach by using music genre labels for the supervised training component, and our framework can be generalized to other music annotations (e.g., emotion, instrument, etc.). Furthermore, our method enables fine-grained control over how much the retrieval process focuses on self-supervised vs. label information at inference time. We evaluate the learned embeddings through a variety of video-to-music and music-to-video retrieval tasks. Our experiments show that the proposed approach successfully combines self-supervised and supervised objectives and is effective for controllable music-video retrieval.

**Link**: [arxiv](http://arxiv.org/abs/2412.05831v1),  [pdf](http://arxiv.org/pdf/2412.05831v1)

**Tags**: cs.MM cs.SD eess.AS 



### Ultrafast lattice and electron dynamics induced in a PbSe crystal by an   intense terahertz pulse
**Authors**: A. A. Melnikov, Yu. G. Selivanov, D. G. Poydashev, S. V. Chekalin

**Updated**: 2024-12-07T17:22:14Z

**Summary**: We have studied the ultrafast optical response of a PbSe crystal to an intense picosecond terahertz pulse with a peak electric field strength of up to $\sim$ 500 kV/cm. The reflectivity anisotropy signal contains oscillations at the fundamental frequency of the resonant infrared-active phonon mode as well as its second, third, and fourth harmonics. The effect is ascribed to coherent anharmonic phonons resonantly excited by the strong terahertz field. Pump terahertz pulses also induce an almost instantaneous Kerr effect and a long-lived optical anisotropy of the crystal with a characteristic decay time of $\gtrsim$ 100 ps. We consider lattice distortion and phonon-assisted side valley population as possible origins of this metastable state.

**Link**: [arxiv](http://arxiv.org/abs/2412.05704v1),  [pdf](http://arxiv.org/pdf/2412.05704v1)

**Tags**: cond-mat.mtrl-sci 



### Batch-Max: Higher LLM Throughput using Larger Batch Sizes and KV Cache   Compression
**Authors**: Michael R. Metel, Boxing Chen, Mehdi Rezagholizadeh

**Updated**: 2024-12-07T16:41:54Z

**Summary**: Several works have developed eviction policies to remove key-value (KV) pairs from the KV cache for more efficient inference. The focus has been on compressing the KV cache after the input prompt has been processed for faster token generation. In settings with limited GPU memory, and when the input context is longer than the generation length, we show that by also compressing the KV cache during the input processing phase, larger batch sizes can be used resulting in significantly higher throughput while still maintaining the original model's accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2412.05693v1),  [pdf](http://arxiv.org/pdf/2412.05693v1)

**Tags**: cs.CL 



### DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via   Adaptive Heads Fusion
**Authors**: Yilong Chen, Linhao Zhang, Junyuan Shang, Zhenyu Zhang, Tingwen Liu, Shuohuan Wang, Yu Sun

**Updated**: 2024-12-07T13:23:39Z

**Summary**: Large language models (LLMs) with billions of parameters demonstrate impressive performance. However, the widely used Multi-Head Attention (MHA) in LLMs incurs substantial computational and memory costs during inference. While some efforts have optimized attention mechanisms by pruning heads or sharing parameters among heads, these methods often lead to performance degradation or necessitate substantial continued pre-training costs to restore performance. Based on the analysis of attention redundancy, we design a Decoupled-Head Attention (DHA) mechanism. DHA adaptively configures group sharing for key heads and value heads across various layers, achieving a better balance between performance and efficiency. Inspired by the observation of clustering similar heads, we propose to progressively transform the MHA checkpoint into the DHA model through linear fusion of similar head parameters step by step, retaining the parametric knowledge of the MHA checkpoint. We construct DHA models by transforming various scales of MHA checkpoints given target head budgets. Our experiments show that DHA remarkably requires a mere 0.25\% of the original model's pre-training budgets to achieve 97.6\% of performance while saving 75\% of KV cache. Compared to Group-Query Attention (GQA), DHA achieves a 5$\times$ training acceleration, a maximum of 13.93\% performance improvement under 0.01\% pre-training budget, and 4\% relative improvement under 0.05\% pre-training budget.

**Link**: [arxiv](http://arxiv.org/abs/2406.06567v2),  [pdf](http://arxiv.org/pdf/2406.06567v2)

**Tags**: cs.LG cs.AI cs.CL 



### PrefixKV: Adaptive Prefix KV Cache is What Vision Instruction-Following   Models Need for Efficient Generation
**Authors**: Ao Wang, Hui Chen, Jianchao Tan, Kefeng Zhang, Xunliang Cai, Zijia Lin, Jungong Han, Guiguang Ding

**Updated**: 2024-12-07T13:23:39Z

**Summary**: Recently, large vision-language models (LVLMs) have rapidly gained popularity for their strong generation and reasoning capabilities given diverse multimodal inputs. However, these models incur significant computational and memory overhead during inference, which greatly hinders the efficient deployment in practical scenarios. The extensive key-value (KV) cache, necessitated by the lengthy input and output sequences, notably contributes to the high inference cost. Based on this, recent works have investigated ways to reduce the KV cache size for higher efficiency. Although effective, they generally overlook the distinct importance distributions of KV vectors across layers and maintain the same cache size for each layer during the next token prediction. This results in the significant contextual information loss for certain layers, leading to notable performance decline. To address this, we present PrefixKV. It reframes the challenge of determining KV cache sizes for all layers into the task of searching for the optimal global prefix configuration. With an adaptive layer-wise KV retention recipe based on binary search, the maximum contextual information can thus be preserved in each layer, facilitating the generation. Extensive experiments demonstrate that our method achieves the state-of-the-art performance compared with others. It exhibits superior inference efficiency and generation quality trade-offs, showing promising potential for practical applications. Code is available at \url{https://github.com/THU-MIG/PrefixKV}.

**Link**: [arxiv](http://arxiv.org/abs/2412.03409v2),  [pdf](http://arxiv.org/pdf/2412.03409v2)

**Tags**: cs.CV 



### Spineless Traversal for Layout Invalidation
**Authors**: Marisa Kirisame, Tiezhi Wang, Pavel Panchekha

**Updated**: 2024-12-07T04:08:56Z

**Summary**: Latency is a major concern for web rendering engines like those in Chrome, Safari, and Firefox. These engines reduce latency by using an incremental layout algorithm to redraw the page when the user interacts with it. In such an algorithm, elements that change frame-to-frame are marked dirty; only the dirty elements need be processed to draw the next frame, dramatically reducing latency. However, the standard incremental layout algorithm must search the page for dirty elements, accessing a number of auxiliary elements in the process. These auxiliary elements add cache misses and stalled cycles, and are responsible for a sizable fraction of all layout latency. We introduce a new, faster incremental layout algorithm called Spineless Traversal. Spineless Traversal uses a more computationally demanding priority queue algorithm to avoid the need to access auxiliary nodes and thus reduces cache traffic and stalls. This leads to dramatic speedups on the most latency-critical interactions such as hovering, typing, or animations. Moreover, thanks to numerous low-level optimizations, we are able to make Spineless Traversal competitive across the whole spectrum of incremental layout workloads. As a result, across 2216 benchmarks, Spineless Traversal is faster on 78.2% of the benchmark, with a mean speedup of 3.23x concentrated in the most latency-critical interactions such as hovering, typing, and animations.

**Link**: [arxiv](http://arxiv.org/abs/2411.10659v2),  [pdf](http://arxiv.org/pdf/2411.10659v2)

**Tags**: cs.PL 



### Effect of electric field on excitons in wide quantum wells
**Authors**: Shiming Zheng, E. S. Khramtsov, I. V. Ignatiev

**Updated**: 2024-12-06T19:35:52Z

**Summary**: A microscopic model of a heterostructure with a quantum well (QW) is proposed to study the exciton behavior in an external electric field. The effect of an electric field ranging from 0 to 6 kV/cm applied to the GaAs/AlGaAs QW structure in the growth direction is studied for several QWs of various widths up to 100 nm. The three-dimensional Schr\"odinger equation (SE) of exciton is numerically solved using the finite difference method. Wave functions and energies for several states of the heavy-hole and light-hole excitons are calculated. Dependencies of the exciton state energy, the binding energy, the radiative broadening, and the static dipole moment on the applied electric fields are determined. The threshold of exciton dissociation for the 100-nm QW is also determined. In addition, we found the electric-field-induced shift of the center of mass of the heavy-hole and light-hole exciton in the QWs. Finally, we have modeled reflection spectra of heterostructures with the GaAs/AlGaAs QWs in the electric field using the calculated energies and radiative broadenings of excitons.

**Link**: [arxiv](http://arxiv.org/abs/2412.05392v1),  [pdf](http://arxiv.org/pdf/2412.05392v1)

**Tags**: cond-mat.mes-hall 



### MC3: Memory Contention based Covert Channel Communication on Shared DRAM   System-on-Chips
**Authors**: Ismet Dagli, James Crea, Soner Seckiner, Yuanchao Xu, Selçuk Köse, Mehmet E. Belviranli

**Updated**: 2024-12-06T17:58:57Z

**Summary**: Shared-memory system-on-chips (SM-SoC) are ubiquitously employed by a wide-range of mobile computing platforms, including edge/IoT devices, autonomous systems and smartphones. In SM-SoCs, system-wide shared physical memory enables a convenient and financially-feasible way to make data accessible by dozens of processing units (PUs), such as CPU cores and domain specific accelerators. In this study, we investigate vulnerabilities that stem from the shared use of physical memory in such systems. Due to the diverse computational characteristics of the PUs they embed, SM-SoCs often do not employ a shared last level cache (LLC). While the literature proposes covert channel attacks for shared memory systems, high-throughput communication is currently possible by either relying on an LLC or privileged/physical access to the shared memory subsystem.   In this study, we introduce a new memory-contention based covert communication attack, MC3, which specifically targets the shared system memory in mobile SoCs. Different from existing attacks, our approach achieves high throughput communication between applications running on CPU and GPU without the need for an LLC or elevated access to the system. We extensively explore the effectiveness of our methodology by demonstrating the trade-off between the channel transmission rate and the robustness of the communication. We demonstrate the utility of MC3 on NVIDIA Orin AGX, Orin NX, and Orin Nano up to a transmit rate of 6.4 kbps with less than 1% error rate.

**Link**: [arxiv](http://arxiv.org/abs/2412.05228v1),  [pdf](http://arxiv.org/pdf/2412.05228v1)

**Tags**: cs.CR 



### SwiftDiffusion: Efficient Diffusion Model Serving with Add-on Modules
**Authors**: Suyi Li, Lingyun Yang, Xiaoxiao Jiang, Hanfeng Lu, Dakai An, Zhipeng Di, Weiyi Lu, Jiawei Chen, Kan Liu, Yinghao Yu, Tao Lan, Guodong Yang, Lin Qu, Liping Zhang, Wei Wang

**Updated**: 2024-12-06T11:47:06Z

**Summary**: Text-to-image (T2I) generation using diffusion models has become a blockbuster service in today's AI cloud. A production T2I service typically involves a serving workflow where a base diffusion model is augmented with various "add-on" modules, notably ControlNet and LoRA, to enhance image generation control. Compared to serving the base model alone, these add-on modules introduce significant loading and computational overhead, resulting in increased latency. In this paper, we present SwiftDiffusion, a system that efficiently serves a T2I workflow through a holistic approach. SwiftDiffusion decouples ControNet from the base model and deploys it as a separate, independently scaled service on dedicated GPUs, enabling ControlNet caching, parallelization, and sharing. To mitigate the high loading overhead of LoRA serving, SwiftDiffusion employs a bounded asynchronous LoRA loading (BAL) technique, allowing LoRA loading to overlap with the initial base model execution by up to k steps without compromising image quality. Furthermore, SwiftDiffusion optimizes base model execution with a novel latent parallelism technique. Collectively, these designs enable SwiftDiffusion to outperform the state-of-the-art T2I serving systems, achieving up to 7.8x latency reduction and 1.6x throughput improvement in serving SDXL models on H800 GPUs, without sacrificing image quality.

**Link**: [arxiv](http://arxiv.org/abs/2407.02031v2),  [pdf](http://arxiv.org/pdf/2407.02031v2)

**Tags**: cs.DC cs.AI cs.LG 



### Ltri-LLM: Streaming Long Context Inference for LLMs with Training-Free   Dynamic Triangular Attention Pattern
**Authors**: Hongyin Tang, Di Xiu, Lanrui Wang, Xiurui Geng, Jingang Wang, Xunliang Cai

**Updated**: 2024-12-06T03:46:06Z

**Summary**: The quadratic computational complexity of the attention mechanism in current Large Language Models (LLMs) renders inference with long contexts prohibitively expensive. To address this challenge, various approaches aim to retain critical portions of the context to optimally approximate Full Attention (FA) through Key-Value (KV) compression or Sparse Attention (SA), enabling the processing of virtually unlimited text lengths in a streaming manner. However, these methods struggle to achieve performance levels comparable to FA, particularly in retrieval tasks. In this paper, our analysis of attention head patterns reveals that LLMs' attention distributions show strong local correlations, naturally reflecting a chunking mechanism for input context. We propose Ltri-LLM framework, which divides KVs into spans, stores them in an offline index, and retrieves the relevant KVs into memory for various queries. Experimental results on popular long text benchmarks show that Ltri-LLM can achieve performance close to FA while maintaining efficient, streaming-based inference.

**Link**: [arxiv](http://arxiv.org/abs/2412.04757v1),  [pdf](http://arxiv.org/pdf/2412.04757v1)

**Tags**: cs.CL cs.LG 



### One-Hop Sub-Query Result Caches for Graph Database Systems
**Authors**: Hieu Nguyen, Jun Li, Shahram Ghandeharizadeh

**Updated**: 2024-12-06T01:20:47Z

**Summary**: This paper introduces a novel one-hop sub-query result cache for processing graph read transactions, gR-Txs, in a graph database system. The one-hop navigation is from a vertex using either its in-coming or out-going edges with selection predicates that filter edges and vertices. Its cache entry identifies a unique one-hop sub-query (key) and its result set consisting of immutable vertex ids (value). When processing a gR-Tx, the query processor identifies its sequence of individual one-hop sub-queries and looks up their results in the cache. A cache hit fetches less data from the storage manager and eliminates the requirement to process the one-hop sub-query. A cache miss populates the cache asynchronously and in a transactional manner, maintaining the separation of read and write paths of our transactional storage manager. A graph read and write transaction, gRW-Tx, identifies the impacted cache entries and either deletes or updates them. Our implementation of the cache is inside the graph query processing engine and transparent to a user application. We evaluate the cache using our eCommerce production workload and with rules that re-write graph queries to maximize the performance enhancements observed with the cache. Obtained results show the cache enhances 95th and 99th percentile of query response times by at least 2x and 1.63x, respectively. When combined with query re-writing, the enhancements are at least 2.33x and 4.48x, respectively. An interesting result is the significant performance enhancement observed by the indirect beneficiaries of the cache, gRW-Txs and gR-Txs that do not reference one-hop sub-queries. The cache frees system resources to expedite their processing significantly.

**Link**: [arxiv](http://arxiv.org/abs/2412.04698v1),  [pdf](http://arxiv.org/pdf/2412.04698v1)

**Tags**: cs.DB cs.PF 



### Cross-Self KV Cache Pruning for Efficient Vision-Language Inference
**Authors**: Xiaohuan Pei, Tao Huang, Chang Xu

**Updated**: 2024-12-05T22:47:17Z

**Summary**: KV cache pruning has emerged as a promising technique for reducing memory and computation costs in long-context auto-regressive generation. Existing methods for vision-language models (VLMs) typically rely on self-attention scores from large language models (LLMs) to identify and prune irrelevant tokens. However, these approaches overlook the inherent distributional discrepancies between modalities, often leading to inaccurate token importance estimation and the over-pruning of critical visual tokens. To address this, we propose decomposing attention scores into intra-modality attention (within the same modality) and inter-modality attention (across modalities), enabling more precise KV cache pruning by independently managing these distinct attention types. Additionally, we introduce an n-softmax function to counteract distribution shifts caused by pruning, preserving the original smoothness of attention scores and ensuring stable performance. Our final training-free method, \textbf{C}ross-\textbf{S}elf \textbf{P}runing (CSP), achieves competitive performance compared to models with full KV caches while significantly outperforming previous pruning methods. Extensive evaluations on MileBench, a benchmark encompassing 29 multimodal datasets, demonstrate CSP's effectiveness, achieving up to a 41\% performance improvement on challenging tasks like conversational embodied dialogue while reducing the KV cache budget by 13.6\%. The code is available at https://github.com/TerryPei/CSP

**Link**: [arxiv](http://arxiv.org/abs/2412.04652v1),  [pdf](http://arxiv.org/pdf/2412.04652v1)

**Tags**: cs.CV cs.AI 



### Neural Two-Level Monte Carlo Real-Time Rendering
**Authors**: Mikhail Dereviannykh, Dmitrii Klepikov, Johannes Hanika, Carsten Dachsbacher

**Updated**: 2024-12-05T22:06:23Z

**Summary**: We introduce an efficient Two-Level Monte Carlo (subset of Multi-Level Monte Carlo, MLMC) estimator for real-time rendering of scenes with global illumination. Using MLMC we split the shading integral into two parts: the radiance cache integral and the residual error integral that compensates for the bias of the first one. For the first part, we developed the Neural Incident Radiance Cache (NIRC) leveraging the power of fully-fused tiny neural networks as a building block, which is trained on the fly. The cache is designed to provide a fast and reasonable approximation of the incident radiance: an evaluation takes 2-25x less compute time than a path tracing sample. This enables us to estimate the radiance cache integral with a high number of samples and by this achieve faster convergence. For the residual error integral, we compute the difference between the NIRC predictions and the unbiased path tracing simulation. Our method makes no assumptions about the geometry, materials, or lighting of a scene and has only few intuitive hyper-parameters. We provide a comprehensive comparative analysis in different experimental scenarios. Since the algorithm is trained in an on-line fashion, it demonstrates significant noise level reduction even for dynamic scenes and can easily be combined with other importance sampling schemes and noise reduction techniques.

**Link**: [arxiv](http://arxiv.org/abs/2412.04634v1),  [pdf](http://arxiv.org/pdf/2412.04634v1)

**Tags**: cs.GR cs.AI 



### p-MoD: Building Mixture-of-Depths MLLMs via Progressive Ratio Decay
**Authors**: Jun Zhang, Desen Meng, Ji Qi, Zhenpeng Huang, Tao Wu, Limin Wang

**Updated**: 2024-12-05T18:58:03Z

**Summary**: Despite the remarkable performance of multimodal large language models (MLLMs) across diverse tasks, the substantial training and inference costs impede their advancement. The majority of computation stems from the overwhelming volume of vision tokens processed by the transformer decoder. In this paper, we propose to build efficient MLLMs by leveraging the Mixture-of-Depths (MoD) mechanism, where each transformer decoder layer selects essential vision tokens to process while skipping redundant ones. However, integrating MoD into MLLMs is non-trivial. To address the challenges of training and inference stability as well as limited training data, we adapt the MoD module with two novel designs: tanh-gated weight normalization (TanhNorm) and symmetric token reweighting (STRing). Moreover, we observe that vision tokens exhibit higher redundancy in deeper layer and thus design a progressive ratio decay (PRD) strategy, which gradually reduces the token retention ratio layer by layer, employing a shifted cosine schedule. This crucial design fully unleashes the potential of MoD, significantly boosting the efficiency and performance of our models. To validate the effectiveness of our approach, we conduct extensive experiments with two baseline models across 14 benchmarks. Our model, p-MoD, matches or even surpasses the performance of the baseline models, with only 55.6% TFLOPs and 53.8% KV cache storage during inference, and 77.7% GPU hours during training.

**Link**: [arxiv](http://arxiv.org/abs/2412.04449v1),  [pdf](http://arxiv.org/pdf/2412.04449v1)

**Tags**: cs.CV cs.CL 



### SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving   Model Transformation
**Authors**: Aurick Qiao, Zhewei Yao, Samyam Rajbhandari, Yuxiong He

**Updated**: 2024-12-05T14:56:56Z

**Summary**: LLM inference for popular enterprise use cases, such as summarization, RAG, and code-generation, typically observes orders of magnitude longer prompt lengths than generation lengths. This characteristic leads to high cost of prefill and increased response latency. In this paper, we present SwiftKV, a novel model transformation and distillation procedure specifically designed to reduce the time and cost of processing prompt tokens while preserving high quality of generated tokens. SwiftKV combines three key mechanisms: i) SingleInputKV, which prefills later layers' KV cache using a much earlier layer's output, allowing prompt tokens to skip much of the model computation, ii) AcrossKV, which merges the KV caches of neighboring layers to reduce the memory footprint and support larger batch size for higher throughput, and iii) a knowledge-preserving distillation procedure that can adapt existing LLMs for SwiftKV with minimal accuracy impact and low compute and data requirement. For Llama-3.1-8B and 70B, SwiftKV reduces the compute requirement of prefill by 50% and the memory requirement of the KV cache by 62.5% while incurring minimum quality degradation across a wide range of tasks. In the end-to-end inference serving using an optimized vLLM implementation, SwiftKV realizes up to 2x higher aggregate throughput and 60% lower time per output token. It can achieve a staggering 560 TFlops/GPU of normalized inference throughput, which translates to 16K tokens/s for Llama-3.1-70B in 16-bit precision on 4x H100 GPUs. Our training, inference, and model implementations are open-sourced and can be found through https://huggingface.co/collections/Snowflake/swiftkv-models-674f7d7474eb789e185d31cb.

**Link**: [arxiv](http://arxiv.org/abs/2410.03960v2),  [pdf](http://arxiv.org/pdf/2410.03960v2)

**Tags**: cs.LG cs.AI cs.CL 



### KV Shifting Attention Enhances Language Modeling
**Authors**: Mingyu Xu, Wei Cheng, Bingning Wang, Weipeng Chen

**Updated**: 2024-12-05T12:19:38Z

**Summary**: The current large language models are mainly based on decode-only structure transformers, which have great in-context learning (ICL) capabilities. It is generally believed that the important foundation of its ICL capability is the induction heads mechanism, which requires at least two layers attention. In order to more efficiently implement the ability of the model's induction, we revisit the induction heads mechanism and proposed a KV shifting attention. We theoretically prove that the KV shifting attention reducing the model's requirements for the depth and width of the induction heads mechanism. Our experimental results demonstrate that KV shifting attention is beneficial to learning induction heads and language modeling, which lead to better performance or faster convergence from toy models to the pre-training models with more than 10 B parameters.

**Link**: [arxiv](http://arxiv.org/abs/2411.19574v2),  [pdf](http://arxiv.org/pdf/2411.19574v2)

**Tags**: cs.CL 



### A Little Goes a Long Way: Efficient Long Context Training and Inference   with Partial Contexts
**Authors**: Suyu Ge, Xihui Lin, Yunan Zhang, Jiawei Han, Hao Peng

**Updated**: 2024-12-05T06:52:42Z

**Summary**: Training and serving long-context large language models (LLMs) incurs substantial overhead. To address this, two critical steps are often required: a pretrained LLM typically undergoes a separate stage for context length extension by training on long-context data, followed by architectural modifications to reduce the overhead of KV cache during serving. This paper argues that integrating length extension with a GPU-friendly KV cache reduction architecture not only reduces training overhead during length extension, but also achieves better long-context performance. This leads to our proposed LongGen, which finetunes a pretrained LLM into an efficient architecture during length extension. LongGen builds on three key insights: (1) Sparse attention patterns, such as window attention (attending to recent tokens), attention sink (initial ones), and blockwise sparse attention (strided token blocks) are well-suited for building efficient long-context models, primarily due to their GPU-friendly memory access patterns, enabling efficiency gains not just theoretically but in practice as well. (2) It is essential for the model to have direct access to all tokens. A hybrid architecture with 1/3 full attention layers and 2/3 efficient ones achieves a balanced trade-off between efficiency and long-context performance. (3) Lightweight training on 5B long-context data is sufficient to extend the hybrid model's context length from 4K to 128K.   We evaluate LongGen on both Llama-2 7B and Llama-2 70B, demonstrating its effectiveness across different scales. During training with 128K-long contexts, LongGen achieves 1.55x training speedup and reduces wall-clock time by 36%, compared to a full-attention baseline. During inference, LongGen reduces KV cache memory by 62%, achieving 1.67x prefilling speedup and 1.41x decoding speedup.

**Link**: [arxiv](http://arxiv.org/abs/2410.01485v2),  [pdf](http://arxiv.org/pdf/2410.01485v2)

**Tags**: cs.CL 



### Yi-Lightning Technical Report
**Authors**: 01. AI, :, Alan Wake, Albert Wang, Bei Chen, C. X. Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, Fan Zhou, Feng Hu, Heng Ji, Howard Qiu, Jiangcheng Zhu, Jun Tian, Katherine Su, Lihuan Zhang, Liying Li, Ming Song, Mou Li, Peng Liu, Qicheng Hu, Shawn Wang, Shijun Zhou, Shiyong Li, Tianhang Zhu, Wen Xie, Xiang He, Xiaobo Chen, Xiaohui Hu, Xiaoyi Ren, Xinyao Niu, Yanpeng Li, Yongke Zhao, Yongzhen Luo, Yuchi Xu, Yuxuan Sha, Zhaodong Yan, Zhiyuan Liu, Zirui Zhang

**Updated**: 2024-12-05T04:29:49Z

**Summary**: This technical report presents Yi-Lightning, our latest flagship large language model (LLM). It achieves exceptional performance, ranking 6th overall on Chatbot Arena, with particularly strong results (2nd to 4th place) in specialized categories including Chinese, Math, Coding, and Hard Prompts. Yi-Lightning leverages an enhanced Mixture-of-Experts (MoE) architecture, featuring advanced expert segmentation and routing mechanisms coupled with optimized KV-caching techniques. Our development process encompasses comprehensive pre-training, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF), where we devise deliberate strategies for multi-stage training, synthetic data construction, and reward modeling. Furthermore, we implement RAISE (Responsible AI Safety Engine), a four-component framework to address safety issues across pre-training, post-training, and serving phases. Empowered by our scalable super-computing infrastructure, all these innovations substantially reduce training, deployment and inference costs while maintaining high-performance standards. With further evaluations on public academic benchmarks, Yi-Lightning demonstrates competitive performance against top-tier LLMs, while we observe a notable disparity between traditional, static benchmark results and real-world, dynamic human preferences. This observation prompts a critical reassessment of conventional benchmarks' utility in guiding the development of more intelligent and powerful AI systems for practical applications. Yi-Lightning is now available through our developer platform at https://platform.lingyiwanwu.com.

**Link**: [arxiv](http://arxiv.org/abs/2412.01253v3),  [pdf](http://arxiv.org/pdf/2412.01253v3)

**Tags**: cs.CL cs.AI cs.LG 



### F2: Designing a Key-Value Store for Large Skewed Workloads
**Authors**: Konstantinos Kanellis, Badrish Chandramouli, Shivaram Venkataraman

**Updated**: 2024-12-05T01:50:27Z

**Summary**: Many real-world workloads present a challenging set of requirements: point operations requiring high throughput, working sets much larger than main memory, and natural skew in key access patterns for both reads and writes. We find that modern key-value designs are either optimized for memory-efficiency, sacrificing high-performance (LSM-tree designs), or achieve high-performance, saturating modern NVMe SSD bandwidth, at the cost of substantial memory resources or high disk wear (CPU-optimized designs). Unfortunately these designs are not able to handle meet the challenging demands of such larger-than-memory, skewed workloads.   To this end, we present F2, a new key-value store that bridges this gap by combining the strengths of both approaches. F2 adopts a tiered, record-oriented architecture inspired by LSM-trees to effectively separate hot from cold records, while incorporating concurrent latch-free mechanisms from CPU-optimized engines to maximize performance on modern NVMe SSDs. To realize this design, we tackle key challenges and introduce several innovations, including new latch-free algorithms for multi-threaded log compaction and user operations (e.g., RMWs), as well as new components: a two-level hash index to reduce indexing overhead for cold records and a read-cache for serving read-hot data.   Detailed experimental results show that F2 matches or outperforms existing solutions, achieving on average better throughput on memory-constrained environments compared to state-of-the-art systems like RocksDB (11.75x), SplinterDB (4.52x), KVell (10.56x), LeanStore (2.04x), and FASTER (2.38x). F2 also maintains its high performance across varying workload skewness levels and memory budgets, while achieving low disk write amplification.

**Link**: [arxiv](http://arxiv.org/abs/2305.01516v2),  [pdf](http://arxiv.org/pdf/2305.01516v2)

**Tags**: cs.DB 



### Marconi: Prefix Caching for the Era of Hybrid LLMs
**Authors**: Rui Pan, Zhuang Wang, Zhen Jia, Can Karakus, Luca Zancato, Tri Dao, Yida Wang, Ravi Netravali

**Updated**: 2024-12-04T18:40:24Z

**Summary**: Hybrid models that combine the language modeling capabilities of Attention layers with the efficiency of Recurrent layers (e.g., State Space Models) have gained traction in practically supporting long contexts in Large Language Model serving. Yet, the unique properties of these models complicate the usage of complementary efficiency optimizations such as prefix caching that skip redundant computations across requests. Most notably, their use of in-place state updates for recurrent layers precludes rolling back cache entries for partial sequence overlaps, and instead mandates only exact-match cache hits; the effect is a deluge of (large) cache entries per sequence, most of which yield minimal reuse opportunities. We present Marconi, the first system that supports efficient prefix caching with Hybrid LLMs. Key to Marconi are its novel admission and eviction policies that more judiciously assess potential cache entries based not only on recency, but also on (1) forecasts of their reuse likelihood across a taxonomy of different hit scenarios, and (2) the compute savings that hits deliver relative to memory footprints. Across diverse workloads and Hybrid models, Marconi achieves up to 34.4$\times$ higher token hit rates (71.1% or 617 ms lower TTFT) compared to state-of-the-art prefix caching systems.

**Link**: [arxiv](http://arxiv.org/abs/2411.19379v2),  [pdf](http://arxiv.org/pdf/2411.19379v2)

**Tags**: cs.DC cs.AI cs.LG 



### Measurement of electron beam induced sample heating in SEM experiments
**Authors**: Christina Koenig, Alice Bastos da Silva Fanta, Joerg R. Jinschek

**Updated**: 2024-12-04T14:47:42Z

**Summary**: Scanning Electron Microscopy (SEM) experiments provide detailed insights into material microstructures, enabling high-resolution imaging as well as crystallographic analysis through advanced techniques like Electron Backscatter Diffraction (EBSD). However, the interaction of the high-energy electron beam with the material can lead to localized heating, which may significantly impact specimen integrity, especially in applications requiring prolonged beam exposure, for instance when mapping the crystal structure using EBSD. This study examines electron-beam-induced heating effects on a model metal sample (iron), directly measuring the locally deposited electron beam energy with a MEMS-based heating device and validating these measurements through simulations, including Monte Carlo and Finite Element methods. The analysis focuses on the effects of various experimental parameters such as acceleration voltage (from 5 to 30 kV), beam current (from 0.17 nA to 22 nA), dwell time (from 1$\mu$s to 1ms) and sample tilt (0{\deg} to 70{\deg}). The findings reveal that local sample temperatures can increase by up to 70 {\deg}C during EBSD experiments, primarily affected by the choice in beam current and acceleration voltage, with beam current having the most significant impact.

**Link**: [arxiv](http://arxiv.org/abs/2412.03361v1),  [pdf](http://arxiv.org/pdf/2412.03361v1)

**Tags**: cond-mat.mtrl-sci physics.app-ph 



### ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable   Compression
**Authors**: Guangda Liu, Chengwei Li, Jieru Zhao, Chenqi Zhang, Minyi Guo

**Updated**: 2024-12-04T10:58:27Z

**Summary**: Large Language Models (LLMs) have been widely deployed in a variety of applications, and the context length is rapidly increasing to handle tasks such as long-document QA and complex logical reasoning. However, long context poses significant challenges for inference efficiency, including high memory costs of key-value (KV) cache and increased latency due to extensive memory accesses. Recent works have proposed compressing KV cache to approximate computation, but these methods either evict tokens permanently, never recalling them for later inference, or recall previous tokens at the granularity of pages divided by textual positions. Both approaches degrade the model accuracy and output quality. To achieve efficient and accurate recallable KV cache compression, we introduce ClusterKV, which recalls tokens at the granularity of semantic clusters. We design and implement efficient algorithms and systems for clustering, selection, indexing and caching. Experiment results show that ClusterKV attains negligible accuracy loss across various tasks with 32k context lengths, using only a 1k to 2k KV cache budget, and achieves up to a 2$\times$ speedup in latency and a 2.5$\times$ improvement in decoding throughput. Compared to SoTA recallable KV compression methods, ClusterKV demonstrates higher model accuracy and output quality, while maintaining or exceeding inference efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.03213v1),  [pdf](http://arxiv.org/pdf/2412.03213v1)

**Tags**: cs.LG cs.AI cs.PF 



### Unifying KV Cache Compression for Large Language Models with LeanKV
**Authors**: Yanqi Zhang, Yuwei Hu, Runyuan Zhao, John C. S. Lui, Haibo Chen

**Updated**: 2024-12-04T08:51:23Z

**Summary**: Large language models (LLMs) demonstrate exceptional performance but incur high serving costs due to substantial memory demands, with the key-value (KV) cache being a primary bottleneck. Existing KV cache compression methods, including quantization and pruning, struggle with limitations such as uniform treatment of keys and values and static memory allocation across attention heads. To address these challenges, we introduce LeanKV, a unified KV cache compression framework that enhances LLM serving efficiency without compromising accuracy through three innovations: (1) Hetero-KV quantization, which stores keys at a higher precision than values to reflect their greater impact on attention computations; (2) per-head dynamic sparsity, which allocates memory based on token importance per head and per request; and (3) unified KV compression, integrating mixed-precision quantization and selective pruning to enable a smooth tradeoff between model accuracy and memory efficiency. To efficiently support these techniques, LeanKV introduces systems optimizations including unified paging and on-GPU parallel memory management. Implemented on vLLM, LeanKV compresses the KV cache by $3.0\times$ to $5.0\times$ without accuracy loss and up to $11.0\times$ with under 5% accuracy loss, enhancing throughput by $1.9\times$ to $2.5\times$, and up to $6.9\times$.

**Link**: [arxiv](http://arxiv.org/abs/2412.03131v1),  [pdf](http://arxiv.org/pdf/2412.03131v1)

**Tags**: cs.LG cs.DC 



### PASCAL: A Learning-aided Cooperative Bandwidth Control Policy for   Hierarchical Storage Systems
**Authors**: Xijun Li, Yunfan Zhou, Ji Zhang

**Updated**: 2024-12-04T05:32:12Z

**Summary**: Nowadays, the Hierarchical Storage System (HSS) is considered as an ideal model to meet the cost-performance demand. The data migration between storing tiers of HSS is the way to achieve the cost-performance goal. The bandwidth control is to limit the maximum amount of data migration. Most of previous research about HSS focus on studying the data migration policy instead of bandwidth control. However, the recent research about cache and networking optimization suggest that the bandwidth control has significant impact on the system performance. Few previous work achieves a satisfactory bandwidth control in HSS since it is hard to control bandwidth for so many data migration tasks simultaneously. In this paper, we first give a stochastic programming model to formalize the bandwidth control problem in HSS. Then we propose a learning-aided bandwidth control policy for HSS, named \Pascal{}, which learns to control the bandwidth of different data migration task in an cooperative way. We implement \Pascal{} on a commercial HSS and compare it with three strong baselines over a group of workloads. Our evaluation on the physical system shows that \Pascal{} can effectively decrease 1.95X the tail latency and greatly improve throughput stability (2X $\downarrow$ throughput jitter), and meanwhile keep the throughput at a relatively high level.

**Link**: [arxiv](http://arxiv.org/abs/2303.08066v2),  [pdf](http://arxiv.org/pdf/2303.08066v2)

**Tags**: cs.NI 



### A Multi-Functional Web Tool for Comprehensive Threat Detection Through   IP Address Analysis
**Authors**: Cebajel Tanan, Sameer G. Kulkarni, Tamal Das, Manjesh K. Hanawal

**Updated**: 2024-12-04T04:29:12Z

**Summary**: In recent years, the advances in digitalisation have also adversely contributed to the significant rise in cybercrimes. Hence, building the threat intelligence to shield against rising cybercrimes has become a fundamental requisite. Internet Protocol (IP) addresses play a crucial role in the threat intelligence and prevention of cyber crimes. However, we have noticed the lack of one-stop, free, and open-source tools that can analyse IP addresses. Hence, this work introduces a comprehensive web tool for advanced IP address characterisation. Our tool offers a wide range of features, including geolocation, blocklist check, VPN detection, proxy detection, bot detection, Tor detection, port scan, and accurate domain statistics that include the details about the name servers and registrar information. In addition, our tool calculates a confidence score based on a weighted sum of publicly accessible online results from different reliable sources to give users a dependable measure of accuracy. Further, to improve performance, our tool also incorporates a local database for caching the results, to enable fast content retrieval with minimal external Web API calls. Our tool supports domain names and IPv4 addresses, making it a multi-functional and powerful IP analyser tool for threat intelligence. Our tool is available at www.ipanalyzer.in

**Link**: [arxiv](http://arxiv.org/abs/2412.03023v1),  [pdf](http://arxiv.org/pdf/2412.03023v1)

**Tags**: cs.CR 



### cRVR: A Stackelberg Game Approach for Joint Privacy-Aware Video   Requesting and Edge Caching
**Authors**: Xianzhi Zhang, Linchang Xiao, Yipeng Zhou, Miao Hu, Di Wu, John C. S. Lui, Quan Z. Sheng

**Updated**: 2024-12-03T22:48:09Z

**Summary**: As users conveniently stream their favorite online videos, video request records are automatically stored by video content providers, which have a high chance of privacy leakage. Unfortunately, most existing privacy-enhancing approaches are not applicable for protecting user privacy in video requests, because they cannot be easily altered or distorted by users and must be visible for content providers to stream correct videos. To preserve request privacy in online video services, it is possible to request additional videos that are irrelevant to users' interests so that content providers cannot precisely infer users' interest information. However, a naive redundant requesting approach would significantly degrade the performance of edge caches and increase bandwidth overhead. In this paper, we are among the first to propose a Cache-Friendly Redundant Video Requesting (cRVR) algorithm for User Devices (UDs) and its corresponding caching algorithm for the Edge Cache (EC), which can effectively mitigate the problem of request privacy leakage with minimal impact on the EC's performance. To tackle the problem, we first develop a Stackelberg game to analyze the dedicated interaction between UDs and EC, and obtain their optimal strategies to maximize their respective utility. For UDs, the utility function is a combination of both video playback utility and privacy protection utility. We prove the existence and uniqueness of the equilibrium of the Stackelberg game. Extensive experiments are conducted with real traces to demonstrate that cRVR can effectively protect video request privacy by reducing up to 59.03\% of privacy disclosure compared to baseline algorithms. Meanwhile, the caching performance of EC is only slightly affected.

**Link**: [arxiv](http://arxiv.org/abs/2310.12622v2),  [pdf](http://arxiv.org/pdf/2310.12622v2)

**Tags**: cs.NI 



### GoldFish: Serverless Actors with Short-Term Memory State for the   Edge-Cloud Continuum
**Authors**: Cynthia Marcelino, Jack Shahhoud, Stefan Nastic

**Updated**: 2024-12-03T22:02:42Z

**Summary**: Serverless Computing is a computing paradigm that provides efficient infrastructure management and elastic scalability. Serverless functions scale up or down based on demand, which means that functions are not directly addressable and rely on platform-managed invocation. Serverless stateless nature requires functions to leverage external services, such as object storage and KVS, to exchange data. Serverless actors have emerged as a solution to these issues. However, the state-of-the-art serverless lifecycle and event-trigger invocation force actors to leverage remote services to manage their state and exchange data, which impacts the performance and incurs additional costs and dependency on third-party services.   To address these issues, in this paper, we introduce a novel serverless lifecycle model that allows short-term stateful actors, enabling actors to maintain their state between executions. Additionally, we propose a novel serverless Invocation Model that enables serverless actors to influence the processing of future messages. We present GoldFish, a lightweight WebAssembly short-term stateful serverless actor platform that provides a novel serverless actor lifecycle and invocation model. GoldFish leverages WebAssembly to provide the actors with lightweight sandbox isolation, making them suitable for the Edge-Cloud Continuum, where computational resources are limited. Experimental results show that GoldFish optimizes the data exchange latency by up to 92% and increases the throughput by up to 10x compared to OpenFaaS and Spin.

**Link**: [arxiv](http://arxiv.org/abs/2412.02867v1),  [pdf](http://arxiv.org/pdf/2412.02867v1)

**Tags**: cs.DC 



### Value Residual Learning For Alleviating Attention Concentration In   Transformers
**Authors**: Zhanchao Zhou, Tianyi Wu, Zhiyun Jiang, Zhenzhong Lan

**Updated**: 2024-12-03T12:36:19Z

**Summary**: Transformers can capture long-range dependencies using self-attention, allowing tokens to attend to all others directly. However, stacking multiple attention layers leads to attention concentration. One natural way to address this issue is to use cross-layer attention, allowing information from earlier layers to be directly accessible to later layers. However, this approach is computationally expensive. To address this problem, we propose Transformer with residual value (ResFormer) which approximates cross-layer attention through adding a residual connection from the values of the the first layer to all subsequent layers. Based on this method, one variant is the Transformer with single layer value (SVFormer), where all layers share the same value embedding from first layer. Comprehensive empirical evidence demonstrates ResFormer achieves equivalent validation loss with 10.4% fewer model parameters and 13.6% less training data compared to Transformer, while maintaining similar memory usage and computational cost. Besides, SVFormer reduces KV cache size by nearly half with only a small performance penalty and can be integrated with other KV-efficient methods, yielding further reductions in KV cache, with performance influenced by sequence length and cumulative learning rate. Further visualization results suggest that Resformer and SVFormer alleviate attention concentration in deeper layers through avoiding value-state drains and enhance representation across most layers.

**Link**: [arxiv](http://arxiv.org/abs/2410.17897v3),  [pdf](http://arxiv.org/pdf/2410.17897v3)

**Tags**: cs.CL 



### Compressing KV Cache for Long-Context LLM Inference with Inter-Layer   Attention Similarity
**Authors**: Da Ma, Lu Chen, Situo Zhang, Yuxun Miao, Su Zhu, Zhi Chen, Hongshen Xu, Hanqi Li, Shuai Fan, Lei Pan, Kai Yu

**Updated**: 2024-12-03T08:29:27Z

**Summary**: The increasing context window size in Large Language Models (LLMs), such as the GPT and LLaMA series, has improved their ability to tackle complex, long-text tasks, but at the cost of inference efficiency, particularly regarding memory and computational complexity. Existing methods, including selective token retention and window-based attention, improve efficiency but risk discarding important tokens needed for future text generation. In this paper, we propose an approach that enhances LLM efficiency without token loss by reducing the memory and computational load of less important tokens, rather than discarding them.We address two challenges: 1) investigating the distribution of important tokens in the context, discovering recent tokens are more important than distant tokens in context, and 2) optimizing resources for distant tokens by sharing attention scores across layers. The experiments show that our method saves $35\%$ KV cache without compromising the performance.

**Link**: [arxiv](http://arxiv.org/abs/2412.02252v1),  [pdf](http://arxiv.org/pdf/2412.02252v1)

**Tags**: cs.CL 



### Improving Sequential Recommender Systems with Online and In-store User   Behavior
**Authors**: Luyi Ma, Aashika Padmanabhan, Anjana Ganesh, Shengwei Tang, Jiao Chen, Xiaohan Li, Lalitesh Morishetti, Kaushiki Nag, Malay Patel, Jason Cho, Sushant Kumar, Kannan Achan

**Updated**: 2024-12-03T03:20:40Z

**Summary**: Online e-commerce platforms have been extending in-store shopping, which allows users to keep the canonical online browsing and checkout experience while exploring in-store shopping. However, the growing transition between online and in-store becomes a challenge to sequential recommender systems for future online interaction prediction due to the lack of holistic modeling of hybrid user behaviors (online and in-store). The challenges are twofold. First, combining online and in-store user behavior data into a single data schema and supporting multiple stages in the model life cycle (pre-training, training, inference, etc.) organically needs a new data pipeline design. Second, online recommender systems, which solely rely on online user behavior sequences, must be redesigned to support online and in-store user data as input under the sequential modeling setting. To overcome the first challenge, we propose a hybrid, omnichannel data pipeline to compile online and in-store user behavior data by caching information from diverse data sources. Later, we introduce a model-agnostic encoder module to the sequential recommender system to interpret the user in-store transaction and augment the modeling capacity for better online interaction prediction given the hybrid user behavior.

**Link**: [arxiv](http://arxiv.org/abs/2412.02122v1),  [pdf](http://arxiv.org/pdf/2412.02122v1)

**Tags**: cs.IR 



### Development and Application of a Decentralized Domain Name Service
**Authors**: Guang Yang

**Updated**: 2024-12-02T20:39:56Z

**Summary**: The current Domain Name System (DNS), as a core infrastructure of the internet, exhibits several shortcomings: its centralized architecture leads to censorship risks and single points of failure, making domain name resolution vulnerable to attacks. The lack of encryption in the resolution process exposes it to DNS hijacking and cache poisoning attacks. Additionally, the high operational costs limit participation and innovation among small to medium-sized users. To address these issues, this paper proposes a Decentralized Domain Name Service (DDNS) based on blockchain (Phicoin) and distributed storage (IPFS). By leveraging the immutability of blockchain and the content verification of IPFS, the system achieves decentralized storage and distribution of domain name records, eliminating the centralized dependencies of traditional DNS. With a block time of 15 seconds, the system supports rapid broadcasting of domain name updates, significantly improving resolution efficiency. The DDNS aims to serve as a complement or backup to the existing DNS system, providing a pollution-resistant, censorship-resistant, high-performance, and low-cost domain name resolution solution, offering a new technical path for the security and stability of the internet.

**Link**: [arxiv](http://arxiv.org/abs/2412.01959v1),  [pdf](http://arxiv.org/pdf/2412.01959v1)

**Tags**: cs.NI 



### RandAR: Decoder-only Autoregressive Visual Generation in Random Orders
**Authors**: Ziqi Pang, Tianyuan Zhang, Fujun Luan, Yunze Man, Hao Tan, Kai Zhang, William T. Freeman, Yu-Xiong Wang

**Updated**: 2024-12-02T18:59:53Z

**Summary**: We introduce RandAR, a decoder-only visual autoregressive (AR) model capable of generating images in arbitrary token orders. Unlike previous decoder-only AR models that rely on a predefined generation order, RandAR removes this inductive bias, unlocking new capabilities in decoder-only generation. Our essential design enables random order by inserting a "position instruction token" before each image token to be predicted, representing the spatial location of the next image token. Trained on randomly permuted token sequences -- a more challenging task than fixed-order generation, RandAR achieves comparable performance to its conventional raster-order counterpart. More importantly, decoder-only transformers trained from random orders acquire new capabilities. For the efficiency bottleneck of AR models, RandAR adopts parallel decoding with KV-Cache at inference time, enjoying 2.5x acceleration without sacrificing generation quality. Additionally, RandAR supports inpainting, outpainting and resolution extrapolation in a zero-shot manner. We hope RandAR inspires new directions for decoder-only visual generation models and broadens their applications across diverse scenarios. Our project page is at https://rand-ar.github.io/.

**Link**: [arxiv](http://arxiv.org/abs/2412.01827v1),  [pdf](http://arxiv.org/pdf/2412.01827v1)

**Tags**: cs.CV cs.AI 



### Local and Regional Contributions to Tropospheric Ozone Concentrations
**Authors**: Callum E. Flowerday, Ryan Thalman, Jaron C. Hansen

**Updated**: 2024-12-02T16:10:26Z

**Summary**: The Wasatch Front in Utah, USA, is currently a non-attainment area for ozone according to the Environmental Protection Agency's (EPA) National Ambient Air Quality Standards (NAAQS). Nitrogen oxides ($\mathrm{NO_x = NO_2 + NO}$) and volatile organic compounds (VOCs), in the presence of sunlight, lead to ozone formation in the troposphere. When the rate of oxidant production, defined as the sum of $\mathrm{O_3}$ and $\mathrm{NO_2}$, is faster than the rate of $\mathrm{NO_x}$ production, a region is said to be $\mathrm{NO_x}$limited, and ozone formation will be limited by the concentration of $\mathrm{NO_x}$ species in the region. The inverse of this situation makes the region VOC-limited. Knowing whether a region is $\mathrm{NO_x}$-limited or VOC-limited can aid in generating effective mitigation strategies. Understanding the background or regional contributions to ozone in a region, whether from the transport of precursors or of ozone, provides information about the lower limit for ozone concentrations that a region can achieve through regulation of local precursors. In this paper, measured oxidant and $\mathrm{NO_x}$ concentrations are analyzed from 14 counties in the state of Utah to calculate the regional and local contributions to ozone for each region. This analysis is used to determine the nature of the atmosphere in each county by identifying whether the region is VOC or $\mathrm{NO_x}$-limited. Furthermore, this analysis is performed for each county for the years 2012 and 2022 to assess changes in the oxidative nature and quantify regional and local contributions to ozone over a 10-year period. All studied counties--except for Washington County--in Utah were found to be VOC-limited in 2012. This shifted in 2022, with most counties being either in a transitional state or $\mathrm{NO_x}$-limited. Local contributions to ozone increased in two major counties, Cache and Salt Lake Counties, but decreased in Carbon, Davis, Duchesne, Uinta, Utah, Washington, and Weber Counties. Generally, the regional contributions to oxidant concentrations decreased across the state. A summertime spike in both regional and local contributions to oxidants was observed. Smoke from wildfires was found to increase regional contributions to oxidants and shift the local regime to be more $\mathrm{NO_x}$-limited.

**Link**: [arxiv](http://arxiv.org/abs/2412.01659v1),  [pdf](http://arxiv.org/pdf/2412.01659v1)

**Tags**: physics.ao-ph 



### Real-time Transformer-based Open-Vocabulary Detection with Efficient   Fusion Head
**Authors**: Tiancheng Zhao, Peng Liu, Xuan He, Lu Zhang, Kyusong Lee

**Updated**: 2024-12-02T11:24:20Z

**Summary**: End-to-end transformer-based detectors (DETRs) have shown exceptional performance in both closed-set and open-vocabulary object detection (OVD) tasks through the integration of language modalities. However, their demanding computational requirements have hindered their practical application in real-time object detection (OD) scenarios. In this paper, we scrutinize the limitations of two leading models in the OVDEval benchmark, OmDet and Grounding-DINO, and introduce OmDet-Turbo. This novel transformer-based real-time OVD model features an innovative Efficient Fusion Head (EFH) module designed to alleviate the bottlenecks observed in OmDet and Grounding-DINO. Notably, OmDet-Turbo-Base achieves a 100.2 frames per second (FPS) with TensorRT and language cache techniques applied. Notably, in zero-shot scenarios on COCO and LVIS datasets, OmDet-Turbo achieves performance levels nearly on par with current state-of-the-art supervised models. Furthermore, it establishes new state-of-the-art benchmarks on ODinW and OVDEval, boasting an AP of 30.1 and an NMS-AP of 26.86, respectively. The practicality of OmDet-Turbo in industrial applications is underscored by its exceptional performance on benchmark datasets and superior inference speed, positioning it as a compelling choice for real-time object detection tasks. Code: \url{https://github.com/om-ai-lab/OmDet}

**Link**: [arxiv](http://arxiv.org/abs/2403.06892v2),  [pdf](http://arxiv.org/pdf/2403.06892v2)

**Tags**: cs.CV cs.CL 



## Keyword: LLM Inference 
 ### HoVLE: Unleashing the Power of Monolithic Vision-Language Models with   Holistic Vision-Language Embedding
**Authors**: Chenxin Tao, Shiqian Su, Xizhou Zhu, Chenyu Zhang, Zhe Chen, Jiawen Liu, Wenhai Wang, Lewei Lu, Gao Huang, Yu Qiao, Jifeng Dai

**Updated**: 2024-12-20T18:59:59Z

**Summary**: The rapid advance of Large Language Models (LLMs) has catalyzed the development of Vision-Language Models (VLMs). Monolithic VLMs, which avoid modality-specific encoders, offer a promising alternative to the compositional ones but face the challenge of inferior performance. Most existing monolithic VLMs require tuning pre-trained LLMs to acquire vision abilities, which may degrade their language capabilities. To address this dilemma, this paper presents a novel high-performance monolithic VLM named HoVLE. We note that LLMs have been shown capable of interpreting images, when image embeddings are aligned with text embeddings. The challenge for current monolithic VLMs actually lies in the lack of a holistic embedding module for both vision and language inputs. Therefore, HoVLE introduces a holistic embedding module that converts visual and textual inputs into a shared space, allowing LLMs to process images in the same way as texts. Furthermore, a multi-stage training strategy is carefully designed to empower the holistic embedding module. It is first trained to distill visual features from a pre-trained vision encoder and text embeddings from the LLM, enabling large-scale training with unpaired random images and text tokens. The whole model further undergoes next-token prediction on multi-modal data to align the embeddings. Finally, an instruction-tuning stage is incorporated. Our experiments show that HoVLE achieves performance close to leading compositional models on various benchmarks, outperforming previous monolithic models by a large margin. Model available at https://huggingface.co/OpenGVLab/HoVLE.

**Link**: [arxiv](http://arxiv.org/abs/2412.16158v1),  [pdf](http://arxiv.org/pdf/2412.16158v1)

**Tags**: cs.CV 



### Can Generative Video Models Help Pose Estimation?
**Authors**: Ruojin Cai, Jason Y. Zhang, Philipp Henzler, Zhengqi Li, Noah Snavely, Ricardo Martin-Brualla

**Updated**: 2024-12-20T18:58:24Z

**Summary**: Pairwise pose estimation from images with little or no overlap is an open challenge in computer vision. Existing methods, even those trained on large-scale datasets, struggle in these scenarios due to the lack of identifiable correspondences or visual overlap. Inspired by the human ability to infer spatial relationships from diverse scenes, we propose a novel approach, InterPose, that leverages the rich priors encoded within pre-trained generative video models. We propose to use a video model to hallucinate intermediate frames between two input images, effectively creating a dense, visual transition, which significantly simplifies the problem of pose estimation. Since current video models can still produce implausible motion or inconsistent geometry, we introduce a self-consistency score that evaluates the consistency of pose predictions from sampled videos. We demonstrate that our approach generalizes among three state-of-the-art video models and show consistent improvements over the state-of-the-art DUSt3R on four diverse datasets encompassing indoor, outdoor, and object-centric scenes. Our findings suggest a promising avenue for improving pose estimation models by leveraging large generative models trained on vast amounts of video data, which is more readily available than 3D data. See our project page for results: https://inter-pose.github.io/.

**Link**: [arxiv](http://arxiv.org/abs/2412.16155v1),  [pdf](http://arxiv.org/pdf/2412.16155v1)

**Tags**: cs.CV 



### The Status of Neutrino Cosmology: Standard $Λ$CDM, Extensions, and   Tensions
**Authors**: Helena García Escudero, Kevork N. Abazajian

**Updated**: 2024-12-20T18:57:40Z

**Summary**: We examine the performance of the six-parameter $\Lambda$CDM model and its extensions in light of recent cosmological observations, with particular focus on neutrino properties inferred from cosmology. Using a broad suite of nine combinations of datasets, with three separate analyses of the Planck Cosmic Microwave Background (CMB) data, and three separate supernovae (SNe) survey data, plus the recent DESI baryon acoustic oscillation (BAO) scale results, we derive constraints on the sum of neutrino masses ($\Sigma m_\nu$). Our results show upper limits in the range of $\Sigma m_\nu < 76.9\,\mathrm{meV}$ to $\Sigma m_\nu < 108\,\mathrm{meV}$ (95\% CL). The variation in the limits on $\Sigma m_\nu$ arises from the separate analyses of the Planck CMB data and the separate supernovae datasets, as they relate to the inferred matter density and its relation to the sensitivity of the BAO scale and CMB lensing to $\Sigma m_\nu$. In the context of hierarchical mass models in $\Lambda$CDM, we find a $1.47\sigma$ preference for normal ordering (NO) over inverted ordering (IO), with similar values of preference across all datasets. Despite the strong constraints, an inclination towards massless neutrinos over NO remains weak at $1.36\sigma$. We find that a ``negative'' neutrino mass, inferred from the shape of the likelihood in the physical regime, $\Sigma m_\nu > 0$, is only present at less than $2\sigma$. We confirm that models allowing extra relativistic degrees of freedom, with $N_{\rm eff} \approx 3.5$, alleviate the Hubble tension. Significantly, we find a $3.3\sigma$ preference for a 0.1 eV partially thermalized sterile neutrino when the SH0ES $H_0$ measurement is included, a scale of interest in short-baseline oscillation experiment results. [abridged]

**Link**: [arxiv](http://arxiv.org/abs/2412.05451v2),  [pdf](http://arxiv.org/pdf/2412.05451v2)

**Tags**: astro-ph.CO hep-ph 



### Offline Reinforcement Learning for LLM Multi-Step Reasoning
**Authors**: Huaijie Wang, Shibo Hao, Hanze Dong, Shenao Zhang, Yilin Bao, Ziran Yang, Yi Wu

**Updated**: 2024-12-20T18:49:45Z

**Summary**: Improving the multi-step reasoning ability of large language models (LLMs) with offline reinforcement learning (RL) is essential for quickly adapting them to complex tasks. While Direct Preference Optimization (DPO) has shown promise in aligning LLMs with human preferences, it is less suitable for multi-step reasoning tasks because (1) DPO relies on paired preference data, which is not readily available for multi-step reasoning tasks, and (2) it treats all tokens uniformly, making it ineffective for credit assignment in multi-step reasoning tasks, which often come with sparse reward. In this work, we propose OREO (Offline Reasoning Optimization), an offline RL method for enhancing LLM multi-step reasoning. Building on insights from previous works of maximum entropy reinforcement learning, it jointly learns a policy model and value function by optimizing the soft Bellman Equation. We show in principle that it reduces the need to collect pairwise data and enables better credit assignment. Empirically, OREO surpasses existing offline learning methods on multi-step reasoning benchmarks, including mathematical reasoning tasks (GSM8K, MATH) and embodied agent control (ALFWorld). The approach can be extended to a multi-iteration framework when additional resources are available. Furthermore, the learned value function can be leveraged to guide the tree search for free, which can further boost performance during test time.

**Link**: [arxiv](http://arxiv.org/abs/2412.16145v1),  [pdf](http://arxiv.org/pdf/2412.16145v1)

**Tags**: cs.LG cs.AI cs.CL 



### Can LLMs Obfuscate Code? A Systematic Analysis of Large Language Models   into Assembly Code Obfuscation
**Authors**: Seyedreza Mohseni, Seyedali Mohammadi, Deepa Tilwani, Yash Saxena, Gerald Ndwula, Sriram Vema, Edward Raff, Manas Gaur

**Updated**: 2024-12-20T18:31:24Z

**Summary**: Malware authors often employ code obfuscations to make their malware harder to detect. Existing tools for generating obfuscated code often require access to the original source code (e.g., C++ or Java), and adding new obfuscations is a non-trivial, labor-intensive process. In this study, we ask the following question: Can Large Language Models (LLMs) potentially generate a new obfuscated assembly code? If so, this poses a risk to anti-virus engines and potentially increases the flexibility of attackers to create new obfuscation patterns. We answer this in the affirmative by developing the MetamorphASM benchmark comprising MetamorphASM Dataset (MAD) along with three code obfuscation techniques: dead code, register substitution, and control flow change. The MetamorphASM systematically evaluates the ability of LLMs to generate and analyze obfuscated code using MAD, which contains 328,200 obfuscated assembly code samples. We release this dataset and analyze the success rate of various LLMs (e.g., GPT-3.5/4, GPT-4o-mini, Starcoder, CodeGemma, CodeLlama, CodeT5, and LLaMA 3.1) in generating obfuscated assembly code. The evaluation was performed using established information-theoretic metrics and manual human review to ensure correctness and provide the foundation for researchers to study and develop remediations to this risk. The source code can be found at the following GitHub link: https://github.com/mohammadi-ali/MetamorphASM.

**Link**: [arxiv](http://arxiv.org/abs/2412.16135v1),  [pdf](http://arxiv.org/pdf/2412.16135v1)

**Tags**: cs.CR cs.AI cs.CL 



### Data-Driven Mechanism Design: Jointly Eliciting Preferences and   Information
**Authors**: Dirk Bergemann, Marek Bojko, Paul Dütting, Renato Paes Leme, Haifeng Xu, Song Zuo

**Updated**: 2024-12-20T18:29:49Z

**Summary**: We study mechanism design when agents hold private information about both their preferences and a common payoff-relevant state. We show that standard message-driven mechanisms cannot implement socially efficient allocations when agents have multidimensional types, even under favorable conditions. To overcome this limitation, we propose data-driven mechanisms that leverage additional post-allocation information, modeled as an estimator of the payoff-relevant state. Our data-driven mechanisms extend the classic Vickrey-Clarke-Groves class. We show that they achieve exact implementation in posterior equilibrium when the state is either fully revealed or the utility is linear in an unbiased estimator. We also show that they achieve approximate implementation with a consistent estimator, converging to exact implementation as the estimator converges, and present bounds on the convergence rate. We demonstrate applications to digital advertising auctions and large language model (LLM)-based mechanisms, where user engagement naturally reveals relevant information.

**Link**: [arxiv](http://arxiv.org/abs/2412.16132v1),  [pdf](http://arxiv.org/pdf/2412.16132v1)

**Tags**: econ.TH cs.GT 



### What is the Role of Small Models in the LLM Era: A Survey
**Authors**: Lihu Chen, Gaël Varoquaux

**Updated**: 2024-12-20T18:11:41Z

**Summary**: Large Language Models (LLMs) have made significant progress in advancing artificial general intelligence (AGI), leading to the development of increasingly large models such as GPT-4 and LLaMA-405B. However, scaling up model sizes results in exponentially higher computational costs and energy consumption, making these models impractical for academic researchers and businesses with limited resources. At the same time, Small Models (SMs) are frequently used in practical settings, although their significance is currently underestimated. This raises important questions about the role of small models in the era of LLMs, a topic that has received limited attention in prior research. In this work, we systematically examine the relationship between LLMs and SMs from two key perspectives: Collaboration and Competition. We hope this survey provides valuable insights for practitioners, fostering a deeper understanding of the contribution of small models and promoting more efficient use of computational resources. The code is available at https://github.com/tigerchen52/role_of_small_models

**Link**: [arxiv](http://arxiv.org/abs/2409.06857v4),  [pdf](http://arxiv.org/pdf/2409.06857v4)

**Tags**: cs.CL 



### PromptOptMe: Error-Aware Prompt Compression for LLM-based MT Evaluation   Metrics
**Authors**: Daniil Larionov, Steffen Eger

**Updated**: 2024-12-20T18:08:02Z

**Summary**: Evaluating the quality of machine-generated natural language content is a challenging task in Natural Language Processing (NLP). Recently, large language models (LLMs) like GPT-4 have been employed for this purpose, but they are computationally expensive due to the extensive token usage required by complex evaluation prompts. In this paper, we propose a prompt optimization approach that uses a smaller, fine-tuned language model to compress input data for evaluation prompt, thus reducing token usage and computational cost when using larger LLMs for downstream evaluation. Our method involves a two-stage fine-tuning process: supervised fine-tuning followed by preference optimization to refine the model's outputs based on human preferences. We focus on Machine Translation (MT) evaluation and utilize the GEMBA-MQM metric as a starting point. Our results show a $2.37\times$ reduction in token usage without any loss in evaluation quality. This work makes state-of-the-art LLM-based metrics like GEMBA-MQM more cost-effective and efficient, enhancing their accessibility for broader use.

**Link**: [arxiv](http://arxiv.org/abs/2412.16120v1),  [pdf](http://arxiv.org/pdf/2412.16120v1)

**Tags**: cs.CL 



### Deciphering the Underserved: Benchmarking LLM OCR for Low-Resource   Scripts
**Authors**: Muhammad Abdullah Sohail, Salaar Masood, Hamza Iqbal

**Updated**: 2024-12-20T18:05:22Z

**Summary**: This study investigates the potential of Large Language Models (LLMs), particularly GPT-4o, for Optical Character Recognition (OCR) in low-resource scripts such as Urdu, Albanian, and Tajik, with English serving as a benchmark. Using a meticulously curated dataset of 2,520 images incorporating controlled variations in text length, font size, background color, and blur, the research simulates diverse real-world challenges. Results emphasize the limitations of zero-shot LLM-based OCR, particularly for linguistically complex scripts, highlighting the need for annotated datasets and fine-tuned models. This work underscores the urgency of addressing accessibility gaps in text digitization, paving the way for inclusive and robust OCR solutions for underserved languages.

**Link**: [arxiv](http://arxiv.org/abs/2412.16119v1),  [pdf](http://arxiv.org/pdf/2412.16119v1)

**Tags**: cs.LG cs.CV eess.IV 



### Trust Dynamics and Market Behavior in Cryptocurrency: A Comparative   Study of Centralized and Decentralized Exchanges
**Authors**: Xintong Wu, Wanlin Deng, Yutong Quan, Luyao Zhang

**Updated**: 2024-12-20T18:03:21Z

**Summary**: In the rapidly evolving cryptocurrency landscape, trust is a critical yet underexplored factor shaping market behaviors and driving user preferences between centralized exchanges (CEXs) and decentralized exchanges (DEXs). Despite its importance, trust remains challenging to measure, limiting the study of its effects on market dynamics. The collapse of FTX, a major CEX, provides a unique natural experiment to examine the measurable impacts of trust and its sudden erosion on the cryptocurrency ecosystem. This pivotal event raised questions about the resilience of centralized trust systems and accelerated shifts toward decentralized alternatives. This research investigates the impacts of the FTX collapse on user trust, focusing on token valuation, trading flows, and sentiment dynamics. Employing causal inference methods, including Regression Discontinuity Design (RDD) and Difference-in-Differences (DID), we reveal significant declines in WETH prices and NetFlow from CEXs to DEXs, signaling a measurable transfer of trust. Additionally, natural language processing methods, including topic modeling and sentiment analysis, uncover the complexities of user responses, highlighting shifts from functional discussions to emotional fragmentation in Binance's community, while Uniswap's sentiment exhibits a gradual upward trend. Despite data limitations and external influences, the findings underscore the intricate interplay between trust, sentiment, and market behavior in the cryptocurrency ecosystem. By bridging blockchain analytics, behavioral finance, and decentralized finance (DeFi), this study contributes to interdisciplinary research, offering a deeper understanding of distributed trust mechanisms and providing critical insights for future investigations into the socio-technical dimensions of trust in digital economies.

**Link**: [arxiv](http://arxiv.org/abs/2404.17227v2),  [pdf](http://arxiv.org/pdf/2404.17227v2)

**Tags**: econ.GN cs.CE cs.CR cs.CY q-fin.EC q-fin.RM 



### PruneVid: Visual Token Pruning for Efficient Video Large Language Models
**Authors**: Xiaohu Huang, Hao Zhou, Kai Han

**Updated**: 2024-12-20T18:01:58Z

**Summary**: In this paper, we introduce PruneVid, a visual token pruning method designed to enhance the efficiency of multi-modal video understanding. Large Language Models (LLMs) have shown promising performance in video tasks due to their extended capabilities in comprehending visual modalities. However, the substantial redundancy in video data presents significant computational challenges for LLMs. To address this issue, we introduce a training-free method that 1) minimizes video redundancy by merging spatial-temporal tokens, and 2) leverages LLMs' reasoning capabilities to selectively prune visual features relevant to question tokens, enhancing model efficiency. We validate our method across multiple video benchmarks, which demonstrate that PruneVid can prune over 80% of tokens while maintaining competitive performance combined with different model networks. This highlights its superior effectiveness and efficiency compared to existing pruning methods. Code: https://github.com/Visual-AI/PruneVid.

**Link**: [arxiv](http://arxiv.org/abs/2412.16117v1),  [pdf](http://arxiv.org/pdf/2412.16117v1)

**Tags**: cs.CV 



### CLEAR: Conv-Like Linearization Revs Pre-Trained Diffusion Transformers   Up
**Authors**: Songhua Liu, Zhenxiong Tan, Xinchao Wang

**Updated**: 2024-12-20T17:57:09Z

**Summary**: Diffusion Transformers (DiT) have become a leading architecture in image generation. However, the quadratic complexity of attention mechanisms, which are responsible for modeling token-wise relationships, results in significant latency when generating high-resolution images. To address this issue, we aim at a linear attention mechanism in this paper that reduces the complexity of pre-trained DiTs to linear. We begin our exploration with a comprehensive summary of existing efficient attention mechanisms and identify four key factors crucial for successful linearization of pre-trained DiTs: locality, formulation consistency, high-rank attention maps, and feature integrity. Based on these insights, we introduce a convolution-like local attention strategy termed CLEAR, which limits feature interactions to a local window around each query token, and thus achieves linear complexity. Our experiments indicate that, by fine-tuning the attention layer on merely 10K self-generated samples for 10K iterations, we can effectively transfer knowledge from a pre-trained DiT to a student model with linear complexity, yielding results comparable to the teacher model. Simultaneously, it reduces attention computations by 99.5% and accelerates generation by 6.3 times for generating 8K-resolution images. Furthermore, we investigate favorable properties in the distilled attention layers, such as zero-shot generalization cross various models and plugins, and improved support for multi-GPU parallel inference. Models and codes are available here: https://github.com/Huage001/CLEAR.

**Link**: [arxiv](http://arxiv.org/abs/2412.16112v1),  [pdf](http://arxiv.org/pdf/2412.16112v1)

**Tags**: cs.CV 



### Text Understanding in GPT-4 vs Humans
**Authors**: Thomas R. Shultz, Jamie M. Wise, Ardavan Salehi Nobandegani

**Updated**: 2024-12-20T17:50:38Z

**Summary**: We examine whether a leading AI system GPT4 understands text as well as humans do, first using a well-established standardized test of discourse comprehension. On this test, GPT4 performs slightly, but not statistically significantly, better than humans given the very high level of human performance. Both GPT4 and humans make correct inferences about information that is not explicitly stated in the text, a critical test of understanding. Next, we use more difficult passages to determine whether that could allow larger differences between GPT4 and humans. GPT4 does considerably better on this more difficult text than do the high school and university students for whom these the text passages are designed, as admission tests of student reading comprehension. Deeper exploration of GPT4 performance on material from one of these admission tests reveals generally accepted signatures of genuine understanding, namely generalization and inference.

**Link**: [arxiv](http://arxiv.org/abs/2403.17196v3),  [pdf](http://arxiv.org/pdf/2403.17196v3)

**Tags**: cs.CL 



### Logical Consistency of Large Language Models in Fact-checking
**Authors**: Bishwamittra Ghosh, Sarah Hasan, Naheed Anjum Arafat, Arijit Khan

**Updated**: 2024-12-20T17:42:25Z

**Summary**: In recent years, large language models (LLMs) have demonstrated significant success in performing varied natural language tasks such as language translation, question-answering, summarizing, fact-checking, etc. Despite LLMs' impressive ability to generate human-like texts, LLMs are infamous for their inconsistent responses -- a meaning-preserving change in the input query results in an inconsistent response and attributes to vulnerabilities of LLMs such as hallucination, jailbreaking, etc. Consequently, existing research focuses on simple paraphrasing-based consistency assessment of LLMs, and ignores complex queries that necessitates an even better understanding of logical reasoning by an LLM. Our work therefore addresses the logical inconsistency of LLMs under complex logical queries with primitive logical operators, e.g., negation, conjunction, and disjunction. As a test bed, we consider retrieval-augmented LLMs on a fact-checking task involving propositional logic queries from real-world knowledge graphs (KGs). Our contributions are three-fold. Benchmark: We introduce three logical fact-checking datasets over KGs for community development towards logically consistent LLMs. Assessment: We propose consistency measures of LLMs on propositional logic queries as input and demonstrate that existing LLMs lack logical consistency, specially on complex queries. Improvement: We employ supervised fine-tuning to improve the logical consistency of LLMs on the complex fact-checking task with KG contexts.

**Link**: [arxiv](http://arxiv.org/abs/2412.16100v1),  [pdf](http://arxiv.org/pdf/2412.16100v1)

**Tags**: cs.CL 



### The Evolution of LLM Adoption in Industry Data Curation Practices
**Authors**: Crystal Qian, Michael Xieyang Liu, Emily Reif, Grady Simon, Nada Hussein, Nathan Clement, James Wexler, Carrie J. Cai, Michael Terry, Minsuk Kahng

**Updated**: 2024-12-20T17:34:16Z

**Summary**: As large language models (LLMs) grow increasingly adept at processing unstructured text data, they offer new opportunities to enhance data curation workflows. This paper explores the evolution of LLM adoption among practitioners at a large technology company, evaluating the impact of LLMs in data curation tasks through participants' perceptions, integration strategies, and reported usage scenarios. Through a series of surveys, interviews, and user studies, we provide a timely snapshot of how organizations are navigating a pivotal moment in LLM evolution. In Q2 2023, we conducted a survey to assess LLM adoption in industry for development tasks (N=84), and facilitated expert interviews to assess evolving data needs (N=10) in Q3 2023. In Q2 2024, we explored practitioners' current and anticipated LLM usage through a user study involving two LLM-based prototypes (N=12). While each study addressed distinct research goals, they revealed a broader narrative about evolving LLM usage in aggregate. We discovered an emerging shift in data understanding from heuristic-first, bottom-up approaches to insights-first, top-down workflows supported by LLMs. Furthermore, to respond to a more complex data landscape, data practitioners now supplement traditional subject-expert-created 'golden datasets' with LLM-generated 'silver' datasets and rigorously validated 'super golden' datasets curated by diverse experts. This research sheds light on the transformative role of LLMs in large-scale analysis of unstructured data and highlights opportunities for further tool development.

**Link**: [arxiv](http://arxiv.org/abs/2412.16089v1),  [pdf](http://arxiv.org/pdf/2412.16089v1)

**Tags**: cs.HC cs.AI 



### Towards Interpretable Radiology Report Generation via Concept   Bottlenecks using a Multi-Agentic RAG
**Authors**: Hasan Md Tusfiqur Alam, Devansh Srivastav, Md Abdul Kadir, Daniel Sonntag

**Updated**: 2024-12-20T17:33:50Z

**Summary**: Deep learning has advanced medical image classification, but interpretability challenges hinder its clinical adoption. This study enhances interpretability in Chest X-ray (CXR) classification by using concept bottleneck models (CBMs) and a multi-agent Retrieval-Augmented Generation (RAG) system for report generation. By modeling relationships between visual features and clinical concepts, we create interpretable concept vectors that guide a multi-agent RAG system to generate radiology reports, enhancing clinical relevance, explainability, and transparency. Evaluation of the generated reports using an LLM-as-a-judge confirmed the interpretability and clinical utility of our model's outputs. On the COVID-QU dataset, our model achieved 81% classification accuracy and demonstrated robust report generation performance, with five key metrics ranging between 84% and 90%. This interpretable multi-agent framework bridges the gap between high-performance AI and the explainability required for reliable AI-driven CXR analysis in clinical settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.16086v1),  [pdf](http://arxiv.org/pdf/2412.16086v1)

**Tags**: cs.IR cs.AI cs.CL cs.CV eess.IV 



### Efficient MedSAMs: Segment Anything in Medical Images on Laptop
**Authors**: Jun Ma, Feifei Li, Sumin Kim, Reza Asakereh, Bao-Hiep Le, Dang-Khoa Nguyen-Vu, Alexander Pfefferle, Muxin Wei, Ruochen Gao, Donghang Lyu, Songxiao Yang, Lennart Purucker, Zdravko Marinov, Marius Staring, Haisheng Lu, Thuy Thanh Dao, Xincheng Ye, Zhi Li, Gianluca Brugnara, Philipp Vollmuth, Martha Foltyn-Dumitru, Jaeyoung Cho, Mustafa Ahmed Mahmutoglu, Martin Bendszus, Irada Pflüger, Aditya Rastogi, Dong Ni, Xin Yang, Guang-Quan Zhou, Kaini Wang, Nicholas Heller, Nikolaos Papanikolopoulos, Christopher Weight, Yubing Tong, Jayaram K Udupa, Cahill J. Patrick, Yaqi Wang, Yifan Zhang, Francisco Contijoch, Elliot McVeigh, Xin Ye, Shucheng He, Robert Haase, Thomas Pinetz, Alexander Radbruch, Inga Krause, Erich Kobler, Jian He, Yucheng Tang, Haichun Yang, Yuankai Huo, Gongning Luo, Kaisar Kushibar, Jandos Amankulov, Dias Toleshbayev, Amangeldi Mukhamejan, Jan Egger, Antonio Pepe, Christina Gsaxner, Gijs Luijten, Shohei Fujita, Tomohiro Kikuchi, Benedikt Wiestler, Jan S. Kirschke, Ezequiel de la Rosa, Federico Bolelli, Luca Lumetti, Costantino Grana, Kunpeng Xie, Guomin Wu, Behrus Puladi, Carlos Martín-Isla, Karim Lekadir, Victor M. Campello, Wei Shao, Wayne Brisbane, Hongxu Jiang, Hao Wei, Wu Yuan, Shuangle Li, Yuyin Zhou, Bo Wang

**Updated**: 2024-12-20T17:33:35Z

**Summary**: Promptable segmentation foundation models have emerged as a transformative approach to addressing the diverse needs in medical images, but most existing models require expensive computing, posing a big barrier to their adoption in clinical practice. In this work, we organized the first international competition dedicated to promptable medical image segmentation, featuring a large-scale dataset spanning nine common imaging modalities from over 20 different institutions. The top teams developed lightweight segmentation foundation models and implemented an efficient inference pipeline that substantially reduced computational requirements while maintaining state-of-the-art segmentation accuracy. Moreover, the post-challenge phase advanced the algorithms through the design of performance booster and reproducibility tasks, resulting in improved algorithms and validated reproducibility of the winning solution. Furthermore, the best-performing algorithms have been incorporated into the open-source software with a user-friendly interface to facilitate clinical adoption. The data and code are publicly available to foster the further development of medical image segmentation foundation models and pave the way for impactful real-world applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.16085v1),  [pdf](http://arxiv.org/pdf/2412.16085v1)

**Tags**: eess.IV cs.CV 



### VaulTor: Putting the TEE in Tor
**Authors**: Humza Ikram, Rumaisa Habib, Muaz Ali, Zartash Afzal Uzmi

**Updated**: 2024-12-20T17:06:55Z

**Summary**: Online services that desire to operate anonymously routinely host themselves as 'Hidden Services' in the Tor network. However, these services are frequently threatened by deanonymization attacks, whereby their IP address and location may be inferred by the authorities. We present VaulTor, a novel architecture for the Tor network to ensure an extra layer of security for the Hidden Services against deanonymization attacks. In this new architecture, a volunteer (vault) is incentivized to host the web application content on behalf of the Hidden Service. The vault runs the hosted application in a Trusted Execution Environment (TEE) and becomes the point of contact for interested clients. This setup can substantially reduce the uptime requirement of the original Hidden Service provider and hence significantly decrease the chance of deanonymization attacks against them. We also show that the VaulTor architecture does not cause any noticeable performance degradation in accessing the hosted content (the performance degradation ranges from 2.6-5.5%).

**Link**: [arxiv](http://arxiv.org/abs/2412.16064v1),  [pdf](http://arxiv.org/pdf/2412.16064v1)

**Tags**: cs.CR cs.NI 



### SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer
**Authors**: Hao Chen, Ze Wang, Xiang Li, Ximeng Sun, Fangyi Chen, Jiang Liu, Jindong Wang, Bhiksha Raj, Zicheng Liu, Emad Barsoum

**Updated**: 2024-12-20T16:59:40Z

**Summary**: Efficient image tokenization with high compression ratios remains a critical challenge for training generative models. We present SoftVQ-VAE, a continuous image tokenizer that leverages soft categorical posteriors to aggregate multiple codewords into each latent token, substantially increasing the representation capacity of the latent space. When applied to Transformer-based architectures, our approach compresses 256x256 and 512x512 images using as few as 32 or 64 1-dimensional tokens. Not only does SoftVQ-VAE show consistent and high-quality reconstruction, more importantly, it also achieves state-of-the-art and significantly faster image generation results across different denoising-based generative models. Remarkably, SoftVQ-VAE improves inference throughput by up to 18x for generating 256x256 images and 55x for 512x512 images while achieving competitive FID scores of 1.78 and 2.21 for SiT-XL. It also improves the training efficiency of the generative models by reducing the number of training iterations by 2.3x while maintaining comparable performance. With its fully-differentiable design and semantic-rich latent space, our experiment demonstrates that SoftVQ-VAE achieves efficient tokenization without compromising generation quality, paving the way for more efficient generative models. Code and model are released.

**Link**: [arxiv](http://arxiv.org/abs/2412.10958v2),  [pdf](http://arxiv.org/pdf/2412.10958v2)

**Tags**: cs.CV cs.AI cs.LG 



### Segmentation of arbitrary features in very high resolution remote   sensing imagery
**Authors**: Henry Cording, Yves Plancherel, Pablo Brito-Parada

**Updated**: 2024-12-20T16:48:52Z

**Summary**: Very high resolution (VHR) mapping through remote sensing (RS) imagery presents a new opportunity to inform decision-making and sustainable practices in countless domains. Efficient processing of big VHR data requires automated tools applicable to numerous geographic regions and features. Contemporary RS studies address this challenge by employing deep learning (DL) models for specific datasets or features, which limits their applicability across contexts.   The present research aims to overcome this limitation by introducing EcoMapper, a scalable solution to segment arbitrary features in VHR RS imagery. EcoMapper fully automates processing of geospatial data, DL model training, and inference. Models trained with EcoMapper successfully segmented two distinct features in a real-world UAV dataset, achieving scores competitive with prior studies which employed context-specific models.   To evaluate EcoMapper, many additional models were trained on permutations of principal field survey characteristics (FSCs). A relationship was discovered allowing derivation of optimal ground sampling distance from feature size, termed Cording Index (CI). A comprehensive methodology for field surveys was developed to ensure DL methods can be applied effectively to collected data.   The EcoMapper code accompanying this work is available at https://github.com/hcording/ecomapper .

**Link**: [arxiv](http://arxiv.org/abs/2412.16046v1),  [pdf](http://arxiv.org/pdf/2412.16046v1)

**Tags**: cs.CV 



### Magnetic Preference Optimization: Achieving Last-iterate Convergence for   Language Model Alignment
**Authors**: Mingzhi Wang, Chengdong Ma, Qizhi Chen, Linjian Meng, Yang Han, Jiancong Xiao, Zhaowei Zhang, Jing Huo, Weijie J. Su, Yaodong Yang

**Updated**: 2024-12-20T16:26:58Z

**Summary**: Self-play methods have demonstrated remarkable success in enhancing model capabilities across various domains. In the context of Reinforcement Learning from Human Feedback (RLHF), self-play not only boosts Large Language Model (LLM) performance but also overcomes the limitations of traditional Bradley-Terry (BT) model assumptions by finding the Nash equilibrium (NE) of a preference-based, two-player constant-sum game. However, existing methods either guarantee only average-iterate convergence, incurring high storage and inference costs, or converge to the NE of a regularized game, failing to accurately reflect true human preferences. In this paper, we introduce Magnetic Preference Optimization (MPO), a novel approach capable of achieving last-iterate convergence to the NE of the original game, effectively overcoming the limitations of existing methods. Building upon Magnetic Mirror Descent (MMD), MPO attains a linear convergence rate, making it particularly suitable for fine-tuning LLMs. To ensure our algorithm is both theoretically sound and practically viable, we present a simple yet effective implementation that adapts the theoretical insights to the RLHF setting. Empirical results demonstrate that MPO can significantly enhance the performance of LLMs, highlighting the potential of self-play methods in alignment.

**Link**: [arxiv](http://arxiv.org/abs/2410.16714v2),  [pdf](http://arxiv.org/pdf/2410.16714v2)

**Tags**: cs.CL 



### Language Models Resist Alignment: Evidence From Data Compression
**Authors**: Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Josef Dai, Yunhuai Liu, Yaodong Yang

**Updated**: 2024-12-20T16:25:12Z

**Summary**: Large language models (LLMs) may exhibit unintended or undesirable behaviors. Recent works have concentrated on aligning LLMs to mitigate harmful outputs. Despite these efforts, some anomalies indicate that even a well-conducted alignment process can be easily circumvented, whether intentionally or accidentally. Does alignment fine-tuning yield have robust effects on models, or are its impacts merely superficial? In this work, we make the first exploration of this phenomenon from both theoretical and empirical perspectives. Empirically, we demonstrate the elasticity of post-alignment models, i.e., the tendency to revert to the behavior distribution formed during the pre-training phase upon further fine-tuning. Leveraging compression theory, we formally deduce that fine-tuning disproportionately undermines alignment relative to pre-training, potentially by orders of magnitude. We validate the presence of elasticity through experiments on models of varying types and scales. Specifically, we find that model performance declines rapidly before reverting to the pre-training distribution, after which the rate of decline drops significantly. Furthermore, we further reveal that elasticity positively correlates with the increased model size and the expansion of pre-training data. Our findings underscore the need to address the inherent elasticity of LLMs to mitigate their resistance to alignment.

**Link**: [arxiv](http://arxiv.org/abs/2406.06144v3),  [pdf](http://arxiv.org/pdf/2406.06144v3)

**Tags**: cs.CL cs.AI 



### BMRS: Bayesian Model Reduction for Structured Pruning
**Authors**: Dustin Wright, Christian Igel, Raghavendra Selvan

**Updated**: 2024-12-20T16:18:13Z

**Summary**: Modern neural networks are often massively overparameterized leading to high compute costs during training and at inference. One effective method to improve both the compute and energy efficiency of neural networks while maintaining good performance is structured pruning, where full network structures (e.g.~neurons or convolutional filters) that have limited impact on the model output are removed. In this work, we propose Bayesian Model Reduction for Structured pruning (BMRS), a fully end-to-end Bayesian method of structured pruning. BMRS is based on two recent methods: Bayesian structured pruning with multiplicative noise, and Bayesian model reduction (BMR), a method which allows efficient comparison of Bayesian models under a change in prior. We present two realizations of BMRS derived from different priors which yield different structured pruning characteristics: 1) BMRS_N with the truncated log-normal prior, which offers reliable compression rates and accuracy without the need for tuning any thresholds and 2) BMRS_U with the truncated log-uniform prior that can achieve more aggressive compression based on the boundaries of truncation. Overall, we find that BMRS offers a theoretically grounded approach to structured pruning of neural networks yielding both high compression rates and accuracy. Experiments on multiple datasets and neural networks of varying complexity showed that the two BMRS methods offer a competitive performance-efficiency trade-off compared to other pruning methods.

**Link**: [arxiv](http://arxiv.org/abs/2406.01345v2),  [pdf](http://arxiv.org/pdf/2406.01345v2)

**Tags**: cs.LG stat.ML 



### The Only Way is Ethics: A Guide to Ethical Research with Large Language   Models
**Authors**: Eddie L. Ungless, Nikolas Vitsakis, Zeerak Talat, James Garforth, Björn Ross, Arno Onken, Atoosa Kasirzadeh, Alexandra Birch

**Updated**: 2024-12-20T16:14:43Z

**Summary**: There is a significant body of work looking at the ethical considerations of large language models (LLMs): critiquing tools to measure performance and harms; proposing toolkits to aid in ideation; discussing the risks to workers; considering legislation around privacy and security etc. As yet there is no work that integrates these resources into a single practical guide that focuses on LLMs; we attempt this ambitious goal. We introduce 'LLM Ethics Whitepaper', which we provide as an open and living resource for NLP practitioners, and those tasked with evaluating the ethical implications of others' work. Our goal is to translate ethics literature into concrete recommendations and provocations for thinking with clear first steps, aimed at computer scientists. 'LLM Ethics Whitepaper' distils a thorough literature review into clear Do's and Don'ts, which we present also in this paper. We likewise identify useful toolkits to support ethical work. We refer the interested reader to the full LLM Ethics Whitepaper, which provides a succinct discussion of ethical considerations at each stage in a project lifecycle, as well as citations for the hundreds of papers from which we drew our recommendations. The present paper can be thought of as a pocket guide to conducting ethical research with LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.16022v1),  [pdf](http://arxiv.org/pdf/2412.16022v1)

**Tags**: cs.CL cs.AI 



### All-in-One Tuning and Structural Pruning for Domain-Specific LLMs
**Authors**: Lei Lu, Zhepeng Wang, Runxue Bao, Mengbing Wang, Fangyi Li, Yawen Wu, Weiwen Jiang, Jie Xu, Yanzhi Wang, Shangqian Gao

**Updated**: 2024-12-20T15:57:10Z

**Summary**: Existing pruning techniques for large language models (LLMs) targeting domain-specific applications typically follow a two-stage process: pruning the pretrained general-purpose LLMs and then fine-tuning the pruned LLMs on specific domains. However, the pruning decisions, derived from the pretrained weights, remain unchanged during fine-tuning, even if the weights have been updated. Therefore, such a combination of the pruning decisions and the finetuned weights may be suboptimal, leading to non-negligible performance degradation. To address these limitations, we propose ATP: All-in-One Tuning and Structural Pruning, a unified one-stage structural pruning and fine-tuning approach that dynamically identifies the current optimal substructure throughout the fine-tuning phase via a trainable pruning decision generator. Moreover, given the limited available data for domain-specific applications, Low-Rank Adaptation (LoRA) becomes a common technique to fine-tune the LLMs. In ATP, we introduce LoRA-aware forward and sparsity regularization to ensure that the substructures corresponding to the learned pruning decisions can be directly removed after the ATP process. ATP outperforms the state-of-the-art two-stage pruning methods on tasks in the legal and healthcare domains. More specifically, ATP recovers up to 88% and 91% performance of the dense model when pruning 40% parameters of LLaMA2-7B and LLaMA3-8B models, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2412.14426v2),  [pdf](http://arxiv.org/pdf/2412.14426v2)

**Tags**: cs.CL cs.AI 



### Fearful Falcons and Angry Llamas: Emotion Category Annotations of   Arguments by Humans and LLMs
**Authors**: Lynn Greschner, Roman Klinger

**Updated**: 2024-12-20T15:41:47Z

**Summary**: Arguments evoke emotions, influencing the effect of the argument itself. Not only the emotional intensity but also the category influence the argument's effects, for instance, the willingness to adapt stances. While binary emotionality has been studied in arguments, there is no work on discrete emotion categories (e.g., "Anger") in such data. To fill this gap, we crowdsource subjective annotations of emotion categories in a German argument corpus and evaluate automatic LLM-based labeling methods. Specifically, we compare three prompting strategies (zero-shot, one-shot, chain-of-thought) on three large instruction-tuned language models (Falcon-7b-instruct, Llama-3.1-8B-instruct, GPT-4o-mini). We further vary the definition of the output space to be binary (is there emotionality in the argument?), closed-domain (which emotion from a given label set is in the argument?), or open-domain (which emotion is in the argument?). We find that emotion categories enhance the prediction of emotionality in arguments, emphasizing the need for discrete emotion annotations in arguments. Across all prompt settings and models, automatic predictions show a high recall but low precision for predicting anger and fear, indicating a strong bias toward negative emotions.

**Link**: [arxiv](http://arxiv.org/abs/2412.15993v1),  [pdf](http://arxiv.org/pdf/2412.15993v1)

**Tags**: cs.CL 



### Improving Factuality in Large Language Models via Decoding-Time   Hallucinatory and Truthful Comparators
**Authors**: Dingkang Yang, Dongling Xiao, Jinjie Wei, Mingcheng Li, Zhaoyu Chen, Ke Li, Lihua Zhang

**Updated**: 2024-12-20T15:26:33Z

**Summary**: Despite their remarkable capabilities, Large Language Models (LLMs) are prone to generate responses that contradict verifiable facts, i.e., unfaithful hallucination content. Existing efforts generally focus on optimizing model parameters or editing semantic representations, which compromise the internal factual knowledge of target LLMs. In addition, hallucinations typically exhibit multifaceted patterns in downstream tasks, limiting the model's holistic performance across tasks. In this paper, we propose a Comparator-driven Decoding-Time (CDT) framework to alleviate the response hallucination. Firstly, we construct hallucinatory and truthful comparators with multi-task fine-tuning samples. In this case, we present an instruction prototype-guided mixture of experts strategy to enhance the ability of the corresponding comparators to capture different hallucination or truthfulness patterns in distinct task instructions. CDT constrains next-token predictions to factuality-robust distributions by contrasting the logit differences between the target LLMs and these comparators. Systematic experiments on multiple downstream tasks show that our framework can significantly improve the model performance and response factuality.

**Link**: [arxiv](http://arxiv.org/abs/2408.12325v4),  [pdf](http://arxiv.org/pdf/2408.12325v4)

**Tags**: cs.CL 



### Never Reset Again: A Mathematical Framework for Continual Inference in   Recurrent Neural Networks
**Authors**: Bojian Yin, Federico Corradi

**Updated**: 2024-12-20T15:24:28Z

**Summary**: Recurrent Neural Networks (RNNs) are widely used for sequential processing but face fundamental limitations with continual inference due to state saturation, requiring disruptive hidden state resets. However, reset-based methods impose synchronization requirements with input boundaries and increase computational costs at inference. To address this, we propose an adaptive loss function that eliminates the need for resets during inference while preserving high accuracy over extended sequences. By combining cross-entropy and Kullback-Leibler divergence, the loss dynamically modulates the gradient based on input informativeness, allowing the network to differentiate meaningful data from noise and maintain stable representations over time. Experimental results demonstrate that our reset-free approach outperforms traditional reset-based methods when applied to a variety of RNNs, particularly in continual tasks, enhancing both the theoretical and practical capabilities of RNNs for streaming applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.15983v1),  [pdf](http://arxiv.org/pdf/2412.15983v1)

**Tags**: cs.LG cs.AI 



### Legommenders: A Comprehensive Content-Based Recommendation Library with   LLM Support
**Authors**: Qijiong Liu, Lu Fan, Xiao-Ming Wu

**Updated**: 2024-12-20T15:18:02Z

**Summary**: We present Legommenders, a unique library designed for content-based recommendation that enables the joint training of content encoders alongside behavior and interaction modules, thereby facilitating the seamless integration of content understanding directly into the recommendation pipeline. Legommenders allows researchers to effortlessly create and analyze over 1,000 distinct models across 15 diverse datasets. Further, it supports the incorporation of contemporary large language models, both as feature encoder and data generator, offering a robust platform for developing state-of-the-art recommendation models and enabling more personalized and effective content delivery.

**Link**: [arxiv](http://arxiv.org/abs/2412.15973v1),  [pdf](http://arxiv.org/pdf/2412.15973v1)

**Tags**: cs.IR 



### Recent Advances in Named Entity Recognition: A Comprehensive Survey and   Comparative Study
**Authors**: Imed Keraghel, Stanislas Morbieu, Mohamed Nadif

**Updated**: 2024-12-20T15:11:13Z

**Summary**: Named Entity Recognition seeks to extract substrings within a text that name real-world objects and to determine their type (for example, whether they refer to persons or organizations). In this survey, we first present an overview of recent popular approaches, including advancements in Transformer-based methods and Large Language Models (LLMs) that have not had much coverage in other surveys. In addition, we discuss reinforcement learning and graph-based approaches, highlighting their role in enhancing NER performance. Second, we focus on methods designed for datasets with scarce annotations. Third, we evaluate the performance of the main NER implementations on a variety of datasets with differing characteristics (as regards their domain, their size, and their number of classes). We thus provide a deep comparison of algorithms that have never been considered together. Our experiments shed some light on how the characteristics of datasets affect the behavior of the methods we compare.

**Link**: [arxiv](http://arxiv.org/abs/2401.10825v3),  [pdf](http://arxiv.org/pdf/2401.10825v3)

**Tags**: cs.CL cs.LG 68T50, 68Q32 



### ChinaTravel: A Real-World Benchmark for Language Agents in Chinese   Travel Planning
**Authors**: Jie-Jing Shao, Xiao-Wen Yang, Bo-Wen Zhang, Baizhi Chen, Wen-Da Wei, Guohao Cai, Zhenhua Dong, Lan-Zhe Guo, Yu-feng Li

**Updated**: 2024-12-20T15:08:25Z

**Summary**: Recent advances in LLMs, particularly in language reasoning and tool integration, have rapidly sparked the real-world development of Language Agents. Among these, travel planning represents a prominent domain, combining academic challenges with practical value due to its complexity and market demand. However, existing benchmarks fail to reflect the diverse, real-world requirements crucial for deployment. To address this gap, we introduce ChinaTravel, a benchmark specifically designed for authentic Chinese travel planning scenarios. We collect the travel requirements from questionnaires and propose a compositionally generalizable domain-specific language that enables a scalable evaluation process, covering feasibility, constraint satisfaction, and preference comparison. Empirical studies reveal the potential of neuro-symbolic agents in travel planning, achieving a constraint satisfaction rate of 27.9%, significantly surpassing purely neural models at 2.6%. Moreover, we identify key challenges in real-world travel planning deployments, including open language reasoning and unseen concept composition. These findings highlight the significance of ChinaTravel as a pivotal milestone for advancing language agents in complex, real-world planning scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2412.13682v2),  [pdf](http://arxiv.org/pdf/2412.13682v2)

**Tags**: cs.AI cs.CL 



### Language Repository for Long Video Understanding
**Authors**: Kumara Kahatapitiya, Kanchana Ranasinghe, Jongwoo Park, Michael S. Ryoo

**Updated**: 2024-12-20T15:06:14Z

**Summary**: Language has become a prominent modality in computer vision with the rise of LLMs. Despite supporting long context-lengths, their effectiveness in handling long-term information gradually declines with input length. This becomes critical, especially in applications such as long-form video understanding. In this paper, we introduce a Language Repository (LangRepo) for LLMs, that maintains concise and structured information as an interpretable (i.e., all-textual) representation. Our repository is updated iteratively based on multi-scale video chunks. We introduce write and read operations that focus on pruning redundancies in text, and extracting information at various temporal scales. The proposed framework is evaluated on zero-shot visual question-answering benchmarks including EgoSchema, NExT-QA, IntentQA and NExT-GQA, showing state-of-the-art performance at its scale. Our code is available at https://github.com/kkahatapitiya/LangRepo.

**Link**: [arxiv](http://arxiv.org/abs/2403.14622v2),  [pdf](http://arxiv.org/pdf/2403.14622v2)

**Tags**: cs.CV 



### FullStack Bench: Evaluating LLMs as Full Stack Coders
**Authors**: Bytedance-Seed-Foundation-Code-Team, :, Yao Cheng, Jianfeng Chen, Jie Chen, Li Chen, Liyu Chen, Wentao Chen, Zhengyu Chen, Shijie Geng, Aoyan Li, Bo Li, Bowen Li, Linyi Li, Boyi Liu, Jerry Liu, Kaibo Liu, Qi Liu, Shukai Liu, Siyao Liu, Tianyi Liu, Tingkai Liu, Yongfei Liu, Rui Long, Jing Mai, Guanghan Ning, Z. Y. Peng, Kai Shen, Jiahao Su, Jing Su, Tao Sun, Yifan Sun, Yunzhe Tao, Guoyin Wang, Siwei Wang, Xuwu Wang, Yite Wang, Zihan Wang, Jinxiang Xia, Liang Xiang, Xia Xiao, Yongsheng Xiao, Chenguang Xi, Shulin Xin, Jingjing Xu, Shikun Xu, Hongxia Yang, Jack Yang, Yingxiang Yang, Jianbo Yuan, Jun Zhang, Yufeng Zhang, Yuyu Zhang, Shen Zheng, He Zhu, Ming Zhu

**Updated**: 2024-12-20T14:58:59Z

**Summary**: As the capabilities of code large language models (LLMs) continue to expand, their applications across diverse code intelligence domains are rapidly increasing. However, most existing datasets only evaluate limited application domains. To address this gap, we have developed a comprehensive code evaluation dataset FullStack Bench focusing on full-stack programming, which encompasses a wide range of application domains (e.g., basic programming, data analysis, software engineering, mathematics, and machine learning). Besides, to assess multilingual programming capabilities, in FullStack Bench, we design real-world instructions and corresponding unit test cases from 16 widely-used programming languages to reflect real-world usage scenarios rather than simple translations. Moreover, we also release an effective code sandbox execution tool (i.e., SandboxFusion) supporting various programming languages and packages to evaluate the performance of our FullStack Bench efficiently. Comprehensive experimental results on our FullStack Bench demonstrate the necessity and effectiveness of our FullStack Bench and SandboxFusion.

**Link**: [arxiv](http://arxiv.org/abs/2412.00535v5),  [pdf](http://arxiv.org/pdf/2412.00535v5)

**Tags**: cs.AI cs.SE 



### Scientific Realism vs. Anti-Realism: Toward a Common Ground
**Authors**: Hanti Lin

**Updated**: 2024-12-20T14:55:54Z

**Summary**: The debate between scientific realism and anti-realism remains at a stalemate, making reconciliation seem hopeless. Yet, important work remains: exploring a common ground, even if only to uncover deeper points of disagreement and, ideally, to benefit both sides of the debate. I propose such a common ground. Specifically, many anti-realists, such as instrumentalists, have yet to seriously engage with Sober's call to justify their preferred version of Ockham's razor through a positive account. Meanwhile, realists face a similar challenge: providing a non-circular explanation of how their version of Ockham's razor connects to truth. The common ground I propose addresses these challenges for both sides; the key is to leverage the idea that everyone values some truths and to draw on insights from scientific fields that study scientific inference -- namely, statistics and machine learning. This common ground also isolates a distinctively epistemic root of the irreconcilability in the realism debate.

**Link**: [arxiv](http://arxiv.org/abs/2412.10643v2),  [pdf](http://arxiv.org/pdf/2412.10643v2)

**Tags**: stat.OT cs.LG stat.ME 



### From General to Specific: Tailoring Large Language Models for   Personalized Healthcare
**Authors**: Ruize Shi, Hong Huang, Wei Zhou, Kehan Yin, Kai Zhao, Yun Zhao

**Updated**: 2024-12-20T14:51:12Z

**Summary**: The rapid development of large language models (LLMs) has transformed many industries, including healthcare. However, previous medical LLMs have largely focused on leveraging general medical knowledge to provide responses, without accounting for patient variability and lacking true personalization at the individual level. To address this, we propose a novel method called personalized medical language model (PMLM), which explores and optimizes personalized LLMs through recommendation systems and reinforcement learning (RL). Specifically, by utilizing self-informed and peer-informed personalization, PMLM captures changes in behaviors and preferences to design initial personalized prompts tailored to individual needs. We further refine these initial personalized prompts through RL, ultimately enhancing the precision of LLM guidance. Notably, the personalized prompt are hard prompt, which grants PMLM high adaptability and reusability, allowing it to directly leverage high-quality proprietary LLMs. We evaluate PMLM using real-world obstetrics and gynecology data, and the experimental results demonstrate that PMLM achieves personalized responses, and it provides more refined and individualized services, offering a potential way for personalized medical LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.15957v1),  [pdf](http://arxiv.org/pdf/2412.15957v1)

**Tags**: cs.CL cs.AI cs.IR 



### Trust Calibration in IDEs: Paving the Way for Widespread Adoption of AI   Refactoring
**Authors**: Markus Borg

**Updated**: 2024-12-20T14:44:11Z

**Summary**: In the software industry, the drive to add new features often overshadows the need to improve existing code. Large Language Models (LLMs) offer a new approach to improving codebases at an unprecedented scale through AI-assisted refactoring. However, LLMs come with inherent risks such as braking changes and the introduction of security vulnerabilities. We advocate for encapsulating the interaction with the models in IDEs and validating refactoring attempts using trustworthy safeguards. However, equally important for the uptake of AI refactoring is research on trust development. In this position paper, we position our future work based on established models from research on human factors in automation. We outline action research within CodeScene on development of 1) novel LLM safeguards and 2) user interaction that conveys an appropriate level of trust. The industry collaboration enables large-scale repository analysis and A/B testing to continuously guide the design of our research interventions.

**Link**: [arxiv](http://arxiv.org/abs/2412.15948v1),  [pdf](http://arxiv.org/pdf/2412.15948v1)

**Tags**: cs.SE cs.AI cs.HC 



### Mamba-based Deep Learning Approaches for Sleep Staging on a Wireless   Multimodal Wearable System without Electroencephalography
**Authors**: Andrew H. Zhang, Alex He-Mo, Richard Fei Yin, Chunlin Li, Yuzhi Tang, Dharmendra Gurve, Nasim Montazeri Ghahjaverestan, Maged Goubran, Bo Wang, Andrew S. P. Lim

**Updated**: 2024-12-20T14:43:02Z

**Summary**: Study Objectives: We investigate using Mamba-based deep learning approaches for sleep staging on signals from ANNE One (Sibel Health, Evanston, IL), a minimally intrusive dual-sensor wireless wearable system measuring chest electrocardiography (ECG), triaxial accelerometry, and temperature, as well as finger photoplethysmography (PPG) and temperature.   Methods: We obtained wearable sensor recordings from 360 adults undergoing concurrent clinical polysomnography (PSG) at a tertiary care sleep lab. PSG recordings were scored according to AASM criteria. PSG and wearable sensor data were automatically aligned using their ECG channels with manual confirmation by visual inspection. We trained Mamba-based models with both convolutional-recurrent neural network (CRNN) and the recurrent neural network (RNN) architectures on these recordings. Ensembling of model variants with similar architectures was performed.   Results: Our best approach, after ensembling, attains a 3-class (wake, NREM, REM) balanced accuracy of 83.50%, F1 score of 84.16%, Cohen's $\kappa$ of 72.68%, and a MCC score of 72.84%; a 4-class (wake, N1/N2, N3, REM) balanced accuracy of 74.64%, F1 score of 74.56%, Cohen's $\kappa$ of 61.63%, and MCC score of 62.04%; a 5-class (wake, N1, N2, N3, REM) balanced accuracy of 64.30%, F1 score of 66.97%, Cohen's $\kappa$ of 53.23%, MCC score of 54.38%.   Conclusions: Deep learning models can infer major sleep stages from a wearable system without electroencephalography (EEG) and can be successfully applied to data from adults attending a tertiary care sleep clinic.

**Link**: [arxiv](http://arxiv.org/abs/2412.15947v1),  [pdf](http://arxiv.org/pdf/2412.15947v1)

**Tags**: q-bio.QM cs.LG 



### Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning
**Authors**: Ziqi Qiu, Jianxing Yu, Yufeng Zhang, Hanjiang Lai, Yanghui Rao, Qinliang Su, Jian Yin

**Updated**: 2024-12-20T14:39:34Z

**Summary**: This paper focuses on sarcasm detection, which aims to identify whether given statements convey criticism, mockery, or other negative sentiment opposite to the literal meaning. To detect sarcasm, humans often require a comprehensive understanding of the semantics in the statement and even resort to external commonsense to infer the fine-grained incongruity. However, existing methods lack commonsense inferential ability when they face complex real-world scenarios, leading to unsatisfactory performance. To address this problem, we propose a novel framework for sarcasm detection, which conducts incongruity reasoning based on commonsense augmentation, called EICR. Concretely, we first employ retrieval-augmented large language models to supplement the missing but indispensable commonsense background knowledge. To capture complex contextual associations, we construct a dependency graph and obtain the optimized topology via graph refinement. We further introduce an adaptive reasoning skeleton that integrates prior rules to extract sentiment-inconsistent subgraphs explicitly. To eliminate the possible spurious relations between words and labels, we employ adversarial contrastive learning to enhance the robustness of the detector. Experiments conducted on five datasets demonstrate the effectiveness of EICR.

**Link**: [arxiv](http://arxiv.org/abs/2412.12808v2),  [pdf](http://arxiv.org/pdf/2412.12808v2)

**Tags**: cs.CL cs.AI 



### Large Language Model assisted Hybrid Fuzzing
**Authors**: Ruijie Meng, Gregory J. Duck, Abhik Roychoudhury

**Updated**: 2024-12-20T14:23:25Z

**Summary**: Greybox fuzzing is one of the most popular methods for detecting software vulnerabilities, which conducts a biased random search within the program input space. To enhance its effectiveness in achieving deep coverage of program behaviors, greybox fuzzing is often combined with concolic execution, which performs a path-sensitive search over the domain of program inputs. In hybrid fuzzing, conventional greybox fuzzing is followed by concolic execution in an iterative loop, where reachability roadblocks encountered by greybox fuzzing are tackled by concolic execution. However, such hybrid fuzzing still suffers from difficulties conventionally faced by symbolic execution, such as the need for environment modeling and system call support. In this work, we show how to achieve the effect of concolic execution without having to compute and solve symbolic path constraints. When coverage-based greybox fuzzing reaches a roadblock in terms of reaching certain branches, we conduct a slicing on the execution trace and suggest modifications of the input to reach the relevant branches. A Large Language Model (LLM) is used as a solver to generate the modified input for reaching the desired branches. Compared with both the vanilla greybox fuzzer AFL and hybrid fuzzers Intriguer and Qsym, our LLM-based hybrid fuzzer HyLLfuzz (pronounced "hill fuzz") demonstrates superior coverage. Furthermore, the LLM-based concolic execution in HyLLfuzz takes a time that is 4-19 times faster than the concolic execution running in existing hybrid fuzzing tools. This experience shows that LLMs can be effectively inserted into the iterative loop of hybrid fuzzers, to efficiently expose more program behaviors.

**Link**: [arxiv](http://arxiv.org/abs/2412.15931v1),  [pdf](http://arxiv.org/pdf/2412.15931v1)

**Tags**: cs.SE cs.CR 



### Less is More: Towards Green Code Large Language Models via Unified   Structural Pruning
**Authors**: Guang Yang, Yu Zhou, Xiangyu Zhang, Wei Cheng, Ke Liu, Xiang Chen, Terry Yue Zhuo, Taolue Chen

**Updated**: 2024-12-20T14:13:09Z

**Summary**: The extensive application of Large Language Models (LLMs) in generative coding tasks has raised concerns due to their high computational demands and energy consumption. Unlike previous structural pruning methods designed for classification models that deal with lowdimensional classification logits, generative Code LLMs produce high-dimensional token logit sequences, making traditional pruning objectives inherently limited. Moreover, existing single component pruning approaches further constrain the effectiveness when applied to generative Code LLMs. In response, we propose Flab-Pruner, an innovative unified structural pruning method that combines vocabulary, layer, and Feed-Forward Network (FFN) pruning. This approach effectively reduces model parameters while maintaining performance. Additionally, we introduce a customized code instruction data strategy for coding tasks to enhance the performance recovery efficiency of the pruned model. Through extensive evaluations on three state-of-the-art Code LLMs across multiple generative coding tasks, the results demonstrate that Flab-Pruner retains 97% of the original performance after pruning 22% of the parameters and achieves the same or even better performance after post-training. The pruned models exhibit significant improvements in storage, GPU usage, computational efficiency, and environmental impact, while maintaining well robustness. Our research provides a sustainable solution for green software engineering and promotes the efficient deployment of LLMs in real-world generative coding intelligence applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.15921v1),  [pdf](http://arxiv.org/pdf/2412.15921v1)

**Tags**: cs.SE cs.AI 



### Employing observability rank conditions for taking into account   experimental information a priori
**Authors**: Alejandro F. Villaverde

**Updated**: 2024-12-20T14:05:41Z

**Summary**: The concept of identifiability describes the possibility of inferring the parameters of a dynamic model by observing its output. It is common and useful to distinguish between structural and practical identifiability. The former property is fully determined by the model equations, while the latter is also influenced by the characteristics of the available experimental data. Structural identifiability can be determined by means of symbolic computations, which may be performed before collecting experimental data, and are hence sometimes called a priori analyses. Practical identifiability is typically assessed numerically, with methods that require simulations - and often also optimization - and are applied a posteriori. An approach to study structural local identifiability is to consider it as a particular case of observability, which is the possibility of inferring the internal state of a system from its output. Thus, both properties can be analysed jointly, by building a generalized observability matrix and computing its rank. The aim of this paper is to investigate to which extent such observability-based methods can also inform about practical aspects related with the experimental setup, which are usually not approached in this way. To this end, we explore a number of possible extensions of the rank tests, and discuss the purposes for which they can be informative as well as others for which they cannot.

**Link**: [arxiv](http://arxiv.org/abs/2410.06984v2),  [pdf](http://arxiv.org/pdf/2410.06984v2)

**Tags**: q-bio.QM cs.SY eess.SY 



### On the Suitability of pre-trained foundational LLMs for Analysis in   German Legal Education
**Authors**: Lorenz Wendlinger, Christian Braun, Abdullah Al Zubaer, Simon Alexander Nonn, Sarah Großkopf, Christofer Fellicious, Michael Granitzer

**Updated**: 2024-12-20T13:54:57Z

**Summary**: We show that current open-source foundational LLMs possess instruction capability and German legal background knowledge that is sufficient for some legal analysis in an educational context. However, model capability breaks down in very specific tasks, such as the classification of "Gutachtenstil" appraisal style components, or with complex contexts, such as complete legal opinions. Even with extended context and effective prompting strategies, they cannot match the Bag-of-Words baseline. To combat this, we introduce a Retrieval Augmented Generation based prompt example selection method that substantially improves predictions in high data availability scenarios. We further evaluate the performance of pre-trained LLMs on two standard tasks for argument mining and automated essay scoring and find it to be more adequate. Throughout, pre-trained LLMs improve upon the baseline in scenarios with little or no labeled data with Chain-of-Thought prompting further helping in the zero-shot case.

**Link**: [arxiv](http://arxiv.org/abs/2412.15902v1),  [pdf](http://arxiv.org/pdf/2412.15902v1)

**Tags**: cs.CL cs.AI 



### Evaluation of Reliability Criteria for News Publishers with Large   Language Models
**Authors**: Manuel Pratelli, John Bianchi, Fabio Pinelli, Marinella Petrocchi

**Updated**: 2024-12-20T13:50:18Z

**Summary**: In this study, we investigate the use of a large language model to assist in the evaluation of the reliability of the vast number of existing online news publishers, addressing the impracticality of relying solely on human expert annotators for this task. In the context of the Italian news media market, we first task the model with evaluating expert-designed reliability criteria using a representative sample of news articles. We then compare the model's answers with those of human experts. The dataset consists of 340 news articles, each annotated by two human experts and the LLM. Six criteria are taken into account, for a total of 6,120 annotations. We observe good agreement between LLM and human annotators in three of the six evaluated criteria, including the critical ability to detect instances where a text negatively targets an entity or individual. For two additional criteria, such as the detection of sensational language and the recognition of bias in news content, LLMs generate fair annotations, albeit with certain trade-offs. Furthermore, we show that the LLM is able to help resolve disagreements among human experts, especially in tasks such as identifying cases of negative targeting.

**Link**: [arxiv](http://arxiv.org/abs/2412.15896v1),  [pdf](http://arxiv.org/pdf/2412.15896v1)

**Tags**: cs.SI 



### Reproducibility of machine learning analyses of 21 cm reionization maps
**Authors**: Kimeel Sooknunan, Emma Chapman, Luke Conaboy, Daniel Mortlock, Jonathan Pritchard

**Updated**: 2024-12-20T13:48:40Z

**Summary**: Machine learning (ML) methods have become popular for parameter inference in cosmology, although their reliance on specific training data can cause difficulties when applied across different data sets. By reproducing and testing networks previously used in the field, and applied to 21cmFast and Simfast21 simulations, we show that convolutional neural networks (CNNs) often learn to identify features of individual simulation boxes rather than the underlying physics, limiting their applicability to real observations. We examine the prediction of the neutral fraction and astrophysical parameters from 21 cm maps and find that networks typically fail to generalise to unseen simulations. We explore a number of case studies to highlight factors that improve or degrade network performance. These results emphasise the responsibility on users to ensure ML models are applied correctly in 21 cm cosmology.

**Link**: [arxiv](http://arxiv.org/abs/2412.15893v1),  [pdf](http://arxiv.org/pdf/2412.15893v1)

**Tags**: astro-ph.CO 



### TelcoLM: collecting data, adapting, and benchmarking language models for   the telecommunication domain
**Authors**: Camille Barboule, Viet-Phi Huynh, Adrien Bufort, Yoan Chabot, Géraldine Damnati, Gwénolé Lecorvé

**Updated**: 2024-12-20T13:47:02Z

**Summary**: Despite outstanding processes in many tasks, Large Language Models (LLMs) still lack accuracy when dealing with highly technical domains. Especially, telecommunications (telco) is a particularly challenging domain due the large amount of lexical, semantic and conceptual peculiarities. Yet, this domain holds many valuable use cases, directly linked to industrial needs. Hence, this paper studies how LLMs can be adapted to the telco domain. It reports our effort to (i) collect a massive corpus of domain-specific data (800M tokens, 80K instructions), (ii) perform adaptation using various methodologies, and (iii) benchmark them against larger generalist models in downstream tasks that require extensive knowledge of telecommunications. Our experiments on Llama-2-7b show that domain-adapted models can challenge the large generalist models. They also suggest that adaptation can be restricted to a unique instruction-tuning step, dicarding the need for any fine-tuning on raw texts beforehand.

**Link**: [arxiv](http://arxiv.org/abs/2412.15891v1),  [pdf](http://arxiv.org/pdf/2412.15891v1)

**Tags**: cs.CL cs.AI 



### Efficient Solutions For An Intriguing Failure of LLMs: Long Context   Window Does Not Mean LLMs Can Analyze Long Sequences Flawlessly
**Authors**: Peyman Hosseini, Ignacio Castro, Iacopo Ghinassi, Matthew Purver

**Updated**: 2024-12-20T13:19:58Z

**Summary**: Large Language Models (LLMs) have demonstrated remarkable capabilities in comprehending and analyzing lengthy sequential inputs, owing to their extensive context windows that allow processing millions of tokens in a single forward pass. However, this paper uncovers a surprising limitation: LLMs fall short when handling long input sequences. We investigate this issue using three datasets and two tasks (sentiment analysis and news categorization) across various LLMs, including Claude 3, Gemini Pro, GPT 3.5 Turbo, Llama 3 Instruct, and Mistral Instruct models. To address this limitation, we propose and evaluate ad-hoc solutions that substantially enhance LLMs' performance on long input sequences by up to 50%, while reducing API cost and latency by up to 93% and 50%, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2408.01866v3),  [pdf](http://arxiv.org/pdf/2408.01866v3)

**Tags**: cs.CL cs.LG I.2.7 



### Large Language Models-guided Dynamic Adaptation for Temporal Knowledge   Graph Reasoning
**Authors**: Jiapu Wang, Kai Sun, Linhao Luo, Wei Wei, Yongli Hu, Alan Wee-Chung Liew, Shirui Pan, Baocai Yin

**Updated**: 2024-12-20T13:15:12Z

**Summary**: Temporal Knowledge Graph Reasoning (TKGR) is the process of utilizing temporal information to capture complex relations within a Temporal Knowledge Graph (TKG) to infer new knowledge. Conventional methods in TKGR typically depend on deep learning algorithms or temporal logical rules. However, deep learning-based TKGRs often lack interpretability, whereas rule-based TKGRs struggle to effectively learn temporal rules that capture temporal patterns. Recently, Large Language Models (LLMs) have demonstrated extensive knowledge and remarkable proficiency in temporal reasoning. Consequently, the employment of LLMs for Temporal Knowledge Graph Reasoning (TKGR) has sparked increasing interest among researchers. Nonetheless, LLMs are known to function as black boxes, making it challenging to comprehend their reasoning process. Additionally, due to the resource-intensive nature of fine-tuning, promptly updating LLMs to integrate evolving knowledge within TKGs for reasoning is impractical. To address these challenges, in this paper, we propose a Large Language Models-guided Dynamic Adaptation (LLM-DA) method for reasoning on TKGs. Specifically, LLM-DA harnesses the capabilities of LLMs to analyze historical data and extract temporal logical rules. These rules unveil temporal patterns and facilitate interpretable reasoning. To account for the evolving nature of TKGs, a dynamic adaptation strategy is proposed to update the LLM-generated rules with the latest events. This ensures that the extracted rules always incorporate the most recent knowledge and better generalize to the predictions on future events. Experimental results show that without the need of fine-tuning, LLM-DA significantly improves the accuracy of reasoning over several common datasets, providing a robust framework for TKGR tasks.

**Link**: [arxiv](http://arxiv.org/abs/2405.14170v2),  [pdf](http://arxiv.org/pdf/2405.14170v2)

**Tags**: cs.AI cs.CL 



### Semantic Foundations of Reductive Reasoning
**Authors**: Alexander V. Gheorghiu, David J. Pym

**Updated**: 2024-12-20T13:13:52Z

**Summary**: The development of logic has largely been through the 'deductive' paradigm: conclusions are inferred from established premisses. However, the use of logic in the context of both human and machine reasoning is typically through the dual 'reductive' perspective: collections of sufficient premisses are generated from putative conclusions. We call this paradigm, 'reductive logic'. This expression of logic encompass as diverse reasoning activities as proving a formula in a formal system to seeking to meet a friend before noon on Saturday. This paper is a semantical analysis of reductive logic. In particular, we provide mathematical foundations for representing and reasoning about 'reduction operators'. Heuristically, reduction operators may be thought of as `backwards' inference rules. In this paper, we address their mathematical representation, how they are used in the context of reductive reasoning, and, crucially, what makes them 'valid'.

**Link**: [arxiv](http://arxiv.org/abs/2412.14758v2),  [pdf](http://arxiv.org/pdf/2412.14758v2)

**Tags**: cs.LO math.LO 



### Recovering the properties of the interstellar medium through integrated   spectroscopy: application to the z~0 ECO volume-limited star-forming galaxy   sample
**Authors**: V. Lebouteiller, C. T. Richardson, M. S. Polimera, D. S. Carr, Z. L. Hutchens, S. J. Kannappan, L. Ramambason, A. J. Moffett, M. Varese, S. C. Madden

**Updated**: 2024-12-20T12:55:29Z

**Summary**: Deriving physical parameters from integrated galaxy spectra is paramount to interpret the cosmic evolution of star formation, chemical enrichment, and energetic sources. We develop modeling techniques to characterize the ionized gas properties in the subset of 2052 star-forming galaxies from the volume-limited, dwarf-dominated, z~0 ECO catalog. The MULTIGRIS statistical framework is used to evaluate the performance of various models using strong lines as constraints. The reference model involves physical parameters distributed as power-laws with free parameter boundaries. Specifically, we use combinations of 1D photoionization models (i.e., considering the propagation of radiation toward a single cloud) to match optical HII region lines, in order to provide probability density functions of the inferred parameters. The inference predicts non-uniform physical conditions within galaxies. The integrated spectra of most galaxies are dominated by relatively low-excitation gas with a metallicity around 0.3 solar. Using the average metallicity in galaxies, we provide a new fit to the mass-metallicity relationship which is in line with direct abundance method determinations from the calibrated range at low metallicity to stacks at high metallicity. The average metallicity shows a weakly bimodal distribution which may be due related to external (e.g., refueling of non-cluster early-type galaxies above ~10^9.5 solar masses) or internal processes (more efficient star-formation in metal-rich regions). The specific line set used for inference affects the results and we identify potential issues with the use of the [SII] line doublet. Complex modelling approaches are limited by the inherent 1D model database as well as caveats regarding the gas geometry. Our results highlight, however, the possibility to extract useful and significant information from integrated spectra.

**Link**: [arxiv](http://arxiv.org/abs/2412.15860v1),  [pdf](http://arxiv.org/pdf/2412.15860v1)

**Tags**: astro-ph.GA 



### MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in   LLMs
**Authors**: Zhongshen Zeng, Yinhong Liu, Yingjia Wan, Jingyao Li, Pengguang Chen, Jianbo Dai, Yuxuan Yao, Rongwu Xu, Zehan Qi, Wanru Zhao, Linling Shen, Jianqiao Lu, Haochen Tan, Yukang Chen, Hao Zhang, Zhan Shi, Bailin Wang, Zhijiang Guo, Jiaya Jia

**Updated**: 2024-12-20T12:52:00Z

**Summary**: Large language models (LLMs) have shown increasing capability in problem-solving and decision-making, largely based on the step-by-step chain-of-thought reasoning processes. However, evaluating these reasoning abilities has become increasingly challenging. Existing outcome-based benchmarks are beginning to saturate, becoming less effective in tracking meaningful progress. To address this, we present a process-based benchmark MR-Ben that demands a meta-reasoning skill, where LMs are asked to locate and analyse potential errors in automatically generated reasoning steps. Our meta-reasoning paradigm is especially suited for system-2 slow thinking, mirroring the human cognitive process of carefully examining assumptions, conditions, calculations, and logic to identify mistakes.MR-Ben comprises 5,975 questions curated by human experts across a wide range of subjects, including physics, chemistry, logic, coding, and more. Through our designed metrics for assessing meta-reasoning on this benchmark, we identify interesting limitations and weaknesses of current LLMs (open-source and closed-source models). For example, with models like the o1 series from OpenAI demonstrating strong performance by effectively scrutinizing the solution space, many other state-of-the-art models fall significantly behind on MR-Ben, exposing potential shortcomings in their training strategies and inference methodologies.

**Link**: [arxiv](http://arxiv.org/abs/2406.13975v3),  [pdf](http://arxiv.org/pdf/2406.13975v3)

**Tags**: cs.CL cs.AI 



### Fake News Detection: Comparative Evaluation of BERT-like Models and   Large Language Models with Generative AI-Annotated Data
**Authors**: Shaina Raza, Drai Paulen-Patterson, Chen Ding

**Updated**: 2024-12-20T12:45:58Z

**Summary**: Fake news poses a significant threat to public opinion and social stability in modern society. This study presents a comparative evaluation of BERT-like encoder-only models and autoregressive decoder-only large language models (LLMs) for fake news detection. We introduce a dataset of news articles labeled with GPT-4 assistance (an AI-labeling method) and verified by human experts to ensure reliability. Both BERT-like encoder-only models and LLMs were fine-tuned on this dataset. Additionally, we developed an instruction-tuned LLM approach with majority voting during inference for label generation. Our analysis reveals that BERT-like models generally outperform LLMs in classification tasks, while LLMs demonstrate superior robustness against text perturbations. Compared to weak labels (distant supervision) data, the results show that AI labels with human supervision achieve better classification results. This study highlights the effectiveness of combining AI-based annotation with human oversight and demonstrates the performance of different families of machine learning models for fake news detection

**Link**: [arxiv](http://arxiv.org/abs/2412.14276v2),  [pdf](http://arxiv.org/pdf/2412.14276v2)

**Tags**: cs.CL cs.AI 



### Are You Human? An Adversarial Benchmark to Expose LLMs
**Authors**: Gilad Gressel, Rahul Pankajakshan, Yisroel Mirsky

**Updated**: 2024-12-20T12:25:22Z

**Summary**: Large Language Models (LLMs) have demonstrated an alarming ability to impersonate humans in conversation, raising concerns about their potential misuse in scams and deception. Humans have a right to know if they are conversing to an LLM. We evaluate text-based prompts designed as challenges to expose LLM imposters in real-time. To this end we compile and release an open-source benchmark dataset that includes 'implicit challenges' that exploit an LLM's instruction-following mechanism to cause role deviation, and 'exlicit challenges' that test an LLM's ability to perform simple tasks typically easy for humans but difficult for LLMs. Our evaluation of 9 leading models from the LMSYS leaderboard revealed that explicit challenges successfully detected LLMs in 78.4% of cases, while implicit challenges were effective in 22.9% of instances. User studies validate the real-world applicability of our methods, with humans outperforming LLMs on explicit challenges (78% vs 22% success rate). Our framework unexpectedly revealed that many study participants were using LLMs to complete tasks, demonstrating its effectiveness in detecting both AI impostors and human misuse of AI tools. This work addresses the critical need for reliable, real-time LLM detection methods in high-stakes conversations.

**Link**: [arxiv](http://arxiv.org/abs/2410.09569v2),  [pdf](http://arxiv.org/pdf/2410.09569v2)

**Tags**: cs.CL cs.AI 



### Improving In-Context Learning with Small Language Model Ensembles
**Authors**: M. Mehdi Mojarradi, Lingyi Yang, Robert McCraith, Adam Mahdi

**Updated**: 2024-12-20T12:22:37Z

**Summary**: Large language models (LLMs) have shown impressive capabilities across various tasks, but their performance on domain-specific tasks remains limited. While methods like retrieval augmented generation and fine-tuning can help to address this, they require significant resources. In-context learning (ICL) is a cheap and efficient alternative but cannot match the accuracies of advanced methods. We present Ensemble SuperICL, a novel approach that enhances ICL by leveraging the expertise of multiple fine-tuned small language models (SLMs). Ensemble SuperICL achieves state of the art (SoTA) results on several natural language understanding benchmarks. Additionally, we test it on a medical-domain labelling task and showcase its practicality by using off-the-shelf SLMs fine-tuned on a general language task, achieving superior accuracy in large-scale data labelling compared to all baselines. Finally, we conduct an ablation study and sensitivity analyses to elucidate the underlying mechanism of Ensemble SuperICL. Our research contributes to the growing demand for efficient domain specialisation methods in LLMs, offering a cheap and effective method for practitioners.

**Link**: [arxiv](http://arxiv.org/abs/2410.21868v2),  [pdf](http://arxiv.org/pdf/2410.21868v2)

**Tags**: cs.CL 



### AIFS-CRPS: Ensemble forecasting using a model trained with a loss   function based on the Continuous Ranked Probability Score
**Authors**: Simon Lang, Mihai Alexe, Mariana C. A. Clare, Christopher Roberts, Rilwan Adewoyin, Zied Ben Bouallègue, Matthew Chantry, Jesper Dramsch, Peter D. Dueben, Sara Hahner, Pedro Maciel, Ana Prieto-Nemesio, Cathal O'Brien, Florian Pinault, Jan Polster, Baudouin Raoult, Steffen Tietsche, Martin Leutbecher

**Updated**: 2024-12-20T12:15:54Z

**Summary**: Over the last three decades, ensemble forecasts have become an integral part of forecasting the weather. They provide users with more complete information than single forecasts as they permit to estimate the probability of weather events by representing the sources of uncertainties and accounting for the day-to-day variability of error growth in the atmosphere. This paper presents a novel approach to obtain a weather forecast model for ensemble forecasting with machine-learning. AIFS-CRPS is a variant of the Artificial Intelligence Forecasting System (AIFS) developed at ECMWF. Its loss function is based on a proper score, the Continuous Ranked Probability Score (CRPS). For the loss, the almost fair CRPS is introduced because it approximately removes the bias in the score due to finite ensemble size yet avoids a degeneracy of the fair CRPS. The trained model is stochastic and can generate as many exchangeable members as desired and computationally feasible in inference. For medium-range forecasts AIFS-CRPS outperforms the physics-based Integrated Forecasting System (IFS) ensemble for the majority of variables and lead times. For subseasonal forecasts, AIFS-CRPS outperforms the IFS ensemble before calibration and is competitive with the IFS ensemble when forecasts are evaluated as anomalies to remove the influence of model biases.

**Link**: [arxiv](http://arxiv.org/abs/2412.15832v1),  [pdf](http://arxiv.org/pdf/2412.15832v1)

**Tags**: physics.ao-ph 



### LLAssist: Simple Tools for Automating Literature Review Using Large   Language Models
**Authors**: Christoforus Yoga Haryanto

**Updated**: 2024-12-20T12:06:25Z

**Summary**: This paper introduces LLAssist, an open-source tool designed to streamline literature reviews in academic research. In an era of exponential growth in scientific publications, researchers face mounting challenges in efficiently processing vast volumes of literature. LLAssist addresses this issue by leveraging Large Language Models (LLMs) and Natural Language Processing (NLP) techniques to automate key aspects of the review process. Specifically, it extracts important information from research articles and evaluates their relevance to user-defined research questions. The goal of LLAssist is to significantly reduce the time and effort required for comprehensive literature reviews, allowing researchers to focus more on analyzing and synthesizing information rather than on initial screening tasks. By automating parts of the literature review workflow, LLAssist aims to help researchers manage the growing volume of academic publications more efficiently.

**Link**: [arxiv](http://arxiv.org/abs/2407.13993v3),  [pdf](http://arxiv.org/pdf/2407.13993v3)

**Tags**: cs.DL cs.AI 



### S$^2$DN: Learning to Denoise Unconvincing Knowledge for Inductive   Knowledge Graph Completion
**Authors**: Tengfei Ma, Yujie Chen, Liang Wang, Xuan Lin, Bosheng Song, Xiangxiang Zeng

**Updated**: 2024-12-20T12:03:33Z

**Summary**: Inductive Knowledge Graph Completion (KGC) aims to infer missing facts between newly emerged entities within knowledge graphs (KGs), posing a significant challenge. While recent studies have shown promising results in inferring such entities through knowledge subgraph reasoning, they suffer from (i) the semantic inconsistencies of similar relations, and (ii) noisy interactions inherent in KGs due to the presence of unconvincing knowledge for emerging entities. To address these challenges, we propose a Semantic Structure-aware Denoising Network (S$^2$DN) for inductive KGC. Our goal is to learn adaptable general semantics and reliable structures to distill consistent semantic knowledge while preserving reliable interactions within KGs. Specifically, we introduce a semantic smoothing module over the enclosing subgraphs to retain the universal semantic knowledge of relations. We incorporate a structure refining module to filter out unreliable interactions and offer additional knowledge, retaining robust structure surrounding target links. Extensive experiments conducted on three benchmark KGs demonstrate that S$^2$DN surpasses the performance of state-of-the-art models. These results demonstrate the effectiveness of S$^2$DN in preserving semantic consistency and enhancing the robustness of filtering out unreliable interactions in contaminated KGs.

**Link**: [arxiv](http://arxiv.org/abs/2412.15822v1),  [pdf](http://arxiv.org/pdf/2412.15822v1)

**Tags**: cs.LG cs.AI cs.CL 



### Cross-Lingual Transfer of Debiasing and Detoxification in Multilingual   LLMs: An Extensive Investigation
**Authors**: Vera Neplenbroek, Arianna Bisazza, Raquel Fernández

**Updated**: 2024-12-20T11:55:35Z

**Summary**: Recent generative large language models (LLMs) show remarkable performance in non-English languages, but when prompted in those languages they tend to express higher harmful social biases and toxicity levels. Prior work has shown that finetuning on specialized datasets can mitigate this behavior, and doing so in English can transfer to other languages. In this work, we investigate the impact of different finetuning methods on the model's bias and toxicity, but also on its ability to produce fluent and diverse text. Our results show that finetuning on curated non-harmful text is more effective for mitigating bias, and finetuning on direct preference optimization (DPO) datasets is more effective for mitigating toxicity. The mitigation caused by applying these methods in English also transfers to non-English languages. We find evidence that the extent to which transfer takes place can be predicted by the amount of data in a given language present in the model's pretraining data. However, this transfer of bias and toxicity mitigation often comes at the expense of decreased language generation ability in non-English languages, highlighting the importance of developing language-specific bias and toxicity mitigation methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.14050v2),  [pdf](http://arxiv.org/pdf/2412.14050v2)

**Tags**: cs.CL 



### Understanding Emotional Body Expressions via Large Language Models
**Authors**: Haifeng Lu, Jiuyi Chen, Feng Liang, Mingkui Tan, Runhao Zeng, Xiping Hu

**Updated**: 2024-12-20T11:49:07Z

**Summary**: Emotion recognition based on body movements is vital in human-computer interaction. However, existing emotion recognition methods predominantly focus on enhancing classification accuracy, often neglecting the provision of textual explanations to justify their classifications. In this paper, we propose an Emotion-Action Interpreter powered by Large Language Model (EAI-LLM), which not only recognizes emotions but also generates textual explanations by treating 3D body movement data as unique input tokens within large language models (LLMs). Specifically, we propose a multi-granularity skeleton tokenizer designed for LLMs, which separately extracts spatio-temporal tokens and semantic tokens from the skeleton data. This approach allows LLMs to generate more nuanced classification descriptions while maintaining robust classification performance. Furthermore, we treat the skeleton sequence as a specific language and propose a unified skeleton token module. This module leverages the extensive background knowledge and language processing capabilities of LLMs to address the challenges of joint training on heterogeneous datasets, thereby significantly enhancing recognition accuracy on individual datasets. Experimental results demonstrate that our model achieves recognition accuracy comparable to existing methods. More importantly, with the support of background knowledge from LLMs, our model can generate detailed emotion descriptions based on classification results, even when trained on a limited amount of labeled skeleton data.

**Link**: [arxiv](http://arxiv.org/abs/2412.12581v2),  [pdf](http://arxiv.org/pdf/2412.12581v2)

**Tags**: cs.HC 



### Prior-Posterior Derived-Predictive Consistency Checks for   Post-Estimation Calculated Quantities of Interest (QOI-Check)
**Authors**: Holger Sennhenn-Reulen

**Updated**: 2024-12-20T11:40:02Z

**Summary**: With flexible modeling software - such as the probabilistic programming language Stan - growing in popularity, quantities of interest (QOIs) calculated post-estimation are increasingly desired and customly implemented, both by statistical software developers and applied scientists. Examples of QOI include the marginal expectation of a multilevel model with a non-linear link function, or an ANOVA decomposition of a bivariate regression spline. For this, the QOI-Check is introduced, a systematic approach to ensure proper calibration and correct interpretation of QOIs. It contributes to Bayesian Workflow, and aims to improve the interpretability and trust in post-estimation conclusions based on QOIs. The QOI-Check builds upon Simulation Based Calibration (SBC), and the Holdout Predictive Check (HPC). SBC verifies computational reliability of Bayesian inference algorithms by consistency check of posterior with prior when the posterior is estimated on prior-predicted data, while HPC ensures robust inference by assessing consistency of model predictions with holdout data. SBC and HPC are combined in QOI-Checking for validating post-estimation QOI calculation and interpretation in the context of a (hypothetical) population definition underlying the QOI.

**Link**: [arxiv](http://arxiv.org/abs/2412.15809v1),  [pdf](http://arxiv.org/pdf/2412.15809v1)

**Tags**: stat.ME 



### CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge   Graph
**Authors**: Hanxiang Xu, Wei Ma, Ting Zhou, Yanjie Zhao, Kai Chen, Qiang Hu, Yang Liu, Haoyu Wang

**Updated**: 2024-12-20T11:25:59Z

**Summary**: In recent years, the programming capabilities of large language models (LLMs) have garnered significant attention. Fuzz testing, a highly effective technique, plays a key role in enhancing software reliability and detecting vulnerabilities. However, traditional fuzz testing tools rely on manually crafted fuzz drivers, which can limit both testing efficiency and effectiveness. To address this challenge, we propose an automated fuzz testing method driven by a code knowledge graph and powered by an LLM-based intelligent agent system, referred to as CKGFuzzer. We approach fuzz driver creation as a code generation task, leveraging the knowledge graph of the code repository to automate the generation process within the fuzzing loop, while continuously refining both the fuzz driver and input seeds. The code knowledge graph is constructed through interprocedural program analysis, where each node in the graph represents a code entity, such as a function or a file. The knowledge graph-enhanced CKGFuzzer not only effectively resolves compilation errors in fuzz drivers and generates input seeds tailored to specific API usage scenarios, but also analyzes fuzz driver crash reports, assisting developers in improving code quality. By querying the knowledge graph of the code repository and learning from API usage scenarios, we can better identify testing targets and understand the specific purpose of each fuzz driver. We evaluated our approach using eight open-source software projects. The experimental results indicate that CKGFuzzer achieved an average improvement of 8.73% in code coverage compared to state-of-the-art techniques. Additionally, CKGFuzzer reduced the manual review workload in crash case analysis by 84.4% and successfully detected 11 real bugs (including nine previously unreported bugs) across the tested libraries.

**Link**: [arxiv](http://arxiv.org/abs/2411.11532v3),  [pdf](http://arxiv.org/pdf/2411.11532v3)

**Tags**: cs.SE cs.CR 



### WebLLM: A High-Performance In-Browser LLM Inference Engine
**Authors**: Charlie F. Ruan, Yucheng Qin, Xun Zhou, Ruihang Lai, Hongyi Jin, Yixin Dong, Bohan Hou, Meng-Shiun Yu, Yiyan Zhai, Sudeep Agarwal, Hangrui Cao, Siyuan Feng, Tianqi Chen

**Updated**: 2024-12-20T11:24:13Z

**Summary**: Advancements in large language models (LLMs) have unlocked remarkable capabilities. While deploying these models typically requires server-grade GPUs and cloud-based inference, the recent emergence of smaller open-source models and increasingly powerful consumer devices have made on-device deployment practical. The web browser as a platform for on-device deployment is universally accessible, provides a natural agentic environment, and conveniently abstracts out the different backends from diverse device vendors. To address this opportunity, we introduce WebLLM, an open-source JavaScript framework that enables high-performance LLM inference entirely within web browsers. WebLLM provides an OpenAI-style API for seamless integration into web applications, and leverages WebGPU for efficient local GPU acceleration and WebAssembly for performant CPU computation. With machine learning compilers MLC-LLM and Apache TVM, WebLLM leverages optimized WebGPU kernels, overcoming the absence of performant WebGPU kernel libraries. Evaluations show that WebLLM can retain up to 80% native performance on the same device, with room to further close the gap. WebLLM paves the way for universally accessible, privacy-preserving, personalized, and locally powered LLM applications in web browsers. The code is available at: https://github.com/mlc-ai/web-llm.

**Link**: [arxiv](http://arxiv.org/abs/2412.15803v1),  [pdf](http://arxiv.org/pdf/2412.15803v1)

**Tags**: cs.LG cs.AI 



### FLUX that Plays Music
**Authors**: Zhengcong Fei, Mingyuan Fan, Changqian Yu, Junshi Huang

**Updated**: 2024-12-20T11:22:01Z

**Summary**: This paper explores a simple extension of diffusion-based rectified flow Transformers for text-to-music generation, termed as FluxMusic. Generally, along with design in advanced Flux\footnote{https://github.com/black-forest-labs/flux} model, we transfers it into a latent VAE space of mel-spectrum. It involves first applying a sequence of independent attention to the double text-music stream, followed by a stacked single music stream for denoised patch prediction. We employ multiple pre-trained text encoders to sufficiently capture caption semantic information as well as inference flexibility. In between, coarse textual information, in conjunction with time step embeddings, is utilized in a modulation mechanism, while fine-grained textual details are concatenated with the music patch sequence as inputs. Through an in-depth study, we demonstrate that rectified flow training with an optimized architecture significantly outperforms established diffusion methods for the text-to-music task, as evidenced by various automatic metrics and human preference evaluations. Our experimental data, code, and model weights are made publicly available at: \url{https://github.com/feizc/FluxMusic}.

**Link**: [arxiv](http://arxiv.org/abs/2409.00587v2),  [pdf](http://arxiv.org/pdf/2409.00587v2)

**Tags**: cs.SD cs.CV eess.AS 



### Diffusion-Based Conditional Image Editing through Optimized Inference   with Guidance
**Authors**: Hyunsoo Lee, Minsoo Kang, Bohyung Han

**Updated**: 2024-12-20T11:15:31Z

**Summary**: We present a simple but effective training-free approach for text-driven image-to-image translation based on a pretrained text-to-image diffusion model. Our goal is to generate an image that aligns with the target task while preserving the structure and background of a source image. To this end, we derive the representation guidance with a combination of two objectives: maximizing the similarity to the target prompt based on the CLIP score and minimizing the structural distance to the source latent variable. This guidance improves the fidelity of the generated target image to the given target prompt while maintaining the structure integrity of the source image. To incorporate the representation guidance component, we optimize the target latent variable of diffusion model's reverse process with the guidance. Experimental results demonstrate that our method achieves outstanding image-to-image translation performance on various tasks when combined with the pretrained Stable Diffusion model.

**Link**: [arxiv](http://arxiv.org/abs/2412.15798v1),  [pdf](http://arxiv.org/pdf/2412.15798v1)

**Tags**: cs.CV 



### A Bayesian Approach for Earthquake Impact Modelling
**Authors**: Max Anderson Loake, Hamish Patten, David Steinsaltz

**Updated**: 2024-12-20T11:07:51Z

**Summary**: Immediately following a disaster event, such as an earthquake, estimates of the damage extent play a key role in informing the coordination of response and recovery efforts. We develop a novel impact estimation tool that leverages a generalised Bayesian approach to generate earthquake impact estimates across three impact types: mortality, population displacement, and building damage. Inference is performed within a likelihood-free framework, and a scoring-rule-based posterior avoids information loss from non-sufficient summary statistics. We propose an adaptation of existing scoring-rule-based loss functions that accommodates the use of an approximate Bayesian computation sequential Monte Carlo (ABC-SMC) framework. The fitted model achieves results comparable to those of two leading impact estimation tools in the prediction of total mortality when tested on a set of held-out past events. The proposed method provides four advantages over existing empirical approaches: modelling produces a gridded spatial map of the estimated impact, predictions benefit from the Bayesian quantification and interpretation of uncertainty, there is direct handling of multi-shock earthquake events, and the use of a joint model between impact types allows predictions to be updated as impact observations become available.

**Link**: [arxiv](http://arxiv.org/abs/2412.15791v1),  [pdf](http://arxiv.org/pdf/2412.15791v1)

**Tags**: stat.AP 



### GraphSeqLM: A Unified Graph Language Framework for Omic Graph Learning
**Authors**: Heming Zhang, Di Huang, Yixin Chen, Fuhai Li

**Updated**: 2024-12-20T11:05:26Z

**Summary**: The integration of multi-omic data is pivotal for understanding complex diseases, but its high dimensionality and noise present significant challenges. Graph Neural Networks (GNNs) offer a robust framework for analyzing large-scale signaling pathways and protein-protein interaction networks, yet they face limitations in expressivity when capturing intricate biological relationships. To address this, we propose Graph Sequence Language Model (GraphSeqLM), a framework that enhances GNNs with biological sequence embeddings generated by Large Language Models (LLMs). These embeddings encode structural and biological properties of DNA, RNA, and proteins, augmenting GNNs with enriched features for analyzing sample-specific multi-omic data. By integrating topological, sequence-derived, and biological information, GraphSeqLM demonstrates superior predictive accuracy and outperforms existing methods, paving the way for more effective multi-omic data integration in precision medicine.

**Link**: [arxiv](http://arxiv.org/abs/2412.15790v1),  [pdf](http://arxiv.org/pdf/2412.15790v1)

**Tags**: q-bio.QM cs.AI cs.LG 



### Linguistic Features Extracted by GPT-4 Improve Alzheimer's Disease   Detection based on Spontaneous Speech
**Authors**: Jonathan Heitz, Gerold Schneider, Nicolas Langer

**Updated**: 2024-12-20T10:43:42Z

**Summary**: Alzheimer's Disease (AD) is a significant and growing public health concern. Investigating alterations in speech and language patterns offers a promising path towards cost-effective and non-invasive early detection of AD on a large scale. Large language models (LLMs), such as GPT, have enabled powerful new possibilities for semantic text analysis. In this study, we leverage GPT-4 to extract five semantic features from transcripts of spontaneous patient speech. The features capture known symptoms of AD, but they are difficult to quantify effectively using traditional methods of computational linguistics. We demonstrate the clinical significance of these features and further validate one of them ("Word-Finding Difficulties") against a proxy measure and human raters. When combined with established linguistic features and a Random Forest classifier, the GPT-derived features significantly improve the detection of AD. Our approach proves effective for both manually transcribed and automatically generated transcripts, representing a novel and impactful use of recent advancements in LLMs for AD speech analysis.

**Link**: [arxiv](http://arxiv.org/abs/2412.15772v1),  [pdf](http://arxiv.org/pdf/2412.15772v1)

**Tags**: cs.CL cs.AI 



### Questioning the Unknown: Optimising Multi-Agent Collaboration in   Narrative-Driven Games
**Authors**: Qinglin Zhu, Runcong Zhao, Jinhua Du, Lin Gui, Yulan He

**Updated**: 2024-12-20T10:35:07Z

**Summary**: We present Questum, a novel framework for Large Language Model (LLM)-based agents in Murder Mystery Games (MMGs). MMGs pose unique challenges, including undefined state spaces, absent intermediate rewards, and the need for strategic interaction in a continuous language domain. Questum addresses these complexities through a sensor-based representation of agent states, a question-targeting mechanism guided by information gain, and a pruning strategy to refine suspect lists and enhance decision-making efficiency. To enable systematic evaluation, we propose WellPlay, a dataset comprising 1,482 inferential questions across 12 games, categorised into objectives, reasoning, and relationships. Experiments demonstrate Questum's capacity to achieve superior performance in reasoning accuracy and efficiency compared to existing approaches, while also significantly improving the quality of agent-human interactions in MMGs. This study advances the development of reasoning agents for complex social and interactive scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2404.17662v3),  [pdf](http://arxiv.org/pdf/2404.17662v3)

**Tags**: cs.CL 



### Function Space Diversity for Uncertainty Prediction via Repulsive   Last-Layer Ensembles
**Authors**: Sophie Steger, Christian Knoll, Bernhard Klein, Holger Fröning, Franz Pernkopf

**Updated**: 2024-12-20T10:24:08Z

**Summary**: Bayesian inference in function space has gained attention due to its robustness against overparameterization in neural networks. However, approximating the infinite-dimensional function space introduces several challenges. In this work, we discuss function space inference via particle optimization and present practical modifications that improve uncertainty estimation and, most importantly, make it applicable for large and pretrained networks. First, we demonstrate that the input samples, where particle predictions are enforced to be diverse, are detrimental to the model performance. While diversity on training data itself can lead to underfitting, the use of label-destroying data augmentation, or unlabeled out-of-distribution data can improve prediction diversity and uncertainty estimates. Furthermore, we take advantage of the function space formulation, which imposes no restrictions on network parameterization other than sufficient flexibility. Instead of using full deep ensembles to represent particles, we propose a single multi-headed network that introduces a minimal increase in parameters and computation. This allows seamless integration to pretrained networks, where this repulsive last-layer ensemble can be used for uncertainty aware fine-tuning at minimal additional cost. We achieve competitive results in disentangling aleatoric and epistemic uncertainty for active learning, detecting out-of-domain data, and providing calibrated uncertainty estimates under distribution shifts with minimal compute and memory.

**Link**: [arxiv](http://arxiv.org/abs/2412.15758v1),  [pdf](http://arxiv.org/pdf/2412.15758v1)

**Tags**: cs.LG 



### Med-Query: Steerable Parsing of 9-DoF Medical Anatomies with Query   Embedding
**Authors**: Heng Guo, Jianfeng Zhang, Ke Yan, Le Lu, Minfeng Xu

**Updated**: 2024-12-20T10:21:14Z

**Summary**: Automatic parsing of human anatomies at the instance-level from 3D computed tomography (CT) is a prerequisite step for many clinical applications. The presence of pathologies, broken structures or limited field-of-view (FOV) can all make anatomy parsing algorithms vulnerable. In this work, we explore how to leverage and implement the successful detection-then-segmentation paradigm for 3D medical data, and propose a steerable, robust, and efficient computing framework for detection, identification, and segmentation of anatomies in CT scans. Considering the complicated shapes, sizes, and orientations of anatomies, without loss of generality, we present a nine degrees of freedom (9-DoF) pose estimation solution in full 3D space using a novel single-stage, non-hierarchical representation. Our whole framework is executed in a steerable manner where any anatomy of interest can be directly retrieved to further boost inference efficiency. We have validated our method on three medical imaging parsing tasks: ribs, spine, and abdominal organs. For rib parsing, CT scans have been annotated at the rib instance-level for quantitative evaluation, similarly for spine vertebrae and abdominal organs. Extensive experiments on 9-DoF box detection and rib instance segmentation demonstrate the high efficiency and effectiveness of our framework (with the identification rate of 97.0% and the segmentation Dice score of 90.9%), compared favorably against several strong baselines (e.g., CenterNet, FCOS, and nnU-Net). For spine parsing and abdominal multi-organ segmentation, our method achieves competitive results on par with state-of-the-art methods on the public CTSpine1K dataset and FLARE22 competition, respectively. Our annotations, code, and models are available at: https://github.com/alibaba-damo-academy/Med_Query.

**Link**: [arxiv](http://arxiv.org/abs/2212.02014v3),  [pdf](http://arxiv.org/pdf/2212.02014v3)

**Tags**: cs.CV 



### Identifying Macro Conditional Independencies and Macro Total Effects in   Summary Causal Graphs with Latent Confounding
**Authors**: Simon Ferreira, Charles K. Assaad

**Updated**: 2024-12-20T10:14:54Z

**Summary**: Understanding causal relations in dynamic systems is essential in epidemiology. While causal inference methods have been extensively studied, they often rely on fully specified causal graphs, which may not always be available in complex dynamic systems. Partially specified causal graphs, and in particular summary causal graphs (SCGs), provide a simplified representation of causal relations between time series when working spacio-temporal data, omitting temporal information and focusing on causal structures between clusters of of temporal variables. Unlike fully specified causal graphs, SCGs can contain cycles, which complicate their analysis and interpretation. In addition, their cluster-based nature introduces new challenges concerning the types of queries of interest: macro queries, which involve relationships between clusters represented as vertices in the graph, and micro queries, which pertain to relationships between variables that are not directly visible through the vertices of the graph. In this paper, we first clearly distinguish between macro conditional independencies and micro conditional independencies and between macro total effects and micro total effects. Then, we demonstrate the soundness and completeness of the d-separation to identify macro conditional independencies in SCGs. Furthermore, we establish that the do-calculus is sound and complete for identifying macro total effects in SCGs. Finally, we give a graphical characterization for the non-identifiability of macro total effects in SCGs.

**Link**: [arxiv](http://arxiv.org/abs/2407.07934v4),  [pdf](http://arxiv.org/pdf/2407.07934v4)

**Tags**: stat.ME cs.AI 



### Extracting Interpretable Task-Specific Circuits from Large Language   Models for Faster Inference
**Authors**: Jorge García-Carrasco, Alejandro Maté, Juan Trujillo

**Updated**: 2024-12-20T10:11:44Z

**Summary**: Large Language Models (LLMs) have shown impressive performance across a wide range of tasks. However, the size of LLMs is steadily increasing, hindering their application on computationally constrained environments. On the other hand, despite their general capabilities, there are many situations where only one specific task is performed, rendering all other capabilities unnecessary and wasteful. This leads us to the following question: Is it possible to extract the minimal subset from an LLM that is able to perform a specific task in a faster, standalone manner? Recent works on Mechanistic Interpretability (MI) have shown that specific tasks are performed by a localized subset of components, or circuit. However, current techniques used to identify the circuit cannot be used to extract it for its standalone usage. In this work, we propose a novel approach to automatically extract the subset of the LLM that properly performs a targeted task requiring no additional training and a small amount of data samples. We evaluate our approach on different tasks and show that the resulting models are (i) considerably smaller, reducing the number of parameters up to 82.77% and (ii) more interpretable, as they focus on the circuit that is used to carry out the specific task, and can therefore be understood using MI techniques.

**Link**: [arxiv](http://arxiv.org/abs/2412.15750v1),  [pdf](http://arxiv.org/pdf/2412.15750v1)

**Tags**: cs.LG 



### Critique of Impure Reason: Unveiling the reasoning behaviour of medical   Large Language Models
**Authors**: Shamus Sim, Tyrone Chen

**Updated**: 2024-12-20T10:06:52Z

**Summary**: Background: Despite the current ubiquity of Large Language Models (LLMs) across the medical domain, there is a surprising lack of studies which address their reasoning behaviour. We emphasise the importance of understanding reasoning behaviour as opposed to high-level prediction accuracies, since it is equivalent to explainable AI (XAI) in this context. In particular, achieving XAI in medical LLMs used in the clinical domain will have a significant impact across the healthcare sector. Results: Therefore, we define the concept of reasoning behaviour in the specific context of medical LLMs. We then categorise and discuss the current state of the art of methods which evaluate reasoning behaviour in medical LLMs. Finally, we propose theoretical frameworks which can empower medical professionals or machine learning engineers to gain insight into the low-level reasoning operations of these previously obscure models. Conclusion: The subsequent increased transparency and trust in medical machine learning models by clinicians as well as patients will accelerate the integration, application as well as further development of medical AI for the healthcare system as a whole

**Link**: [arxiv](http://arxiv.org/abs/2412.15748v1),  [pdf](http://arxiv.org/pdf/2412.15748v1)

**Tags**: cs.CL cs.AI cs.LG 



### Dynamic Learning Rate Decay for Stochastic Variational Inference
**Authors**: Maximilian Dinkel, Gil Robalo Rei, Wolfgang A. Wall

**Updated**: 2024-12-20T10:04:59Z

**Summary**: Like many optimization algorithms, Stochastic Variational Inference (SVI) is sensitive to the choice of the learning rate. If the learning rate is too small, the optimization process may be slow, and the algorithm might get stuck in local optima. On the other hand, if the learning rate is too large, the algorithm may oscillate or diverge, failing to converge to a solution. Adaptive learning rate methods such as Adam, AdaMax, Adagrad, or RMSprop automatically adjust the learning rate based on the history of gradients. Nevertheless, if the base learning rate is too large, the variational parameters might still oscillate around the optimal solution. With learning rate schedules, the learning rate can be reduced gradually to mitigate this problem. However, the amount at which the learning rate should be decreased in each iteration is not known a priori, which can significantly impact the performance of the optimization. In this work, we propose a method to decay the learning rate based on the history of the variational parameters. We use an empirical measure to quantify the amount of oscillations against the progress of the variational parameters to adapt the learning rate. The approach requires little memory and is computationally efficient. We demonstrate in various numerical examples that our method reduces the sensitivity of the optimization performance to the learning rate and that it can also be used in combination with other adaptive learning rate methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.15745v1),  [pdf](http://arxiv.org/pdf/2412.15745v1)

**Tags**: cs.CE 



### Prompt-based Unifying Inference Attack on Graph Neural Networks
**Authors**: Yuecen Wei, Xingcheng Fu, Lingyun Liu, Qingyun Sun, Hao Peng, Chunming Hu

**Updated**: 2024-12-20T09:56:17Z

**Summary**: Graph neural networks (GNNs) provide important prospective insights in applications such as social behavior analysis and financial risk analysis based on their powerful learning capabilities on graph data. Nevertheless, GNNs' predictive performance relies on the quality of task-specific node labels, so it is common practice to improve the model's generalization ability in the downstream execution of decision-making tasks through pre-training. Graph prompting is a prudent choice but risky without taking measures to prevent data leakage. In other words, in high-risk decision scenarios, prompt learning can infer private information by accessing model parameters trained on private data (publishing model parameters in pre-training, i.e., without directly leaking the raw data, is a tacitly accepted trend). However, myriad graph inference attacks necessitate tailored module design and processing to enhance inference capabilities due to variations in supervision signals. In this paper, we propose a novel Prompt-based unifying Inference Attack framework on GNNs, named ProIA. Specifically, ProIA retains the crucial topological information of the graph during pre-training, enhancing the background knowledge of the inference attack model. It then utilizes a unified prompt and introduces additional disentanglement factors in downstream attacks to adapt to task-relevant knowledge. Finally, extensive experiments show that ProIA enhances attack capabilities and demonstrates remarkable adaptability to various inference attacks.

**Link**: [arxiv](http://arxiv.org/abs/2412.15735v1),  [pdf](http://arxiv.org/pdf/2412.15735v1)

**Tags**: cs.LG 



### Utilize the Flow before Stepping into the Same River Twice: Certainty   Represented Knowledge Flow for Refusal-Aware Instruction Tuning
**Authors**: Runchuan Zhu, Zhipeng Ma, Jiang Wu, Junyuan Gao, Jiaqi Wang, Dahua Lin, Conghui He

**Updated**: 2024-12-20T09:40:54Z

**Summary**: Refusal-Aware Instruction Tuning (RAIT) enables Large Language Models (LLMs) to refuse to answer unknown questions. By modifying responses of unknown questions in the training data to refusal responses such as "I don't know", RAIT enhances the reliability of LLMs and reduces their hallucination. Generally, RAIT modifies training samples based on the correctness of the initial LLM's response. However, this crude approach can cause LLMs to excessively refuse answering questions they could have correctly answered, the problem we call over-refusal. In this paper, we explore two primary causes of over-refusal: Static conflict occurs when similar samples within the LLM's feature space receive differing supervision signals (original vs. modified "I don't know"). Dynamic conflict arises as the LLM's evolving knowledge during SFT enables it to answer previously unanswerable questions, but the now-answerable training samples still retain the original "I don't know" supervision signals from the initial LLM state, leading to inconsistencies. These conflicts cause the trained LLM to misclassify known questions as unknown, resulting in over-refusal. To address this issue, we introduce Certainty Represented Knowledge Flow for Refusal-Aware Instructions Tuning (CRaFT). CRaFT centers on two main contributions: First, we additionally incorporate response certainty to selectively filter and modify data, reducing static conflicts. Second, we implement preliminary rehearsal training to characterize changes in the LLM's knowledge state, which helps mitigate dynamic conflicts during the fine-tuning process. We conducted extensive experiments on open-ended question answering and multiple-choice question task. Experiment results show that CRaFT can improve LLM's overall performance during the RAIT process. Code and data will be released at https://github.com/opendatalab/CRaFT .

**Link**: [arxiv](http://arxiv.org/abs/2410.06913v3),  [pdf](http://arxiv.org/pdf/2410.06913v3)

**Tags**: cs.CL 



### A Plug-and-Play Fully On-the-Job Real-Time Reinforcement Learning   Algorithm for a Direct-Drive Tandem-Wing Experiment Platforms Under Multiple   Random Operating Conditions
**Authors**: Zhang Minghao, Song Bifeng, Yang Xiaojun, Wang Liang

**Updated**: 2024-12-20T09:39:06Z

**Summary**: The nonlinear and unstable aerodynamic interference generated by the tandem wings of such biomimetic systems poses substantial challenges for motion control, especially under multiple random operating conditions. To address these challenges, the Concerto Reinforcement Learning Extension (CRL2E) algorithm has been developed. This plug-and-play, fully on-the-job, real-time reinforcement learning algorithm incorporates a novel Physics-Inspired Rule-Based Policy Composer Strategy with a Perturbation Module alongside a lightweight network optimized for real-time control. To validate the performance and the rationality of the module design, experiments were conducted under six challenging operating conditions, comparing seven different algorithms. The results demonstrate that the CRL2E algorithm achieves safe and stable training within the first 500 steps, improving tracking accuracy by 14 to 66 times compared to the Soft Actor-Critic, Proximal Policy Optimization, and Twin Delayed Deep Deterministic Policy Gradient algorithms. Additionally, CRL2E significantly enhances performance under various random operating conditions, with improvements in tracking accuracy ranging from 8.3% to 60.4% compared to the Concerto Reinforcement Learning (CRL) algorithm. The convergence speed of CRL2E is 36.11% to 57.64% faster than the CRL algorithm with only the Composer Perturbation and 43.52% to 65.85% faster than the CRL algorithm when both the Composer Perturbation and Time-Interleaved Capability Perturbation are introduced, especially in conditions where the standard CRL struggles to converge. Hardware tests indicate that the optimized lightweight network structure excels in weight loading and average inference time, meeting real-time control requirements.

**Link**: [arxiv](http://arxiv.org/abs/2410.15554v2),  [pdf](http://arxiv.org/pdf/2410.15554v2)

**Tags**: cs.LG cs.AI cs.RO 



### AutoLife: Automatic Life Journaling with Smartphones and LLMs
**Authors**: Huatao Xu, Panron Tong, Mo Li, Mani Srivastava

**Updated**: 2024-12-20T09:37:02Z

**Summary**: This paper introduces a novel mobile sensing application - life journaling - designed to generate semantic descriptions of users' daily lives. We present AutoLife, an automatic life journaling system based on commercial smartphones. AutoLife only inputs low-cost sensor data (without photos or audio) from smartphones and can automatically generate comprehensive life journals for users. To achieve this, we first derive time, motion, and location contexts from multimodal sensor data, and harness the zero-shot capabilities of Large Language Models (LLMs), enriched with commonsense knowledge about human lives, to interpret diverse contexts and generate life journals. To manage the task complexity and long sensing duration, a multilayer framework is proposed, which decomposes tasks and seamlessly integrates LLMs with other techniques for life journaling. This study establishes a real-life dataset as a benchmark and extensive experiment results demonstrate that AutoLife produces accurate and reliable life journals.

**Link**: [arxiv](http://arxiv.org/abs/2412.15714v1),  [pdf](http://arxiv.org/pdf/2412.15714v1)

**Tags**: cs.AI cs.CL cs.HC 



### Contrastive Learning for Task-Independent SpeechLLM-Pretraining
**Authors**: Maike Züfle, Jan Niehues

**Updated**: 2024-12-20T09:33:31Z

**Summary**: Large language models (LLMs) excel in natural language processing but adapting these LLMs to speech processing tasks efficiently is not straightforward. Direct task-specific fine-tuning is limited by overfitting risks, data requirements, and computational costs. To address these challenges, we propose a scalable, two-stage training approach: (1) A task-independent speech pretraining stage using contrastive learning to align text and speech representations over all layers, followed by (2) a task-specific fine-tuning stage requiring minimal data. This approach outperforms traditional ASR pretraining and enables the model to surpass models specialized on speech translation and question answering while being trained on only 10% of the task-specific data.

**Link**: [arxiv](http://arxiv.org/abs/2412.15712v1),  [pdf](http://arxiv.org/pdf/2412.15712v1)

**Tags**: cs.CL cs.HC 



### Cracking the Code: Evaluating Zero-Shot Prompting Methods for Providing   Programming Feedback
**Authors**: Niklas Ippisch, Anna-Carolina Haensch, Jan Simson, Jacob Beck, Markus Herklotz, Malte Schierholz

**Updated**: 2024-12-20T09:24:50Z

**Summary**: Despite the growing use of large language models (LLMs) for providing feedback, limited research has explored how to achieve high-quality feedback. This case study introduces an evaluation framework to assess different zero-shot prompt engineering methods. We varied the prompts systematically and analyzed the provided feedback on programming errors in R. The results suggest that prompts suggesting a stepwise procedure increase the precision, while omitting explicit specifications about which provided data to analyze improves error identification.

**Link**: [arxiv](http://arxiv.org/abs/2412.15702v1),  [pdf](http://arxiv.org/pdf/2412.15702v1)

**Tags**: cs.SE 



### Code Review Automation Via Multi-task Federated LLM -- An Empirical   Study
**Authors**: Jahnavi Kumar, Sridhar Chimalakonda

**Updated**: 2024-12-20T08:46:46Z

**Summary**: Code review is a crucial process before deploying code to production, as it validates the code, provides suggestions for improvements, and identifies errors such as missed edge cases. In projects with regular production releases, the effort required for peer code-reviews remains high. Consequently, there has been significant interest from software engineering (SE) researchers in automating the code review process. Previous research on code review automation has typically approached the task as three independent sub-tasks: review necessity prediction, review comment generation, and code refinement. Our study attempts to (i) leverage the relationships between the sub-tasks of code review automation, by developing a multi-task model that addresses all tasks in an integrated manner, and (ii) increase model robustness on unseen data via collaborative large language model (LLM) modeling, while retaining the proprietary nature of code, by using federated learning (FL). The study explores five simple techniques for multi-task training, including two sequential methods, one parallel method, and two cumulative methods. The results indicate that sequentially training a federated LLM (FedLLM) for our code review multi-task use case is less efficient in terms of time, computation, and performance metrics, compared to training separate models for each task. Because sequential training demonstrates catastrophic forgetting, alternatively cumulative fine-tuning for multi-task training performs better than training models for individual tasks. This study highlights the need for research focused on effective fine-tuning of multi-task FedLLMs for SE tasks.

**Link**: [arxiv](http://arxiv.org/abs/2412.15676v1),  [pdf](http://arxiv.org/pdf/2412.15676v1)

**Tags**: cs.SE 



### Small Language Models as Effective Guides for Large Language Models in   Chinese Relation Extraction
**Authors**: Xuemei Tang, Jun Wang

**Updated**: 2024-12-20T08:46:30Z

**Summary**: Recently, large language models (LLMs) have been successful in relational extraction (RE) tasks, especially in the few-shot learning. An important problem in the field of RE is long-tailed data, while not much attention is paid to this problem using LLM approaches. Therefore, in this paper, we propose SLCoLM, a model collaboration framework, to mitigate the data long-tail problem. In our framework, we use the ``\textit{Training-Guide-Predict}'' strategy to combine the strengths of small pre-trained language models (SLMs) and LLMs, where a task-specific SLM framework acts as a guider, transfers task knowledge to the LLM and guides the LLM in performing RE tasks. Our experiments on an ancient Chinese RE dataset rich in relation types show that the approach facilitates RE of long-tail relation types.

**Link**: [arxiv](http://arxiv.org/abs/2402.14373v2),  [pdf](http://arxiv.org/pdf/2402.14373v2)

**Tags**: cs.CL 



### AdaSociety: An Adaptive Environment with Social Structures for   Multi-Agent Decision-Making
**Authors**: Yizhe Huang, Xingbo Wang, Hao Liu, Fanqi Kong, Aoyang Qin, Min Tang, Xiaoxi Wang, Song-Chun Zhu, Mingjie Bi, Siyuan Qi, Xue Feng

**Updated**: 2024-12-20T08:38:38Z

**Summary**: Traditional interactive environments limit agents' intelligence growth with fixed tasks. Recently, single-agent environments address this by generating new tasks based on agent actions, enhancing task diversity. We consider the decision-making problem in multi-agent settings, where tasks are further influenced by social connections, affecting rewards and information access. However, existing multi-agent environments lack a combination of adaptive physical surroundings and social connections, hindering the learning of intelligent behaviors. To address this, we introduce AdaSociety, a customizable multi-agent environment featuring expanding state and action spaces, alongside explicit and alterable social structures. As agents progress, the environment adaptively generates new tasks with social structures for agents to undertake. In AdaSociety, we develop three mini-games showcasing distinct social structures and tasks. Initial results demonstrate that specific social structures can promote both individual and collective benefits, though current reinforcement learning and LLM-based algorithms show limited effectiveness in leveraging social structures to enhance performance. Overall, AdaSociety serves as a valuable research platform for exploring intelligence in diverse physical and social settings. The code is available at https://github.com/bigai-ai/AdaSociety.

**Link**: [arxiv](http://arxiv.org/abs/2411.03865v3),  [pdf](http://arxiv.org/pdf/2411.03865v3)

**Tags**: cs.MA cs.AI cs.GT cs.LG cs.SI 



### Measuring Human and AI Values Based on Generative Psychometrics with   Large Language Models
**Authors**: Haoran Ye, Yuhang Xie, Yuanyi Ren, Hanjun Fang, Xin Zhang, Guojie Song

**Updated**: 2024-12-20T08:35:24Z

**Summary**: Human values and their measurement are long-standing interdisciplinary inquiry. Recent advances in AI have sparked renewed interest in this area, with large language models (LLMs) emerging as both tools and subjects of value measurement. This work introduces Generative Psychometrics for Values (GPV), an LLM-based, data-driven value measurement paradigm, theoretically grounded in text-revealed selective perceptions. The core idea is to dynamically parse unstructured texts into perceptions akin to static stimuli in traditional psychometrics, measure the value orientations they reveal, and aggregate the results. Applying GPV to human-authored blogs, we demonstrate its stability, validity, and superiority over prior psychological tools. Then, extending GPV to LLM value measurement, we advance the current art with 1) a psychometric methodology that measures LLM values based on their scalable and free-form outputs, enabling context-specific measurement; 2) a comparative analysis of measurement paradigms, indicating response biases of prior methods; and 3) an attempt to bridge LLM values and their safety, revealing the predictive power of different value systems and the impacts of various values on LLM safety. Through interdisciplinary efforts, we aim to leverage AI for next-generation psychometrics and psychometrics for value-aligned AI.

**Link**: [arxiv](http://arxiv.org/abs/2409.12106v2),  [pdf](http://arxiv.org/pdf/2409.12106v2)

**Tags**: cs.CL cs.AI 



### WigglyEyes: Inferring Eye Movements from Keypress Data
**Authors**: Yujun Zhu, Danqing Shi, Hee-Seung Moon, Antti Oulasvirta

**Updated**: 2024-12-20T08:35:12Z

**Summary**: We present a model for inferring where users look during interaction based on keypress data only. Given a key log, it outputs a scanpath that tells, moment-by-moment, how the user had moved eyes while entering those keys. The model can be used as a proxy for human data in cases where collecting real eye tracking data is expensive or impossible. Our technical insight is three-fold: first, we present an inference architecture that considers the individual characteristics of the user, inferred as a low-dimensional parameter vector; second, we present a novel loss function for synchronizing inferred eye movements with the keypresses; third, we train the model using a hybrid approach with both human data and synthetically generated data. The approach can be applied in interactive systems where predictive models of user behavior are available. We report results from evaluation in the challenging case of touchscreen typing, where the model accurately inferred real eye movements.

**Link**: [arxiv](http://arxiv.org/abs/2412.15669v1),  [pdf](http://arxiv.org/pdf/2412.15669v1)

**Tags**: cs.HC 



### A survey on FPGA-based accelerator for ML models
**Authors**: Feng Yan, Andreas Koch, Oliver Sinnen

**Updated**: 2024-12-20T08:30:40Z

**Summary**: This paper thoroughly surveys machine learning (ML) algorithms acceleration in hardware accelerators, focusing on Field-Programmable Gate Arrays (FPGAs). It reviews 287 out of 1138 papers from the past six years, sourced from four top FPGA conferences. Such selection underscores the increasing integration of ML and FPGA technologies and their mutual importance in technological advancement. Research clearly emphasises inference acceleration (81\%) compared to training acceleration (13\%). Additionally, the findings reveals that CNN dominates current FPGA acceleration research while emerging models like GNN show obvious growth trends. The categorization of the FPGA research papers reveals a wide range of topics, demonstrating the growing relevance of ML in FPGA research. This comprehensive analysis provides valuable insights into the current trends and future directions of FPGA research in the context of ML applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.15666v1),  [pdf](http://arxiv.org/pdf/2412.15666v1)

**Tags**: cs.AR cs.LG 68W25, 68M20, 68Q25 I.5.4; C.1.3; B.5.2 



### Adaptable and Precise: Enterprise-Scenario LLM Function-Calling   Capability Training Pipeline
**Authors**: Guancheng Zeng, Wentao Ding, Beining Xu, Chi Zhang, Wenqiang Han, Gang Li, Jingjing Mo, Pengxu Qiu, Xinran Tao, Wang Tao, Haowen Hu

**Updated**: 2024-12-20T08:20:21Z

**Summary**: Enterprises possess a vast array of API assets scattered across various functions, forming the backbone of existing business processes. By leveraging these APIs as functional tools, enterprises can design diverse, scenario-specific agent applications, driven by on-premise function-calling models as the core engine. However, generic models often fail to meet enterprise requirements in terms of computational efficiency, output accuracy, and stability, necessitating scenario-specific adaptation. In this paper, we propose a training pipeline for function-calling capabilities tailored to real-world business scenarios. This pipeline includes the synthesis and augmentation of scenario-specific function-calling data, model fine-tuning, and performance evaluation and analysis. Using this pipeline, we generated 1,260 fully AI-generated samples and 1,035 augmented manually-labeled samples in digital HR agent scenario. The Qwen2.5-Coder-7B-Instruct model was employed as the base model and fine-tuned using the LoRA method on four GPUs with 24GB VRAM. Our fine-tuned model demonstrated outstanding performance in evaluations and practical applications, surpassing GPT-4 and GPT-4o in accuracy on the test set. These results validate the reliability of the proposed pipeline for training scenario-specific function-calling models.

**Link**: [arxiv](http://arxiv.org/abs/2412.15660v1),  [pdf](http://arxiv.org/pdf/2412.15660v1)

**Tags**: cs.AI cs.CL cs.SE 



### MathSpeech: Leveraging Small LMs for Accurate Conversion in Mathematical   Speech-to-Formula
**Authors**: Sieun Hyeon, Kyudan Jung, Jaehee Won, Nam-Joon Kim, Hyun Gon Ryu, Hyuk-Jae Lee, Jaeyoung Do

**Updated**: 2024-12-20T08:13:05Z

**Summary**: In various academic and professional settings, such as mathematics lectures or research presentations, it is often necessary to convey mathematical expressions orally. However, reading mathematical expressions aloud without accompanying visuals can significantly hinder comprehension, especially for those who are hearing-impaired or rely on subtitles due to language barriers. For instance, when a presenter reads Euler's Formula, current Automatic Speech Recognition (ASR) models often produce a verbose and error-prone textual description (e.g., e to the power of i x equals cosine of x plus i $\textit{side}$ of x), instead of the concise $\LaTeX{}$ format (i.e., $ e^{ix} = \cos(x) + i\sin(x) $), which hampers clear understanding and communication. To address this issue, we introduce MathSpeech, a novel pipeline that integrates ASR models with small Language Models (sLMs) to correct errors in mathematical expressions and accurately convert spoken expressions into structured $\LaTeX{}$ representations. Evaluated on a new dataset derived from lecture recordings, MathSpeech demonstrates $\LaTeX{}$ generation capabilities comparable to leading commercial Large Language Models (LLMs), while leveraging fine-tuned small language models of only 120M parameters. Specifically, in terms of CER, BLEU, and ROUGE scores for $\LaTeX{}$ translation, MathSpeech demonstrated significantly superior capabilities compared to GPT-4o. We observed a decrease in CER from 0.390 to 0.298, and higher ROUGE/BLEU scores compared to GPT-4o.

**Link**: [arxiv](http://arxiv.org/abs/2412.15655v1),  [pdf](http://arxiv.org/pdf/2412.15655v1)

**Tags**: cs.CL cs.AI 



### SLAM-Omni: Timbre-Controllable Voice Interaction System with   Single-Stage Training
**Authors**: Wenxi Chen, Ziyang Ma, Ruiqi Yan, Yuzhe Liang, Xiquan Li, Ruiyang Xu, Zhikang Niu, Yanqiao Zhu, Yifan Yang, Zhanxun Liu, Kai Yu, Yuxuan Hu, Jinyu Li, Yan Lu, Shujie Liu, Xie Chen

**Updated**: 2024-12-20T08:05:55Z

**Summary**: Recent advancements highlight the potential of end-to-end real-time spoken dialogue systems, showcasing their low latency and high quality. In this paper, we introduce SLAM-Omni, a timbre-controllable, end-to-end voice interaction system with single-stage training. SLAM-Omni achieves zero-shot timbre control by modeling spoken language with semantic tokens and decoupling speaker information to a vocoder. By predicting grouped speech semantic tokens at each step, our method significantly reduces the sequence length of audio tokens, accelerating both training and inference. Additionally, we propose historical text prompting to compress dialogue history, facilitating efficient multi-round interactions. Comprehensive evaluations reveal that SLAM-Omni outperforms prior models of similar scale, requiring only 15 hours of training on 4 GPUs with limited data. Notably, it is the first spoken dialogue system to achieve competitive performance with a single-stage training approach, eliminating the need for pre-training on TTS or ASR tasks. Further experiments validate its multilingual and multi-turn dialogue capabilities on larger datasets.

**Link**: [arxiv](http://arxiv.org/abs/2412.15649v1),  [pdf](http://arxiv.org/pdf/2412.15649v1)

**Tags**: eess.AS 



### What to Preserve and What to Transfer: Faithful, Identity-Preserving   Diffusion-based Hairstyle Transfer
**Authors**: Chaeyeon Chung, Sunghyun Park, Jeongho Kim, Jaegul Choo

**Updated**: 2024-12-20T08:01:10Z

**Summary**: Hairstyle transfer is a challenging task in the image editing field that modifies the hairstyle of a given face image while preserving its other appearance and background features. The existing hairstyle transfer approaches heavily rely on StyleGAN, which is pre-trained on cropped and aligned face images. Hence, they struggle to generalize under challenging conditions such as extreme variations of head poses or focal lengths. To address this issue, we propose a one-stage hairstyle transfer diffusion model, HairFusion, that applies to real-world scenarios. Specifically, we carefully design a hair-agnostic representation as the input of the model, where the original hair information is thoroughly eliminated. Next, we introduce a hair align cross-attention (Align-CA) to accurately align the reference hairstyle with the face image while considering the difference in their head poses. To enhance the preservation of the face image's original features, we leverage adaptive hair blending during the inference, where the output's hair regions are estimated by the cross-attention map in Align-CA and blended with non-hair areas of the face image. Our experimental results show that our method achieves state-of-the-art performance compared to the existing methods in preserving the integrity of both the transferred hairstyle and the surrounding features. The codes are available at https://github.com/cychungg/HairFusion

**Link**: [arxiv](http://arxiv.org/abs/2408.16450v2),  [pdf](http://arxiv.org/pdf/2408.16450v2)

**Tags**: cs.CV 



### ConCSE: Unified Contrastive Learning and Augmentation for Code-Switched   Embeddings
**Authors**: Jangyeong Jeon, Sangyeon Cho, Minuk Ma, Junyoung Kim

**Updated**: 2024-12-20T07:58:22Z

**Summary**: This paper examines the Code-Switching (CS) phenomenon where two languages intertwine within a single utterance. There exists a noticeable need for research on the CS between English and Korean. We highlight that the current Equivalence Constraint (EC) theory for CS in other languages may only partially capture English-Korean CS complexities due to the intrinsic grammatical differences between the languages. We introduce a novel Koglish dataset tailored for English-Korean CS scenarios to mitigate such challenges. First, we constructed the Koglish-GLUE dataset to demonstrate the importance and need for CS datasets in various tasks. We found the differential outcomes of various foundation multilingual language models when trained on a monolingual versus a CS dataset. Motivated by this, we hypothesized that SimCSE, which has shown strengths in monolingual sentence embedding, would have limitations in CS scenarios. We construct a novel Koglish-NLI (Natural Language Inference) dataset using a CS augmentation-based approach to verify this. From this CS-augmented dataset Koglish-NLI, we propose a unified contrastive learning and augmentation method for code-switched embeddings, ConCSE, highlighting the semantics of CS sentences. Experimental results validate the proposed ConCSE with an average performance enhancement of 1.77\% on the Koglish-STS(Semantic Textual Similarity) tasks.

**Link**: [arxiv](http://arxiv.org/abs/2409.00120v2),  [pdf](http://arxiv.org/pdf/2409.00120v2)

**Tags**: cs.CL cs.AI 



### Stroboscopic measurements in Markov networks: Exact generator   reconstruction vs. thermodynamic inference
**Authors**: Malena T. Bauer, Udo Seifert, Jann van der Meer

**Updated**: 2024-12-20T07:57:56Z

**Summary**: A major goal of stochastic thermodynamics is to estimate the inevitable dissipation that accompanies particular observable phenomena in an otherwise not fully accessible system. Quantitative results are often formulated as lower bounds on the total entropy production, which capture the part of the total dissipation that can be determined based on the available data alone. In this work, we discuss the case of a continuous-time dynamics on a Markov network that is observed stroboscopically, i.e., at discrete points in time in regular intervals. We compare the standard approach of deriving a lower bound on the entropy production rate in the steady state to the less common method of reconstructing the generator from the observed propagators by taking the matrix logarithm. Provided that the timescale of the stroboscopic measurements is smaller than a critical value that can be determined from the available data, this latter method is able to recover all thermodynamic quantities like entropy production or cycle affinities and is therefore superior to the usual approach of deriving lower bounds. Beyond the critical value, we still obtain tight upper and lower bounds on these quantities that improve on extant methods. We conclude the comparison with numerical illustrations and a discussion of the requirements and limitations of both methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.15642v1),  [pdf](http://arxiv.org/pdf/2412.15642v1)

**Tags**: cond-mat.stat-mech 



### Federated Graph Condensation with Information Bottleneck Principles
**Authors**: Bo Yan, Sihao He, Cheng Yang, Shang Liu, Yang Cao, Chuan Shi

**Updated**: 2024-12-20T07:57:07Z

**Summary**: Graph condensation (GC), which reduces the size of a large-scale graph by synthesizing a small-scale condensed graph as its substitution, has benefited various graph learning tasks. However, existing GC methods rely on centralized data storage, which is unfeasible for real-world decentralized data distribution, and overlook data holders' privacy-preserving requirements. To bridge this gap, we propose and study the novel problem of federated graph condensation (FGC) for graph neural networks (GNNs). Specifically, we first propose a general framework for FGC, where we decouple the typical gradient matching process for GC into client-side gradient calculation and server-side gradient matching, integrating knowledge from multiple clients' subgraphs into one smaller condensed graph. Nevertheless, our empirical studies show that under the federated setting, the condensed graph will consistently leak data membership privacy, i.e., the condensed graph during federated training can be utilized to steal training data under the membership inference attack (MIA). To tackle this issue, we innovatively incorporate information bottleneck principles into the FGC, which only needs to extract partial node features in one local pre-training step and utilize the features during federated training. Theoretical and experimental analyses demonstrate that our framework consistently protects membership privacy during training. Meanwhile, it can achieve comparable and even superior performance against existing centralized GC and federated graph learning (FGL) methods.

**Link**: [arxiv](http://arxiv.org/abs/2405.03911v4),  [pdf](http://arxiv.org/pdf/2405.03911v4)

**Tags**: cs.LG cs.AI cs.CR cs.DC 



### Tacit Learning with Adaptive Information Selection for Cooperative   Multi-Agent Reinforcement Learning
**Authors**: Lunjun Liu, Weilai Jiang, Yaonan Wang

**Updated**: 2024-12-20T07:55:59Z

**Summary**: In multi-agent reinforcement learning (MARL), the centralized training with decentralized execution (CTDE) framework has gained widespread adoption due to its strong performance. However, the further development of CTDE faces two key challenges. First, agents struggle to autonomously assess the relevance of input information for cooperative tasks, impairing their decision-making abilities. Second, in communication-limited scenarios with partial observability, agents are unable to access global information, restricting their ability to collaborate effectively from a global perspective. To address these challenges, we introduce a novel cooperative MARL framework based on information selection and tacit learning. In this framework, agents gradually develop implicit coordination during training, enabling them to infer the cooperative behavior of others in a discrete space without communication, relying solely on local information. Moreover, we integrate gating and selection mechanisms, allowing agents to adaptively filter information based on environmental changes, thereby enhancing their decision-making capabilities. Experiments on popular MARL benchmarks show that our framework can be seamlessly integrated with state-of-the-art algorithms, leading to significant performance improvements.

**Link**: [arxiv](http://arxiv.org/abs/2412.15639v1),  [pdf](http://arxiv.org/pdf/2412.15639v1)

**Tags**: cs.MA cs.AI cs.LG 



### Competition Dynamics Shape Algorithmic Phases of In-Context Learning
**Authors**: Core Francisco Park, Ekdeep Singh Lubana, Itamar Pres, Hidenori Tanaka

**Updated**: 2024-12-20T07:53:56Z

**Summary**: In-Context Learning (ICL) has significantly expanded the general-purpose nature of large language models, allowing them to adapt to novel tasks using merely the inputted context. This has motivated a series of papers that analyze tractable synthetic domains and postulate precise mechanisms that may underlie ICL. However, the use of relatively distinct setups that often lack a sequence modeling nature to them makes it unclear how general the reported insights from such studies are. Motivated by this, we propose a synthetic sequence modeling task that involves learning to simulate a finite mixture of Markov chains. As we show, models trained on this task reproduce most well-known results on ICL, hence offering a unified setting for studying the concept. Building on this setup, we demonstrate we can explain a model's behavior by decomposing it into four broad algorithms that combine a fuzzy retrieval vs. inference approach with either unigram or bigram statistics of the context. These algorithms engage in a competition dynamics to dominate model behavior, with the precise experimental conditions dictating which algorithm ends up superseding others: e.g., we find merely varying context size or amount of training yields (at times sharp) transitions between which algorithm dictates the model behavior, revealing a mechanism that explains the transient nature of ICL. In this sense, we argue ICL is best thought of as a mixture of different algorithms, each with its own peculiarities, instead of a monolithic capability. This also implies that making general claims about ICL that hold universally across all settings may be infeasible.

**Link**: [arxiv](http://arxiv.org/abs/2412.01003v2),  [pdf](http://arxiv.org/pdf/2412.01003v2)

**Tags**: cs.LG cs.CL 



### Darkit: A User-Friendly Software Toolkit for Spiking Large Language   Model
**Authors**: Xin Du, Shifan Ye, Qian Zheng, Yangfan Hu, Rui Yan, Shunyu Qi, Shuyang Chen, Huajin Tang, Gang Pan, Shuiguang Deng

**Updated**: 2024-12-20T07:50:08Z

**Summary**: Large language models (LLMs) have been widely applied in various practical applications, typically comprising billions of parameters, with inference processes requiring substantial energy and computational resources. In contrast, the human brain, employing bio-plausible spiking mechanisms, can accomplish the same tasks while significantly reducing energy consumption, even with a similar number of parameters. Based on this, several pioneering researchers have proposed and implemented various large language models that leverage spiking neural networks. They have demonstrated the feasibility of these models, validated their performance, and open-sourced their frameworks and partial source code. To accelerate the adoption of brain-inspired large language models and facilitate secondary development for researchers, we are releasing a software toolkit named DarwinKit (Darkit). The toolkit is designed specifically for learners, researchers, and developers working on spiking large models, offering a suite of highly user-friendly features that greatly simplify the learning, deployment, and development processes.

**Link**: [arxiv](http://arxiv.org/abs/2412.15634v1),  [pdf](http://arxiv.org/pdf/2412.15634v1)

**Tags**: cs.SE 



### DiveR-CT: Diversity-enhanced Red Teaming Large Language Model Assistants   with Relaxing Constraints
**Authors**: Andrew Zhao, Quentin Xu, Matthieu Lin, Shenzhi Wang, Yong-jin Liu, Zilong Zheng, Gao Huang

**Updated**: 2024-12-20T07:37:32Z

**Summary**: Recent advances in large language model assistants have made them indispensable, raising significant concerns over managing their safety. Automated red teaming offers a promising alternative to the labor-intensive and error-prone manual probing for vulnerabilities, providing more consistent and scalable safety evaluations. However, existing approaches often compromise diversity by focusing on maximizing attack success rate. Additionally, methods that decrease the cosine similarity from historical embeddings with semantic diversity rewards lead to novelty stagnation as history grows. To address these issues, we introduce DiveR-CT, which relaxes conventional constraints on the objective and semantic reward, granting greater freedom for the policy to enhance diversity. Our experiments demonstrate DiveR-CT's marked superiority over baselines by 1) generating data that perform better in various diversity metrics across different attack success rate levels, 2) better-enhancing resiliency in blue team models through safety tuning based on collected data, 3) allowing dynamic control of objective weights for reliable and controllable attack success rates, and 4) reducing susceptibility to reward overoptimization. Overall, our method provides an effective and efficient approach to LLM red teaming, accelerating real-world deployment.

**Link**: [arxiv](http://arxiv.org/abs/2405.19026v2),  [pdf](http://arxiv.org/pdf/2405.19026v2)

**Tags**: cs.LG cs.AI cs.CL cs.CR 



### Can Input Attributions Interpret the Inductive Reasoning Process   Elicited in In-Context Learning?
**Authors**: Mengyu Ye, Tatsuki Kuribayashi, Goro Kobayashi, Jun Suzuki

**Updated**: 2024-12-20T07:35:42Z

**Summary**: Elucidating the rationale behind neural models' outputs has been challenging in the machine learning field, which is indeed applicable in this age of large language models (LLMs) and in-context learning (ICL). When it comes to estimating input attributions (IA), ICL poses a new issue of interpreting which example in the prompt, consisting of a set of examples, contributed to identifying the task/rule to be solved. To this end, in this paper, we introduce synthetic diagnostic tasks inspired by the poverty of the stimulus design in inductive reasoning; here, most in-context examples are ambiguous w.r.t. their underlying rule, and one critical example disambiguates the task demonstrated. The question is whether conventional IA methods can identify such an example in interpreting the inductive reasoning process in ICL. Our experiments provide several practical findings; for example, a certain simple IA method works the best, and the larger the model, the generally harder it is to interpret the ICL with gradient-based IA methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.15628v1),  [pdf](http://arxiv.org/pdf/2412.15628v1)

**Tags**: cs.CL 



### JailPO: A Novel Black-box Jailbreak Framework via Preference   Optimization against Aligned LLMs
**Authors**: Hongyi Li, Jiawei Ye, Jie Wu, Tianjie Yan, Chu Wang, Zhixin Li

**Updated**: 2024-12-20T07:29:10Z

**Summary**: Large Language Models (LLMs) aligned with human feedback have recently garnered significant attention. However, it remains vulnerable to jailbreak attacks, where adversaries manipulate prompts to induce harmful outputs. Exploring jailbreak attacks enables us to investigate the vulnerabilities of LLMs and further guides us in enhancing their security. Unfortunately, existing techniques mainly rely on handcrafted templates or generated-based optimization, posing challenges in scalability, efficiency and universality. To address these issues, we present JailPO, a novel black-box jailbreak framework to examine LLM alignment. For scalability and universality, JailPO meticulously trains attack models to automatically generate covert jailbreak prompts. Furthermore, we introduce a preference optimization-based attack method to enhance the jailbreak effectiveness, thereby improving efficiency. To analyze model vulnerabilities, we provide three flexible jailbreak patterns. Extensive experiments demonstrate that JailPO not only automates the attack process while maintaining effectiveness but also exhibits superior performance in efficiency, universality, and robustness against defenses compared to baselines. Additionally, our analysis of the three JailPO patterns reveals that attacks based on complex templates exhibit higher attack strength, whereas covert question transformations elicit riskier responses and are more likely to bypass defense mechanisms.

**Link**: [arxiv](http://arxiv.org/abs/2412.15623v1),  [pdf](http://arxiv.org/pdf/2412.15623v1)

**Tags**: cs.CR cs.AI 



### Supercompliers
**Authors**: Matthew L. Comey, Amanda R. Eng, Pauline Leung, Zhuan Pei

**Updated**: 2024-12-20T07:22:32Z

**Summary**: In a binary-treatment instrumental variable framework, we define supercompliers as the subpopulation whose treatment take-up positively responds to eligibility and whose outcome positively responds to take-up. Supercompliers are the only subpopulation to benefit from treatment eligibility and, hence, are important for policy. We provide tools to characterize supercompliers under a set of jointly testable assumptions. Specifically, we require standard assumptions from the local average treatment effect literature plus an outcome monotonicity assumption. Estimation and inference can be conducted with instrumental variable regression. In two job-training experiments, we demonstrate our machinery's utility, particularly in incorporating social welfare weights into marginal-value-of-public-funds analysis.

**Link**: [arxiv](http://arxiv.org/abs/2212.14105v3),  [pdf](http://arxiv.org/pdf/2212.14105v3)

**Tags**: econ.EM 



### Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool   Usage
**Authors**: Zhi Gao, Bofei Zhang, Pengxiang Li, Xiaojian Ma, Tao Yuan, Yue Fan, Yuwei Wu, Yunde Jia, Song-Chun Zhu, Qing Li

**Updated**: 2024-12-20T07:00:46Z

**Summary**: The advancement of large language models (LLMs) prompts the development of multi-modal agents, which are used as a controller to call external tools, providing a feasible way to solve practical tasks. In this paper, we propose a multi-modal agent tuning method that automatically generates multi-modal tool-usage data and tunes a vision-language model (VLM) as the controller for powerful tool-usage reasoning. To preserve the data quality, we prompt the GPT-4o mini model to generate queries, files, and trajectories, followed by query-file and trajectory verifiers. Based on the data synthesis pipeline, we collect the MM-Traj dataset that contains 20K tasks with trajectories of tool usage. Then, we develop the T3-Agent via \underline{T}rajectory \underline{T}uning on VLMs for \underline{T}ool usage using MM-Traj. Evaluations on the GTA and GAIA benchmarks show that the T3-Agent consistently achieves improvements on two popular VLMs: MiniCPM-V-8.5B and {Qwen2-VL-7B}, which outperforms untrained VLMs by $20\%$, showing the effectiveness of the proposed data synthesis pipeline, leading to high-quality data for tool-usage capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2412.15606v1),  [pdf](http://arxiv.org/pdf/2412.15606v1)

**Tags**: cs.AI cs.CV 



## Keyword: LLM Deployment 
 ### HoVLE: Unleashing the Power of Monolithic Vision-Language Models with   Holistic Vision-Language Embedding
**Authors**: Chenxin Tao, Shiqian Su, Xizhou Zhu, Chenyu Zhang, Zhe Chen, Jiawen Liu, Wenhai Wang, Lewei Lu, Gao Huang, Yu Qiao, Jifeng Dai

**Updated**: 2024-12-20T18:59:59Z

**Summary**: The rapid advance of Large Language Models (LLMs) has catalyzed the development of Vision-Language Models (VLMs). Monolithic VLMs, which avoid modality-specific encoders, offer a promising alternative to the compositional ones but face the challenge of inferior performance. Most existing monolithic VLMs require tuning pre-trained LLMs to acquire vision abilities, which may degrade their language capabilities. To address this dilemma, this paper presents a novel high-performance monolithic VLM named HoVLE. We note that LLMs have been shown capable of interpreting images, when image embeddings are aligned with text embeddings. The challenge for current monolithic VLMs actually lies in the lack of a holistic embedding module for both vision and language inputs. Therefore, HoVLE introduces a holistic embedding module that converts visual and textual inputs into a shared space, allowing LLMs to process images in the same way as texts. Furthermore, a multi-stage training strategy is carefully designed to empower the holistic embedding module. It is first trained to distill visual features from a pre-trained vision encoder and text embeddings from the LLM, enabling large-scale training with unpaired random images and text tokens. The whole model further undergoes next-token prediction on multi-modal data to align the embeddings. Finally, an instruction-tuning stage is incorporated. Our experiments show that HoVLE achieves performance close to leading compositional models on various benchmarks, outperforming previous monolithic models by a large margin. Model available at https://huggingface.co/OpenGVLab/HoVLE.

**Link**: [arxiv](http://arxiv.org/abs/2412.16158v1),  [pdf](http://arxiv.org/pdf/2412.16158v1)

**Tags**: cs.CV 



### Offline Reinforcement Learning for LLM Multi-Step Reasoning
**Authors**: Huaijie Wang, Shibo Hao, Hanze Dong, Shenao Zhang, Yilin Bao, Ziran Yang, Yi Wu

**Updated**: 2024-12-20T18:49:45Z

**Summary**: Improving the multi-step reasoning ability of large language models (LLMs) with offline reinforcement learning (RL) is essential for quickly adapting them to complex tasks. While Direct Preference Optimization (DPO) has shown promise in aligning LLMs with human preferences, it is less suitable for multi-step reasoning tasks because (1) DPO relies on paired preference data, which is not readily available for multi-step reasoning tasks, and (2) it treats all tokens uniformly, making it ineffective for credit assignment in multi-step reasoning tasks, which often come with sparse reward. In this work, we propose OREO (Offline Reasoning Optimization), an offline RL method for enhancing LLM multi-step reasoning. Building on insights from previous works of maximum entropy reinforcement learning, it jointly learns a policy model and value function by optimizing the soft Bellman Equation. We show in principle that it reduces the need to collect pairwise data and enables better credit assignment. Empirically, OREO surpasses existing offline learning methods on multi-step reasoning benchmarks, including mathematical reasoning tasks (GSM8K, MATH) and embodied agent control (ALFWorld). The approach can be extended to a multi-iteration framework when additional resources are available. Furthermore, the learned value function can be leveraged to guide the tree search for free, which can further boost performance during test time.

**Link**: [arxiv](http://arxiv.org/abs/2412.16145v1),  [pdf](http://arxiv.org/pdf/2412.16145v1)

**Tags**: cs.LG cs.AI cs.CL 



### Can LLMs Obfuscate Code? A Systematic Analysis of Large Language Models   into Assembly Code Obfuscation
**Authors**: Seyedreza Mohseni, Seyedali Mohammadi, Deepa Tilwani, Yash Saxena, Gerald Ndwula, Sriram Vema, Edward Raff, Manas Gaur

**Updated**: 2024-12-20T18:31:24Z

**Summary**: Malware authors often employ code obfuscations to make their malware harder to detect. Existing tools for generating obfuscated code often require access to the original source code (e.g., C++ or Java), and adding new obfuscations is a non-trivial, labor-intensive process. In this study, we ask the following question: Can Large Language Models (LLMs) potentially generate a new obfuscated assembly code? If so, this poses a risk to anti-virus engines and potentially increases the flexibility of attackers to create new obfuscation patterns. We answer this in the affirmative by developing the MetamorphASM benchmark comprising MetamorphASM Dataset (MAD) along with three code obfuscation techniques: dead code, register substitution, and control flow change. The MetamorphASM systematically evaluates the ability of LLMs to generate and analyze obfuscated code using MAD, which contains 328,200 obfuscated assembly code samples. We release this dataset and analyze the success rate of various LLMs (e.g., GPT-3.5/4, GPT-4o-mini, Starcoder, CodeGemma, CodeLlama, CodeT5, and LLaMA 3.1) in generating obfuscated assembly code. The evaluation was performed using established information-theoretic metrics and manual human review to ensure correctness and provide the foundation for researchers to study and develop remediations to this risk. The source code can be found at the following GitHub link: https://github.com/mohammadi-ali/MetamorphASM.

**Link**: [arxiv](http://arxiv.org/abs/2412.16135v1),  [pdf](http://arxiv.org/pdf/2412.16135v1)

**Tags**: cs.CR cs.AI cs.CL 



### Data-Driven Mechanism Design: Jointly Eliciting Preferences and   Information
**Authors**: Dirk Bergemann, Marek Bojko, Paul Dütting, Renato Paes Leme, Haifeng Xu, Song Zuo

**Updated**: 2024-12-20T18:29:49Z

**Summary**: We study mechanism design when agents hold private information about both their preferences and a common payoff-relevant state. We show that standard message-driven mechanisms cannot implement socially efficient allocations when agents have multidimensional types, even under favorable conditions. To overcome this limitation, we propose data-driven mechanisms that leverage additional post-allocation information, modeled as an estimator of the payoff-relevant state. Our data-driven mechanisms extend the classic Vickrey-Clarke-Groves class. We show that they achieve exact implementation in posterior equilibrium when the state is either fully revealed or the utility is linear in an unbiased estimator. We also show that they achieve approximate implementation with a consistent estimator, converging to exact implementation as the estimator converges, and present bounds on the convergence rate. We demonstrate applications to digital advertising auctions and large language model (LLM)-based mechanisms, where user engagement naturally reveals relevant information.

**Link**: [arxiv](http://arxiv.org/abs/2412.16132v1),  [pdf](http://arxiv.org/pdf/2412.16132v1)

**Tags**: econ.TH cs.GT 



### What is the Role of Small Models in the LLM Era: A Survey
**Authors**: Lihu Chen, Gaël Varoquaux

**Updated**: 2024-12-20T18:11:41Z

**Summary**: Large Language Models (LLMs) have made significant progress in advancing artificial general intelligence (AGI), leading to the development of increasingly large models such as GPT-4 and LLaMA-405B. However, scaling up model sizes results in exponentially higher computational costs and energy consumption, making these models impractical for academic researchers and businesses with limited resources. At the same time, Small Models (SMs) are frequently used in practical settings, although their significance is currently underestimated. This raises important questions about the role of small models in the era of LLMs, a topic that has received limited attention in prior research. In this work, we systematically examine the relationship between LLMs and SMs from two key perspectives: Collaboration and Competition. We hope this survey provides valuable insights for practitioners, fostering a deeper understanding of the contribution of small models and promoting more efficient use of computational resources. The code is available at https://github.com/tigerchen52/role_of_small_models

**Link**: [arxiv](http://arxiv.org/abs/2409.06857v4),  [pdf](http://arxiv.org/pdf/2409.06857v4)

**Tags**: cs.CL 



### PromptOptMe: Error-Aware Prompt Compression for LLM-based MT Evaluation   Metrics
**Authors**: Daniil Larionov, Steffen Eger

**Updated**: 2024-12-20T18:08:02Z

**Summary**: Evaluating the quality of machine-generated natural language content is a challenging task in Natural Language Processing (NLP). Recently, large language models (LLMs) like GPT-4 have been employed for this purpose, but they are computationally expensive due to the extensive token usage required by complex evaluation prompts. In this paper, we propose a prompt optimization approach that uses a smaller, fine-tuned language model to compress input data for evaluation prompt, thus reducing token usage and computational cost when using larger LLMs for downstream evaluation. Our method involves a two-stage fine-tuning process: supervised fine-tuning followed by preference optimization to refine the model's outputs based on human preferences. We focus on Machine Translation (MT) evaluation and utilize the GEMBA-MQM metric as a starting point. Our results show a $2.37\times$ reduction in token usage without any loss in evaluation quality. This work makes state-of-the-art LLM-based metrics like GEMBA-MQM more cost-effective and efficient, enhancing their accessibility for broader use.

**Link**: [arxiv](http://arxiv.org/abs/2412.16120v1),  [pdf](http://arxiv.org/pdf/2412.16120v1)

**Tags**: cs.CL 



### Deciphering the Underserved: Benchmarking LLM OCR for Low-Resource   Scripts
**Authors**: Muhammad Abdullah Sohail, Salaar Masood, Hamza Iqbal

**Updated**: 2024-12-20T18:05:22Z

**Summary**: This study investigates the potential of Large Language Models (LLMs), particularly GPT-4o, for Optical Character Recognition (OCR) in low-resource scripts such as Urdu, Albanian, and Tajik, with English serving as a benchmark. Using a meticulously curated dataset of 2,520 images incorporating controlled variations in text length, font size, background color, and blur, the research simulates diverse real-world challenges. Results emphasize the limitations of zero-shot LLM-based OCR, particularly for linguistically complex scripts, highlighting the need for annotated datasets and fine-tuned models. This work underscores the urgency of addressing accessibility gaps in text digitization, paving the way for inclusive and robust OCR solutions for underserved languages.

**Link**: [arxiv](http://arxiv.org/abs/2412.16119v1),  [pdf](http://arxiv.org/pdf/2412.16119v1)

**Tags**: cs.LG cs.CV eess.IV 



### PruneVid: Visual Token Pruning for Efficient Video Large Language Models
**Authors**: Xiaohu Huang, Hao Zhou, Kai Han

**Updated**: 2024-12-20T18:01:58Z

**Summary**: In this paper, we introduce PruneVid, a visual token pruning method designed to enhance the efficiency of multi-modal video understanding. Large Language Models (LLMs) have shown promising performance in video tasks due to their extended capabilities in comprehending visual modalities. However, the substantial redundancy in video data presents significant computational challenges for LLMs. To address this issue, we introduce a training-free method that 1) minimizes video redundancy by merging spatial-temporal tokens, and 2) leverages LLMs' reasoning capabilities to selectively prune visual features relevant to question tokens, enhancing model efficiency. We validate our method across multiple video benchmarks, which demonstrate that PruneVid can prune over 80% of tokens while maintaining competitive performance combined with different model networks. This highlights its superior effectiveness and efficiency compared to existing pruning methods. Code: https://github.com/Visual-AI/PruneVid.

**Link**: [arxiv](http://arxiv.org/abs/2412.16117v1),  [pdf](http://arxiv.org/pdf/2412.16117v1)

**Tags**: cs.CV 



### Logical Consistency of Large Language Models in Fact-checking
**Authors**: Bishwamittra Ghosh, Sarah Hasan, Naheed Anjum Arafat, Arijit Khan

**Updated**: 2024-12-20T17:42:25Z

**Summary**: In recent years, large language models (LLMs) have demonstrated significant success in performing varied natural language tasks such as language translation, question-answering, summarizing, fact-checking, etc. Despite LLMs' impressive ability to generate human-like texts, LLMs are infamous for their inconsistent responses -- a meaning-preserving change in the input query results in an inconsistent response and attributes to vulnerabilities of LLMs such as hallucination, jailbreaking, etc. Consequently, existing research focuses on simple paraphrasing-based consistency assessment of LLMs, and ignores complex queries that necessitates an even better understanding of logical reasoning by an LLM. Our work therefore addresses the logical inconsistency of LLMs under complex logical queries with primitive logical operators, e.g., negation, conjunction, and disjunction. As a test bed, we consider retrieval-augmented LLMs on a fact-checking task involving propositional logic queries from real-world knowledge graphs (KGs). Our contributions are three-fold. Benchmark: We introduce three logical fact-checking datasets over KGs for community development towards logically consistent LLMs. Assessment: We propose consistency measures of LLMs on propositional logic queries as input and demonstrate that existing LLMs lack logical consistency, specially on complex queries. Improvement: We employ supervised fine-tuning to improve the logical consistency of LLMs on the complex fact-checking task with KG contexts.

**Link**: [arxiv](http://arxiv.org/abs/2412.16100v1),  [pdf](http://arxiv.org/pdf/2412.16100v1)

**Tags**: cs.CL 



### Dual-Polarized Beyond Diagonal RIS
**Authors**: Matteo Nerini, Bruno Clerckx

**Updated**: 2024-12-20T17:41:02Z

**Summary**: Beyond diagonal reconfigurable intelligent surface (BD-RIS) is a family of RIS architectures more flexible than conventional RIS. While BD-RIS has been primarily analyzed assuming uni-polarized systems, modern wireless deployments are dual-polarized. To address this gap, this paper investigates the fundamental limits of dual-polarized BD-RIS-aided systems. We derive the scaling laws governing the performance of BD-RIS and the Pareto frontier of the trade-off between performance and circuit complexity enabled by BD-RIS. Theoretical results show that the group-connected RIS with group size 2 provides remarkable gains over conventional RIS in both Rayleigh and line-of-sight (LoS) channels, while maintaining a reduced circuit complexity.

**Link**: [arxiv](http://arxiv.org/abs/2412.16097v1),  [pdf](http://arxiv.org/pdf/2412.16097v1)

**Tags**: cs.IT eess.SP math.IT 



### The Evolution of LLM Adoption in Industry Data Curation Practices
**Authors**: Crystal Qian, Michael Xieyang Liu, Emily Reif, Grady Simon, Nada Hussein, Nathan Clement, James Wexler, Carrie J. Cai, Michael Terry, Minsuk Kahng

**Updated**: 2024-12-20T17:34:16Z

**Summary**: As large language models (LLMs) grow increasingly adept at processing unstructured text data, they offer new opportunities to enhance data curation workflows. This paper explores the evolution of LLM adoption among practitioners at a large technology company, evaluating the impact of LLMs in data curation tasks through participants' perceptions, integration strategies, and reported usage scenarios. Through a series of surveys, interviews, and user studies, we provide a timely snapshot of how organizations are navigating a pivotal moment in LLM evolution. In Q2 2023, we conducted a survey to assess LLM adoption in industry for development tasks (N=84), and facilitated expert interviews to assess evolving data needs (N=10) in Q3 2023. In Q2 2024, we explored practitioners' current and anticipated LLM usage through a user study involving two LLM-based prototypes (N=12). While each study addressed distinct research goals, they revealed a broader narrative about evolving LLM usage in aggregate. We discovered an emerging shift in data understanding from heuristic-first, bottom-up approaches to insights-first, top-down workflows supported by LLMs. Furthermore, to respond to a more complex data landscape, data practitioners now supplement traditional subject-expert-created 'golden datasets' with LLM-generated 'silver' datasets and rigorously validated 'super golden' datasets curated by diverse experts. This research sheds light on the transformative role of LLMs in large-scale analysis of unstructured data and highlights opportunities for further tool development.

**Link**: [arxiv](http://arxiv.org/abs/2412.16089v1),  [pdf](http://arxiv.org/pdf/2412.16089v1)

**Tags**: cs.HC cs.AI 



### Towards Interpretable Radiology Report Generation via Concept   Bottlenecks using a Multi-Agentic RAG
**Authors**: Hasan Md Tusfiqur Alam, Devansh Srivastav, Md Abdul Kadir, Daniel Sonntag

**Updated**: 2024-12-20T17:33:50Z

**Summary**: Deep learning has advanced medical image classification, but interpretability challenges hinder its clinical adoption. This study enhances interpretability in Chest X-ray (CXR) classification by using concept bottleneck models (CBMs) and a multi-agent Retrieval-Augmented Generation (RAG) system for report generation. By modeling relationships between visual features and clinical concepts, we create interpretable concept vectors that guide a multi-agent RAG system to generate radiology reports, enhancing clinical relevance, explainability, and transparency. Evaluation of the generated reports using an LLM-as-a-judge confirmed the interpretability and clinical utility of our model's outputs. On the COVID-QU dataset, our model achieved 81% classification accuracy and demonstrated robust report generation performance, with five key metrics ranging between 84% and 90%. This interpretable multi-agent framework bridges the gap between high-performance AI and the explainability required for reliable AI-driven CXR analysis in clinical settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.16086v1),  [pdf](http://arxiv.org/pdf/2412.16086v1)

**Tags**: cs.IR cs.AI cs.CL cs.CV eess.IV 



### Magnetic Preference Optimization: Achieving Last-iterate Convergence for   Language Model Alignment
**Authors**: Mingzhi Wang, Chengdong Ma, Qizhi Chen, Linjian Meng, Yang Han, Jiancong Xiao, Zhaowei Zhang, Jing Huo, Weijie J. Su, Yaodong Yang

**Updated**: 2024-12-20T16:26:58Z

**Summary**: Self-play methods have demonstrated remarkable success in enhancing model capabilities across various domains. In the context of Reinforcement Learning from Human Feedback (RLHF), self-play not only boosts Large Language Model (LLM) performance but also overcomes the limitations of traditional Bradley-Terry (BT) model assumptions by finding the Nash equilibrium (NE) of a preference-based, two-player constant-sum game. However, existing methods either guarantee only average-iterate convergence, incurring high storage and inference costs, or converge to the NE of a regularized game, failing to accurately reflect true human preferences. In this paper, we introduce Magnetic Preference Optimization (MPO), a novel approach capable of achieving last-iterate convergence to the NE of the original game, effectively overcoming the limitations of existing methods. Building upon Magnetic Mirror Descent (MMD), MPO attains a linear convergence rate, making it particularly suitable for fine-tuning LLMs. To ensure our algorithm is both theoretically sound and practically viable, we present a simple yet effective implementation that adapts the theoretical insights to the RLHF setting. Empirical results demonstrate that MPO can significantly enhance the performance of LLMs, highlighting the potential of self-play methods in alignment.

**Link**: [arxiv](http://arxiv.org/abs/2410.16714v2),  [pdf](http://arxiv.org/pdf/2410.16714v2)

**Tags**: cs.CL 



### Language Models Resist Alignment: Evidence From Data Compression
**Authors**: Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Josef Dai, Yunhuai Liu, Yaodong Yang

**Updated**: 2024-12-20T16:25:12Z

**Summary**: Large language models (LLMs) may exhibit unintended or undesirable behaviors. Recent works have concentrated on aligning LLMs to mitigate harmful outputs. Despite these efforts, some anomalies indicate that even a well-conducted alignment process can be easily circumvented, whether intentionally or accidentally. Does alignment fine-tuning yield have robust effects on models, or are its impacts merely superficial? In this work, we make the first exploration of this phenomenon from both theoretical and empirical perspectives. Empirically, we demonstrate the elasticity of post-alignment models, i.e., the tendency to revert to the behavior distribution formed during the pre-training phase upon further fine-tuning. Leveraging compression theory, we formally deduce that fine-tuning disproportionately undermines alignment relative to pre-training, potentially by orders of magnitude. We validate the presence of elasticity through experiments on models of varying types and scales. Specifically, we find that model performance declines rapidly before reverting to the pre-training distribution, after which the rate of decline drops significantly. Furthermore, we further reveal that elasticity positively correlates with the increased model size and the expansion of pre-training data. Our findings underscore the need to address the inherent elasticity of LLMs to mitigate their resistance to alignment.

**Link**: [arxiv](http://arxiv.org/abs/2406.06144v3),  [pdf](http://arxiv.org/pdf/2406.06144v3)

**Tags**: cs.CL cs.AI 



### The Only Way is Ethics: A Guide to Ethical Research with Large Language   Models
**Authors**: Eddie L. Ungless, Nikolas Vitsakis, Zeerak Talat, James Garforth, Björn Ross, Arno Onken, Atoosa Kasirzadeh, Alexandra Birch

**Updated**: 2024-12-20T16:14:43Z

**Summary**: There is a significant body of work looking at the ethical considerations of large language models (LLMs): critiquing tools to measure performance and harms; proposing toolkits to aid in ideation; discussing the risks to workers; considering legislation around privacy and security etc. As yet there is no work that integrates these resources into a single practical guide that focuses on LLMs; we attempt this ambitious goal. We introduce 'LLM Ethics Whitepaper', which we provide as an open and living resource for NLP practitioners, and those tasked with evaluating the ethical implications of others' work. Our goal is to translate ethics literature into concrete recommendations and provocations for thinking with clear first steps, aimed at computer scientists. 'LLM Ethics Whitepaper' distils a thorough literature review into clear Do's and Don'ts, which we present also in this paper. We likewise identify useful toolkits to support ethical work. We refer the interested reader to the full LLM Ethics Whitepaper, which provides a succinct discussion of ethical considerations at each stage in a project lifecycle, as well as citations for the hundreds of papers from which we drew our recommendations. The present paper can be thought of as a pocket guide to conducting ethical research with LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.16022v1),  [pdf](http://arxiv.org/pdf/2412.16022v1)

**Tags**: cs.CL cs.AI 



### All-in-One Tuning and Structural Pruning for Domain-Specific LLMs
**Authors**: Lei Lu, Zhepeng Wang, Runxue Bao, Mengbing Wang, Fangyi Li, Yawen Wu, Weiwen Jiang, Jie Xu, Yanzhi Wang, Shangqian Gao

**Updated**: 2024-12-20T15:57:10Z

**Summary**: Existing pruning techniques for large language models (LLMs) targeting domain-specific applications typically follow a two-stage process: pruning the pretrained general-purpose LLMs and then fine-tuning the pruned LLMs on specific domains. However, the pruning decisions, derived from the pretrained weights, remain unchanged during fine-tuning, even if the weights have been updated. Therefore, such a combination of the pruning decisions and the finetuned weights may be suboptimal, leading to non-negligible performance degradation. To address these limitations, we propose ATP: All-in-One Tuning and Structural Pruning, a unified one-stage structural pruning and fine-tuning approach that dynamically identifies the current optimal substructure throughout the fine-tuning phase via a trainable pruning decision generator. Moreover, given the limited available data for domain-specific applications, Low-Rank Adaptation (LoRA) becomes a common technique to fine-tune the LLMs. In ATP, we introduce LoRA-aware forward and sparsity regularization to ensure that the substructures corresponding to the learned pruning decisions can be directly removed after the ATP process. ATP outperforms the state-of-the-art two-stage pruning methods on tasks in the legal and healthcare domains. More specifically, ATP recovers up to 88% and 91% performance of the dense model when pruning 40% parameters of LLaMA2-7B and LLaMA3-8B models, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2412.14426v2),  [pdf](http://arxiv.org/pdf/2412.14426v2)

**Tags**: cs.CL cs.AI 



### Detection of Aerial Spoofing Attacks to LEO Satellite Systems via Deep   Learning
**Authors**: Jos Wigchert, Savio Sciancalepore, Gabriele Oligeri

**Updated**: 2024-12-20T15:56:09Z

**Summary**: Detecting spoofing attacks to Low-Earth-Orbit (LEO) satellite systems is a cornerstone to assessing the authenticity of the received information and guaranteeing robust service delivery in several application domains. The solutions available today for spoofing detection either rely on additional communication systems, receivers, and antennas, or require mobile deployments. Detection systems working at the Physical (PHY) layer of the satellite communication link also require time-consuming and energy-hungry training processes on all satellites of the constellation, and rely on the availability of spoofed data, which are often challenging to collect. Moreover, none of such contributions investigate the feasibility of aerial spoofing attacks launched via drones operating at various altitudes. In this paper, we propose a new spoofing detection technique for LEO satellite constellation systems, applying anomaly detection on the received PHY signal via autoencoders. We validate our solution through an extensive measurement campaign involving the deployment of an actual spoofer (Software-Defined Radio) installed on a drone and injecting rogue IRIDIUM messages while flying at different altitudes with various movement patterns. Our results demonstrate that the proposed technique can reliably detect LEO spoofing attacks launched at different altitudes, while state-of-the-art competing approaches simply fail. We also release the collected data as open source, fostering further research on satellite security.

**Link**: [arxiv](http://arxiv.org/abs/2412.16008v1),  [pdf](http://arxiv.org/pdf/2412.16008v1)

**Tags**: cs.CR 



### Fearful Falcons and Angry Llamas: Emotion Category Annotations of   Arguments by Humans and LLMs
**Authors**: Lynn Greschner, Roman Klinger

**Updated**: 2024-12-20T15:41:47Z

**Summary**: Arguments evoke emotions, influencing the effect of the argument itself. Not only the emotional intensity but also the category influence the argument's effects, for instance, the willingness to adapt stances. While binary emotionality has been studied in arguments, there is no work on discrete emotion categories (e.g., "Anger") in such data. To fill this gap, we crowdsource subjective annotations of emotion categories in a German argument corpus and evaluate automatic LLM-based labeling methods. Specifically, we compare three prompting strategies (zero-shot, one-shot, chain-of-thought) on three large instruction-tuned language models (Falcon-7b-instruct, Llama-3.1-8B-instruct, GPT-4o-mini). We further vary the definition of the output space to be binary (is there emotionality in the argument?), closed-domain (which emotion from a given label set is in the argument?), or open-domain (which emotion is in the argument?). We find that emotion categories enhance the prediction of emotionality in arguments, emphasizing the need for discrete emotion annotations in arguments. Across all prompt settings and models, automatic predictions show a high recall but low precision for predicting anger and fear, indicating a strong bias toward negative emotions.

**Link**: [arxiv](http://arxiv.org/abs/2412.15993v1),  [pdf](http://arxiv.org/pdf/2412.15993v1)

**Tags**: cs.CL 



### Improving Factuality in Large Language Models via Decoding-Time   Hallucinatory and Truthful Comparators
**Authors**: Dingkang Yang, Dongling Xiao, Jinjie Wei, Mingcheng Li, Zhaoyu Chen, Ke Li, Lihua Zhang

**Updated**: 2024-12-20T15:26:33Z

**Summary**: Despite their remarkable capabilities, Large Language Models (LLMs) are prone to generate responses that contradict verifiable facts, i.e., unfaithful hallucination content. Existing efforts generally focus on optimizing model parameters or editing semantic representations, which compromise the internal factual knowledge of target LLMs. In addition, hallucinations typically exhibit multifaceted patterns in downstream tasks, limiting the model's holistic performance across tasks. In this paper, we propose a Comparator-driven Decoding-Time (CDT) framework to alleviate the response hallucination. Firstly, we construct hallucinatory and truthful comparators with multi-task fine-tuning samples. In this case, we present an instruction prototype-guided mixture of experts strategy to enhance the ability of the corresponding comparators to capture different hallucination or truthfulness patterns in distinct task instructions. CDT constrains next-token predictions to factuality-robust distributions by contrasting the logit differences between the target LLMs and these comparators. Systematic experiments on multiple downstream tasks show that our framework can significantly improve the model performance and response factuality.

**Link**: [arxiv](http://arxiv.org/abs/2408.12325v4),  [pdf](http://arxiv.org/pdf/2408.12325v4)

**Tags**: cs.CL 



### Legommenders: A Comprehensive Content-Based Recommendation Library with   LLM Support
**Authors**: Qijiong Liu, Lu Fan, Xiao-Ming Wu

**Updated**: 2024-12-20T15:18:02Z

**Summary**: We present Legommenders, a unique library designed for content-based recommendation that enables the joint training of content encoders alongside behavior and interaction modules, thereby facilitating the seamless integration of content understanding directly into the recommendation pipeline. Legommenders allows researchers to effortlessly create and analyze over 1,000 distinct models across 15 diverse datasets. Further, it supports the incorporation of contemporary large language models, both as feature encoder and data generator, offering a robust platform for developing state-of-the-art recommendation models and enabling more personalized and effective content delivery.

**Link**: [arxiv](http://arxiv.org/abs/2412.15973v1),  [pdf](http://arxiv.org/pdf/2412.15973v1)

**Tags**: cs.IR 



### Recent Advances in Named Entity Recognition: A Comprehensive Survey and   Comparative Study
**Authors**: Imed Keraghel, Stanislas Morbieu, Mohamed Nadif

**Updated**: 2024-12-20T15:11:13Z

**Summary**: Named Entity Recognition seeks to extract substrings within a text that name real-world objects and to determine their type (for example, whether they refer to persons or organizations). In this survey, we first present an overview of recent popular approaches, including advancements in Transformer-based methods and Large Language Models (LLMs) that have not had much coverage in other surveys. In addition, we discuss reinforcement learning and graph-based approaches, highlighting their role in enhancing NER performance. Second, we focus on methods designed for datasets with scarce annotations. Third, we evaluate the performance of the main NER implementations on a variety of datasets with differing characteristics (as regards their domain, their size, and their number of classes). We thus provide a deep comparison of algorithms that have never been considered together. Our experiments shed some light on how the characteristics of datasets affect the behavior of the methods we compare.

**Link**: [arxiv](http://arxiv.org/abs/2401.10825v3),  [pdf](http://arxiv.org/pdf/2401.10825v3)

**Tags**: cs.CL cs.LG 68T50, 68Q32 



### ChinaTravel: A Real-World Benchmark for Language Agents in Chinese   Travel Planning
**Authors**: Jie-Jing Shao, Xiao-Wen Yang, Bo-Wen Zhang, Baizhi Chen, Wen-Da Wei, Guohao Cai, Zhenhua Dong, Lan-Zhe Guo, Yu-feng Li

**Updated**: 2024-12-20T15:08:25Z

**Summary**: Recent advances in LLMs, particularly in language reasoning and tool integration, have rapidly sparked the real-world development of Language Agents. Among these, travel planning represents a prominent domain, combining academic challenges with practical value due to its complexity and market demand. However, existing benchmarks fail to reflect the diverse, real-world requirements crucial for deployment. To address this gap, we introduce ChinaTravel, a benchmark specifically designed for authentic Chinese travel planning scenarios. We collect the travel requirements from questionnaires and propose a compositionally generalizable domain-specific language that enables a scalable evaluation process, covering feasibility, constraint satisfaction, and preference comparison. Empirical studies reveal the potential of neuro-symbolic agents in travel planning, achieving a constraint satisfaction rate of 27.9%, significantly surpassing purely neural models at 2.6%. Moreover, we identify key challenges in real-world travel planning deployments, including open language reasoning and unseen concept composition. These findings highlight the significance of ChinaTravel as a pivotal milestone for advancing language agents in complex, real-world planning scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2412.13682v2),  [pdf](http://arxiv.org/pdf/2412.13682v2)

**Tags**: cs.AI cs.CL 



### Language Repository for Long Video Understanding
**Authors**: Kumara Kahatapitiya, Kanchana Ranasinghe, Jongwoo Park, Michael S. Ryoo

**Updated**: 2024-12-20T15:06:14Z

**Summary**: Language has become a prominent modality in computer vision with the rise of LLMs. Despite supporting long context-lengths, their effectiveness in handling long-term information gradually declines with input length. This becomes critical, especially in applications such as long-form video understanding. In this paper, we introduce a Language Repository (LangRepo) for LLMs, that maintains concise and structured information as an interpretable (i.e., all-textual) representation. Our repository is updated iteratively based on multi-scale video chunks. We introduce write and read operations that focus on pruning redundancies in text, and extracting information at various temporal scales. The proposed framework is evaluated on zero-shot visual question-answering benchmarks including EgoSchema, NExT-QA, IntentQA and NExT-GQA, showing state-of-the-art performance at its scale. Our code is available at https://github.com/kkahatapitiya/LangRepo.

**Link**: [arxiv](http://arxiv.org/abs/2403.14622v2),  [pdf](http://arxiv.org/pdf/2403.14622v2)

**Tags**: cs.CV 



### FullStack Bench: Evaluating LLMs as Full Stack Coders
**Authors**: Bytedance-Seed-Foundation-Code-Team, :, Yao Cheng, Jianfeng Chen, Jie Chen, Li Chen, Liyu Chen, Wentao Chen, Zhengyu Chen, Shijie Geng, Aoyan Li, Bo Li, Bowen Li, Linyi Li, Boyi Liu, Jerry Liu, Kaibo Liu, Qi Liu, Shukai Liu, Siyao Liu, Tianyi Liu, Tingkai Liu, Yongfei Liu, Rui Long, Jing Mai, Guanghan Ning, Z. Y. Peng, Kai Shen, Jiahao Su, Jing Su, Tao Sun, Yifan Sun, Yunzhe Tao, Guoyin Wang, Siwei Wang, Xuwu Wang, Yite Wang, Zihan Wang, Jinxiang Xia, Liang Xiang, Xia Xiao, Yongsheng Xiao, Chenguang Xi, Shulin Xin, Jingjing Xu, Shikun Xu, Hongxia Yang, Jack Yang, Yingxiang Yang, Jianbo Yuan, Jun Zhang, Yufeng Zhang, Yuyu Zhang, Shen Zheng, He Zhu, Ming Zhu

**Updated**: 2024-12-20T14:58:59Z

**Summary**: As the capabilities of code large language models (LLMs) continue to expand, their applications across diverse code intelligence domains are rapidly increasing. However, most existing datasets only evaluate limited application domains. To address this gap, we have developed a comprehensive code evaluation dataset FullStack Bench focusing on full-stack programming, which encompasses a wide range of application domains (e.g., basic programming, data analysis, software engineering, mathematics, and machine learning). Besides, to assess multilingual programming capabilities, in FullStack Bench, we design real-world instructions and corresponding unit test cases from 16 widely-used programming languages to reflect real-world usage scenarios rather than simple translations. Moreover, we also release an effective code sandbox execution tool (i.e., SandboxFusion) supporting various programming languages and packages to evaluate the performance of our FullStack Bench efficiently. Comprehensive experimental results on our FullStack Bench demonstrate the necessity and effectiveness of our FullStack Bench and SandboxFusion.

**Link**: [arxiv](http://arxiv.org/abs/2412.00535v5),  [pdf](http://arxiv.org/pdf/2412.00535v5)

**Tags**: cs.AI cs.SE 



### From General to Specific: Tailoring Large Language Models for   Personalized Healthcare
**Authors**: Ruize Shi, Hong Huang, Wei Zhou, Kehan Yin, Kai Zhao, Yun Zhao

**Updated**: 2024-12-20T14:51:12Z

**Summary**: The rapid development of large language models (LLMs) has transformed many industries, including healthcare. However, previous medical LLMs have largely focused on leveraging general medical knowledge to provide responses, without accounting for patient variability and lacking true personalization at the individual level. To address this, we propose a novel method called personalized medical language model (PMLM), which explores and optimizes personalized LLMs through recommendation systems and reinforcement learning (RL). Specifically, by utilizing self-informed and peer-informed personalization, PMLM captures changes in behaviors and preferences to design initial personalized prompts tailored to individual needs. We further refine these initial personalized prompts through RL, ultimately enhancing the precision of LLM guidance. Notably, the personalized prompt are hard prompt, which grants PMLM high adaptability and reusability, allowing it to directly leverage high-quality proprietary LLMs. We evaluate PMLM using real-world obstetrics and gynecology data, and the experimental results demonstrate that PMLM achieves personalized responses, and it provides more refined and individualized services, offering a potential way for personalized medical LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.15957v1),  [pdf](http://arxiv.org/pdf/2412.15957v1)

**Tags**: cs.CL cs.AI cs.IR 



### Trust Calibration in IDEs: Paving the Way for Widespread Adoption of AI   Refactoring
**Authors**: Markus Borg

**Updated**: 2024-12-20T14:44:11Z

**Summary**: In the software industry, the drive to add new features often overshadows the need to improve existing code. Large Language Models (LLMs) offer a new approach to improving codebases at an unprecedented scale through AI-assisted refactoring. However, LLMs come with inherent risks such as braking changes and the introduction of security vulnerabilities. We advocate for encapsulating the interaction with the models in IDEs and validating refactoring attempts using trustworthy safeguards. However, equally important for the uptake of AI refactoring is research on trust development. In this position paper, we position our future work based on established models from research on human factors in automation. We outline action research within CodeScene on development of 1) novel LLM safeguards and 2) user interaction that conveys an appropriate level of trust. The industry collaboration enables large-scale repository analysis and A/B testing to continuously guide the design of our research interventions.

**Link**: [arxiv](http://arxiv.org/abs/2412.15948v1),  [pdf](http://arxiv.org/pdf/2412.15948v1)

**Tags**: cs.SE cs.AI cs.HC 



### Large Language Model assisted Hybrid Fuzzing
**Authors**: Ruijie Meng, Gregory J. Duck, Abhik Roychoudhury

**Updated**: 2024-12-20T14:23:25Z

**Summary**: Greybox fuzzing is one of the most popular methods for detecting software vulnerabilities, which conducts a biased random search within the program input space. To enhance its effectiveness in achieving deep coverage of program behaviors, greybox fuzzing is often combined with concolic execution, which performs a path-sensitive search over the domain of program inputs. In hybrid fuzzing, conventional greybox fuzzing is followed by concolic execution in an iterative loop, where reachability roadblocks encountered by greybox fuzzing are tackled by concolic execution. However, such hybrid fuzzing still suffers from difficulties conventionally faced by symbolic execution, such as the need for environment modeling and system call support. In this work, we show how to achieve the effect of concolic execution without having to compute and solve symbolic path constraints. When coverage-based greybox fuzzing reaches a roadblock in terms of reaching certain branches, we conduct a slicing on the execution trace and suggest modifications of the input to reach the relevant branches. A Large Language Model (LLM) is used as a solver to generate the modified input for reaching the desired branches. Compared with both the vanilla greybox fuzzer AFL and hybrid fuzzers Intriguer and Qsym, our LLM-based hybrid fuzzer HyLLfuzz (pronounced "hill fuzz") demonstrates superior coverage. Furthermore, the LLM-based concolic execution in HyLLfuzz takes a time that is 4-19 times faster than the concolic execution running in existing hybrid fuzzing tools. This experience shows that LLMs can be effectively inserted into the iterative loop of hybrid fuzzers, to efficiently expose more program behaviors.

**Link**: [arxiv](http://arxiv.org/abs/2412.15931v1),  [pdf](http://arxiv.org/pdf/2412.15931v1)

**Tags**: cs.SE cs.CR 



### Less is More: Towards Green Code Large Language Models via Unified   Structural Pruning
**Authors**: Guang Yang, Yu Zhou, Xiangyu Zhang, Wei Cheng, Ke Liu, Xiang Chen, Terry Yue Zhuo, Taolue Chen

**Updated**: 2024-12-20T14:13:09Z

**Summary**: The extensive application of Large Language Models (LLMs) in generative coding tasks has raised concerns due to their high computational demands and energy consumption. Unlike previous structural pruning methods designed for classification models that deal with lowdimensional classification logits, generative Code LLMs produce high-dimensional token logit sequences, making traditional pruning objectives inherently limited. Moreover, existing single component pruning approaches further constrain the effectiveness when applied to generative Code LLMs. In response, we propose Flab-Pruner, an innovative unified structural pruning method that combines vocabulary, layer, and Feed-Forward Network (FFN) pruning. This approach effectively reduces model parameters while maintaining performance. Additionally, we introduce a customized code instruction data strategy for coding tasks to enhance the performance recovery efficiency of the pruned model. Through extensive evaluations on three state-of-the-art Code LLMs across multiple generative coding tasks, the results demonstrate that Flab-Pruner retains 97% of the original performance after pruning 22% of the parameters and achieves the same or even better performance after post-training. The pruned models exhibit significant improvements in storage, GPU usage, computational efficiency, and environmental impact, while maintaining well robustness. Our research provides a sustainable solution for green software engineering and promotes the efficient deployment of LLMs in real-world generative coding intelligence applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.15921v1),  [pdf](http://arxiv.org/pdf/2412.15921v1)

**Tags**: cs.SE cs.AI 



### Development of a Large-scale Dataset of Chest Computed Tomography   Reports in Japanese and a High-performance Finding Classification Model
**Authors**: Yosuke Yamagishi, Yuta Nakamura, Tomohiro Kikuchi, Yuki Sonoda, Hiroshi Hirakawa, Shintaro Kano, Satoshi Nakamura, Shouhei Hanaoka, Takeharu Yoshikawa, Osamu Abe

**Updated**: 2024-12-20T13:59:11Z

**Summary**: Background: Recent advances in large language models highlight the need for high-quality multilingual medical datasets. While Japan leads globally in CT scanner deployment and utilization, the lack of large-scale Japanese radiology datasets has hindered the development of specialized language models for medical imaging analysis. Objective: To develop a comprehensive Japanese CT report dataset through machine translation and establish a specialized language model for structured finding classification. Additionally, to create a rigorously validated evaluation dataset through expert radiologist review. Methods: We translated the CT-RATE dataset (24,283 CT reports from 21,304 patients) into Japanese using GPT-4o mini. The training dataset consisted of 22,778 machine-translated reports, while the validation dataset included 150 radiologist-revised reports. We developed CT-BERT-JPN based on "tohoku-nlp/bert-base-japanese-v3" architecture for extracting 18 structured findings from Japanese radiology reports. Results: Translation metrics showed strong performance with BLEU scores of 0.731 and 0.690, and ROUGE scores ranging from 0.770 to 0.876 for Findings and from 0.748 to 0.857 for Impression sections. CT-BERT-JPN demonstrated superior performance compared to GPT-4o in 11 out of 18 conditions, including lymphadenopathy (+14.2%), interlobular septal thickening (+10.9%), and atelectasis (+7.4%). The model maintained F1 scores exceeding 0.95 in 14 out of 18 conditions and achieved perfect scores in four conditions. Conclusions: Our study establishes a robust Japanese CT report dataset and demonstrates the effectiveness of a specialized language model for structured finding classification. The hybrid approach of machine translation and expert validation enables the creation of large-scale medical datasets while maintaining high quality.

**Link**: [arxiv](http://arxiv.org/abs/2412.15907v1),  [pdf](http://arxiv.org/pdf/2412.15907v1)

**Tags**: cs.CL cs.AI 



### On the Suitability of pre-trained foundational LLMs for Analysis in   German Legal Education
**Authors**: Lorenz Wendlinger, Christian Braun, Abdullah Al Zubaer, Simon Alexander Nonn, Sarah Großkopf, Christofer Fellicious, Michael Granitzer

**Updated**: 2024-12-20T13:54:57Z

**Summary**: We show that current open-source foundational LLMs possess instruction capability and German legal background knowledge that is sufficient for some legal analysis in an educational context. However, model capability breaks down in very specific tasks, such as the classification of "Gutachtenstil" appraisal style components, or with complex contexts, such as complete legal opinions. Even with extended context and effective prompting strategies, they cannot match the Bag-of-Words baseline. To combat this, we introduce a Retrieval Augmented Generation based prompt example selection method that substantially improves predictions in high data availability scenarios. We further evaluate the performance of pre-trained LLMs on two standard tasks for argument mining and automated essay scoring and find it to be more adequate. Throughout, pre-trained LLMs improve upon the baseline in scenarios with little or no labeled data with Chain-of-Thought prompting further helping in the zero-shot case.

**Link**: [arxiv](http://arxiv.org/abs/2412.15902v1),  [pdf](http://arxiv.org/pdf/2412.15902v1)

**Tags**: cs.CL cs.AI 



### Evaluation of Reliability Criteria for News Publishers with Large   Language Models
**Authors**: Manuel Pratelli, John Bianchi, Fabio Pinelli, Marinella Petrocchi

**Updated**: 2024-12-20T13:50:18Z

**Summary**: In this study, we investigate the use of a large language model to assist in the evaluation of the reliability of the vast number of existing online news publishers, addressing the impracticality of relying solely on human expert annotators for this task. In the context of the Italian news media market, we first task the model with evaluating expert-designed reliability criteria using a representative sample of news articles. We then compare the model's answers with those of human experts. The dataset consists of 340 news articles, each annotated by two human experts and the LLM. Six criteria are taken into account, for a total of 6,120 annotations. We observe good agreement between LLM and human annotators in three of the six evaluated criteria, including the critical ability to detect instances where a text negatively targets an entity or individual. For two additional criteria, such as the detection of sensational language and the recognition of bias in news content, LLMs generate fair annotations, albeit with certain trade-offs. Furthermore, we show that the LLM is able to help resolve disagreements among human experts, especially in tasks such as identifying cases of negative targeting.

**Link**: [arxiv](http://arxiv.org/abs/2412.15896v1),  [pdf](http://arxiv.org/pdf/2412.15896v1)

**Tags**: cs.SI 



### TelcoLM: collecting data, adapting, and benchmarking language models for   the telecommunication domain
**Authors**: Camille Barboule, Viet-Phi Huynh, Adrien Bufort, Yoan Chabot, Géraldine Damnati, Gwénolé Lecorvé

**Updated**: 2024-12-20T13:47:02Z

**Summary**: Despite outstanding processes in many tasks, Large Language Models (LLMs) still lack accuracy when dealing with highly technical domains. Especially, telecommunications (telco) is a particularly challenging domain due the large amount of lexical, semantic and conceptual peculiarities. Yet, this domain holds many valuable use cases, directly linked to industrial needs. Hence, this paper studies how LLMs can be adapted to the telco domain. It reports our effort to (i) collect a massive corpus of domain-specific data (800M tokens, 80K instructions), (ii) perform adaptation using various methodologies, and (iii) benchmark them against larger generalist models in downstream tasks that require extensive knowledge of telecommunications. Our experiments on Llama-2-7b show that domain-adapted models can challenge the large generalist models. They also suggest that adaptation can be restricted to a unique instruction-tuning step, dicarding the need for any fine-tuning on raw texts beforehand.

**Link**: [arxiv](http://arxiv.org/abs/2412.15891v1),  [pdf](http://arxiv.org/pdf/2412.15891v1)

**Tags**: cs.CL cs.AI 



### Efficient Solutions For An Intriguing Failure of LLMs: Long Context   Window Does Not Mean LLMs Can Analyze Long Sequences Flawlessly
**Authors**: Peyman Hosseini, Ignacio Castro, Iacopo Ghinassi, Matthew Purver

**Updated**: 2024-12-20T13:19:58Z

**Summary**: Large Language Models (LLMs) have demonstrated remarkable capabilities in comprehending and analyzing lengthy sequential inputs, owing to their extensive context windows that allow processing millions of tokens in a single forward pass. However, this paper uncovers a surprising limitation: LLMs fall short when handling long input sequences. We investigate this issue using three datasets and two tasks (sentiment analysis and news categorization) across various LLMs, including Claude 3, Gemini Pro, GPT 3.5 Turbo, Llama 3 Instruct, and Mistral Instruct models. To address this limitation, we propose and evaluate ad-hoc solutions that substantially enhance LLMs' performance on long input sequences by up to 50%, while reducing API cost and latency by up to 93% and 50%, respectively.

**Link**: [arxiv](http://arxiv.org/abs/2408.01866v3),  [pdf](http://arxiv.org/pdf/2408.01866v3)

**Tags**: cs.CL cs.LG I.2.7 



### Large Language Models-guided Dynamic Adaptation for Temporal Knowledge   Graph Reasoning
**Authors**: Jiapu Wang, Kai Sun, Linhao Luo, Wei Wei, Yongli Hu, Alan Wee-Chung Liew, Shirui Pan, Baocai Yin

**Updated**: 2024-12-20T13:15:12Z

**Summary**: Temporal Knowledge Graph Reasoning (TKGR) is the process of utilizing temporal information to capture complex relations within a Temporal Knowledge Graph (TKG) to infer new knowledge. Conventional methods in TKGR typically depend on deep learning algorithms or temporal logical rules. However, deep learning-based TKGRs often lack interpretability, whereas rule-based TKGRs struggle to effectively learn temporal rules that capture temporal patterns. Recently, Large Language Models (LLMs) have demonstrated extensive knowledge and remarkable proficiency in temporal reasoning. Consequently, the employment of LLMs for Temporal Knowledge Graph Reasoning (TKGR) has sparked increasing interest among researchers. Nonetheless, LLMs are known to function as black boxes, making it challenging to comprehend their reasoning process. Additionally, due to the resource-intensive nature of fine-tuning, promptly updating LLMs to integrate evolving knowledge within TKGs for reasoning is impractical. To address these challenges, in this paper, we propose a Large Language Models-guided Dynamic Adaptation (LLM-DA) method for reasoning on TKGs. Specifically, LLM-DA harnesses the capabilities of LLMs to analyze historical data and extract temporal logical rules. These rules unveil temporal patterns and facilitate interpretable reasoning. To account for the evolving nature of TKGs, a dynamic adaptation strategy is proposed to update the LLM-generated rules with the latest events. This ensures that the extracted rules always incorporate the most recent knowledge and better generalize to the predictions on future events. Experimental results show that without the need of fine-tuning, LLM-DA significantly improves the accuracy of reasoning over several common datasets, providing a robust framework for TKGR tasks.

**Link**: [arxiv](http://arxiv.org/abs/2405.14170v2),  [pdf](http://arxiv.org/pdf/2405.14170v2)

**Tags**: cs.AI cs.CL 



### MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in   LLMs
**Authors**: Zhongshen Zeng, Yinhong Liu, Yingjia Wan, Jingyao Li, Pengguang Chen, Jianbo Dai, Yuxuan Yao, Rongwu Xu, Zehan Qi, Wanru Zhao, Linling Shen, Jianqiao Lu, Haochen Tan, Yukang Chen, Hao Zhang, Zhan Shi, Bailin Wang, Zhijiang Guo, Jiaya Jia

**Updated**: 2024-12-20T12:52:00Z

**Summary**: Large language models (LLMs) have shown increasing capability in problem-solving and decision-making, largely based on the step-by-step chain-of-thought reasoning processes. However, evaluating these reasoning abilities has become increasingly challenging. Existing outcome-based benchmarks are beginning to saturate, becoming less effective in tracking meaningful progress. To address this, we present a process-based benchmark MR-Ben that demands a meta-reasoning skill, where LMs are asked to locate and analyse potential errors in automatically generated reasoning steps. Our meta-reasoning paradigm is especially suited for system-2 slow thinking, mirroring the human cognitive process of carefully examining assumptions, conditions, calculations, and logic to identify mistakes.MR-Ben comprises 5,975 questions curated by human experts across a wide range of subjects, including physics, chemistry, logic, coding, and more. Through our designed metrics for assessing meta-reasoning on this benchmark, we identify interesting limitations and weaknesses of current LLMs (open-source and closed-source models). For example, with models like the o1 series from OpenAI demonstrating strong performance by effectively scrutinizing the solution space, many other state-of-the-art models fall significantly behind on MR-Ben, exposing potential shortcomings in their training strategies and inference methodologies.

**Link**: [arxiv](http://arxiv.org/abs/2406.13975v3),  [pdf](http://arxiv.org/pdf/2406.13975v3)

**Tags**: cs.CL cs.AI 



### Fake News Detection: Comparative Evaluation of BERT-like Models and   Large Language Models with Generative AI-Annotated Data
**Authors**: Shaina Raza, Drai Paulen-Patterson, Chen Ding

**Updated**: 2024-12-20T12:45:58Z

**Summary**: Fake news poses a significant threat to public opinion and social stability in modern society. This study presents a comparative evaluation of BERT-like encoder-only models and autoregressive decoder-only large language models (LLMs) for fake news detection. We introduce a dataset of news articles labeled with GPT-4 assistance (an AI-labeling method) and verified by human experts to ensure reliability. Both BERT-like encoder-only models and LLMs were fine-tuned on this dataset. Additionally, we developed an instruction-tuned LLM approach with majority voting during inference for label generation. Our analysis reveals that BERT-like models generally outperform LLMs in classification tasks, while LLMs demonstrate superior robustness against text perturbations. Compared to weak labels (distant supervision) data, the results show that AI labels with human supervision achieve better classification results. This study highlights the effectiveness of combining AI-based annotation with human oversight and demonstrates the performance of different families of machine learning models for fake news detection

**Link**: [arxiv](http://arxiv.org/abs/2412.14276v2),  [pdf](http://arxiv.org/pdf/2412.14276v2)

**Tags**: cs.CL cs.AI 



### Rethinking Hardware Impairments in Multi-User Systems: Can FAS Make a   Difference?
**Authors**: Junteng Yao, Tuo Wu, Liaoshi Zhou, Ming Jin, Cunhua Pan, Maged Elkashlan, Fumiyuki Adachi, George K. Karagiannidis, Naofal Al-Dhahir, Chau Yuen

**Updated**: 2024-12-20T12:34:58Z

**Summary**: In this paper, we analyze the role of fluid antenna systems (FAS) in multi-user systems with hardware impairments (HIs). Specifically, we investigate a scenario where a base station (BS) equipped with multiple fluid antennas communicates with multiple users (CUs), each equipped with a single fluid antenna. Our objective is to maximize the minimum communication rate among all users by jointly optimizing the BS's transmit beamforming, the positions of its transmit fluid antennas, and the positions of the CUs' receive fluid antennas. To address this non-convex problem, we propose a block coordinate descent (BCD) algorithm integrating semidefinite relaxation (SDR), rank-one constraint relaxation (SRCR), successive convex approximation (SCA), and majorization-minimization (MM). Simulation results demonstrate that FAS significantly enhances system performance and robustness, with notable gains when both the BS and CUs are equipped with fluid antennas. Even under low transmit power conditions, deploying FAS at the BS alone yields substantial performance gains. However, the effectiveness of FAS depends on the availability of sufficient movement space, as space constraints may limit its benefits compared to fixed antenna strategies. Our findings highlight the potential of FAS to mitigate HIs and enhance multi-user system performance, while emphasizing the need for practical deployment considerations.

**Link**: [arxiv](http://arxiv.org/abs/2412.15843v1),  [pdf](http://arxiv.org/pdf/2412.15843v1)

**Tags**: eess.SP 



### Are You Human? An Adversarial Benchmark to Expose LLMs
**Authors**: Gilad Gressel, Rahul Pankajakshan, Yisroel Mirsky

**Updated**: 2024-12-20T12:25:22Z

**Summary**: Large Language Models (LLMs) have demonstrated an alarming ability to impersonate humans in conversation, raising concerns about their potential misuse in scams and deception. Humans have a right to know if they are conversing to an LLM. We evaluate text-based prompts designed as challenges to expose LLM imposters in real-time. To this end we compile and release an open-source benchmark dataset that includes 'implicit challenges' that exploit an LLM's instruction-following mechanism to cause role deviation, and 'exlicit challenges' that test an LLM's ability to perform simple tasks typically easy for humans but difficult for LLMs. Our evaluation of 9 leading models from the LMSYS leaderboard revealed that explicit challenges successfully detected LLMs in 78.4% of cases, while implicit challenges were effective in 22.9% of instances. User studies validate the real-world applicability of our methods, with humans outperforming LLMs on explicit challenges (78% vs 22% success rate). Our framework unexpectedly revealed that many study participants were using LLMs to complete tasks, demonstrating its effectiveness in detecting both AI impostors and human misuse of AI tools. This work addresses the critical need for reliable, real-time LLM detection methods in high-stakes conversations.

**Link**: [arxiv](http://arxiv.org/abs/2410.09569v2),  [pdf](http://arxiv.org/pdf/2410.09569v2)

**Tags**: cs.CL cs.AI 



### Improving In-Context Learning with Small Language Model Ensembles
**Authors**: M. Mehdi Mojarradi, Lingyi Yang, Robert McCraith, Adam Mahdi

**Updated**: 2024-12-20T12:22:37Z

**Summary**: Large language models (LLMs) have shown impressive capabilities across various tasks, but their performance on domain-specific tasks remains limited. While methods like retrieval augmented generation and fine-tuning can help to address this, they require significant resources. In-context learning (ICL) is a cheap and efficient alternative but cannot match the accuracies of advanced methods. We present Ensemble SuperICL, a novel approach that enhances ICL by leveraging the expertise of multiple fine-tuned small language models (SLMs). Ensemble SuperICL achieves state of the art (SoTA) results on several natural language understanding benchmarks. Additionally, we test it on a medical-domain labelling task and showcase its practicality by using off-the-shelf SLMs fine-tuned on a general language task, achieving superior accuracy in large-scale data labelling compared to all baselines. Finally, we conduct an ablation study and sensitivity analyses to elucidate the underlying mechanism of Ensemble SuperICL. Our research contributes to the growing demand for efficient domain specialisation methods in LLMs, offering a cheap and effective method for practitioners.

**Link**: [arxiv](http://arxiv.org/abs/2410.21868v2),  [pdf](http://arxiv.org/pdf/2410.21868v2)

**Tags**: cs.CL 



### LLAssist: Simple Tools for Automating Literature Review Using Large   Language Models
**Authors**: Christoforus Yoga Haryanto

**Updated**: 2024-12-20T12:06:25Z

**Summary**: This paper introduces LLAssist, an open-source tool designed to streamline literature reviews in academic research. In an era of exponential growth in scientific publications, researchers face mounting challenges in efficiently processing vast volumes of literature. LLAssist addresses this issue by leveraging Large Language Models (LLMs) and Natural Language Processing (NLP) techniques to automate key aspects of the review process. Specifically, it extracts important information from research articles and evaluates their relevance to user-defined research questions. The goal of LLAssist is to significantly reduce the time and effort required for comprehensive literature reviews, allowing researchers to focus more on analyzing and synthesizing information rather than on initial screening tasks. By automating parts of the literature review workflow, LLAssist aims to help researchers manage the growing volume of academic publications more efficiently.

**Link**: [arxiv](http://arxiv.org/abs/2407.13993v3),  [pdf](http://arxiv.org/pdf/2407.13993v3)

**Tags**: cs.DL cs.AI 



### Robustness-enhanced Myoelectric Control with GAN-based Open-set   Recognition
**Authors**: Cheng Wang, Ziyang Feng, Pin Zhang, Manjiang Cao, Yiming Yuan, Tengfei Chang

**Updated**: 2024-12-20T12:01:01Z

**Summary**: Electromyography (EMG) signals are widely used in human motion recognition and medical rehabilitation, yet their variability and susceptibility to noise significantly limit the reliability of myoelectric control systems. Existing recognition algorithms often fail to handle unfamiliar actions effectively, leading to system instability and errors. This paper proposes a novel framework based on Generative Adversarial Networks (GANs) to enhance the robustness and usability of myoelectric control systems by enabling open-set recognition. The method incorporates a GAN-based discriminator to identify and reject unknown actions, maintaining system stability by preventing misclassifications. Experimental evaluations on publicly available and self-collected datasets demonstrate a recognition accuracy of 97.6\% for known actions and a 23.6\% improvement in Active Error Rate (AER) after rejecting unknown actions. The proposed approach is computationally efficient and suitable for deployment on edge devices, making it practical for real-world applications.

**Link**: [arxiv](http://arxiv.org/abs/2412.15819v1),  [pdf](http://arxiv.org/pdf/2412.15819v1)

**Tags**: cs.CV cs.HC eess.SP 



### Cross-Lingual Transfer of Debiasing and Detoxification in Multilingual   LLMs: An Extensive Investigation
**Authors**: Vera Neplenbroek, Arianna Bisazza, Raquel Fernández

**Updated**: 2024-12-20T11:55:35Z

**Summary**: Recent generative large language models (LLMs) show remarkable performance in non-English languages, but when prompted in those languages they tend to express higher harmful social biases and toxicity levels. Prior work has shown that finetuning on specialized datasets can mitigate this behavior, and doing so in English can transfer to other languages. In this work, we investigate the impact of different finetuning methods on the model's bias and toxicity, but also on its ability to produce fluent and diverse text. Our results show that finetuning on curated non-harmful text is more effective for mitigating bias, and finetuning on direct preference optimization (DPO) datasets is more effective for mitigating toxicity. The mitigation caused by applying these methods in English also transfers to non-English languages. We find evidence that the extent to which transfer takes place can be predicted by the amount of data in a given language present in the model's pretraining data. However, this transfer of bias and toxicity mitigation often comes at the expense of decreased language generation ability in non-English languages, highlighting the importance of developing language-specific bias and toxicity mitigation methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.14050v2),  [pdf](http://arxiv.org/pdf/2412.14050v2)

**Tags**: cs.CL 



### Understanding Emotional Body Expressions via Large Language Models
**Authors**: Haifeng Lu, Jiuyi Chen, Feng Liang, Mingkui Tan, Runhao Zeng, Xiping Hu

**Updated**: 2024-12-20T11:49:07Z

**Summary**: Emotion recognition based on body movements is vital in human-computer interaction. However, existing emotion recognition methods predominantly focus on enhancing classification accuracy, often neglecting the provision of textual explanations to justify their classifications. In this paper, we propose an Emotion-Action Interpreter powered by Large Language Model (EAI-LLM), which not only recognizes emotions but also generates textual explanations by treating 3D body movement data as unique input tokens within large language models (LLMs). Specifically, we propose a multi-granularity skeleton tokenizer designed for LLMs, which separately extracts spatio-temporal tokens and semantic tokens from the skeleton data. This approach allows LLMs to generate more nuanced classification descriptions while maintaining robust classification performance. Furthermore, we treat the skeleton sequence as a specific language and propose a unified skeleton token module. This module leverages the extensive background knowledge and language processing capabilities of LLMs to address the challenges of joint training on heterogeneous datasets, thereby significantly enhancing recognition accuracy on individual datasets. Experimental results demonstrate that our model achieves recognition accuracy comparable to existing methods. More importantly, with the support of background knowledge from LLMs, our model can generate detailed emotion descriptions based on classification results, even when trained on a limited amount of labeled skeleton data.

**Link**: [arxiv](http://arxiv.org/abs/2412.12581v2),  [pdf](http://arxiv.org/pdf/2412.12581v2)

**Tags**: cs.HC 



### CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge   Graph
**Authors**: Hanxiang Xu, Wei Ma, Ting Zhou, Yanjie Zhao, Kai Chen, Qiang Hu, Yang Liu, Haoyu Wang

**Updated**: 2024-12-20T11:25:59Z

**Summary**: In recent years, the programming capabilities of large language models (LLMs) have garnered significant attention. Fuzz testing, a highly effective technique, plays a key role in enhancing software reliability and detecting vulnerabilities. However, traditional fuzz testing tools rely on manually crafted fuzz drivers, which can limit both testing efficiency and effectiveness. To address this challenge, we propose an automated fuzz testing method driven by a code knowledge graph and powered by an LLM-based intelligent agent system, referred to as CKGFuzzer. We approach fuzz driver creation as a code generation task, leveraging the knowledge graph of the code repository to automate the generation process within the fuzzing loop, while continuously refining both the fuzz driver and input seeds. The code knowledge graph is constructed through interprocedural program analysis, where each node in the graph represents a code entity, such as a function or a file. The knowledge graph-enhanced CKGFuzzer not only effectively resolves compilation errors in fuzz drivers and generates input seeds tailored to specific API usage scenarios, but also analyzes fuzz driver crash reports, assisting developers in improving code quality. By querying the knowledge graph of the code repository and learning from API usage scenarios, we can better identify testing targets and understand the specific purpose of each fuzz driver. We evaluated our approach using eight open-source software projects. The experimental results indicate that CKGFuzzer achieved an average improvement of 8.73% in code coverage compared to state-of-the-art techniques. Additionally, CKGFuzzer reduced the manual review workload in crash case analysis by 84.4% and successfully detected 11 real bugs (including nine previously unreported bugs) across the tested libraries.

**Link**: [arxiv](http://arxiv.org/abs/2411.11532v3),  [pdf](http://arxiv.org/pdf/2411.11532v3)

**Tags**: cs.SE cs.CR 



### WebLLM: A High-Performance In-Browser LLM Inference Engine
**Authors**: Charlie F. Ruan, Yucheng Qin, Xun Zhou, Ruihang Lai, Hongyi Jin, Yixin Dong, Bohan Hou, Meng-Shiun Yu, Yiyan Zhai, Sudeep Agarwal, Hangrui Cao, Siyuan Feng, Tianqi Chen

**Updated**: 2024-12-20T11:24:13Z

**Summary**: Advancements in large language models (LLMs) have unlocked remarkable capabilities. While deploying these models typically requires server-grade GPUs and cloud-based inference, the recent emergence of smaller open-source models and increasingly powerful consumer devices have made on-device deployment practical. The web browser as a platform for on-device deployment is universally accessible, provides a natural agentic environment, and conveniently abstracts out the different backends from diverse device vendors. To address this opportunity, we introduce WebLLM, an open-source JavaScript framework that enables high-performance LLM inference entirely within web browsers. WebLLM provides an OpenAI-style API for seamless integration into web applications, and leverages WebGPU for efficient local GPU acceleration and WebAssembly for performant CPU computation. With machine learning compilers MLC-LLM and Apache TVM, WebLLM leverages optimized WebGPU kernels, overcoming the absence of performant WebGPU kernel libraries. Evaluations show that WebLLM can retain up to 80% native performance on the same device, with room to further close the gap. WebLLM paves the way for universally accessible, privacy-preserving, personalized, and locally powered LLM applications in web browsers. The code is available at: https://github.com/mlc-ai/web-llm.

**Link**: [arxiv](http://arxiv.org/abs/2412.15803v1),  [pdf](http://arxiv.org/pdf/2412.15803v1)

**Tags**: cs.LG cs.AI 



### GraphSeqLM: A Unified Graph Language Framework for Omic Graph Learning
**Authors**: Heming Zhang, Di Huang, Yixin Chen, Fuhai Li

**Updated**: 2024-12-20T11:05:26Z

**Summary**: The integration of multi-omic data is pivotal for understanding complex diseases, but its high dimensionality and noise present significant challenges. Graph Neural Networks (GNNs) offer a robust framework for analyzing large-scale signaling pathways and protein-protein interaction networks, yet they face limitations in expressivity when capturing intricate biological relationships. To address this, we propose Graph Sequence Language Model (GraphSeqLM), a framework that enhances GNNs with biological sequence embeddings generated by Large Language Models (LLMs). These embeddings encode structural and biological properties of DNA, RNA, and proteins, augmenting GNNs with enriched features for analyzing sample-specific multi-omic data. By integrating topological, sequence-derived, and biological information, GraphSeqLM demonstrates superior predictive accuracy and outperforms existing methods, paving the way for more effective multi-omic data integration in precision medicine.

**Link**: [arxiv](http://arxiv.org/abs/2412.15790v1),  [pdf](http://arxiv.org/pdf/2412.15790v1)

**Tags**: q-bio.QM cs.AI cs.LG 



### Responsibility-aware Strategic Reasoning in Probabilistic Multi-Agent   Systems
**Authors**: Chunyan Mu, Muhammad Najib, Nir Oren

**Updated**: 2024-12-20T10:50:09Z

**Summary**: Responsibility plays a key role in the development and deployment of trustworthy autonomous systems. In this paper, we focus on the problem of strategic reasoning in probabilistic multi-agent systems with responsibility-aware agents. We introduce the logic PATL+R, a variant of Probabilistic Alternating-time Temporal Logic. The novelty of PATL+R lies in its incorporation of modalities for causal responsibility, providing a framework for responsibility-aware multi-agent strategic reasoning. We present an approach to synthesise joint strategies that satisfy an outcome specified in PATL+R, while optimising the share of expected causal responsibility and reward. This provides a notion of balanced distribution of responsibility and reward gain among agents. To this end, we utilise the Nash equilibrium as the solution concept for our strategic reasoning problem and demonstrate how to compute responsibility-aware Nash equilibrium strategies via a reduction to parametric model checking of concurrent stochastic multi-player games.

**Link**: [arxiv](http://arxiv.org/abs/2411.00146v2),  [pdf](http://arxiv.org/pdf/2411.00146v2)

**Tags**: cs.AI 



### Linguistic Features Extracted by GPT-4 Improve Alzheimer's Disease   Detection based on Spontaneous Speech
**Authors**: Jonathan Heitz, Gerold Schneider, Nicolas Langer

**Updated**: 2024-12-20T10:43:42Z

**Summary**: Alzheimer's Disease (AD) is a significant and growing public health concern. Investigating alterations in speech and language patterns offers a promising path towards cost-effective and non-invasive early detection of AD on a large scale. Large language models (LLMs), such as GPT, have enabled powerful new possibilities for semantic text analysis. In this study, we leverage GPT-4 to extract five semantic features from transcripts of spontaneous patient speech. The features capture known symptoms of AD, but they are difficult to quantify effectively using traditional methods of computational linguistics. We demonstrate the clinical significance of these features and further validate one of them ("Word-Finding Difficulties") against a proxy measure and human raters. When combined with established linguistic features and a Random Forest classifier, the GPT-derived features significantly improve the detection of AD. Our approach proves effective for both manually transcribed and automatically generated transcripts, representing a novel and impactful use of recent advancements in LLMs for AD speech analysis.

**Link**: [arxiv](http://arxiv.org/abs/2412.15772v1),  [pdf](http://arxiv.org/pdf/2412.15772v1)

**Tags**: cs.CL cs.AI 



### Questioning the Unknown: Optimising Multi-Agent Collaboration in   Narrative-Driven Games
**Authors**: Qinglin Zhu, Runcong Zhao, Jinhua Du, Lin Gui, Yulan He

**Updated**: 2024-12-20T10:35:07Z

**Summary**: We present Questum, a novel framework for Large Language Model (LLM)-based agents in Murder Mystery Games (MMGs). MMGs pose unique challenges, including undefined state spaces, absent intermediate rewards, and the need for strategic interaction in a continuous language domain. Questum addresses these complexities through a sensor-based representation of agent states, a question-targeting mechanism guided by information gain, and a pruning strategy to refine suspect lists and enhance decision-making efficiency. To enable systematic evaluation, we propose WellPlay, a dataset comprising 1,482 inferential questions across 12 games, categorised into objectives, reasoning, and relationships. Experiments demonstrate Questum's capacity to achieve superior performance in reasoning accuracy and efficiency compared to existing approaches, while also significantly improving the quality of agent-human interactions in MMGs. This study advances the development of reasoning agents for complex social and interactive scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2404.17662v3),  [pdf](http://arxiv.org/pdf/2404.17662v3)

**Tags**: cs.CL 



### Probabilistic Latent Variable Modeling for Dynamic Friction   Identification and Estimation
**Authors**: Victor Vantilborgh, Sander De Witte, Frederik Ostyn, Tom Lefebvre, Guillaume Crevecoeur

**Updated**: 2024-12-20T10:16:18Z

**Summary**: Precise identification of dynamic models in robotics is essential to support control design, friction compensation, output torque estimation, etc. A longstanding challenge remains in the identification of friction models for robotic joints, given the numerous physical phenomena affecting the underlying friction dynamics which result into nonlinear characteristics and hysteresis behaviour in particular. These phenomena proof difficult to be modelled and captured accurately using physical analogies alone. This has motivated researchers to shift from physics-based to data-driven models. Currently, these methods are still limited in their ability to generalize effectively to typical industrial robot deployement, characterized by high- and low-velocity operations and frequent direction reversals. Empirical observations motivate the use of dynamic friction models but these remain particulary challenging to establish. To address the current limitations, we propose to account for unidentified dynamics in the robot joints using latent dynamic states. The friction model may then utilize both the dynamic robot state and additional information encoded in the latent state to evaluate the friction torque. We cast this stochastic and partially unsupervised identification problem as a standard probabilistic representation learning problem. In this work both the friction model and latent state dynamics are parametrized as neural networks and integrated in the conventional lumped parameter dynamic robot model. The complete dynamics model is directly learned from the noisy encoder measurements in the robot joints. We use the Expectation-Maximisation (EM) algorithm to find a Maximum Likelihood Estimate (MLE) of the model parameters. The effectiveness of the proposed method is validated in terms of open-loop prediction accuracy in comparison with baseline methods, using the Kuka KR6 R700 as a test platform.

**Link**: [arxiv](http://arxiv.org/abs/2412.15756v1),  [pdf](http://arxiv.org/pdf/2412.15756v1)

**Tags**: cs.RO cs.LG cs.SY eess.SY 



### Extracting Interpretable Task-Specific Circuits from Large Language   Models for Faster Inference
**Authors**: Jorge García-Carrasco, Alejandro Maté, Juan Trujillo

**Updated**: 2024-12-20T10:11:44Z

**Summary**: Large Language Models (LLMs) have shown impressive performance across a wide range of tasks. However, the size of LLMs is steadily increasing, hindering their application on computationally constrained environments. On the other hand, despite their general capabilities, there are many situations where only one specific task is performed, rendering all other capabilities unnecessary and wasteful. This leads us to the following question: Is it possible to extract the minimal subset from an LLM that is able to perform a specific task in a faster, standalone manner? Recent works on Mechanistic Interpretability (MI) have shown that specific tasks are performed by a localized subset of components, or circuit. However, current techniques used to identify the circuit cannot be used to extract it for its standalone usage. In this work, we propose a novel approach to automatically extract the subset of the LLM that properly performs a targeted task requiring no additional training and a small amount of data samples. We evaluate our approach on different tasks and show that the resulting models are (i) considerably smaller, reducing the number of parameters up to 82.77% and (ii) more interpretable, as they focus on the circuit that is used to carry out the specific task, and can therefore be understood using MI techniques.

**Link**: [arxiv](http://arxiv.org/abs/2412.15750v1),  [pdf](http://arxiv.org/pdf/2412.15750v1)

**Tags**: cs.LG 



### Critique of Impure Reason: Unveiling the reasoning behaviour of medical   Large Language Models
**Authors**: Shamus Sim, Tyrone Chen

**Updated**: 2024-12-20T10:06:52Z

**Summary**: Background: Despite the current ubiquity of Large Language Models (LLMs) across the medical domain, there is a surprising lack of studies which address their reasoning behaviour. We emphasise the importance of understanding reasoning behaviour as opposed to high-level prediction accuracies, since it is equivalent to explainable AI (XAI) in this context. In particular, achieving XAI in medical LLMs used in the clinical domain will have a significant impact across the healthcare sector. Results: Therefore, we define the concept of reasoning behaviour in the specific context of medical LLMs. We then categorise and discuss the current state of the art of methods which evaluate reasoning behaviour in medical LLMs. Finally, we propose theoretical frameworks which can empower medical professionals or machine learning engineers to gain insight into the low-level reasoning operations of these previously obscure models. Conclusion: The subsequent increased transparency and trust in medical machine learning models by clinicians as well as patients will accelerate the integration, application as well as further development of medical AI for the healthcare system as a whole

**Link**: [arxiv](http://arxiv.org/abs/2412.15748v1),  [pdf](http://arxiv.org/pdf/2412.15748v1)

**Tags**: cs.CL cs.AI cs.LG 



### Building Bridges: AI Custom Chatbots as Mediators between Mathematics   and Physics
**Authors**: Julia Lademann, Jannik Henze, Sebastian Becker-Genschow

**Updated**: 2024-12-20T10:06:30Z

**Summary**: This work explores the integration of AI custom chatbots in educational settings, with a particular focus on their applicability in the context of mathematics and physics. In view of the increasing deployment of AI tools such as ChatGPT in educational contexts, the present study examines their potential as personalized tutoring systems. The study assesses the impact of AI-generated learning materials on the learning experiences and performance of sixth-grade students, with a particular focus on proportional relationships in mathematical and physical contexts. The randomized controlled study with N = 214 students compared traditional textbook materials with explanations generated by a custom chatbot. The results demonstrated that while AI-generated materials had an indefinite impact on learning outcomes, they significantly enhanced positive-activating emotions, situational interest, and self-efficacy, while reducing intrinsic and extrinsic cognitive load. These findings underscore the potential of AI to transform educational practices by fostering a superior learning experience. However, further research is required to clarify its impact on learning performance and long-term learning outcomes. The study highlights the importance of careful integration and customization of AI tools to maximize their benefits in physics education.

**Link**: [arxiv](http://arxiv.org/abs/2412.15747v1),  [pdf](http://arxiv.org/pdf/2412.15747v1)

**Tags**: physics.ed-ph 



### VORD: Visual Ordinal Calibration for Mitigating Object Hallucinations in   Large Vision-Language Models
**Authors**: Dexter Neo, Tsuhan Chen

**Updated**: 2024-12-20T10:00:26Z

**Summary**: Large Vision-Language Models (LVLMs) have made remarkable developments along with the recent surge of large language models. Despite their advancements, LVLMs have a tendency to generate plausible yet inaccurate or inconsistent information based on the provided source content. This phenomenon, also known as ``hallucinations" can have serious downstream implications during the deployment of LVLMs. To address this, we present VORD a simple and effective method that alleviates hallucinations by calibrating token predictions based on ordinal relationships between modified image pairs. VORD is presented in two forms: 1.) a minimalist training-free variant which eliminates implausible tokens from modified image pairs, and 2.) a trainable objective function that penalizes unlikely tokens. Our experiments demonstrate that VORD delivers better calibration and effectively mitigates object hallucinations on a wide-range of LVLM benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2412.15739v1),  [pdf](http://arxiv.org/pdf/2412.15739v1)

**Tags**: cs.CV 



### Switching Frequency as FPGA Monitor: Studying Degradation and Ageing   Prognosis at Large Scale
**Authors**: Leandro Lanzieri, Lukasz Butkowski, Jiri Kral, Goerschwin Fey, Holger Schlarb, Thomas C. Schmidt

**Updated**: 2024-12-20T09:42:28Z

**Summary**: The growing deployment of unhardened embedded devices in critical systems demands the monitoring of hardware ageing as part of predictive maintenance. In this paper, we study degradation on a large deployment of 298 naturally aged FPGAs operating in the European XFEL particle accelerator. We base our statistical analyses on 280 days of in-field measurements and find a generalized and continuous degradation of the switching frequency across all devices with a median value of 0.064%. The large scale of this study allows us to localize areas of the deployed FPGAs that are highly impacted by degradation. Moreover, by training machine learning models on the collected data, we are able to forecast future trends of frequency degradation with horizons of 60 days and relative errors as little as 0.002% over an evaluation period of 100 days.

**Link**: [arxiv](http://arxiv.org/abs/2412.15720v1),  [pdf](http://arxiv.org/pdf/2412.15720v1)

**Tags**: cs.AR cs.SY eess.SY 



### Utilize the Flow before Stepping into the Same River Twice: Certainty   Represented Knowledge Flow for Refusal-Aware Instruction Tuning
**Authors**: Runchuan Zhu, Zhipeng Ma, Jiang Wu, Junyuan Gao, Jiaqi Wang, Dahua Lin, Conghui He

**Updated**: 2024-12-20T09:40:54Z

**Summary**: Refusal-Aware Instruction Tuning (RAIT) enables Large Language Models (LLMs) to refuse to answer unknown questions. By modifying responses of unknown questions in the training data to refusal responses such as "I don't know", RAIT enhances the reliability of LLMs and reduces their hallucination. Generally, RAIT modifies training samples based on the correctness of the initial LLM's response. However, this crude approach can cause LLMs to excessively refuse answering questions they could have correctly answered, the problem we call over-refusal. In this paper, we explore two primary causes of over-refusal: Static conflict occurs when similar samples within the LLM's feature space receive differing supervision signals (original vs. modified "I don't know"). Dynamic conflict arises as the LLM's evolving knowledge during SFT enables it to answer previously unanswerable questions, but the now-answerable training samples still retain the original "I don't know" supervision signals from the initial LLM state, leading to inconsistencies. These conflicts cause the trained LLM to misclassify known questions as unknown, resulting in over-refusal. To address this issue, we introduce Certainty Represented Knowledge Flow for Refusal-Aware Instructions Tuning (CRaFT). CRaFT centers on two main contributions: First, we additionally incorporate response certainty to selectively filter and modify data, reducing static conflicts. Second, we implement preliminary rehearsal training to characterize changes in the LLM's knowledge state, which helps mitigate dynamic conflicts during the fine-tuning process. We conducted extensive experiments on open-ended question answering and multiple-choice question task. Experiment results show that CRaFT can improve LLM's overall performance during the RAIT process. Code and data will be released at https://github.com/opendatalab/CRaFT .

**Link**: [arxiv](http://arxiv.org/abs/2410.06913v3),  [pdf](http://arxiv.org/pdf/2410.06913v3)

**Tags**: cs.CL 



### AutoLife: Automatic Life Journaling with Smartphones and LLMs
**Authors**: Huatao Xu, Panron Tong, Mo Li, Mani Srivastava

**Updated**: 2024-12-20T09:37:02Z

**Summary**: This paper introduces a novel mobile sensing application - life journaling - designed to generate semantic descriptions of users' daily lives. We present AutoLife, an automatic life journaling system based on commercial smartphones. AutoLife only inputs low-cost sensor data (without photos or audio) from smartphones and can automatically generate comprehensive life journals for users. To achieve this, we first derive time, motion, and location contexts from multimodal sensor data, and harness the zero-shot capabilities of Large Language Models (LLMs), enriched with commonsense knowledge about human lives, to interpret diverse contexts and generate life journals. To manage the task complexity and long sensing duration, a multilayer framework is proposed, which decomposes tasks and seamlessly integrates LLMs with other techniques for life journaling. This study establishes a real-life dataset as a benchmark and extensive experiment results demonstrate that AutoLife produces accurate and reliable life journals.

**Link**: [arxiv](http://arxiv.org/abs/2412.15714v1),  [pdf](http://arxiv.org/pdf/2412.15714v1)

**Tags**: cs.AI cs.CL cs.HC 



### Contrastive Learning for Task-Independent SpeechLLM-Pretraining
**Authors**: Maike Züfle, Jan Niehues

**Updated**: 2024-12-20T09:33:31Z

**Summary**: Large language models (LLMs) excel in natural language processing but adapting these LLMs to speech processing tasks efficiently is not straightforward. Direct task-specific fine-tuning is limited by overfitting risks, data requirements, and computational costs. To address these challenges, we propose a scalable, two-stage training approach: (1) A task-independent speech pretraining stage using contrastive learning to align text and speech representations over all layers, followed by (2) a task-specific fine-tuning stage requiring minimal data. This approach outperforms traditional ASR pretraining and enables the model to surpass models specialized on speech translation and question answering while being trained on only 10% of the task-specific data.

**Link**: [arxiv](http://arxiv.org/abs/2412.15712v1),  [pdf](http://arxiv.org/pdf/2412.15712v1)

**Tags**: cs.CL cs.HC 



### Cracking the Code: Evaluating Zero-Shot Prompting Methods for Providing   Programming Feedback
**Authors**: Niklas Ippisch, Anna-Carolina Haensch, Jan Simson, Jacob Beck, Markus Herklotz, Malte Schierholz

**Updated**: 2024-12-20T09:24:50Z

**Summary**: Despite the growing use of large language models (LLMs) for providing feedback, limited research has explored how to achieve high-quality feedback. This case study introduces an evaluation framework to assess different zero-shot prompt engineering methods. We varied the prompts systematically and analyzed the provided feedback on programming errors in R. The results suggest that prompts suggesting a stepwise procedure increase the precision, while omitting explicit specifications about which provided data to analyze improves error identification.

**Link**: [arxiv](http://arxiv.org/abs/2412.15702v1),  [pdf](http://arxiv.org/pdf/2412.15702v1)

**Tags**: cs.SE 



### Concept Boundary Vectors
**Authors**: Thomas Walker

**Updated**: 2024-12-20T09:18:11Z

**Summary**: Machine learning models are trained with relatively simple objectives, such as next token prediction. However, on deployment, they appear to capture a more fundamental representation of their input data. It is of interest to understand the nature of these representations to help interpret the model's outputs and to identify ways to improve the salience of these representations. Concept vectors are constructions aimed at attributing concepts in the input data to directions, represented by vectors, in the model's latent space. In this work, we introduce concept boundary vectors as a concept vector construction derived from the boundary between the latent representations of concepts. Empirically we demonstrate that concept boundary vectors capture a concept's semantic meaning, and we compare their effectiveness against concept activation vectors.

**Link**: [arxiv](http://arxiv.org/abs/2412.15698v1),  [pdf](http://arxiv.org/pdf/2412.15698v1)

**Tags**: cs.LG 



### Code Review Automation Via Multi-task Federated LLM -- An Empirical   Study
**Authors**: Jahnavi Kumar, Sridhar Chimalakonda

**Updated**: 2024-12-20T08:46:46Z

**Summary**: Code review is a crucial process before deploying code to production, as it validates the code, provides suggestions for improvements, and identifies errors such as missed edge cases. In projects with regular production releases, the effort required for peer code-reviews remains high. Consequently, there has been significant interest from software engineering (SE) researchers in automating the code review process. Previous research on code review automation has typically approached the task as three independent sub-tasks: review necessity prediction, review comment generation, and code refinement. Our study attempts to (i) leverage the relationships between the sub-tasks of code review automation, by developing a multi-task model that addresses all tasks in an integrated manner, and (ii) increase model robustness on unseen data via collaborative large language model (LLM) modeling, while retaining the proprietary nature of code, by using federated learning (FL). The study explores five simple techniques for multi-task training, including two sequential methods, one parallel method, and two cumulative methods. The results indicate that sequentially training a federated LLM (FedLLM) for our code review multi-task use case is less efficient in terms of time, computation, and performance metrics, compared to training separate models for each task. Because sequential training demonstrates catastrophic forgetting, alternatively cumulative fine-tuning for multi-task training performs better than training models for individual tasks. This study highlights the need for research focused on effective fine-tuning of multi-task FedLLMs for SE tasks.

**Link**: [arxiv](http://arxiv.org/abs/2412.15676v1),  [pdf](http://arxiv.org/pdf/2412.15676v1)

**Tags**: cs.SE 



### Small Language Models as Effective Guides for Large Language Models in   Chinese Relation Extraction
**Authors**: Xuemei Tang, Jun Wang

**Updated**: 2024-12-20T08:46:30Z

**Summary**: Recently, large language models (LLMs) have been successful in relational extraction (RE) tasks, especially in the few-shot learning. An important problem in the field of RE is long-tailed data, while not much attention is paid to this problem using LLM approaches. Therefore, in this paper, we propose SLCoLM, a model collaboration framework, to mitigate the data long-tail problem. In our framework, we use the ``\textit{Training-Guide-Predict}'' strategy to combine the strengths of small pre-trained language models (SLMs) and LLMs, where a task-specific SLM framework acts as a guider, transfers task knowledge to the LLM and guides the LLM in performing RE tasks. Our experiments on an ancient Chinese RE dataset rich in relation types show that the approach facilitates RE of long-tail relation types.

**Link**: [arxiv](http://arxiv.org/abs/2402.14373v2),  [pdf](http://arxiv.org/pdf/2402.14373v2)

**Tags**: cs.CL 



### AdaSociety: An Adaptive Environment with Social Structures for   Multi-Agent Decision-Making
**Authors**: Yizhe Huang, Xingbo Wang, Hao Liu, Fanqi Kong, Aoyang Qin, Min Tang, Xiaoxi Wang, Song-Chun Zhu, Mingjie Bi, Siyuan Qi, Xue Feng

**Updated**: 2024-12-20T08:38:38Z

**Summary**: Traditional interactive environments limit agents' intelligence growth with fixed tasks. Recently, single-agent environments address this by generating new tasks based on agent actions, enhancing task diversity. We consider the decision-making problem in multi-agent settings, where tasks are further influenced by social connections, affecting rewards and information access. However, existing multi-agent environments lack a combination of adaptive physical surroundings and social connections, hindering the learning of intelligent behaviors. To address this, we introduce AdaSociety, a customizable multi-agent environment featuring expanding state and action spaces, alongside explicit and alterable social structures. As agents progress, the environment adaptively generates new tasks with social structures for agents to undertake. In AdaSociety, we develop three mini-games showcasing distinct social structures and tasks. Initial results demonstrate that specific social structures can promote both individual and collective benefits, though current reinforcement learning and LLM-based algorithms show limited effectiveness in leveraging social structures to enhance performance. Overall, AdaSociety serves as a valuable research platform for exploring intelligence in diverse physical and social settings. The code is available at https://github.com/bigai-ai/AdaSociety.

**Link**: [arxiv](http://arxiv.org/abs/2411.03865v3),  [pdf](http://arxiv.org/pdf/2411.03865v3)

**Tags**: cs.MA cs.AI cs.GT cs.LG cs.SI 



### Measuring Human and AI Values Based on Generative Psychometrics with   Large Language Models
**Authors**: Haoran Ye, Yuhang Xie, Yuanyi Ren, Hanjun Fang, Xin Zhang, Guojie Song

**Updated**: 2024-12-20T08:35:24Z

**Summary**: Human values and their measurement are long-standing interdisciplinary inquiry. Recent advances in AI have sparked renewed interest in this area, with large language models (LLMs) emerging as both tools and subjects of value measurement. This work introduces Generative Psychometrics for Values (GPV), an LLM-based, data-driven value measurement paradigm, theoretically grounded in text-revealed selective perceptions. The core idea is to dynamically parse unstructured texts into perceptions akin to static stimuli in traditional psychometrics, measure the value orientations they reveal, and aggregate the results. Applying GPV to human-authored blogs, we demonstrate its stability, validity, and superiority over prior psychological tools. Then, extending GPV to LLM value measurement, we advance the current art with 1) a psychometric methodology that measures LLM values based on their scalable and free-form outputs, enabling context-specific measurement; 2) a comparative analysis of measurement paradigms, indicating response biases of prior methods; and 3) an attempt to bridge LLM values and their safety, revealing the predictive power of different value systems and the impacts of various values on LLM safety. Through interdisciplinary efforts, we aim to leverage AI for next-generation psychometrics and psychometrics for value-aligned AI.

**Link**: [arxiv](http://arxiv.org/abs/2409.12106v2),  [pdf](http://arxiv.org/pdf/2409.12106v2)

**Tags**: cs.CL cs.AI 



### Adaptable and Precise: Enterprise-Scenario LLM Function-Calling   Capability Training Pipeline
**Authors**: Guancheng Zeng, Wentao Ding, Beining Xu, Chi Zhang, Wenqiang Han, Gang Li, Jingjing Mo, Pengxu Qiu, Xinran Tao, Wang Tao, Haowen Hu

**Updated**: 2024-12-20T08:20:21Z

**Summary**: Enterprises possess a vast array of API assets scattered across various functions, forming the backbone of existing business processes. By leveraging these APIs as functional tools, enterprises can design diverse, scenario-specific agent applications, driven by on-premise function-calling models as the core engine. However, generic models often fail to meet enterprise requirements in terms of computational efficiency, output accuracy, and stability, necessitating scenario-specific adaptation. In this paper, we propose a training pipeline for function-calling capabilities tailored to real-world business scenarios. This pipeline includes the synthesis and augmentation of scenario-specific function-calling data, model fine-tuning, and performance evaluation and analysis. Using this pipeline, we generated 1,260 fully AI-generated samples and 1,035 augmented manually-labeled samples in digital HR agent scenario. The Qwen2.5-Coder-7B-Instruct model was employed as the base model and fine-tuned using the LoRA method on four GPUs with 24GB VRAM. Our fine-tuned model demonstrated outstanding performance in evaluations and practical applications, surpassing GPT-4 and GPT-4o in accuracy on the test set. These results validate the reliability of the proposed pipeline for training scenario-specific function-calling models.

**Link**: [arxiv](http://arxiv.org/abs/2412.15660v1),  [pdf](http://arxiv.org/pdf/2412.15660v1)

**Tags**: cs.AI cs.CL cs.SE 



### MathSpeech: Leveraging Small LMs for Accurate Conversion in Mathematical   Speech-to-Formula
**Authors**: Sieun Hyeon, Kyudan Jung, Jaehee Won, Nam-Joon Kim, Hyun Gon Ryu, Hyuk-Jae Lee, Jaeyoung Do

**Updated**: 2024-12-20T08:13:05Z

**Summary**: In various academic and professional settings, such as mathematics lectures or research presentations, it is often necessary to convey mathematical expressions orally. However, reading mathematical expressions aloud without accompanying visuals can significantly hinder comprehension, especially for those who are hearing-impaired or rely on subtitles due to language barriers. For instance, when a presenter reads Euler's Formula, current Automatic Speech Recognition (ASR) models often produce a verbose and error-prone textual description (e.g., e to the power of i x equals cosine of x plus i $\textit{side}$ of x), instead of the concise $\LaTeX{}$ format (i.e., $ e^{ix} = \cos(x) + i\sin(x) $), which hampers clear understanding and communication. To address this issue, we introduce MathSpeech, a novel pipeline that integrates ASR models with small Language Models (sLMs) to correct errors in mathematical expressions and accurately convert spoken expressions into structured $\LaTeX{}$ representations. Evaluated on a new dataset derived from lecture recordings, MathSpeech demonstrates $\LaTeX{}$ generation capabilities comparable to leading commercial Large Language Models (LLMs), while leveraging fine-tuned small language models of only 120M parameters. Specifically, in terms of CER, BLEU, and ROUGE scores for $\LaTeX{}$ translation, MathSpeech demonstrated significantly superior capabilities compared to GPT-4o. We observed a decrease in CER from 0.390 to 0.298, and higher ROUGE/BLEU scores compared to GPT-4o.

**Link**: [arxiv](http://arxiv.org/abs/2412.15655v1),  [pdf](http://arxiv.org/pdf/2412.15655v1)

**Tags**: cs.CL cs.AI 



### Darkit: A User-Friendly Software Toolkit for Spiking Large Language   Model
**Authors**: Xin Du, Shifan Ye, Qian Zheng, Yangfan Hu, Rui Yan, Shunyu Qi, Shuyang Chen, Huajin Tang, Gang Pan, Shuiguang Deng

**Updated**: 2024-12-20T07:50:08Z

**Summary**: Large language models (LLMs) have been widely applied in various practical applications, typically comprising billions of parameters, with inference processes requiring substantial energy and computational resources. In contrast, the human brain, employing bio-plausible spiking mechanisms, can accomplish the same tasks while significantly reducing energy consumption, even with a similar number of parameters. Based on this, several pioneering researchers have proposed and implemented various large language models that leverage spiking neural networks. They have demonstrated the feasibility of these models, validated their performance, and open-sourced their frameworks and partial source code. To accelerate the adoption of brain-inspired large language models and facilitate secondary development for researchers, we are releasing a software toolkit named DarwinKit (Darkit). The toolkit is designed specifically for learners, researchers, and developers working on spiking large models, offering a suite of highly user-friendly features that greatly simplify the learning, deployment, and development processes.

**Link**: [arxiv](http://arxiv.org/abs/2412.15634v1),  [pdf](http://arxiv.org/pdf/2412.15634v1)

**Tags**: cs.SE 



### DiveR-CT: Diversity-enhanced Red Teaming Large Language Model Assistants   with Relaxing Constraints
**Authors**: Andrew Zhao, Quentin Xu, Matthieu Lin, Shenzhi Wang, Yong-jin Liu, Zilong Zheng, Gao Huang

**Updated**: 2024-12-20T07:37:32Z

**Summary**: Recent advances in large language model assistants have made them indispensable, raising significant concerns over managing their safety. Automated red teaming offers a promising alternative to the labor-intensive and error-prone manual probing for vulnerabilities, providing more consistent and scalable safety evaluations. However, existing approaches often compromise diversity by focusing on maximizing attack success rate. Additionally, methods that decrease the cosine similarity from historical embeddings with semantic diversity rewards lead to novelty stagnation as history grows. To address these issues, we introduce DiveR-CT, which relaxes conventional constraints on the objective and semantic reward, granting greater freedom for the policy to enhance diversity. Our experiments demonstrate DiveR-CT's marked superiority over baselines by 1) generating data that perform better in various diversity metrics across different attack success rate levels, 2) better-enhancing resiliency in blue team models through safety tuning based on collected data, 3) allowing dynamic control of objective weights for reliable and controllable attack success rates, and 4) reducing susceptibility to reward overoptimization. Overall, our method provides an effective and efficient approach to LLM red teaming, accelerating real-world deployment.

**Link**: [arxiv](http://arxiv.org/abs/2405.19026v2),  [pdf](http://arxiv.org/pdf/2405.19026v2)

**Tags**: cs.LG cs.AI cs.CL cs.CR 



### Can Input Attributions Interpret the Inductive Reasoning Process   Elicited in In-Context Learning?
**Authors**: Mengyu Ye, Tatsuki Kuribayashi, Goro Kobayashi, Jun Suzuki

**Updated**: 2024-12-20T07:35:42Z

**Summary**: Elucidating the rationale behind neural models' outputs has been challenging in the machine learning field, which is indeed applicable in this age of large language models (LLMs) and in-context learning (ICL). When it comes to estimating input attributions (IA), ICL poses a new issue of interpreting which example in the prompt, consisting of a set of examples, contributed to identifying the task/rule to be solved. To this end, in this paper, we introduce synthetic diagnostic tasks inspired by the poverty of the stimulus design in inductive reasoning; here, most in-context examples are ambiguous w.r.t. their underlying rule, and one critical example disambiguates the task demonstrated. The question is whether conventional IA methods can identify such an example in interpreting the inductive reasoning process in ICL. Our experiments provide several practical findings; for example, a certain simple IA method works the best, and the larger the model, the generally harder it is to interpret the ICL with gradient-based IA methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.15628v1),  [pdf](http://arxiv.org/pdf/2412.15628v1)

**Tags**: cs.CL 



### JailPO: A Novel Black-box Jailbreak Framework via Preference   Optimization against Aligned LLMs
**Authors**: Hongyi Li, Jiawei Ye, Jie Wu, Tianjie Yan, Chu Wang, Zhixin Li

**Updated**: 2024-12-20T07:29:10Z

**Summary**: Large Language Models (LLMs) aligned with human feedback have recently garnered significant attention. However, it remains vulnerable to jailbreak attacks, where adversaries manipulate prompts to induce harmful outputs. Exploring jailbreak attacks enables us to investigate the vulnerabilities of LLMs and further guides us in enhancing their security. Unfortunately, existing techniques mainly rely on handcrafted templates or generated-based optimization, posing challenges in scalability, efficiency and universality. To address these issues, we present JailPO, a novel black-box jailbreak framework to examine LLM alignment. For scalability and universality, JailPO meticulously trains attack models to automatically generate covert jailbreak prompts. Furthermore, we introduce a preference optimization-based attack method to enhance the jailbreak effectiveness, thereby improving efficiency. To analyze model vulnerabilities, we provide three flexible jailbreak patterns. Extensive experiments demonstrate that JailPO not only automates the attack process while maintaining effectiveness but also exhibits superior performance in efficiency, universality, and robustness against defenses compared to baselines. Additionally, our analysis of the three JailPO patterns reveals that attacks based on complex templates exhibit higher attack strength, whereas covert question transformations elicit riskier responses and are more likely to bypass defense mechanisms.

**Link**: [arxiv](http://arxiv.org/abs/2412.15623v1),  [pdf](http://arxiv.org/pdf/2412.15623v1)

**Tags**: cs.CR cs.AI 



### TouchASP: Elastic Automatic Speech Perception that Everyone Can Touch
**Authors**: Xingchen Song, Chengdong Liang, Binbin Zhang, Pengshen Zhang, ZiYu Wang, Youcheng Ma, Menglong Xu, Lin Wang, Di Wu, Fuping Pan, Dinghao Zhou, Zhendong Peng

**Updated**: 2024-12-20T07:28:04Z

**Summary**: Large Automatic Speech Recognition (ASR) models demand a vast number of parameters, copious amounts of data, and significant computational resources during the training process. However, such models can merely be deployed on high-compute cloud platforms and are only capable of performing speech recognition tasks. This leads to high costs and restricted capabilities. In this report, we initially propose the elastic mixture of the expert (eMoE) model. This model can be trained just once and then be elastically scaled in accordance with deployment requirements. Secondly, we devise an unsupervised data creation and validation procedure and gather millions of hours of audio data from diverse domains for training. Using these two techniques, our system achieves elastic deployment capabilities while reducing the Character Error Rate (CER) on the SpeechIO testsets from 4.98\% to 2.45\%. Thirdly, our model is not only competent in Mandarin speech recognition but also proficient in multilingual, multi-dialect, emotion, gender, and sound event perception. We refer to this as Automatic Speech Perception (ASP), and the perception results are presented in the experimental section.

**Link**: [arxiv](http://arxiv.org/abs/2412.15622v1),  [pdf](http://arxiv.org/pdf/2412.15622v1)

**Tags**: eess.AS cs.CL eess.SP 



### Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool   Usage
**Authors**: Zhi Gao, Bofei Zhang, Pengxiang Li, Xiaojian Ma, Tao Yuan, Yue Fan, Yuwei Wu, Yunde Jia, Song-Chun Zhu, Qing Li

**Updated**: 2024-12-20T07:00:46Z

**Summary**: The advancement of large language models (LLMs) prompts the development of multi-modal agents, which are used as a controller to call external tools, providing a feasible way to solve practical tasks. In this paper, we propose a multi-modal agent tuning method that automatically generates multi-modal tool-usage data and tunes a vision-language model (VLM) as the controller for powerful tool-usage reasoning. To preserve the data quality, we prompt the GPT-4o mini model to generate queries, files, and trajectories, followed by query-file and trajectory verifiers. Based on the data synthesis pipeline, we collect the MM-Traj dataset that contains 20K tasks with trajectories of tool usage. Then, we develop the T3-Agent via \underline{T}rajectory \underline{T}uning on VLMs for \underline{T}ool usage using MM-Traj. Evaluations on the GTA and GAIA benchmarks show that the T3-Agent consistently achieves improvements on two popular VLMs: MiniCPM-V-8.5B and {Qwen2-VL-7B}, which outperforms untrained VLMs by $20\%$, showing the effectiveness of the proposed data synthesis pipeline, leading to high-quality data for tool-usage capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2412.15606v1),  [pdf](http://arxiv.org/pdf/2412.15606v1)

**Tags**: cs.AI cs.CV 



### Don't Do RAG: When Cache-Augmented Generation is All You Need for   Knowledge Tasks
**Authors**: Brian J Chan, Chao-Ting Chen, Jui-Hung Cheng, Hen-Hsen Huang

**Updated**: 2024-12-20T06:58:32Z

**Summary**: Retrieval-augmented generation (RAG) has gained traction as a powerful approach for enhancing language models by integrating external knowledge sources. However, RAG introduces challenges such as retrieval latency, potential errors in document selection, and increased system complexity. With the advent of large language models (LLMs) featuring significantly extended context windows, this paper proposes an alternative paradigm, cache-augmented generation (CAG) that bypasses real-time retrieval. Our method involves preloading all relevant resources, especially when the documents or knowledge for retrieval are of a limited and manageable size, into the LLM's extended context and caching its runtime parameters. During inference, the model utilizes these preloaded parameters to answer queries without additional retrieval steps. Comparative analyses reveal that CAG eliminates retrieval latency and minimizes retrieval errors while maintaining context relevance. Performance evaluations across multiple benchmarks highlight scenarios where long-context LLMs either outperform or complement traditional RAG pipelines. These findings suggest that, for certain applications, particularly those with a constrained knowledge base, CAG provide a streamlined and efficient alternative to RAG, achieving comparable or superior results with reduced complexity.

**Link**: [arxiv](http://arxiv.org/abs/2412.15605v1),  [pdf](http://arxiv.org/pdf/2412.15605v1)

**Tags**: cs.CL 



### Recording for Eyes, Not Echoing to Ears: Contextualized   Spoken-to-Written Conversion of ASR Transcripts
**Authors**: Jiaqing Liu, Chong Deng, Qinglin Zhang, Shilin Zhou, Qian Chen, Hai Yu, Wen Wang

**Updated**: 2024-12-20T06:57:52Z

**Summary**: Automatic Speech Recognition (ASR) transcripts exhibit recognition errors and various spoken language phenomena such as disfluencies, ungrammatical sentences, and incomplete sentences, hence suffering from poor readability. To improve readability, we propose a Contextualized Spoken-to-Written conversion (CoS2W) task to address ASR and grammar errors and also transfer the informal text into the formal style with content preserved, utilizing contexts and auxiliary information. This task naturally matches the in-context learning capabilities of Large Language Models (LLMs). To facilitate comprehensive comparisons of various LLMs, we construct a document-level Spoken-to-Written conversion of ASR Transcripts Benchmark (SWAB) dataset. Using SWAB, we study the impact of different granularity levels on the CoS2W performance, and propose methods to exploit contexts and auxiliary information to enhance the outputs. Experimental results reveal that LLMs have the potential to excel in the CoS2W task, particularly in grammaticality and formality, our methods achieve effective understanding of contexts and auxiliary information by LLMs. We further investigate the effectiveness of using LLMs as evaluators and find that LLM evaluators show strong correlations with human evaluations on rankings of faithfulness and formality, which validates the reliability of LLM evaluators for the CoS2W task.

**Link**: [arxiv](http://arxiv.org/abs/2408.09688v3),  [pdf](http://arxiv.org/pdf/2408.09688v3)

**Tags**: cs.CL 



### Template-Driven LLM-Paraphrased Framework for Tabular Math Word Problem   Generation
**Authors**: Xiaoqiang Kang, Zimu Wang, Xiaobo Jin, Wei Wang, Kaizhu Huang, Qiufeng Wang

**Updated**: 2024-12-20T06:34:57Z

**Summary**: Solving tabular math word problems (TMWPs) has become a critical role in evaluating the mathematical reasoning ability of large language models (LLMs), where large-scale TMWP samples are commonly required for LLM fine-tuning. Since the collection of high-quality TMWP datasets is costly and time-consuming, recent research has concentrated on automatic TMWP generation. However, current generated samples usually suffer from issues of either correctness or diversity. In this paper, we propose a Template-driven LLM-paraphrased (TeLL) framework for generating high-quality TMWP samples with diverse backgrounds and accurate tables, questions, answers, and solutions. To this end, we first extract templates from existing real samples to generate initial problems, ensuring correctness. Then, we adopt an LLM to extend templates and paraphrase problems, obtaining diverse TMWP samples. Furthermore, we find the reasoning annotation is important for solving TMWPs. Therefore, we propose to enrich each solution with illustrative reasoning steps. Through the proposed framework, we construct a high-quality dataset TabMWP-TeLL by adhering to the question types in the TabMWP dataset, and we conduct extensive experiments on a variety of LLMs to demonstrate the effectiveness of TabMWP-TeLL in improving TMWP solving performance. The code and data of this paper are available at: https://github.com/Jason8Kang/TELL.

**Link**: [arxiv](http://arxiv.org/abs/2412.15594v1),  [pdf](http://arxiv.org/pdf/2412.15594v1)

**Tags**: cs.CL 



### ExpeL: LLM Agents Are Experiential Learners
**Authors**: Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang

**Updated**: 2024-12-20T06:14:53Z

**Summary**: The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model's generalization capabilities. Moreover, state-of-the-art language models like GPT-4 and Claude are primarily accessible through API calls, with their parametric weights remaining proprietary and unavailable to the public. This scenario emphasizes the growing need for new methodologies that allow learning from agent experiences without requiring parametric updates. To address these problems, we introduce the Experiential Learning (ExpeL) agent. Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions. Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences. We further explore the emerging capabilities and transfer learning potential of the ExpeL agent through qualitative observations and additional experiments.

**Link**: [arxiv](http://arxiv.org/abs/2308.10144v3),  [pdf](http://arxiv.org/pdf/2308.10144v3)

**Tags**: cs.LG cs.AI cs.CL 



### LLM-Based Multi-Agent Systems for Software Engineering: Literature   Review, Vision and the Road Ahead
**Authors**: Junda He, Christoph Treude, David Lo

**Updated**: 2024-12-20T06:01:33Z

**Summary**: Integrating Large Language Models (LLMs) into autonomous agents marks a significant shift in the research landscape by offering cognitive abilities that are competitive with human planning and reasoning. This paper explores the transformative potential of integrating Large Language Models into Multi-Agent (LMA) systems for addressing complex challenges in software engineering (SE). By leveraging the collaborative and specialized abilities of multiple agents, LMA systems enable autonomous problem-solving, improve robustness, and provide scalable solutions for managing the complexity of real-world software projects. In this paper, we conduct a systematic review of recent primary studies to map the current landscape of LMA applications across various stages of the software development lifecycle (SDLC). To illustrate current capabilities and limitations, we perform two case studies to demonstrate the effectiveness of state-of-the-art LMA frameworks. Additionally, we identify critical research gaps and propose a comprehensive research agenda focused on enhancing individual agent capabilities and optimizing agent synergy. Our work outlines a forward-looking vision for developing fully autonomous, scalable, and trustworthy LMA systems, laying the foundation for the evolution of Software Engineering 2.0.

**Link**: [arxiv](http://arxiv.org/abs/2404.04834v3),  [pdf](http://arxiv.org/pdf/2404.04834v3)

**Tags**: cs.SE 



### NeSyCoCo: A Neuro-Symbolic Concept Composer for Compositional   Generalization
**Authors**: Danial Kamali, Elham J. Barezi, Parisa Kordjamshidi

**Updated**: 2024-12-20T05:48:58Z

**Summary**: Compositional generalization is crucial for artificial intelligence agents to solve complex vision-language reasoning tasks. Neuro-symbolic approaches have demonstrated promise in capturing compositional structures, but they face critical challenges: (a) reliance on predefined predicates for symbolic representations that limit adaptability, (b) difficulty in extracting predicates from raw data, and (c) using non-differentiable operations for combining primitive concepts. To address these issues, we propose NeSyCoCo, a neuro-symbolic framework that leverages large language models (LLMs) to generate symbolic representations and map them to differentiable neural computations. NeSyCoCo introduces three innovations: (a) augmenting natural language inputs with dependency structures to enhance the alignment with symbolic representations, (b) employing distributed word representations to link diverse, linguistically motivated logical predicates to neural modules, and (c) using the soft composition of normalized predicate scores to align symbolic and differentiable reasoning. Our framework achieves state-of-the-art results on the ReaSCAN and CLEVR-CoGenT compositional generalization benchmarks and demonstrates robust performance with novel concepts in the CLEVR-SYN benchmark.

**Link**: [arxiv](http://arxiv.org/abs/2412.15588v1),  [pdf](http://arxiv.org/pdf/2412.15588v1)

**Tags**: cs.CL 



### AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark
**Authors**: Jianlyu Chen, Nan Wang, Chaofan Li, Bo Wang, Shitao Xiao, Han Xiao, Hao Liao, Defu Lian, Zheng Liu

**Updated**: 2024-12-20T05:42:38Z

**Summary**: Evaluation plays a crucial role in the advancement of information retrieval (IR) models. However, current benchmarks, which are based on predefined domains and human-labeled data, face limitations in addressing evaluation needs for emerging domains both cost-effectively and efficiently. To address this challenge, we propose the Automated Heterogeneous Information Retrieval Benchmark (AIR-Bench). AIR-Bench is distinguished by three key features: 1) Automated. The testing data in AIR-Bench is automatically generated by large language models (LLMs) without human intervention. 2) Heterogeneous. The testing data in AIR-Bench is generated with respect to diverse tasks, domains and languages. 3) Dynamic. The domains and languages covered by AIR-Bench are constantly augmented to provide an increasingly comprehensive evaluation benchmark for community developers. We develop a reliable and robust data generation pipeline to automatically create diverse and high-quality evaluation datasets based on real-world corpora. Our findings demonstrate that the generated testing data in AIR-Bench aligns well with human-labeled testing data, making AIR-Bench a dependable benchmark for evaluating IR models. The resources in AIR-Bench are publicly available at https://github.com/AIR-Bench/AIR-Bench.

**Link**: [arxiv](http://arxiv.org/abs/2412.13102v3),  [pdf](http://arxiv.org/pdf/2412.13102v3)

**Tags**: cs.IR cs.CL 



### To Rely or Not to Rely? Evaluating Interventions for Appropriate   Reliance on Large Language Models
**Authors**: Jessica Y. Bo, Sophia Wan, Ashton Anderson

**Updated**: 2024-12-20T05:40:32Z

**Summary**: As Large Language Models become integral to decision-making, optimism about their power is tempered with concern over their errors. Users may over-rely on LLM advice that is confidently stated but wrong, or under-rely due to mistrust. Reliance interventions have been developed to help users of LLMs, but they lack rigorous evaluation for appropriate reliance. We benchmark the performance of three relevant interventions by conducting a randomized online experiment with 400 participants attempting two challenging tasks: LSAT logical reasoning and image-based numerical estimation. For each question, participants first answered independently, then received LLM advice modified by one of three reliance interventions and answered the question again. Our findings indicate that while interventions reduce over-reliance, they generally fail to improve appropriate reliance. Furthermore, people became more confident after making incorrect reliance decisions in certain contexts, demonstrating poor calibration. Based on our findings, we discuss implications for designing effective reliance interventions in human-LLM collaboration.

**Link**: [arxiv](http://arxiv.org/abs/2412.15584v1),  [pdf](http://arxiv.org/pdf/2412.15584v1)

**Tags**: cs.HC 



### Combining Domain-Specific Models and LLMs for Automated Disease   Phenotyping from Survey Data
**Authors**: Gal Beeri, Benoit Chamot, Elena Latchem, Shruthi Venkatesh, Sarah Whalan, Van Zyl Kruger, David Martino

**Updated**: 2024-12-20T05:38:58Z

**Summary**: This exploratory pilot study investigated the potential of combining a domain-specific model, BERN2, with large language models (LLMs) to enhance automated disease phenotyping from research survey data. Motivated by the need for efficient and accurate methods to harmonize the growing volume of survey data with standardized disease ontologies, we employed BERN2, a biomedical named entity recognition and normalization model, to extract disease information from the ORIGINS birth cohort survey data. After rigorously evaluating BERN2's performance against a manually curated ground truth dataset, we integrated various LLMs using prompt engineering, Retrieval-Augmented Generation (RAG), and Instructional Fine-Tuning (IFT) to refine the model's outputs. BERN2 demonstrated high performance in extracting and normalizing disease mentions, and the integration of LLMs, particularly with Few Shot Inference and RAG orchestration, further improved accuracy. This approach, especially when incorporating structured examples, logical reasoning prompts, and detailed context, offers a promising avenue for developing tools to enable efficient cohort profiling and data harmonization across large, heterogeneous research datasets.

**Link**: [arxiv](http://arxiv.org/abs/2410.20695v2),  [pdf](http://arxiv.org/pdf/2410.20695v2)

**Tags**: cs.CL 



### Towards the Scalable Fabrication of thin-film Superconducting Parametric   Amplifiers
**Authors**: Abdallah El Kass, Kevin A. F. Simoes, Cassandra Chua, David J. Reilly, Kun Zuo, Thomas A. Ohki

**Updated**: 2024-12-20T05:24:42Z

**Summary**: Kinetic inductance travelling-wave parametric amplifiers (KTWPAs) are emerging as core components in many applications where wideband cryogenic rf amplification at or near the quantum limit of added noise is critical. These thin film superconducting devices are unique in their ability to simultaneously provide large dynamic range and quantum-limited amplification of single photon to 100,000s of photon signals. Despite the promising performance of co-planar NbTiN thin-film KTWPAs, the original promise of a "simple" single-layer metal fabrication has encountered roadblocks and their broader adoption has been hindered by low fabrication yield. In this work, we present a post-lithography correction technique that eliminates short circuits, significantly improving yield and enabling reliable wafer-scale production. Using automated image acquisition, error analysis, and correction, we successfully fabricated operational KTWPAs on high-resistivity silicon, achieving > 10 dB between 2 - 4 GHz. This approach paves the way for the scaling up manufacturing of KTWPAs, positioning them for widespread deployment in quantum technologies.

**Link**: [arxiv](http://arxiv.org/abs/2410.17512v2),  [pdf](http://arxiv.org/pdf/2410.17512v2)

**Tags**: cond-mat.mes-hall 



### Towards Unifying Evaluation of Counterfactual Explanations: Leveraging   Large Language Models for Human-Centric Assessments
**Authors**: Marharyta Domnich, Julius Valja, Rasmus Moorits Veski, Giacomo Magnifico, Kadi Tulver, Eduard Barbu, Raul Vicente

**Updated**: 2024-12-20T05:20:50Z

**Summary**: As machine learning models evolve, maintaining transparency demands more human-centric explainable AI techniques. Counterfactual explanations, with roots in human reasoning, identify the minimal input changes needed to obtain a given output and, hence, are crucial for supporting decision-making. Despite their importance, the evaluation of these explanations often lacks grounding in user studies and remains fragmented, with existing metrics not fully capturing human perspectives. To address this challenge, we developed a diverse set of 30 counterfactual scenarios and collected ratings across 8 evaluation metrics from 206 respondents. Subsequently, we fine-tuned different Large Language Models (LLMs) to predict average or individual human judgment across these metrics. Our methodology allowed LLMs to achieve an accuracy of up to 63% in zero-shot evaluations and 85% (over a 3-classes prediction) with fine-tuning across all metrics. The fine-tuned models predicting human ratings offer better comparability and scalability in evaluating different counterfactual explanation frameworks.

**Link**: [arxiv](http://arxiv.org/abs/2410.21131v2),  [pdf](http://arxiv.org/pdf/2410.21131v2)

**Tags**: cs.AI cs.CL 



### J-EDI QA: Benchmark for deep-sea organism-specific multimodal LLM
**Authors**: Takero Yoshida, Yuikazu Ito, Yoshihiro Fujiwara, Shinji Tsuchida, Daisuke Sugiyama, Daisuke Matsuoka

**Updated**: 2024-12-20T05:11:51Z

**Summary**: Japan Agency for Marine-Earth Science and Technology (JAMSTEC) has made available the JAMSTEC Earth Deep-sea Image (J-EDI), a deep-sea video and image archive (https://www.godac.jamstec.go.jp/jedi/e/index.html). This archive serves as a valuable resource for researchers and scholars interested in deep-sea imagery. The dataset comprises images and videos of deep-sea phenomena, predominantly of marine organisms, but also of the seafloor and physical processes. In this study, we propose J-EDI QA, a benchmark for understanding images of deep-sea organisms using a multimodal large language model (LLM). The benchmark is comprised of 100 images, accompanied by questions and answers with four options by JAMSTEC researchers for each image. The QA pairs are provided in Japanese, and the benchmark assesses the ability to understand deep-sea species in Japanese. In the evaluation presented in this paper, OpenAI o1 achieved a 50% correct response rate. This result indicates that even with the capabilities of state-of-the-art models as of December 2024, deep-sea species comprehension is not yet at an expert level. Further advances in deep-sea species-specific LLMs are therefore required.

**Link**: [arxiv](http://arxiv.org/abs/2412.15574v1),  [pdf](http://arxiv.org/pdf/2412.15574v1)

**Tags**: cs.CV 



### Improving Zero-shot LLM Re-Ranker with Risk Minimization
**Authors**: Xiaowei Yuan, Zhao Yang, Yequan Wang, Jun Zhao, Kang Liu

**Updated**: 2024-12-20T04:59:10Z

**Summary**: In the Retrieval-Augmented Generation (RAG) system, advanced Large Language Models (LLMs) have emerged as effective Query Likelihood Models (QLMs) in an unsupervised way, which re-rank documents based on the probability of generating the query given the content of a document. However, directly prompting LLMs to approximate QLMs inherently is biased, where the estimated distribution might diverge from the actual document-specific distribution. In this study, we introduce a novel framework, $\mathrm{UR^3}$, which leverages Bayesian decision theory to both quantify and mitigate this estimation bias. Specifically, $\mathrm{UR^3}$ reformulates the problem as maximizing the probability of document generation, thereby harmonizing the optimization of query and document generation probabilities under a unified risk minimization objective. Our empirical results indicate that $\mathrm{UR^3}$ significantly enhances re-ranking, particularly in improving the Top-1 accuracy. It benefits the QA tasks by achieving higher accuracy with fewer input documents.

**Link**: [arxiv](http://arxiv.org/abs/2406.13331v2),  [pdf](http://arxiv.org/pdf/2406.13331v2)

**Tags**: cs.CL 



### In-context Continual Learning Assisted by an External Continual Learner
**Authors**: Saleh Momeni, Sahisnu Mazumder, Zixuan Ke, Bing Liu

**Updated**: 2024-12-20T04:44:41Z

**Summary**: Existing continual learning (CL) methods mainly rely on fine-tuning or adapting large language models (LLMs). They still suffer from catastrophic forgetting (CF). Little work has been done to exploit in-context learning (ICL) to leverage the extensive knowledge within LLMs for CL without updating any parameters. However, incrementally learning each new task in ICL necessitates adding training examples from each class of the task to the prompt, which hampers scalability as the prompt length increases. This issue not only leads to excessively long prompts that exceed the input token limit of the underlying LLM but also degrades the model's performance due to the overextended context. To address this, we introduce InCA, a novel approach that integrates an external continual learner (ECL) with ICL to enable scalable CL without CF. The ECL is built incrementally to pre-select a small subset of likely classes for each test instance. By restricting the ICL prompt to only these selected classes, InCA prevents prompt lengths from becoming excessively long, while maintaining high performance. Experimental results demonstrate that InCA significantly outperforms existing CL baselines, achieving substantial performance gains.

**Link**: [arxiv](http://arxiv.org/abs/2412.15563v1),  [pdf](http://arxiv.org/pdf/2412.15563v1)

**Tags**: cs.CL cs.AI cs.LG 



### MORTAR: Metamorphic Multi-turn Testing for LLM-based Dialogue Systems
**Authors**: Guoxiang Guo, Aldeida Aleti, Neelofar Neelofar, Chakkrit Tantithamthavorn

**Updated**: 2024-12-20T04:31:03Z

**Summary**: With the widespread application of LLM-based dialogue systems in daily life, quality assurance has become more important than ever. Recent research has successfully introduced methods to identify unexpected behaviour in single-turn scenarios. However, multi-turn dialogue testing remains underexplored, with the Oracle problem in multi-turn testing posing a persistent challenge for dialogue system developers and researchers. In this paper, we propose MORTAR, a MetamORphic multi-TuRn diAlogue testing appRoach, which mitigates the test oracle problem in the assessment of LLM-based dialogue systems. MORTAR automates the generation of follow-up question-answer (QA) dialogue test cases with multiple dialogue-level perturbations and metamorphic relations. MORTAR employs a novel knowledge graph-based dialogue information model which effectively generates perturbed dialogue test datasets and detects bugs of multi-turn dialogue systems in a low-cost manner. The proposed approach does not require an LLM as a judge, eliminating potential of any biases in the evaluation step. According to the experiment results on multiple LLM-based dialogue systems and comparisons with single-turn metamorphic testing approaches, MORTAR explores more unique bugs in LLM-based dialogue systems, especially for severe bugs that MORTAR detects up to four times more unique bugs than the most effective existing metamorphic testing approach.

**Link**: [arxiv](http://arxiv.org/abs/2412.15557v1),  [pdf](http://arxiv.org/pdf/2412.15557v1)

**Tags**: cs.SE cs.CL 



### NGQA: A Nutritional Graph Question Answering Benchmark for Personalized   Health-aware Nutritional Reasoning
**Authors**: Zheyuan Zhang, Yiyang Li, Nhi Ha Lan Le, Zehong Wang, Tianyi Ma, Vincent Galassi, Keerthiram Murugesan, Nuno Moniz, Werner Geyer, Nitesh V Chawla, Chuxu Zhang, Yanfang Ye

**Updated**: 2024-12-20T04:13:46Z

**Summary**: Diet plays a critical role in human health, yet tailoring dietary reasoning to individual health conditions remains a major challenge. Nutrition Question Answering (QA) has emerged as a popular method for addressing this problem. However, current research faces two critical limitations. On one hand, the absence of datasets involving user-specific medical information severely limits \textit{personalization}. This challenge is further compounded by the wide variability in individual health needs. On the other hand, while large language models (LLMs), a popular solution for this task, demonstrate strong reasoning abilities, they struggle with the domain-specific complexities of personalized healthy dietary reasoning, and existing benchmarks fail to capture these challenges. To address these gaps, we introduce the Nutritional Graph Question Answering (NGQA) benchmark, the first graph question answering dataset designed for personalized nutritional health reasoning. NGQA leverages data from the National Health and Nutrition Examination Survey (NHANES) and the Food and Nutrient Database for Dietary Studies (FNDDS) to evaluate whether a food is healthy for a specific user, supported by explanations of the key contributing nutrients. The benchmark incorporates three question complexity settings and evaluates reasoning across three downstream tasks. Extensive experiments with LLM backbones and baseline models demonstrate that the NGQA benchmark effectively challenges existing models. In sum, NGQA addresses a critical real-world problem while advancing GraphQA research with a novel domain-specific benchmark.

**Link**: [arxiv](http://arxiv.org/abs/2412.15547v1),  [pdf](http://arxiv.org/pdf/2412.15547v1)

**Tags**: cs.CL cs.AI cs.LG 



### MRAG: A Modular Retrieval Framework for Time-Sensitive Question   Answering
**Authors**: Zhang Siyue, Xue Yuxiang, Zhang Yiming, Wu Xiaobao, Luu Anh Tuan, Zhao Chen

**Updated**: 2024-12-20T03:58:27Z

**Summary**: Understanding temporal relations and answering time-sensitive questions is crucial yet a challenging task for question-answering systems powered by large language models (LLMs). Existing approaches either update the parametric knowledge of LLMs with new facts, which is resource-intensive and often impractical, or integrate LLMs with external knowledge retrieval (i.e., retrieval-augmented generation). However, off-the-shelf retrievers often struggle to identify relevant documents that require intensive temporal reasoning. To systematically study time-sensitive question answering, we introduce the TempRAGEval benchmark, which repurposes existing datasets by incorporating temporal perturbations and gold evidence labels. As anticipated, all existing retrieval methods struggle with these temporal reasoning-intensive questions. We further propose Modular Retrieval (MRAG), a trainless framework that includes three modules: (1) Question Processing that decomposes question into a main content and a temporal constraint; (2) Retrieval and Summarization that retrieves evidence and uses LLMs to summarize according to the main content; (3) Semantic-Temporal Hybrid Ranking that scores each evidence summarization based on both semantic and temporal relevance. On TempRAGEval, MRAG significantly outperforms baseline retrievers in retrieval performance, leading to further improvements in final answer accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2412.15540v1),  [pdf](http://arxiv.org/pdf/2412.15540v1)

**Tags**: cs.CL 



### XRAG: eXamining the Core -- Benchmarking Foundational Components in   Advanced Retrieval-Augmented Generation
**Authors**: Qianren Mao, Yangyifei Luo, Jinlong Zhang, Hanwen Hao, Zhilong Cao, Xiaolong Wang, Xiao Guan, Zhenting Huang, Weifeng Jiang, Shuyu Guo, Zhentao Han, Qili Zhang, Siyuan Tao, Yujie Liu, Junnan Liu, Zhixing Tan, Jie Sun, Bo Li, Xudong Liu, Richong Zhang, Jianxin Li

**Updated**: 2024-12-20T03:37:07Z

**Summary**: Retrieval-augmented generation (RAG) synergizes the retrieval of pertinent data with the generative capabilities of Large Language Models (LLMs), ensuring that the generated output is not only contextually relevant but also accurate and current.We introduce XRAG, an open-source, modular codebase that facilitates exhaustive evaluation of the performance of foundational components of advanced RAG modules. These components are systematically categorized into four core phases: pre-retrieval, retrieval, post-retrieval, and generation. We systematically analyse them across reconfigured datasets, providing a comprehensive benchmark for their effectiveness. Given the escalating complexity of RAG systems, we underscore the necessity of identifying potential failure points of RAG modules. We formulate a suite of experimental methodologies and diagnostic testing protocols to dissect the failure points inherent in the engineering of RAG modules. Subsequently, we proffer bespoke solutions that are designed to augment the validation processes and bolster the overall performance of these modules. Our work thoroughly evaluates the performance of core advanced components in RAG systems, providing insights into optimizations for prevalent failure points.

**Link**: [arxiv](http://arxiv.org/abs/2412.15529v1),  [pdf](http://arxiv.org/pdf/2412.15529v1)

**Tags**: cs.CL cs.AI 



### HREF: Human Response-Guided Evaluation of Instruction Following in   Language Models
**Authors**: Xinxi Lyu, Yizhong Wang, Hannaneh Hajishirzi, Pradeep Dasigi

**Updated**: 2024-12-20T03:26:47Z

**Summary**: Evaluating the capability of Large Language Models (LLMs) in following instructions has heavily relied on a powerful LLM as the judge, introducing unresolved biases that deviate the judgments from human judges. In this work, we reevaluate various choices for automatic evaluation on a wide range of instruction-following tasks. We experiment with methods that leverage human-written responses and observe that they enhance the reliability of automatic evaluations across a wide range of tasks, resulting in up to a 3.2% improvement in agreement with human judges. We also discovered that human-written responses offer an orthogonal perspective to model-generated responses in following instructions and should be used as an additional context when comparing model responses. Based on these observations, we develop a new evaluation benchmark, Human Response-Guided Evaluation of Instruction Following (HREF), comprising 4,258 samples across 11 task categories with a composite evaluation setup, employing a composite evaluation setup that selects the most reliable method for each category. In addition to providing reliable evaluation, HREF emphasizes individual task performance and is free from contamination. Finally, we study the impact of key design choices in HREF, including the size of the evaluation set, the judge model, the baseline model, and the prompt template. We host a live leaderboard that evaluates LLMs on the private evaluation set of HREF.

**Link**: [arxiv](http://arxiv.org/abs/2412.15524v1),  [pdf](http://arxiv.org/pdf/2412.15524v1)

**Tags**: cs.CL cs.AI 



### PreNeT: Leveraging Computational Features to Predict Deep Neural Network   Training Time
**Authors**: Alireza Pourali, Arian Boukani, Hamzeh Khazaei

**Updated**: 2024-12-20T03:15:02Z

**Summary**: Training deep learning models, particularly Transformer-based architectures such as Large Language Models (LLMs), demands substantial computational resources and extended training periods. While optimal configuration and infrastructure selection can significantly reduce associated costs, this optimization requires preliminary analysis tools. This paper introduces PreNeT, a novel predictive framework designed to address this optimization challenge. PreNeT facilitates training optimization by integrating comprehensive computational metrics, including layer-specific parameters, arithmetic operations and memory utilization. A key feature of PreNeT is its capacity to accurately predict training duration on previously unexamined hardware infrastructures, including novel accelerator architectures. This framework employs a sophisticated approach to capture and analyze the distinct characteristics of various neural network layers, thereby enhancing existing prediction methodologies. Through proactive implementation of PreNeT, researchers and practitioners can determine optimal configurations, parameter settings, and hardware specifications to maximize cost-efficiency and minimize training duration. Experimental results demonstrate that PreNeT achieves up to 72% improvement in prediction accuracy compared to contemporary state-of-the-art frameworks.

**Link**: [arxiv](http://arxiv.org/abs/2412.15519v1),  [pdf](http://arxiv.org/pdf/2412.15519v1)

**Tags**: cs.LG 



### Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced   Retrieval-Augmented Generation on Knowledge Graphs
**Authors**: Xiaqiang Tang, Jian Li, Nan Du, Sihong Xie

**Updated**: 2024-12-20T03:12:49Z

**Summary**: Despite the superior performance of Large language models on many NLP tasks, they still face significant limitations in memorizing extensive world knowledge. Recent studies have demonstrated that leveraging the Retrieval-Augmented Generation (RAG) framework, combined with Knowledge Graphs that encapsulate extensive factual data in a structured format, robustly enhances the reasoning capabilities of LLMs. However, deploying such systems in real-world scenarios presents challenges: the continuous evolution of non-stationary environments may lead to performance degradation and user satisfaction requires a careful balance of performance and responsiveness. To address these challenges, we introduce a Multi-objective Multi-Armed Bandit enhanced RAG framework, supported by multiple retrieval methods with diverse capabilities under rich and evolving retrieval contexts in practice. Within this framework, each retrieval method is treated as a distinct ``arm''. The system utilizes real-time user feedback to adapt to dynamic environments, by selecting the appropriate retrieval method based on input queries and the historical multi-objective performance of each arm. Extensive experiments conducted on two benchmark KGQA datasets demonstrate that our method significantly outperforms baseline methods in non-stationary settings while achieving state-of-the-art performance in stationary environments. Code and data are available at https://github.com/FUTUREEEEEE/Dynamic-RAG.git

**Link**: [arxiv](http://arxiv.org/abs/2412.07618v2),  [pdf](http://arxiv.org/pdf/2412.07618v2)

**Tags**: cs.AI cs.CL 



### Towards Efficient Object Re-Identification with A Novel Cloud-Edge   Collaborative Framework
**Authors**: Chuanming Wang, Yuxin Yang, Mengshi Qi, Huadong Ma

**Updated**: 2024-12-20T03:10:55Z

**Summary**: Object re-identification (ReID) is committed to searching for objects of the same identity across cameras, and its real-world deployment is gradually increasing. Current ReID methods assume that the deployed system follows the centralized processing paradigm, i.e., all computations are conducted in the cloud server and edge devices are only used to capture images. As the number of videos experiences a rapid escalation, this paradigm has become impractical due to the finite computational resources in the cloud server. Therefore, the ReID system should be converted to fit in the cloud-edge collaborative processing paradigm, which is crucial to boost its scalability and practicality. However, current works lack relevant research on this important specific issue, making it difficult to adapt them into a cloud-edge framework effectively. In this paper, we propose a cloud-edge collaborative inference framework for ReID systems, aiming to expedite the return of the desired image captured by the camera to the cloud server by learning the spatial-temporal correlations among objects. In the system, a Distribution-aware Correlation Modeling network (DaCM) is particularly proposed to embed the spatial-temporal correlations of the camera network implicitly into a graph structure, and it can be applied 1) in the cloud to regulate the size of the upload window and 2) on the edge device to adjust the sequence of images, respectively. Notably, the proposed DaCM can be seamlessly combined with traditional ReID methods, enabling their application within our proposed edge-cloud collaborative framework. Extensive experiments demonstrate that our method obviously reduces transmission overhead and significantly improves performance.

**Link**: [arxiv](http://arxiv.org/abs/2401.02041v2),  [pdf](http://arxiv.org/pdf/2401.02041v2)

**Tags**: cs.CV 



### System Safety Monitoring of Learned Components Using Temporal Metric   Forecasting
**Authors**: Sepehr Sharifi, Andrea Stocco, Lionel C. Briand

**Updated**: 2024-12-20T03:10:32Z

**Summary**: In learning-enabled autonomous systems, safety monitoring of learned components is crucial to ensure their outputs do not lead to system safety violations, given the operational context of the system. However, developing a safety monitor for practical deployment in real-world applications is challenging. This is due to limited access to internal workings and training data of the learned component. Furthermore, safety monitors should predict safety violations with low latency, while consuming a reasonable amount of computation. To address the challenges, we propose a safety monitoring method based on probabilistic time series forecasting. Given the learned component outputs and an operational context, we empirically investigate different Deep Learning (DL)-based probabilistic forecasting to predict the objective measure capturing the satisfaction or violation of a safety requirement (safety metric). We empirically evaluate safety metric and violation prediction accuracy, and inference latency and resource usage of four state-of-the-art models, with varying horizons, using autonomous aviation and autonomous driving case studies. Our results suggest that probabilistic forecasting of safety metrics, given learned component outputs and scenarios, is effective for safety monitoring. Furthermore, for both case studies, Temporal Fusion Transformer (TFT) was the most accurate model for predicting imminent safety violations, with acceptable latency and resource consumption.

**Link**: [arxiv](http://arxiv.org/abs/2405.13254v3),  [pdf](http://arxiv.org/pdf/2405.13254v3)

**Tags**: cs.LG cs.AI cs.RO cs.SE 



### ResoFilter: Fine-grained Synthetic Data Filtering for Large Language   Models through Data-Parameter Resonance Analysis
**Authors**: Zeao Tu, Xiangdi Meng, Yu He, Zihan Yao, Tianyu Qi, Jun Liu, Ming Li

**Updated**: 2024-12-20T03:01:06Z

**Summary**: Large language models (LLMs) have shown remarkable effectiveness across various domains, with data augmentation methods utilizing GPT for synthetic data generation becoming prevalent. However, the quality and utility of augmented data remain questionable, and current methods lack clear metrics for evaluating data characteristics. To address these challenges, we propose ResoFilter, a novel method that integrates models, data, and tasks to refine datasets. ResoFilter leverages the fine-tuning process to obtain Data-Parameter features for data selection, offering improved interpretability by representing data characteristics through model weights. Our experiments demonstrate that ResoFilter achieves comparable results to full-scale fine-tuning using only half the data in mathematical tasks and exhibits strong generalization across different models and domains. This method provides valuable insights for constructing synthetic datasets and evaluating high-quality data, offering a promising solution for enhancing data augmentation techniques and improving training dataset quality for LLMs. For reproducibility, we will release our code and data upon acceptance.

**Link**: [arxiv](http://arxiv.org/abs/2412.14809v2),  [pdf](http://arxiv.org/pdf/2412.14809v2)

**Tags**: cs.CL 



### Mapping and Influencing the Political Ideology of Large Language Models   using Synthetic Personas
**Authors**: Pietro Bernardelle, Leon Fröhling, Stefano Civelli, Riccardo Lunardi, Kevin Roitero, Gianluca Demartini

**Updated**: 2024-12-20T02:59:23Z

**Summary**: The analysis of political biases in large language models (LLMs) has primarily examined these systems as single entities with fixed viewpoints. While various methods exist for measuring such biases, the impact of persona-based prompting on LLMs' political orientation remains unexplored. In this work we leverage PersonaHub, a collection of synthetic persona descriptions, to map the political distribution of persona-based prompted LLMs using the Political Compass Test (PCT). We then examine whether these initial compass distributions can be manipulated through explicit ideological prompting towards diametrically opposed political orientations: right-authoritarian and left-libertarian. Our experiments reveal that synthetic personas predominantly cluster in the left-libertarian quadrant, with models demonstrating varying degrees of responsiveness when prompted with explicit ideological descriptors. While all models demonstrate significant shifts towards right-authoritarian positions, they exhibit more limited shifts towards left-libertarian positions, suggesting an asymmetric response to ideological manipulation that may reflect inherent biases in model training.

**Link**: [arxiv](http://arxiv.org/abs/2412.14843v2),  [pdf](http://arxiv.org/pdf/2412.14843v2)

**Tags**: cs.CL cs.AI 



### A Roadmap for Software Testing in Open Collaborative Development   Environments
**Authors**: Qing Wang, Junjie Wang, Mingyang Li, Yawen Wang, Zhe Liu

**Updated**: 2024-12-20T02:52:36Z

**Summary**: Amidst the ever-expanding digital sphere, the evolution of the Internet has not only fostered an atmosphere of information transparency and sharing but has also sparked a revolution in software development practices. The distributed nature of open collaborative development, along with its diverse contributors and rapid iterations, presents new challenges for ensuring software quality. This paper offers a comprehensive review and analysis of recent advancements in software quality assurance within open collaborative development environments. Our examination covers various aspects, including process management, personnel dynamics, and technological advancements, providing valuable insights into effective approaches for maintaining software quality in such collaborative settings. Furthermore, we delve into the challenges and opportunities arising from emerging technologies such as LLMs and the AI model-centric development paradigm. By addressing these topics, our study contributes to a deeper understanding of software quality assurance in open collaborative environments and lays the groundwork for future exploration and innovation.

**Link**: [arxiv](http://arxiv.org/abs/2406.05438v2),  [pdf](http://arxiv.org/pdf/2406.05438v2)

**Tags**: cs.SE 



### DialSim: A Real-Time Simulator for Evaluating Long-Term Multi-Party   Dialogue Understanding of Conversational Agents
**Authors**: Jiho Kim, Woosog Chay, Hyeonji Hwang, Daeun Kyung, Hyunseung Chung, Eunbyeol Cho, Yohan Jo, Edward Choi

**Updated**: 2024-12-20T02:44:19Z

**Summary**: Recent advancements in Large Language Models (LLMs) have significantly enhanced the capabilities of conversational agents, making them applicable to various fields (e.g., education). Despite their progress, the evaluation of the agents often overlooks the complexities of real-world conversations, such as real-time interactions, multi-party dialogues, and extended contextual dependencies. To bridge this gap, we introduce DialSim, a real-time dialogue simulator. In this simulator, an agent is assigned the role of a character from popular TV shows, requiring it to respond to spontaneous questions using past dialogue information and to distinguish between known and unknown information. Key features of DialSim include assessing the agent's ability to respond within a reasonable time limit, handling long-term multi-party dialogues, and evaluating performance under randomized questioning with LongDialQA, a novel, high-quality question-answering dataset. Our experiments using DialSim reveal the strengths and weaknesses of the latest conversational agents, offering valuable insights for future advancements in conversational AI. DialSim is available at https://dialsim.github.io/.

**Link**: [arxiv](http://arxiv.org/abs/2406.13144v4),  [pdf](http://arxiv.org/pdf/2406.13144v4)

**Tags**: cs.CL cs.AI 



### Mitigating Social Bias in Large Language Models: A Multi-Objective   Approach within a Multi-Agent Framework
**Authors**: Zhenjie Xu, Wenqing Chen, Yi Tang, Xuanying Li, Cheng Hu, Zhixuan Chu, Kui Ren, Zibin Zheng, Zhichao Lu

**Updated**: 2024-12-20T02:35:39Z

**Summary**: Natural language processing (NLP) has seen remarkable advancements with the development of large language models (LLMs). Despite these advancements, LLMs often produce socially biased outputs. Recent studies have mainly addressed this problem by prompting LLMs to behave ethically, but this approach results in unacceptable performance degradation. In this paper, we propose a multi-objective approach within a multi-agent framework (MOMA) to mitigate social bias in LLMs without significantly compromising their performance. The key idea of MOMA involves deploying multiple agents to perform causal interventions on bias-related contents of the input questions, breaking the shortcut connection between these contents and the corresponding answers. Unlike traditional debiasing techniques leading to performance degradation, MOMA substantially reduces bias while maintaining accuracy in downstream tasks. Our experiments conducted on two datasets and two models demonstrate that MOMA reduces bias scores by up to 87.7%, with only a marginal performance degradation of up to 6.8% in the BBQ dataset. Additionally, it significantly enhances the multi-objective metric icat in the StereoSet dataset by up to 58.1%. Code will be made available at https://github.com/Cortantse/MOMA.

**Link**: [arxiv](http://arxiv.org/abs/2412.15504v1),  [pdf](http://arxiv.org/pdf/2412.15504v1)

**Tags**: cs.CL 



