import os
import json
import pandas as pd
folder = 'result'


results = []
result_file_list = [filename for filename in os.listdir(folder) if filename.startswith('deepfake_homoglyph')]
for file in result_file_list:
    in_file = open('result/'+file, "r")
    sublist = json.load(in_file)
    in_file.close()
    for item in sublist:
        results.append(item)
out_file_name = "result/deepfake_homoglyph_" + str(0) + "-" + str(len(results)-1) + ".json"
out_file = open(out_file_name, "w")
json.dump(results, out_file)
out_file.close()
