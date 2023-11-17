from generate_datasets import *
from detectors import radar
import os
import json

# homoglyphs used for conversion
homoglyph_file_name = 'data/homoglyphs.json'

# target dataframe for extracting text
data_file_name = 'data/deepfake_test.csv'
source_target = 'src'
text_target = 'text'

# e.g START_INDEX=0, END_INDEX=2 -> process index 0, 1
START_INDEX = 0
END_INDEX = 1

# generate homoglyphs-replaced data from input data
original_dataset = generate_original_dataset(data_file_name, source_target, text_target)
homoglyph_dataset = homoglyph_conversion(original_dataset, homoglyph_file_name)

# pass to RADAR detector
print(radar.radar_detect(original_dataset, START_INDEX, END_INDEX))
