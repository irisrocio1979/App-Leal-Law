import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util
import gradio as gr
import time

if torch.cuda.is_available():
    dev = "cuda"
else:
    dev = "cpu"
device = torch.device(dev)

# Modelo a usar
Mpnet2 = SentenceTransformer('all-mpnet-base-v2')
DistilRoBERTa = SentenceTransformer('hackathon-pln-es/paraphrase-spanish-distilroberta')