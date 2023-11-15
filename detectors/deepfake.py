# This code is from https://github.com/yafuly/DeepfakeTextDetect

import torch
import os
from transformers import AutoModelForSequenceClassification,AutoTokenizer
from .DeepfakeTextDetect import deployment

# init
device = 'cpu' # use 'cuda:0' if GPU is available
model_dir = "nealcly/detection-longformer"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir).to(device)

def deepfake_detect(dataset, START_INDEX, END_INDEX):
    i = 1
    result_list = []
    for text in dataset[START_INDEX:END_INDEX]:
        print('Number', i)
        # preprocess
        preprocessed_text = deployment.preprocess(text)
        # detection
        result = deployment.detect(preprocessed_text,tokenizer,model,device)
        result_list.append(result)
        i += 1
    return result_list
