from generate_datasets import *
from detectors import sapling
import os
from time import sleep

data_file_name = 'data/deepfake_test.csv'
label_target = 'src'
text_target = 'text'
homoglyph_file_name = 'data/homoglyphs.json'
trial_number = 1

def clear():
    os.system('cls')

# generate homoglyphs-replaced data from input data
original_dataset = generate_original_dataset(data_file_name, label_target, text_target)
homoglyph_dataset = homoglyph_conversion(original_dataset, homoglyph_file_name)

# pass to detectors
