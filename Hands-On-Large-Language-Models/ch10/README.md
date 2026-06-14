# Chapter 10: 建立文字嵌入模型 (Creating Text Embedding Models)

![TwinkleAI Reading Club Banner](../images/TwinkleAI-Reading-Club-ch10.png)

- **日期：** 2026-06-14
- **內容：** 深入探索文字嵌入模型的訓練與微調方法，涵蓋多種損失函數策略與無監督學習技術。

## 本章重點

### 建立嵌入模型（Creating an Embedding Model）

- **資料集（Data）**：使用 GLUE MNLI（Multi-Genre Natural Language Inference）資料集，包含蘊含（entailment）、中立（neutral）、矛盾（contradiction）三類標籤
- **基底模型（Model）**：以 `bert-base-uncased` 作為 SentenceTransformer 的基底，生成固定維度的句子嵌入向量
- **評估方式（Evaluation）**：使用 STS-B（Semantic Textual Similarity Benchmark）驗證集，透過餘弦相似度評估嵌入品質

### 損失函數（Loss Functions）

| 損失函數 | 說明 |
| --- | --- |
| **Softmax Loss** | 多分類設定下直接學習句子關係分類，需指定標籤數量 |
| **Cosine Similarity Loss** | 以餘弦相似度為目標，將蘊含對映射至高相似度、矛盾對映射至低相似度 |
| **Multiple Negatives Ranking Loss** | 以正例對比多個負例進行排序學習，適合只有正例的資料場景 |

### MTEB（大規模文字嵌入基準測試）

- **標準化評估**：透過 MTEB（Massive Text Embedding Benchmark）在多種下游任務（如分類、聚類、語意搜尋）上系統性地衡量嵌入模型表現
- **實作範例**：以 `Banking77Classification` 為評估任務，對訓練完成的嵌入模型進行測試

### 微調（Fine-tuning）

| 方法 | 說明 |
| --- | --- |
| **監督式微調（Supervised）** | 以有標記的 NLI 資料對預訓練嵌入模型（`all-MiniLM-L6-v2`）直接微調，快速適應目標任務 |
| **Augmented SBERT** | 利用 Cross-Encoder 擴充訓練資料，結合金標與銀標資料訓練 Bi-Encoder，突破標記資料不足的限制 |

**Augmented SBERT 五步驟流程：**

1. 以金標資料微調 Cross-Encoder（`bert-base-uncased`）
2. 生成新句子對候選集（silver dataset）
3. 以 Cross-Encoder 為新句子對打標（產生銀標資料）
4. 合併金標 + 銀標資料，以 Cosine Similarity Loss 訓練 Bi-Encoder（SBERT）
5. 對比僅使用金標資料的基線進行評估，驗證銀標資料的效益

### 無監督學習（Unsupervised Learning）

- **TSDAE（Transformer-based Denoising AutoEncoder）**：對輸入句子隨機刪除詞彙加入雜訊，訓練模型從受損句子重建原句，在完全無標記資料的情況下學習高品質句子表示
- **CLS Pooling**：搭配使用 CLS token pooling，以編碼器最終隱藏狀態作為句子向量表示

## 資源

- [簡報](Chapter%2010.pdf) | [Marimo Notebook](Chapter_10_Creating_Text_Embedding_Models.py) | [線上版 Notebook](https://molab.marimo.io/notebooks/nb_WArp2vmVRgN2RfwdQu9p1Z)
