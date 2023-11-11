# the code is from https://sapling.ai/programming-language/ai-content-detector/python
# usage: result_list = return_sapling(dataset, trial_number, threshold = 0.7)

import requests

def sapling_detector(text):
    key = 'NRY6TPBJ7RPPQOXLLJMIO46JONA0T5B8'
    url = 'https://api.sapling.ai/api/v1/aidetect'
    data = {
        'key': key,
        'text': text,
    }

    try:
        resp = requests.post(url, json=data)
        resp_json = resp.json()
        if 200 < resp.status_code < 300:
            edits = resp_json['edits']
            print('Edits: ', edits)
        else:
            print('Status Error: ', resp_json)
            return
    except Exception as e:
        print('Exception Error: ', e)
        return
    return resp_json['score']

def return_sapling(dataset, trial_number, threshold = 0.7):
    score_list = []
    judge_list = []
    i = 1
    for paragraph in dataset[0:trial_number]:
        print('Original Progress:', i, 'of', trial_number) #original_dataset.size
        result = sapling.sapling_detector(paragraph)
        result_list_original.append(result)
        i += 1

    for score in score_list:
        if score > threshold:
            judge_list.append(True)
        else:
            judge_list.append(False)
    return judge_list
