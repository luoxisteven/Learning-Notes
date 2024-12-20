# LLM (Large Language Model)

## Why is it "Large"?

1) **Ability to Perform Multiple Tasks**:  
   Large Language Models can handle a wide range of tasks, such as text translation, sentiment analysis, text classification, and more.

2) **Model Size and Parameters**:  
   To effectively perform various NLP tasks, LLMs must have a sufficiently large scale, providing greater model capacity to map diverse tasks.

---

## How is an LLM Trained?

### 1. **Pre-training**
   - LLMs, particularly GPT models, are based on a stacked Transformer architecture, specifically a **Decoder-only model**.
   - During pre-training, the model is trained using **Language Modeling** for self-supervised learning. The model predicts the next word based on the preceding words.

### 2. **Supervised Fine-tuning (SFT)**
   - SFT fine-tunes the model on various tasks, such as **SQuAD** (question answering), **GLUE** (natural language understanding), and **MS MARCO** (information retrieval).  
   - Additionally, annotated data is used for further tuning. The goal of SFT is to enable the model to generalize well across a wide range of tasks.

### 3. **Reinforcement Learning with Human Feedback (RLHF)**
   - After pre-training and SFT, RLHF is used to optimize the model.  
   - **Steps in RLHF**:
     1. Collect human feedback where humans rank the outputs of the language model.
     2. Use this feedback to train a **Reward Model (RM)** that assigns reward scores to outputs aligning with human preferences.
     3. Optimize the model using **Proximal Policy Optimization (PPO)**, a reinforcement learning algorithm.
