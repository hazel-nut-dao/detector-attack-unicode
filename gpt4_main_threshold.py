from generate_datasets import *
from detectors import gpt4
import os
import json
import pandas as pd

# homoglyphs used for conversion
homoglyph_file_name = 'data/homoglyphs.json'

# target dataframe for extracting text
data_file_name = 'data/deepfake_test.csv'
source_target = 'src'
text_target = 'text'
label_target = 'label'
folder = 'result'

# e.g START_INDEX=0, END_INDEX=2 -> process index 0, 1
START_INDEX = 0
END_INDEX = 1000
threshold = 0.1
text_count = 1000

# generate homoglyphs-replaced data from input data
original_dataset = generate_original_dataset(data_file_name, source_target, text_target)
homoglyph_dataset = homoglyph_conversion_threshold(original_dataset, homoglyph_file_name, threshold)

# pass to deepfake detector
output_deepfake_list = gpt4.gpt4_detect(homoglyph_dataset, START_INDEX, END_INDEX)
out_file_name = "result/gpt4_homoglyph_" + str(threshold) + "_" + str(START_INDEX) + "-" + str(END_INDEX-1) + ".json"
out_file = open(out_file_name, "w")
json.dump(output_deepfake_list, out_file)
out_file.close()

# evaluation
print('With sample size', text_count, 'and threshold', str(threshold),':')

# Obtaining the detection result of attacked text
results = []
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('gpt4_homoglyph_'+ str(threshold))]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item)
false_detection_homoglyph = results[0:text_count].count('human-written')
print('Number of texts mistaken as human-written in the attacked dataset =', false_detection_homoglyph)
