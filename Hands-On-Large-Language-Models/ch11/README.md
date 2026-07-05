# Chapter 11: 微調表示型模型 (Fine-Tuning Representation Models)

![TwinkleAI Reading Club Banner](../images/TwinkleAI-Reading-Club-ch11.png)

- **日期：** 2026-06-28
- **內容：** 深入探索如何微調 BERT 系列的表示型模型，涵蓋監督式分類、層凍結策略、少樣本學習、遮罩語言建模與命名實體辨識等任務。

## 本章重點

### 監督式分類（Supervised Classification）

- **資料集**：使用 `rotten_tomatoes` 情感分類資料集，以 `bert-base-cased` 作為基底模型搭配 HuggingFace `Trainer` 進行微調
- **層凍結策略**：比較「凍結全部主幹、僅訓練分類頭」、「凍結前 9 層編碼器區塊」與「全參數微調」三種策略對 F1 分數的影響，觀察可訓練層數與效能的權衡關係

### 少樣本分類（Few-shot Classification）

- **SetFit**：以 `sentence-transformers/all-mpnet-base-v2` 為基底，每類別僅取樣 16 筆資料，透過對比學習（Contrastive Learning）生成句子對並訓練分類頭，大幅降低對標記資料的需求

### 遮罩語言建模（Masked Language Modeling, MLM）

- **持續預訓練**：以 `DataCollatorForLanguageModeling` 對輸入序列進行 15% 機率的 token 遮罩，讓 `bert-base-cased` 在目標領域資料上持續進行 MLM 訓練
- **效果驗證**：透過 `fill-mask` pipeline 比較原始模型與領域適應後模型的填空預測結果

### 命名實體辨識（Named Entity Recognition, NER）

- **資料集與標籤對齊**：使用 CoNLL-2003 資料集，透過 `word_ids` 將 subword token 對齊回原始詞彙標籤，並以 `AutoModelForTokenClassification` 進行 token 分類微調
- **評估指標**：以 `seqeval` 計算序列標記任務的 F1 分數

## 資源

- [簡報](TwinkleAI%20Ch11%20Deck.pdf) | [Notebook](Chapter%2011%20-%20Fine-Tuning%20BERT.ipynb)
