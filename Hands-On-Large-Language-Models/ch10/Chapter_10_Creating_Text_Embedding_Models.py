# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "accelerate>=0.27.2",
#     "bitsandbytes>=0.43.0",
#     "datasets==3.0.1",
#     "huggingface-hub>=0.24",
#     "mteb==2.15.4",
#     "numpy==2.4.6",
#     "pandas==3.0.3",
#     "peft>=0.9.0",
#     "sentence-transformers==5.5.1",
#     "sentencepiece>=0.1.99",
#     "tqdm==4.68.2",
#     "transformers==5.12.0",
#     "trl>=0.7.11",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <h1>Chapter 10 - Creating Text Embedding Models</h1>
    <i>Exploring methods for both training and fine-tuning embedding models.</i>

    <a href="https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961"><img src="https://img.shields.io/badge/Buy%20the%20Book!-grey?logo=amazon"></a>
    <a href="https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/"><img src="https://img.shields.io/badge/O'Reilly-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzQiIGhlaWdodD0iMjciIHZpZXdCb3g9IjAgMCAzNCAyNyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTMiIGN5PSIxNCIgcj0iMTEiIHN0cm9rZT0iI0Q0MDEwMSIgc3Ryb2tlLXdpZHRoPSI0Ii8+CjxjaXJjbGUgY3g9IjMwLjUiIGN5PSIzLjUiIHI9IjMuNSIgZmlsbD0iI0Q0MDEwMSIvPgo8L3N2Zz4K"></a>
    <a href="https://github.com/HandsOnLLM/Hands-On-Large-Language-Models"><img src="https://img.shields.io/badge/GitHub%20Repository-black?logo=github"></a>
    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_WArp2vmVRgN2RfwdQu9p1Z)

    ---

    This notebook is for Chapter 10 of the [Hands-On Large Language Models](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961) book by [Jay Alammar](https://www.linkedin.com/in/jalammar) and [Maarten Grootendorst](https://www.linkedin.com/in/mgrootendorst/).

    ---

    <a href="https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961">
    <img src="https://raw.githubusercontent.com/HandsOnLLM/Hands-On-Large-Language-Models/main/images/book_cover.png" width="350"/></a>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### [OPTIONAL] - Installing Packages

    If you are viewing this notebook on Google Colab (or any other cloud vendor), you need to **uncomment and run** the following codeblock to install the dependencies for this chapter:

    ---

    💡 **NOTE**: We will want to use a GPU to run the examples in this notebook. In Google Colab, go to
    **Runtime > Change runtime type > Hardware accelerator > GPU > GPU type > T4**.

    ---
    """)
    return


@app.cell
def _():
    # %%capture
    # !pip install -q accelerate>=0.27.2 peft>=0.9.0 bitsandbytes>=0.43.0 transformers>=4.38.2 trl>=0.7.11 sentencepiece>=0.1.99
    # !pip install -q sentence-transformers>=3.0.0 mteb>=1.1.2 datasets>=2.18.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Creating an Embedding Model
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Data**
    """)
    return


@app.cell
def _():
    from datasets import load_dataset

    # Load MNLI dataset from GLUE
    # 0 = entailment, 1 = neutral, 2 = contradiction
    train_dataset = load_dataset("nyu-mll/glue", "mnli", split="train").select(range(50_000))
    train_dataset = train_dataset.remove_columns("idx")
    return load_dataset, train_dataset


@app.cell
def _(train_dataset):
    train_dataset[2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Model**
    """)
    return


@app.cell
def _():
    from sentence_transformers import SentenceTransformer

    # Use a base model
    embedding_model = SentenceTransformer('bert-base-uncased')
    return SentenceTransformer, embedding_model


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Loss Function**
    """)
    return


@app.cell
def _(embedding_model):
    from sentence_transformers import losses

    # Define the loss function. In soft-max loss, we will also need to explicitly set the number of labels.
    train_loss = losses.SoftmaxLoss(
        model=embedding_model,
        sentence_embedding_dimension=embedding_model.get_embedding_dimension(),
        num_labels=3
    )
    return losses, train_loss


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Evaluation
    """)
    return


@app.cell
def _(load_dataset):
    from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')# Create an embedding similarity evaluator for stsb
    evaluator = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return EmbeddingSimilarityEvaluator, evaluator


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Training**
    """)
    return


