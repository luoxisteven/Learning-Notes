# LLM

## 大模型的大，体现在：
1) `可以完成的任务多:` 无论是文本翻译，情感分析，文本分类等问题，大模型都可以胜任。
2) `模型体量和参数大:` 为了能够完成各种NLP任务，大模型的体量必须足够大，从而有更大的模型空间去映射各类任务。

## LLM时如何训练出来的?
1. `Pre-training (预训练)`
    - LLM模型特别是GPT模型是通过叠加多个Transformer的Decoder-only模型，预训练阶段通过语言模型Language Modeling进行自监督学习。语言模型就是通过前面的词去预测下一个词是什么。
2. `Supervised Fine-tuning (SFT) 有监督微调`
    - 有监督微调是让大模型对各类任务进行微调，比如SQuAD（问答）、GLUE（自然语言理解）、MS MARCO（信息检索等），也会用一些人工标注对模型进行微调。SFT的目的在于对各类任务都有一个泛化的优秀表现。
3. `Reinforcement Learning with Human Feedback (RLHF) 基于人类反馈的强化学习`
    - 通过预训练和SFT训练出来的模型，通过RLHF进行优化。首先，收集人类的反馈，让人类对大语言模型的输出结果进行排序打分；接着，通过`“奖励模型（Reward Model)”`给符合人类期望的文本给一个奖励分数；最后，这个强化学习的优化算法为`"近端策略优化(Proximal Policy Optimization)"`。
