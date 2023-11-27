# This code is from https://huggingface.co/roberta-base-openai-detector#how-to-get-started-with-the-model

from transformers import pipeline
pipe = pipeline("text-classification", model="Polygraf/detector_gpt4_features")
MAX_TOKEN = 400


def gpt4_detect(dataset, START_INDEX, END_INDEX):
    i = 1
    result_list = []
    for text in dataset[START_INDEX:END_INDEX]:
        print('Number', i)
        result = pipe(text[0:min(len(text), MAX_TOKEN)])
        #result = pipe(text)
        result_list.append(result)
        i += 1
    return result_list