@app.cell
def _():
    from sentence_transformers.sentence_transformer.training_args import SentenceTransformerTrainingArguments

    # Define the training arguments
    args = SentenceTransformerTrainingArguments(
        output_dir="base_embedding_model",
        num_train_epochs=1,
        per_device_train_batch_size=32,
        per_device_eval_batch_size=32,
        warmup_steps=100,
        fp16=True,
        eval_steps=100,
        logging_steps=100,
    )
    return SentenceTransformerTrainingArguments, args


@app.cell
def _(args, embedding_model, evaluator, train_dataset, train_loss):
    from sentence_transformers.sentence_transformer.trainer import SentenceTransformerTrainer

    # Train embedding model
    trainer = SentenceTransformerTrainer(
        model=embedding_model,
        args=args,
        train_dataset=train_dataset,
        loss=train_loss,
        evaluator=evaluator
    )
    trainer.train()
    return (SentenceTransformerTrainer,)


@app.cell
def _(embedding_model, evaluator):
    # Evaluate our trained model
    evaluator(embedding_model)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # MTEB
    """)
    return


@app.cell
def _(embedding_model):
    import mteb

    # Choose evaluation task
    tasks = mteb.get_tasks(tasks=["Banking77Classification.v2"])
    evaluation = mteb.MTEB(tasks=tasks)

    # Calculate results
    results = evaluation.run(embedding_model)
    results
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up** - You will need to run the code below to partially empty the VRAM (GPU RAM). If that does not work, it is advised to restart the notebook instead. You can check the resources on the right-hand side (if you are using Google Colab) to check whether the used VRAM is indeed low. You can also run `!nivia-smi` to check current usage.
    """)
    return


@app.cell
def _():
    # # Empty and delete trainer/model
    # trainer.accelerator.clear()
    # del trainer, embedding_model

    # # Garbage collection and empty cache
    # import gc
    # import torch

    # gc.collect()
    # torch.cuda.empty_cache()
    return


@app.cell
def _():
    import gc
    import torch

    gc.collect()
    torch.cuda.empty_cache()
    return gc, torch


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Loss Fuctions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up**
    * `Restart` the notebook in order to clean-up memory if you move on to the next training example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cosine Similarity Loss
    """)
    return


@app.cell
def _(load_dataset):
    from datasets import Dataset
    train_dataset_1 = load_dataset('nyu-mll/glue', 'mnli', split='train').select(range(50000))
    train_dataset_1 = train_dataset_1.remove_columns('idx')
    _mapping = {2: 0, 1: 0, 0: 1}
    train_dataset_1 = Dataset.from_dict({'sentence1': train_dataset_1['premise'], 'sentence2': train_dataset_1['hypothesis'], 'label': [float(_mapping[label]) for label in train_dataset_1['label']]})
    return Dataset, train_dataset_1


@app.cell
def _(EmbeddingSimilarityEvaluator, load_dataset):
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')
    evaluator_1 = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return (evaluator_1,)


@app.cell
def _(
    SentenceTransformer,
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    evaluator_1,
    losses,
    train_dataset_1,
):
    embedding_model_1 = SentenceTransformer('bert-base-uncased')
    train_loss_1 = losses.CosineSimilarityLoss(model=embedding_model_1)
    args_1 = SentenceTransformerTrainingArguments(output_dir='cosineloss_embedding_model', num_train_epochs=1, per_device_train_batch_size=32, per_device_eval_batch_size=32, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_1 = SentenceTransformerTrainer(model=embedding_model_1, args=args_1, train_dataset=train_dataset_1, loss=train_loss_1, evaluator=evaluator_1)
    # Define model
    # Loss function
    # Define the training arguments
    # Train model
    trainer_1.train()
    return (embedding_model_1,)


@app.cell
def _(embedding_model_1, evaluator_1):
    # Evaluate our trained model
    evaluator_1(embedding_model_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up**
    * `Restart` the notebook in order to clean-up memory if you move on to the next training example.
    """)
    return


