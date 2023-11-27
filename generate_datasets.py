import json
import pandas as pd
from random import random

# finding the data labelled as machine-generated
def if_machine(name):
    if name.find('machine') != -1:
        return True
    else:
        return False

# extract original dataset
def generate_original_dataset(file_name, origin_column, text_column):
    raw_dataset = pd.read_csv(file_name)
    names_list = filter(if_machine, list(raw_dataset[origin_column].unique()))
    middle_df = raw_dataset[raw_dataset[origin_column].isin(names_list)]
    result_df = middle_df[text_column].copy()
    return result_df

# converting input data string to homoglyphs
def homoglyph_conversion(dataset, homo_file_name):
    with open(homo_file_name) as homo:
        homoglyph_dict = json.load(homo)
    homoglyph_map = str.maketrans(homoglyph_dict)

    converted_text_list = [x.translate(homoglyph_map) for x in list(dataset)]
    result_df = pd.Series(converted_text_list, name='homoglyph_text')
    return result_df

def homoglyph_conversion_threshold(dataset, homo_file_name, threshold):
    with open(homo_file_name) as homo:
        homoglyph_dict = json.load(homo)
    homoglyph_map = str.maketrans(homoglyph_dict)
    converted_text_list = []
    for text in list(dataset):
        text_h = text.translate(homoglyph_map)
        result_text = str()
        for i in range(len(text)):
            rand = random()
            if rand <= threshold:
                result_text = result_text + text_h[i]
            else:
                result_text = result_text + text[i]
        converted_text_list.append(result_text)
    result_df = pd.Series(converted_text_list, name='homoglyph_text')
    return result_df