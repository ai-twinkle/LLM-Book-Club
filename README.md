# Twinkle AI 熬夜書坊 - LLM 讀書會資源庫

![TwinkleAI Reading Club Banner](Hands-On-Large-Language-Models/images/TwinkleAI-Reading-Club-v2.png)

歡迎來到 **Twinkle AI 熬夜書坊 (Late-Night Study Session)** 的專屬 GitHub Repository！

本專案旨在存放我們線上讀書會的所有開源資源，包含簡報、討論筆記以及可執行的 Jupyter Notebooks。目前我們正在共讀由 Jay Alammar 與 Maarten Grootendorst 共同撰寫的重量級大作——**《LLM 語意理解與生成技術 完全開發》 (Hands-On Large Language Models)**。

無論你是剛踏入 LLM 領域的新手，還是想穩固底層知識、掌握實作細節的開發者，都歡迎跟著石虎的腳步，一起輕鬆交流、共同成長！☕️📚

## 📖 讀書會時程與大綱

活動固定於 **每週日晚間 20:00** 於線上進行。以下是各章節的資源與實作進度：

- [x] **Chapter 1: 基礎 (Introduction to Language Models)**
  - 日期：2026-04-05
  - 內容：LLM OS 概念、生成式 AI 歷史時間軸、Text input 與 Embeddings 基礎。
  - 實作：使用 Twinkle AI 專屬模型 `gemma-3-4B-T1-it` 進行 Formosa Vision 專案問答實作。
  - 資源：[簡報](ch1/Twinkle-llm-book-ch1.pdf) | [Notebook](ch1/Chapter_1_Introduction_to_Language_Models.ipynb) | [TwinkleAI 版 Notebook](ch1/Chapter_1_Introduction_to_Language_Models_twinkleai_version.ipynb)

- [x] **Chapter 2: Tokens 與 Embeddings (Tokens and Embeddings)**
  - 日期：2026-04-12
  - 內容：Tokenization 解析、Vocabulary 與 Special Tokens、Embeddings 向量魔法。
  - 實作：深入拆解 Tokenizer 的編碼與解碼過程，含八種模型 Tokenizer 視覺化比較、Word2Vec 音樂推薦實作。
  - 資源：[簡報](ch2/Twinkle-llm-book-ch2-slide.pdf) | [Notebook](ch2/Chapter_2_Tokens_and_Token_Embeddings.ipynb) | [TwinkleAI 版 Notebook](ch2/Chapter_2_Tokens_and_Token_Embeddings-twinkleai.ipynb) | [NotebookLM 筆記](ch2/NotebookLM-Language_Blueprints.pdf)

- [X] **Chapter 3: 看進語言模型的黑盒子 (Looking Inside Large Language Models)**
  - 日期：2026-04-19
  - 內容：打開語言模型的黑盒子，透視 Transformer 架構的內部運作機制。
    - **生成機制的秘密**：LLM 如何以自迴歸（autoregressive）方式逐 Token 生成，以及 KV Cache 最佳化技術如何大幅加速生成過程。
    - **Transformer 內部解密**：拆解 Transformer 區塊的兩大核心組件——負責記憶與推論的「前饋神經網路 (Feedforward Neural Network)」，以及整合上下文資訊的「注意力機制 (Attention Layer)」。
    - **注意力機制的進化**：深入認識 Queries、Keys、Values (QKV) 投影矩陣的產生與互動計算，以及近年架構改良——Grouped-Query Attention (GQA)、Flash Attention 與旋轉位置編碼 (RoPE)。
  - 實作：（待更新）
  - 資源：[簡報](ch3/Twinkle-llm-book-ch3.pdf)

