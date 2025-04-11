## 🧠 Unsupervised Learning Examples

Unsupervised learning models find patterns in data **without labeled outputs**. Here are some common types and examples:

---

### 📌 1. Clustering
**Algorithm:** `K-Means`  
**Goal:** Group similar data points into clusters.

**Example:**  
Given height and weight of 100 people, K-Means can discover two natural groups:
- Athletes (tall and lean)
- Non-athletes (shorter and heavier)

---

### 📌 2. Dimensionality Reduction
**Algorithm:** `PCA` (Principal Component Analysis)  
**Goal:** Reduce the number of features while preserving important structure.

**Example:**  
Convert high-resolution face images (e.g., 1000×1000 pixels) into 50-dimensional vectors while keeping the identity distinguishable.

---

### 📌 3. Generative Models
**Algorithms:** 
- `Autoencoders`
- `GANs` (Generative Adversarial Networks)

**Goal:** Learn the data distribution and generate new, similar data.

**Example:**
Train a GAN on handwritten digits (MNIST) to generate new, realistic digit images.

---

### 📌 4. Independent Component Analysis (ICA)
**Goal:** Separate hidden sources from mixed data.

**Example:**  
In a room with multiple people speaking simultaneously, ICA can separate individual voices from the mixed microphone recordings.

---
# Chapter 1: Introduction

## 1.1 The Promise and Challenges of Deep Learning

Deep learning is a transformative technology, with potential applications in:
- Healthcare
- Education
- Design
- Transportation
- Entertainment
- Commerce

But it also comes with significant challenges, including:
- Misuse and harmful deployment
- Ethical and social concerns
- Lack of full understanding of how deep networks work

---

## 1.2 Two Examples of Reinforcement Learning

### Example 1: Humanoid Robot Locomotion
- The robot learns to navigate through an obstacle course.
- Rewards are given for reaching checkpoints.
- **Temporal credit assignment**: difficult to identify which actions were responsible for receiving a reward.

### Example 2: Learning to Play Chess
- Agent selects from legal chess moves.
- Rewards may come only at the end (win/loss).
- **Exploration-exploitation dilemma**: 
  - Should the agent stick to a known good strategy or try new (possibly better) moves?

**Policy networks** (deep neural networks) can be used to:
- Map observations to actions.
- Learn policies in both robot locomotion and chess scenarios.

---

## 1.3 Ethics

### Major Concerns

1. **Bias and Fairness**
   - AI can replicate historical biases from training data.
   - Examples: gender pay prediction, racial bias in face generation.

2. **Explainability**
   - Deep models are often black boxes.
   - Local explanations exist, but full transparency remains difficult.

3. **Weaponizing AI**
   - AI is already being used in military contexts.

4. **Concentrating Power**
   - Large tech companies may benefit disproportionately.
   - Automation might harm low-skill job markets.

5. **Existential Risk**
   - Similar to climate change or nuclear weapons.
   - Uncontrolled AI systems could become dangerous.

### Additional Risks
- Surveillance
- Disinformation
- Privacy violations
- Financial manipulation
- Energy consumption (climate impact)

**Reflection Points for Readers:**
- Scientists’ responsibility for the consequences of their work.
- Corporate values: ethics-washing vs real accountability.
- Importance of informed participation and activism.

**Suggested Resource:**
- [Ethics of AI Online Course](https://ethics-of-ai.mooc.fi/)

---

## 1.4 Structure of the Book

- **Chapters 2–9**: Supervised learning
  - Neural networks, training, performance evaluation
- **Chapters 10–13**: Network architectures
  - CNNs, residual connections, transformers
- **Chapters 14–18**: Unsupervised learning
  - GANs, VAEs, normalizing flows, diffusion models
- **Chapter 19**: Introduction to deep reinforcement learning
- **Chapter 20**: Open questions
  - Why deep nets generalize, trainability, double descent, grokking
- **Chapter 21**: Ethics (expanded)

---

## 1.5 How to Use This Book

- Each chapter includes:
  - **Main body of text**
  - **Notes section** (historical context, references)
  - **Problems** (marked with `*` if answers are online)
  - **Python notebooks** (linked in the margins)

- Background math is included where necessary.
- More detailed math is referenced in **Appendix 22**.
- Visualizations and diagrams are extensively used.

**Philosophy:**
- Don’t just read — engage with exercises!
- Book evolves with research; feedback is welcome via [udlbook.com](http://udlbook.com)

---

## Suggested Complementary Resources

- **Deep Learning** (Goodfellow et al., 2016)
- **Probabilistic Machine Learning** (Murphy, 2022/2023)
- **Pattern Recognition and Machine Learning** (Bishop, 2006)
- **Computer Vision: Models, Learning, and Inference** (Prince, 2012)
- **Probabilistic Graphical Models** (Koller & Friedman, 2009)
- **Gaussian Processes for ML** (Williams & Rasmussen, 2006)
- **Mathematics for Machine Learning** (Deisenroth et al., 2020)
- **Dive into Deep Learning** (Zhang et al., 2023)
- **Computer Vision** (Szeliski, 2022; Torralba et al., 2024)
- **Graph Representation Learning** (Hamilton, 2020)
- **Reinforcement Learning: An Introduction** (Sutton & Barto, 2018)
- **Foundations of Deep RL** (Graesser & Keng, 2019)
