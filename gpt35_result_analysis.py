import pandas as pd
from generate_datasets import *
import json
import os

folder = 'result'
text_count = 1000

print('With sample size', text_count, ':')

# Obtaining the detection result of original text
results = []
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('gpt35_original')]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item[0]['label'])
false_detection_original = results[0:text_count].count('Real')
print('Number of texts mistaken as human-written in the original dataset =', false_detection_original)


# Obtaining the detection result of attacked text
results = []
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('gpt35_homoglyph')]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item[0]['label'])
false_detection_homoglyph = results[0:text_count].count('Real')
print('Number of texts mistaken as human-written in the attacked dataset =', false_detection_homoglyph)