@app.cell
def _(gc, torch):
    gc.collect()
    torch.cuda.empty_cache()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Multiple Negatives Ranking Loss
    """)
    return


@app.cell
def _(Dataset, load_dataset):
    import random
    from tqdm import tqdm
    _mnli = load_dataset('nyu-mll/glue', 'mnli', split='train').select(range(50000))
    _mnli = _mnli.remove_columns('idx')
    _mnli = _mnli.filter(lambda x: True if x['label'] == 0 else False)
    train_dataset_2 = {'anchor': [], 'positive': [], 'negative': []}
    soft_negatives = list(_mnli['hypothesis'])
    random.shuffle(soft_negatives)
    for row, soft_negative in tqdm(zip(_mnli, soft_negatives)):
        train_dataset_2['anchor'].append(row['premise'])
        train_dataset_2['positive'].append(row['hypothesis'])
        train_dataset_2['negative'].append(soft_negative)
    train_dataset_2 = Dataset.from_dict(train_dataset_2)
    len(train_dataset_2)
    return tqdm, train_dataset_2


@app.cell
def _(EmbeddingSimilarityEvaluator, load_dataset):
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')
    evaluator_2 = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return (evaluator_2,)


@app.cell
def _(
    SentenceTransformer,
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    evaluator_2,
    losses,
    train_dataset_2,
):
    embedding_model_2 = SentenceTransformer('bert-base-uncased')
    train_loss_2 = losses.MultipleNegativesRankingLoss(model=embedding_model_2)
    args_2 = SentenceTransformerTrainingArguments(output_dir='mnrloss_embedding_model', num_train_epochs=1, per_device_train_batch_size=32, per_device_eval_batch_size=32, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_2 = SentenceTransformerTrainer(model=embedding_model_2, args=args_2, train_dataset=train_dataset_2, loss=train_loss_2, evaluator=evaluator_2)
    # Define model
    # Loss function
    # Define the training arguments
    # Train model
    trainer_2.train()
    return (embedding_model_2,)


@app.cell
def _(embedding_model_2, evaluator_2):
    # Evaluate our trained model
    evaluator_2(embedding_model_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Fine-tuning**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up**
    * `Restart` the notebook in order to clean-up memory if you move on to the next training example.
    """)
    return


@app.cell
def _(gc, torch):
    gc.collect()
    torch.cuda.empty_cache()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Supervised**
    """)
    return


@app.cell
def _(EmbeddingSimilarityEvaluator, load_dataset):
    train_dataset_3 = load_dataset('nyu-mll/glue', 'mnli', split='train').select(range(50000))
    train_dataset_3 = train_dataset_3.remove_columns('idx')
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')
    evaluator_3 = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return evaluator_3, train_dataset_3


@app.cell
def _(
    SentenceTransformer,
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    evaluator_3,
    losses,
    train_dataset_3,
):
    embedding_model_3 = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    train_loss_3 = losses.MultipleNegativesRankingLoss(model=embedding_model_3)
    args_3 = SentenceTransformerTrainingArguments(output_dir='finetuned_embedding_model', num_train_epochs=1, per_device_train_batch_size=32, per_device_eval_batch_size=32, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_3 = SentenceTransformerTrainer(model=embedding_model_3, args=args_3, train_dataset=train_dataset_3, loss=train_loss_3, evaluator=evaluator_3)
    # Define model
    # Loss function
    # Define the training arguments
    # Train model
    trainer_3.train()
    return (embedding_model_3,)


@app.cell
def _(embedding_model_3, evaluator_3):
    # Evaluate our trained model
    evaluator_3(embedding_model_3)
    return


@app.cell
def _(SentenceTransformer, evaluator_3):
    # Evaluate the pre-trained model
    original_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    evaluator_3(original_model)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up**
    * `Restart` the notebook in order to clean-up memory if you move on to the next training example.
    """)
    return