- [X] **Chapter 4: 文本分類的全景圖 (Text Classification)**
  - 日期：2026-05-03
  - 內容：從傳統表示型模型到最新生成式模型，全面探索 LLM 如何精準判斷文字背後的意圖與情緒。
    - **表示型模型的分類雙重奏**：利用 BERT 家族等 Encoder-only 模型進行分類，涵蓋兩條路徑——針對特定目標微調的「任務特定模型 (Task-specific models)」，以及將文字轉為向量特徵再搭配邏輯迴歸 (Logistic Regression) 的「嵌入模型 (Embedding models)」輕量級方案。
    - **零樣本分類 (Zero-shot Classification)**：面對標記資料匱乏的實務困境，透過嵌入向量與標記描述之間的餘弦相似度 (Cosine Similarity)，在不訓練模型的情況下完成分類。
    - **生成式模型的分類新思維**：比較 Sequence-to-sequence 模型（如 Flan-T5）與閉源模型（如 ChatGPT）在分類上的表現，深入提示工程 (Prompt Engineering) 技巧與偏好對齊 (Preference Tuning) 概念。
    - **專業的評估指標**：解讀混淆矩陣 (Confusion Matrix)，掌握準確率 (Accuracy)、精確率 (Precision)、召回率 (Recall) 與 F1 分數的實務應用。
  - 實作：[TwinkleAI 版 Notebook](ch4/Chapter_4_Text_Classification_twinkle.ipynb)
  - 資源：[簡報](ch4/Twinkle-llm-book-ch4-slide.pdf) | [Notebook](ch4/Chapter%204%20-%20Text%20Classification.ipynb) | [TwinkleAI 版 Notebook](ch4/Chapter_4_Text_Classification_twinkle.ipynb)

- [x] **Chapter 5: 文本分群與主題建模 (Text Clustering and Topic Modeling)**
  - 日期：2026-05-10
  - 內容：跳脫需要大量標記資料的框架，運用語言模型在海量且未標記的文本中，自動找出潛藏的結構與主題。
    - **文本分群的經典三部曲**：嵌入文件 (Embed documents)、利用 UMAP 進行降維 (Dimensionality Reduction)、以 HDBSCAN 密度分群演算法自動找出語意相似群體並過濾離群值 (Outliers)。
    - **BERTopic：主題建模的樂高積木**：透過基於類別的 TF-IDF (c-TF-IDF) 萃取代表性關鍵字，並以高度模組化設計自由抽換嵌入模型、降維套件與分群演算法。
    - **重新排序：升級你的主題表示法**：以 KeyBERTInspired 利用餘弦相似度提取最具語意代表性的詞彙，並透過最大邊際相關性 (MMR) 消除關鍵字冗餘、確保多樣性。
    - **生成式 AI 神助攻**：結合 Flan-T5 或 GPT-3.5 與提示工程，將代表性文件與初始關鍵字餵給 LLM，自動生成精準且高可讀性的主題標籤。
  - 實作：[TwinkleAI 版 Notebook](Hands-On-Large-Language-Models/ch5/Chapter_5_Text_Clustering_and_Topic_Modeling-twinkle.ipynb)
  - 資源：[簡報](Hands-On-Large-Language-Models/ch5/Twinkle-llm-book-ch5.pdf) | [Notebook](Hands-On-Large-Language-Models/ch5/Chapter%205%20-%20Text%20Clustering%20and%20Topic%20Modeling.ipynb) | [TwinkleAI 版 Notebook](Hands-On-Large-Language-Models/ch5/Chapter_5_Text_Clustering_and_Topic_Modeling-twinkle.ipynb)

- [x] **Chapter 6: 提示工程 (Prompt Engineering)**
  - 日期：2026-05-17
  - 內容：直擊 LLM 核心，解密提示工程的關鍵技巧，從基礎指令到複雜邏輯推理，全面掌握引導模型產出高品質結果的訣竅。
    - **駕馭隨機與創造力**：精準微調 Temperature 與 Top_p 參數，完美平衡模型輸出的穩定性與創意。
    - **模組化 Prompt 框架**：靈活運用 Persona、Context、Format 與 Tone 四大元素，打造專業級指令。
    - **喚醒 System 2 邏輯推理**：掌握 In-Context Learning 範例引導，並運用 CoT（思維鏈）與 ToT（思維樹）帶領模型攻克複雜難題。
    - **輸出驗證與格式約束**：學習引導結構化輸出（JSON）及受限採樣（Constrained Sampling）的底層防呆機制，確保 Production 環境穩定運行。
  - 實作：[TwinkleAI 版 Notebook](Hands-On-Large-Language-Models/ch6/Chapter%206%20-%20Prompt%20Engineering-twinkle.ipynb)
  - 資源：[簡報](Hands-On-Large-Language-Models/ch6/Twinkle-llm-book-ch6.pdf) | [Notebook](Hands-On-Large-Language-Models/ch6/Chapter%206%20-%20Prompt%20Engineering.ipynb) | [TwinkleAI 版 Notebook](Hands-On-Large-Language-Models/ch6/Chapter%206%20-%20Prompt%20Engineering-twinkle.ipynb)

