# This code is from https://radar.vizhub.ai/
from gradio_client import Client

client = Client("https://trustsafeai-radar-ai-text-detector.hf.space/")

def radar_detect(dataset, START_INDEX, END_INDEX):
    i = 1
    result_list = []
    for text in dataset[START_INDEX:END_INDEX]:
        print('Number', i)
        #detection
        result = client.predict(
        				text,	# str  in 'Text to be detected' Textbox component
        				api_name="/predict"
        )
        result_list.append(result)
        i += 1
    return result_list