@app.cell
def _(gc, torch):
    gc.collect()
    torch.cuda.empty_cache()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Augmented SBERT**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 1:** Fine-tune a cross-encoder
    """)
    return


@app.cell
def _(load_dataset, tqdm):
    import pandas as pd
    from sentence_transformers import InputExample
    from sentence_transformers.datasets import NoDuplicatesDataLoader
    dataset = load_dataset('nyu-mll/glue', 'mnli', split='train').select(range(10000))
    _mapping = {2: 0, 1: 0, 0: 1}
    gold_examples = [InputExample(texts=[row['premise'], row['hypothesis']], label=_mapping[row['label']]) for row in tqdm(dataset)]
    gold_dataloader = NoDuplicatesDataLoader(gold_examples, batch_size=32)
    gold = pd.DataFrame({'sentence1': dataset['premise'], 'sentence2': dataset['hypothesis'], 'label': [_mapping[label] for label in dataset['label']]})
    return gold, gold_dataloader, pd


@app.cell
def _(gold_dataloader):
    from sentence_transformers.cross_encoder import CrossEncoder

    # Train a cross-encoder on the gold dataset
    cross_encoder = CrossEncoder('bert-base-uncased', num_labels=2)
    cross_encoder.fit(
        train_dataloader=gold_dataloader,
        epochs=1,
        show_progress_bar=True,
        warmup_steps=100,
        use_amp=False
    )
    return (cross_encoder,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 2:** Create new sentence pairs
    """)
    return


@app.cell
def _(load_dataset):
    # Prepare the silver dataset by predicting labels with the cross-encoder
    silver = load_dataset("nyu-mll/glue", "mnli", split="train").select(range(10_000, 50_000))
    pairs = list(zip(silver['premise'], silver['hypothesis']))
    return pairs, silver


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 3:** Label new sentence pairs with the fine-tuned cross-encoder (silver dataset)
    """)
    return


@app.cell
def _(cross_encoder, pairs, pd, silver):
    import numpy as np
    output = cross_encoder.predict(pairs, apply_softmax=True, show_progress_bar=True)
    # Label the sentence pairs using our fine-tuned cross-encoder
    silver_1 = pd.DataFrame({'sentence1': silver['premise'], 'sentence2': silver['hypothesis'], 'label': np.argmax(output, axis=1)})
    return (silver_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 4:** Train a bi-encoder (SBERT) on the extended dataset (gold + silver dataset)
    """)
    return


@app.cell
def _(Dataset, gold, pd, silver_1):
    _data = pd.concat([gold, silver_1], ignore_index=True, axis=0)
    _data = _data.drop_duplicates(subset=['sentence1', 'sentence2'], keep='first')
    train_dataset_4 = Dataset.from_pandas(_data, preserve_index=False)
    return (train_dataset_4,)


@app.cell
def _(EmbeddingSimilarityEvaluator, load_dataset):
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')
    evaluator_4 = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return (evaluator_4,)


@app.cell
def _(
    SentenceTransformer,
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    evaluator_4,
    losses,
    train_dataset_4,
):
    embedding_model_4 = SentenceTransformer('bert-base-uncased')
    train_loss_4 = losses.CosineSimilarityLoss(model=embedding_model_4)
    args_4 = SentenceTransformerTrainingArguments(output_dir='augmented_embedding_model', num_train_epochs=1, per_device_train_batch_size=32, per_device_eval_batch_size=32, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_4 = SentenceTransformerTrainer(model=embedding_model_4, args=args_4, train_dataset=train_dataset_4, loss=train_loss_4, evaluator=evaluator_4)
    # Define model
    # Loss function
    # Define the training arguments
    # Train model
    trainer_4.train()
    return embedding_model_4, trainer_4


@app.cell
def _(embedding_model_4, evaluator_4):
    # Evaluate our trained model
    evaluator_4(embedding_model_4)
    return


@app.cell
def _(trainer_4):
    trainer_4.accelerator.clear()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 5**: Evaluate without silver dataset
    """)
    return


@app.cell
def _(
    Dataset,
    SentenceTransformer,
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    evaluator_4,
    gold,
    losses,
    pd,
):
    _data = pd.concat([gold], ignore_index=True, axis=0)
    _data = _data.drop_duplicates(subset=['sentence1', 'sentence2'], keep='first')
    train_dataset_5 = Dataset.from_pandas(_data, preserve_index=False)
    embedding_model_5 = SentenceTransformer('bert-base-uncased')
    train_loss_5 = losses.CosineSimilarityLoss(model=embedding_model_5)
    args_5 = SentenceTransformerTrainingArguments(output_dir='gold_only_embedding_model', num_train_epochs=1, per_device_train_batch_size=32, per_device_eval_batch_size=32, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_5 = SentenceTransformerTrainer(model=embedding_model_5, args=args_5, train_dataset=train_dataset_5, loss=train_loss_5, evaluator=evaluator_4)
    trainer_5.train()
    return (embedding_model_5,)


@app.cell
def _(embedding_model_5, evaluator_4):
    # Evaluate our trained model
    evaluator_4(embedding_model_5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Compared to using both the silver and gold datasets, using only the gold dataset reduces the performance of the model!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ **VRAM Clean-up**
    * `Restart` the notebook in order to clean-up memory if you move on to the next training example.
    """)
    return


