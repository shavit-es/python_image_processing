from PIL import Image
import os
import numpy as np
from typing import OrderedDict
import json
import os

path_dir = 'C:/Users/Admin/Desktop/LHH/code/jsontotxt/Train/Defective/'
 
file_list = os.listdir(path_dir)

for file_name in file_list:
    if file_name[-5:]=='.json':
        with open(path_dir + file_name, 'r') as f:
            json_data = json.load(f)
            file = open(path_dir+"/jsontotxt/"+file_name[:-5] + ".txt", "w")
            for ele in json_data['shapes']:
                if ele['label'] == "normal":
                    label_info = 0
                elif ele['label'] == "abnormal":
                    label_info = 1
                image_height=json_data["imageHeight"]
                image_width=json_data["imageWidth"]
                x1 = ele['points'][0][0] 
                y1 = ele['points'][0][1]
                x2 = ele['points'][1][0]
                y2 = ele['points'][1][1]

                if not os.path.exists(path_dir+"jsontotxt/"):
                    os.makedirs(path_dir+"jsontotxt/")
                
                centerx = ((x2+x1)/2)/image_width
                centery = ((y2+y1)/2)/image_height
                width = (x2-x1)/image_width
                height = (y2-y1)/image_height
                write_str= str(label_info) + " " + str(centerx) +" "+  str(centery) + " "+ str(width) + " "+ str(height) + "\n"
                file.write(write_str)
            print(file_name, "done")
            file.close()