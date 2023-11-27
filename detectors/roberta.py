# This code is from https://huggingface.co/roberta-base-openai-detector#how-to-get-started-with-the-model

from transformers import pipeline
pipe = pipeline("text-classification", model="roberta-base-openai-detector")
MAX_TOKEN = 450

# output: [{'label': 'Real', 'score': 0.8036582469940186}]

def roberta_detect(dataset, START_INDEX, END_INDEX):
    i = 1
    result_list = []
    for text in dataset[START_INDEX:END_INDEX]:
        print('Number', i)
        result = pipe(text[0:min(len(text), MAX_TOKEN)])
        result_list.append(result)
        i += 1
    return result_list