@app.cell
def _(gc, torch):
    gc.collect()
    torch.cuda.empty_cache()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Unsupervised Learning**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tranformer-based Denoising AutoEncoder (TSDAE)
    """)
    return


@app.cell
def _():
    # Download additional tokenizer
    import nltk
    nltk.download('punkt_tab')
    return


@app.cell
def _(Dataset, load_dataset, tqdm):
    from sentence_transformers.datasets import DenoisingAutoEncoderDataset
    _mnli = load_dataset('nyu-mll/glue', 'mnli', split='train').select(range(25000))
    flat_sentences = list(_mnli['premise']) + list(_mnli['hypothesis'])
    damaged_data = DenoisingAutoEncoderDataset(list(set(flat_sentences)))
    train_dataset_6 = {'damaged_sentence': [], 'original_sentence': []}
    for _data in tqdm(damaged_data):
        train_dataset_6['damaged_sentence'].append(_data.texts[0])
        train_dataset_6['original_sentence'].append(_data.texts[1])
    train_dataset_6 = Dataset.from_dict(train_dataset_6)
    return (train_dataset_6,)


@app.cell
def _(train_dataset_6):
    train_dataset_6[0]
    return


@app.cell
def _():
    # # Choose a different deletion ratio
    # flat_sentences = list(set(flat_sentences))
    # damaged_data = DenoisingAutoEncoderDataset(
    #     flat_sentences,
    #     noise_fn=lambda s: DenoisingAutoEncoderDataset.delete(s, del_ratio=0.6)
    # )
    return


@app.cell
def _(EmbeddingSimilarityEvaluator, load_dataset):
    _val_sts = load_dataset('nyu-mll/glue', 'stsb', split='validation')
    evaluator_5 = EmbeddingSimilarityEvaluator(sentences1=_val_sts['sentence1'], sentences2=_val_sts['sentence2'], scores=[score / 5 for score in _val_sts['label']], main_similarity='cosine')
    return (evaluator_5,)


@app.cell
def _(SentenceTransformer):
    from sentence_transformers import models
    word_embedding_model = models.Transformer('bert-base-uncased')
    # Create your embedding model
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(), 'cls')
    embedding_model_6 = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    return (embedding_model_6,)


@app.cell
def _(embedding_model_6, losses):
    train_loss_6 = losses.DenoisingAutoEncoderLoss(
        embedding_model_6,
        decoder_name_or_path='bert-base-uncased',
        tie_encoder_decoder=False
    )
    # Device placement handled automatically by trainer
    return (train_loss_6,)


@app.cell
def _(
    SentenceTransformerTrainer,
    SentenceTransformerTrainingArguments,
    embedding_model_6,
    evaluator_5,
    train_dataset_6,
    train_loss_6,
):
    args_6 = SentenceTransformerTrainingArguments(output_dir='tsdae_embedding_model', num_train_epochs=1, per_device_train_batch_size=16, per_device_eval_batch_size=16, warmup_steps=100, fp16=True, eval_steps=100, logging_steps=100)
    trainer_6 = SentenceTransformerTrainer(model=embedding_model_6, args=args_6, train_dataset=train_dataset_6, loss=train_loss_6, evaluator=evaluator_5)
    # Define the training arguments
    # Train model
    trainer_6.train()
    return


@app.cell
def _(embedding_model_6, evaluator_5):
    # Evaluate our trained model
    evaluator_5(embedding_model_6)
    return


@app.cell
def _(gc, torch):
    gc.collect()
    torch.cuda.empty_cache()
    return


if __name__ == "__main__":
    app.run()
