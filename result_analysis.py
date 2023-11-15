import pandas as pd
from generate_datasets import *
#from glob import glob
import json
import os

data_file_name = 'data/deepfake_test.csv'
source_target = 'src'
label_target = 'label'
folder = 'result'
text_count = 200

# Obtaining the detection result stated in the paper
'''
All instances are stored as rows in a csv format,
with each row consiting of 3 columns:
Text, Label (0 for machine-generated and 1 for human-written) and
Index (indexes in the original data source, used restore alignment after filtering).
'''
original_output = generate_original_dataset(data_file_name, source_target, label_target)
false_detection_original = sum(original_output.head(text_count))
print('Number of texts mistaken as human-written in the original study =', false_detection_original)

# Obtaining the detection result of attacked text
results = []
#result_file_list =  [f for f in glob("result/*.json")]
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('deepfake_original')]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item)
false_detection_homoglyph = results[0:text_count].count('human-written')
print('Number of texts mistaken as human-written in the original dataset =', false_detection_homoglyph)


# Obtaining the detection result of attacked text
results = []
#result_file_list =  [f for f in glob("result/*.json")]
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('deepfake_homoglyph')]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item)
false_detection_homoglyph = results[0:text_count].count('human-written')
print('Number of texts mistaken as human-written in the attacked dataset =', false_detection_homoglyph)
