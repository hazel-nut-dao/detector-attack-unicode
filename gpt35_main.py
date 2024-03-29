from generate_datasets import *
from detectors import gpt35
import os
import json

# homoglyphs used for conversion
homoglyph_file_name = '/mnt/Data/chen19/detector-attack-unicode/data/homoglyphs.json'

# target dataframe for extracting text
data_file_name = '/mnt/Data/chen19/detector-attack-unicode/data/deepfake_test.csv'
source_target = 'src'
text_target = 'text'

# e.g START_INDEX=0, END_INDEX=2 -> process index 0, 1
START_INDEX = 0
END_INDEX = 10

# generate homoglyphs-replaced data from input data
original_dataset = generate_original_dataset(data_file_name, source_target, text_target)
homoglyph_dataset = homoglyph_conversion(original_dataset, homoglyph_file_name)

# pass to RADAR detector
output_gpt35_list = gpt35.gpt35_detect(homoglyph_dataset, START_INDEX, END_INDEX)
out_file_name = "result/gpt35_homoglyph_" + str(START_INDEX) + "-" + str(END_INDEX-1) + ".json"
out_file = open(out_file_name, "w")
json.dump(output_gpt35_list, out_file)
out_file.close()