- [x] **Chapter 7: 進階文本生成技術與工具 (Advanced Text Generation Techniques and Tools)**
  - 日期：2026-05-24
  - 內容：超越提示工程，深入探索 LLM 應用開發的三大核心支柱，學習如何將語言模型整合進複雜的工作流程。
    - **載入與串接 LLM（Chains）**：掌握如何載入本地或雲端 LLM，並透過 Chain 架構將多個模型或處理步驟串接成自動化流水線，實現 Multiple Chains 的複雜邏輯組合。
    - **對話記憶管理（Memory）**：比較三種主流記憶策略——完整保留上下文的 ConversationBuffer、以滑動視窗控制記憶長度的 ConversationBufferMemoryWindow，以及以摘要壓縮歷史對話的 ConversationSummary，在效能與成本間取得平衡。
    - **自主行動的 Agent**：讓 LLM 自主決策、選用工具、執行多步驟任務，理解 Agent 的運作循環與工具呼叫機制，打造能與外部世界互動的智慧代理。
  - 資源：[簡報](Hands-On-Large-Language-Models/ch7/Twinkle-llm-book-ch7.0.0.pdf) | [Notebook](Hands-On-Large-Language-Models/ch7/Chapter%207%20-%20Advanced%20Text%20Generation%20Techniques%20and%20Tools.ipynb)

> 後續章節將每週持續更新...

## 🚀 Getting Started (如何開始實作)

如果你想跟著讀書會一起動手跑程式碼，請參考以下步驟：

1. **環境準備**：強烈建議使用具備 GPU 資源的環境（例如 Google Colab 的 T4 GPU）以獲得順暢的推論體驗。或者你也可以使用自己習慣的 Jupyter / marimo 環境。
2. **安裝套件**：確保已安裝最新版的 `transformers` 與 `accelerate`。

   ```bash
   pip install transformers>=4.50.0 accelerate>=0.31.0
   ```

3. **模型存取**：部分模型可能需要 Hugging Face 帳號授權，請確保你在環境中設定了 `HF_TOKEN`。

## 🌟 About Twinkle AI

**Twinkle AI** 是一個以繁體中文為核心的開源 AI 社群，專注於打造在地語言模型與資料集。我們致力於推動可公開使用的模型權重、訓練資料與實務經驗分享，串聯研究者、工程師與創作者，促進台灣在地 AI 生態的交流與共創。

Twinkle AI is a research community founded in late 2024, dedicated to enhancing Traditional Chinese language models with local cultural context. Starting with open-source LLaMA models, we are developing practical technologies tailored to the linguistic nuances of Taiwan. Our mission is to promote knowledge of large language model training through real-world practices. By embracing openness and collaboration, we aim to advance the local ecosystem in the field of generative AI.

## 🤝 貢獻與參與

這個讀書會與資源庫是社群共創的心血。如果你在閱讀或執行程式碼時發現任何問題，或是想補充更棒的繁體中文/在地化 LLM 範例，非常歡迎發起 **Pull Request** 或建立 **Issue** 一起討論！

## 參考資源

### Twinkle AI

- [Twinkle AI 官網](https://twinkleai.tw/)
- [Hugging Face](https://huggingface.co/twinkle-ai)
- [GitHub](https://github.com/ai-twinkle)
- [Discord](https://discord.com/servers/twinkle-ai-1310544431983759450)

### 書籍相關

- [Hands-On Large Language Models 官網](https://www.llm-book.com/)
- [Hands-On Large Language Models (Official Repo)](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
- [Jay Alammar's Blog](https://jalammar.github.io/)
- [Maarten Grootendorst's Newsletter](https://newsletter.maartengrootendorst.com/)

### 本讀書會

- [GitHub Repo](https://github.com/thliang01/TwinkleAI-LLM-Book-Club)
- [Maintainer: thliang01](https://github.com/thliang01)
