# Arxiv Results
## Keyword: kv cache 
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



### MagicPIG: LSH Sampling for Efficient LLM Generation
**Authors**: Zhuoming Chen, Ranajoy Sadhukhan, Zihao Ye, Yang Zhou, Jianyu Zhang, Niklas Nolte, Yuandong Tian, Matthijs Douze, Leon Bottou, Zhihao Jia, Beidi Chen

**Updated**: 2024-12-17T03:56:26Z

**Summary**: Large language models (LLMs) with long context windows have gained significant attention. However, the KV cache, stored to avoid re-computation, becomes a bottleneck. Various dynamic sparse or TopK-based attention approximation methods have been proposed to leverage the common insight that attention is sparse. In this paper, we first show that TopK attention itself suffers from quality degradation in certain downstream tasks because attention is not always as sparse as expected. Rather than selecting the keys and values with the highest attention scores, sampling with theoretical guarantees can provide a better estimation for attention output. To make the sampling-based approximation practical in LLM generation, we propose MagicPIG, a heterogeneous system based on Locality Sensitive Hashing (LSH). MagicPIG significantly reduces the workload of attention computation while preserving high accuracy for diverse tasks. MagicPIG stores the LSH hash tables and runs the attention computation on the CPU, which allows it to serve longer contexts and larger batch sizes with high approximation accuracy. MagicPIG can improve decoding throughput by up to $5\times$ across various GPU hardware and achieve 54ms decoding latency on a single RTX 4090 for Llama-3.1-8B-Instruct model with a context of 96k tokens. The code is available at https://github.com/Infini-AI-Lab/MagicPIG.

**Link**: [arxiv](http://arxiv.org/abs/2410.16179v3),  [pdf](http://arxiv.org/pdf/2410.16179v3)

**Tags**: cs.CL cs.LG 



### A System for Microserving of LLMs
**Authors**: Hongyi Jin, Ruihang Lai, Charlie F. Ruan, Yingcheng Wang, Todd C. Mowry, Xupeng Miao, Zhihao Jia, Tianqi Chen

**Updated**: 2024-12-17T02:44:43Z

**Summary**: The recent advances in LLMs bring a strong demand for efficient system support to improve overall serving efficiency. As LLM inference scales towards multiple GPUs and even multiple compute nodes, various coordination patterns, such as prefill-decode disaggregation and context migration, arise in serving systems. Most inference services today expose a coarse-grained request-level API with a pre-configured coordination strategy, limiting the ability to customize and dynamically reconfigure the coordination. In this paper, we propose LLM microserving, a multi-level architecture for structuring and programming LLM inference services. We introduces simple yet effective microserving APIs to support fine-grained sub-request level actions. A programmable router transforms user requests into sub-request calls, enabling the dynamic reconfiguration of serving patterns. To support diverse execution patterns, we develop a unified KV cache interface that handles various KV compute, transfer, and reuse scenarios. Our evaluation shows that LLM microserving can be reconfigured to support multiple disaggregation orchestration strategies in a few lines of Python code while maintaining state-of-the-art performance for LLM inference tasks. Additionally, it allows us to explore new strategy variants that reduce up to 47% of job completion time compared to the existing strategies.

**Link**: [arxiv](http://arxiv.org/abs/2412.12488v1),  [pdf](http://arxiv.org/pdf/2412.12488v1)

**Tags**: cs.DC 



### Boosting Long-Context Information Seeking via Query-Guided Activation   Refilling
**Authors**: Hongjin Qian, Zheng Liu, Peitian Zhang, Zhicheng Dou, Defu Lian

**Updated**: 2024-12-17T02:43:54Z

**Summary**: Processing long contexts poses a significant challenge for large language models (LLMs) due to their inherent context-window limitations and the computational burden of extensive key-value (KV) activations, which severely impact efficiency. For information-seeking tasks, full context perception is often unnecessary, as a query's information needs can dynamically range from localized details to a global perspective, depending on its complexity. However, existing methods struggle to adapt effectively to these dynamic information needs.   In the paper, we propose a method for processing long-context information-seeking tasks via query-guided Activation Refilling (ACRE). ACRE constructs a Bi-layer KV Cache for long contexts, where the layer-1 (L1) cache compactly captures global information, and the layer-2 (L2) cache provides detailed and localized information. ACRE establishes a proxying relationship between the two caches, allowing the input query to attend to the L1 cache and dynamically refill it with relevant entries from the L2 cache. This mechanism integrates global understanding with query-specific local details, thus improving answer decoding. Experiments on a variety of long-context information-seeking datasets demonstrate ACRE's effectiveness, achieving improvements in both performance and efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12486v1),  [pdf](http://arxiv.org/pdf/2412.12486v1)

**Tags**: cs.CL cs.AI cs.IR 



### LazyDiT: Lazy Learning for the Acceleration of Diffusion Transformers
**Authors**: Xuan Shen, Zhao Song, Yufa Zhou, Bo Chen, Yanyu Li, Yifan Gong, Kai Zhang, Hao Tan, Jason Kuen, Henghui Ding, Zhihao Shu, Wei Niu, Pu Zhao, Yanzhi Wang, Jiuxiang Gu

**Updated**: 2024-12-17T01:12:35Z

**Summary**: Diffusion Transformers have emerged as the preeminent models for a wide array of generative tasks, demonstrating superior performance and efficacy across various applications. The promising results come at the cost of slow inference, as each denoising step requires running the whole transformer model with a large amount of parameters. In this paper, we show that performing the full computation of the model at each diffusion step is unnecessary, as some computations can be skipped by lazily reusing the results of previous steps. Furthermore, we show that the lower bound of similarity between outputs at consecutive steps is notably high, and this similarity can be linearly approximated using the inputs. To verify our demonstrations, we propose the \textbf{LazyDiT}, a lazy learning framework that efficiently leverages cached results from earlier steps to skip redundant computations. Specifically, we incorporate lazy learning layers into the model, effectively trained to maximize laziness, enabling dynamic skipping of redundant computations. Experimental results show that LazyDiT outperforms the DDIM sampler across multiple diffusion transformer models at various resolutions. Furthermore, we implement our method on mobile devices, achieving better performance than DDIM with similar latency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12444v1),  [pdf](http://arxiv.org/pdf/2412.12444v1)

**Tags**: cs.LG cs.AI 



### SepLLM: Accelerate Large Language Models by Compressing One Segment into   One Separator
**Authors**: Guoxuan Chen, Han Shi, Jiawei Li, Yihang Gao, Xiaozhe Ren, Yimeng Chen, Xin Jiang, Zhenguo Li, Weiyang Liu, Chao Huang

**Updated**: 2024-12-16T18:58:57Z

**Summary**: Large Language Models (LLMs) have exhibited exceptional performance across a spectrum of natural language processing tasks. However, their substantial sizes pose considerable challenges, particularly in computational demands and inference speed, due to their quadratic complexity. In this work, we have identified a key pattern: certain seemingly meaningless special tokens (i.e., separators) contribute disproportionately to attention scores compared to semantically meaningful tokens. This observation suggests that information of the segments between these separator tokens can be effectively condensed into the separator tokens themselves without significant information loss. Guided by this insight, we introduce SepLLM, a plug-and-play framework that accelerates inference by compressing these segments and eliminating redundant tokens. Additionally, we implement efficient kernels for training acceleration. Experimental results across training-free, training-from-scratch, and post-training settings demonstrate SepLLM's effectiveness. Notably, using the Llama-3-8B backbone, SepLLM achieves over 50% reduction in KV cache on the GSM8K-CoT benchmark while maintaining comparable performance. Furthermore, in streaming settings, SepLLM effectively processes sequences of up to 4 million tokens or more while maintaining consistent language modeling capabilities.

**Link**: [arxiv](http://arxiv.org/abs/2412.12094v1),  [pdf](http://arxiv.org/pdf/2412.12094v1)

**Tags**: cs.CL cs.AI cs.LG 



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



### DroidSpeak: KV Cache Sharing for Efficient Multi-LLM Serving
**Authors**: Yuhan Liu, Yuyang Huang, Jiayi Yao, Zhuohan Gu, Kuntai Du, Hanchen Li, Yihua Cheng, Junchen Jiang, Shan Lu, Madan Musuvathi, Esha Choukse

**Updated**: 2024-12-13T17:53:25Z

**Summary**: Large Language Models (LLMs) are increasingly employed in complex workflows, where different LLMs and fine-tuned variants collaboratively address complex tasks. However, these systems face significant inefficiencies due to redundant context processing of the shared context. We propose DroidSpeak, a framework that optimizes context sharing between fine-tuned LLMs derived from the same foundational model. DroidSpeak identifies critical layers in the KV cache and selectively recomputes them, enabling effective reuse of intermediate data while maintaining high accuracy.   Our approach balances computational efficiency and task fidelity, significantly reducing inference latency and throughput bottlenecks. Experiments on diverse datasets and model pairs demonstrate that DroidSpeak achieves up to 3x higher throughputs and 2.6x faster prefill times with negligible accuracy loss compared to full recomputation.

**Link**: [arxiv](http://arxiv.org/abs/2411.02820v2),  [pdf](http://arxiv.org/pdf/2411.02820v2)

**Tags**: cs.MA cs.AI cs.CL cs.LG 



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



### Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking
**Authors**: Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough

**Updated**: 2024-12-02T11:07:51Z

**Summary**: While mobile devices provide ever more compute power, improvements in DRAM bandwidth are much slower. This is unfortunate for large language model (LLM) token generation, which is heavily memory-bound. Previous work has proposed to leverage natural dynamic activation sparsity in ReLU-activated LLMs to reduce effective DRAM bandwidth per token. However, more recent LLMs use SwiGLU instead of ReLU, which result in little inherent sparsity. While SwiGLU activations can be pruned based on magnitude, the resulting sparsity patterns are difficult to predict, rendering previous approaches ineffective. To circumvent this issue, our work introduces Dynamic Input Pruning (DIP): a predictor-free dynamic sparsification approach, which preserves accuracy with minimal fine-tuning. DIP can further use lightweight LoRA adapters to regain some performance lost during sparsification. Lastly, we describe a novel cache-aware masking strategy, which considers the cache state and activation magnitude to further increase cache hit rate, improving LLM token rate on mobile devices. DIP outperforms other methods in terms of accuracy, memory and throughput trade-offs across simulated hardware settings. On Phi-3-Medium, DIP achieves a 46% reduction in memory and 40% increase in throughput with $<$ 0.1 loss in perplexity.

**Link**: [arxiv](http://arxiv.org/abs/2412.01380v1),  [pdf](http://arxiv.org/pdf/2412.01380v1)

**Tags**: cs.LG cs.CL 



### Memory-Efficient Training for Deep Speaker Embedding Learning in Speaker   Verification
**Authors**: Bei Liu, Yanmin Qian

**Updated**: 2024-12-02T06:57:46Z

**Summary**: Recent speaker verification (SV) systems have shown a trend toward adopting deeper speaker embedding extractors. Although deeper and larger neural networks can significantly improve performance, their substantial memory requirements hinder training on consumer GPUs. In this paper, we explore a memory-efficient training strategy for deep speaker embedding learning in resource-constrained scenarios. Firstly, we conduct a systematic analysis of GPU memory allocation during SV system training. Empirical observations show that activations and optimizer states are the main sources of memory consumption. For activations, we design two types of reversible neural networks which eliminate the need to store intermediate activations during back-propagation, thereby significantly reducing memory usage without performance loss. For optimizer states, we introduce a dynamic quantization approach that replaces the original 32-bit floating-point values with a dynamic tree-based 8-bit data type. Experimental results on VoxCeleb demonstrate that the reversible variants of ResNets and DF-ResNets can perform training without the need to cache activations in GPU memory. In addition, the 8-bit versions of SGD and Adam save 75% of memory costs while maintaining performance compared to their 32-bit counterparts. Finally, a detailed comparison of memory usage and performance indicates that our proposed models achieve up to 16.2x memory savings, with nearly identical parameters and performance compared to the vanilla systems. In contrast to the previous need for multiple high-end GPUs such as the A100, we can effectively train deep speaker embedding extractors with just one or two consumer-level 2080Ti GPUs.

**Link**: [arxiv](http://arxiv.org/abs/2412.01195v1),  [pdf](http://arxiv.org/pdf/2412.01195v1)

**Tags**: eess.AS cs.AI cs.SD 



### JC5A: Service Delay Minimization for Aerial MEC-assisted Industrial   Cyber-Physical Systems
**Authors**: Geng Sun, Jiaxu Wu, Zemin Sun, Long He, Jiacheng Wang, Dusit Niyato, Abbas Jamalipour, Shiwen Mao

**Updated**: 2024-12-02T06:30:04Z

**Summary**: In the era of the sixth generation (6G) and industrial Internet of Things (IIoT), an industrial cyber-physical system (ICPS) drives the proliferation of sensor devices and computing-intensive tasks. To address the limited resources of IIoT sensor devices, unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has emerged as a promising solution, providing flexible and cost-effective services in close proximity of IIoT sensor devices (ISDs). However, leveraging aerial MEC to meet the delay-sensitive and computation-intensive requirements of the ISDs could face several challenges, including the limited communication, computation and caching (3C) resources, stringent offloading requirements for 3C services, and constrained on-board energy of UAVs. To address these issues, we first present a collaborative aerial MEC-assisted ICPS architecture by incorporating the computing capabilities of the macro base station (MBS) and UAVs. We then formulate a service delay minimization optimization problem (SDMOP). Since the SDMOP is proved to be an NP-hard problem, we propose a joint computation offloading, caching, communication resource allocation, computation resource allocation, and UAV trajectory control approach (JC5A). Specifically, JC5A consists of a block successive upper bound minimization method of multipliers (BSUMM) for computation offloading and service caching, a convex optimization-based method for communication and computation resource allocation, and a successive convex approximation (SCA)-based method for UAV trajectory control. Moreover, we theoretically prove the convergence and polynomial complexity of JC5A. Simulation results demonstrate that the proposed approach can achieve superior system performance compared to the benchmark approaches and algorithms.

**Link**: [arxiv](http://arxiv.org/abs/2411.04762v2),  [pdf](http://arxiv.org/pdf/2411.04762v2)

**Tags**: cs.NI eess.SP 



### Optimal Power Allocation in Uplink NOMA with Simultaneous Cache-Enabled   D2D Communications
**Authors**: Aditya Powari, Daniel K. C. So

**Updated**: 2024-12-01T21:47:35Z

**Summary**: Non-orthogonal multiple access (NOMA) is widely viewed as a potential candidate for providing enhanced multiple access in future mobile networks by eliminating the orthogonal distribution of radio resources amongst the users. Nevertheless, the performance of NOMA can be significantly improved by combining it with other sophisticated technologies such as wireless data caching and device-to-device (D2D) communications. In this letter, we propose a novel cellular system model which integrates uplink NOMA with cache based device-to-device (D2D) communications. The proposed system would enable a cellular user to upload data file to base station while simultaneously exchanging useful cache content with another nearby user. We maximize the system sum rate by deriving closed form solutions for optimal power allocation. Simulation results demonstrate the superior performance of our proposed model over other potential combinations of uplink NOMA and D2D communications.

**Link**: [arxiv](http://arxiv.org/abs/2412.00977v1),  [pdf](http://arxiv.org/pdf/2412.00977v1)

**Tags**: eess.SP cs.ET 



### Advanced Video Inpainting Using Optical Flow-Guided Efficient Diffusion
**Authors**: Bohai Gu, Hao Luo, Song Guo, Peiran Dong

**Updated**: 2024-12-01T15:45:26Z

**Summary**: Recently, diffusion-based methods have achieved great improvements in the video inpainting task. However, these methods still face many challenges, such as maintaining temporal consistency and the time-consuming issue. This paper proposes an advanced video inpainting framework using optical Flow-guided Efficient Diffusion, called FloED. Specifically, FloED employs a dual-branch architecture, where a flow branch first restores corrupted flow and a multi-scale flow adapter provides motion guidance to the main inpainting branch. Additionally, a training-free latent interpolation method is proposed to accelerate the multi-step denoising process using flow warping. Further introducing a flow attention cache mechanism, FLoED efficiently reduces the computational cost brought by incorporating optical flow. Comprehensive experiments in both background restoration and object removal tasks demonstrate that FloED outperforms state-of-the-art methods from the perspective of both performance and efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.00857v1),  [pdf](http://arxiv.org/pdf/2412.00857v1)

**Tags**: cs.CV 



### SpecExec: Massively Parallel Speculative Decoding for Interactive LLM   Inference on Consumer Devices
**Authors**: Ruslan Svirschevski, Avner May, Zhuoming Chen, Beidi Chen, Zhihao Jia, Max Ryabinin

**Updated**: 2024-11-30T21:33:59Z

**Summary**: As large language models gain widespread adoption, running them efficiently becomes crucial. Recent works on LLM inference use speculative decoding to achieve extreme speedups. However, most of these works implicitly design their algorithms for high-end datacenter hardware. In this work, we ask the opposite question: how fast can we run LLMs on consumer machines? Consumer GPUs can no longer fit the largest available models (50B+ parameters) and must offload them to RAM or SSD. When running with offloaded parameters, the inference engine can process batches of hundreds or thousands of tokens at the same time as just one token, making it a natural fit for speculative decoding. We propose SpecExec (Speculative Execution), a simple parallel decoding method that can generate up to 20 tokens per target model iteration for popular LLM families. It utilizes the high spikiness of the token probabilities distribution in modern LLMs and a high degree of alignment between model output probabilities. SpecExec takes the most probable tokens continuation from the draft model to build a "cache" tree for the target model, which then gets validated in a single pass. Using SpecExec, we demonstrate inference of 50B+ parameter LLMs on consumer GPUs with RAM offloading at 4-6 tokens per second with 4-bit quantization or 2-3 tokens per second with 16-bit weights.

**Link**: [arxiv](http://arxiv.org/abs/2406.02532v3),  [pdf](http://arxiv.org/pdf/2406.02532v3)

**Tags**: cs.CL 



### Digital Twin in Industries: A Comprehensive Survey
**Authors**: Md Bokhtiar Al Zami, Shaba Shaon, Vu Khanh Quy, Dinh C. Nguyen

**Updated**: 2024-11-29T19:14:45Z

**Summary**: Industrial networks are undergoing rapid transformation driven by the convergence of emerging technologies that are revolutionizing conventional workflows, enhancing operational efficiency, and fundamentally redefining the industrial landscape across diverse sectors. Amidst this revolution, Digital Twin (DT) emerges as a transformative innovation that seamlessly integrates real-world systems with their virtual counterparts, bridging the physical and digital realms. In this article, we present a comprehensive survey of the emerging DT-enabled services and applications across industries, beginning with an overview of DT fundamentals and its components to a discussion of key enabling technologies for DT. Different from literature works, we investigate and analyze the capabilities of DT across a wide range of industrial services, including data sharing, data offloading, integrated sensing and communication, content caching, resource allocation, wireless networking, and metaverse. In particular, we present an in-depth technical discussion of the roles of DT in industrial applications across various domains, including manufacturing, healthcare, transportation, energy, agriculture, space, oil and gas, as well as robotics. Throughout the technical analysis, we delve into real-time data communications between physical and virtual platforms to enable industrial DT networking. Subsequently, we extensively explore and analyze a wide range of major privacy and security issues in DT-based industry. Taxonomy tables and the key research findings from the survey are also given, emphasizing important insights into the significance of DT in industries. Finally, we point out future research directions to spur further research in this promising area.

**Link**: [arxiv](http://arxiv.org/abs/2412.00209v1),  [pdf](http://arxiv.org/pdf/2412.00209v1)

**Tags**: cs.AI 



### Ten Ways in which Virtual Reality Differs from Video Streaming
**Authors**: Gustavo de Veciana, Sonia Fahmy, George Kesidis, Voicu Popescu

**Updated**: 2024-11-29T14:23:25Z

**Summary**: Virtual Reality (VR) applications have a number of unique characteristics that set them apart from traditional video streaming. These characteristics have major implications on the design of VR rendering, adaptation, prefetching, caching, and transport mechanisms. This paper contrasts VR to video streaming, stored 2D video streaming in particular, and discusses how to rethink system and network support for VR.

**Link**: [arxiv](http://arxiv.org/abs/2411.19730v1),  [pdf](http://arxiv.org/pdf/2411.19730v1)

**Tags**: cs.PF cs.MM cs.NI 



### Communication efficient application of sequences of planar rotations to   a matrix
**Authors**: Thijs Steel, Julien Langou

**Updated**: 2024-11-29T10:21:12Z

**Summary**: We present an efficient algorithm for the application of sequences of planar rotations to a matrix. Applying such sequences efficiently is important in many numerical linear algebra algorithms for eigenvalues. Our algorithm is novel in three main ways. First, we introduce a new kernel that is optimized for register reuse in a novel way. Second, we introduce a blocking and packing scheme that improves the cache efficiency of the algorithm. Finally, we thoroughly analyze the memory operations of the algorithm which leads to important theoretical insights and makes it easier to select good parameters. Numerical experiments show that our algorithm outperforms the state-of-the-art and achieves a flop rate close to the theoretical peak on modern hardware.

**Link**: [arxiv](http://arxiv.org/abs/2412.01852v1),  [pdf](http://arxiv.org/pdf/2412.01852v1)

**Tags**: cs.PF cs.DS 65F15, 65Y05 G.4 



### DID Link: Authentication in TLS with Decentralized Identifiers and   Verifiable Credentials
**Authors**: Sandro Rodriguez Garzon, Dennis Natusch, Artur Philipp, Axel Küpper, Hans Joachim Einsiedler, Daniela Schneider

**Updated**: 2024-11-29T08:48:01Z

**Summary**: Authentication in TLS is predominately carried out with X.509 digital certificates issued by certificate authorities (CA). The centralized nature of current public key infrastructures, however, comes along with severe risks, such as single points of failure and susceptibility to cyber-attacks, potentially undermining the security and trustworthiness of the entire system. With Decentralized Identifiers (DID) alongside distributed ledger technology, it becomes technically feasible to prove ownership of a unique identifier without requiring an attestation of the proof's public key by a centralized and therefore vulnerable CA. This article presents DID Link, a novel authentication scheme for TLS 1.3 that empowers entities to authenticate in a TLS-compliant way with self-issued X.509 certificates that are equipped with ledger-anchored DIDs instead of CA-issued identifiers. It facilitates the exchange of tamper-proof and 3rd-party attested claims in the form of DID-bound Verifiable Credentials after the TLS handshake to complete the authentication with a full identification of the communication partner. A prototypical implementation shows comparable TLS handshake durations of DID Link if verification material is cached and reasonable prolongations if it is obtained from a ledger. The significant speed improvement of the resulting TLS channel over a widely used, DID-based alternative transport protocol on the application layer demonstrates the potential of DID Link to become a viable solution for the establishment of secure and trustful end-to-end communication links with decentrally managed digital identities.

**Link**: [arxiv](http://arxiv.org/abs/2405.07533v3),  [pdf](http://arxiv.org/pdf/2405.07533v3)

**Tags**: cs.CR cs.NI 



### InputSnatch: Stealing Input in LLM Services via Timing Side-Channel   Attacks
**Authors**: Xinyao Zheng, Husheng Han, Shangyi Shi, Qiyan Fang, Zidong Du, Xing Hu, Qi Guo

**Updated**: 2024-11-29T08:33:49Z

**Summary**: Large language models (LLMs) possess extensive knowledge and question-answering capabilities, having been widely deployed in privacy-sensitive domains like finance and medical consultation. During LLM inferences, cache-sharing methods are commonly employed to enhance efficiency by reusing cached states or responses for the same or similar inference requests. However, we identify that these cache mechanisms pose a risk of private input leakage, as the caching can result in observable variations in response times, making them a strong candidate for a timing-based attack hint.   In this study, we propose a novel timing-based side-channel attack to execute input theft in LLMs inference. The cache-based attack faces the challenge of constructing candidate inputs in a large search space to hit and steal cached user queries. To address these challenges, we propose two primary components. The input constructor employs machine learning techniques and LLM-based approaches for vocabulary correlation learning while implementing optimized search mechanisms for generalized input construction. The time analyzer implements statistical time fitting with outlier elimination to identify cache hit patterns, continuously providing feedback to refine the constructor's search strategy. We conduct experiments across two cache mechanisms and the results demonstrate that our approach consistently attains high attack success rates in various applications. Our work highlights the security vulnerabilities associated with performance optimizations, underscoring the necessity of prioritizing privacy and security alongside enhancements in LLM inference.

**Link**: [arxiv](http://arxiv.org/abs/2411.18191v2),  [pdf](http://arxiv.org/pdf/2411.18191v2)

**Tags**: cs.CR 



### BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix   Sharing and Throughput-oriented Token Batching
**Authors**: Zhen Zheng, Xin Ji, Taosong Fang, Fanghao Zhou, Chuanjie Liu, Gang Peng

**Updated**: 2024-11-29T05:57:37Z

**Summary**: Many LLM tasks are performed in large batches or even offline, and the performance indictor for which is throughput. These tasks usually show the characteristic of prefix sharing, where different prompt input can partially show the common prefix. However, the existing LLM inference engines tend to optimize the streaming requests and show limitations of supporting the large batched tasks with the prefix sharing characteristic. The existing solutions use the LRU-based cache to reuse the KV context of common prefix. The KV context that is about to be reused may prematurely be evicted with the implicit cache management. Even if not evicted, the lifetime of the shared KV context is extended since requests sharing the same context are not scheduled together, resulting in larger memory usage. These streaming oriented systems schedule the requests in the first-come-first-serve or similar order. As a result, the requests with larger ratio of decoding steps may be scheduled too late to be able to mix with the prefill chunks to increase the hardware utilization. Besides, the token and request number based batching can limit the size of token-batch, which keeps the GPU from saturating for the iterations dominated by decoding tokens. We propose BatchLLM to address the above problems. BatchLLM explicitly identifies the common prefixes globally. The requests sharing the same prefix will be scheduled together to reuse the KV context the best, which also shrinks the lifetime of common KV memory. BatchLLM reorders the requests and schedules the requests with larger ratio of decoding first to better mix the decoding tokens with the latter prefill chunks and applies memory-centric token batching to enlarge the token-batch sizes, which helps to increase the GPU utilization. Extensive evaluation shows that BatchLLM outperforms vLLM by 1.1x to 2x on a set of microbenchmarks and two typical industry workloads.

**Link**: [arxiv](http://arxiv.org/abs/2412.03594v1),  [pdf](http://arxiv.org/pdf/2412.03594v1)

**Tags**: cs.CL cs.AI cs.DC cs.LG 



### Reflecting Intelligent Surfaces-Assisted Multiple-Antenna Coded Caching
**Authors**: Xiaofan Niu, Minquan Cheng, Kai Wan, Robert Caiming Qiu, Giuseppe Caire

**Updated**: 2024-11-28T16:35:22Z

**Summary**: Reconfigurable intelligent surface (RIS) has been treated as a core technique in improving wireless propagation environments for the next generation wireless communication systems. This paper proposes a new coded caching problem, referred to as Reconfigurable Intelligent Surface (RIS)-assisted multiple-antenna coded caching, which is composed of a server with multiple antennas and some single-antenna cache-aided users. Different from the existing multi-antenna coded caching problems, we introduce a passive RIS (with limited number of units) into the systems to further increase the multicast gain (i.e., degrees of freedom (DoF)) in the transmission, which is done by using RIS-assisted interference nulling. That is, by using RIS, we can `erase' any path between one transmission antenna and one receive antenna. We first propose a new RIS-assisted interference nulling approach to search for the phase-shift coefficients of RIS for the sake of interference nulling, which converges faster than the state-of-the-art algorithm. After erasing some paths in each time slot, the delivery can be divided into several non-overlapping groups including transmission antennas and users, where in each group the transmission antennas serve the contained users without suffering interference from the transmissions by other groups. The division of groups for the sake of maximizing the DoF could be formulated into a combinatorial optimization problem. We propose a grouping algorithm which can find the optimal solution with low complexity, and the corresponding coded caching scheme achieving this DoF.

**Link**: [arxiv](http://arxiv.org/abs/2411.19248v1),  [pdf](http://arxiv.org/pdf/2411.19248v1)

**Tags**: cs.IT math.IT 



### Fresh Caching of Dynamic Contents using Restless Multi-armed Bandits
**Authors**: Ankita Koley, Chandramani Singh

**Updated**: 2024-11-28T14:42:54Z

**Summary**: We consider a dynamic content caching problem wherein the contents get updated at a central server, and local copies of a subset of contents are cached at a local cache associated with a Base station (BS). When a content request arrives, based on whether the content is in the local cache, the BS can decide whether to fetch the content from the central server or serve the cached version from the local cache. Fetching a content incurs a fixed fetching cost, and serving the cached version incurs an ageing cost proportional to the age-of-version (AoV) of the content. The BS has only partial information regarding AoVs of the contents. We formulate an optimal content fetching and caching problem to minimize the average cost subject to cache capacity constraints. The problem suffers from the curse of dimensionality and is provably hard to solve. We formulate this problem as a continuous time restless multi-armed bandit process (RMAB), where a single content problem of the corresponding RMAB is a partially observable Markov decision process. We reformulate the single content problem as a semi-Markov decision process, prove indexability, and provide a Whittle index based solution to this problem. Finally, we compare the performance with recent work and show that our proposed policy is optimal via simulations.

**Link**: [arxiv](http://arxiv.org/abs/2404.12468v2),  [pdf](http://arxiv.org/pdf/2404.12468v2)

**Tags**: cs.NI 



### Timestep Embedding Tells: It's Time to Cache for Video Diffusion Model
**Authors**: Feng Liu, Shiwei Zhang, Xiaofeng Wang, Yujie Wei, Haonan Qiu, Yuzhong Zhao, Yingya Zhang, Qixiang Ye, Fang Wan

**Updated**: 2024-11-28T12:50:05Z

**Summary**: As a fundamental backbone for video generation, diffusion models are challenged by low inference speed due to the sequential nature of denoising. Previous methods speed up the models by caching and reusing model outputs at uniformly selected timesteps. However, such a strategy neglects the fact that differences among model outputs are not uniform across timesteps, which hinders selecting the appropriate model outputs to cache, leading to a poor balance between inference efficiency and visual quality. In this study, we introduce Timestep Embedding Aware Cache (TeaCache), a training-free caching approach that estimates and leverages the fluctuating differences among model outputs across timesteps. Rather than directly using the time-consuming model outputs, TeaCache focuses on model inputs, which have a strong correlation with the modeloutputs while incurring negligible computational cost. TeaCache first modulates the noisy inputs using the timestep embeddings to ensure their differences better approximating those of model outputs. TeaCache then introduces a rescaling strategy to refine the estimated differences and utilizes them to indicate output caching. Experiments show that TeaCache achieves up to 4.41x acceleration over Open-Sora-Plan with negligible (-0.07% Vbench score) degradation of visual quality.

**Link**: [arxiv](http://arxiv.org/abs/2411.19108v1),  [pdf](http://arxiv.org/pdf/2411.19108v1)

**Tags**: cs.CV 



### Many Hands Make Light Work: Accelerating Edge Inference via Multi-Client   Collaborative Caching
**Authors**: Wenyi Liang, Jianchun Liu, Hongli Xu, Chunming Qiao, Liusheng Huang

**Updated**: 2024-11-28T10:40:47Z

**Summary**: Edge inference is a technology that enables real-time data processing and analysis on clients near the data source. To ensure compliance with the Service-Level Objectives (SLOs), such as a 30% latency reduction target, caching is usually adopted to reduce redundant computations in inference tasks on stream data. Due to task and data correlations, sharing cache information among clients can improve the inference performance. However, the non-independent and identically distributed (non-IID) nature of data across different clients and the long-tail distributions, where some classes have significantly more samples than others, will reduce cache hit ratios and increase latency. To address the aforementioned challenges, we propose an efficient inference framework, CoCa, which leverages a multi-client collaborative caching mechanism to accelerate edge inference. On the client side, the model is pre-set with multiple cache layers to achieve a quick inference. During inference, the model performs sequential lookups at cache layers activated by the edge server. On the server side, CoCa uses a two-dimensional global cache to periodically aggregate information from clients, mitigating the effects of non-IID data. For client cache allocation, CoCa first evaluates the importance of classes based on how frequently and recently their samples have been accessed. CoCa then selects frequently recurring classes to address long-tail distribution challenges. Finally, CoCa dynamically activates cache layers to balance lookup overhead and accuracy. Extensive experiments demonstrate that CoCa reduces inference latency by 23.0% to 45.2% on the VGG, ResNet and AST models with a slight loss of accuracy.

**Link**: [arxiv](http://arxiv.org/abs/2412.10382v1),  [pdf](http://arxiv.org/pdf/2412.10382v1)

**Tags**: cs.DC 



### MiniKV: Pushing the Limits of LLM Inference via 2-Bit   Layer-Discriminative KV Cache
**Authors**: Akshat Sharma, Hangliang Ding, Jianping Li, Neel Dani, Minjia Zhang

**Updated**: 2024-11-28T02:01:50Z

**Summary**: How to efficiently serve LLMs in practice has become exceptionally challenging due to their prohibitive memory and computation requirements. In this study, we investigate optimizing the KV cache, whose memory footprint poses a critical bottleneck in LLM inference, especially when dealing with long context tasks. To tackle the challenge, we introduce MiniKV, a KV cache optimization method that simultaneously preserves long context task accuracy while significantly reducing KV cache size via a novel 2-bit layer-discriminative KV cache. More importantly, we develop specialized CUDA kernels to make MiniKV compatible with FlashAttention. Experiments on a wide range of long context tasks show that MiniKV effectively achieves 86% KV cache compression ratio while recovering over 98.5% of accuracy, outperforming state-of-the-art methods while achieving excellent measured system performance improvements.

**Link**: [arxiv](http://arxiv.org/abs/2411.18077v2),  [pdf](http://arxiv.org/pdf/2411.18077v2)

**Tags**: cs.CL cs.LG 



## Keyword: LLM Inference 
 ### SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM   Agents
**Authors**: Sheng Yin, Xianghe Pang, Yuanzhuo Ding, Menglan Chen, Yutong Bi, Yichen Xiong, Wenhao Huang, Zhen Xiang, Jing Shao, Siheng Chen

**Updated**: 2024-12-17T18:55:58Z

**Summary**: With the integration of large language models (LLMs), embodied agents have strong capabilities to execute complicated instructions in natural language, paving a way for the potential deployment of embodied robots. However, a foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in real world. To study this issue, we present SafeAgentBench -- a new benchmark for safety-aware task planning of embodied LLM agents. SafeAgentBench includes: (1) a new dataset with 750 tasks, covering 10 potential hazards and 3 task types; (2) SafeAgentEnv, a universal embodied environment with a low-level controller, supporting multi-agent execution with 17 high-level actions for 8 state-of-the-art baselines; and (3) reliable evaluation methods from both execution and semantic perspectives. Experimental results show that the best-performing baseline gets 69% success rate for safe tasks, but only 5% rejection rate for hazardous tasks, indicating significant safety risks. More details and codes are available at https://github.com/shengyin1224/SafeAgentBench.

**Link**: [arxiv](http://arxiv.org/abs/2412.13178v1),  [pdf](http://arxiv.org/pdf/2412.13178v1)

**Tags**: cs.CR cs.AI cs.RO 



### DataEnvGym: Data Generation Agents in Teacher Environments with Student   Feedback
**Authors**: Zaid Khan, Elias Stengel-Eskin, Jaemin Cho, Mohit Bansal

**Updated**: 2024-12-17T18:54:45Z

**Summary**: The process of creating training data to teach models is currently driven by humans, who manually analyze model weaknesses and plan how to create data that improves a student model. Approaches using LLMs as annotators reduce human effort, but still require humans to interpret feedback from evaluations and control the LLM to produce data the student needs. Automating this labor-intensive process by creating autonomous data generation agents - or teachers - is desirable, but requires environments that can simulate the feedback-driven, iterative, closed loop of data creation. To enable rapid, scalable testing for such agents and their modules, we introduce DataEnvGym, a testbed of teacher environments for data generation agents. DataEnvGym frames data generation as a sequential decision-making task, involving an agent consisting of a data generation policy (which generates a plan for creating training data) and a data generation engine (which transforms the plan into data), inside an environment that provides student feedback. The agent's goal is to improve student performance. Students are iteratively trained and evaluated on generated data, and their feedback (in the form of errors or weak skills) is reported to the agent after each iteration. DataEnvGym includes multiple teacher environment instantiations across 3 levels of structure in the state representation and action space. More structured environments are based on inferred skills and offer more interpretability and curriculum control. We support 4 domains (math, code, VQA, and tool-use) and test multiple students and teachers. Example agents in our teaching environments can iteratively improve students across tasks and settings. Moreover, we show that environments teach different skill levels and test variants of key modules, pointing to future work in improving data generation agents, engines, and feedback mechanisms.

**Link**: [arxiv](http://arxiv.org/abs/2410.06215v2),  [pdf](http://arxiv.org/pdf/2410.06215v2)

**Tags**: cs.CL cs.AI cs.LG 



### DnDScore: Decontextualization and Decomposition for Factuality   Verification in Long-Form Text Generation
**Authors**: Miriam Wanner, Benjamin Van Durme, Mark Dredze

**Updated**: 2024-12-17T18:54:01Z

**Summary**: The decompose-then-verify strategy for verification of Large Language Model (LLM) generations decomposes claims that are then independently verified. Decontextualization augments text (claims) to ensure it can be verified outside of the original context, enabling reliable verification. While decomposition and decontextualization have been explored independently, their interactions in a complete system have not been investigated. Their conflicting purposes can create tensions: decomposition isolates atomic facts while decontextualization inserts relevant information. Furthermore, a decontextualized subclaim presents a challenge to the verification step: what part of the augmented text should be verified as it now contains multiple atomic facts? We conduct an evaluation of different decomposition, decontextualization, and verification strategies and find that the choice of strategy matters in the resulting factuality scores. Additionally, we introduce DnDScore, a decontextualization aware verification method which validates subclaims in the context of contextual information.

**Link**: [arxiv](http://arxiv.org/abs/2412.13175v1),  [pdf](http://arxiv.org/pdf/2412.13175v1)

**Tags**: cs.CL 



### Compressed Chain of Thought: Efficient Reasoning Through Dense   Representations
**Authors**: Jeffrey Cheng, Benjamin Van Durme

**Updated**: 2024-12-17T18:50:33Z

**Summary**: Chain-of-thought (CoT) decoding enables language models to improve reasoning performance at the cost of high generation latency in decoding. Recent proposals have explored variants of contemplation tokens, a term we introduce that refers to special tokens used during inference to allow for extra computation. Prior work has considered fixed-length sequences drawn from a discrete set of embeddings as contemplation tokens. Here we propose Compressed Chain-of-Thought (CCoT), a framework to generate contentful and continuous contemplation tokens of variable sequence length. The generated contemplation tokens are compressed representations of explicit reasoning chains, and our method can be applied to off-the-shelf decoder language models. Through experiments, we illustrate how CCoT enables additional reasoning over dense contentful representations to achieve corresponding improvements in accuracy. Moreover, the reasoning improvements can be adaptively modified on demand by controlling the number of contemplation tokens generated.

**Link**: [arxiv](http://arxiv.org/abs/2412.13171v1),  [pdf](http://arxiv.org/pdf/2412.13171v1)

**Tags**: cs.CL 



### Algorithmic Fidelity of Large Language Models in Generating Synthetic   German Public Opinions: A Case Study
**Authors**: Bolei Ma, Berk Yoztyurk, Anna-Carolina Haensch, Xinpeng Wang, Markus Herklotz, Frauke Kreuter, Barbara Plank, Matthias Assenmacher

**Updated**: 2024-12-17T18:46:32Z

**Summary**: In recent research, large language models (LLMs) have been increasingly used to investigate public opinions. This study investigates the algorithmic fidelity of LLMs, i.e., the ability to replicate the socio-cultural context and nuanced opinions of human participants. Using open-ended survey data from the German Longitudinal Election Studies (GLES), we prompt different LLMs to generate synthetic public opinions reflective of German subpopulations by incorporating demographic features into the persona prompts. Our results show that Llama performs better than other LLMs at representing subpopulations, particularly when there is lower opinion diversity within those groups. Our findings further reveal that the LLM performs better for supporters of left-leaning parties like The Greens and The Left compared to other parties, and matches the least with the right-party AfD. Additionally, the inclusion or exclusion of specific variables in the prompts can significantly impact the models' predictions. These findings underscore the importance of aligning LLMs to more effectively model diverse public opinions while minimizing political biases and enhancing robustness in representativeness.

**Link**: [arxiv](http://arxiv.org/abs/2412.13169v1),  [pdf](http://arxiv.org/pdf/2412.13169v1)

**Tags**: cs.CL 



### C-FedRAG: A Confidential Federated Retrieval-Augmented Generation System
**Authors**: Parker Addison, Minh-Tuan H. Nguyen, Tomislav Medan, Mohammad T. Manzari, Brendan McElrone, Laksh Lalwani, Aboli More, Smita Sharma, Holger R. Roth, Isaac Yang, Chester Chen, Daguang Xu, Yan Cheng, Andrew Feng, Ziyue Xu

**Updated**: 2024-12-17T18:42:21Z

**Summary**: Organizations seeking to utilize Large Language Models (LLMs) for knowledge querying and analysis often encounter challenges in maintaining an LLM fine-tuned on targeted, up-to-date information that keeps answers relevant and grounded. Retrieval Augmented Generation (RAG) has quickly become a feasible solution for organizations looking to overcome the challenges of maintaining proprietary models and to help reduce LLM hallucinations in their query responses. However, RAG comes with its own issues regarding scaling data pipelines across tiered-access and disparate data sources. In many scenarios, it is necessary to query beyond a single data silo to provide richer and more relevant context for an LLM. Analyzing data sources within and across organizational trust boundaries is often limited by complex data-sharing policies that prohibit centralized data storage, therefore, inhibit the fast and effective setup and scaling of RAG solutions. In this paper, we introduce Confidential Computing (CC) techniques as a solution for secure Federated Retrieval Augmented Generation (FedRAG). Our proposed Confidential FedRAG system (C-FedRAG) enables secure connection and scaling of a RAG workflows across a decentralized network of data providers by ensuring context confidentiality. We also demonstrate how to implement a C-FedRAG system using the NVIDIA FLARE SDK and assess its performance using the MedRAG toolkit and MIRAGE benchmarking dataset.

**Link**: [arxiv](http://arxiv.org/abs/2412.13163v1),  [pdf](http://arxiv.org/pdf/2412.13163v1)

**Tags**: cs.DC cs.IR 



### Let's Get to the Point: LLM-Supported Planning, Drafting, and Revising   of Research-Paper Blog Posts
**Authors**: Marissa Radensky, Daniel S. Weld, Joseph Chee Chang, Pao Siangliulue, Jonathan Bragg

**Updated**: 2024-12-17T18:35:27Z

**Summary**: Research-paper blog posts help scientists to disseminate their work to a larger audience, but translating scientific long documents into long-form summaries like blog posts raises unique challenges: 1) planning what paper content to include in the blog post, 2) drafting the selected content in sections amenable to a paper blog post, and 3) revising the blog post to be scientifically accurate but also concise, easy to understand, and engaging. Can we harness the power of large language models (LLMs) to assist researchers with these challenges? To investigate this question, we developed Papers-to-Posts, an LLM-powered tool that implements a new Plan-Draft-Revise workflow for mixed-initiative long-form paper summarization. An LLM-generated paper outline with pre-selected yet adjustable bullet points helps users to plan what information to include. Meanwhile, customizable LLM instructions support drafting the text with a suitable structure and revising the text to have an appropriate tone. Through two studies, we compared Papers-to-Posts to a strong baseline tool that provides an LLM-generated draft and access to free-form LLM prompting, and we found that Papers-to-Posts improved researchers' editing power. In a within-subjects lab study (N=20 participants), Papers-to-Posts led participants to make significantly more change to initial LLM drafts within a fixed amount of time and to be significantly more satisfied with their final blog post, without increasing cognitive load. Furthermore, in a between-subjects deployment study (N=37 blog posts, 26 participants), Papers-to-Posts led participants to make more change to initial LLM drafts within a given amount of time as well as writing actions, without decreasing satisfaction with the final blog posts or increasing cognitive load.

**Link**: [arxiv](http://arxiv.org/abs/2406.10370v2),  [pdf](http://arxiv.org/pdf/2406.10370v2)

**Tags**: cs.HC 



### S2S2: Semantic Stacking for Robust Semantic Segmentation in Medical   Imaging
**Authors**: Yimu Pan, Sitao Zhang, Alison D. Gernand, Jeffery A. Goldstein, James Z. Wang

**Updated**: 2024-12-17T18:30:22Z

**Summary**: Robustness and generalizability in medical image segmentation are often hindered by scarcity and limited diversity of training data, which stands in contrast to the variability encountered during inference. While conventional strategies -- such as domain-specific augmentation, specialized architectures, and tailored training procedures -- can alleviate these issues, they depend on the availability and reliability of domain knowledge. When such knowledge is unavailable, misleading, or improperly applied, performance may deteriorate. In response, we introduce a novel, domain-agnostic, add-on, and data-driven strategy inspired by image stacking in image denoising. Termed ``semantic stacking,'' our method estimates a denoised semantic representation that complements the conventional segmentation loss during training. This method does not depend on domain-specific assumptions, making it broadly applicable across diverse image modalities, model architectures, and augmentation techniques. Through extensive experiments, we validate the superiority of our approach in improving segmentation performance under diverse conditions. Code is available at https://github.com/ymp5078/Semantic-Stacking.

**Link**: [arxiv](http://arxiv.org/abs/2412.13156v1),  [pdf](http://arxiv.org/pdf/2412.13156v1)

**Tags**: cs.CV 



### Adaptive Nonparametric Perturbations of Parametric Bayesian Models
**Authors**: Bohan Wu, Eli N. Weinstein, Sohrab Salehi, Yixin Wang, David M. Blei

**Updated**: 2024-12-17T18:24:35Z

**Summary**: Parametric Bayesian modeling offers a powerful and flexible toolbox for scientific data analysis. Yet the model, however detailed, may still be wrong, and this can make inferences untrustworthy. In this paper we study nonparametrically perturbed parametric (NPP) Bayesian models, in which a parametric Bayesian model is relaxed via a distortion of its likelihood. We analyze the properties of NPP models when the target of inference is the true data distribution or some functional of it, such as in causal inference. We show that NPP models can offer the robustness of nonparametric models while retaining the data efficiency of parametric models, achieving fast convergence when the parametric model is close to true. To efficiently analyze data with an NPP model, we develop a generalized Bayes procedure to approximate its posterior. We demonstrate our method by estimating causal effects of gene expression from single cell RNA sequencing data. NPP modeling offers an efficient approach to robust Bayesian inference and can be used to robustify any parametric Bayesian model.

**Link**: [arxiv](http://arxiv.org/abs/2412.10683v2),  [pdf](http://arxiv.org/pdf/2412.10683v2)

**Tags**: stat.ME 



### Continuous Patient Monitoring with AI: Real-Time Analysis of Video in   Hospital Care Settings
**Authors**: Paolo Gabriel, Peter Rehani, Tyler Troy, Tiffany Wyatt, Michael Choma, Narinder Singh

**Updated**: 2024-12-17T18:23:33Z

**Summary**: This study introduces an AI-driven platform for continuous and passive patient monitoring in hospital settings, developed by LookDeep Health. Leveraging advanced computer vision, the platform provides real-time insights into patient behavior and interactions through video analysis, securely storing inference results in the cloud for retrospective evaluation. The dataset, compiled in collaboration with 11 hospital partners, encompasses over 300 high-risk fall patients and over 1,000 days of inference, enabling applications such as fall detection and safety monitoring for vulnerable patient populations. To foster innovation and reproducibility, an anonymized subset of this dataset is publicly available. The AI system detects key components in hospital rooms, including individual presence and role, furniture location, motion magnitude, and boundary crossings. Performance evaluation demonstrates strong accuracy in object detection (macro F1-score = 0.92) and patient-role classification (F1-score = 0.98), as well as reliable trend analysis for the "patient alone" metric (mean logistic regression accuracy = 0.82 \pm 0.15). These capabilities enable automated detection of patient isolation, wandering, or unsupervised movement-key indicators for fall risk and other adverse events. This work establishes benchmarks for validating AI-driven patient monitoring systems, highlighting the platform's potential to enhance patient safety and care by providing continuous, data-driven insights into patient behavior and interactions.

**Link**: [arxiv](http://arxiv.org/abs/2412.13152v1),  [pdf](http://arxiv.org/pdf/2412.13152v1)

**Tags**: cs.CV cs.AI 



### SWAN: Preprocessing SGD Enables Adam-Level Performance On LLM Training   With Significant Memory Reduction
**Authors**: Chao Ma, Wenbo Gong, Meyer Scetbon, Edward Meeds

**Updated**: 2024-12-17T18:13:18Z

**Summary**: Adaptive optimizers such as Adam (Kingma & Ba, 2015) have been central to the success of large language models. However, they maintain additional moving average states throughout training, which results in memory requirements several times greater than the model. This overhead imposes constraints on scalability and computational efficiency. On the other hand, while stochastic gradient descent (SGD) is optimal in terms of memory efficiency, their capability in LLM training is limited (Zhao et al., 2024b).   To address this dilemma, we show that pre-processing SGD is sufficient to reach Adam-level performance on LLMs. Specifically, we propose to preprocess the instantaneous stochastic gradients with two simple operators: $\mathtt{GradNorm}$ and $\mathtt{GradWhitening}$. $\mathtt{GradNorm}$ stabilizes gradient distributions, and $\mathtt{GradWhitening}$ counteracts the local curvature of the loss landscape, respectively. This results in SWAN (SGD with Whitening And Normalization), a stochastic optimizer that eliminates the need to store any accumulative state variables. Empirically, SWAN has the same memory footprint as SGD, achieving $\approx 50\%$ reduction on total end-to-end memory compared to Adam. In language modeling tasks, SWAN demonstrates the same or even a substantial improvement over Adam. Specifically, when pre-training the LLaMa model with 350M and 1.3B parameters, SWAN achieves a 2x speedup by reaching the same evaluation perplexity in less than half tokens seen.

**Link**: [arxiv](http://arxiv.org/abs/2412.13148v1),  [pdf](http://arxiv.org/pdf/2412.13148v1)

**Tags**: cs.LG cs.AI 



### Are Your LLMs Capable of Stable Reasoning?
**Authors**: Junnan Liu, Hongwei Liu, Linchen Xiao, Ziyi Wang, Kuikun Liu, Songyang Gao, Wenwei Zhang, Songyang Zhang, Kai Chen

**Updated**: 2024-12-17T18:12:47Z

**Summary**: The rapid advancement of Large Language Models (LLMs) has demonstrated remarkable progress in complex reasoning tasks. However, a significant discrepancy persists between benchmark performances and real-world applications. We identify this gap as primarily stemming from current evaluation protocols and metrics, which inadequately capture the full spectrum of LLM capabilities, particularly in complex reasoning tasks where both accuracy and consistency are crucial. This work makes two key contributions. First, we introduce G-Pass@k, a novel evaluation metric that provides a continuous assessment of model performance across multiple sampling attempts, quantifying both the model's peak performance potential and its stability. Second, we present LiveMathBench, a dynamic benchmark comprising challenging, contemporary mathematical problems designed to minimize data leakage risks during evaluation. Through extensive experiments using G-Pass@k on state-of-the-art LLMs with LiveMathBench, we provide comprehensive insights into both their maximum capabilities and operational consistency. Our findings reveal substantial room for improvement in LLMs' "realistic" reasoning capabilities, highlighting the need for more robust evaluation methods. The benchmark and detailed results are available at: https://github.com/open-compass/GPassK.

**Link**: [arxiv](http://arxiv.org/abs/2412.13147v1),  [pdf](http://arxiv.org/pdf/2412.13147v1)

**Tags**: cs.AI cs.CL 



### Reinforcement Learning Enhanced LLMs: A Survey
**Authors**: Shuhe Wang, Shengyu Zhang, Jie Zhang, Runyi Hu, Xiaoya Li, Tianwei Zhang, Jiwei Li, Fei Wu, Guoyin Wang, Eduard Hovy

**Updated**: 2024-12-17T18:05:11Z

**Summary**: This paper surveys research in the rapidly growing field of enhancing large language models (LLMs) with reinforcement learning (RL), a technique that enables LLMs to improve their performance by receiving feedback in the form of rewards based on the quality of their outputs, allowing them to generate more accurate, coherent, and contextually appropriate responses. In this work, we make a systematic review of the most up-to-date state of knowledge on RL-enhanced LLMs, attempting to consolidate and analyze the rapidly growing research in this field, helping researchers understand the current challenges and advancements. Specifically, we (1) detail the basics of RL; (2) introduce popular RL-enhanced LLMs; (3) review researches on two widely-used reward model-based RL techniques: Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAIF); and (4) explore Direct Preference Optimization (DPO), a set of methods that bypass the reward model to directly use human preference data for aligning LLM outputs with human expectations. We will also point out current challenges and deficiencies of existing methods and suggest some avenues for further improvements. Project page of this work can be found at: \url{https://github.com/ShuheWang1998/Reinforcement-Learning-Enhanced-LLMs-A-Survey}.

**Link**: [arxiv](http://arxiv.org/abs/2412.10400v2),  [pdf](http://arxiv.org/pdf/2412.10400v2)

**Tags**: cs.CL cs.AI cs.LG 



### Alternate Preference Optimization for Unlearning Factual Knowledge in   Large Language Models
**Authors**: Anmol Mekala, Vineeth Dorna, Shreya Dubey, Abhishek Lalwani, David Koleczek, Mukund Rungta, Sadid Hasan, Elita Lobo

**Updated**: 2024-12-17T17:45:07Z

**Summary**: Machine unlearning aims to efficiently eliminate the influence of specific training data, known as the forget set, from the model. However, existing unlearning methods for Large Language Models (LLMs) face a critical challenge: they rely solely on negative feedback to suppress responses related to the forget set, which often results in nonsensical or inconsistent outputs, diminishing model utility and posing potential privacy risks. To address this limitation, we propose a novel approach called Alternate Preference Optimization (AltPO), which combines negative feedback with in-domain positive feedback on the forget set. Additionally, we introduce new evaluation metrics to assess the quality of responses related to the forget set. Extensive experiments show that our approach not only enables effective unlearning but also avoids undesirable model behaviors while maintaining overall model performance. Our implementation can be found at https://github.com/molereddy/Alternate-Preference-Optimization.

**Link**: [arxiv](http://arxiv.org/abs/2409.13474v3),  [pdf](http://arxiv.org/pdf/2409.13474v3)

**Tags**: cs.CL cs.LG 



### RISCORE: Enhancing In-Context Riddle Solving in Language Models through   Context-Reconstructed Example Augmentation
**Authors**: Ioannis Panagiotopoulos, Giorgos Filandrianos, Maria Lymperaiou, Giorgos Stamou

**Updated**: 2024-12-17T17:42:18Z

**Summary**: Riddle-solving requires advanced reasoning skills, pushing LLMs to engage in abstract thinking and creative problem-solving, often revealing limitations in their cognitive abilities. In this paper, we examine the riddle-solving capabilities of LLMs using a multiple-choice format, exploring how different prompting techniques impact performance on riddles that demand diverse reasoning skills. To enhance results, we introduce RISCORE (RIddle Solving with COntext REcontruciton) a novel fully automated prompting method that generates and utilizes contextually reconstructed sentence-based puzzles in conjunction with the original examples to create few-shot exemplars. Our experiments demonstrate that RISCORE significantly improves the performance of language models in both vertical and lateral thinking tasks, surpassing traditional exemplar selection strategies across a variety of few-shot settings.

**Link**: [arxiv](http://arxiv.org/abs/2409.16383v4),  [pdf](http://arxiv.org/pdf/2409.16383v4)

**Tags**: cs.CL 



### Systematic Biases in LLM Simulations of Debates
**Authors**: Amir Taubenfeld, Yaniv Dover, Roi Reichart, Ariel Goldstein

**Updated**: 2024-12-17T17:17:21Z

**Summary**: The emergence of Large Language Models (LLMs), has opened exciting possibilities for constructing computational simulations designed to replicate human behavior accurately. Current research suggests that LLM-based agents become increasingly human-like in their performance, sparking interest in using these AI agents as substitutes for human participants in behavioral studies. However, LLMs are complex statistical learners without straightforward deductive rules, making them prone to unexpected behaviors. Hence, it is crucial to study and pinpoint the key behavioral distinctions between humans and LLM-based agents. In this study, we highlight the limitations of LLMs in simulating human interactions, particularly focusing on LLMs' ability to simulate political debates on topics that are important aspects of people's day-to-day lives and decision-making processes. Our findings indicate a tendency for LLM agents to conform to the model's inherent social biases despite being directed to debate from certain political perspectives. This tendency results in behavioral patterns that seem to deviate from well-established social dynamics among humans. We reinforce these observations using an automatic self-fine-tuning method, which enables us to manipulate the biases within the LLM and demonstrate that agents subsequently align with the altered biases. These results underscore the need for further research to develop methods that help agents overcome these biases, a critical step toward creating more realistic simulations.

**Link**: [arxiv](http://arxiv.org/abs/2402.04049v3),  [pdf](http://arxiv.org/pdf/2402.04049v3)

**Tags**: cs.CL cs.AI 



### AI PERSONA: Towards Life-long Personalization of LLMs
**Authors**: Tiannan Wang, Meiling Tao, Ruoyu Fang, Huilin Wang, Shuai Wang, Yuchen Eleanor Jiang, Wangchunshu Zhou

**Updated**: 2024-12-17T17:17:03Z

**Summary**: In this work, we introduce the task of life-long personalization of large language models. While recent mainstream efforts in the LLM community mainly focus on scaling data and compute for improved capabilities of LLMs, we argue that it is also very important to enable LLM systems, or language agents, to continuously adapt to the diverse and ever-changing profiles of every distinct user and provide up-to-date personalized assistance. We provide a clear task formulation and introduce a simple, general, effective, and scalable framework for life-long personalization of LLM systems and language agents. To facilitate future research on LLM personalization, we also introduce methods to synthesize realistic benchmarks and robust evaluation metrics. We will release all codes and data for building and benchmarking life-long personalized LLM systems.

**Link**: [arxiv](http://arxiv.org/abs/2412.13103v1),  [pdf](http://arxiv.org/pdf/2412.13103v1)

**Tags**: cs.CL cs.AI 



### AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark
**Authors**: Jianlyu Chen, Nan Wang, Chaofan Li, Bo Wang, Shitao Xiao, Han Xiao, Hao Liao, Defu Lian, Zheng Liu

**Updated**: 2024-12-17T17:15:21Z

**Summary**: Evaluation plays a crucial role in the advancement of information retrieval (IR) models. However, current benchmarks, which are based on predefined domains and human-labeled data, face limitations in addressing evaluation needs for emerging domains both cost-effectively and efficiently. To address this challenge, we propose the Automated Heterogeneous Information Retrieval Benchmark (AIR-Bench). AIR-Bench is distinguished by three key features: 1) Automated. The testing data in AIR-Bench is automatically generated by large language models (LLMs) without human intervention. 2) Heterogeneous. The testing data in AIR-Bench is generated with respect to diverse tasks, domains and languages. 3) Dynamic. The domains and languages covered by AIR-Bench are constantly augmented to provide an increasingly comprehensive evaluation benchmark for community developers. We develop a reliable and robust data generation pipeline to automatically create diverse and high-quality evaluation datasets based on real-world corpora. Our findings demonstrate that the generated testing data in AIR-Bench aligns well with human-labeled testing data, making AIR-Bench a dependable benchmark for evaluating IR models. The resources in AIR-Bench are publicly available at https://github.com/AIR-Bench/AIR-Bench.

**Link**: [arxiv](http://arxiv.org/abs/2412.13102v1),  [pdf](http://arxiv.org/pdf/2412.13102v1)

**Tags**: cs.IR cs.CL 



### Chatbots im Schulunterricht: Wir testen das Fobizz-Tool zur   automatischen Bewertung von Hausaufgaben
**Authors**: Rainer Muehlhoff, Marte Henningsen

**Updated**: 2024-12-17T17:06:01Z

**Summary**: [Study in German language.] This study examines the AI-powered grading tool "AI Grading Assistant" by the German company Fobizz, designed to support teachers in evaluating and providing feedback on student assignments. Against the societal backdrop of an overburdened education system and rising expectations for artificial intelligence as a solution to these challenges, the investigation evaluates the tool's functional suitability through two test series. The results reveal significant shortcomings: The tool's numerical grades and qualitative feedback are often random and do not improve even when its suggestions are incorporated. The highest ratings are achievable only with texts generated by ChatGPT. False claims and nonsensical submissions frequently go undetected, while the implementation of some grading criteria is unreliable and opaque. Since these deficiencies stem from the inherent limitations of large language models (LLMs), fundamental improvements to this or similar tools are not immediately foreseeable. The study critiques the broader trend of adopting AI as a quick fix for systemic problems in education, concluding that Fobizz's marketing of the tool as an objective and time-saving solution is misleading and irresponsible. Finally, the study calls for systematic evaluation and subject-specific pedagogical scrutiny of the use of AI tools in educational contexts.

**Link**: [arxiv](http://arxiv.org/abs/2412.06651v4),  [pdf](http://arxiv.org/pdf/2412.06651v4)

**Tags**: cs.CY cs.AI cs.CL cs.ET 97B10 



### LMUnit: Fine-grained Evaluation with Natural Language Unit Tests
**Authors**: Jon Saad-Falcon, Rajan Vivek, William Berrios, Nandita Shankar Naik, Matija Franklin, Bertie Vidgen, Amanpreet Singh, Douwe Kiela, Shikib Mehri

**Updated**: 2024-12-17T17:01:15Z

**Summary**: As language models become integral to critical workflows, assessing their behavior remains a fundamental challenge -- human evaluation is costly and noisy, while automated metrics provide only coarse, difficult-to-interpret signals. We introduce natural language unit tests, a paradigm that decomposes response quality into explicit, testable criteria, along with a unified scoring model, LMUnit, which combines multi-objective training across preferences, direct ratings, and natural language rationales. Through controlled human studies, we show this paradigm significantly improves inter-annotator agreement and enables more effective LLM development workflows. LMUnit achieves state-of-the-art performance on evaluation benchmarks (FLASK, BigGenBench) and competitive results on RewardBench. These results validate both our proposed paradigm and scoring model, suggesting a promising path forward for language model evaluation and development.

**Link**: [arxiv](http://arxiv.org/abs/2412.13091v1),  [pdf](http://arxiv.org/pdf/2412.13091v1)

**Tags**: cs.CL cs.AI 



### PersonaMark: Personalized LLM watermarking for model protection and user   attribution
**Authors**: Yuehan Zhang, Peizhuo Lv, Yinpeng Liu, Yongqiang Ma, Wei Lu, Xiaofeng Wang, Xiaozhong Liu, Jiawei Liu

**Updated**: 2024-12-17T16:52:12Z

**Summary**: The rapid advancement of customized Large Language Models (LLMs) offers considerable convenience. However, it also intensifies concerns regarding the protection of copyright/confidential information. With the extensive adoption of private LLMs, safeguarding model copyright and ensuring data privacy have become critical. Text watermarking has emerged as a viable solution for detecting AI-generated content and protecting models. However, existing methods fall short in providing individualized watermarks for each user, a critical feature for enhancing accountability and traceability. In this paper, we introduce PersonaMark, a novel personalized text watermarking scheme designed to protect LLMs' copyrights and bolster accountability. PersonaMark leverages sentence structure as a subtle carrier of watermark information and optimizes the generation process to maintain the natural output of the model. By employing a personalized hashing function, unique watermarks are embedded for each user, enabling high-quality text generation without compromising the model's performance. This approach is both time-efficient and scalable, capable of handling large numbers of users through a multi-user hashing mechanism. To the best of our knowledge, this is a pioneer study to explore personalized watermarking in LLMs. We conduct extensive evaluations across four LLMs, analyzing various metrics such as perplexity, sentiment, alignment, and readability. The results validate that PersonaMark preserves text quality, ensures unbiased watermark insertion, and offers robust watermark detection capabilities, all while maintaining the model's behavior with minimal disruption.

**Link**: [arxiv](http://arxiv.org/abs/2409.09739v2),  [pdf](http://arxiv.org/pdf/2409.09739v2)

**Tags**: cs.CR cs.CL 



### Sharp finite statistics for quantum key distribution
**Authors**: Vaisakh Mannalath, Víctor Zapatero, Marcos Curty

**Updated**: 2024-12-17T16:51:14Z

**Summary**: The performance of quantum key distribution (QKD) heavily depends on statistical inference. For a broad class of protocols, the central statistical task is a random sampling problem, customarily addressed using exponential tail bounds on the hypergeometric distribution. Here we devise a strikingly simple exponential bound for this task, of unprecedented tightness among QKD security analyses. As a by-product, confidence intervals for the average of non-identical Bernoulli parameters follow too. These naturally fit in statistical analyses of decoy-state QKD and also outperform standard tools. Lastly, we show that, in a vast parameter regime, the use of tail bounds is not enforced because the cumulative mass function of the hypergeometric distribution is accurately computable. This sharply decreases the minimum block sizes necessary for QKD, and reveals the tightness of our simple analytical bounds when moderate-to-large blocks are considered.

**Link**: [arxiv](http://arxiv.org/abs/2410.04095v2),  [pdf](http://arxiv.org/pdf/2410.04095v2)

**Tags**: quant-ph 



### Rethinking the Alignment of Psychotherapy Dialogue Generation with   Motivational Interviewing Strategies
**Authors**: Xin Sun, Xiao Tang, Abdallah El Ali, Zhuying Li, Pengjie Ren, Jan de Wit, Jiahuan Pei, Jos A. Bosch

**Updated**: 2024-12-17T16:44:16Z

**Summary**: Recent advancements in large language models (LLMs) have shown promise in generating psychotherapeutic dialogues, particularly in the context of motivational interviewing (MI). However, the inherent lack of transparency in LLM outputs presents significant challenges given the sensitive nature of psychotherapy. Applying MI strategies, a set of MI skills, to generate more controllable therapeutic-adherent conversations with explainability provides a possible solution. In this work, we explore the alignment of LLMs with MI strategies by first prompting the LLMs to predict the appropriate strategies as reasoning and then utilizing these strategies to guide the subsequent dialogue generation. We seek to investigate whether such alignment leads to more controllable and explainable generations. Multiple experiments including automatic and human evaluations are conducted to validate the effectiveness of MI strategies in aligning psychotherapy dialogue generation. Our findings demonstrate the potential of LLMs in producing strategically aligned dialogues and suggest directions for practical applications in psychotherapeutic settings.

**Link**: [arxiv](http://arxiv.org/abs/2408.06527v2),  [pdf](http://arxiv.org/pdf/2408.06527v2)

**Tags**: cs.CL cs.AI 



### Predicting Change, Not States: An Alternate Framework for Neural PDE   Surrogates
**Authors**: Anthony Zhou, Amir Barati Farimani

**Updated**: 2024-12-17T16:41:53Z

**Summary**: Neural surrogates for partial differential equations (PDEs) have become popular due to their potential to quickly simulate physics. With a few exceptions, neural surrogates generally treat the forward evolution of time-dependent PDEs as a black box by directly predicting the next state. While this is a natural and easy framework for applying neural surrogates, it can be an over-simplified and rigid framework for predicting physics. In this work, we propose an alternative framework in which neural solvers predict the temporal derivative and an ODE integrator forwards the solution in time, which has little overhead and is broadly applicable across model architectures and PDEs. We find that by simply changing the training target and introducing numerical integration during inference, neural surrogates can gain accuracy and stability. Predicting temporal derivatives also allows models to not be constrained to a specific temporal discretization, allowing for flexible time-stepping during inference or training on higher-resolution PDE data. Lastly, we investigate why this new framework can be beneficial and in what situations does it work well.

**Link**: [arxiv](http://arxiv.org/abs/2412.13074v1),  [pdf](http://arxiv.org/pdf/2412.13074v1)

**Tags**: cs.LG 



### On Distilling the Displacement Knowledge for Few-Shot Class-Incremental   Learning
**Authors**: Pengfei Fang, Yongchun Qin, Hui Xue

**Updated**: 2024-12-17T16:27:21Z

**Summary**: Few-shot Class-Incremental Learning (FSCIL) addresses the challenges of evolving data distributions and the difficulty of data acquisition in real-world scenarios. To counteract the catastrophic forgetting typically encountered in FSCIL, knowledge distillation is employed as a way to maintain the knowledge from learned data distribution. Recognizing the limitations of generating discriminative feature representations in a few-shot context, our approach incorporates structural information between samples into knowledge distillation. This structural information serves as a remedy for the low quality of features. Diverging from traditional structured distillation methods that compute sample similarity, we introduce the Displacement Knowledge Distillation (DKD) method. DKD utilizes displacement rather than similarity between samples, incorporating both distance and angular information to significantly enhance the information density retained through knowledge distillation. Observing performance disparities in feature distribution between base and novel classes, we propose the Dual Distillation Network (DDNet). This network applies traditional knowledge distillation to base classes and DKD to novel classes, challenging the conventional integration of novel classes with base classes. Additionally, we implement an instance-aware sample selector during inference to dynamically adjust dual branch weights, thereby leveraging the complementary strengths of each approach. Extensive testing on three benchmarks demonstrates that DDNet achieves state-of-the-art results. Moreover, through rigorous experimentation and comparison, we establish the robustness and general applicability of our proposed DKD method.

**Link**: [arxiv](http://arxiv.org/abs/2412.11017v2),  [pdf](http://arxiv.org/pdf/2412.11017v2)

**Tags**: cs.LG cs.CV 



### FunEditor: Achieving Complex Image Edits via Function Aggregation with   Diffusion Models
**Authors**: Mohammadreza Samadi, Fred X. Han, Mohammad Salameh, Hao Wu, Fengyu Sun, Chunhua Zhou, Di Niu

**Updated**: 2024-12-17T16:21:31Z

**Summary**: Diffusion models have demonstrated outstanding performance in generative tasks, making them ideal candidates for image editing. Recent studies highlight their ability to apply desired edits effectively by following textual instructions, yet with two key challenges remaining. First, these models struggle to apply multiple edits simultaneously, resulting in computational inefficiencies due to their reliance on sequential processing. Second, relying on textual prompts to determine the editing region can lead to unintended alterations to the image. We introduce FunEditor, an efficient diffusion model designed to learn atomic editing functions and perform complex edits by aggregating simpler functions. This approach enables complex editing tasks, such as object movement, by aggregating multiple functions and applying them simultaneously to specific areas. Our experiments demonstrate that FunEditor significantly outperforms recent inference-time optimization methods and fine-tuned models, either quantitatively across various metrics or through visual comparisons or both, on complex tasks like object movement and object pasting. In the meantime, with only 4 steps of inference, FunEditor achieves 5-24x inference speedups over existing popular methods. The code is available at: mhmdsmdi.github.io/funeditor/.

**Link**: [arxiv](http://arxiv.org/abs/2408.08495v2),  [pdf](http://arxiv.org/pdf/2408.08495v2)

**Tags**: cs.CV 



### Causal Prompting: Debiasing Large Language Model Prompting based on   Front-Door Adjustment
**Authors**: Congzhi Zhang, Linhai Zhang, Jialong Wu, Yulan He, Deyu Zhou

**Updated**: 2024-12-17T16:10:26Z

**Summary**: Despite the notable advancements of existing prompting methods, such as In-Context Learning and Chain-of-Thought for Large Language Models (LLMs), they still face challenges related to various biases. Traditional debiasing methods primarily focus on the model training stage, including approaches based on data augmentation and reweighting, yet they struggle with the complex biases inherent in LLMs. To address such limitations, the causal relationship behind the prompting methods is uncovered using a structural causal model, and a novel causal prompting method based on front-door adjustment is proposed to effectively mitigate LLMs biases. In specific, causal intervention is achieved by designing the prompts without accessing the parameters and logits of LLMs. The chain-of-thought generated by LLM is employed as the mediator variable and the causal effect between input prompts and output answers is calculated through front-door adjustment to mitigate model biases. Moreover, to accurately represent the chain-of-thoughts and estimate the causal effects, contrastive learning is used to fine-tune the encoder of chain-of-thought by aligning its space with that of the LLM. Experimental results show that the proposed causal prompting approach achieves excellent performance across seven natural language processing datasets on both open-source and closed-source LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2403.02738v3),  [pdf](http://arxiv.org/pdf/2403.02738v3)

**Tags**: cs.CL 



### CNNSum: Exploring Long-Context Summarization with Large Language Models   in Chinese Novels
**Authors**: Lingxiao Wei, He Yan, Xiangju Lu, Junmin Zhu, Jun Wang, Wei Zhang

**Updated**: 2024-12-17T16:03:43Z

**Summary**: Large Language Models (LLMs) have been well-researched in various long-context tasks. However, the scarcity of high-quality long-context summarization datasets has hindered further advancements in this area. To address this, we introduce CNNSum, a multi-scale long-context summarization benchmark based on Chinese novels, featuring human-driven annotations, which comprises four subsets totaling 695 samples, with lengths ranging from 16k to 128k. We evaluate numerous LLMs and conduct detailed case analyses. Furthermore, we conduct extensive fine-tuning experiments to explore and improve long-context summarization. In our study: (1) Advanced LLMs like GPT-4o may still generate subjective commentary, leading to vague summaries. (2) Currently, long-context summarization mainly relies on memory ability afforded by longer context lengths. The advantages of Large LLMs are hard to utilize, thus small LLMs are the most cost-effective. (3) Different prompt templates paired with various version models may cause large performance gaps. In further fine-tuning, these can be mitigated, and the Base version models perform better. (4) LLMs with RoPE-base scaled exhibit strong extrapolation potential; using short-context data can significantly improve long-context summarization performance. However, further applying other interpolation methods requires careful selection. (5) CNNSum provides more reliable and insightful evaluation results than other benchmarks. We release CNNSum to advance future research in this field. https://github.com/CxsGhost/CNNSum

**Link**: [arxiv](http://arxiv.org/abs/2412.02819v4),  [pdf](http://arxiv.org/pdf/2412.02819v4)

**Tags**: cs.CL cs.AI 



### Unleashing the Power of Pre-trained Language Models for Offline   Reinforcement Learning
**Authors**: Ruizhe Shi, Yuyao Liu, Yanjie Ze, Simon S. Du, Huazhe Xu

**Updated**: 2024-12-17T15:59:44Z

**Summary**: Offline reinforcement learning (RL) aims to find a near-optimal policy using pre-collected datasets. In real-world scenarios, data collection could be costly and risky; therefore, offline RL becomes particularly challenging when the in-domain data is limited. Given recent advances in Large Language Models (LLMs) and their few-shot learning prowess, this paper introduces $\textbf{La}$nguage Models for $\textbf{Mo}$tion Control ($\textbf{LaMo}$), a general framework based on Decision Transformers to effectively use pre-trained Language Models (LMs) for offline RL. Our framework highlights four crucial components: (1) Initializing Decision Transformers with sequentially pre-trained LMs, (2) employing the LoRA fine-tuning method, in contrast to full-weight fine-tuning, to combine the pre-trained knowledge from LMs and in-domain knowledge effectively, (3) using the non-linear MLP transformation instead of linear projections, to generate embeddings, and (4) integrating an auxiliary language prediction loss during fine-tuning to stabilize the LMs and retain their original abilities on languages. Empirical results indicate $\textbf{LaMo}$ achieves excellent performance in sparse-reward tasks and closes the gap between value-based offline RL methods and decision transformers in dense-reward tasks. In particular, our method demonstrates superior performance in scenarios with limited data samples.

**Link**: [arxiv](http://arxiv.org/abs/2310.20587v5),  [pdf](http://arxiv.org/pdf/2310.20587v5)

**Tags**: cs.LG 



### WHAT-IF: Exploring Branching Narratives by Meta-Prompting Large Language   Models
**Authors**: Runsheng "Anson" Huang, Lara J. Martin, Chris Callison-Burch

**Updated**: 2024-12-17T15:56:50Z

**Summary**: WHAT-IF -- Writing a Hero's Alternate Timeline through Interactive Fiction -- is a system that uses zero-shot meta-prompting to create branching narratives from a prewritten story. Played as an interactive fiction (IF) game, WHAT-IF lets the player choose between decisions that the large language model (LLM) GPT-4 generates as possible branches in the story. Starting with an existing linear plot as input, a branch is created at each key decision taken by the main character. By meta-prompting the LLM to consider the major plot points from the story, the system produces coherent and well-structured alternate storylines. WHAT-IF stores the branching plot tree in a graph which helps it to both keep track of the story for prompting and maintain the structure for the final IF system. A video demo of our system can be found here: https://youtu.be/8vBqjqtupcc.

**Link**: [arxiv](http://arxiv.org/abs/2412.10582v2),  [pdf](http://arxiv.org/pdf/2412.10582v2)

**Tags**: cs.CL 



### Late-Time Optical and X-ray Emission Evolution of the Oxygen-Rich SN   1996cr
**Authors**: Daniel Patnaude, Kathryn Weil, Robert Fesen, Dan Milisavljevic, Ralph Kraft

**Updated**: 2024-12-17T15:42:03Z

**Summary**: When the ejecta of supernovae interact with the progenitor star's circumstellar environment, a strong shock is driven back into the ejecta, causing the material to become bright optically and in X-rays. Most notably, as the shock traverses the H-rich envelope, it begins to interact with metal rich material. Thus, continued monitoring of bright and nearby supernovae provides valuable clues about both the progenitor structure and its pre-supernova evolution. Here we present late-time, multi-epoch optical and Chandra} X-ray spectra of the core-collapse supernova SN 1996cr. Magellan IMACS optical spectra taken in July 2017 and August 2021 show a very different spectrum from that seen in 2006 with broad, double-peaked optical emission lines of oxygen, argon, and sulfur with expansion velocities of $\pm 4500$ km s$^{-1}$. Red-shifted emission components are considerably fainter compared to the blue-shifted components, presumably due to internal extinction from dust in the supernova ejecta. Broad $\pm 2400$ km s$^{-1}$ H$\alpha$ is also seen which we infer is shocked progenitor pre-SN mass-loss, H-rich material. Chandra data indicate a slow but steady decline in overall X-ray luminosity, suggesting that the forward shock has broken through any circumstellar shell or torus which is inferred from prior deep Chandra ACIS-S/HETG observations. The X-ray properties are consistent with what is expected from a shock breaking out into a lower density environment. Though originally identified as a SN IIn, based upon late time optical emission line spectra, we argue that the SN 1996cr progenitor was partially or highly stripped, suggesting a SN IIb/Ib.

**Link**: [arxiv](http://arxiv.org/abs/2412.13024v1),  [pdf](http://arxiv.org/pdf/2412.13024v1)

**Tags**: astro-ph.HE 



### Relational Neurosymbolic Markov Models
**Authors**: Lennert De Smet, Gabriele Venturato, Luc De Raedt, Giuseppe Marra

**Updated**: 2024-12-17T15:41:51Z

**Summary**: Sequential problems are ubiquitous in AI, such as in reinforcement learning or natural language processing. State-of-the-art deep sequential models, like transformers, excel in these settings but fail to guarantee the satisfaction of constraints necessary for trustworthy deployment. In contrast, neurosymbolic AI (NeSy) provides a sound formalism to enforce constraints in deep probabilistic models but scales exponentially on sequential problems. To overcome these limitations, we introduce relational neurosymbolic Markov models (NeSy-MMs), a new class of end-to-end differentiable sequential models that integrate and provably satisfy relational logical constraints. We propose a strategy for inference and learning that scales on sequential settings, and that combines approximate Bayesian inference, automated reasoning, and gradient estimation. Our experiments show that NeSy-MMs can solve problems beyond the current state-of-the-art in neurosymbolic AI and still provide strong guarantees with respect to desired properties. Moreover, we show that our models are more interpretable and that constraints can be adapted at test time to out-of-distribution scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2412.13023v1),  [pdf](http://arxiv.org/pdf/2412.13023v1)

**Tags**: cs.AI cs.LG 



### OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in   Financial Domain
**Authors**: Shuting Wang, Jiejun Tan, Zhicheng Dou, Ji-Rong Wen

**Updated**: 2024-12-17T15:38:42Z

**Summary**: As a typical and practical application of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) techniques have gained extensive attention, particularly in vertical domains where LLMs may lack domain-specific knowledge. In this paper, we introduce an omnidirectional and automatic RAG benchmark, OmniEval, in the financial domain. Our benchmark is characterized by its multi-dimensional evaluation framework, including (1) a matrix-based RAG scenario evaluation system that categorizes queries into five task classes and 16 financial topics, leading to a structured assessment of diverse query scenarios; (2) a multi-dimensional evaluation data generation approach, which combines GPT-4-based automatic generation and human annotation, achieving an 87.47\% acceptance ratio in human evaluations on generated instances; (3) a multi-stage evaluation system that evaluates both retrieval and generation performance, result in a comprehensive evaluation on the RAG pipeline; and (4) robust evaluation metrics derived from rule-based and LLM-based ones, enhancing the reliability of assessments through manual annotations and supervised fine-tuning of an LLM evaluator. Our experiments demonstrate the comprehensiveness of OmniEval, which includes extensive test datasets and highlights the performance variations of RAG systems across diverse topics and tasks, revealing significant opportunities for RAG models to improve their capabilities in vertical domains. We open source the code of our benchmark in \href{https://github.com/RUC-NLPIR/OmniEval}{https://github.com/RUC-NLPIR/OmniEval}.

**Link**: [arxiv](http://arxiv.org/abs/2412.13018v1),  [pdf](http://arxiv.org/pdf/2412.13018v1)

**Tags**: cs.CL 



### Towards Reliable Latent Knowledge Estimation in LLMs: Zero-Prompt   Many-Shot Based Factual Knowledge Extraction
**Authors**: Qinyuan Wu, Mohammad Aflah Khan, Soumi Das, Vedant Nanda, Bishwamittra Ghosh, Camila Kolling, Till Speicher, Laurent Bindschaedler, Krishna P. Gummadi, Evimaria Terzi

**Updated**: 2024-12-17T15:38:23Z

**Summary**: In this paper, we focus on the challenging task of reliably estimating factual knowledge that is embedded inside large language models (LLMs). To avoid reliability concerns with prior approaches, we propose to eliminate prompt engineering when probing LLMs for factual knowledge. Our approach, called Zero-Prompt Latent Knowledge Estimator (ZP-LKE), leverages the in-context learning ability of LLMs to communicate both the factual knowledge question as well as the expected answer format. Our knowledge estimator is both conceptually simpler (i.e., doesn't depend on meta-linguistic judgments of LLMs) and easier to apply (i.e., is not LLM-specific), and we demonstrate that it can surface more of the latent knowledge embedded in LLMs. We also investigate how different design choices affect the performance of ZP-LKE. Using the proposed estimator, we perform a large-scale evaluation of the factual knowledge of a variety of open-source LLMs, like OPT, Pythia, Llama(2), Mistral, Gemma, etc. over a large set of relations and facts from the Wikidata knowledge base. We observe differences in the factual knowledge between different model families and models of different sizes, that some relations are consistently better known than others but that models differ in the precise facts they know, and differences in the knowledge of base models and their finetuned counterparts. Code available at: https://github.com/QinyuanWu0710/ZeroPrompt_LKE

**Link**: [arxiv](http://arxiv.org/abs/2404.12957v2),  [pdf](http://arxiv.org/pdf/2404.12957v2)

**Tags**: cs.CL cs.LG 



### The Emergence of Strategic Reasoning of Large Language Models
**Authors**: Dongwoo Lee, Gavin Kader

**Updated**: 2024-12-17T15:34:00Z

**Summary**: As Large Language Models (LLMs) are increasingly used for a variety of complex and critical tasks, it is vital to assess their logical capabilities in strategic environments. This paper examines their ability in strategic reasoning -- the process of choosing an optimal course of action by predicting and adapting to other agents' behavior. Using six LLMs, we analyze responses from play in classical games from behavioral economics (p-Beauty Contest, 11-20 Money Request Game, and Guessing Game) and evaluate their performance through hierarchical models of reasoning (level-$k$ theory and cognitive hierarchy theory). Our findings reveal that while LLMs show understanding of the games, the majority struggle with higher-order strategic reasoning. Although most LLMs did demonstrate learning ability with games involving repeated interactions, they still consistently fall short of the reasoning levels demonstrated by typical behavior from human subjects. The exception to these overall findings is with OpenAI's GPT-o1 -- specifically trained to solve complex reasoning tasks -- which consistently outperforms other LLMs and human subjects. These findings highlight the challenges and pathways in advancing LLMs toward robust strategic reasoning from the perspective of behavioral economics.

**Link**: [arxiv](http://arxiv.org/abs/2412.13013v1),  [pdf](http://arxiv.org/pdf/2412.13013v1)

**Tags**: econ.GN q-fin.EC 



### FootstepNet: an Efficient Actor-Critic Method for Fast On-line Bipedal   Footstep Planning and Forecasting
**Authors**: Clément Gaspard, Grégoire Passault, Mélodie Daniel, Olivier Ly

**Updated**: 2024-12-17T15:28:10Z

**Summary**: Designing a humanoid locomotion controller is challenging and classically split up in sub-problems. Footstep planning is one of those, where the sequence of footsteps is defined. Even in simpler environments, finding a minimal sequence, or even a feasible sequence, yields a complex optimization problem. In the literature, this problem is usually addressed by search-based algorithms (e.g. variants of A*). However, such approaches are either computationally expensive or rely on hand-crafted tuning of several parameters. In this work, at first, we propose an efficient footstep planning method to navigate in local environments with obstacles, based on state-of-the art Deep Reinforcement Learning (DRL) techniques, with very low computational requirements for on-line inference. Our approach is heuristic-free and relies on a continuous set of actions to generate feasible footsteps. In contrast, other methods necessitate the selection of a relevant discrete set of actions. Second, we propose a forecasting method, allowing to quickly estimate the number of footsteps required to reach different candidates of local targets. This approach relies on inherent computations made by the actor-critic DRL architecture. We demonstrate the validity of our approach with simulation results, and by a deployment on a kid-size humanoid robot during the RoboCup 2023 competition.

**Link**: [arxiv](http://arxiv.org/abs/2403.12589v2),  [pdf](http://arxiv.org/pdf/2403.12589v2)

**Tags**: cs.RO cs.AI 



### What is YOLOv6? A Deep Insight into the Object Detection Model
**Authors**: Athulya Sundaresan Geetha

**Updated**: 2024-12-17T15:26:15Z

**Summary**: This work explores the YOLOv6 object detection model in depth, concentrating on its design framework, optimization techniques, and detection capabilities. YOLOv6's core elements consist of the EfficientRep Backbone for robust feature extraction and the Rep-PAN Neck for seamless feature aggregation, ensuring high-performance object detection. Evaluated on the COCO dataset, YOLOv6-N achieves 37.5\% AP at 1187 FPS on an NVIDIA Tesla T4 GPU. YOLOv6-S reaches 45.0\% AP at 484 FPS, outperforming models like PPYOLOE-S, YOLOv5-S, YOLOX-S, and YOLOv8-S in the same class. Moreover, YOLOv6-M and YOLOv6-L also show better accuracy (50.0\% and 52.8\%) while maintaining comparable inference speeds to other detectors. With an upgraded backbone and neck structure, YOLOv6-L6 delivers cutting-edge accuracy in real-time.

**Link**: [arxiv](http://arxiv.org/abs/2412.13006v1),  [pdf](http://arxiv.org/pdf/2412.13006v1)

**Tags**: cs.CV 



### Exploring natural variation in tendon constitutive parameters via   Bayesian data selection and mixed effects models
**Authors**: James Casey, Jessica Forsyth, Timothy Waite, Simon Cotter, Tom Shearer

**Updated**: 2024-12-17T15:02:33Z

**Summary**: Combining microstructural mechanical models with experimental data enhances our understanding of the mechanics of soft tissue, such as tendons. In previous work, a Bayesian framework was used to infer constitutive parameters from uniaxial stress-strain experiments on horse tendons, specifically the superficial digital flexor tendon (SDFT) and common digital extensor tendon (CDET), on a per-experiment basis. Here, we extend this analysis to investigate the natural variation of these parameters across a population of horses. Using a Bayesian mixed effects model, we infer population distributions of these parameters. Given that the chosen hyperelastic model does not account for tendon damage, careful data selection is necessary. Avoiding ad hoc methods, we introduce a hierarchical Bayesian data selection method. This two-stage approach selects data per experiment, and integrates data weightings into the Bayesian mixed effects model. Our results indicate that the CDET is stiffer than the SDFT, likely due to a higher collagen volume fraction. The modes of the parameter distributions yield estimates of the product of the collagen volume fraction and Young's modulus as 811.5 MPa for the SDFT and 1430.2 MPa for the CDET. This suggests that positional tendons have stiffer collagen fibrils and/or higher collagen volume density than energy-storing tendons.

**Link**: [arxiv](http://arxiv.org/abs/2412.12983v1),  [pdf](http://arxiv.org/pdf/2412.12983v1)

**Tags**: stat.AP 



### Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental   Health
**Authors**: Vivek Kumar, Eirini Ntoutsi, Pushpraj Singh Rajawat, Giacomo Medda, Diego Reforgiato Recupero

**Updated**: 2024-12-17T15:01:07Z

**Summary**: Large language models (LLMs) have shown promising capabilities in healthcare analysis but face several challenges like hallucinations, parroting, and bias manifestation. These challenges are exacerbated in complex, sensitive, and low-resource domains. Therefore, in this work we introduce IC-AnnoMI, an expert-annotated motivational interviewing (MI) dataset built upon AnnoMI by generating in-context conversational dialogues leveraging LLMs, particularly ChatGPT. IC-AnnoMI employs targeted prompts accurately engineered through cues and tailored information, taking into account therapy style (empathy, reflection), contextual relevance, and false semantic change. Subsequently, the dialogues are annotated by experts, strictly adhering to the Motivational Interviewing Skills Code (MISC), focusing on both the psychological and linguistic dimensions of MI dialogues. We comprehensively evaluate the IC-AnnoMI dataset and ChatGPT's emotional reasoning ability and understanding of domain intricacies by modeling novel classification tasks employing several classical machine learning and current state-of-the-art transformer approaches. Finally, we discuss the effects of progressive prompting strategies and the impact of augmented data in mitigating the biases manifested in IC-AnnoM. Our contributions provide the MI community with not only a comprehensive dataset but also valuable insights for using LLMs in empathetic text generation for conversational therapy in supervised settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12981v1),  [pdf](http://arxiv.org/pdf/2412.12981v1)

**Tags**: cs.CL 



### ArchesWeather & ArchesWeatherGen: a deterministic and generative model   for efficient ML weather forecasting
**Authors**: Guillaume Couairon, Renu Singh, Anastase Charantonis, Christian Lessig, Claire Monteleoni

**Updated**: 2024-12-17T14:54:30Z

**Summary**: Weather forecasting plays a vital role in today's society, from agriculture and logistics to predicting the output of renewable energies, and preparing for extreme weather events. Deep learning weather forecasting models trained with the next state prediction objective on ERA5 have shown great success compared to numerical global circulation models. However, for a wide range of applications, being able to provide representative samples from the distribution of possible future weather states is critical. In this paper, we propose a methodology to leverage deterministic weather models in the design of probabilistic weather models, leading to improved performance and reduced computing costs. We first introduce \textbf{ArchesWeather}, a transformer-based deterministic model that improves upon Pangu-Weather by removing overrestrictive inductive priors. We then design a probabilistic weather model called \textbf{ArchesWeatherGen} based on flow matching, a modern variant of diffusion models, that is trained to project ArchesWeather's predictions to the distribution of ERA5 weather states. ArchesWeatherGen is a true stochastic emulator of ERA5 and surpasses IFS ENS and NeuralGCM on all WeatherBench headline variables (except for NeuralGCM's geopotential). Our work also aims to democratize the use of deterministic and generative machine learning models in weather forecasting research, with academic computing resources. All models are trained at 1.5{\deg} resolution, with a training budget of $\sim$9 V100 days for ArchesWeather and $\sim$45 V100 days for ArchesWeatherGen. For inference, ArchesWeatherGen generates 15-day weather trajectories at a rate of 1 minute per ensemble member on a A100 GPU card. To make our work fully reproducible, our code and models are open source, including the complete pipeline for data preparation, training, and evaluation, at https://github.com/INRIA/geoarches .

**Link**: [arxiv](http://arxiv.org/abs/2412.12971v1),  [pdf](http://arxiv.org/pdf/2412.12971v1)

**Tags**: cs.LG 



### On Local Overfitting and Forgetting in Deep Neural Networks
**Authors**: Uri Stern, Tomer Yaacoby, Daphna Weinshall

**Updated**: 2024-12-17T14:53:38Z

**Summary**: The infrequent occurrence of overfitting in deep neural networks is perplexing: contrary to theoretical expectations, increasing model size often enhances performance in practice. But what if overfitting does occur, though restricted to specific sub-regions of the data space? In this work, we propose a novel score that captures the forgetting rate of deep models on validation data. We posit that this score quantifies local overfitting: a decline in performance confined to certain regions of the data space. We then show empirically that local overfitting occurs regardless of the presence of traditional overfitting. Using the framework of deep over-parametrized linear models, we offer a certain theoretical characterization of forgotten knowledge, and show that it correlates with knowledge forgotten by real deep models. Finally, we devise a new ensemble method that aims to recover forgotten knowledge, relying solely on the training history of a single network. When combined with self-distillation, this method enhances the performance of any trained model without adding inference costs. Extensive empirical evaluations demonstrate the efficacy of our method across multiple datasets, contemporary neural network architectures, and training protocols.

**Link**: [arxiv](http://arxiv.org/abs/2412.12968v1),  [pdf](http://arxiv.org/pdf/2412.12968v1)

**Tags**: cs.LG 



### Neural Posterior Estimation for Stochastic Epidemic Modeling
**Authors**: Prayag Chatha, Fan Bu, Jeffrey Regier, Evan Snitkin, Jon Zelner

**Updated**: 2024-12-17T14:51:46Z

**Summary**: Stochastic infectious disease models capture uncertainty in public health outcomes and have become increasingly popular in epidemiological practice. However, calibrating these models to observed data is challenging with existing methods for parameter estimation. Stochastic epidemic models are nonlinear dynamical systems with potentially large latent state spaces, resulting in computationally intractable likelihood densities. We develop an approach to calibrating complex epidemiological models to high-dimensional data using Neural Posterior Estimation, a novel technique for simulation-based inference. In NPE, a neural conditional density estimator trained on simulated data learns to "invert" a stochastic simulator, returning a parametric approximation to the posterior distribution. We introduce a stochastic, discrete-time Susceptible Infected (SI) model with heterogeneous transmission for healthcare-associated infections (HAIs). HAIs are a major burden on healthcare systems. They exhibit high rates of asymptotic carriage, making it difficult to estimate infection rates. Through extensive simulation experiments, we show that NPE produces accurate posterior estimates of infection rates with greater sample efficiency compared to Approximate Bayesian Computation (ABC). We then use NPE to fit our SI model to an outbreak of carbapenem-resistant Klebsiella pneumoniae in a long-term acute care facility, finding evidence of location-based heterogeneity in patient-to-patient transmission risk. We argue that our methodology can be fruitfully applied to a wide range of mechanistic transmission models and problems in the epidemiology of infectious disease.

**Link**: [arxiv](http://arxiv.org/abs/2412.12967v1),  [pdf](http://arxiv.org/pdf/2412.12967v1)

**Tags**: stat.ME 



### Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic   Vision-language Context Sparsification
**Authors**: Wenxuan Huang, Zijie Zhai, Yunhang Shen, Shaosheng Cao, Fei Zhao, Xiangfeng Xu, Zheyu Ye, Shaohui Lin

**Updated**: 2024-12-17T14:45:12Z

**Summary**: Multimodal Large Language Models (MLLMs) have achieved remarkable success in vision understanding, reasoning, and interaction. However, the inference computation and memory increase progressively with the generation of output tokens during decoding, directly affecting the efficacy of MLLMs. Existing methods attempt to reduce the vision context redundancy to achieve efficient MLLMs. Unfortunately, the efficiency benefits of the vision context reduction in the prefill stage gradually diminish during the decoding stage. To address this problem, we proposed a dynamic vision-language context sparsification framework Dynamic-LLaVA, which dynamically reduces the redundancy of vision context in the prefill stage and decreases the memory and computation overhead of the generated language context during decoding. Dynamic-LLaVA designs a tailored sparsification inference scheme for different inference modes, i.e., prefill, decoding with and without KV cache, to achieve efficient inference of MLLMs. In practice, Dynamic-LLaVA can reduce computation consumption by $\sim$75\% in the prefill stage. Meanwhile, throughout the entire generation process of MLLMs, Dynamic-LLaVA reduces the $\sim$50\% computation consumption under decoding without KV cache, while saving $\sim$50\% GPU memory overhead when decoding with KV cache, due to the vision-language context sparsification. Extensive experiments also demonstrate that Dynamic-LLaVA achieves efficient inference for MLLMs with negligible understanding and generation ability degradation or even performance gains compared to the full-context inference baselines. Code is available at https://github.com/Osilly/dynamic_llava .

**Link**: [arxiv](http://arxiv.org/abs/2412.00876v3),  [pdf](http://arxiv.org/pdf/2412.00876v3)

**Tags**: cs.CV cs.AI cs.CL cs.LG 



### Adaptations of AI models for querying the LandMatrix database in natural   language
**Authors**: Fatiha Ait Kbir, Jérémy Bourgoin, Rémy Decoupes, Marie Gradeler, Roberto Interdonato

**Updated**: 2024-12-17T14:44:27Z

**Summary**: The Land Matrix initiative (https://landmatrix.org) and its global observatory aim to provide reliable data on large-scale land acquisitions to inform debates and actions in sectors such as agriculture, extraction, or energy in low- and middle-income countries. Although these data are recognized in the academic world, they remain underutilized in public policy, mainly due to the complexity of access and exploitation, which requires technical expertise and a good understanding of the database schema.   The objective of this work is to simplify access to data from different database systems. The methods proposed in this article are evaluated using data from the Land Matrix. This work presents various comparisons of Large Language Models (LLMs) as well as combinations of LLM adaptations (Prompt Engineering, RAG, Agents) to query different database systems (GraphQL and REST queries). The experiments are reproducible, and a demonstration is available online: https://github.com/tetis-nlp/landmatrix-graphql-python.

**Link**: [arxiv](http://arxiv.org/abs/2412.12961v1),  [pdf](http://arxiv.org/pdf/2412.12961v1)

**Tags**: cs.CL 



### SnakModel: Lessons Learned from Training an Open Danish Large Language   Model
**Authors**: Mike Zhang, Max Müller-Eberstein, Elisa Bassignana, Rob van der Goot

**Updated**: 2024-12-17T14:38:21Z

**Summary**: We present SnakModel, a Danish large language model (LLM) based on Llama2-7B, which we continuously pre-train on 13.6B Danish words, and further tune on 3.7M Danish instructions. As best practices for creating LLMs for smaller language communities have yet to be established, we examine the effects of early modeling and training decisions on downstream performance throughout the entire training pipeline, including (1) the creation of a strictly curated corpus of Danish text from diverse sources; (2) the language modeling and instruction-tuning training process itself, including the analysis of intermediate training dynamics, and ablations across different hyperparameters; (3) an evaluation on eight language and culturally-specific tasks. Across these experiments SnakModel achieves the highest overall performance, outperforming multiple contemporary Llama2-7B-based models. By making SnakModel, the majority of our pre-training corpus, and the associated code available under open licenses, we hope to foster further research and development in Danish Natural Language Processing, and establish training guidelines for languages with similar resource constraints.

**Link**: [arxiv](http://arxiv.org/abs/2412.12956v1),  [pdf](http://arxiv.org/pdf/2412.12956v1)

**Tags**: cs.CL 



### Efficient Diffusion Transformer Policies with Mixture of Expert   Denoisers for Multitask Learning
**Authors**: Moritz Reuss, Jyothish Pari, Pulkit Agrawal, Rudolf Lioutikov

**Updated**: 2024-12-17T14:34:51Z

**Summary**: Diffusion Policies have become widely used in Imitation Learning, offering several appealing properties, such as generating multimodal and discontinuous behavior. As models are becoming larger to capture more complex capabilities, their computational demands increase, as shown by recent scaling laws. Therefore, continuing with the current architectures will present a computational roadblock. To address this gap, we propose Mixture-of-Denoising Experts (MoDE) as a novel policy for Imitation Learning. MoDE surpasses current state-of-the-art Transformer-based Diffusion Policies while enabling parameter-efficient scaling through sparse experts and noise-conditioned routing, reducing both active parameters by 40% and inference costs by 90% via expert caching. Our architecture combines this efficient scaling with noise-conditioned self-attention mechanism, enabling more effective denoising across different noise levels. MoDE achieves state-of-the-art performance on 134 tasks in four established imitation learning benchmarks (CALVIN and LIBERO). Notably, by pretraining MoDE on diverse robotics data, we achieve 4.01 on CALVIN ABC and 0.95 on LIBERO-90. It surpasses both CNN-based and Transformer Diffusion Policies by an average of 57% across 4 benchmarks, while using 90% fewer FLOPs and fewer active parameters compared to default Diffusion Transformer architectures. Furthermore, we conduct comprehensive ablations on MoDE's components, providing insights for designing efficient and scalable Transformer architectures for Diffusion Policies. Code and demonstrations are available at https://mbreuss.github.io/MoDE_Diffusion_Policy/.

**Link**: [arxiv](http://arxiv.org/abs/2412.12953v1),  [pdf](http://arxiv.org/pdf/2412.12953v1)

**Tags**: cs.LG cs.RO 



### FineGates: LLMs Finetuning with Compression using Stochastic Gates
**Authors**: Jonathan Svirsky, Yehonathan Refael, Ofir Lindenbaum

**Updated**: 2024-12-17T14:33:05Z

**Summary**: Large Language Models (LLMs), with billions of parameters, present significant challenges for full finetuning due to the high computational demands, memory requirements, and impracticality of many real-world applications. When faced with limited computational resources or small datasets, updating all model parameters can often result in overfitting. To address this, lightweight finetuning techniques have been proposed, like learning low-rank adapter layers. These methods aim to train only a few additional parameters combined with the base model, which remains frozen, reducing resource usage and mitigating overfitting risks. In this work, we propose an adaptor model based on stochastic gates that simultaneously sparsify the frozen base model with task-specific adaptation. Our method comes with a small number of trainable parameters and allows us to speed up the base model inference with competitive accuracy. We evaluate it in additional variants by equipping it with additional low-rank parameters and comparing it to several recent baselines. Our results show that the proposed method improves the finetuned model accuracy comparatively to the several baselines and allows the removal of up to 20-40\% without significant accuracy loss.

**Link**: [arxiv](http://arxiv.org/abs/2412.12951v1),  [pdf](http://arxiv.org/pdf/2412.12951v1)

**Tags**: cs.LG 



### ProxyLLM : LLM-Driven Framework for Customer Support Through Text-Style   Transfer
**Authors**: Sehyeong Jo, Jungwon Seo

**Updated**: 2024-12-17T14:30:16Z

**Summary**: Chatbot-based customer support services have significantly advanced with the introduction of large language models (LLMs), enabling enhanced response quality and broader application across industries. However, while these advancements focus on reducing business costs and improving customer satisfaction, limited attention has been given to the experiences of customer service agents, who are critical to the service ecosystem. A major challenge faced by agents is the stress caused by unnecessary emotional exhaustion from harmful texts, which not only impairs their efficiency but also negatively affects customer satisfaction and business outcomes. In this work, we propose an LLM-powered system designed to enhance the working conditions of customer service agents by addressing emotionally intensive communications. Our proposed system leverages LLMs to transform the tone of customer messages, preserving actionable content while mitigating the emotional impact on human agents. Furthermore, the application is implemented as a Chrome extension, making it highly adaptable and easy to integrate into existing systems. Our method aims to enhance the overall service experience for businesses, customers, and agents.

**Link**: [arxiv](http://arxiv.org/abs/2412.09916v2),  [pdf](http://arxiv.org/pdf/2412.09916v2)

**Tags**: cs.HC 



### CrAM: Credibility-Aware Attention Modification in LLMs for Combating   Misinformation in RAG
**Authors**: Boyi Deng, Wenjie Wang, Fengbin Zhu, Qifan Wang, Fuli Feng

**Updated**: 2024-12-17T14:11:19Z

**Summary**: Retrieval-Augmented Generation (RAG) can alleviate hallucinations of Large Language Models (LLMs) by referencing external documents. However, the misinformation in external documents may mislead LLMs' generation. To address this issue, we explore the task of "credibility-aware RAG", in which LLMs automatically adjust the influence of retrieved documents based on their credibility scores to counteract misinformation. To this end, we introduce a plug-and-play method named $\textbf{Cr}$edibility-aware $\textbf{A}$ttention $\textbf{M}$odification (CrAM). CrAM identifies influential attention heads in LLMs and adjusts their attention weights based on the credibility of the documents, thereby reducing the impact of low-credibility documents. Experiments on Natual Questions and TriviaQA using Llama2-13B, Llama3-8B, and Qwen1.5-7B show that CrAM improves the RAG performance of LLMs against misinformation pollution by over 20%, even surpassing supervised fine-tuning methods.

**Link**: [arxiv](http://arxiv.org/abs/2406.11497v3),  [pdf](http://arxiv.org/pdf/2406.11497v3)

**Tags**: cs.CL 



### Truthful Text Sanitization Guided by Inference Attacks
**Authors**: Ildikó Pilán, Benet Manzanares-Salor, David Sánchez, Pierre Lison

**Updated**: 2024-12-17T14:07:01Z

**Summary**: The purpose of text sanitization is to rewrite those text spans in a document that may directly or indirectly identify an individual, to ensure they no longer disclose personal information. Text sanitization must strike a balance between preventing the leakage of personal information (privacy protection) while also retaining as much of the document's original content as possible (utility preservation). We present an automated text sanitization strategy based on generalizations, which are more abstract (but still informative) terms that subsume the semantic content of the original text spans. The approach relies on instruction-tuned large language models (LLMs) and is divided into two stages. The LLM is first applied to obtain truth-preserving replacement candidates and rank them according to their abstraction level. Those candidates are then evaluated for their ability to protect privacy by conducting inference attacks with the LLM. Finally, the system selects the most informative replacement shown to be resistant to those attacks. As a consequence of this two-stage process, the chosen replacements effectively balance utility and privacy. We also present novel metrics to automatically evaluate these two aspects without the need to manually annotate data. Empirical results on the Text Anonymization Benchmark show that the proposed approach leads to enhanced utility, with only a marginal increase in the risk of re-identifying protected individuals compared to fully suppressing the original information. Furthermore, the selected replacements are shown to be more truth-preserving and abstractive than previous methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.12928v1),  [pdf](http://arxiv.org/pdf/2412.12928v1)

**Tags**: cs.CL 



### SCANS: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious   Activation Steering
**Authors**: Zouying Cao, Yifei Yang, Hai Zhao

**Updated**: 2024-12-17T13:32:36Z

**Summary**: Safety alignment is indispensable for Large Language Models (LLMs) to defend threats from malicious instructions. However, recent researches reveal safety-aligned LLMs prone to reject benign queries due to the exaggerated safety issue, limiting their helpfulness. In this paper, we propose a Safety-Conscious Activation Steering (SCANS) method to mitigate the exaggerated safety concerns in aligned LLMs. First, SCANS extracts the refusal steering vectors within the activation space and utilizes vocabulary projection to anchor some specific safety-critical layers which influence model refusal behavior. Second, by tracking the hidden state transition, SCANS identifies the steering direction and steers the model behavior accordingly, achieving a balance between exaggerated safety and adequate safety. Experiments show that SCANS achieves new state-of-the-art performance on XSTest and OKTest benchmarks, without impairing their defense capability against harmful queries and maintaining almost unchanged model capability.

**Link**: [arxiv](http://arxiv.org/abs/2408.11491v2),  [pdf](http://arxiv.org/pdf/2408.11491v2)

**Tags**: cs.AI 



### Black-box Model Ensembling for Textual and Visual Question Answering via   Information Fusion
**Authors**: Yuxi Xia, Kilm Zaporojets, Benjamin Roth

**Updated**: 2024-12-17T13:31:18Z

**Summary**: A diverse range of large language models (LLMs), e.g., ChatGPT, and visual question answering (VQA) models, e.g., BLIP, have been developed for solving textual and visual question answering tasks. However, fine-tuning these models is either difficult, as it requires access via APIs, rendering them as black-boxes, or costly due to the need of tuning a large number of parameters. To address this, we introduce InfoSel, a data-efficient ensemble method that learns to dynamically pick the winner from existing black-box models for predictions on both textual and multimodal visual question answering tasks. Unlike traditional ensemble models, InfoSel does not rely on prediction probabilities or confidences, which typically are not available in black-box models. Experimental results on four datasets demonstrate that our approach achieves an absolute increase of up to +5.19\% in the F1-score compared to standalone LLMs using only 1K training instances.

**Link**: [arxiv](http://arxiv.org/abs/2407.12841v2),  [pdf](http://arxiv.org/pdf/2407.12841v2)

**Tags**: cs.CL cs.AI 



### Testing mirror symmetry in the Universe with LIGO-Virgo black-hole   mergers
**Authors**: Juan Calderón Bustillo, Adrian del Rio, Nicolas Sanchis-Gual, Koustav Chandra, Samson H. W. Leong

**Updated**: 2024-12-17T13:26:37Z

**Summary**: Certain precessing black-hole mergers produce gravitational waves with net circular polarization, understood as an imbalance between right- and left-handed amplitudes. According to the Cosmological Principle, such emission must average to zero across all binary mergers in our Universe to preserve mirror-reflection symmetry at very large scales. We present a new independent gravitational-wave test of this hypothesis. Using a novel observable based on the Chern-Pontryagin pseudo-scalar, we measure the emission of net circular polarization across 47 black-hole mergers recently analyzed by Islam et. al. with a state-of-the art model for precessing black-hole mergers in General Relativity. The average value obtained is consistent with zero. Remarkably, however, we find that at least $82\%$ of the analysed sources must have produced net circular polarization. Of these, GW200129 shows strong evidence for mirror asymmetry, with a Bayes Factor of 12.6 or, equivalently, $93.1\%$ probability. We obtain consistent (although stronger) results of $97.5\%$ and $94.3\%$ respectively using public results on this event from Hannam et. al. and performing our own parameter inference. This finding further implies evidence of astrophysical sources that can spontaneously emit circularly polarized photons by quantum effects. Forthcoming black-hole merger detections will enable stronger constraints on large-scale mirror asymmetry and the Cosmological Principle.

**Link**: [arxiv](http://arxiv.org/abs/2402.09861v3),  [pdf](http://arxiv.org/pdf/2402.09861v3)

**Tags**: gr-qc astro-ph.HE 



### DoPTA: Improving Document Layout Analysis using Patch-Text Alignment
**Authors**: Nikitha SR, Tarun Ram Menta, Mausoom Sarkar

**Updated**: 2024-12-17T13:26:31Z

**Summary**: The advent of multimodal learning has brought a significant improvement in document AI. Documents are now treated as multimodal entities, incorporating both textual and visual information for downstream analysis. However, works in this space are often focused on the textual aspect, using the visual space as auxiliary information. While some works have explored pure vision based techniques for document image understanding, they require OCR identified text as input during inference, or do not align with text in their learning procedure. Therefore, we present a novel image-text alignment technique specially designed for leveraging the textual information in document images to improve performance on visual tasks. Our document encoder model DoPTA - trained with this technique demonstrates strong performance on a wide range of document image understanding tasks, without requiring OCR during inference. Combined with an auxiliary reconstruction objective, DoPTA consistently outperforms larger models, while using significantly lesser pre-training compute. DoPTA also sets new state-of-the art results on D4LA, and FUNSD, two challenging document visual analysis benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2412.12902v1),  [pdf](http://arxiv.org/pdf/2412.12902v1)

**Tags**: cs.CV 



### An Agentic Approach to Automatic Creation of P&ID Diagrams from Natural   Language Descriptions
**Authors**: Shreeyash Gowaikar, Srinivasan Iyengar, Sameer Segal, Shivkumar Kalyanaraman

**Updated**: 2024-12-17T13:21:26Z

**Summary**: The Piping and Instrumentation Diagrams (P&IDs) are foundational to the design, construction, and operation of workflows in the engineering and process industries. However, their manual creation is often labor-intensive, error-prone, and lacks robust mechanisms for error detection and correction. While recent advancements in Generative AI, particularly Large Language Models (LLMs) and Vision-Language Models (VLMs), have demonstrated significant potential across various domains, their application in automating generation of engineering workflows remains underexplored. In this work, we introduce a novel copilot for automating the generation of P&IDs from natural language descriptions. Leveraging a multi-step agentic workflow, our copilot provides a structured and iterative approach to diagram creation directly from Natural Language prompts. We demonstrate the feasibility of the generation process by evaluating the soundness and completeness of the workflow, and show improved results compared to vanilla zero-shot and few-shot generation approaches.

**Link**: [arxiv](http://arxiv.org/abs/2412.12898v1),  [pdf](http://arxiv.org/pdf/2412.12898v1)

**Tags**: cs.LG cs.CE cs.CL cs.MA 



### Question: How do Large Language Models perform on the Question Answering   tasks? Answer:
**Authors**: Kevin Fischer, Darren Fürst, Sebastian Steindl, Jakob Lindner, Ulrich Schäfer

**Updated**: 2024-12-17T13:19:38Z

**Summary**: Large Language Models (LLMs) have been showing promising results for various NLP-tasks without the explicit need to be trained for these tasks by using few-shot or zero-shot prompting techniques. A common NLP-task is question-answering (QA). In this study, we propose a comprehensive performance comparison between smaller fine-tuned models and out-of-the-box instruction-following LLMs on the Stanford Question Answering Dataset 2.0 (SQuAD2), specifically when using a single-inference prompting technique. Since the dataset contains unanswerable questions, previous work used a double inference method. We propose a prompting style which aims to elicit the same ability without the need for double inference, saving compute time and resources. Furthermore, we investigate their generalization capabilities by comparing their performance on similar but different QA datasets, without fine-tuning neither model, emulating real-world uses where the context and questions asked may differ from the original training distribution, for example swapping Wikipedia for news articles.   Our results show that smaller, fine-tuned models outperform current State-Of-The-Art (SOTA) LLMs on the fine-tuned task, but recent SOTA models are able to close this gap on the out-of-distribution test and even outperform the fine-tuned models on 3 of the 5 tested QA datasets.

**Link**: [arxiv](http://arxiv.org/abs/2412.12893v1),  [pdf](http://arxiv.org/pdf/2412.12893v1)

**Tags**: cs.CL 



### Can GPT-O1 Kill All Bugs? An Evaluation of GPT-Family LLMs on QuixBugs
**Authors**: Haichuan Hu, Ye Shang, Guolin Xu, Congqing He, Quanjun Zhang

**Updated**: 2024-12-17T13:16:56Z

**Summary**: LLMs have long demonstrated remarkable effectiveness in automatic program repair (APR), with OpenAI's ChatGPT being one of the most widely used models in this domain. Through continuous iterations and upgrades of GPT-family models, their performance in fixing bugs has already reached state-of-the-art levels. However, there are few works comparing the effectiveness and variations of different versions of GPT-family models on APR. In this work, inspired by the recent public release of the GPT-o1 models, we conduct the first study to compare the effectiveness of different versions of the GPT-family models in APR. We evaluate the performance of the latest version of the GPT-family models (i.e., O1-preview and O1-mini), GPT-4o, and the historical version of ChatGPT on APR. We conduct an empirical study of the four GPT-family models against other LLMs and APR techniques on the QuixBugs benchmark from multiple evaluation perspectives, including repair success rate, repair cost, response length, and behavior patterns. The results demonstrate that O1's repair capability exceeds that of prior GPT-family models, successfully fixing all 40 bugs in the benchmark. Our work can serve as a foundation for further in-depth exploration of the applications of GPT-family models in APR.

**Link**: [arxiv](http://arxiv.org/abs/2409.10033v3),  [pdf](http://arxiv.org/pdf/2409.10033v3)

**Tags**: cs.SE cs.AI 



### Theory of Unsupervised Super-Resolution Data Assimilation with   Conditional Variational Autoencoders: Estimating Background Covariances via   Super-Resolution
**Authors**: Yuki Yasuda, Ryo Onishi

**Updated**: 2024-12-17T13:13:51Z

**Summary**: This study proposes a theory of unsupervised super-resolution data assimilation (SRDA) using conditional variational autoencoders (CVAEs). The theory is based on an evidence lower bound that leads to an objective function for unsupervised learning. This function can be reduced to the objective function of a traditional data assimilation method, namely the three-dimensional variational (3D-Var) formalism. Similar to 3D-Var, it is essential to use a non-diagonal background error covariance matrix to assimilate distant observations. Instead of using such a non-diagonal matrix, we extend the proposed theory by using the non-locality of super-resolution (SR). For linear SR, SR operators serve as background error covariance matrices. For nonlinear SR, error backpropagation through SR neural networks induces covariance structures in inference. SRDA can be performed using CVAEs because the loss function for CVAEs is generally an evidence lower bound. By incorporating the SR neural network into the CVAE, the encoder estimates the high-resolution (HR) analysis from HR observations and low-resolution (LR) forecasts. The decoder acts as the observation operator and reconstructs the HR observations from the estimated HR analysis. The effectiveness of SRDA was evaluated through numerical experiments using an idealized barotropic ocean jet system. Compared to inference with an ensemble Kalman filter, SRDA demonstrated superior accuracy in HR inference. SRDA was also computationally efficient because it does not require HR numerical integration or ensemble calculations. The findings of this study provide a theoretical basis for integrating SR and DA, which will stimulate further research in this direction.

**Link**: [arxiv](http://arxiv.org/abs/2308.03351v4),  [pdf](http://arxiv.org/pdf/2308.03351v4)

**Tags**: physics.ao-ph 



### A Comparative Study of Pruning Methods in Transformer-based Time Series   Forecasting
**Authors**: Nicholas Kiefer, Arvid Weyrauch, Muhammed Öz, Achim Streit, Markus Götz, Charlotte Debus

**Updated**: 2024-12-17T13:07:31Z

**Summary**: The current landscape in time-series forecasting is dominated by Transformer-based models. Their high parameter count and corresponding demand in computational resources pose a challenge to real-world deployment, especially for commercial and scientific applications with low-power embedded devices. Pruning is an established approach to reduce neural network parameter count and save compute. However, the implications and benefits of pruning Transformer-based models for time series forecasting are largely unknown. To close this gap, we provide a comparative benchmark study by evaluating unstructured and structured pruning on various state-of-the-art multivariate time series models. We study the effects of these pruning strategies on model predictive performance and computational aspects like model size, operations, and inference time. Our results show that certain models can be pruned even up to high sparsity levels, outperforming their dense counterpart. However, fine-tuning pruned models is necessary. Furthermore, we demonstrate that even with corresponding hardware and software support, structured pruning is unable to provide significant time savings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12883v1),  [pdf](http://arxiv.org/pdf/2412.12883v1)

**Tags**: cs.LG cs.AI 



### RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented   Verification and Refinement
**Authors**: Jinhao Jiang, Jiayi Chen, Junyi Li, Ruiyang Ren, Shijie Wang, Wayne Xin Zhao, Yang Song, Tao Zhang

**Updated**: 2024-12-17T13:05:36Z

**Summary**: Existing large language models (LLMs) show exceptional problem-solving capabilities but might struggle with complex reasoning tasks. Despite the successes of chain-of-thought and tree-based search methods, they mainly depend on the internal knowledge of LLMs to search over intermediate reasoning steps, limited to dealing with simple tasks involving fewer reasoning steps. In this paper, we propose \textbf{RAG-Star}, a novel RAG approach that integrates the retrieved information to guide the tree-based deliberative reasoning process that relies on the inherent knowledge of LLMs. By leveraging Monte Carlo Tree Search, RAG-Star iteratively plans intermediate sub-queries and answers for reasoning based on the LLM itself. To consolidate internal and external knowledge, we propose an retrieval-augmented verification that utilizes query- and answer-aware reward modeling to provide feedback for the inherent reasoning of LLMs. Our experiments involving Llama-3.1-8B-Instruct and GPT-4o demonstrate that RAG-Star significantly outperforms previous RAG and reasoning methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.12881v1),  [pdf](http://arxiv.org/pdf/2412.12881v1)

**Tags**: cs.CL cs.AI 



### Preference-Oriented Supervised Fine-Tuning: Favoring Target Model Over   Aligned Large Language Models
**Authors**: Yuchen Fan, Yuzhong Hong, Qiushi Wang, Junwei Bao, Hongfei Jiang, Yang Song

**Updated**: 2024-12-17T12:49:14Z

**Summary**: Alignment, endowing a pre-trained Large language model (LLM) with the ability to follow instructions, is crucial for its real-world applications. Conventional supervised fine-tuning (SFT) methods formalize it as causal language modeling typically with a cross-entropy objective, requiring a large amount of high-quality instruction-response pairs. However, the quality of widely used SFT datasets can not be guaranteed due to the high cost and intensive labor for the creation and maintenance in practice. To overcome the limitations associated with the quality of SFT datasets, we introduce a novel \textbf{p}reference-\textbf{o}riented supervised \textbf{f}ine-\textbf{t}uning approach, namely PoFT. The intuition is to boost SFT by imposing a particular preference: \textit{favoring the target model over aligned LLMs on the same SFT data.} This preference encourages the target model to predict a higher likelihood than that predicted by the aligned LLMs, incorporating assessment information on data quality (i.e., predicted likelihood by the aligned LLMs) into the training process. Extensive experiments are conducted, and the results validate the effectiveness of the proposed method. PoFT achieves stable and consistent improvements over the SFT baselines across different training datasets and base models. Moreover, we prove that PoFT can be integrated with existing SFT data filtering methods to achieve better performance, and further improved by following preference optimization procedures, such as DPO.

**Link**: [arxiv](http://arxiv.org/abs/2412.12865v1),  [pdf](http://arxiv.org/pdf/2412.12865v1)

**Tags**: cs.CL 



### Fine-tuning Large Language Models for Domain-specific Machine   Translation
**Authors**: Jiawei Zheng, Hanghai Hong, Feiyan Liu, Xiaoli Wang, Jingsong Su, Yonggui Liang, Shikai Wu

**Updated**: 2024-12-17T12:45:20Z

**Summary**: Large language models (LLMs) have shown great potential in domain-specific machine translation (MT). However, one major issue is that LLMs pre-trained on general domain corpus might not generalize well to specific domains due to the lack of domain-specific knowledge. To address this issue, this paper focuses on enhancing the domain-specific MT capability of LLMs, by providing high-quality training datasets and proposing a novel fine-tuning framework denoted by DragFT. DragFT augments LLMs via three techniques: (i) Dictionary-enhanced prompting integrates dictionary information into prompts to improve the translation of domain-specific terminology.; (ii) RAG-based few-shot example selection provides high-quality examples that simulate both the domain and style characteristics; (iii) Fine-tuning with few-shot examples further enhances performance when using in-domain examples. We deploy DragFT on three well-known LLM backbones with 13B training parameters to validate its effectiveness. The results on three domain-specific datasets show that DragFT achieves a significant performance boost and shows superior performance compared to advanced models such as GPT-3.5 and GPT-4o. The drastic performance improvement of DragFT over existing LLMs can be attributed to incorporating relevant knowledge while mitigating noise.

**Link**: [arxiv](http://arxiv.org/abs/2402.15061v2),  [pdf](http://arxiv.org/pdf/2402.15061v2)

**Tags**: cs.CL cs.LG 



### DISC: Plug-and-Play Decoding Intervention with Similarity of Characters   for Chinese Spelling Check
**Authors**: Ziheng Qiao, Houquan Zhou, Yumeng Liu, Zhenghua Li, Min Zhang, Bo Zhang, Chen Li, Ji Zhang, Fei Huang

**Updated**: 2024-12-17T12:44:06Z

**Summary**: One key characteristic of the Chinese spelling check (CSC) task is that incorrect characters are usually similar to the correct ones in either phonetics or glyph. To accommodate this, previous works usually leverage confusion sets, which suffer from two problems, i.e., difficulty in determining which character pairs to include and lack of probabilities to distinguish items in the set. In this paper, we propose a light-weight plug-and-play DISC (i.e., decoding intervention with similarity of characters) module for CSC models.DISC measures phonetic and glyph similarities between characters and incorporates this similarity information only during the inference phase. This method can be easily integrated into various existing CSC models, such as ReaLiSe, SCOPE, and ReLM, without additional training costs. Experiments on three CSC benchmarks demonstrate that our proposed method significantly improves model performance, approaching and even surpassing the current state-of-the-art models.

**Link**: [arxiv](http://arxiv.org/abs/2412.12863v1),  [pdf](http://arxiv.org/pdf/2412.12863v1)

**Tags**: cs.CL cs.AI 



### LLMLight: Large Language Models as Traffic Signal Control Agents
**Authors**: Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, Hui Xiong

**Updated**: 2024-12-17T12:41:13Z

**Summary**: Traffic Signal Control (TSC) is a crucial component in urban traffic management, aiming to optimize road network efficiency and reduce congestion. Traditional TSC methods, primarily based on transportation engineering and reinforcement learning (RL), often struggle with generalization abilities across varied traffic scenarios and lack interpretability. This paper presents LLMLight, a novel framework employing Large Language Models (LLMs) as decision-making agents for TSC. Specifically, the framework begins by instructing the LLM with a knowledgeable prompt detailing real-time traffic conditions. Leveraging the advanced generalization capabilities of LLMs, LLMLight engages a reasoning and decision-making process akin to human intuition for effective traffic control. Moreover, we build LightGPT, a specialized backbone LLM tailored for TSC tasks. By learning nuanced traffic patterns and control strategies, LightGPT enhances the LLMLight framework cost-effectively. Extensive experiments conducted on ten real-world and synthetic datasets, along with evaluations by fifteen human experts, demonstrate the exceptional effectiveness, generalization ability, and interpretability of LLMLight with LightGPT, outperforming nine baseline methods and ten advanced LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2312.16044v5),  [pdf](http://arxiv.org/pdf/2312.16044v5)

**Tags**: cs.AI 



### Identification and Estimation of Average Causal Effects in Fixed Effects   Logit Models
**Authors**: Laurent Davezies, Xavier D'Haultfœuille, Louise Laage

**Updated**: 2024-12-17T12:40:40Z

**Summary**: This paper studies identification and estimation of average causal effects, such as average marginal or treatment effects, in fixed effects logit models with short panels. Relating the identified set of these effects to an extremal moment problem, we first show how to obtain sharp bounds on such effects simply, without any optimization. We also consider even simpler outer bounds, which, contrary to the sharp bounds, do not require any first-step nonparametric estimators. We build confidence intervals based on these two approaches and show their asymptotic validity. Monte Carlo simulations suggest that both approaches work well in practice, the second being typically competitive in terms of interval length. Finally, we show that our method is also useful to measure treatment effect heterogeneity.

**Link**: [arxiv](http://arxiv.org/abs/2105.00879v4),  [pdf](http://arxiv.org/pdf/2105.00879v4)

**Tags**: econ.EM stat.ME 



### Enhancing Character-Level Understanding in LLMs through Token Internal   Structure Learning
**Authors**: Zhu Xu, Zhiqiang Zhao, Zihan Zhang, Yuchi Liu, Quanwei Shen, Fei Liu, Yu Kuang, Jian He, Conglin Liu

**Updated**: 2024-12-17T12:37:47Z

**Summary**: Tokenization methods like Byte-Pair Encoding (BPE) enhance computational efficiency in large language models (LLMs) but often obscure internal character structures within tokens. This limitation hinders LLMs' ability to predict precise character positions, which is crucial in tasks like Chinese Spelling Correction (CSC) where identifying the positions of misspelled characters accelerates correction processes. We propose Token Internal Position Awareness (TIPA), a method that significantly improves models' ability to capture character positions within tokens by training them on reverse character prediction tasks using the tokenizer's vocabulary. Experiments demonstrate that TIPA enhances position prediction accuracy in LLMs, enabling more precise identification of target characters in original text. Furthermore, when applied to downstream tasks that do not require exact position prediction, TIPA still boosts performance in tasks needing character-level information, validating its versatility and effectiveness.

**Link**: [arxiv](http://arxiv.org/abs/2411.17679v3),  [pdf](http://arxiv.org/pdf/2411.17679v3)

**Tags**: cs.CL 



### Selective Shot Learning for Code Explanation
**Authors**: Paheli Bhattacharya, Rishabh Gupta

**Updated**: 2024-12-17T12:26:14Z

**Summary**: Code explanation plays a crucial role in the software engineering domain, aiding developers in grasping code functionality efficiently. Recent work shows that the performance of LLMs for code explanation improves in a few-shot setting, especially when the few-shot examples are selected intelligently. State-of-the-art approaches for such Selective Shot Learning (SSL) include token-based and embedding-based methods. However, these SSL approaches have been evaluated on proprietary LLMs, without much exploration on open-source Code-LLMs. Additionally, these methods lack consideration for programming language syntax. To bridge these gaps, we present a comparative study and propose a novel SSL method (SSL_ner) that utilizes entity information for few-shot example selection. We present several insights and show the effectiveness of SSL_ner approach over state-of-the-art methods across two datasets. To the best of our knowledge, this is the first systematic benchmarking of open-source Code-LLMs while assessing the performances of the various few-shot examples selection approaches for the code explanation task.

**Link**: [arxiv](http://arxiv.org/abs/2412.12852v1),  [pdf](http://arxiv.org/pdf/2412.12852v1)

**Tags**: cs.SE cs.CL cs.IR 



### ClarityEthic: Explainable Moral Judgment Utilizing Contrastive Ethical   Insights from Large Language Models
**Authors**: Yuxi Sun, Wei Gao, Jing Ma, Hongzhan Lin, Ziyang Luo, Wenxuan Zhang

**Updated**: 2024-12-17T12:22:44Z

**Summary**: With the rise and widespread use of Large Language Models (LLMs), ensuring their safety is crucial to prevent harm to humans and promote ethical behaviors. However, directly assessing value valence (i.e., support or oppose) by leveraging large-scale data training is untrustworthy and inexplainable. We assume that emulating humans to rely on social norms to make moral decisions can help LLMs understand and predict moral judgment. However, capturing human values remains a challenge, as multiple related norms might conflict in specific contexts. Consider norms that are upheld by the majority and promote the well-being of society are more likely to be accepted and widely adopted (e.g., "don't cheat,"). Therefore, it is essential for LLM to identify the appropriate norms for a given scenario before making moral decisions. To this end, we introduce a novel moral judgment approach called \textit{ClarityEthic} that leverages LLMs' reasoning ability and contrastive learning to uncover relevant social norms for human actions from different perspectives and select the most reliable one to enhance judgment accuracy. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches in moral judgment tasks. Moreover, human evaluations confirm that the generated social norms provide plausible explanations that support the judgments. This suggests that modeling human moral judgment with the emulating humans moral strategy is promising for improving the ethical behaviors of LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.12848v1),  [pdf](http://arxiv.org/pdf/2412.12848v1)

**Tags**: cs.CY cs.AI cs.SI 



### Towards Reliable Detection of LLM-Generated Texts: A Comprehensive   Evaluation Framework with CUDRT
**Authors**: Zhen Tao, Yanfang Chen, Dinghao Xi, Zhiyu Li, Wei Xu

**Updated**: 2024-12-17T12:20:34Z

**Summary**: The increasing prevalence of large language models (LLMs) has significantly advanced text generation, but the human-like quality of LLM outputs presents major challenges in reliably distinguishing between human-authored and LLM-generated texts. Existing detection benchmarks are constrained by their reliance on static datasets, scenario-specific tasks (e.g., question answering and text refinement), and a primary focus on English, overlooking the diverse linguistic and operational subtleties of LLMs. To address these gaps, we propose CUDRT, a comprehensive evaluation framework and bilingual benchmark in Chinese and English, categorizing LLM activities into five key operations: Create, Update, Delete, Rewrite, and Translate. CUDRT provides extensive datasets tailored to each operation, featuring outputs from state-of-the-art LLMs to assess the reliability of LLM-generated text detectors. This framework supports scalable, reproducible experiments and enables in-depth analysis of how operational diversity, multilingual training sets, and LLM architectures influence detection performance. Our extensive experiments demonstrate the framework's capacity to optimize detection systems, providing critical insights to enhance reliability, cross-linguistic adaptability, and detection accuracy. By advancing robust methodologies for identifying LLM-generated texts, this work contributes to the development of intelligent systems capable of meeting real-world multilingual detection challenges. Source code and dataset are available at GitHub.

**Link**: [arxiv](http://arxiv.org/abs/2406.09056v3),  [pdf](http://arxiv.org/pdf/2406.09056v3)

**Tags**: cs.CL cs.AI 



### Efficient Event-based Semantic Segmentation with Spike-driven   Lightweight Transformer-based Networks
**Authors**: Xiaxin Zhu, Fangming Guo, Xianlei Long, Qingyi Gu, Chao Chen, Fuqiang Gu

**Updated**: 2024-12-17T12:11:04Z

**Summary**: Event-based semantic segmentation has great potential in autonomous driving and robotics due to the advantages of event cameras, such as high dynamic range, low latency, and low power cost. Unfortunately, current artificial neural network (ANN)-based segmentation methods suffer from high computational demands, the requirements for image frames, and massive energy consumption, limiting their efficiency and application on resource-constrained edge/mobile platforms. To address these problems, we introduce SLTNet, a spike-driven lightweight transformer-based network designed for event-based semantic segmentation. Specifically, SLTNet is built on efficient spike-driven convolution blocks (SCBs) to extract rich semantic features while reducing the model's parameters. Then, to enhance the long-range contextural feature interaction, we propose novel spike-driven transformer blocks (STBs) with binary mask operations. Based on these basic blocks, SLTNet employs a high-efficiency single-branch architecture while maintaining the low energy consumption of the Spiking Neural Network (SNN). Finally, extensive experiments on DDD17 and DSEC-Semantic datasets demonstrate that SLTNet outperforms state-of-the-art (SOTA) SNN-based methods by at least 7.30% and 3.30% mIoU, respectively, with extremely 5.48x lower energy consumption and 1.14x faster inference speed.

**Link**: [arxiv](http://arxiv.org/abs/2412.12843v1),  [pdf](http://arxiv.org/pdf/2412.12843v1)

**Tags**: cs.CV cs.AI 



### Benchmarking and Understanding Compositional Relational Reasoning of   LLMs
**Authors**: Ruikang Ni, Da Xiao, Qingye Meng, Xiangyu Li, Shihui Zheng, Hongliang Liang

**Updated**: 2024-12-17T12:10:38Z

**Summary**: Compositional relational reasoning (CRR) is a hallmark of human intelligence, but we lack a clear understanding of whether and how existing transformer large language models (LLMs) can solve CRR tasks. To enable systematic exploration of the CRR capability of LLMs, we first propose a new synthetic benchmark called Generalized Associative Recall (GAR) by integrating and generalizing the essence of several tasks in mechanistic interpretability (MI) study in a unified framework. Evaluation shows that GAR is challenging enough for existing LLMs, revealing their fundamental deficiency in CRR. Meanwhile, it is easy enough for systematic MI study. Then, to understand how LLMs solve GAR tasks, we use attribution patching to discover the core circuits reused by Vicuna-33B across different tasks and a set of vital attention heads. Intervention experiments show that the correct functioning of these heads significantly impacts task performance. Especially, we identify two classes of heads whose activations represent the abstract notion of true and false in GAR tasks respectively. They play a fundamental role in CRR across various models and tasks. The dataset and code are available at https://github.com/Caiyun-AI/GAR.

**Link**: [arxiv](http://arxiv.org/abs/2412.12841v1),  [pdf](http://arxiv.org/pdf/2412.12841v1)

**Tags**: cs.CL cs.LG 



### From An LLM Swarm To A PDDL-Empowered HIVE: Planning Self-Executed   Instructions In A Multi-Modal Jungle
**Authors**: Kaustubh Vyas, Damien Graux, Yijun Yang, Sébastien Montella, Chenxin Diao, Wendi Zhou, Pavlos Vougiouklis, Ruofei Lai, Yang Ren, Keshuang Li, Jeff Z. Pan

**Updated**: 2024-12-17T12:05:21Z

**Summary**: In response to the call for agent-based solutions that leverage the ever-increasing capabilities of the deep models' ecosystem, we introduce Hive -- a comprehensive solution for selecting appropriate models and subsequently planning a set of atomic actions to satisfy the end-users' instructions. Hive operates over sets of models and, upon receiving natural language instructions (i.e. user queries), schedules and executes explainable plans of atomic actions. These actions can involve one or more of the available models to achieve the overall task, while respecting end-users specific constraints. Notably, Hive handles tasks that involve multi-modal inputs and outputs, enabling it to handle complex, real-world queries. Our system is capable of planning complex chains of actions while guaranteeing explainability, using an LLM-based formal logic backbone empowered by PDDL operations. We introduce the MuSE benchmark in order to offer a comprehensive evaluation of the multi-modal capabilities of agent systems. Our findings show that our framework redefines the state-of-the-art for task selection, outperforming other competing systems that plan operations across multiple models while offering transparency guarantees while fully adhering to user constraints.

**Link**: [arxiv](http://arxiv.org/abs/2412.12839v1),  [pdf](http://arxiv.org/pdf/2412.12839v1)

**Tags**: cs.AI 



### Scrutinizing the Vulnerability of Decentralized Learning to Membership   Inference Attacks
**Authors**: Ousmane Touat, Jezekael Brunon, Yacine Belal, Julien Nicolas, Mohamed Maouche, César Sabater, Sonia Ben Mokhtar

**Updated**: 2024-12-17T12:02:47Z

**Summary**: The primary promise of decentralized learning is to allow users to engage in the training of machine learning models in a collaborative manner while keeping their data on their premises and without relying on any central entity. However, this paradigm necessitates the exchange of model parameters or gradients between peers. Such exchanges can be exploited to infer sensitive information about training data, which is achieved through privacy attacks (e.g Membership Inference Attacks -- MIA). In order to devise effective defense mechanisms, it is important to understand the factors that increase/reduce the vulnerability of a given decentralized learning architecture to MIA. In this study, we extensively explore the vulnerability to MIA of various decentralized learning architectures by varying the graph structure (e.g number of neighbors), the graph dynamics, and the aggregation strategy, across diverse datasets and data distributions. Our key finding, which to the best of our knowledge we are the first to report, is that the vulnerability to MIA is heavily correlated to (i) the local model mixing strategy performed by each node upon reception of models from neighboring nodes and (ii) the global mixing properties of the communication graph. We illustrate these results experimentally using four datasets and by theoretically analyzing the mixing properties of various decentralized architectures. Our paper draws a set of lessons learned for devising decentralized learning systems that reduce by design the vulnerability to MIA.

**Link**: [arxiv](http://arxiv.org/abs/2412.12837v1),  [pdf](http://arxiv.org/pdf/2412.12837v1)

**Tags**: cs.LG cs.DC 



### FocusChat: Text-guided Long Video Understanding via Spatiotemporal   Information Filtering
**Authors**: Zheng Cheng, Rendong Wang, Zhicheng Wang

**Updated**: 2024-12-17T11:54:47Z

**Summary**: Recently, multi-modal large language models have made significant progress. However, visual information lacking of guidance from the user's intention may lead to redundant computation and involve unnecessary visual noise, especially in long, untrimmed videos. To address this issue, we propose FocusChat, a text-guided multi-modal large language model (LLM) that emphasizes visual information correlated to the user's prompt. In detail, Our model first undergoes the semantic extraction module, which comprises a visual semantic branch and a text semantic branch to extract image and text semantics, respectively. The two branches are combined using the Spatial-Temporal Filtering Module (STFM). STFM enables explicit spatial-level information filtering and implicit temporal-level feature filtering, ensuring that the visual tokens are closely aligned with the user's query. It lowers the essential number of visual tokens inputted into the LLM. FocusChat significantly outperforms Video-LLaMA in zero-shot experiments, using an order of magnitude less training data with only 16 visual tokens occupied. It achieves results comparable to the state-of-the-art in few-shot experiments, with only 0.72M pre-training data.

**Link**: [arxiv](http://arxiv.org/abs/2412.12833v1),  [pdf](http://arxiv.org/pdf/2412.12833v1)

**Tags**: cs.CV 



### DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction   in the Era of Large Language Models
**Authors**: Jinxiang Xie, Yilin Li, Xunjian Yin, Xiaojun Wan

**Updated**: 2024-12-17T11:54:16Z

**Summary**: Evaluating the performance of Grammatical Error Correction (GEC) models has become increasingly challenging, as large language model (LLM)-based GEC systems often produce corrections that diverge from provided gold references. This discrepancy undermines the reliability of traditional reference-based evaluation metrics. In this study, we propose a novel evaluation framework for GEC models, DSGram, integrating Semantic Coherence, Edit Level, and Fluency, and utilizing a dynamic weighting mechanism. Our framework employs the Analytic Hierarchy Process (AHP) in conjunction with large language models to ascertain the relative importance of various evaluation criteria. Additionally, we develop a dataset incorporating human annotations and LLM-simulated sentences to validate our algorithms and fine-tune more cost-effective models. Experimental results indicate that our proposed approach enhances the effectiveness of GEC model evaluations.

**Link**: [arxiv](http://arxiv.org/abs/2412.12832v1),  [pdf](http://arxiv.org/pdf/2412.12832v1)

**Tags**: cs.CL cs.AI 



### Revisiting In-context Learning Inference Circuit in Large Language   Models
**Authors**: Hakaze Cho, Mariko Kato, Yoshihiro Sakai, Naoya Inoue

**Updated**: 2024-12-17T11:51:51Z

**Summary**: In-context Learning (ICL) is an emerging few-shot learning paradigm on Language Models (LMs) with inner mechanisms un-explored. There are already existing works describing the inner processing of ICL, while they struggle to capture all the inference phenomena in large language models. Therefore, this paper proposes a comprehensive circuit to model the inference dynamics and try to explain the observed phenomena of ICL. In detail, we divide ICL inference into 3 major operations: (1) Input Text Encode: LMs encode every input text (demonstrations and queries) into linear representation in the hidden states with sufficient information to solve ICL tasks. (2) Semantics Merge: LMs merge the encoded representations of demonstrations with their corresponding label tokens to produce joint representations of labels and demonstrations. (3) Feature Retrieval and Copy: LMs search the joint representations similar to the query representation on a task subspace, and copy the searched representations into the query. Then, language model heads capture these copied label representations to a certain extent and decode them into predicted labels. The proposed inference circuit successfully captured many phenomena observed during the ICL process, making it a comprehensive and practical explanation of the ICL inference process. Moreover, ablation analysis by disabling the proposed steps seriously damages the ICL performance, suggesting the proposed inference circuit is a dominating mechanism. Additionally, we confirm and list some bypass mechanisms that solve ICL tasks in parallel with the proposed circuit.

**Link**: [arxiv](http://arxiv.org/abs/2410.04468v2),  [pdf](http://arxiv.org/pdf/2410.04468v2)

**Tags**: cs.CL cs.AI cs.LG 



### Detecting Emotional Incongruity of Sarcasm by Commonsense Reasoning
**Authors**: Ziqi Qiu, Jianxing Yu, Yufeng Zhang, Hanjiang Lai, Yanghui Rao, Qinliang Su, Jian Yin

**Updated**: 2024-12-17T11:25:55Z

**Summary**: This paper focuses on sarcasm detection, which aims to identify whether given statements convey criticism, mockery, or other negative sentiment opposite to the literal meaning. To detect sarcasm, humans often require a comprehensive understanding of the semantics in the statement and even resort to external commonsense to infer the fine-grained incongruity. However, existing methods lack commonsense inferential ability when they face complex real-world scenarios, leading to unsatisfactory performance. To address this problem, we propose a novel framework for sarcasm detection, which conducts incongruity reasoning based on commonsense augmentation, called EICR. Concretely, we first employ retrieval-augmented large language models to supplement the missing but indispensable commonsense background knowledge. To capture complex contextual associations, we construct a dependency graph and obtain the optimized topology via graph refinement. We further introduce an adaptive reasoning skeleton that integrates prior rules to extract sentiment-inconsistent subgraphs explicitly. To eliminate the possible spurious relations between words and labels, we employ adversarial contrastive learning to enhance the robustness of the detector. Experiments conducted on five datasets demonstrate the effectiveness of EICR.

**Link**: [arxiv](http://arxiv.org/abs/2412.12808v1),  [pdf](http://arxiv.org/pdf/2412.12808v1)

**Tags**: cs.CL cs.AI 



### Learning Set Functions with Implicit Differentiation
**Authors**: Gözde Özcan, Chengzhi Shi, Stratis Ioannidis

**Updated**: 2024-12-17T11:14:52Z

**Summary**: Ou et al. (2022) introduce the problem of learning set functions from data generated by a so-called optimal subset oracle. Their approach approximates the underlying utility function with an energy-based model, whose parameters are estimated via mean-field variational inference. Ou et al. (2022) show this reduces to fixed point iterations; however, as the number of iterations increases, automatic differentiation quickly becomes computationally prohibitive due to the size of the Jacobians that are stacked during backpropagation. We address this challenge with implicit differentiation and examine the convergence conditions for the fixed-point iterations. We empirically demonstrate the efficiency of our method on synthetic and real-world subset selection applications including product recommendation, set anomaly detection and compound selection tasks.

**Link**: [arxiv](http://arxiv.org/abs/2412.11239v2),  [pdf](http://arxiv.org/pdf/2412.11239v2)

**Tags**: cs.LG cs.AI 



### RCTrans: Radar-Camera Transformer via Radar Densifier and Sequential   Decoder for 3D Object Detection
**Authors**: Yiheng Li, Yang Yang, Zhen Lei

**Updated**: 2024-12-17T11:02:36Z

**Summary**: In radar-camera 3D object detection, the radar point clouds are sparse and noisy, which causes difficulties in fusing camera and radar modalities. To solve this, we introduce a novel query-based detection method named Radar-Camera Transformer (RCTrans). Specifically, we first design a Radar Dense Encoder to enrich the sparse valid radar tokens, and then concatenate them with the image tokens. By doing this, we can fully explore the 3D information of each interest region and reduce the interference of empty tokens during the fusing stage. We then design a Pruning Sequential Decoder to predict 3D boxes based on the obtained tokens and random initialized queries. To alleviate the effect of elevation ambiguity in radar point clouds, we gradually locate the position of the object via a sequential fusion structure. It helps to get more precise and flexible correspondences between tokens and queries. A pruning training strategy is adopted in the decoder, which can save much time during inference and inhibit queries from losing their distinctiveness. Extensive experiments on the large-scale nuScenes dataset prove the superiority of our method, and we also achieve new state-of-the-art radar-camera 3D detection results. Our implementation is available at https://github.com/liyih/RCTrans.

**Link**: [arxiv](http://arxiv.org/abs/2412.12799v1),  [pdf](http://arxiv.org/pdf/2412.12799v1)

**Tags**: cs.CV cs.AI 



### Implicit Location-Caption Alignment via Complementary Masking for   Weakly-Supervised Dense Video Captioning
**Authors**: Shiping Ge, Qiang Chen, Zhiwei Jiang, Yafeng Yin, Liu Qin, Ziyao Chen, Qing Gu

**Updated**: 2024-12-17T10:52:50Z

**Summary**: Weakly-Supervised Dense Video Captioning (WSDVC) aims to localize and describe all events of interest in a video without requiring annotations of event boundaries. This setting poses a great challenge in accurately locating the temporal location of event, as the relevant supervision is unavailable. Existing methods rely on explicit alignment constraints between event locations and captions, which involve complex event proposal procedures during both training and inference. To tackle this problem, we propose a novel implicit location-caption alignment paradigm by complementary masking, which simplifies the complex event proposal and localization process while maintaining effectiveness. Specifically, our model comprises two components: a dual-mode video captioning module and a mask generation module. The dual-mode video captioning module captures global event information and generates descriptive captions, while the mask generation module generates differentiable positive and negative masks for localizing the events. These masks enable the implicit alignment of event locations and captions by ensuring that captions generated from positively and negatively masked videos are complementary, thereby forming a complete video description. In this way, even under weak supervision, the event location and event caption can be aligned implicitly. Extensive experiments on the public datasets demonstrate that our method outperforms existing weakly-supervised methods and achieves competitive results compared to fully-supervised methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.12791v1),  [pdf](http://arxiv.org/pdf/2412.12791v1)

**Tags**: cs.CV cs.AI cs.MM I.2.10 



### Activating Distributed Visual Region within LLMs for Efficient and   Effective Vision-Language Training and Inference
**Authors**: Siyuan Wang, Dianyi Wang, Chengxing Zhou, Zejun Li, Zhihao Fan, Xuanjing Huang, Zhongyu Wei

**Updated**: 2024-12-17T10:44:47Z

**Summary**: Large Vision-Language Models (LVLMs) typically learn visual capacity through visual instruction tuning, involving updates to both a projector and their LLM backbones. Drawing inspiration from the concept of visual region in the human brain, we investigate the existence of an analogous \textit{visual region} within LLMs that functions as a cognitive core, and explore the possibility of efficient training of LVLMs via selective layers tuning. We use Bunny-Llama-3-8B-V for detailed experiments and LLaVA-1.5-7B and LLaVA-1.5-13B for validation across a range of visual and textual tasks. Our findings reveal that selectively updating 25\% of LLMs layers, when sparsely and uniformly distributed, can preserve nearly 99\% of visual performance while maintaining or enhancing textual task results, and also effectively reducing training time. Based on this targeted training approach, we further propose a novel visual region-based pruning paradigm, removing non-critical layers outside the visual region, which can achieve minimal performance loss. This study offers an effective and efficient strategy for LVLM training and inference by activating a layer-wise visual region within LLMs, which is consistently effective across different models and parameter scales.

**Link**: [arxiv](http://arxiv.org/abs/2412.12785v1),  [pdf](http://arxiv.org/pdf/2412.12785v1)

**Tags**: cs.CV 



### RemoteRAG: A Privacy-Preserving LLM Cloud RAG Service
**Authors**: Yihang Cheng, Lan Zhang, Junyang Wang, Mu Yuan, Yunhao Yao

**Updated**: 2024-12-17T10:36:52Z

**Summary**: Retrieval-augmented generation (RAG) improves the service quality of large language models by retrieving relevant documents from credible literature and integrating them into the context of the user query. Recently, the rise of the cloud RAG service has made it possible for users to query relevant documents conveniently. However, directly sending queries to the cloud brings potential privacy leakage. In this paper, we are the first to formally define the privacy-preserving cloud RAG service to protect the user query and propose RemoteRAG as a solution regarding privacy, efficiency, and accuracy. For privacy, we introduce $(n,\epsilon)$-DistanceDP to characterize privacy leakage of the user query and the leakage inferred from relevant documents. For efficiency, we limit the search range from the total documents to a small number of selected documents related to a perturbed embedding generated from $(n,\epsilon)$-DistanceDP, so that computation and communication costs required for privacy protection significantly decrease. For accuracy, we ensure that the small range includes target documents related to the user query with detailed theoretical analysis. Experimental results also demonstrate that RemoteRAG can resist existing embedding inversion attack methods while achieving no loss in retrieval under various settings. Moreover, RemoteRAG is efficient, incurring only $0.67$ seconds and $46.66$KB of data transmission ($2.72$ hours and $1.43$ GB with the non-optimized privacy-preserving scheme) when retrieving from a total of $10^6$ documents.

**Link**: [arxiv](http://arxiv.org/abs/2412.12775v1),  [pdf](http://arxiv.org/pdf/2412.12775v1)

**Tags**: cs.IR cs.CR 



### HyperGraphOS: A Modern Meta-Operating System for the Scientific and   Engineering Domains
**Authors**: Antonello Ceravola, Frank Joublin

**Updated**: 2024-12-17T10:35:33Z

**Summary**: This paper presents HyperGraphOS, a significant innovation in the domain of operating systems, specifically designed to address the needs of scientific and engineering domains. This platform aims to combine model-based engineering, graph modeling, data containers, and documents, along with tools for handling computational elements. HyperGraphOS functions as an Operating System offering to users an infinite workspace for creating and managing complex models represented as graphs with customizable semantics. By leveraging a web-based architecture, it requires only a modern web browser for access, allowing organization of knowledge, documents, and content into models represented in a network of workspaces. Elements of the workspace are defined in terms of domain-specific languages (DSLs). These DSLs are pivotal for navigating workspaces, generating code, triggering AI components, and organizing information and processes. The models' dual nature as both visual drawings and data structures allows dynamic modifications and inspections both interactively as well as programaticaly. We evaluated HyperGraphOS's efficiency and applicability across a large set of diverse domains, including the design and development of a virtual Avatar dialog system, a robotic task planner based on large language models (LLMs), a new meta-model for feature-based code development and many others. Our findings show that HyperGraphOS offers substantial benefits in the interaction with a computer as information system, as platoform for experiments and data analysis, as streamlined engineering processes, demonstrating enhanced flexibility in managing data, computation and documents, showing an innovative approaches to persistent desktop environments.

**Link**: [arxiv](http://arxiv.org/abs/2412.10487v2),  [pdf](http://arxiv.org/pdf/2412.10487v2)

**Tags**: cs.SE cs.OS cs.PL 68 



### Optimize the Unseen -- Fast NeRF Cleanup with Free Space Prior
**Authors**: Leo Segre, Shai Avidan

**Updated**: 2024-12-17T10:33:36Z

**Summary**: Neural Radiance Fields (NeRF) have advanced photorealistic novel view synthesis, but their reliance on photometric reconstruction introduces artifacts, commonly known as "floaters". These artifacts degrade novel view quality, especially in areas unseen by the training cameras. We present a fast, post-hoc NeRF cleanup method that eliminates such artifacts by enforcing our Free Space Prior, effectively minimizing floaters without disrupting the NeRF's representation of observed regions. Unlike existing approaches that rely on either Maximum Likelihood (ML) estimation to fit the data or a complex, local data-driven prior, our method adopts a Maximum-a-Posteriori (MAP) approach, selecting the optimal model parameters under a simple global prior assumption that unseen regions should remain empty. This enables our method to clean artifacts in both seen and unseen areas, enhancing novel view quality even in challenging scene regions. Our method is comparable with existing NeRF cleanup models while being 2.5x faster in inference time, requires no additional memory beyond the original NeRF, and achieves cleanup training in less than 30 seconds. Our code will be made publically available.

**Link**: [arxiv](http://arxiv.org/abs/2412.12772v1),  [pdf](http://arxiv.org/pdf/2412.12772v1)

**Tags**: cs.CV 



### A Survey on Sequential Recommendation
**Authors**: Liwei Pan, Weike Pan, Meiyan Wei, Hongzhi Yin, Zhong Ming

**Updated**: 2024-12-17T10:33:13Z

**Summary**: Different from most conventional recommendation problems, sequential recommendation focuses on learning users' preferences by exploiting the internal order and dependency among the interacted items, which has received significant attention from both researchers and practitioners. In recent years, we have witnessed great progress and achievements in this field, necessitating a new survey. In this survey, we study the SR problem from a new perspective (i.e., the construction of an item's properties), and summarize the most recent techniques used in sequential recommendation such as pure ID-based SR, SR with side information, multi-modal SR, generative SR, LLM-powered SR, ultra-long SR and data-augmented SR. Moreover, we introduce some frontier research topics in sequential recommendation, e.g., open-domain SR, data-centric SR, could-edge collaborative SR, continuous SR, SR for good, and explainable SR. We believe that our survey could be served as a valuable roadmap for readers in this field.

**Link**: [arxiv](http://arxiv.org/abs/2412.12770v1),  [pdf](http://arxiv.org/pdf/2412.12770v1)

**Tags**: cs.IR 



### A Survey of Calibration Process for Black-Box LLMs
**Authors**: Liangru Xie, Hui Liu, Jingying Zeng, Xianfeng Tang, Yan Han, Chen Luo, Jing Huang, Zhen Li, Suhang Wang, Qi He

**Updated**: 2024-12-17T10:31:21Z

**Summary**: Large Language Models (LLMs) demonstrate remarkable performance in semantic understanding and generation, yet accurately assessing their output reliability remains a significant challenge. While numerous studies have explored calibration techniques, they primarily focus on White-Box LLMs with accessible parameters. Black-Box LLMs, despite their superior performance, pose heightened requirements for calibration techniques due to their API-only interaction constraints. Although recent researches have achieved breakthroughs in black-box LLMs calibration, a systematic survey of these methodologies is still lacking. To bridge this gap, we presents the first comprehensive survey on calibration techniques for black-box LLMs. We first define the Calibration Process of LLMs as comprising two interrelated key steps: Confidence Estimation and Calibration. Second, we conduct a systematic review of applicable methods within black-box settings, and provide insights on the unique challenges and connections in implementing these key steps. Furthermore, we explore typical applications of Calibration Process in black-box LLMs and outline promising future research directions, providing new perspectives for enhancing reliability and human-machine alignment. This is our GitHub link: https://github.com/LiangruXie/Calibration-Process-in-Black-Box-LLMs

**Link**: [arxiv](http://arxiv.org/abs/2412.12767v1),  [pdf](http://arxiv.org/pdf/2412.12767v1)

**Tags**: cs.AI cs.CL 



### First-order integer-valued autoregressive processes with Generalized   Katz innovations
**Authors**: Ovielt Baltodano Lopez, Federico Bassetti, Giulia Carallo, Roberto Casarin

**Updated**: 2024-12-17T10:25:14Z

**Summary**: A new integer--valued autoregressive process (INAR) with Generalised Lagrangian Katz (GLK) innovations is defined. This process family provides a flexible modelling framework for count data, allowing for under and over--dispersion, asymmetry, and excess of kurtosis and includes standard INAR models such as Generalized Poisson and Negative Binomial as special cases. We show that the GLK--INAR process is discrete semi--self--decomposable, infinite divisible, stable by aggregation and provides stationarity conditions. Some extensions are discussed, such as the Markov--Switching and the zero--inflated GLK--INARs. A Bayesian inference framework and an efficient posterior approximation procedure are introduced. The proposed models are applied to 130 time series from Google Trend, which proxy the worldwide public concern about climate change. New evidence is found of heterogeneity across time, countries and keywords in the persistence, uncertainty, and long--run public awareness level.

**Link**: [arxiv](http://arxiv.org/abs/2202.02029v2),  [pdf](http://arxiv.org/pdf/2202.02029v2)

**Tags**: stat.ME econ.EM 62F15, 62M10 



### PolSAM: Polarimetric Scattering Mechanism Informed Segment Anything   Model
**Authors**: Yuqing Wang, Zhongling Huang, Shuxin Yang, Hao Tang, Xiaolan Qiu, Junwei Han, Dingwen Zhang

**Updated**: 2024-12-17T09:59:53Z

**Summary**: PolSAR data presents unique challenges due to its rich and complex characteristics. Existing data representations, such as complex-valued data, polarimetric features, and amplitude images, are widely used. However, these formats often face issues related to usability, interpretability, and data integrity. Most feature extraction networks for PolSAR are small, limiting their ability to capture features effectively. To address these issues, We propose the Polarimetric Scattering Mechanism-Informed SAM (PolSAM), an enhanced Segment Anything Model (SAM) that integrates domain-specific scattering characteristics and a novel prompt generation strategy. PolSAM introduces Microwave Vision Data (MVD), a lightweight and interpretable data representation derived from polarimetric decomposition and semantic correlations. We propose two key components: the Feature-Level Fusion Prompt (FFP), which fuses visual tokens from pseudo-colored SAR images and MVD to address modality incompatibility in the frozen SAM encoder, and the Semantic-Level Fusion Prompt (SFP), which refines sparse and dense segmentation prompts using semantic information. Experimental results on the PhySAR-Seg datasets demonstrate that PolSAM significantly outperforms existing SAM-based and multimodal fusion models, improving segmentation accuracy, reducing data storage, and accelerating inference time. The source code and datasets will be made publicly available at \url{https://github.com/XAI4SAR/PolSAM}.

**Link**: [arxiv](http://arxiv.org/abs/2412.12737v1),  [pdf](http://arxiv.org/pdf/2412.12737v1)

**Tags**: cs.CV 



### Using LLM-Generated Draft Replies to Support Human Experts in Responding   to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of   Industrial AI
**Authors**: Tita Alissa Bach, Aleksandar Babic, Narae Park, Tor Sporsem, Rasmus Ulfsnes, Henrik Smith-Meyer, Torkel Skeie

**Updated**: 2024-12-17T09:55:02Z

**Summary**: The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

**Link**: [arxiv](http://arxiv.org/abs/2412.12732v1),  [pdf](http://arxiv.org/pdf/2412.12732v1)

**Tags**: cs.HC 



### RetClean: Retrieval-Based Data Cleaning Using Foundation Models and Data   Lakes
**Authors**: Zan Ahmad Naeem, Mohammad Shahmeer Ahmad, Mohamed Eltabakh, Mourad Ouzzani, Nan Tang

**Updated**: 2024-12-17T09:54:15Z

**Summary**: Can foundation models (such as ChatGPT) clean your data? In this proposal, we demonstrate that indeed ChatGPT can assist in data cleaning by suggesting corrections for specific cells in a data table (scenario 1). However, ChatGPT may struggle with datasets it has never encountered before (e.g., local enterprise data) or when the user requires an explanation of the source of the suggested clean values. To address these issues, we developed a retrieval-based method that complements ChatGPT's power with a user-provided data lake. The data lake is first indexed, we then retrieve the top-k relevant tuples to the user's query tuple and finally leverage ChatGPT to infer the correct value (scenario 2). Nevertheless, sharing enterprise data with ChatGPT, an externally hosted model, might not be feasible for privacy reasons. To assist with this scenario, we developed a custom RoBERTa-based foundation model that can be locally deployed. By fine-tuning it on a small number of examples, it can effectively make value inferences based on the retrieved tuples (scenario 3). Our proposed system, RetClean, seamlessly supports all three scenarios and provides a user-friendly GUI that enables the VLDB audience to explore and experiment with the system.

**Link**: [arxiv](http://arxiv.org/abs/2303.16909v2),  [pdf](http://arxiv.org/pdf/2303.16909v2)

**Tags**: cs.DB cs.AI 



### WIKIGENBENCH: Exploring Full-length Wikipedia Generation under   Real-World Scenario
**Authors**: Jiebin Zhang, Eugene J. Yu, Qinyu Chen, Chenhao Xiong, Dawei Zhu, Han Qian, Mingbo Song, Weimin Xiong, Xiaoguang Li, Qun Liu, Sujian Li

**Updated**: 2024-12-17T09:53:41Z

**Summary**: It presents significant challenges to generate comprehensive and accurate Wikipedia articles for newly emerging events under a real-world scenario. Existing attempts fall short either by focusing only on short snippets or by using metrics that are insufficient to evaluate real-world scenarios. In this paper, we construct WIKIGENBENCH, a new benchmark consisting of 1,320 entries, designed to align with real-world scenarios in both generation and evaluation. For generation, we explore a real-world scenario where structured, full-length Wikipedia articles with citations are generated for new events using input documents from web sources. For evaluation, we integrate systematic metrics and LLM-based metrics to assess the verifiability, organization, and other aspects aligned with real-world scenarios. Based on this benchmark, we conduct extensive experiments using various models within three commonly used frameworks: direct RAG, hierarchical structure-based RAG, and RAG with a fine-tuned generation model. Experimental results show that hierarchical-based methods can generate more comprehensive content, while fine-tuned methods achieve better verifiability. However, even the best methods still show a significant gap compared to existing Wikipedia content, indicating that further research is necessary.

**Link**: [arxiv](http://arxiv.org/abs/2402.18264v2),  [pdf](http://arxiv.org/pdf/2402.18264v2)

**Tags**: cs.CL 



### VisualRWKV: Exploring Recurrent Neural Networks for Visual Language   Models
**Authors**: Haowen Hou, Peigen Zeng, Fei Ma, Fei Richard Yu

**Updated**: 2024-12-17T09:46:19Z

**Summary**: Visual Language Models (VLMs) have rapidly progressed with the recent success of large language models. However, there have been few attempts to incorporate efficient linear Recurrent Neural Networks (RNNs) architectures into VLMs. In this study, we introduce VisualRWKV, the first application of a linear RNN model to multimodal learning tasks, leveraging the pre-trained RWKV language model. We propose a data-dependent recurrence and sandwich prompts to enhance our modeling capabilities, along with a 2D image scanning mechanism to enrich the processing of visual sequences. Extensive experiments demonstrate that VisualRWKV achieves competitive performance compared to Transformer-based models like LLaVA-1.5 on various benchmarks. Compared to LLaVA-1.5, VisualRWKV has a speed advantage of 3.98 times and can save 54% of GPU memory when reaching an inference length of 24K tokens. To facilitate further research and analysis, we have made the checkpoints and the associated code publicly accessible at the following GitHub repository: see https://github.com/howard-hou/VisualRWKV.

**Link**: [arxiv](http://arxiv.org/abs/2406.13362v2),  [pdf](http://arxiv.org/pdf/2406.13362v2)

**Tags**: cs.CV cs.CL cs.LG 



### TSD-SR: One-Step Diffusion with Target Score Distillation for Real-World   Image Super-Resolution
**Authors**: Linwei Dong, Qingnan Fan, Yihong Guo, Zhonghao Wang, Qi Zhang, Jinwei Chen, Yawei Luo, Changqing Zou

**Updated**: 2024-12-17T09:34:49Z

**Summary**: Pre-trained text-to-image diffusion models are increasingly applied to real-world image super-resolution (Real-ISR) task. Given the iterative refinement nature of diffusion models, most existing approaches are computationally expensive. While methods such as SinSR and OSEDiff have emerged to condense inference steps via distillation, their performance in image restoration or details recovery is not satisfied. To address this, we propose TSD-SR, a novel distillation framework specifically designed for real-world image super-resolution, aiming to construct an efficient and effective one-step model. We first introduce the Target Score Distillation, which leverages the priors of diffusion models and real image references to achieve more realistic image restoration. Secondly, we propose a Distribution-Aware Sampling Module to make detail-oriented gradients more readily accessible, addressing the challenge of recovering fine details. Extensive experiments demonstrate that our TSD-SR has superior restoration results (most of the metrics perform the best) and the fastest inference speed (e.g. 40 times faster than SeeSR) compared to the past Real-ISR approaches based on pre-trained diffusion priors.

**Link**: [arxiv](http://arxiv.org/abs/2411.18263v2),  [pdf](http://arxiv.org/pdf/2411.18263v2)

**Tags**: cs.CV 



### ASAP: Advancing Semantic Alignment Promotes Multi-Modal Manipulation   Detecting and Grounding
**Authors**: Zhenxing Zhang, Yaxiong Wang, Lechao Cheng, Zhun Zhong, Dan Guo, Meng Wang

**Updated**: 2024-12-17T09:33:06Z

**Summary**: We present ASAP, a new framework for detecting and grounding multi-modal media manipulation (DGM4).Upon thorough examination, we observe that accurate fine-grained cross-modal semantic alignment between the image and text is vital for accurately manipulation detection and grounding. While existing DGM4 methods pay rare attention to the cross-modal alignment, hampering the accuracy of manipulation detecting to step further. To remedy this issue, this work targets to advance the semantic alignment learning to promote this task. Particularly, we utilize the off-the-shelf Multimodal Large-Language Models (MLLMs) and Large Language Models (LLMs) to construct paired image-text pairs, especially for the manipulated instances. Subsequently, a cross-modal alignment learning is performed to enhance the semantic alignment. Besides the explicit auxiliary clues, we further design a Manipulation-Guided Cross Attention (MGCA) to provide implicit guidance for augmenting the manipulation perceiving. With the grounding truth available during training, MGCA encourages the model to concentrate more on manipulated components while downplaying normal ones, enhancing the model's ability to capture manipulations. Extensive experiments are conducted on the DGM4 dataset, the results demonstrate that our model can surpass the comparison method with a clear margin.

**Link**: [arxiv](http://arxiv.org/abs/2412.12718v1),  [pdf](http://arxiv.org/pdf/2412.12718v1)

**Tags**: cs.CV cs.MM Multimedia 



### No More Adam: Learning Rate Scaling at Initialization is All You Need
**Authors**: Minghao Xu, Lichuan Xiang, Xu Cai, Hongkai Wen

**Updated**: 2024-12-17T09:30:44Z

**Summary**: In this work, we question the necessity of adaptive gradient methods for training deep neural networks. SGD-SaI is a simple yet effective enhancement to stochastic gradient descent with momentum (SGDM). SGD-SaI performs learning rate Scaling at Initialization (SaI) to distinct parameter groups, guided by their respective gradient signal-to-noise ratios (g-SNR). By adjusting learning rates without relying on adaptive second-order momentum, SGD-SaI helps prevent training imbalances from the very first iteration and cuts the optimizer's memory usage by half compared to AdamW. Despite its simplicity and efficiency, SGD-SaI consistently matches or outperforms AdamW in training a variety of Transformer-based tasks, effectively overcoming a long-standing challenge of using SGD for training Transformers. SGD-SaI excels in ImageNet-1K classification with Vision Transformers(ViT) and GPT-2 pretraining for large language models (LLMs, transformer decoder-only), demonstrating robustness to hyperparameter variations and practicality for diverse applications. We further tested its robustness on tasks like LoRA fine-tuning for LLMs and diffusion models, where it consistently outperforms state-of-the-art optimizers. From a memory efficiency perspective, SGD-SaI achieves substantial memory savings for optimizer states, reducing memory usage by 5.93 GB for GPT-2 (1.5B parameters) and 25.15 GB for Llama2-7B compared to AdamW in full-precision training settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.11768v2),  [pdf](http://arxiv.org/pdf/2412.11768v2)

**Tags**: cs.LG cs.AI 



### Enhancing Naturalness in LLM-Generated Utterances through Disfluency   Insertion
**Authors**: Syed Zohaib Hassan, Pierre Lison, Pål Halvorsen

**Updated**: 2024-12-17T09:25:44Z

**Summary**: Disfluencies are a natural feature of spontaneous human speech but are typically absent from the outputs of Large Language Models (LLMs). This absence can diminish the perceived naturalness of synthesized speech, which is an important criteria when building conversational agents that aim to mimick human behaviours. We show how the insertion of disfluencies can alleviate this shortcoming. The proposed approach involves (1) fine-tuning an LLM with Low-Rank Adaptation (LoRA) to incorporate various types of disfluencies into LLM-generated utterances and (2) synthesizing those utterances using a text-to-speech model that supports the generation of speech phenomena such as disfluencies. We evaluated the quality of the generated speech across two metrics: intelligibility and perceived spontaneity. We demonstrate through a user study that the insertion of disfluencies significantly increase the perceived spontaneity of the generated speech. This increase came, however, along with a slight reduction in intelligibility.

**Link**: [arxiv](http://arxiv.org/abs/2412.12710v1),  [pdf](http://arxiv.org/pdf/2412.12710v1)

**Tags**: cs.CL 



### More Tokens, Lower Precision: Towards the Optimal Token-Precision   Trade-off in KV Cache Compression
**Authors**: Jiebin Zhang, Dawei Zhu, Yifan Song, Wenhao Wu, Chuqiao Kuang, Xiaoguang Li, Lifeng Shang, Qun Liu, Sujian Li

**Updated**: 2024-12-17T09:20:31Z

**Summary**: As large language models (LLMs) process increasing context windows, the memory usage of KV cache has become a critical bottleneck during inference. The mainstream KV compression methods, including KV pruning and KV quantization, primarily focus on either token or precision dimension and seldom explore the efficiency of their combination. In this paper, we comprehensively investigate the token-precision trade-off in KV cache compression. Experiments demonstrate that storing more tokens in the KV cache with lower precision, i.e., quantized pruning, can significantly enhance the long-context performance of LLMs. Furthermore, in-depth analysis regarding token-precision trade-off from a series of key aspects exhibit that, quantized pruning achieves substantial improvements in retrieval-related tasks and consistently performs well across varying input lengths. Moreover, quantized pruning demonstrates notable stability across different KV pruning methods, quantization strategies, and model scales. These findings provide valuable insights into the token-precision trade-off in KV cache compression. We plan to release our code in the near future.

**Link**: [arxiv](http://arxiv.org/abs/2412.12706v1),  [pdf](http://arxiv.org/pdf/2412.12706v1)

**Tags**: cs.CL 



### Trigger$^3$: Refining Query Correction via Adaptive Model Selector
**Authors**: Kepu Zhang, Zhongxiang Sun, Xiao Zhang, Xiaoxue Zang, Kai Zheng, Yang Song, Jun Xu

**Updated**: 2024-12-17T09:16:54Z

**Summary**: In search scenarios, user experience can be hindered by erroneous queries due to typos, voice errors, or knowledge gaps. Therefore, query correction is crucial for search engines. Current correction models, usually small models trained on specific data, often struggle with queries beyond their training scope or those requiring contextual understanding. While the advent of Large Language Models (LLMs) offers a potential solution, they are still limited by their pre-training data and inference cost, particularly for complex queries, making them not always effective for query correction. To tackle these, we propose Trigger$^3$, a large-small model collaboration framework that integrates the traditional correction model and LLM for query correction, capable of adaptively choosing the appropriate correction method based on the query and the correction results from the traditional correction model and LLM. Trigger$^3$ first employs a correction trigger to filter out correct queries. Incorrect queries are then corrected by the traditional correction model. If this fails, an LLM trigger is activated to call the LLM for correction. Finally, for queries that no model can correct, a fallback trigger decides to return the original query. Extensive experiments demonstrate Trigger$^3$ outperforms correction baselines while maintaining efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12701v1),  [pdf](http://arxiv.org/pdf/2412.12701v1)

**Tags**: cs.CL 



### FiRST: Finetuning Router-Selective Transformers for Input-Adaptive   Latency Reduction
**Authors**: Akriti Jain, Saransh Sharma, Koyel Mukherjee, Soumyabrata Pal

**Updated**: 2024-12-17T09:11:47Z

**Summary**: Auto-regressive Large Language Models (LLMs) demonstrate remarkable performance across different domains such as vision and language processing. However, due to sequential processing through a stack of transformer layers, autoregressive decoding faces significant computation/latency challenges, particularly in resource-constrained environments like mobile and edge devices. Existing approaches in literature that aim to improve latency via skipping layers have two distinct flavors - 1) Early exit, and 2) Input-agnostic heuristics where tokens exit at pre-determined layers irrespective of input sequence. Both the above strategies have limitations - the former cannot be applied to handle KV Caching necessary for speed-ups in modern framework and the latter does not capture the variation in layer importance across tasks or more generally, across input sequences. To address both limitations, we propose FiRST, an algorithm that reduces inference latency by using layer-specific routers to select a subset of transformer layers adaptively for each input sequence - the prompt (during the prefill stage) decides which layers will be skipped during decoding. FiRST preserves compatibility with KV caching enabling faster inference while being quality-aware. FiRST is model-agnostic and can be easily enabled on any pre-trained LLM. Our approach reveals that input adaptivity is critical - indeed, different task-specific middle layers play a crucial role in evolving hidden representations depending on tasks. Extensive experiments show that FiRST significantly reduces latency while outperforming other layer selection strategies in quality metics. It retains competitive performance to base model (without layer skipping) and in some cases, even improves upon it. FiRST is thus a promising and efficient solution for LLM deployment in low-resource environments.

**Link**: [arxiv](http://arxiv.org/abs/2410.12513v2),  [pdf](http://arxiv.org/pdf/2410.12513v2)

**Tags**: cs.CL 



### UniEntrezDB: Large-scale Gene Ontology Annotation Dataset and Evaluation   Benchmarks with Unified Entrez Gene Identifiers
**Authors**: Yuwei Miao, Yuzhi Guo, Hehuan Ma, Jingquan Yan, Feng Jiang, Weizhi An, Jean Gao, Junzhou Huang

**Updated**: 2024-12-17T09:08:52Z

**Summary**: Gene studies are crucial for fields such as protein structure prediction, drug discovery, and cancer genomics, yet they face challenges in fully utilizing the vast and diverse information available. Gene studies require clean, factual datasets to ensure reliable results. Ontology graphs, neatly organized domain terminology graphs, provide ideal sources for domain facts. However, available gene ontology annotations are currently distributed across various databases without unified identifiers for genes and gene products. To address these challenges, we introduce Unified Entrez Gene Identifier Dataset and Benchmarks (UniEntrezDB), the first systematic effort to unify large-scale public Gene Ontology Annotations (GOA) from various databases using unique gene identifiers. UniEntrezDB includes a pre-training dataset and four downstream tasks designed to comprehensively evaluate gene embedding performance from gene, protein, and cell levels, ultimately enhancing the reliability and applicability of LLMs in gene research and other professional settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12688v1),  [pdf](http://arxiv.org/pdf/2412.12688v1)

**Tags**: cs.DB 



## Keyword: LLM Deployment 
 ### SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM   Agents
**Authors**: Sheng Yin, Xianghe Pang, Yuanzhuo Ding, Menglan Chen, Yutong Bi, Yichen Xiong, Wenhao Huang, Zhen Xiang, Jing Shao, Siheng Chen

**Updated**: 2024-12-17T18:55:58Z

**Summary**: With the integration of large language models (LLMs), embodied agents have strong capabilities to execute complicated instructions in natural language, paving a way for the potential deployment of embodied robots. However, a foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in real world. To study this issue, we present SafeAgentBench -- a new benchmark for safety-aware task planning of embodied LLM agents. SafeAgentBench includes: (1) a new dataset with 750 tasks, covering 10 potential hazards and 3 task types; (2) SafeAgentEnv, a universal embodied environment with a low-level controller, supporting multi-agent execution with 17 high-level actions for 8 state-of-the-art baselines; and (3) reliable evaluation methods from both execution and semantic perspectives. Experimental results show that the best-performing baseline gets 69% success rate for safe tasks, but only 5% rejection rate for hazardous tasks, indicating significant safety risks. More details and codes are available at https://github.com/shengyin1224/SafeAgentBench.

**Link**: [arxiv](http://arxiv.org/abs/2412.13178v1),  [pdf](http://arxiv.org/pdf/2412.13178v1)

**Tags**: cs.CR cs.AI cs.RO 



### DataEnvGym: Data Generation Agents in Teacher Environments with Student   Feedback
**Authors**: Zaid Khan, Elias Stengel-Eskin, Jaemin Cho, Mohit Bansal

**Updated**: 2024-12-17T18:54:45Z

**Summary**: The process of creating training data to teach models is currently driven by humans, who manually analyze model weaknesses and plan how to create data that improves a student model. Approaches using LLMs as annotators reduce human effort, but still require humans to interpret feedback from evaluations and control the LLM to produce data the student needs. Automating this labor-intensive process by creating autonomous data generation agents - or teachers - is desirable, but requires environments that can simulate the feedback-driven, iterative, closed loop of data creation. To enable rapid, scalable testing for such agents and their modules, we introduce DataEnvGym, a testbed of teacher environments for data generation agents. DataEnvGym frames data generation as a sequential decision-making task, involving an agent consisting of a data generation policy (which generates a plan for creating training data) and a data generation engine (which transforms the plan into data), inside an environment that provides student feedback. The agent's goal is to improve student performance. Students are iteratively trained and evaluated on generated data, and their feedback (in the form of errors or weak skills) is reported to the agent after each iteration. DataEnvGym includes multiple teacher environment instantiations across 3 levels of structure in the state representation and action space. More structured environments are based on inferred skills and offer more interpretability and curriculum control. We support 4 domains (math, code, VQA, and tool-use) and test multiple students and teachers. Example agents in our teaching environments can iteratively improve students across tasks and settings. Moreover, we show that environments teach different skill levels and test variants of key modules, pointing to future work in improving data generation agents, engines, and feedback mechanisms.

**Link**: [arxiv](http://arxiv.org/abs/2410.06215v2),  [pdf](http://arxiv.org/pdf/2410.06215v2)

**Tags**: cs.CL cs.AI cs.LG 



### DnDScore: Decontextualization and Decomposition for Factuality   Verification in Long-Form Text Generation
**Authors**: Miriam Wanner, Benjamin Van Durme, Mark Dredze

**Updated**: 2024-12-17T18:54:01Z

**Summary**: The decompose-then-verify strategy for verification of Large Language Model (LLM) generations decomposes claims that are then independently verified. Decontextualization augments text (claims) to ensure it can be verified outside of the original context, enabling reliable verification. While decomposition and decontextualization have been explored independently, their interactions in a complete system have not been investigated. Their conflicting purposes can create tensions: decomposition isolates atomic facts while decontextualization inserts relevant information. Furthermore, a decontextualized subclaim presents a challenge to the verification step: what part of the augmented text should be verified as it now contains multiple atomic facts? We conduct an evaluation of different decomposition, decontextualization, and verification strategies and find that the choice of strategy matters in the resulting factuality scores. Additionally, we introduce DnDScore, a decontextualization aware verification method which validates subclaims in the context of contextual information.

**Link**: [arxiv](http://arxiv.org/abs/2412.13175v1),  [pdf](http://arxiv.org/pdf/2412.13175v1)

**Tags**: cs.CL 



### Algorithmic Fidelity of Large Language Models in Generating Synthetic   German Public Opinions: A Case Study
**Authors**: Bolei Ma, Berk Yoztyurk, Anna-Carolina Haensch, Xinpeng Wang, Markus Herklotz, Frauke Kreuter, Barbara Plank, Matthias Assenmacher

**Updated**: 2024-12-17T18:46:32Z

**Summary**: In recent research, large language models (LLMs) have been increasingly used to investigate public opinions. This study investigates the algorithmic fidelity of LLMs, i.e., the ability to replicate the socio-cultural context and nuanced opinions of human participants. Using open-ended survey data from the German Longitudinal Election Studies (GLES), we prompt different LLMs to generate synthetic public opinions reflective of German subpopulations by incorporating demographic features into the persona prompts. Our results show that Llama performs better than other LLMs at representing subpopulations, particularly when there is lower opinion diversity within those groups. Our findings further reveal that the LLM performs better for supporters of left-leaning parties like The Greens and The Left compared to other parties, and matches the least with the right-party AfD. Additionally, the inclusion or exclusion of specific variables in the prompts can significantly impact the models' predictions. These findings underscore the importance of aligning LLMs to more effectively model diverse public opinions while minimizing political biases and enhancing robustness in representativeness.

**Link**: [arxiv](http://arxiv.org/abs/2412.13169v1),  [pdf](http://arxiv.org/pdf/2412.13169v1)

**Tags**: cs.CL 



### C-FedRAG: A Confidential Federated Retrieval-Augmented Generation System
**Authors**: Parker Addison, Minh-Tuan H. Nguyen, Tomislav Medan, Mohammad T. Manzari, Brendan McElrone, Laksh Lalwani, Aboli More, Smita Sharma, Holger R. Roth, Isaac Yang, Chester Chen, Daguang Xu, Yan Cheng, Andrew Feng, Ziyue Xu

**Updated**: 2024-12-17T18:42:21Z

**Summary**: Organizations seeking to utilize Large Language Models (LLMs) for knowledge querying and analysis often encounter challenges in maintaining an LLM fine-tuned on targeted, up-to-date information that keeps answers relevant and grounded. Retrieval Augmented Generation (RAG) has quickly become a feasible solution for organizations looking to overcome the challenges of maintaining proprietary models and to help reduce LLM hallucinations in their query responses. However, RAG comes with its own issues regarding scaling data pipelines across tiered-access and disparate data sources. In many scenarios, it is necessary to query beyond a single data silo to provide richer and more relevant context for an LLM. Analyzing data sources within and across organizational trust boundaries is often limited by complex data-sharing policies that prohibit centralized data storage, therefore, inhibit the fast and effective setup and scaling of RAG solutions. In this paper, we introduce Confidential Computing (CC) techniques as a solution for secure Federated Retrieval Augmented Generation (FedRAG). Our proposed Confidential FedRAG system (C-FedRAG) enables secure connection and scaling of a RAG workflows across a decentralized network of data providers by ensuring context confidentiality. We also demonstrate how to implement a C-FedRAG system using the NVIDIA FLARE SDK and assess its performance using the MedRAG toolkit and MIRAGE benchmarking dataset.

**Link**: [arxiv](http://arxiv.org/abs/2412.13163v1),  [pdf](http://arxiv.org/pdf/2412.13163v1)

**Tags**: cs.DC cs.IR 



### Let's Get to the Point: LLM-Supported Planning, Drafting, and Revising   of Research-Paper Blog Posts
**Authors**: Marissa Radensky, Daniel S. Weld, Joseph Chee Chang, Pao Siangliulue, Jonathan Bragg

**Updated**: 2024-12-17T18:35:27Z

**Summary**: Research-paper blog posts help scientists to disseminate their work to a larger audience, but translating scientific long documents into long-form summaries like blog posts raises unique challenges: 1) planning what paper content to include in the blog post, 2) drafting the selected content in sections amenable to a paper blog post, and 3) revising the blog post to be scientifically accurate but also concise, easy to understand, and engaging. Can we harness the power of large language models (LLMs) to assist researchers with these challenges? To investigate this question, we developed Papers-to-Posts, an LLM-powered tool that implements a new Plan-Draft-Revise workflow for mixed-initiative long-form paper summarization. An LLM-generated paper outline with pre-selected yet adjustable bullet points helps users to plan what information to include. Meanwhile, customizable LLM instructions support drafting the text with a suitable structure and revising the text to have an appropriate tone. Through two studies, we compared Papers-to-Posts to a strong baseline tool that provides an LLM-generated draft and access to free-form LLM prompting, and we found that Papers-to-Posts improved researchers' editing power. In a within-subjects lab study (N=20 participants), Papers-to-Posts led participants to make significantly more change to initial LLM drafts within a fixed amount of time and to be significantly more satisfied with their final blog post, without increasing cognitive load. Furthermore, in a between-subjects deployment study (N=37 blog posts, 26 participants), Papers-to-Posts led participants to make more change to initial LLM drafts within a given amount of time as well as writing actions, without decreasing satisfaction with the final blog posts or increasing cognitive load.

**Link**: [arxiv](http://arxiv.org/abs/2406.10370v2),  [pdf](http://arxiv.org/pdf/2406.10370v2)

**Tags**: cs.HC 



### SWAN: Preprocessing SGD Enables Adam-Level Performance On LLM Training   With Significant Memory Reduction
**Authors**: Chao Ma, Wenbo Gong, Meyer Scetbon, Edward Meeds

**Updated**: 2024-12-17T18:13:18Z

**Summary**: Adaptive optimizers such as Adam (Kingma & Ba, 2015) have been central to the success of large language models. However, they maintain additional moving average states throughout training, which results in memory requirements several times greater than the model. This overhead imposes constraints on scalability and computational efficiency. On the other hand, while stochastic gradient descent (SGD) is optimal in terms of memory efficiency, their capability in LLM training is limited (Zhao et al., 2024b).   To address this dilemma, we show that pre-processing SGD is sufficient to reach Adam-level performance on LLMs. Specifically, we propose to preprocess the instantaneous stochastic gradients with two simple operators: $\mathtt{GradNorm}$ and $\mathtt{GradWhitening}$. $\mathtt{GradNorm}$ stabilizes gradient distributions, and $\mathtt{GradWhitening}$ counteracts the local curvature of the loss landscape, respectively. This results in SWAN (SGD with Whitening And Normalization), a stochastic optimizer that eliminates the need to store any accumulative state variables. Empirically, SWAN has the same memory footprint as SGD, achieving $\approx 50\%$ reduction on total end-to-end memory compared to Adam. In language modeling tasks, SWAN demonstrates the same or even a substantial improvement over Adam. Specifically, when pre-training the LLaMa model with 350M and 1.3B parameters, SWAN achieves a 2x speedup by reaching the same evaluation perplexity in less than half tokens seen.

**Link**: [arxiv](http://arxiv.org/abs/2412.13148v1),  [pdf](http://arxiv.org/pdf/2412.13148v1)

**Tags**: cs.LG cs.AI 



### Are Your LLMs Capable of Stable Reasoning?
**Authors**: Junnan Liu, Hongwei Liu, Linchen Xiao, Ziyi Wang, Kuikun Liu, Songyang Gao, Wenwei Zhang, Songyang Zhang, Kai Chen

**Updated**: 2024-12-17T18:12:47Z

**Summary**: The rapid advancement of Large Language Models (LLMs) has demonstrated remarkable progress in complex reasoning tasks. However, a significant discrepancy persists between benchmark performances and real-world applications. We identify this gap as primarily stemming from current evaluation protocols and metrics, which inadequately capture the full spectrum of LLM capabilities, particularly in complex reasoning tasks where both accuracy and consistency are crucial. This work makes two key contributions. First, we introduce G-Pass@k, a novel evaluation metric that provides a continuous assessment of model performance across multiple sampling attempts, quantifying both the model's peak performance potential and its stability. Second, we present LiveMathBench, a dynamic benchmark comprising challenging, contemporary mathematical problems designed to minimize data leakage risks during evaluation. Through extensive experiments using G-Pass@k on state-of-the-art LLMs with LiveMathBench, we provide comprehensive insights into both their maximum capabilities and operational consistency. Our findings reveal substantial room for improvement in LLMs' "realistic" reasoning capabilities, highlighting the need for more robust evaluation methods. The benchmark and detailed results are available at: https://github.com/open-compass/GPassK.

**Link**: [arxiv](http://arxiv.org/abs/2412.13147v1),  [pdf](http://arxiv.org/pdf/2412.13147v1)

**Tags**: cs.AI cs.CL 



### Reinforcement Learning Enhanced LLMs: A Survey
**Authors**: Shuhe Wang, Shengyu Zhang, Jie Zhang, Runyi Hu, Xiaoya Li, Tianwei Zhang, Jiwei Li, Fei Wu, Guoyin Wang, Eduard Hovy

**Updated**: 2024-12-17T18:05:11Z

**Summary**: This paper surveys research in the rapidly growing field of enhancing large language models (LLMs) with reinforcement learning (RL), a technique that enables LLMs to improve their performance by receiving feedback in the form of rewards based on the quality of their outputs, allowing them to generate more accurate, coherent, and contextually appropriate responses. In this work, we make a systematic review of the most up-to-date state of knowledge on RL-enhanced LLMs, attempting to consolidate and analyze the rapidly growing research in this field, helping researchers understand the current challenges and advancements. Specifically, we (1) detail the basics of RL; (2) introduce popular RL-enhanced LLMs; (3) review researches on two widely-used reward model-based RL techniques: Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAIF); and (4) explore Direct Preference Optimization (DPO), a set of methods that bypass the reward model to directly use human preference data for aligning LLM outputs with human expectations. We will also point out current challenges and deficiencies of existing methods and suggest some avenues for further improvements. Project page of this work can be found at: \url{https://github.com/ShuheWang1998/Reinforcement-Learning-Enhanced-LLMs-A-Survey}.

**Link**: [arxiv](http://arxiv.org/abs/2412.10400v2),  [pdf](http://arxiv.org/pdf/2412.10400v2)

**Tags**: cs.CL cs.AI cs.LG 



### Alternate Preference Optimization for Unlearning Factual Knowledge in   Large Language Models
**Authors**: Anmol Mekala, Vineeth Dorna, Shreya Dubey, Abhishek Lalwani, David Koleczek, Mukund Rungta, Sadid Hasan, Elita Lobo

**Updated**: 2024-12-17T17:45:07Z

**Summary**: Machine unlearning aims to efficiently eliminate the influence of specific training data, known as the forget set, from the model. However, existing unlearning methods for Large Language Models (LLMs) face a critical challenge: they rely solely on negative feedback to suppress responses related to the forget set, which often results in nonsensical or inconsistent outputs, diminishing model utility and posing potential privacy risks. To address this limitation, we propose a novel approach called Alternate Preference Optimization (AltPO), which combines negative feedback with in-domain positive feedback on the forget set. Additionally, we introduce new evaluation metrics to assess the quality of responses related to the forget set. Extensive experiments show that our approach not only enables effective unlearning but also avoids undesirable model behaviors while maintaining overall model performance. Our implementation can be found at https://github.com/molereddy/Alternate-Preference-Optimization.

**Link**: [arxiv](http://arxiv.org/abs/2409.13474v3),  [pdf](http://arxiv.org/pdf/2409.13474v3)

**Tags**: cs.CL cs.LG 



### RISCORE: Enhancing In-Context Riddle Solving in Language Models through   Context-Reconstructed Example Augmentation
**Authors**: Ioannis Panagiotopoulos, Giorgos Filandrianos, Maria Lymperaiou, Giorgos Stamou

**Updated**: 2024-12-17T17:42:18Z

**Summary**: Riddle-solving requires advanced reasoning skills, pushing LLMs to engage in abstract thinking and creative problem-solving, often revealing limitations in their cognitive abilities. In this paper, we examine the riddle-solving capabilities of LLMs using a multiple-choice format, exploring how different prompting techniques impact performance on riddles that demand diverse reasoning skills. To enhance results, we introduce RISCORE (RIddle Solving with COntext REcontruciton) a novel fully automated prompting method that generates and utilizes contextually reconstructed sentence-based puzzles in conjunction with the original examples to create few-shot exemplars. Our experiments demonstrate that RISCORE significantly improves the performance of language models in both vertical and lateral thinking tasks, surpassing traditional exemplar selection strategies across a variety of few-shot settings.

**Link**: [arxiv](http://arxiv.org/abs/2409.16383v4),  [pdf](http://arxiv.org/pdf/2409.16383v4)

**Tags**: cs.CL 



### GPS-IDS: An Anomaly-based GPS Spoofing Attack Detection Framework for   Autonomous Vehicles
**Authors**: Murad Mehrab Abrar, Amal Youssef, Raian Islam, Shalaka Satam, Banafsheh Saber Latibari, Salim Hariri, Sicong Shao, Soheil Salehi, Pratik Satam

**Updated**: 2024-12-17T17:31:46Z

**Summary**: Autonomous Vehicles (AVs) heavily rely on sensors and communication networks like Global Positioning System (GPS) to navigate autonomously. Prior research has indicated that networks like GPS are vulnerable to cyber-attacks such as spoofing and jamming, thus posing serious risks like navigation errors and system failures. These threats are expected to intensify with the widespread deployment of AVs, making it crucial to detect and mitigate such attacks. This paper proposes GPS Intrusion Detection System, or GPS-IDS, an Anomaly-based intrusion detection framework to detect GPS spoofing attacks on AVs. The framework uses a novel physics-based vehicle behavior model where a GPS navigation model is integrated into the conventional dynamic bicycle model for accurate AV behavior representation. Temporal features derived from this behavior model are analyzed using machine learning to detect normal and abnormal navigation behaviors. The performance of the GPS-IDS framework is evaluated on the AV-GPS-Dataset -- a GPS security dataset for AVs comprising real-world data collected using an AV testbed, and simulated data representing urban traffic environments. To the best of our knowledge, this dataset is the first of its kind and has been publicly released for the global research community to address such security challenges.

**Link**: [arxiv](http://arxiv.org/abs/2405.08359v2),  [pdf](http://arxiv.org/pdf/2405.08359v2)

**Tags**: cs.CR cs.RO 



### Systematic Biases in LLM Simulations of Debates
**Authors**: Amir Taubenfeld, Yaniv Dover, Roi Reichart, Ariel Goldstein

**Updated**: 2024-12-17T17:17:21Z

**Summary**: The emergence of Large Language Models (LLMs), has opened exciting possibilities for constructing computational simulations designed to replicate human behavior accurately. Current research suggests that LLM-based agents become increasingly human-like in their performance, sparking interest in using these AI agents as substitutes for human participants in behavioral studies. However, LLMs are complex statistical learners without straightforward deductive rules, making them prone to unexpected behaviors. Hence, it is crucial to study and pinpoint the key behavioral distinctions between humans and LLM-based agents. In this study, we highlight the limitations of LLMs in simulating human interactions, particularly focusing on LLMs' ability to simulate political debates on topics that are important aspects of people's day-to-day lives and decision-making processes. Our findings indicate a tendency for LLM agents to conform to the model's inherent social biases despite being directed to debate from certain political perspectives. This tendency results in behavioral patterns that seem to deviate from well-established social dynamics among humans. We reinforce these observations using an automatic self-fine-tuning method, which enables us to manipulate the biases within the LLM and demonstrate that agents subsequently align with the altered biases. These results underscore the need for further research to develop methods that help agents overcome these biases, a critical step toward creating more realistic simulations.

**Link**: [arxiv](http://arxiv.org/abs/2402.04049v3),  [pdf](http://arxiv.org/pdf/2402.04049v3)

**Tags**: cs.CL cs.AI 



### AI PERSONA: Towards Life-long Personalization of LLMs
**Authors**: Tiannan Wang, Meiling Tao, Ruoyu Fang, Huilin Wang, Shuai Wang, Yuchen Eleanor Jiang, Wangchunshu Zhou

**Updated**: 2024-12-17T17:17:03Z

**Summary**: In this work, we introduce the task of life-long personalization of large language models. While recent mainstream efforts in the LLM community mainly focus on scaling data and compute for improved capabilities of LLMs, we argue that it is also very important to enable LLM systems, or language agents, to continuously adapt to the diverse and ever-changing profiles of every distinct user and provide up-to-date personalized assistance. We provide a clear task formulation and introduce a simple, general, effective, and scalable framework for life-long personalization of LLM systems and language agents. To facilitate future research on LLM personalization, we also introduce methods to synthesize realistic benchmarks and robust evaluation metrics. We will release all codes and data for building and benchmarking life-long personalized LLM systems.

**Link**: [arxiv](http://arxiv.org/abs/2412.13103v1),  [pdf](http://arxiv.org/pdf/2412.13103v1)

**Tags**: cs.CL cs.AI 



### AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark
**Authors**: Jianlyu Chen, Nan Wang, Chaofan Li, Bo Wang, Shitao Xiao, Han Xiao, Hao Liao, Defu Lian, Zheng Liu

**Updated**: 2024-12-17T17:15:21Z

**Summary**: Evaluation plays a crucial role in the advancement of information retrieval (IR) models. However, current benchmarks, which are based on predefined domains and human-labeled data, face limitations in addressing evaluation needs for emerging domains both cost-effectively and efficiently. To address this challenge, we propose the Automated Heterogeneous Information Retrieval Benchmark (AIR-Bench). AIR-Bench is distinguished by three key features: 1) Automated. The testing data in AIR-Bench is automatically generated by large language models (LLMs) without human intervention. 2) Heterogeneous. The testing data in AIR-Bench is generated with respect to diverse tasks, domains and languages. 3) Dynamic. The domains and languages covered by AIR-Bench are constantly augmented to provide an increasingly comprehensive evaluation benchmark for community developers. We develop a reliable and robust data generation pipeline to automatically create diverse and high-quality evaluation datasets based on real-world corpora. Our findings demonstrate that the generated testing data in AIR-Bench aligns well with human-labeled testing data, making AIR-Bench a dependable benchmark for evaluating IR models. The resources in AIR-Bench are publicly available at https://github.com/AIR-Bench/AIR-Bench.

**Link**: [arxiv](http://arxiv.org/abs/2412.13102v1),  [pdf](http://arxiv.org/pdf/2412.13102v1)

**Tags**: cs.IR cs.CL 



### Chatbots im Schulunterricht: Wir testen das Fobizz-Tool zur   automatischen Bewertung von Hausaufgaben
**Authors**: Rainer Muehlhoff, Marte Henningsen

**Updated**: 2024-12-17T17:06:01Z

**Summary**: [Study in German language.] This study examines the AI-powered grading tool "AI Grading Assistant" by the German company Fobizz, designed to support teachers in evaluating and providing feedback on student assignments. Against the societal backdrop of an overburdened education system and rising expectations for artificial intelligence as a solution to these challenges, the investigation evaluates the tool's functional suitability through two test series. The results reveal significant shortcomings: The tool's numerical grades and qualitative feedback are often random and do not improve even when its suggestions are incorporated. The highest ratings are achievable only with texts generated by ChatGPT. False claims and nonsensical submissions frequently go undetected, while the implementation of some grading criteria is unreliable and opaque. Since these deficiencies stem from the inherent limitations of large language models (LLMs), fundamental improvements to this or similar tools are not immediately foreseeable. The study critiques the broader trend of adopting AI as a quick fix for systemic problems in education, concluding that Fobizz's marketing of the tool as an objective and time-saving solution is misleading and irresponsible. Finally, the study calls for systematic evaluation and subject-specific pedagogical scrutiny of the use of AI tools in educational contexts.

**Link**: [arxiv](http://arxiv.org/abs/2412.06651v4),  [pdf](http://arxiv.org/pdf/2412.06651v4)

**Tags**: cs.CY cs.AI cs.CL cs.ET 97B10 



### LMUnit: Fine-grained Evaluation with Natural Language Unit Tests
**Authors**: Jon Saad-Falcon, Rajan Vivek, William Berrios, Nandita Shankar Naik, Matija Franklin, Bertie Vidgen, Amanpreet Singh, Douwe Kiela, Shikib Mehri

**Updated**: 2024-12-17T17:01:15Z

**Summary**: As language models become integral to critical workflows, assessing their behavior remains a fundamental challenge -- human evaluation is costly and noisy, while automated metrics provide only coarse, difficult-to-interpret signals. We introduce natural language unit tests, a paradigm that decomposes response quality into explicit, testable criteria, along with a unified scoring model, LMUnit, which combines multi-objective training across preferences, direct ratings, and natural language rationales. Through controlled human studies, we show this paradigm significantly improves inter-annotator agreement and enables more effective LLM development workflows. LMUnit achieves state-of-the-art performance on evaluation benchmarks (FLASK, BigGenBench) and competitive results on RewardBench. These results validate both our proposed paradigm and scoring model, suggesting a promising path forward for language model evaluation and development.

**Link**: [arxiv](http://arxiv.org/abs/2412.13091v1),  [pdf](http://arxiv.org/pdf/2412.13091v1)

**Tags**: cs.CL cs.AI 



### PersonaMark: Personalized LLM watermarking for model protection and user   attribution
**Authors**: Yuehan Zhang, Peizhuo Lv, Yinpeng Liu, Yongqiang Ma, Wei Lu, Xiaofeng Wang, Xiaozhong Liu, Jiawei Liu

**Updated**: 2024-12-17T16:52:12Z

**Summary**: The rapid advancement of customized Large Language Models (LLMs) offers considerable convenience. However, it also intensifies concerns regarding the protection of copyright/confidential information. With the extensive adoption of private LLMs, safeguarding model copyright and ensuring data privacy have become critical. Text watermarking has emerged as a viable solution for detecting AI-generated content and protecting models. However, existing methods fall short in providing individualized watermarks for each user, a critical feature for enhancing accountability and traceability. In this paper, we introduce PersonaMark, a novel personalized text watermarking scheme designed to protect LLMs' copyrights and bolster accountability. PersonaMark leverages sentence structure as a subtle carrier of watermark information and optimizes the generation process to maintain the natural output of the model. By employing a personalized hashing function, unique watermarks are embedded for each user, enabling high-quality text generation without compromising the model's performance. This approach is both time-efficient and scalable, capable of handling large numbers of users through a multi-user hashing mechanism. To the best of our knowledge, this is a pioneer study to explore personalized watermarking in LLMs. We conduct extensive evaluations across four LLMs, analyzing various metrics such as perplexity, sentiment, alignment, and readability. The results validate that PersonaMark preserves text quality, ensures unbiased watermark insertion, and offers robust watermark detection capabilities, all while maintaining the model's behavior with minimal disruption.

**Link**: [arxiv](http://arxiv.org/abs/2409.09739v2),  [pdf](http://arxiv.org/pdf/2409.09739v2)

**Tags**: cs.CR cs.CL 



### Rethinking the Alignment of Psychotherapy Dialogue Generation with   Motivational Interviewing Strategies
**Authors**: Xin Sun, Xiao Tang, Abdallah El Ali, Zhuying Li, Pengjie Ren, Jan de Wit, Jiahuan Pei, Jos A. Bosch

**Updated**: 2024-12-17T16:44:16Z

**Summary**: Recent advancements in large language models (LLMs) have shown promise in generating psychotherapeutic dialogues, particularly in the context of motivational interviewing (MI). However, the inherent lack of transparency in LLM outputs presents significant challenges given the sensitive nature of psychotherapy. Applying MI strategies, a set of MI skills, to generate more controllable therapeutic-adherent conversations with explainability provides a possible solution. In this work, we explore the alignment of LLMs with MI strategies by first prompting the LLMs to predict the appropriate strategies as reasoning and then utilizing these strategies to guide the subsequent dialogue generation. We seek to investigate whether such alignment leads to more controllable and explainable generations. Multiple experiments including automatic and human evaluations are conducted to validate the effectiveness of MI strategies in aligning psychotherapy dialogue generation. Our findings demonstrate the potential of LLMs in producing strategically aligned dialogues and suggest directions for practical applications in psychotherapeutic settings.

**Link**: [arxiv](http://arxiv.org/abs/2408.06527v2),  [pdf](http://arxiv.org/pdf/2408.06527v2)

**Tags**: cs.CL cs.AI 



### Causal Prompting: Debiasing Large Language Model Prompting based on   Front-Door Adjustment
**Authors**: Congzhi Zhang, Linhai Zhang, Jialong Wu, Yulan He, Deyu Zhou

**Updated**: 2024-12-17T16:10:26Z

**Summary**: Despite the notable advancements of existing prompting methods, such as In-Context Learning and Chain-of-Thought for Large Language Models (LLMs), they still face challenges related to various biases. Traditional debiasing methods primarily focus on the model training stage, including approaches based on data augmentation and reweighting, yet they struggle with the complex biases inherent in LLMs. To address such limitations, the causal relationship behind the prompting methods is uncovered using a structural causal model, and a novel causal prompting method based on front-door adjustment is proposed to effectively mitigate LLMs biases. In specific, causal intervention is achieved by designing the prompts without accessing the parameters and logits of LLMs. The chain-of-thought generated by LLM is employed as the mediator variable and the causal effect between input prompts and output answers is calculated through front-door adjustment to mitigate model biases. Moreover, to accurately represent the chain-of-thoughts and estimate the causal effects, contrastive learning is used to fine-tune the encoder of chain-of-thought by aligning its space with that of the LLM. Experimental results show that the proposed causal prompting approach achieves excellent performance across seven natural language processing datasets on both open-source and closed-source LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2403.02738v3),  [pdf](http://arxiv.org/pdf/2403.02738v3)

**Tags**: cs.CL 



### CNNSum: Exploring Long-Context Summarization with Large Language Models   in Chinese Novels
**Authors**: Lingxiao Wei, He Yan, Xiangju Lu, Junmin Zhu, Jun Wang, Wei Zhang

**Updated**: 2024-12-17T16:03:43Z

**Summary**: Large Language Models (LLMs) have been well-researched in various long-context tasks. However, the scarcity of high-quality long-context summarization datasets has hindered further advancements in this area. To address this, we introduce CNNSum, a multi-scale long-context summarization benchmark based on Chinese novels, featuring human-driven annotations, which comprises four subsets totaling 695 samples, with lengths ranging from 16k to 128k. We evaluate numerous LLMs and conduct detailed case analyses. Furthermore, we conduct extensive fine-tuning experiments to explore and improve long-context summarization. In our study: (1) Advanced LLMs like GPT-4o may still generate subjective commentary, leading to vague summaries. (2) Currently, long-context summarization mainly relies on memory ability afforded by longer context lengths. The advantages of Large LLMs are hard to utilize, thus small LLMs are the most cost-effective. (3) Different prompt templates paired with various version models may cause large performance gaps. In further fine-tuning, these can be mitigated, and the Base version models perform better. (4) LLMs with RoPE-base scaled exhibit strong extrapolation potential; using short-context data can significantly improve long-context summarization performance. However, further applying other interpolation methods requires careful selection. (5) CNNSum provides more reliable and insightful evaluation results than other benchmarks. We release CNNSum to advance future research in this field. https://github.com/CxsGhost/CNNSum

**Link**: [arxiv](http://arxiv.org/abs/2412.02819v4),  [pdf](http://arxiv.org/pdf/2412.02819v4)

**Tags**: cs.CL cs.AI 



### Unleashing the Power of Pre-trained Language Models for Offline   Reinforcement Learning
**Authors**: Ruizhe Shi, Yuyao Liu, Yanjie Ze, Simon S. Du, Huazhe Xu

**Updated**: 2024-12-17T15:59:44Z

**Summary**: Offline reinforcement learning (RL) aims to find a near-optimal policy using pre-collected datasets. In real-world scenarios, data collection could be costly and risky; therefore, offline RL becomes particularly challenging when the in-domain data is limited. Given recent advances in Large Language Models (LLMs) and their few-shot learning prowess, this paper introduces $\textbf{La}$nguage Models for $\textbf{Mo}$tion Control ($\textbf{LaMo}$), a general framework based on Decision Transformers to effectively use pre-trained Language Models (LMs) for offline RL. Our framework highlights four crucial components: (1) Initializing Decision Transformers with sequentially pre-trained LMs, (2) employing the LoRA fine-tuning method, in contrast to full-weight fine-tuning, to combine the pre-trained knowledge from LMs and in-domain knowledge effectively, (3) using the non-linear MLP transformation instead of linear projections, to generate embeddings, and (4) integrating an auxiliary language prediction loss during fine-tuning to stabilize the LMs and retain their original abilities on languages. Empirical results indicate $\textbf{LaMo}$ achieves excellent performance in sparse-reward tasks and closes the gap between value-based offline RL methods and decision transformers in dense-reward tasks. In particular, our method demonstrates superior performance in scenarios with limited data samples.

**Link**: [arxiv](http://arxiv.org/abs/2310.20587v5),  [pdf](http://arxiv.org/pdf/2310.20587v5)

**Tags**: cs.LG 



### WHAT-IF: Exploring Branching Narratives by Meta-Prompting Large Language   Models
**Authors**: Runsheng "Anson" Huang, Lara J. Martin, Chris Callison-Burch

**Updated**: 2024-12-17T15:56:50Z

**Summary**: WHAT-IF -- Writing a Hero's Alternate Timeline through Interactive Fiction -- is a system that uses zero-shot meta-prompting to create branching narratives from a prewritten story. Played as an interactive fiction (IF) game, WHAT-IF lets the player choose between decisions that the large language model (LLM) GPT-4 generates as possible branches in the story. Starting with an existing linear plot as input, a branch is created at each key decision taken by the main character. By meta-prompting the LLM to consider the major plot points from the story, the system produces coherent and well-structured alternate storylines. WHAT-IF stores the branching plot tree in a graph which helps it to both keep track of the story for prompting and maintain the structure for the final IF system. A video demo of our system can be found here: https://youtu.be/8vBqjqtupcc.

**Link**: [arxiv](http://arxiv.org/abs/2412.10582v2),  [pdf](http://arxiv.org/pdf/2412.10582v2)

**Tags**: cs.CL 



### Relational Neurosymbolic Markov Models
**Authors**: Lennert De Smet, Gabriele Venturato, Luc De Raedt, Giuseppe Marra

**Updated**: 2024-12-17T15:41:51Z

**Summary**: Sequential problems are ubiquitous in AI, such as in reinforcement learning or natural language processing. State-of-the-art deep sequential models, like transformers, excel in these settings but fail to guarantee the satisfaction of constraints necessary for trustworthy deployment. In contrast, neurosymbolic AI (NeSy) provides a sound formalism to enforce constraints in deep probabilistic models but scales exponentially on sequential problems. To overcome these limitations, we introduce relational neurosymbolic Markov models (NeSy-MMs), a new class of end-to-end differentiable sequential models that integrate and provably satisfy relational logical constraints. We propose a strategy for inference and learning that scales on sequential settings, and that combines approximate Bayesian inference, automated reasoning, and gradient estimation. Our experiments show that NeSy-MMs can solve problems beyond the current state-of-the-art in neurosymbolic AI and still provide strong guarantees with respect to desired properties. Moreover, we show that our models are more interpretable and that constraints can be adapted at test time to out-of-distribution scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2412.13023v1),  [pdf](http://arxiv.org/pdf/2412.13023v1)

**Tags**: cs.AI cs.LG 



### Queries, Representation & Detection: The Next 100 Model Fingerprinting   Schemes
**Authors**: Augustin Godinot, Erwan Le Merrer, Camilla Penzo, François Taïani, Gilles Trédan

**Updated**: 2024-12-17T15:41:36Z

**Summary**: The deployment of machine learning models in operational contexts represents a significant investment for any organisation. Consequently, the risk of these models being misappropriated by competitors needs to be addressed. In recent years, numerous proposals have been put forth to detect instances of model stealing. However, these proposals operate under implicit and disparate data and model access assumptions; as a consequence, it remains unclear how they can be effectively compared to one another. Our evaluation shows that a simple baseline that we introduce performs on par with existing state-of-the-art fingerprints, which, on the other hand, are much more complex. To uncover the reasons behind this intriguing result, this paper introduces a systematic approach to both the creation of model fingerprinting schemes and their evaluation benchmarks. By dividing model fingerprinting into three core components -- Query, Representation and Detection (QuRD) -- we are able to identify $\sim100$ previously unexplored QuRD combinations and gain insights into their performance. Finally, we introduce a set of metrics to compare and guide the creation of more representative model stealing detection benchmarks. Our approach reveals the need for more challenging benchmarks and a sound comparison with baselines. To foster the creation of new fingerprinting schemes and benchmarks, we open-source our fingerprinting toolbox.

**Link**: [arxiv](http://arxiv.org/abs/2412.13021v1),  [pdf](http://arxiv.org/pdf/2412.13021v1)

**Tags**: cs.LG cs.CR 



### OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in   Financial Domain
**Authors**: Shuting Wang, Jiejun Tan, Zhicheng Dou, Ji-Rong Wen

**Updated**: 2024-12-17T15:38:42Z

**Summary**: As a typical and practical application of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) techniques have gained extensive attention, particularly in vertical domains where LLMs may lack domain-specific knowledge. In this paper, we introduce an omnidirectional and automatic RAG benchmark, OmniEval, in the financial domain. Our benchmark is characterized by its multi-dimensional evaluation framework, including (1) a matrix-based RAG scenario evaluation system that categorizes queries into five task classes and 16 financial topics, leading to a structured assessment of diverse query scenarios; (2) a multi-dimensional evaluation data generation approach, which combines GPT-4-based automatic generation and human annotation, achieving an 87.47\% acceptance ratio in human evaluations on generated instances; (3) a multi-stage evaluation system that evaluates both retrieval and generation performance, result in a comprehensive evaluation on the RAG pipeline; and (4) robust evaluation metrics derived from rule-based and LLM-based ones, enhancing the reliability of assessments through manual annotations and supervised fine-tuning of an LLM evaluator. Our experiments demonstrate the comprehensiveness of OmniEval, which includes extensive test datasets and highlights the performance variations of RAG systems across diverse topics and tasks, revealing significant opportunities for RAG models to improve their capabilities in vertical domains. We open source the code of our benchmark in \href{https://github.com/RUC-NLPIR/OmniEval}{https://github.com/RUC-NLPIR/OmniEval}.

**Link**: [arxiv](http://arxiv.org/abs/2412.13018v1),  [pdf](http://arxiv.org/pdf/2412.13018v1)

**Tags**: cs.CL 



### Towards Reliable Latent Knowledge Estimation in LLMs: Zero-Prompt   Many-Shot Based Factual Knowledge Extraction
**Authors**: Qinyuan Wu, Mohammad Aflah Khan, Soumi Das, Vedant Nanda, Bishwamittra Ghosh, Camila Kolling, Till Speicher, Laurent Bindschaedler, Krishna P. Gummadi, Evimaria Terzi

**Updated**: 2024-12-17T15:38:23Z

**Summary**: In this paper, we focus on the challenging task of reliably estimating factual knowledge that is embedded inside large language models (LLMs). To avoid reliability concerns with prior approaches, we propose to eliminate prompt engineering when probing LLMs for factual knowledge. Our approach, called Zero-Prompt Latent Knowledge Estimator (ZP-LKE), leverages the in-context learning ability of LLMs to communicate both the factual knowledge question as well as the expected answer format. Our knowledge estimator is both conceptually simpler (i.e., doesn't depend on meta-linguistic judgments of LLMs) and easier to apply (i.e., is not LLM-specific), and we demonstrate that it can surface more of the latent knowledge embedded in LLMs. We also investigate how different design choices affect the performance of ZP-LKE. Using the proposed estimator, we perform a large-scale evaluation of the factual knowledge of a variety of open-source LLMs, like OPT, Pythia, Llama(2), Mistral, Gemma, etc. over a large set of relations and facts from the Wikidata knowledge base. We observe differences in the factual knowledge between different model families and models of different sizes, that some relations are consistently better known than others but that models differ in the precise facts they know, and differences in the knowledge of base models and their finetuned counterparts. Code available at: https://github.com/QinyuanWu0710/ZeroPrompt_LKE

**Link**: [arxiv](http://arxiv.org/abs/2404.12957v2),  [pdf](http://arxiv.org/pdf/2404.12957v2)

**Tags**: cs.CL cs.LG 



### The Emergence of Strategic Reasoning of Large Language Models
**Authors**: Dongwoo Lee, Gavin Kader

**Updated**: 2024-12-17T15:34:00Z

**Summary**: As Large Language Models (LLMs) are increasingly used for a variety of complex and critical tasks, it is vital to assess their logical capabilities in strategic environments. This paper examines their ability in strategic reasoning -- the process of choosing an optimal course of action by predicting and adapting to other agents' behavior. Using six LLMs, we analyze responses from play in classical games from behavioral economics (p-Beauty Contest, 11-20 Money Request Game, and Guessing Game) and evaluate their performance through hierarchical models of reasoning (level-$k$ theory and cognitive hierarchy theory). Our findings reveal that while LLMs show understanding of the games, the majority struggle with higher-order strategic reasoning. Although most LLMs did demonstrate learning ability with games involving repeated interactions, they still consistently fall short of the reasoning levels demonstrated by typical behavior from human subjects. The exception to these overall findings is with OpenAI's GPT-o1 -- specifically trained to solve complex reasoning tasks -- which consistently outperforms other LLMs and human subjects. These findings highlight the challenges and pathways in advancing LLMs toward robust strategic reasoning from the perspective of behavioral economics.

**Link**: [arxiv](http://arxiv.org/abs/2412.13013v1),  [pdf](http://arxiv.org/pdf/2412.13013v1)

**Tags**: econ.GN q-fin.EC 



### FootstepNet: an Efficient Actor-Critic Method for Fast On-line Bipedal   Footstep Planning and Forecasting
**Authors**: Clément Gaspard, Grégoire Passault, Mélodie Daniel, Olivier Ly

**Updated**: 2024-12-17T15:28:10Z

**Summary**: Designing a humanoid locomotion controller is challenging and classically split up in sub-problems. Footstep planning is one of those, where the sequence of footsteps is defined. Even in simpler environments, finding a minimal sequence, or even a feasible sequence, yields a complex optimization problem. In the literature, this problem is usually addressed by search-based algorithms (e.g. variants of A*). However, such approaches are either computationally expensive or rely on hand-crafted tuning of several parameters. In this work, at first, we propose an efficient footstep planning method to navigate in local environments with obstacles, based on state-of-the art Deep Reinforcement Learning (DRL) techniques, with very low computational requirements for on-line inference. Our approach is heuristic-free and relies on a continuous set of actions to generate feasible footsteps. In contrast, other methods necessitate the selection of a relevant discrete set of actions. Second, we propose a forecasting method, allowing to quickly estimate the number of footsteps required to reach different candidates of local targets. This approach relies on inherent computations made by the actor-critic DRL architecture. We demonstrate the validity of our approach with simulation results, and by a deployment on a kid-size humanoid robot during the RoboCup 2023 competition.

**Link**: [arxiv](http://arxiv.org/abs/2403.12589v2),  [pdf](http://arxiv.org/pdf/2403.12589v2)

**Tags**: cs.RO cs.AI 



### Reranking individuals: The effect of fair classification within-groups
**Authors**: Sofie Goethals, Marco Favier, Toon Calders

**Updated**: 2024-12-17T15:12:02Z

**Summary**: Artificial Intelligence (AI) finds widespread application across various domains, but it sparks concerns about fairness in its deployment. The prevailing discourse in classification often emphasizes outcome-based metrics comparing sensitive subgroups without a nuanced consideration of the differential impacts within subgroups. Bias mitigation techniques not only affect the ranking of pairs of instances across sensitive groups, but often also significantly affect the ranking of instances within these groups. Such changes are hard to explain and raise concerns regarding the validity of the intervention. Unfortunately, these effects remain under the radar in the accuracy-fairness evaluation framework that is usually applied. Additionally, we illustrate the effect of several popular bias mitigation methods, and how their output often does not reflect real-world scenarios.

**Link**: [arxiv](http://arxiv.org/abs/2401.13391v3),  [pdf](http://arxiv.org/pdf/2401.13391v3)

**Tags**: cs.LG 



### Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental   Health
**Authors**: Vivek Kumar, Eirini Ntoutsi, Pushpraj Singh Rajawat, Giacomo Medda, Diego Reforgiato Recupero

**Updated**: 2024-12-17T15:01:07Z

**Summary**: Large language models (LLMs) have shown promising capabilities in healthcare analysis but face several challenges like hallucinations, parroting, and bias manifestation. These challenges are exacerbated in complex, sensitive, and low-resource domains. Therefore, in this work we introduce IC-AnnoMI, an expert-annotated motivational interviewing (MI) dataset built upon AnnoMI by generating in-context conversational dialogues leveraging LLMs, particularly ChatGPT. IC-AnnoMI employs targeted prompts accurately engineered through cues and tailored information, taking into account therapy style (empathy, reflection), contextual relevance, and false semantic change. Subsequently, the dialogues are annotated by experts, strictly adhering to the Motivational Interviewing Skills Code (MISC), focusing on both the psychological and linguistic dimensions of MI dialogues. We comprehensively evaluate the IC-AnnoMI dataset and ChatGPT's emotional reasoning ability and understanding of domain intricacies by modeling novel classification tasks employing several classical machine learning and current state-of-the-art transformer approaches. Finally, we discuss the effects of progressive prompting strategies and the impact of augmented data in mitigating the biases manifested in IC-AnnoM. Our contributions provide the MI community with not only a comprehensive dataset but also valuable insights for using LLMs in empathetic text generation for conversational therapy in supervised settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12981v1),  [pdf](http://arxiv.org/pdf/2412.12981v1)

**Tags**: cs.CL 



### System-Level Experimental Evaluation of Reconfigurable Intelligent   Surfaces for NextG Communication Systems
**Authors**: Maria Tsampazi, Tommaso Melodia

**Updated**: 2024-12-17T14:53:51Z

**Summary**: Reconfigurable Intelligent Surfaces (RISs) are a promising technique for enhancing the performance of Next Generation (NextG) wireless communication systems in terms of both spectral and energy efficiency, as well as resource utilization. However, current RIS research has primarily focused on theoretical modeling and Physical (PHY) layer considerations only. Full protocol stack emulation and accurate modeling of the propagation characteristics of the wireless channel are necessary for studying the benefits introduced by RIS technology across various spectrum bands and use-cases. In this paper, we propose, for the first time: (i) accurate PHY layer RIS-enabled channel modeling through Geometry-Based Stochastic Models (GBSMs), leveraging the QUAsi Deterministic RadIo channel GenerAtor (QuaDRiGa) open-source statistical ray-tracer; (ii) optimized resource allocation with RISs by comprehensively studying energy efficiency and power control on different portions of the spectrum through a single-leader multiple-followers Stackelberg game theoretical approach; (iii) full-stack emulation and performance evaluation of RIS-assisted channels with SCOPE/srsRAN for Enhanced Mobile Broadband (eMBB) and Ultra Reliable and Low Latency Communications (URLLC) applications in the worlds largest emulator of wireless systems with hardware-in-the-loop, namely Colosseum. Our findings indicate (i) the significant power savings in terms of energy efficiency achieved with RIS-assisted topologies, especially in the millimeter wave (mmWave) band; and (ii) the benefits introduced for Sub-6 GHz band User Equipments (UEs), where the deployment of a relatively small RIS (e.g., in the order of 100 RIS elements) can result in decreased levels of latency for URLLC services in resource-constrained environments.

**Link**: [arxiv](http://arxiv.org/abs/2412.12969v1),  [pdf](http://arxiv.org/pdf/2412.12969v1)

**Tags**: cs.NI eess.SP 



### Adaptations of AI models for querying the LandMatrix database in natural   language
**Authors**: Fatiha Ait Kbir, Jérémy Bourgoin, Rémy Decoupes, Marie Gradeler, Roberto Interdonato

**Updated**: 2024-12-17T14:44:27Z

**Summary**: The Land Matrix initiative (https://landmatrix.org) and its global observatory aim to provide reliable data on large-scale land acquisitions to inform debates and actions in sectors such as agriculture, extraction, or energy in low- and middle-income countries. Although these data are recognized in the academic world, they remain underutilized in public policy, mainly due to the complexity of access and exploitation, which requires technical expertise and a good understanding of the database schema.   The objective of this work is to simplify access to data from different database systems. The methods proposed in this article are evaluated using data from the Land Matrix. This work presents various comparisons of Large Language Models (LLMs) as well as combinations of LLM adaptations (Prompt Engineering, RAG, Agents) to query different database systems (GraphQL and REST queries). The experiments are reproducible, and a demonstration is available online: https://github.com/tetis-nlp/landmatrix-graphql-python.

**Link**: [arxiv](http://arxiv.org/abs/2412.12961v1),  [pdf](http://arxiv.org/pdf/2412.12961v1)

**Tags**: cs.CL 



### SnakModel: Lessons Learned from Training an Open Danish Large Language   Model
**Authors**: Mike Zhang, Max Müller-Eberstein, Elisa Bassignana, Rob van der Goot

**Updated**: 2024-12-17T14:38:21Z

**Summary**: We present SnakModel, a Danish large language model (LLM) based on Llama2-7B, which we continuously pre-train on 13.6B Danish words, and further tune on 3.7M Danish instructions. As best practices for creating LLMs for smaller language communities have yet to be established, we examine the effects of early modeling and training decisions on downstream performance throughout the entire training pipeline, including (1) the creation of a strictly curated corpus of Danish text from diverse sources; (2) the language modeling and instruction-tuning training process itself, including the analysis of intermediate training dynamics, and ablations across different hyperparameters; (3) an evaluation on eight language and culturally-specific tasks. Across these experiments SnakModel achieves the highest overall performance, outperforming multiple contemporary Llama2-7B-based models. By making SnakModel, the majority of our pre-training corpus, and the associated code available under open licenses, we hope to foster further research and development in Danish Natural Language Processing, and establish training guidelines for languages with similar resource constraints.

**Link**: [arxiv](http://arxiv.org/abs/2412.12956v1),  [pdf](http://arxiv.org/pdf/2412.12956v1)

**Tags**: cs.CL 



### FineGates: LLMs Finetuning with Compression using Stochastic Gates
**Authors**: Jonathan Svirsky, Yehonathan Refael, Ofir Lindenbaum

**Updated**: 2024-12-17T14:33:05Z

**Summary**: Large Language Models (LLMs), with billions of parameters, present significant challenges for full finetuning due to the high computational demands, memory requirements, and impracticality of many real-world applications. When faced with limited computational resources or small datasets, updating all model parameters can often result in overfitting. To address this, lightweight finetuning techniques have been proposed, like learning low-rank adapter layers. These methods aim to train only a few additional parameters combined with the base model, which remains frozen, reducing resource usage and mitigating overfitting risks. In this work, we propose an adaptor model based on stochastic gates that simultaneously sparsify the frozen base model with task-specific adaptation. Our method comes with a small number of trainable parameters and allows us to speed up the base model inference with competitive accuracy. We evaluate it in additional variants by equipping it with additional low-rank parameters and comparing it to several recent baselines. Our results show that the proposed method improves the finetuned model accuracy comparatively to the several baselines and allows the removal of up to 20-40\% without significant accuracy loss.

**Link**: [arxiv](http://arxiv.org/abs/2412.12951v1),  [pdf](http://arxiv.org/pdf/2412.12951v1)

**Tags**: cs.LG 



### ProxyLLM : LLM-Driven Framework for Customer Support Through Text-Style   Transfer
**Authors**: Sehyeong Jo, Jungwon Seo

**Updated**: 2024-12-17T14:30:16Z

**Summary**: Chatbot-based customer support services have significantly advanced with the introduction of large language models (LLMs), enabling enhanced response quality and broader application across industries. However, while these advancements focus on reducing business costs and improving customer satisfaction, limited attention has been given to the experiences of customer service agents, who are critical to the service ecosystem. A major challenge faced by agents is the stress caused by unnecessary emotional exhaustion from harmful texts, which not only impairs their efficiency but also negatively affects customer satisfaction and business outcomes. In this work, we propose an LLM-powered system designed to enhance the working conditions of customer service agents by addressing emotionally intensive communications. Our proposed system leverages LLMs to transform the tone of customer messages, preserving actionable content while mitigating the emotional impact on human agents. Furthermore, the application is implemented as a Chrome extension, making it highly adaptable and easy to integrate into existing systems. Our method aims to enhance the overall service experience for businesses, customers, and agents.

**Link**: [arxiv](http://arxiv.org/abs/2412.09916v2),  [pdf](http://arxiv.org/pdf/2412.09916v2)

**Tags**: cs.HC 



### CrAM: Credibility-Aware Attention Modification in LLMs for Combating   Misinformation in RAG
**Authors**: Boyi Deng, Wenjie Wang, Fengbin Zhu, Qifan Wang, Fuli Feng

**Updated**: 2024-12-17T14:11:19Z

**Summary**: Retrieval-Augmented Generation (RAG) can alleviate hallucinations of Large Language Models (LLMs) by referencing external documents. However, the misinformation in external documents may mislead LLMs' generation. To address this issue, we explore the task of "credibility-aware RAG", in which LLMs automatically adjust the influence of retrieved documents based on their credibility scores to counteract misinformation. To this end, we introduce a plug-and-play method named $\textbf{Cr}$edibility-aware $\textbf{A}$ttention $\textbf{M}$odification (CrAM). CrAM identifies influential attention heads in LLMs and adjusts their attention weights based on the credibility of the documents, thereby reducing the impact of low-credibility documents. Experiments on Natual Questions and TriviaQA using Llama2-13B, Llama3-8B, and Qwen1.5-7B show that CrAM improves the RAG performance of LLMs against misinformation pollution by over 20%, even surpassing supervised fine-tuning methods.

**Link**: [arxiv](http://arxiv.org/abs/2406.11497v3),  [pdf](http://arxiv.org/pdf/2406.11497v3)

**Tags**: cs.CL 



### Truthful Text Sanitization Guided by Inference Attacks
**Authors**: Ildikó Pilán, Benet Manzanares-Salor, David Sánchez, Pierre Lison

**Updated**: 2024-12-17T14:07:01Z

**Summary**: The purpose of text sanitization is to rewrite those text spans in a document that may directly or indirectly identify an individual, to ensure they no longer disclose personal information. Text sanitization must strike a balance between preventing the leakage of personal information (privacy protection) while also retaining as much of the document's original content as possible (utility preservation). We present an automated text sanitization strategy based on generalizations, which are more abstract (but still informative) terms that subsume the semantic content of the original text spans. The approach relies on instruction-tuned large language models (LLMs) and is divided into two stages. The LLM is first applied to obtain truth-preserving replacement candidates and rank them according to their abstraction level. Those candidates are then evaluated for their ability to protect privacy by conducting inference attacks with the LLM. Finally, the system selects the most informative replacement shown to be resistant to those attacks. As a consequence of this two-stage process, the chosen replacements effectively balance utility and privacy. We also present novel metrics to automatically evaluate these two aspects without the need to manually annotate data. Empirical results on the Text Anonymization Benchmark show that the proposed approach leads to enhanced utility, with only a marginal increase in the risk of re-identifying protected individuals compared to fully suppressing the original information. Furthermore, the selected replacements are shown to be more truth-preserving and abstractive than previous methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.12928v1),  [pdf](http://arxiv.org/pdf/2412.12928v1)

**Tags**: cs.CL 



### SCANS: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious   Activation Steering
**Authors**: Zouying Cao, Yifei Yang, Hai Zhao

**Updated**: 2024-12-17T13:32:36Z

**Summary**: Safety alignment is indispensable for Large Language Models (LLMs) to defend threats from malicious instructions. However, recent researches reveal safety-aligned LLMs prone to reject benign queries due to the exaggerated safety issue, limiting their helpfulness. In this paper, we propose a Safety-Conscious Activation Steering (SCANS) method to mitigate the exaggerated safety concerns in aligned LLMs. First, SCANS extracts the refusal steering vectors within the activation space and utilizes vocabulary projection to anchor some specific safety-critical layers which influence model refusal behavior. Second, by tracking the hidden state transition, SCANS identifies the steering direction and steers the model behavior accordingly, achieving a balance between exaggerated safety and adequate safety. Experiments show that SCANS achieves new state-of-the-art performance on XSTest and OKTest benchmarks, without impairing their defense capability against harmful queries and maintaining almost unchanged model capability.

**Link**: [arxiv](http://arxiv.org/abs/2408.11491v2),  [pdf](http://arxiv.org/pdf/2408.11491v2)

**Tags**: cs.AI 



### Black-box Model Ensembling for Textual and Visual Question Answering via   Information Fusion
**Authors**: Yuxi Xia, Kilm Zaporojets, Benjamin Roth

**Updated**: 2024-12-17T13:31:18Z

**Summary**: A diverse range of large language models (LLMs), e.g., ChatGPT, and visual question answering (VQA) models, e.g., BLIP, have been developed for solving textual and visual question answering tasks. However, fine-tuning these models is either difficult, as it requires access via APIs, rendering them as black-boxes, or costly due to the need of tuning a large number of parameters. To address this, we introduce InfoSel, a data-efficient ensemble method that learns to dynamically pick the winner from existing black-box models for predictions on both textual and multimodal visual question answering tasks. Unlike traditional ensemble models, InfoSel does not rely on prediction probabilities or confidences, which typically are not available in black-box models. Experimental results on four datasets demonstrate that our approach achieves an absolute increase of up to +5.19\% in the F1-score compared to standalone LLMs using only 1K training instances.

**Link**: [arxiv](http://arxiv.org/abs/2407.12841v2),  [pdf](http://arxiv.org/pdf/2407.12841v2)

**Tags**: cs.CL cs.AI 



### An Agentic Approach to Automatic Creation of P&ID Diagrams from Natural   Language Descriptions
**Authors**: Shreeyash Gowaikar, Srinivasan Iyengar, Sameer Segal, Shivkumar Kalyanaraman

**Updated**: 2024-12-17T13:21:26Z

**Summary**: The Piping and Instrumentation Diagrams (P&IDs) are foundational to the design, construction, and operation of workflows in the engineering and process industries. However, their manual creation is often labor-intensive, error-prone, and lacks robust mechanisms for error detection and correction. While recent advancements in Generative AI, particularly Large Language Models (LLMs) and Vision-Language Models (VLMs), have demonstrated significant potential across various domains, their application in automating generation of engineering workflows remains underexplored. In this work, we introduce a novel copilot for automating the generation of P&IDs from natural language descriptions. Leveraging a multi-step agentic workflow, our copilot provides a structured and iterative approach to diagram creation directly from Natural Language prompts. We demonstrate the feasibility of the generation process by evaluating the soundness and completeness of the workflow, and show improved results compared to vanilla zero-shot and few-shot generation approaches.

**Link**: [arxiv](http://arxiv.org/abs/2412.12898v1),  [pdf](http://arxiv.org/pdf/2412.12898v1)

**Tags**: cs.LG cs.CE cs.CL cs.MA 



### Design of Restricted Normalizing Flow towards Arbitrary Stochastic   Policy with Computational Efficiency
**Authors**: Taisuke Kobayashi, Takumi Aotani

**Updated**: 2024-12-17T13:19:55Z

**Summary**: This paper proposes a new design method for a stochastic control policy using a normalizing flow (NF). In reinforcement learning (RL), the policy is usually modeled as a distribution model with trainable parameters. When this parameterization has less expressiveness, it would fail to acquiring the optimal policy. A mixture model has capability of a universal approximation, but it with too much redundancy increases the computational cost, which can become a bottleneck when considering the use of real-time robot control. As another approach, NF, which is with additional parameters for invertible transformation from a simple stochastic model as a base, is expected to exert high expressiveness and lower computational cost. However, NF cannot compute its mean analytically due to complexity of the invertible transformation, and it lacks reliability because it retains stochastic behaviors after deployment for robot controller. This paper therefore designs a restricted NF (RNF) that achieves an analytic mean by appropriately restricting the invertible transformation. In addition, the expressiveness impaired by this restriction is regained using bimodal student-t distribution as its base, so-called Bit-RNF. In RL benchmarks, Bit-RNF policy outperformed the previous models. Finally, a real robot experiment demonstrated the applicability of Bit-RNF policy to real world. The attached video is uploaded on youtube: https://youtu.be/R_GJVZDW9bk

**Link**: [arxiv](http://arxiv.org/abs/2412.12894v1),  [pdf](http://arxiv.org/pdf/2412.12894v1)

**Tags**: cs.RO cs.LG 



### Question: How do Large Language Models perform on the Question Answering   tasks? Answer:
**Authors**: Kevin Fischer, Darren Fürst, Sebastian Steindl, Jakob Lindner, Ulrich Schäfer

**Updated**: 2024-12-17T13:19:38Z

**Summary**: Large Language Models (LLMs) have been showing promising results for various NLP-tasks without the explicit need to be trained for these tasks by using few-shot or zero-shot prompting techniques. A common NLP-task is question-answering (QA). In this study, we propose a comprehensive performance comparison between smaller fine-tuned models and out-of-the-box instruction-following LLMs on the Stanford Question Answering Dataset 2.0 (SQuAD2), specifically when using a single-inference prompting technique. Since the dataset contains unanswerable questions, previous work used a double inference method. We propose a prompting style which aims to elicit the same ability without the need for double inference, saving compute time and resources. Furthermore, we investigate their generalization capabilities by comparing their performance on similar but different QA datasets, without fine-tuning neither model, emulating real-world uses where the context and questions asked may differ from the original training distribution, for example swapping Wikipedia for news articles.   Our results show that smaller, fine-tuned models outperform current State-Of-The-Art (SOTA) LLMs on the fine-tuned task, but recent SOTA models are able to close this gap on the out-of-distribution test and even outperform the fine-tuned models on 3 of the 5 tested QA datasets.

**Link**: [arxiv](http://arxiv.org/abs/2412.12893v1),  [pdf](http://arxiv.org/pdf/2412.12893v1)

**Tags**: cs.CL 



### Can GPT-O1 Kill All Bugs? An Evaluation of GPT-Family LLMs on QuixBugs
**Authors**: Haichuan Hu, Ye Shang, Guolin Xu, Congqing He, Quanjun Zhang

**Updated**: 2024-12-17T13:16:56Z

**Summary**: LLMs have long demonstrated remarkable effectiveness in automatic program repair (APR), with OpenAI's ChatGPT being one of the most widely used models in this domain. Through continuous iterations and upgrades of GPT-family models, their performance in fixing bugs has already reached state-of-the-art levels. However, there are few works comparing the effectiveness and variations of different versions of GPT-family models on APR. In this work, inspired by the recent public release of the GPT-o1 models, we conduct the first study to compare the effectiveness of different versions of the GPT-family models in APR. We evaluate the performance of the latest version of the GPT-family models (i.e., O1-preview and O1-mini), GPT-4o, and the historical version of ChatGPT on APR. We conduct an empirical study of the four GPT-family models against other LLMs and APR techniques on the QuixBugs benchmark from multiple evaluation perspectives, including repair success rate, repair cost, response length, and behavior patterns. The results demonstrate that O1's repair capability exceeds that of prior GPT-family models, successfully fixing all 40 bugs in the benchmark. Our work can serve as a foundation for further in-depth exploration of the applications of GPT-family models in APR.

**Link**: [arxiv](http://arxiv.org/abs/2409.10033v3),  [pdf](http://arxiv.org/pdf/2409.10033v3)

**Tags**: cs.SE cs.AI 



### A Comparative Study of Pruning Methods in Transformer-based Time Series   Forecasting
**Authors**: Nicholas Kiefer, Arvid Weyrauch, Muhammed Öz, Achim Streit, Markus Götz, Charlotte Debus

**Updated**: 2024-12-17T13:07:31Z

**Summary**: The current landscape in time-series forecasting is dominated by Transformer-based models. Their high parameter count and corresponding demand in computational resources pose a challenge to real-world deployment, especially for commercial and scientific applications with low-power embedded devices. Pruning is an established approach to reduce neural network parameter count and save compute. However, the implications and benefits of pruning Transformer-based models for time series forecasting are largely unknown. To close this gap, we provide a comparative benchmark study by evaluating unstructured and structured pruning on various state-of-the-art multivariate time series models. We study the effects of these pruning strategies on model predictive performance and computational aspects like model size, operations, and inference time. Our results show that certain models can be pruned even up to high sparsity levels, outperforming their dense counterpart. However, fine-tuning pruned models is necessary. Furthermore, we demonstrate that even with corresponding hardware and software support, structured pruning is unable to provide significant time savings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12883v1),  [pdf](http://arxiv.org/pdf/2412.12883v1)

**Tags**: cs.LG cs.AI 



### RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented   Verification and Refinement
**Authors**: Jinhao Jiang, Jiayi Chen, Junyi Li, Ruiyang Ren, Shijie Wang, Wayne Xin Zhao, Yang Song, Tao Zhang

**Updated**: 2024-12-17T13:05:36Z

**Summary**: Existing large language models (LLMs) show exceptional problem-solving capabilities but might struggle with complex reasoning tasks. Despite the successes of chain-of-thought and tree-based search methods, they mainly depend on the internal knowledge of LLMs to search over intermediate reasoning steps, limited to dealing with simple tasks involving fewer reasoning steps. In this paper, we propose \textbf{RAG-Star}, a novel RAG approach that integrates the retrieved information to guide the tree-based deliberative reasoning process that relies on the inherent knowledge of LLMs. By leveraging Monte Carlo Tree Search, RAG-Star iteratively plans intermediate sub-queries and answers for reasoning based on the LLM itself. To consolidate internal and external knowledge, we propose an retrieval-augmented verification that utilizes query- and answer-aware reward modeling to provide feedback for the inherent reasoning of LLMs. Our experiments involving Llama-3.1-8B-Instruct and GPT-4o demonstrate that RAG-Star significantly outperforms previous RAG and reasoning methods.

**Link**: [arxiv](http://arxiv.org/abs/2412.12881v1),  [pdf](http://arxiv.org/pdf/2412.12881v1)

**Tags**: cs.CL cs.AI 



### Preference-Oriented Supervised Fine-Tuning: Favoring Target Model Over   Aligned Large Language Models
**Authors**: Yuchen Fan, Yuzhong Hong, Qiushi Wang, Junwei Bao, Hongfei Jiang, Yang Song

**Updated**: 2024-12-17T12:49:14Z

**Summary**: Alignment, endowing a pre-trained Large language model (LLM) with the ability to follow instructions, is crucial for its real-world applications. Conventional supervised fine-tuning (SFT) methods formalize it as causal language modeling typically with a cross-entropy objective, requiring a large amount of high-quality instruction-response pairs. However, the quality of widely used SFT datasets can not be guaranteed due to the high cost and intensive labor for the creation and maintenance in practice. To overcome the limitations associated with the quality of SFT datasets, we introduce a novel \textbf{p}reference-\textbf{o}riented supervised \textbf{f}ine-\textbf{t}uning approach, namely PoFT. The intuition is to boost SFT by imposing a particular preference: \textit{favoring the target model over aligned LLMs on the same SFT data.} This preference encourages the target model to predict a higher likelihood than that predicted by the aligned LLMs, incorporating assessment information on data quality (i.e., predicted likelihood by the aligned LLMs) into the training process. Extensive experiments are conducted, and the results validate the effectiveness of the proposed method. PoFT achieves stable and consistent improvements over the SFT baselines across different training datasets and base models. Moreover, we prove that PoFT can be integrated with existing SFT data filtering methods to achieve better performance, and further improved by following preference optimization procedures, such as DPO.

**Link**: [arxiv](http://arxiv.org/abs/2412.12865v1),  [pdf](http://arxiv.org/pdf/2412.12865v1)

**Tags**: cs.CL 



### Fine-tuning Large Language Models for Domain-specific Machine   Translation
**Authors**: Jiawei Zheng, Hanghai Hong, Feiyan Liu, Xiaoli Wang, Jingsong Su, Yonggui Liang, Shikai Wu

**Updated**: 2024-12-17T12:45:20Z

**Summary**: Large language models (LLMs) have shown great potential in domain-specific machine translation (MT). However, one major issue is that LLMs pre-trained on general domain corpus might not generalize well to specific domains due to the lack of domain-specific knowledge. To address this issue, this paper focuses on enhancing the domain-specific MT capability of LLMs, by providing high-quality training datasets and proposing a novel fine-tuning framework denoted by DragFT. DragFT augments LLMs via three techniques: (i) Dictionary-enhanced prompting integrates dictionary information into prompts to improve the translation of domain-specific terminology.; (ii) RAG-based few-shot example selection provides high-quality examples that simulate both the domain and style characteristics; (iii) Fine-tuning with few-shot examples further enhances performance when using in-domain examples. We deploy DragFT on three well-known LLM backbones with 13B training parameters to validate its effectiveness. The results on three domain-specific datasets show that DragFT achieves a significant performance boost and shows superior performance compared to advanced models such as GPT-3.5 and GPT-4o. The drastic performance improvement of DragFT over existing LLMs can be attributed to incorporating relevant knowledge while mitigating noise.

**Link**: [arxiv](http://arxiv.org/abs/2402.15061v2),  [pdf](http://arxiv.org/pdf/2402.15061v2)

**Tags**: cs.CL cs.LG 



### LLMLight: Large Language Models as Traffic Signal Control Agents
**Authors**: Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, Hui Xiong

**Updated**: 2024-12-17T12:41:13Z

**Summary**: Traffic Signal Control (TSC) is a crucial component in urban traffic management, aiming to optimize road network efficiency and reduce congestion. Traditional TSC methods, primarily based on transportation engineering and reinforcement learning (RL), often struggle with generalization abilities across varied traffic scenarios and lack interpretability. This paper presents LLMLight, a novel framework employing Large Language Models (LLMs) as decision-making agents for TSC. Specifically, the framework begins by instructing the LLM with a knowledgeable prompt detailing real-time traffic conditions. Leveraging the advanced generalization capabilities of LLMs, LLMLight engages a reasoning and decision-making process akin to human intuition for effective traffic control. Moreover, we build LightGPT, a specialized backbone LLM tailored for TSC tasks. By learning nuanced traffic patterns and control strategies, LightGPT enhances the LLMLight framework cost-effectively. Extensive experiments conducted on ten real-world and synthetic datasets, along with evaluations by fifteen human experts, demonstrate the exceptional effectiveness, generalization ability, and interpretability of LLMLight with LightGPT, outperforming nine baseline methods and ten advanced LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2312.16044v5),  [pdf](http://arxiv.org/pdf/2312.16044v5)

**Tags**: cs.AI 



### Efficient Speech Command Recognition Leveraging Spiking Neural Network   and Curriculum Learning-based Knowledge Distillation
**Authors**: Jiaqi Wang, Liutao Yu, Liwei Huang, Chenlin Zhou, Han Zhang, Zhenxi Song, Min Zhang, Zhengyu Ma, Zhiguo Zhang

**Updated**: 2024-12-17T12:38:45Z

**Summary**: The intrinsic dynamics and event-driven nature of spiking neural networks (SNNs) make them excel in processing temporal information by naturally utilizing embedded time sequences as time steps. Recent studies adopting this approach have demonstrated SNNs' effectiveness in speech command recognition, achieving high performance by employing large time steps for long time sequences. However, the large time steps lead to increased deployment burdens for edge computing applications. Thus, it is important to balance high performance and low energy consumption when detecting temporal patterns in edge devices. Our solution comprises two key components. 1). We propose a high-performance fully spike-driven framework termed SpikeSCR, characterized by a global-local hybrid structure for efficient representation learning, which exhibits long-term learning capabilities with extended time steps. 2). To further fully embrace low energy consumption, we propose an effective knowledge distillation method based on curriculum learning (KDCL), where valuable representations learned from the easy curriculum are progressively transferred to the hard curriculum with minor loss, striking a trade-off between power efficiency and high performance. We evaluate our method on three benchmark datasets: the Spiking Heidelberg Dataset (SHD), the Spiking Speech Commands (SSC), and the Google Speech Commands (GSC) V2. Our experimental results demonstrate that SpikeSCR outperforms current state-of-the-art (SOTA) methods across these three datasets with the same time steps. Furthermore, by executing KDCL, we reduce the number of time steps by 60% and decrease energy consumption by 54.8% while maintaining comparable performance to recent SOTA results. Therefore, this work offers valuable insights for tackling temporal processing challenges with long time sequences in edge neuromorphic computing systems.

**Link**: [arxiv](http://arxiv.org/abs/2412.12858v1),  [pdf](http://arxiv.org/pdf/2412.12858v1)

**Tags**: cs.LG cs.AI cs.HC 



### Enhancing Character-Level Understanding in LLMs through Token Internal   Structure Learning
**Authors**: Zhu Xu, Zhiqiang Zhao, Zihan Zhang, Yuchi Liu, Quanwei Shen, Fei Liu, Yu Kuang, Jian He, Conglin Liu

**Updated**: 2024-12-17T12:37:47Z

**Summary**: Tokenization methods like Byte-Pair Encoding (BPE) enhance computational efficiency in large language models (LLMs) but often obscure internal character structures within tokens. This limitation hinders LLMs' ability to predict precise character positions, which is crucial in tasks like Chinese Spelling Correction (CSC) where identifying the positions of misspelled characters accelerates correction processes. We propose Token Internal Position Awareness (TIPA), a method that significantly improves models' ability to capture character positions within tokens by training them on reverse character prediction tasks using the tokenizer's vocabulary. Experiments demonstrate that TIPA enhances position prediction accuracy in LLMs, enabling more precise identification of target characters in original text. Furthermore, when applied to downstream tasks that do not require exact position prediction, TIPA still boosts performance in tasks needing character-level information, validating its versatility and effectiveness.

**Link**: [arxiv](http://arxiv.org/abs/2411.17679v3),  [pdf](http://arxiv.org/pdf/2411.17679v3)

**Tags**: cs.CL 



### Selective Shot Learning for Code Explanation
**Authors**: Paheli Bhattacharya, Rishabh Gupta

**Updated**: 2024-12-17T12:26:14Z

**Summary**: Code explanation plays a crucial role in the software engineering domain, aiding developers in grasping code functionality efficiently. Recent work shows that the performance of LLMs for code explanation improves in a few-shot setting, especially when the few-shot examples are selected intelligently. State-of-the-art approaches for such Selective Shot Learning (SSL) include token-based and embedding-based methods. However, these SSL approaches have been evaluated on proprietary LLMs, without much exploration on open-source Code-LLMs. Additionally, these methods lack consideration for programming language syntax. To bridge these gaps, we present a comparative study and propose a novel SSL method (SSL_ner) that utilizes entity information for few-shot example selection. We present several insights and show the effectiveness of SSL_ner approach over state-of-the-art methods across two datasets. To the best of our knowledge, this is the first systematic benchmarking of open-source Code-LLMs while assessing the performances of the various few-shot examples selection approaches for the code explanation task.

**Link**: [arxiv](http://arxiv.org/abs/2412.12852v1),  [pdf](http://arxiv.org/pdf/2412.12852v1)

**Tags**: cs.SE cs.CL cs.IR 



### ClarityEthic: Explainable Moral Judgment Utilizing Contrastive Ethical   Insights from Large Language Models
**Authors**: Yuxi Sun, Wei Gao, Jing Ma, Hongzhan Lin, Ziyang Luo, Wenxuan Zhang

**Updated**: 2024-12-17T12:22:44Z

**Summary**: With the rise and widespread use of Large Language Models (LLMs), ensuring their safety is crucial to prevent harm to humans and promote ethical behaviors. However, directly assessing value valence (i.e., support or oppose) by leveraging large-scale data training is untrustworthy and inexplainable. We assume that emulating humans to rely on social norms to make moral decisions can help LLMs understand and predict moral judgment. However, capturing human values remains a challenge, as multiple related norms might conflict in specific contexts. Consider norms that are upheld by the majority and promote the well-being of society are more likely to be accepted and widely adopted (e.g., "don't cheat,"). Therefore, it is essential for LLM to identify the appropriate norms for a given scenario before making moral decisions. To this end, we introduce a novel moral judgment approach called \textit{ClarityEthic} that leverages LLMs' reasoning ability and contrastive learning to uncover relevant social norms for human actions from different perspectives and select the most reliable one to enhance judgment accuracy. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches in moral judgment tasks. Moreover, human evaluations confirm that the generated social norms provide plausible explanations that support the judgments. This suggests that modeling human moral judgment with the emulating humans moral strategy is promising for improving the ethical behaviors of LLMs.

**Link**: [arxiv](http://arxiv.org/abs/2412.12848v1),  [pdf](http://arxiv.org/pdf/2412.12848v1)

**Tags**: cs.CY cs.AI cs.SI 



### Towards Reliable Detection of LLM-Generated Texts: A Comprehensive   Evaluation Framework with CUDRT
**Authors**: Zhen Tao, Yanfang Chen, Dinghao Xi, Zhiyu Li, Wei Xu

**Updated**: 2024-12-17T12:20:34Z

**Summary**: The increasing prevalence of large language models (LLMs) has significantly advanced text generation, but the human-like quality of LLM outputs presents major challenges in reliably distinguishing between human-authored and LLM-generated texts. Existing detection benchmarks are constrained by their reliance on static datasets, scenario-specific tasks (e.g., question answering and text refinement), and a primary focus on English, overlooking the diverse linguistic and operational subtleties of LLMs. To address these gaps, we propose CUDRT, a comprehensive evaluation framework and bilingual benchmark in Chinese and English, categorizing LLM activities into five key operations: Create, Update, Delete, Rewrite, and Translate. CUDRT provides extensive datasets tailored to each operation, featuring outputs from state-of-the-art LLMs to assess the reliability of LLM-generated text detectors. This framework supports scalable, reproducible experiments and enables in-depth analysis of how operational diversity, multilingual training sets, and LLM architectures influence detection performance. Our extensive experiments demonstrate the framework's capacity to optimize detection systems, providing critical insights to enhance reliability, cross-linguistic adaptability, and detection accuracy. By advancing robust methodologies for identifying LLM-generated texts, this work contributes to the development of intelligent systems capable of meeting real-world multilingual detection challenges. Source code and dataset are available at GitHub.

**Link**: [arxiv](http://arxiv.org/abs/2406.09056v3),  [pdf](http://arxiv.org/pdf/2406.09056v3)

**Tags**: cs.CL cs.AI 



### Benchmarking and Understanding Compositional Relational Reasoning of   LLMs
**Authors**: Ruikang Ni, Da Xiao, Qingye Meng, Xiangyu Li, Shihui Zheng, Hongliang Liang

**Updated**: 2024-12-17T12:10:38Z

**Summary**: Compositional relational reasoning (CRR) is a hallmark of human intelligence, but we lack a clear understanding of whether and how existing transformer large language models (LLMs) can solve CRR tasks. To enable systematic exploration of the CRR capability of LLMs, we first propose a new synthetic benchmark called Generalized Associative Recall (GAR) by integrating and generalizing the essence of several tasks in mechanistic interpretability (MI) study in a unified framework. Evaluation shows that GAR is challenging enough for existing LLMs, revealing their fundamental deficiency in CRR. Meanwhile, it is easy enough for systematic MI study. Then, to understand how LLMs solve GAR tasks, we use attribution patching to discover the core circuits reused by Vicuna-33B across different tasks and a set of vital attention heads. Intervention experiments show that the correct functioning of these heads significantly impacts task performance. Especially, we identify two classes of heads whose activations represent the abstract notion of true and false in GAR tasks respectively. They play a fundamental role in CRR across various models and tasks. The dataset and code are available at https://github.com/Caiyun-AI/GAR.

**Link**: [arxiv](http://arxiv.org/abs/2412.12841v1),  [pdf](http://arxiv.org/pdf/2412.12841v1)

**Tags**: cs.CL cs.LG 



### From An LLM Swarm To A PDDL-Empowered HIVE: Planning Self-Executed   Instructions In A Multi-Modal Jungle
**Authors**: Kaustubh Vyas, Damien Graux, Yijun Yang, Sébastien Montella, Chenxin Diao, Wendi Zhou, Pavlos Vougiouklis, Ruofei Lai, Yang Ren, Keshuang Li, Jeff Z. Pan

**Updated**: 2024-12-17T12:05:21Z

**Summary**: In response to the call for agent-based solutions that leverage the ever-increasing capabilities of the deep models' ecosystem, we introduce Hive -- a comprehensive solution for selecting appropriate models and subsequently planning a set of atomic actions to satisfy the end-users' instructions. Hive operates over sets of models and, upon receiving natural language instructions (i.e. user queries), schedules and executes explainable plans of atomic actions. These actions can involve one or more of the available models to achieve the overall task, while respecting end-users specific constraints. Notably, Hive handles tasks that involve multi-modal inputs and outputs, enabling it to handle complex, real-world queries. Our system is capable of planning complex chains of actions while guaranteeing explainability, using an LLM-based formal logic backbone empowered by PDDL operations. We introduce the MuSE benchmark in order to offer a comprehensive evaluation of the multi-modal capabilities of agent systems. Our findings show that our framework redefines the state-of-the-art for task selection, outperforming other competing systems that plan operations across multiple models while offering transparency guarantees while fully adhering to user constraints.

**Link**: [arxiv](http://arxiv.org/abs/2412.12839v1),  [pdf](http://arxiv.org/pdf/2412.12839v1)

**Tags**: cs.AI 



### What Matters in Learning A Zero-Shot Sim-to-Real RL Policy for Quadrotor   Control? A Comprehensive Study
**Authors**: Jiayu Chen, Chao Yu, Yuqing Xie, Feng Gao, Yinuo Chen, Shu'ang Yu, Wenhao Tang, Shilong Ji, Mo Mu, Yi Wu, Huazhong Yang, Yu Wang

**Updated**: 2024-12-17T12:04:49Z

**Summary**: Executing precise and agile flight maneuvers is critical for quadrotors in various applications. Traditional quadrotor control approaches are limited by their reliance on flat trajectories or time-consuming optimization, which restricts their flexibility. Recently, RL-based policy has emerged as a promising alternative due to its ability to directly map observations to actions, reducing the need for detailed system knowledge and actuation constraints. However, a significant challenge remains in bridging the sim-to-real gap, where RL-based policies often experience instability when deployed in real world. In this paper, we investigate key factors for learning robust RL-based control policies that are capable of zero-shot deployment in real-world quadrotors. We identify five critical factors and we develop a PPO-based training framework named SimpleFlight, which integrates these five techniques. We validate the efficacy of SimpleFlight on Crazyflie quadrotor, demonstrating that it achieves more than a 50% reduction in trajectory tracking error compared to state-of-the-art RL baselines, and achieves 70% improvement over the traditional MPC. The policy derived by SimpleFlight consistently excels across both smooth polynominal trajectories and challenging infeasible zigzag trajectories on small thrust-to-weight quadrotors. In contrast, baseline methods struggle with high-speed or infeasible trajectories. To support further research and reproducibility, we integrate SimpleFlight into a GPU-based simulator Omnidrones and provide open-source access to the code and model checkpoints. We hope SimpleFlight will offer valuable insights for advancing RL-based quadrotor control. For more details, visit our project website at https://sites.google.com/view/simpleflight/.

**Link**: [arxiv](http://arxiv.org/abs/2412.11764v2),  [pdf](http://arxiv.org/pdf/2412.11764v2)

**Tags**: cs.RO cs.LG 



### FocusChat: Text-guided Long Video Understanding via Spatiotemporal   Information Filtering
**Authors**: Zheng Cheng, Rendong Wang, Zhicheng Wang

**Updated**: 2024-12-17T11:54:47Z

**Summary**: Recently, multi-modal large language models have made significant progress. However, visual information lacking of guidance from the user's intention may lead to redundant computation and involve unnecessary visual noise, especially in long, untrimmed videos. To address this issue, we propose FocusChat, a text-guided multi-modal large language model (LLM) that emphasizes visual information correlated to the user's prompt. In detail, Our model first undergoes the semantic extraction module, which comprises a visual semantic branch and a text semantic branch to extract image and text semantics, respectively. The two branches are combined using the Spatial-Temporal Filtering Module (STFM). STFM enables explicit spatial-level information filtering and implicit temporal-level feature filtering, ensuring that the visual tokens are closely aligned with the user's query. It lowers the essential number of visual tokens inputted into the LLM. FocusChat significantly outperforms Video-LLaMA in zero-shot experiments, using an order of magnitude less training data with only 16 visual tokens occupied. It achieves results comparable to the state-of-the-art in few-shot experiments, with only 0.72M pre-training data.

**Link**: [arxiv](http://arxiv.org/abs/2412.12833v1),  [pdf](http://arxiv.org/pdf/2412.12833v1)

**Tags**: cs.CV 



### DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction   in the Era of Large Language Models
**Authors**: Jinxiang Xie, Yilin Li, Xunjian Yin, Xiaojun Wan

**Updated**: 2024-12-17T11:54:16Z

**Summary**: Evaluating the performance of Grammatical Error Correction (GEC) models has become increasingly challenging, as large language model (LLM)-based GEC systems often produce corrections that diverge from provided gold references. This discrepancy undermines the reliability of traditional reference-based evaluation metrics. In this study, we propose a novel evaluation framework for GEC models, DSGram, integrating Semantic Coherence, Edit Level, and Fluency, and utilizing a dynamic weighting mechanism. Our framework employs the Analytic Hierarchy Process (AHP) in conjunction with large language models to ascertain the relative importance of various evaluation criteria. Additionally, we develop a dataset incorporating human annotations and LLM-simulated sentences to validate our algorithms and fine-tune more cost-effective models. Experimental results indicate that our proposed approach enhances the effectiveness of GEC model evaluations.

**Link**: [arxiv](http://arxiv.org/abs/2412.12832v1),  [pdf](http://arxiv.org/pdf/2412.12832v1)

**Tags**: cs.CL cs.AI 



### Africanus IV. The Stimela2 framework: scalable and reproducible   workflows, from local to cloud compute
**Authors**: Oleg M. Smirnov, Sphesihle Makhathini, Jonathan S. Kenyon, Hertzog L. Bester, Simon J. Perkins, Athanaseus J. T. Ramaila, Benjamin V. Hugo

**Updated**: 2024-12-17T11:45:55Z

**Summary**: Stimela2 is a new-generation framework for developing data reduction workflows. It is designed for radio astronomy data but can be adapted for other data processing applications. Stimela2 aims at the middle ground between ease of development, human readability, and enabling robust, scalable and reproducible workflows. It represents workflows by linear, concise and intuitive YAML-format "recipes". Atomic data reduction tasks (binary executables, Python functions and code, and CASA tasks) are described by YAML-format "cab definitions" detailing each task's "schema" (inputs and outputs). Stimela2 provides a rich syntax for chaining tasks together, and encourages a high degree of modularity: recipes may be nested into other recipes, and configuration is cleanly separated from recipe logic. Tasks can be executed natively or in isolated environments using containerization technologies such as Apptainer. The container images are open-source and maintained through a companion package called cult-cargo. This enables the development of system-agnostic and fully reproducible workflows. Stimela2 facilitates the deployment of scalable, distributed workflows by interfacing with the Slurm scheduler and the Kubernetes API. The latter allows workflows to be readily deployed in the cloud. Previous papers in this series used Stimela2 as the underlying technology to run workflows on the AWS cloud.   This paper presents an overview of Stimela2's design, architecture and use in the radio astronomy context.

**Link**: [arxiv](http://arxiv.org/abs/2412.10080v2),  [pdf](http://arxiv.org/pdf/2412.10080v2)

**Tags**: astro-ph.IM 



### Activating Distributed Visual Region within LLMs for Efficient and   Effective Vision-Language Training and Inference
**Authors**: Siyuan Wang, Dianyi Wang, Chengxing Zhou, Zejun Li, Zhihao Fan, Xuanjing Huang, Zhongyu Wei

**Updated**: 2024-12-17T10:44:47Z

**Summary**: Large Vision-Language Models (LVLMs) typically learn visual capacity through visual instruction tuning, involving updates to both a projector and their LLM backbones. Drawing inspiration from the concept of visual region in the human brain, we investigate the existence of an analogous \textit{visual region} within LLMs that functions as a cognitive core, and explore the possibility of efficient training of LVLMs via selective layers tuning. We use Bunny-Llama-3-8B-V for detailed experiments and LLaVA-1.5-7B and LLaVA-1.5-13B for validation across a range of visual and textual tasks. Our findings reveal that selectively updating 25\% of LLMs layers, when sparsely and uniformly distributed, can preserve nearly 99\% of visual performance while maintaining or enhancing textual task results, and also effectively reducing training time. Based on this targeted training approach, we further propose a novel visual region-based pruning paradigm, removing non-critical layers outside the visual region, which can achieve minimal performance loss. This study offers an effective and efficient strategy for LVLM training and inference by activating a layer-wise visual region within LLMs, which is consistently effective across different models and parameter scales.

**Link**: [arxiv](http://arxiv.org/abs/2412.12785v1),  [pdf](http://arxiv.org/pdf/2412.12785v1)

**Tags**: cs.CV 



### RemoteRAG: A Privacy-Preserving LLM Cloud RAG Service
**Authors**: Yihang Cheng, Lan Zhang, Junyang Wang, Mu Yuan, Yunhao Yao

**Updated**: 2024-12-17T10:36:52Z

**Summary**: Retrieval-augmented generation (RAG) improves the service quality of large language models by retrieving relevant documents from credible literature and integrating them into the context of the user query. Recently, the rise of the cloud RAG service has made it possible for users to query relevant documents conveniently. However, directly sending queries to the cloud brings potential privacy leakage. In this paper, we are the first to formally define the privacy-preserving cloud RAG service to protect the user query and propose RemoteRAG as a solution regarding privacy, efficiency, and accuracy. For privacy, we introduce $(n,\epsilon)$-DistanceDP to characterize privacy leakage of the user query and the leakage inferred from relevant documents. For efficiency, we limit the search range from the total documents to a small number of selected documents related to a perturbed embedding generated from $(n,\epsilon)$-DistanceDP, so that computation and communication costs required for privacy protection significantly decrease. For accuracy, we ensure that the small range includes target documents related to the user query with detailed theoretical analysis. Experimental results also demonstrate that RemoteRAG can resist existing embedding inversion attack methods while achieving no loss in retrieval under various settings. Moreover, RemoteRAG is efficient, incurring only $0.67$ seconds and $46.66$KB of data transmission ($2.72$ hours and $1.43$ GB with the non-optimized privacy-preserving scheme) when retrieving from a total of $10^6$ documents.

**Link**: [arxiv](http://arxiv.org/abs/2412.12775v1),  [pdf](http://arxiv.org/pdf/2412.12775v1)

**Tags**: cs.IR cs.CR 



### HyperGraphOS: A Modern Meta-Operating System for the Scientific and   Engineering Domains
**Authors**: Antonello Ceravola, Frank Joublin

**Updated**: 2024-12-17T10:35:33Z

**Summary**: This paper presents HyperGraphOS, a significant innovation in the domain of operating systems, specifically designed to address the needs of scientific and engineering domains. This platform aims to combine model-based engineering, graph modeling, data containers, and documents, along with tools for handling computational elements. HyperGraphOS functions as an Operating System offering to users an infinite workspace for creating and managing complex models represented as graphs with customizable semantics. By leveraging a web-based architecture, it requires only a modern web browser for access, allowing organization of knowledge, documents, and content into models represented in a network of workspaces. Elements of the workspace are defined in terms of domain-specific languages (DSLs). These DSLs are pivotal for navigating workspaces, generating code, triggering AI components, and organizing information and processes. The models' dual nature as both visual drawings and data structures allows dynamic modifications and inspections both interactively as well as programaticaly. We evaluated HyperGraphOS's efficiency and applicability across a large set of diverse domains, including the design and development of a virtual Avatar dialog system, a robotic task planner based on large language models (LLMs), a new meta-model for feature-based code development and many others. Our findings show that HyperGraphOS offers substantial benefits in the interaction with a computer as information system, as platoform for experiments and data analysis, as streamlined engineering processes, demonstrating enhanced flexibility in managing data, computation and documents, showing an innovative approaches to persistent desktop environments.

**Link**: [arxiv](http://arxiv.org/abs/2412.10487v2),  [pdf](http://arxiv.org/pdf/2412.10487v2)

**Tags**: cs.SE cs.OS cs.PL 68 



### A Survey on Sequential Recommendation
**Authors**: Liwei Pan, Weike Pan, Meiyan Wei, Hongzhi Yin, Zhong Ming

**Updated**: 2024-12-17T10:33:13Z

**Summary**: Different from most conventional recommendation problems, sequential recommendation focuses on learning users' preferences by exploiting the internal order and dependency among the interacted items, which has received significant attention from both researchers and practitioners. In recent years, we have witnessed great progress and achievements in this field, necessitating a new survey. In this survey, we study the SR problem from a new perspective (i.e., the construction of an item's properties), and summarize the most recent techniques used in sequential recommendation such as pure ID-based SR, SR with side information, multi-modal SR, generative SR, LLM-powered SR, ultra-long SR and data-augmented SR. Moreover, we introduce some frontier research topics in sequential recommendation, e.g., open-domain SR, data-centric SR, could-edge collaborative SR, continuous SR, SR for good, and explainable SR. We believe that our survey could be served as a valuable roadmap for readers in this field.

**Link**: [arxiv](http://arxiv.org/abs/2412.12770v1),  [pdf](http://arxiv.org/pdf/2412.12770v1)

**Tags**: cs.IR 



### A Survey of Calibration Process for Black-Box LLMs
**Authors**: Liangru Xie, Hui Liu, Jingying Zeng, Xianfeng Tang, Yan Han, Chen Luo, Jing Huang, Zhen Li, Suhang Wang, Qi He

**Updated**: 2024-12-17T10:31:21Z

**Summary**: Large Language Models (LLMs) demonstrate remarkable performance in semantic understanding and generation, yet accurately assessing their output reliability remains a significant challenge. While numerous studies have explored calibration techniques, they primarily focus on White-Box LLMs with accessible parameters. Black-Box LLMs, despite their superior performance, pose heightened requirements for calibration techniques due to their API-only interaction constraints. Although recent researches have achieved breakthroughs in black-box LLMs calibration, a systematic survey of these methodologies is still lacking. To bridge this gap, we presents the first comprehensive survey on calibration techniques for black-box LLMs. We first define the Calibration Process of LLMs as comprising two interrelated key steps: Confidence Estimation and Calibration. Second, we conduct a systematic review of applicable methods within black-box settings, and provide insights on the unique challenges and connections in implementing these key steps. Furthermore, we explore typical applications of Calibration Process in black-box LLMs and outline promising future research directions, providing new perspectives for enhancing reliability and human-machine alignment. This is our GitHub link: https://github.com/LiangruXie/Calibration-Process-in-Black-Box-LLMs

**Link**: [arxiv](http://arxiv.org/abs/2412.12767v1),  [pdf](http://arxiv.org/pdf/2412.12767v1)

**Tags**: cs.AI cs.CL 



### Using LLM-Generated Draft Replies to Support Human Experts in Responding   to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of   Industrial AI
**Authors**: Tita Alissa Bach, Aleksandar Babic, Narae Park, Tor Sporsem, Rasmus Ulfsnes, Henrik Smith-Meyer, Torkel Skeie

**Updated**: 2024-12-17T09:55:02Z

**Summary**: The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

**Link**: [arxiv](http://arxiv.org/abs/2412.12732v1),  [pdf](http://arxiv.org/pdf/2412.12732v1)

**Tags**: cs.HC 



### WIKIGENBENCH: Exploring Full-length Wikipedia Generation under   Real-World Scenario
**Authors**: Jiebin Zhang, Eugene J. Yu, Qinyu Chen, Chenhao Xiong, Dawei Zhu, Han Qian, Mingbo Song, Weimin Xiong, Xiaoguang Li, Qun Liu, Sujian Li

**Updated**: 2024-12-17T09:53:41Z

**Summary**: It presents significant challenges to generate comprehensive and accurate Wikipedia articles for newly emerging events under a real-world scenario. Existing attempts fall short either by focusing only on short snippets or by using metrics that are insufficient to evaluate real-world scenarios. In this paper, we construct WIKIGENBENCH, a new benchmark consisting of 1,320 entries, designed to align with real-world scenarios in both generation and evaluation. For generation, we explore a real-world scenario where structured, full-length Wikipedia articles with citations are generated for new events using input documents from web sources. For evaluation, we integrate systematic metrics and LLM-based metrics to assess the verifiability, organization, and other aspects aligned with real-world scenarios. Based on this benchmark, we conduct extensive experiments using various models within three commonly used frameworks: direct RAG, hierarchical structure-based RAG, and RAG with a fine-tuned generation model. Experimental results show that hierarchical-based methods can generate more comprehensive content, while fine-tuned methods achieve better verifiability. However, even the best methods still show a significant gap compared to existing Wikipedia content, indicating that further research is necessary.

**Link**: [arxiv](http://arxiv.org/abs/2402.18264v2),  [pdf](http://arxiv.org/pdf/2402.18264v2)

**Tags**: cs.CL 



### ASAP: Advancing Semantic Alignment Promotes Multi-Modal Manipulation   Detecting and Grounding
**Authors**: Zhenxing Zhang, Yaxiong Wang, Lechao Cheng, Zhun Zhong, Dan Guo, Meng Wang

**Updated**: 2024-12-17T09:33:06Z

**Summary**: We present ASAP, a new framework for detecting and grounding multi-modal media manipulation (DGM4).Upon thorough examination, we observe that accurate fine-grained cross-modal semantic alignment between the image and text is vital for accurately manipulation detection and grounding. While existing DGM4 methods pay rare attention to the cross-modal alignment, hampering the accuracy of manipulation detecting to step further. To remedy this issue, this work targets to advance the semantic alignment learning to promote this task. Particularly, we utilize the off-the-shelf Multimodal Large-Language Models (MLLMs) and Large Language Models (LLMs) to construct paired image-text pairs, especially for the manipulated instances. Subsequently, a cross-modal alignment learning is performed to enhance the semantic alignment. Besides the explicit auxiliary clues, we further design a Manipulation-Guided Cross Attention (MGCA) to provide implicit guidance for augmenting the manipulation perceiving. With the grounding truth available during training, MGCA encourages the model to concentrate more on manipulated components while downplaying normal ones, enhancing the model's ability to capture manipulations. Extensive experiments are conducted on the DGM4 dataset, the results demonstrate that our model can surpass the comparison method with a clear margin.

**Link**: [arxiv](http://arxiv.org/abs/2412.12718v1),  [pdf](http://arxiv.org/pdf/2412.12718v1)

**Tags**: cs.CV cs.MM Multimedia 



### No More Adam: Learning Rate Scaling at Initialization is All You Need
**Authors**: Minghao Xu, Lichuan Xiang, Xu Cai, Hongkai Wen

**Updated**: 2024-12-17T09:30:44Z

**Summary**: In this work, we question the necessity of adaptive gradient methods for training deep neural networks. SGD-SaI is a simple yet effective enhancement to stochastic gradient descent with momentum (SGDM). SGD-SaI performs learning rate Scaling at Initialization (SaI) to distinct parameter groups, guided by their respective gradient signal-to-noise ratios (g-SNR). By adjusting learning rates without relying on adaptive second-order momentum, SGD-SaI helps prevent training imbalances from the very first iteration and cuts the optimizer's memory usage by half compared to AdamW. Despite its simplicity and efficiency, SGD-SaI consistently matches or outperforms AdamW in training a variety of Transformer-based tasks, effectively overcoming a long-standing challenge of using SGD for training Transformers. SGD-SaI excels in ImageNet-1K classification with Vision Transformers(ViT) and GPT-2 pretraining for large language models (LLMs, transformer decoder-only), demonstrating robustness to hyperparameter variations and practicality for diverse applications. We further tested its robustness on tasks like LoRA fine-tuning for LLMs and diffusion models, where it consistently outperforms state-of-the-art optimizers. From a memory efficiency perspective, SGD-SaI achieves substantial memory savings for optimizer states, reducing memory usage by 5.93 GB for GPT-2 (1.5B parameters) and 25.15 GB for Llama2-7B compared to AdamW in full-precision training settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.11768v2),  [pdf](http://arxiv.org/pdf/2412.11768v2)

**Tags**: cs.LG cs.AI 



### Enhancing Naturalness in LLM-Generated Utterances through Disfluency   Insertion
**Authors**: Syed Zohaib Hassan, Pierre Lison, Pål Halvorsen

**Updated**: 2024-12-17T09:25:44Z

**Summary**: Disfluencies are a natural feature of spontaneous human speech but are typically absent from the outputs of Large Language Models (LLMs). This absence can diminish the perceived naturalness of synthesized speech, which is an important criteria when building conversational agents that aim to mimick human behaviours. We show how the insertion of disfluencies can alleviate this shortcoming. The proposed approach involves (1) fine-tuning an LLM with Low-Rank Adaptation (LoRA) to incorporate various types of disfluencies into LLM-generated utterances and (2) synthesizing those utterances using a text-to-speech model that supports the generation of speech phenomena such as disfluencies. We evaluated the quality of the generated speech across two metrics: intelligibility and perceived spontaneity. We demonstrate through a user study that the insertion of disfluencies significantly increase the perceived spontaneity of the generated speech. This increase came, however, along with a slight reduction in intelligibility.

**Link**: [arxiv](http://arxiv.org/abs/2412.12710v1),  [pdf](http://arxiv.org/pdf/2412.12710v1)

**Tags**: cs.CL 



### More Tokens, Lower Precision: Towards the Optimal Token-Precision   Trade-off in KV Cache Compression
**Authors**: Jiebin Zhang, Dawei Zhu, Yifan Song, Wenhao Wu, Chuqiao Kuang, Xiaoguang Li, Lifeng Shang, Qun Liu, Sujian Li

**Updated**: 2024-12-17T09:20:31Z

**Summary**: As large language models (LLMs) process increasing context windows, the memory usage of KV cache has become a critical bottleneck during inference. The mainstream KV compression methods, including KV pruning and KV quantization, primarily focus on either token or precision dimension and seldom explore the efficiency of their combination. In this paper, we comprehensively investigate the token-precision trade-off in KV cache compression. Experiments demonstrate that storing more tokens in the KV cache with lower precision, i.e., quantized pruning, can significantly enhance the long-context performance of LLMs. Furthermore, in-depth analysis regarding token-precision trade-off from a series of key aspects exhibit that, quantized pruning achieves substantial improvements in retrieval-related tasks and consistently performs well across varying input lengths. Moreover, quantized pruning demonstrates notable stability across different KV pruning methods, quantization strategies, and model scales. These findings provide valuable insights into the token-precision trade-off in KV cache compression. We plan to release our code in the near future.

**Link**: [arxiv](http://arxiv.org/abs/2412.12706v1),  [pdf](http://arxiv.org/pdf/2412.12706v1)

**Tags**: cs.CL 



### Trigger$^3$: Refining Query Correction via Adaptive Model Selector
**Authors**: Kepu Zhang, Zhongxiang Sun, Xiao Zhang, Xiaoxue Zang, Kai Zheng, Yang Song, Jun Xu

**Updated**: 2024-12-17T09:16:54Z

**Summary**: In search scenarios, user experience can be hindered by erroneous queries due to typos, voice errors, or knowledge gaps. Therefore, query correction is crucial for search engines. Current correction models, usually small models trained on specific data, often struggle with queries beyond their training scope or those requiring contextual understanding. While the advent of Large Language Models (LLMs) offers a potential solution, they are still limited by their pre-training data and inference cost, particularly for complex queries, making them not always effective for query correction. To tackle these, we propose Trigger$^3$, a large-small model collaboration framework that integrates the traditional correction model and LLM for query correction, capable of adaptively choosing the appropriate correction method based on the query and the correction results from the traditional correction model and LLM. Trigger$^3$ first employs a correction trigger to filter out correct queries. Incorrect queries are then corrected by the traditional correction model. If this fails, an LLM trigger is activated to call the LLM for correction. Finally, for queries that no model can correct, a fallback trigger decides to return the original query. Extensive experiments demonstrate Trigger$^3$ outperforms correction baselines while maintaining efficiency.

**Link**: [arxiv](http://arxiv.org/abs/2412.12701v1),  [pdf](http://arxiv.org/pdf/2412.12701v1)

**Tags**: cs.CL 



### Audio Array-Based 3D UAV Trajectory Estimation with LiDAR   Pseudo-Labeling
**Authors**: Allen Lei, Tianchen Deng, Han Wang, Jianfei Yang, Shenghai Yuan

**Updated**: 2024-12-17T09:16:28Z

**Summary**: As small unmanned aerial vehicles (UAVs) become increasingly prevalent, there is growing concern regarding their impact on public safety and privacy, highlighting the need for advanced tracking and trajectory estimation solutions. In response, this paper introduces a novel framework that utilizes audio array for 3D UAV trajectory estimation. Our approach incorporates a self-supervised learning model, starting with the conversion of audio data into mel-spectrograms, which are analyzed through an encoder to extract crucial temporal and spectral information. Simultaneously, UAV trajectories are estimated using LiDAR point clouds via unsupervised methods. These LiDAR-based estimations act as pseudo labels, enabling the training of an Audio Perception Network without requiring labeled data. In this architecture, the LiDAR-based system operates as the Teacher Network, guiding the Audio Perception Network, which serves as the Student Network. Once trained, the model can independently predict 3D trajectories using only audio signals, with no need for LiDAR data or external ground truth during deployment. To further enhance precision, we apply Gaussian Process modeling for improved spatiotemporal tracking. Our method delivers top-tier performance on the MMAUD dataset, establishing a new benchmark in trajectory estimation using self-supervised learning techniques without reliance on ground truth annotations.

**Link**: [arxiv](http://arxiv.org/abs/2412.12698v1),  [pdf](http://arxiv.org/pdf/2412.12698v1)

**Tags**: cs.RO cs.SD eess.AS 



### FiRST: Finetuning Router-Selective Transformers for Input-Adaptive   Latency Reduction
**Authors**: Akriti Jain, Saransh Sharma, Koyel Mukherjee, Soumyabrata Pal

**Updated**: 2024-12-17T09:11:47Z

**Summary**: Auto-regressive Large Language Models (LLMs) demonstrate remarkable performance across different domains such as vision and language processing. However, due to sequential processing through a stack of transformer layers, autoregressive decoding faces significant computation/latency challenges, particularly in resource-constrained environments like mobile and edge devices. Existing approaches in literature that aim to improve latency via skipping layers have two distinct flavors - 1) Early exit, and 2) Input-agnostic heuristics where tokens exit at pre-determined layers irrespective of input sequence. Both the above strategies have limitations - the former cannot be applied to handle KV Caching necessary for speed-ups in modern framework and the latter does not capture the variation in layer importance across tasks or more generally, across input sequences. To address both limitations, we propose FiRST, an algorithm that reduces inference latency by using layer-specific routers to select a subset of transformer layers adaptively for each input sequence - the prompt (during the prefill stage) decides which layers will be skipped during decoding. FiRST preserves compatibility with KV caching enabling faster inference while being quality-aware. FiRST is model-agnostic and can be easily enabled on any pre-trained LLM. Our approach reveals that input adaptivity is critical - indeed, different task-specific middle layers play a crucial role in evolving hidden representations depending on tasks. Extensive experiments show that FiRST significantly reduces latency while outperforming other layer selection strategies in quality metics. It retains competitive performance to base model (without layer skipping) and in some cases, even improves upon it. FiRST is thus a promising and efficient solution for LLM deployment in low-resource environments.

**Link**: [arxiv](http://arxiv.org/abs/2410.12513v2),  [pdf](http://arxiv.org/pdf/2410.12513v2)

**Tags**: cs.CL 



### UniEntrezDB: Large-scale Gene Ontology Annotation Dataset and Evaluation   Benchmarks with Unified Entrez Gene Identifiers
**Authors**: Yuwei Miao, Yuzhi Guo, Hehuan Ma, Jingquan Yan, Feng Jiang, Weizhi An, Jean Gao, Junzhou Huang

**Updated**: 2024-12-17T09:08:52Z

**Summary**: Gene studies are crucial for fields such as protein structure prediction, drug discovery, and cancer genomics, yet they face challenges in fully utilizing the vast and diverse information available. Gene studies require clean, factual datasets to ensure reliable results. Ontology graphs, neatly organized domain terminology graphs, provide ideal sources for domain facts. However, available gene ontology annotations are currently distributed across various databases without unified identifiers for genes and gene products. To address these challenges, we introduce Unified Entrez Gene Identifier Dataset and Benchmarks (UniEntrezDB), the first systematic effort to unify large-scale public Gene Ontology Annotations (GOA) from various databases using unique gene identifiers. UniEntrezDB includes a pre-training dataset and four downstream tasks designed to comprehensively evaluate gene embedding performance from gene, protein, and cell levels, ultimately enhancing the reliability and applicability of LLMs in gene research and other professional settings.

**Link**: [arxiv](http://arxiv.org/abs/2412.12688v1),  [pdf](http://arxiv.org/pdf/2412.12688v1)

**Tags**: cs.DB 



### Uncertainty-Aware Hybrid Inference with On-Device Small and Remote Large   Language Models
**Authors**: Seungeun Oh, Jinhyuk Kim, Jihong Park, Seung-Woo Ko, Tony Q. S. Quek, Seong-Lyun Kim

**Updated**: 2024-12-17T09:08:18Z

**Summary**: This paper studies a hybrid language model (HLM) architecture that integrates a small language model (SLM) operating on a mobile device with a large language model (LLM) hosted at the base station (BS) of a wireless network. The HLM token generation process follows the speculative inference principle: the SLM's vocabulary distribution is uploaded to the LLM, which either accepts or rejects it, with rejected tokens being resampled by the LLM. While this approach ensures alignment between the vocabulary distributions of the SLM and LLM, it suffers from low token throughput due to uplink transmission and the computation costs of running both language models. To address this, we propose a novel HLM structure coined Uncertainty-aware HLM (U-HLM), wherein the SLM locally measures its output uncertainty, and skips both uplink transmissions and LLM operations for tokens that are likely to be accepted. This opportunistic skipping is enabled by our empirical finding of a linear correlation between the SLM's uncertainty and the LLM's rejection probability. We analytically derive the uncertainty threshold and evaluate its expected risk of rejection. Simulations show that U-HLM reduces uplink transmissions and LLM computation by 45.93%, while achieving up to 97.54% of the LLM's inference accuracy and 2.54$\times$ faster token throughput than HLM without skipping.

**Link**: [arxiv](http://arxiv.org/abs/2412.12687v1),  [pdf](http://arxiv.org/pdf/2412.12687v1)

**Tags**: cs.LG cs.DC cs.IT cs.NI eess.SP math.IT 



### XTransplant: A Probe into the Upper Bound Performance of Multilingual   Capability and Culture Adaptability in LLMs via Mutual Cross-lingual   Feed-forward Transplantation
**Authors**: Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Libo Qin, Yichong Huang, Lei Huang, Weitao Ma, Zhirui Zhang, Yunfei Lu, Xiaohui Yan, Duyu Tang, Dandan Tu, Bing Qin

**Updated**: 2024-12-17T09:05:30Z

**Summary**: Current large language models (LLMs) often exhibit imbalances in multilingual capabilities and cultural adaptability, largely due to their English-centric pretraining data. To address this imbalance, we propose a probing method named XTransplant that explores cross-lingual latent interactions via cross-lingual feed-forward transplantation during inference stage, with the hope of enabling the model to leverage the strengths of both English and non-English languages. Through extensive pilot experiments, we empirically prove that both the multilingual capabilities and cultural adaptability of LLMs hold the potential to be significantly improved by XTransplant, respectively from En -> non-En and non-En -> En, highlighting the underutilization of current LLMs' multilingual potential. And the patterns observed in these pilot experiments further motivate an offline scaling inference strategy, which demonstrates consistent performance improvements in multilingual and culture-aware tasks, sometimes even surpassing multilingual supervised fine-tuning. And we do hope our further analysis and discussion could help gain deeper insights into XTransplant mechanism.

**Link**: [arxiv](http://arxiv.org/abs/2412.12686v1),  [pdf](http://arxiv.org/pdf/2412.12686v1)

**Tags**: cs.CL 



### Detecting Document-level Paraphrased Machine Generated Content:   Mimicking Human Writing Style and Involving Discourse Features
**Authors**: Yupei Li, Manuel Milling, Lucia Specia, Björn W. Schuller

**Updated**: 2024-12-17T08:47:41Z

**Summary**: The availability of high-quality APIs for Large Language Models (LLMs) has facilitated the widespread creation of Machine-Generated Content (MGC), posing challenges such as academic plagiarism and the spread of misinformation. Existing MGC detectors often focus solely on surface-level information, overlooking implicit and structural features. This makes them susceptible to deception by surface-level sentence patterns, particularly for longer texts and in texts that have been subsequently paraphrased.   To overcome these challenges, we introduce novel methodologies and datasets. Besides the publicly available dataset Plagbench, we developed the paraphrased Long-Form Question and Answer (paraLFQA) and paraphrased Writing Prompts (paraWP) datasets using GPT and DIPPER, a discourse paraphrasing tool, by extending artifacts from their original versions. To address the challenge of detecting highly similar paraphrased texts, we propose MhBART, an encoder-decoder model designed to emulate human writing style while incorporating a novel difference score mechanism. This model outperforms strong classifier baselines and identifies deceptive sentence patterns. To better capture the structure of longer texts at document level, we propose DTransformer, a model that integrates discourse analysis through PDTB preprocessing to encode structural features. It results in substantial performance gains across both datasets -- 15.5\% absolute improvement on paraLFQA, 4\% absolute improvement on paraWP, and 1.5\% absolute improvement on M4 compared to SOTA approaches.

**Link**: [arxiv](http://arxiv.org/abs/2412.12679v1),  [pdf](http://arxiv.org/pdf/2412.12679v1)

**Tags**: cs.CL 



### Train More Parameters But Mind Their Placement: Insights into Language   Adaptation with PEFT
**Authors**: Jenny Kunz

**Updated**: 2024-12-17T08:44:00Z

**Summary**: Smaller LLMs still face significant challenges even in medium-resourced languages, particularly when it comes to language-specific knowledge -- a problem not easily resolved with machine-translated data. In this case study on Icelandic, we aim to enhance the generation performance of an LLM by specialising it using unstructured text corpora. A key focus is on preventing interference with the models' capabilities of handling longer context during this adaptation. Through ablation studies using various parameter-efficient fine-tuning (PEFT) methods and setups, we find that increasing the number of trainable parameters leads to better and more robust language adaptation. LoRAs placed in the feed-forward layers and bottleneck adapters show promising results with sufficient parameters, while prefix tuning and (IA)3 are not suitable. Although improvements are consistent in 0-shot summarisation, some adapted models struggle with longer context lengths, an issue that can be mitigated by adapting only the final layers.

**Link**: [arxiv](http://arxiv.org/abs/2412.12674v1),  [pdf](http://arxiv.org/pdf/2412.12674v1)

**Tags**: cs.CL 



### Citekit: A Modular Toolkit for Large Language Model Citation Generation
**Authors**: Jiajun Shen, Tong Zhou, Yubo Chen, Kang Liu

**Updated**: 2024-12-17T08:37:34Z

**Summary**: Enabling Large Language Models (LLMs) to generate citations in Question-Answering (QA) tasks is an emerging paradigm aimed at enhancing the verifiability of their responses when LLMs are utilizing external references to generate an answer. However, there is currently no unified framework to standardize and fairly compare different citation generation methods, leading to difficulties in reproducing different methods and a comprehensive assessment. To cope with the problems above, we introduce \name, an open-source and modular toolkit designed to facilitate the implementation and evaluation of existing citation generation methods, while also fostering the development of new approaches to improve citation quality in LLM outputs. This tool is highly extensible, allowing users to utilize 4 main modules and 14 components to construct a pipeline, evaluating an existing method or innovative designs. Our experiments with two state-of-the-art LLMs and 11 citation generation baselines demonstrate varying strengths of different modules in answer accuracy and citation quality improvement, as well as the challenge of enhancing granularity. Based on our analysis of the effectiveness of components, we propose a new method, self-RAG \snippet, obtaining a balanced answer accuracy and citation quality. Citekit is released at https://github.com/SjJ1017/Citekit.

**Link**: [arxiv](http://arxiv.org/abs/2408.04662v2),  [pdf](http://arxiv.org/pdf/2408.04662v2)

**Tags**: cs.CL cs.AI 



### Predicting User Behavior in Smart Spaces with LLM-Enhanced Logs and   Personalized Prompts (Data Description)
**Authors**: Yunpeng Song

**Updated**: 2024-12-17T08:20:56Z

**Summary**: Enhancing the intelligence of smart systems, such as smart home, and smart vehicle, and smart grids, critically depends on developing sophisticated planning capabilities that can anticipate the next desired function based on historical interactions. While existing methods view user behaviors as sequential data and apply models like RNNs and Transformers to predict future actions, they often fail to incorporate domain knowledge and capture personalized user preferences. In this paper, we propose a novel approach that incorporates LLM-enhanced logs and personalized prompts. Our approach first constructs a graph that captures individual behavior preferences derived from their interaction histories. This graph effectively transforms into a soft continuous prompt that precedes the sequence of user behaviors. Then our approach leverages the vast general knowledge and robust reasoning capabilities of a pretrained LLM to enrich the oversimplified and incomplete log records. By enhancing these logs semantically, our approach better understands the user's actions and intentions, especially for those rare events in the dataset. We evaluate the method across four real-world datasets from both smart vehicle and smart home settings. The findings validate the effectiveness of our LLM-enhanced description and personalized prompt, shedding light on potential ways to advance the intelligence of smart space. Note: While this manuscript provides description of the data, we are \textbf{not} permitted to make these datasets publicly available due to restrictions imposed by the data provider.

**Link**: [arxiv](http://arxiv.org/abs/2412.12653v1),  [pdf](http://arxiv.org/pdf/2412.12653v1)

**Tags**: cs.HC 



### LLM-based Discriminative Reasoning for Knowledge Graph Question   Answering
**Authors**: Mufan Xu, Kehai Chen, Xuefeng Bai, Muyun Yang, Tiejun Zhao, Min Zhang

**Updated**: 2024-12-17T08:07:16Z

**Summary**: Large language models (LLMs) based on generative pre-trained Transformer have achieved remarkable performance on knowledge graph question-answering (KGQA) tasks. However, LLMs often produce ungrounded subgraph planning or reasoning results in KGQA due to the hallucinatory behavior brought by the generative paradigm, which may hinder the advancement of the LLM-based KGQA model. To deal with the issue, we propose a novel LLM-based Discriminative Reasoning (LDR) method to explicitly model the subgraph retrieval and answer inference process. By adopting discriminative strategies, the proposed LDR method not only enhances the capability of LLMs to retrieve question-related subgraphs but also alleviates the issue of ungrounded reasoning brought by the generative paradigm of LLMs. Experimental results show that the proposed approach outperforms multiple strong comparison methods, along with achieving state-of-the-art performance on two widely used WebQSP and CWQ benchmarks.

**Link**: [arxiv](http://arxiv.org/abs/2412.12643v1),  [pdf](http://arxiv.org/pdf/2412.12643v1)

**Tags**: cs.CL 



### $C^2$: Scalable Auto-Feedback for LLM-based Chart Generation
**Authors**: Woosung Koh, Jang Han Yoon, MinHyung Lee, Youngjin Song, Jaegwan Cho, Jaehyun Kang, Taehyeon Kim, Se-young Yun, Youngjae Yu, Bongshin Lee

**Updated**: 2024-12-17T08:03:10Z

**Summary**: Generating high-quality charts with Large Language Models (LLMs) presents significant challenges due to limited data and the high cost of scaling through human curation. $\langle \text{instruction}, \text{data}, \text{code} \rangle$ triplets are scarce and expensive to manually curate as their creation demands technical expertise. To address this scalability challenge, we introduce a reference-free automatic feedback generator, which eliminates the need for costly human intervention. Our novel framework, C$^2$, consists of (1) an automatic feedback provider (ChartAF) and (2) a diverse, reference-free dataset (ChartUIE-8K). The results are compelling: in our first experiment, 74% of respondents strongly preferred, and 10% preferred, the results after feedback. The second post-feedback experiment demonstrates that ChartAF outperform nine baselines. Moreover, ChartUIE-8K significantly improves data diversity by increasing queries, datasets, and chart types by 5982%, 1936%, and 91%, respectively, over benchmarks. Finally, a study of LLM users revealed that 94% of participants preferred ChartUIE-8K's queries, with 93% deeming them aligned with real-world use cases. Core contributions are available as open-source at chartsquared.github.io, with ample qualitative examples.

**Link**: [arxiv](http://arxiv.org/abs/2410.18652v4),  [pdf](http://arxiv.org/pdf/2410.18652v4)

**Tags**: cs.LG cs.AI cs.CL 



### Falcon: Faster and Parallel Inference of Large Language Models through   Enhanced Semi-Autoregressive Drafting and Custom-Designed Decoding Tree
**Authors**: Xiangxiang Gao, Weisheng Xie, Yiwei Xiang, Feng Ji

**Updated**: 2024-12-17T08:02:08Z

**Summary**: Striking an optimal balance between minimal drafting latency and high speculation accuracy to enhance the inference speed of Large Language Models remains a significant challenge in speculative decoding. In this paper, we introduce Falcon, an innovative semi-autoregressive speculative decoding framework fashioned to augment both the drafter's parallelism and output quality. Falcon incorporates the Coupled Sequential Glancing Distillation technique, which fortifies inter-token dependencies within the same block, leading to increased speculation accuracy. We offer a comprehensive theoretical analysis to illuminate the underlying mechanisms. Additionally, we introduce a Custom-Designed Decoding Tree, which permits the drafter to generate multiple tokens in a single forward pass and accommodates multiple forward passes as needed, thereby boosting the number of drafted tokens and significantly improving the overall acceptance rate. Comprehensive evaluations on benchmark datasets such as MT-Bench, HumanEval, and GSM8K demonstrate Falcon's superior acceleration capabilities. The framework achieves a lossless speedup ratio ranging from 2.91x to 3.51x when tested on the Vicuna and LLaMA2-Chat model series. These results outstrip existing speculative decoding methods for LLMs, including Eagle, Medusa, Lookahead, SPS, and PLD, while maintaining a compact drafter architecture equivalent to merely two Transformer layers.

**Link**: [arxiv](http://arxiv.org/abs/2412.12639v1),  [pdf](http://arxiv.org/pdf/2412.12639v1)

**Tags**: cs.CL cs.AI 



### What External Knowledge is Preferred by LLMs? Characterizing and   Exploring Chain of Evidence in Imperfect Context
**Authors**: Zhiyuan Chang, Mingyang Li, Xiaojun Jia, Junjie Wang, Yuekai Huang, Qing Wang, Yihao Huang, Yang Liu

**Updated**: 2024-12-17T07:49:49Z

**Summary**: Incorporating external knowledge into large language models (LLMs) has emerged as a promising approach to mitigate outdated knowledge and hallucination in LLMs. However, external knowledge is often imperfect. In addition to useful knowledge, external knowledge is rich in irrelevant or misinformation in the context that can impair the reliability of LLM responses. This paper focuses on LLMs' preferred external knowledge in imperfect contexts when handling multi-hop QA. Inspired by criminal procedural law's Chain of Evidence (CoE), we characterize that knowledge preferred by LLMs should maintain both relevance to the question and mutual support among knowledge pieces. Accordingly, we propose an automated CoE discrimination approach and explore LLMs' preferences from their effectiveness, faithfulness and robustness, as well as CoE's usability in a naive Retrieval-Augmented Generation (RAG) case. The evaluation on five LLMs reveals that CoE enhances LLMs through more accurate generation, stronger answer faithfulness, better robustness against knowledge conflict, and improved performance in a popular RAG case.

**Link**: [arxiv](http://arxiv.org/abs/2412.12632v1),  [pdf](http://arxiv.org/pdf/2412.12632v1)

**Tags**: cs.CL cs.AI 



### Jailbreaking? One Step Is Enough!
**Authors**: Weixiong Zheng, Peijian Zeng, Yiwei Li, Hongyan Wu, Nankai Lin, Junhao Chen, Aimin Yang, Yongmei Zhou

**Updated**: 2024-12-17T07:33:41Z

**Summary**: Large language models (LLMs) excel in various tasks but remain vulnerable to jailbreak attacks, where adversaries manipulate prompts to generate harmful outputs. Examining jailbreak prompts helps uncover the shortcomings of LLMs. However, current jailbreak methods and the target model's defenses are engaged in an independent and adversarial process, resulting in the need for frequent attack iterations and redesigning attacks for different models. To address these gaps, we propose a Reverse Embedded Defense Attack (REDA) mechanism that disguises the attack intention as the "defense". intention against harmful content. Specifically, REDA starts from the target response, guiding the model to embed harmful content within its defensive measures, thereby relegating harmful content to a secondary role and making the model believe it is performing a defensive task. The attacking model considers that it is guiding the target model to deal with harmful content, while the target model thinks it is performing a defensive task, creating an illusion of cooperation between the two. Additionally, to enhance the model's confidence and guidance in "defensive" intentions, we adopt in-context learning (ICL) with a small number of attack examples and construct a corresponding dataset of attack examples. Extensive evaluations demonstrate that the REDA method enables cross-model attacks without the need to redesign attack strategies for different models, enables successful jailbreak in one iteration, and outperforms existing methods on both open-source and closed-source models.

**Link**: [arxiv](http://arxiv.org/abs/2412.12621v1),  [pdf](http://arxiv.org/pdf/2412.12621v1)

**Tags**: cs.CL 



### I-SHEEP: Self-Alignment of LLM from Scratch through an Iterative   Self-Enhancement Paradigm
**Authors**: Yiming Liang, Ge Zhang, Xingwei Qu, Tianyu Zheng, Jiawei Guo, Xinrun Du, Zhenzhu Yang, Jiaheng Liu, Chenghua Lin, Lei Ma, Wenhao Huang, Jiajun Zhang

**Updated**: 2024-12-17T07:30:54Z

**Summary**: Large Language Models (LLMs) have achieved significant advancements, however, the common learning paradigm treats LLMs as passive information repositories, neglecting their potential for active learning and alignment. Some approaches train LLMs using their own generated synthetic data, exploring the possibility of active alignment. However, there is still a huge gap between these one-time alignment methods and the continuous automatic alignment of humans. In this paper, we introduce \textbf{I-SHEEP}, an \textbf{I}terative \textbf{S}elf-En\textbf{H}anc\textbf{E}m\textbf{E}nt \textbf{P}aradigm.This human-like paradigm enables LLMs to \textbf{continuously self-align from scratch with nothing}. Compared to the one-time alignment method Dromedary \cite{sun2023principledriven}, which refers to the first iteration in this paper, I-SHEEP can significantly enhance capacities on both Qwen and Llama models. I-SHEEP achieves a maximum relative improvement of 78.2\% in the Alpaca Eval, 24.0\% in the MT Bench, and an absolute increase of 8.88\% in the IFEval accuracy over subsequent iterations in Qwen-1.5 72B model. Additionally, I-SHEEP surpasses the base model in various standard benchmark generation tasks, achieving an average improvement of 24.77\% in code generation tasks, 12.04\% in TrivialQA, and 20.29\% in SQuAD. We also provide new insights based on the experiment results. Our codes, datasets, and models are available at \textbf{https://anonymous.4open.science/r/I-SHEEP}.

**Link**: [arxiv](http://arxiv.org/abs/2408.08072v3),  [pdf](http://arxiv.org/pdf/2408.08072v3)

**Tags**: cs.CL 



### Deep Learning and Machine Learning -- Natural Language Processing: From   Theory to Application
**Authors**: Keyu Chen, Cheng Fei, Ziqian Bi, Junyu Liu, Benji Peng, Sen Zhang, Xuanhe Pan, Jiawei Xu, Jinlang Wang, Caitlyn Heqi Yin, Yichao Zhang, Pohsun Feng, Yizhu Wen, Tianyang Wang, Ming Li, Jintao Ren, Qian Niu, Silin Chen, Weiche Hsieh, Lawrence K. Q. Yan, Chia Xin Liang, Han Xu, Hong-Ming Tseng, Xinyuan Song, Ming Liu

**Updated**: 2024-12-17T07:26:39Z

**Summary**: With a focus on natural language processing (NLP) and the role of large language models (LLMs), we explore the intersection of machine learning, deep learning, and artificial intelligence. As artificial intelligence continues to revolutionize fields from healthcare to finance, NLP techniques such as tokenization, text classification, and entity recognition are essential for processing and understanding human language. This paper discusses advanced data preprocessing techniques and the use of frameworks like Hugging Face for implementing transformer-based models. Additionally, it highlights challenges such as handling multilingual data, reducing bias, and ensuring model robustness. By addressing key aspects of data processing and model fine-tuning, this work aims to provide insights into deploying effective and ethically sound AI solutions.

**Link**: [arxiv](http://arxiv.org/abs/2411.05026v2),  [pdf](http://arxiv.org/pdf/2411.05026v2)

**Tags**: cs.CL cs.HC 



### SynthCypher: A Fully Synthetic Data Generation Framework for   Text-to-Cypher Querying in Knowledge Graphs
**Authors**: Aman Tiwari, Shiva Krishna Reddy Malay, Vikas Yadav, Masoud Hashemi, Sathwik Tejaswi Madhusudhan

**Updated**: 2024-12-17T07:21:25Z

**Summary**: Cypher, the query language for Neo4j graph databases, plays a critical role in enabling graph-based analytics and data exploration. While substantial research has been dedicated to natural language to SQL query generation (Text2SQL), the analogous problem for graph databases referred to as Text2Cypher remains underexplored. In this work, we introduce SynthCypher, a fully synthetic and automated data generation pipeline designed to address this gap. SynthCypher employs a novel LLMSupervised Generation-Verification framework, ensuring syntactically and semantically correct Cypher queries across diverse domains and query complexities. Using this pipeline, we create SynthCypher Dataset, a large-scale benchmark containing 29.8k Text2Cypher instances. Fine-tuning open-source large language models (LLMs), including LLaMa-3.1- 8B, Mistral-7B, and QWEN-7B, on SynthCypher yields significant performance improvements of up to 40% on the Text2Cypher test set and 30% on the SPIDER benchmark adapted for graph databases. This work demonstrates that high-quality synthetic data can effectively advance the state-of-the-art in Text2Cypher tasks.

**Link**: [arxiv](http://arxiv.org/abs/2412.12612v1),  [pdf](http://arxiv.org/pdf/2412.12612v1)

**Tags**: cs.CL cs.AI cs.IR cs.LG 



### Can Large Language Models Act as Ensembler for Multi-GNNs?
**Authors**: Hanqi Duan, Yao Cheng, Jianxiang Yu, Xiang Li

**Updated**: 2024-12-17T07:20:33Z

**Summary**: Graph Neural Networks (GNNs) have emerged as powerful models for learning from graph-structured data. However, GNNs lack the inherent semantic understanding capability of rich textual node attributes, limiting their effectiveness in applications. On the other hand, we empirically observe that for existing GNN models, no one can consistently outperforms others across diverse datasets. In this paper, we study whether LLMs can act as an ensembler for multi-GNNs and propose the LensGNN model. The model first aligns multiple GNNs, mapping the representations of different GNNs into the same space. Then, through LoRA fine-tuning, it aligns the space between the GNN and the LLM, injecting graph tokens and textual information into LLMs. This allows LensGNN to ensemble multiple GNNs and take advantage of the strengths of LLM, leading to a deeper understanding of both textual semantic information and graph structural information. The experimental results show that LensGNN outperforms existing models. This research advances text-attributed graph ensemble learning by providing a robust and superior solution for integrating semantic and structural information. We provide our code and data here: https://anonymous.4open.science/r/EnsemGNN-E267/.

**Link**: [arxiv](http://arxiv.org/abs/2410.16822v2),  [pdf](http://arxiv.org/pdf/2410.16822v2)

**Tags**: cs.AI 



### SEED: Accelerating Reasoning Tree Construction via Scheduled Speculative   Decoding
**Authors**: Zhenglin Wang, Jialong Wu, Yilong Lai, Congzhi Zhang, Deyu Zhou

**Updated**: 2024-12-17T07:18:53Z

**Summary**: Large Language Models (LLMs) demonstrate remarkable emergent abilities across various tasks, yet fall short of complex reasoning and planning tasks. The tree-search-based reasoning methods address this by surpassing the capabilities of chain-of-thought prompting, encouraging exploration of intermediate steps. However, such methods introduce significant inference latency due to the systematic exploration and evaluation of multiple thought paths. This paper introduces SeeD, a novel and efficient inference framework to optimize runtime speed and GPU memory management concurrently. By employing a scheduled speculative execution, SeeD efficiently handles multiple iterations for the thought generation and the state evaluation, leveraging a rounds-scheduled strategy to manage draft model dispatching. Extensive experimental evaluations on three reasoning datasets demonstrate superior speedup performance of SeeD, providing a viable path for batched inference in training-free speculative decoding.

**Link**: [arxiv](http://arxiv.org/abs/2406.18200v2),  [pdf](http://arxiv.org/pdf/2406.18200v2)

**Tags**: cs.CL 



### Can Large Language Models Address Open-Target Stance Detection?
**Authors**: Abu Ubaida Akash, Ahmed Fahmy, Amine Trabelsi

**Updated**: 2024-12-17T07:15:38Z

**Summary**: Stance detection (SD) identifies the text position towards a target, typically labeled as favor, against, or none. We introduce Open-Target Stance Detection (OTSD), the most realistic task where targets are neither seen during training nor provided as input. We evaluate Large Language Models (LLMs) from GPT, Gemini, Llama, and Mistral families, comparing their performance to the only existing work, Target-Stance Extraction (TSE), which benefits from predefined targets. Unlike TSE, OTSD removes the dependency of a predefined list, making target generation and evaluation more challenging. We also provide a metric for evaluating target quality that correlates well with human judgment. Our experiments reveal that LLMs outperform TSE in target generation, both when the real target is explicitly and not explicitly mentioned in the text. Similarly, LLMs overall surpass TSE in stance detection for both explicit and non-explicit cases. However, LLMs struggle in both target generation and stance detection when the target is not explicit.

**Link**: [arxiv](http://arxiv.org/abs/2409.00222v5),  [pdf](http://arxiv.org/pdf/2409.00222v5)

**Tags**: cs.CL 



### MultiLingPoT: Enhancing Mathematical Reasoning with Multilingual Program   Fine-tuning
**Authors**: Nianqi Li, Zujie Liang, Siyu Yuan, Jiaqing Liang, Feng Wei, Yanghua Xiao

**Updated**: 2024-12-17T07:14:03Z

**Summary**: Program-of-Thought (PoT), which aims to use programming language instead of natural language as an intermediate step in reasoning, is an important way for LLMs to solve mathematical problems. Since different programming languages excel in different areas, it is natural to use the most suitable language for solving specific problems. However, current PoT research only focuses on single language PoT, ignoring the differences between different programming languages. Therefore, this paper proposes an multilingual program reasoning method, MultiLingPoT. This method allows the model to answer questions using multiple programming languages by fine-tuning on multilingual data. Additionally, prior and posterior hybrid methods are used to help the model select the most suitable language for each problem. Our experimental results show that the training of MultiLingPoT improves each program's mathematical reasoning by about 2.5\%. Moreover, with proper mixing, the performance of MultiLingPoT can be further improved, achieving a 6\% increase compared to the single-language PoT with the data augmentation.Resources of this paper can be found at https://github.com/Nianqi-Li/MultiLingPoT.

**Link**: [arxiv](http://arxiv.org/abs/2412.12609v1),  [pdf](http://arxiv.org/pdf/2412.12609v1)

**Tags**: cs.CL 



### MMTrail: A Multimodal Trailer Video Dataset with Language and Music   Descriptions
**Authors**: Xiaowei Chi, Yatian Wang, Aosong Cheng, Pengjun Fang, Zeyue Tian, Yingqing He, Zhaoyang Liu, Xingqun Qi, Jiahao Pan, Rongyu Zhang, Mengfei Li, Ruibin Yuan, Yanbing Jiang, Wei Xue, Wenhan Luo, Qifeng Chen, Shanghang Zhang, Qifeng Liu, Yike Guo

**Updated**: 2024-12-17T07:13:38Z

**Summary**: Massive multi-modality datasets play a significant role in facilitating the success of large video-language models. However, current video-language datasets primarily provide text descriptions for visual frames, considering audio to be weakly related information. They usually overlook exploring the potential of inherent audio-visual correlation, leading to monotonous annotation within each modality instead of comprehensive and precise descriptions. Such ignorance results in the difficulty of multiple cross-modality studies. To fulfill this gap, we present MMTrail, a large-scale multi-modality video-language dataset incorporating more than 20M trailer clips with visual captions, and 2M high-quality clips with multimodal captions. Trailers preview full-length video works and integrate context, visual frames, and background music. In particular, the trailer has two main advantages: (1) the topics are diverse, and the content characters are of various types, e.g., film, news, and gaming. (2) the corresponding background music is custom-designed, making it more coherent with the visual context. Upon these insights, we propose a systemic captioning framework, achieving various modality annotations with more than 27.1k hours of trailer videos. Here, to ensure the caption retains music perspective while preserving the authority of visual context, we leverage the advanced LLM to merge all annotations adaptively. In this fashion, our MMtrail dataset potentially paves the path for fine-grained large multimodal-language model training. In experiments, we provide evaluation metrics and benchmark results on our dataset, demonstrating the high quality of our annotation and its effectiveness for model training.

**Link**: [arxiv](http://arxiv.org/abs/2407.20962v3),  [pdf](http://arxiv.org/pdf/2407.20962v3)

**Tags**: cs.CV cs.MM cs.SD eess.AS 



### Don't Yell at Your Robot: Physical Correction as the Collaborative   Interface for Language Model Powered Robots
**Authors**: Chuye Zhang, Yifei Simon Shao, Harshil Parekh, Junyao Shi, Pratik Chaudhari, Vijay Kumar, Nadia Figueroa

**Updated**: 2024-12-17T06:59:29Z

**Summary**: We present a novel approach for enhancing human-robot collaboration using physical interactions for real-time error correction of large language model (LLM) powered robots. Unlike other methods that rely on verbal or text commands, the robot leverages an LLM to proactively executes 6 DoF linear Dynamical System (DS) commands using a description of the scene in natural language. During motion, a human can provide physical corrections, used to re-estimate the desired intention, also parameterized by linear DS. This corrected DS can be converted to natural language and used as part of the prompt to improve future LLM interactions. We provide proof-of-concept result in a hybrid real+sim experiment, showcasing physical interaction as a new possibility for LLM powered human-robot interface.

**Link**: [arxiv](http://arxiv.org/abs/2412.12602v1),  [pdf](http://arxiv.org/pdf/2412.12602v1)

**Tags**: cs.RO cs.HC 



### Not All Votes Count! Programs as Verifiers Improve Self-Consistency of   Language Models for Math Reasoning
**Authors**: Vernon Y. H. Toh, Deepanway Ghosal, Soujanya Poria

**Updated**: 2024-12-17T06:55:00Z

**Summary**: Large language models (LLMs) have shown increasing competence in solving mathematical reasoning problems. However, many open-source LLMs still struggle with errors in calculation and semantic understanding during intermediate reasoning steps. In this work, we introduce Prove, a simple yet effective framework that leverages translated programs derived from natural language solutions as a verification mechanism to filter out potentially incorrect reasoning paths before aggregating final answers. Unlike vanilla majority voting, our approach filters out solutions whose corresponding program output is inconsistent with the generated solution, aggregating only those that pass verification. We conducted extensive experiments using 13 open-source LLMs from various model families and sizes, ranging from 0.5B to 13B parameters, across eight mathematical benchmarks. Our results show that Prove consistently outperforms vanilla majority voting as a heuristic for solving mathematical reasoning tasks across all model sizes and datasets, achieving improvements of up to 18% on GSM8K and 8% on MATH-500. Our codes are available at https://github.com/declare-lab/prove.

**Link**: [arxiv](http://arxiv.org/abs/2410.12608v2),  [pdf](http://arxiv.org/pdf/2410.12608v2)

**Tags**: cs.CL 



### DreamRunner: Fine-Grained Storytelling Video Generation with   Retrieval-Augmented Motion Adaptation
**Authors**: Zun Wang, Jialu Li, Han Lin, Jaehong Yoon, Mohit Bansal

**Updated**: 2024-12-17T06:52:46Z

**Summary**: Storytelling video generation (SVG) has recently emerged as a task to create long, multi-motion, multi-scene videos that consistently represent the story described in the input text script. SVG holds great potential for diverse content creation in media and entertainment; however, it also presents significant challenges: (1) objects must exhibit a range of fine-grained, complex motions, (2) multiple objects need to appear consistently across scenes, and (3) subjects may require multiple motions with seamless transitions within a single scene. To address these challenges, we propose DreamRunner, a novel story-to-video generation method: First, we structure the input script using a large language model (LLM) to facilitate both coarse-grained scene planning as well as fine-grained object-level layout and motion planning. Next, DreamRunner presents retrieval-augmented test-time adaptation to capture target motion priors for objects in each scene, supporting diverse motion customization based on retrieved videos, thus facilitating the generation of new videos with complex, scripted motions. Lastly, we propose a novel spatial-temporal region-based 3D attention and prior injection module SR3AI for fine-grained object-motion binding and frame-by-frame semantic control. We compare DreamRunner with various SVG baselines, demonstrating state-of-the-art performance in character consistency, text alignment, and smooth transitions. Additionally, DreamRunner exhibits strong fine-grained condition-following ability in compositional text-to-video generation, significantly outperforming baselines on T2V-ComBench. Finally, we validate DreamRunner's robust ability to generate multi-object interactions with qualitative examples.

**Link**: [arxiv](http://arxiv.org/abs/2411.16657v2),  [pdf](http://arxiv.org/pdf/2411.16657v2)

**Tags**: cs.CV cs.AI cs.CL 



### Asymmetric protocols for mode pairing quantum key distribution with   finite-key analysis
**Authors**: Zhenhua Li, Tianqi Dou, Yuheng Xie, Weiwen Kong, Yang Liu, Haiqiang Ma, Jianjun Tang

**Updated**: 2024-12-17T06:50:15Z

**Summary**: The mode pairing quantum key distribution (MP-QKD) protocol has attracted considerable attention for its capability to ensure high secure key rates over long distances without requiring global phase locking. However, ensuring symmetric channels for the MP-QKD protocol is challenging in practical quantum communication networks. Previous studies on the asymmetric MP-QKD protocol have relied on ideal decoy state assumptions and infinite-key analysis, which are unattainable for real-world deployment. In this paper, we conduct a security analysis of asymmetric MP-QKD protocol with the finite-key analysis, where we discard the previously impractical assumptions made in the decoy-state method. Combined with statistical fluctuation analysis, we globally optimized the 12 independent parameters in the asymmetric MP-QKD protocol by employing our modified particle swarm optimization. The simulation results demonstrate that our work can achieve significantly enhanced secure key rates and transmission distances compared to the original strategy with adding extra attenuation. We further investigate the relationship between the intensities and probabilities of signal, decoy, and vacuum states with transmission distance, facilitating its more efficient deployment in future quantum networks.

**Link**: [arxiv](http://arxiv.org/abs/2412.12593v1),  [pdf](http://arxiv.org/pdf/2412.12593v1)

**Tags**: quant-ph 



### LLMs are Also Effective Embedding Models: An In-depth Overview
**Authors**: Chongyang Tao, Tao Shen, Shen Gao, Junshuo Zhang, Zhen Li, Zhengwei Tao, Shuai Ma

**Updated**: 2024-12-17T06:48:24Z

**Summary**: Large language models (LLMs) have revolutionized natural language processing by achieving state-of-the-art performance across various tasks. Recently, their effectiveness as embedding models has gained attention, marking a paradigm shift from traditional encoder-only models like ELMo and BERT to decoder-only, large-scale LLMs such as GPT, LLaMA, and Mistral. This survey provides an in-depth overview of this transition, beginning with foundational techniques before the LLM era, followed by LLM-based embedding models through two main strategies to derive embeddings from LLMs. 1) Direct prompting: We mainly discuss the prompt designs and the underlying rationale for deriving competitive embeddings. 2) Data-centric tuning: We cover extensive aspects that affect tuning an embedding model, including model architecture, training objectives, data constructions, etc. Upon the above, we also cover advanced methods, such as handling longer texts, and multilingual and cross-modal data. Furthermore, we discuss factors affecting choices of embedding models, such as performance/efficiency comparisons, dense vs sparse embeddings, pooling strategies, and scaling law. Lastly, the survey highlights the limitations and challenges in adapting LLMs for embeddings, including cross-task embedding quality, trade-offs between efficiency and accuracy, low-resource, long-context, data bias, robustness, etc. This survey serves as a valuable resource for researchers and practitioners by synthesizing current advancements, highlighting key challenges, and offering a comprehensive framework for future work aimed at enhancing the effectiveness and efficiency of LLMs as embedding models.

**Link**: [arxiv](http://arxiv.org/abs/2412.12591v1),  [pdf](http://arxiv.org/pdf/2412.12591v1)

**Tags**: cs.CL 



### Large Language Model-Brained GUI Agents: A Survey
**Authors**: Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang

**Updated**: 2024-12-17T06:35:56Z

**Summary**: GUIs have long been central to human-computer interaction, providing an intuitive and visually-driven way to access and interact with digital systems. The advent of LLMs, particularly multimodal models, has ushered in a new era of GUI automation. They have demonstrated exceptional capabilities in natural language understanding, code generation, and visual processing. This has paved the way for a new generation of LLM-brained GUI agents capable of interpreting complex GUI elements and autonomously executing actions based on natural language instructions. These agents represent a paradigm shift, enabling users to perform intricate, multi-step tasks through simple conversational commands. Their applications span across web navigation, mobile app interactions, and desktop automation, offering a transformative user experience that revolutionizes how individuals interact with software. This emerging field is rapidly advancing, with significant progress in both research and industry.   To provide a structured understanding of this trend, this paper presents a comprehensive survey of LLM-brained GUI agents, exploring their historical evolution, core components, and advanced techniques. We address research questions such as existing GUI agent frameworks, the collection and utilization of data for training specialized GUI agents, the development of large action models tailored for GUI tasks, and the evaluation metrics and benchmarks necessary to assess their effectiveness. Additionally, we examine emerging applications powered by these agents. Through a detailed analysis, this survey identifies key research gaps and outlines a roadmap for future advancements in the field. By consolidating foundational knowledge and state-of-the-art developments, this work aims to guide both researchers and practitioners in overcoming challenges and unlocking the full potential of LLM-brained GUI agents.

**Link**: [arxiv](http://arxiv.org/abs/2411.18279v4),  [pdf](http://arxiv.org/pdf/2411.18279v4)

**Tags**: cs.AI cs.CL cs.HC 



