from generate_datasets import *
from detectors import deepfake
import os

# homoglyphs used for conversion
homoglyph_file_name = 'data/homoglyphs.json'

# target dataframe
data_file_name = 'data/deepfake_test.csv'
source_target = 'src'
text_target = 'text'

# e.g START_INDEX=0, END_INDEX=2 -> process index 0, 1
START_INDEX = 100
END_INDEX = 150

# generate homoglyphs-replaced data from input data
original_dataset = generate_original_dataset(data_file_name, source_target, text_target)
#homoglyph_dataset = homoglyph_conversion(original_dataset, homoglyph_file_name)

# pass to deepfake detector
output_deepfake_list = deepfake.deepfake_detect(original_dataset, START_INDEX, END_INDEX)
out_file_name = "result/deepfake_original_" + str(START_INDEX) + "-" + str(END_INDEX-1) + ".json"
out_file = open(out_file_name, "w")
json.dump(output_deepfake_list, out_file)
out_file.close()
